"""Brain CLI — ingest a source, then query your second brain.

    python -m brain.cli ingest --adapter mem --source ./sample_mem_export
    python -m brain.cli query "what were the MOA consignment terms?"
    python -m brain.cli query "why did we pick the IKEA enclosure?" --layer reasoning
    python -m brain.cli stats

Embedder defaults to `fake` (offline, deps-free). For real recall:
    --embedder local    (private, on-device; needs sentence-transformers)
    --embedder openai    (needs OPENAI_API_KEY)
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from .adapters.calendar_adapter import CalendarAdapter
from .adapters.chatgpt_adapter import ChatGPTAdapter
from .adapters.claude_adapter import ClaudeAdapter
from .adapters.claude_code_adapter import ClaudeCodeAdapter
from .adapters.contacts_adapter import ContactsAdapter
from .adapters.entity_base import ingest_entities
from .adapters.fieldy_adapter import FieldyAdapter
from .adapters.filesystem_adapter import FilesystemAdapter
from .adapters.mem_adapter import MemAdapter
# Live Google adapters import lazily inside the CLI helpers below so
# `google-api-python-client` is an optional dep.
from .core.checkpoint import CheckpointStore
from .core.dossier import dossier
from .core.embed import get_embedder
from .core.entities import EntityStore
from .core.index import BrainIndex
from .core.ledger import IngestLedger
from .core.pipeline import IngestStats, ingest
from .core.resolve import Status, resolve


def _build_adapter(name: str, source: str, entdb: str, exclude: list[str] | None = None):
    if name == "mem":
        return MemAdapter(source)
    if name == "fieldy":
        return FieldyAdapter(checkpoint_db=entdb)
    if name == "filesystem":
        return FilesystemAdapter(source, checkpoint_db=entdb, exclude_patterns=exclude)
    if name == "claude":
        return ClaudeAdapter(source)
    if name == "claude-code":
        return ClaudeCodeAdapter(source, checkpoint_db=entdb, exclude=exclude)
    if name == "chatgpt":
        return ChatGPTAdapter(source)
    if name == "drive":
        from .adapters.drive_adapter import DriveAdapter
        return DriveAdapter(checkpoint_db=entdb, folder_id=source or None)
    if name == "granola":
        from .adapters.granola_adapter import GranolaAdapter
        return GranolaAdapter(source, checkpoint_db=entdb)
    if name == "gmail":
        from .adapters.gmail_adapter import GmailAdapter
        return GmailAdapter(checkpoint_db=entdb, entdb=entdb)
    if name == "imap":
        from .adapters.imap_adapter import IMAPAdapter
        return IMAPAdapter(checkpoint_db=entdb, entdb=entdb, folder=source or "INBOX")
    if name == "imessage":
        from .adapters.imessage_adapter import IMessageAdapter
        return IMessageAdapter(
            db_path=source or None, checkpoint_db=entdb,
        )
    if name == "icloud-notes":
        from .adapters.icloud_notes_adapter import ICloudNotesAdapter
        return ICloudNotesAdapter(source=source or "", checkpoint_db=entdb)
    if name == "github":
        from .adapters.github_adapter import GitHubAdapter
        return GitHubAdapter(checkpoint_db=entdb)
    if name == "m365":
        from .adapters.m365_adapter import M365Adapter
        return M365Adapter(source or "mail", checkpoint_db=entdb, entdb=entdb)
    if name == "slack":
        from .adapters.slack_adapter import SlackAdapter
        return SlackAdapter(checkpoint_db=entdb)
    if name == "inbox":
        from .adapters.inbox_adapter import InboxAdapter
        return InboxAdapter(source or os.environ.get("BRAIN_INBOX_DIR", ""))
    if name == "agentmail":
        from .adapters.agentmail_adapter import AgentMailAdapter
        return AgentMailAdapter(source, checkpoint_db=entdb)
    raise ValueError(f"unknown adapter {name!r}")


ADAPTERS = ("mem", "fieldy", "filesystem", "claude", "claude-code", "chatgpt",
            "drive", "granola", "gmail", "imap", "imessage", "icloud-notes",
            "github", "m365", "slack", "inbox", "agentmail")
ENTITY_ADAPTERS = {"contacts": ContactsAdapter, "calendar": CalendarAdapter}
LIVE_ENTITY_ADAPTERS = ("gcal-live", "people-live")


def _build_live_entity_adapter(kind: str, source: str, entdb: str):
    if kind == "gcal-live":
        from .adapters.gcal_live_adapter import GoogleCalendarLiveAdapter
        return GoogleCalendarLiveAdapter(
            calendar_id=source or "primary",
            checkpoint_db=entdb,
        )
    if kind == "people-live":
        from .adapters.people_live_adapter import GooglePeopleLiveAdapter
        return GooglePeopleLiveAdapter(checkpoint_db=entdb)
    raise ValueError(f"unknown live entity adapter {kind!r}")


# Memoized per (db, embedder): one-shot commands see no difference, and the
# watch daemon avoids reloading the sentence-transformers model every cycle.
_INDEX_CACHE: dict[tuple[str, str], BrainIndex] = {}


def _index(args: argparse.Namespace) -> BrainIndex:
    key = (args.db, args.embedder)
    idx = _INDEX_CACHE.get(key)
    if idx is None:
        idx = _INDEX_CACHE[key] = BrainIndex(args.db, get_embedder(args.embedder))
    return idx


def _snapshot_checkpoints(entdb: str, adapter_name: str) -> dict[tuple[str, str], str]:
    return {
        (r["adapter"], r["key"]): r["value"]
        for r in CheckpointStore(entdb).all()
        if r["adapter"] == adapter_name
    }


def _restore_checkpoints(
    entdb: str, adapter_name: str, before: dict[tuple[str, str], str]
) -> None:
    """Undo any watermark movement a dry-run caused: some adapters advance
    checkpoints inside fetch(), so we snapshot before and roll back after.
    Scoped to the adapter under test — the checkpoints table is shared by
    every adapter in this entdb, and a global restore would revert (or
    delete) tokens that a CONCURRENT real ingest just wrote."""
    cp = CheckpointStore(entdb)
    for r in cp.all():
        if r["adapter"] != adapter_name:
            continue
        k = (r["adapter"], r["key"])
        if k not in before:
            cp.clear(r["adapter"], r["key"])
        elif r["value"] != before[k]:
            cp.set(r["adapter"], before[k], key=r["key"])
    for (adp, key), value in before.items():
        if cp.get(adp, key) is None:
            cp.set(adp, value, key=key)


def _finish_ledger(
    ledger: IngestLedger,
    run_id: str,
    status: str,
    stats: IngestStats,
    adapter,
    extra_meta: dict | None = None,
) -> None:
    skip_report = getattr(adapter, "skip_report", None) or {}
    skipped = sum(entry["count"] for entry in skip_report.values())
    meta = dict(extra_meta or {})
    if skip_report:
        meta["skip_report"] = skip_report
    ledger.finish(
        run_id, status,
        docs=stats.docs, chunks=stats.chunks, errors=stats.errors, skipped=skipped,
        llm_classified=stats.llm_classified,
        heuristic_classified=stats.heuristic_classified,
        error_samples=stats.error_samples, meta=meta,
    )


def _print_dry_run_report(adapter_name: str, src: str, stats: IngestStats,
                          skip_report: dict | None) -> None:
    print(f"DRY RUN — {adapter_name} ({src}) — nothing written")
    print(f"  docs seen:          {stats.docs}")
    print(f"  chunks (would add): {stats.chunks}")
    print(f"  errors:             {stats.errors}")
    print(f"  classified:         llm={stats.llm_classified} "
          f"heuristic={stats.heuristic_classified}")
    for label, counts in (("layer", stats.by_layer), ("project", stats.by_project),
                          ("source", stats.by_source)):
        if counts:
            joined = " ".join(f"{k}={v}" for k, v in sorted(counts.items()))
            print(f"  by {label}: {joined}")
    if skip_report:
        print("  skipped:")
        for reason, entry in sorted(skip_report.items()):
            print(f"    {reason}: {entry['count']}")
            for p in entry["samples"][:3]:
                print(f"      - {p}")
    for s in stats.error_samples:
        print(f"  error sample: {s}")


def cmd_ingest(args: argparse.Namespace) -> int:
    if args.adapter not in ADAPTERS:
        print(f"unknown adapter {args.adapter!r}; have: {', '.join(ADAPTERS)}", file=sys.stderr)
        return 2
    src = args.source or f"<{args.adapter}>"
    ledger = IngestLedger(args.entdb)
    # Ledger row opens BEFORE adapter construction: a missing source dir
    # (unmounted CloudStorage, typo) must surface as a failed run in the
    # dashboard's Intake panel, not vanish with a traceback.
    run_id = ledger.start(args.adapter, src, meta={"dry_run": args.dry_run})
    stats = IngestStats()
    try:
        adapter = _build_adapter(args.adapter, args.source, args.entdb,
                                 exclude=args.exclude)
    except Exception as exc:
        _finish_ledger(ledger, run_id, "failed", stats, None,
                       extra_meta={"dry_run": args.dry_run,
                                   "exception": f"{type(exc).__name__}: {exc}"})
        raise
    classify_fn = None
    if args.llm_classifier:
        from .core.synthesize import classify_layer_llm
        classify_fn = classify_layer_llm
    snapshot = (_snapshot_checkpoints(args.entdb, adapter.name)
                if args.dry_run else None)
    try:
        ingest(_index(args), adapter.fetch(), classify_fn=classify_fn,
               dry_run=args.dry_run, stats=stats,
               entity_store=EntityStore(args.entdb))
    except Exception as exc:
        _finish_ledger(ledger, run_id, "failed", stats, adapter,
                       extra_meta={"dry_run": args.dry_run,
                                   "exception": f"{type(exc).__name__}: {exc}"})
        raise
    finally:
        if snapshot is not None:
            _restore_checkpoints(args.entdb, adapter.name, snapshot)
    watermark_held = False
    if not args.dry_run:
        if stats.errors == 0:
            # Commit deferred watermarks only after the pipeline (including
            # its final flush) succeeded — see adapter.commit_checkpoint().
            getattr(adapter, "commit_checkpoint", lambda: None)()
        else:
            # Errored docs would be skipped forever if the watermark moved
            # past them; hold it so the next run retries the whole window
            # (chunk ids are deterministic, so re-ingest is a cheap upsert).
            watermark_held = hasattr(adapter, "commit_checkpoint")
    skipped_total = sum(
        e["count"] for e in (getattr(adapter, "skip_report", None) or {}).values()
    )
    if (getattr(args, "prune_empty", False) and not args.dry_run
            and stats.docs == 0 and stats.errors == 0 and skipped_total == 0):
        # Watch-loop cycles that saw nothing leave no ledger row — otherwise
        # a 60s poll would bury the dashboard's Intake panel in empty runs.
        ledger.delete(run_id)
        return 0
    _finish_ledger(ledger, run_id, "dry-run" if args.dry_run else "completed",
                   stats, adapter,
                   extra_meta={"dry_run": args.dry_run,
                               **({"watermark_held": True} if watermark_held else {})})
    if args.dry_run:
        _print_dry_run_report(args.adapter, src, stats,
                              getattr(adapter, "skip_report", None))
    else:
        print(f"ingested {stats.chunks} chunks from {args.adapter} ({src})")
        if stats.errors:
            print(f"  {stats.errors} doc(s) errored — see ledger run {run_id}"
                  + ("; watermark held for retry" if watermark_held else ""))
    return 0


def cmd_watch(args: argparse.Namespace) -> int:
    """Universal-intake daemon: poll the BrainInbox drop folder every cycle
    and the AgentMail intake inbox every --mail-every cycles. Empty cycles
    leave no ledger rows. Ctrl-C to stop. Do NOT run alongside a bulk ingest
    (single-writer assumption on the LanceDB index)."""
    import time as _time

    from .adapters.inbox_adapter import DEFAULT_INBOX_DIR, InboxAdapter

    inbox_dir = args.source or os.environ.get("BRAIN_INBOX_DIR", "") or DEFAULT_INBOX_DIR
    Path(inbox_dir).expanduser().mkdir(parents=True, exist_ok=True)
    mail_on = bool(os.environ.get("AGENTMAIL_API_KEY"))
    interval = max(10, args.interval)
    print(f"watching {inbox_dir} every {interval}s | agentmail "
          f"{'every ' + str(args.mail_every) + ' cycles' if mail_on else 'OFF (no AGENTMAIL_API_KEY)'}",
          flush=True)

    cycle = 0
    while True:
        cycle += 1
        targets: list[tuple[str, str]] = []
        try:
            if InboxAdapter(inbox_dir).has_pending():
                targets.append(("inbox", inbox_dir))
        except FileNotFoundError as exc:
            print(f"[watch] {exc}", flush=True)
        if mail_on and cycle % args.mail_every == 1 % args.mail_every:
            targets.append(("agentmail", args.mail_inbox))
        for adapter_name, source in targets:
            ns = argparse.Namespace(**vars(args))
            ns.adapter = adapter_name
            ns.source = source
            ns.dry_run = False
            ns.exclude = None
            ns.llm_classifier = False
            ns.prune_empty = True
            try:
                cmd_ingest(ns)
            except KeyboardInterrupt:
                raise
            except Exception as exc:
                # Ledger already holds the failed row; keep the daemon alive.
                print(f"[watch] {adapter_name} cycle failed: "
                      f"{type(exc).__name__}: {exc}", flush=True)
        try:
            _time.sleep(interval)
        except KeyboardInterrupt:
            print("watch stopped", flush=True)
            return 0


def cmd_serve(args: argparse.Namespace) -> int:
    """Run the HTTP API. Defaults to localhost-only; export BRAIN_BEARER_TOKEN
    to require auth on the LAN."""
    import uvicorn
    os.environ.setdefault("BRAIN_DB", args.db)
    os.environ.setdefault("BRAIN_ENTDB", args.entdb)
    os.environ.setdefault("BRAIN_EMBEDDER", args.embedder)
    uvicorn.run("brain.api:app", host=args.host, port=args.port, reload=args.reload)
    return 0


def cmd_checkpoints(args: argparse.Namespace) -> int:
    rows = CheckpointStore(args.entdb).all()
    if not rows:
        print("no checkpoints yet")
        return 0
    for r in rows:
        print(f"{r['adapter']:14s} {r['key']:12s} = {r['value']}  ({r['updated_at']})")
    return 0


def cmd_query(args: argparse.Namespace) -> int:
    # Same boundary rule as the HTTP API: project is interpolated into the
    # LanceDB filter, so quote characters are rejected, not escaped.
    if args.project and ("'" in args.project or '"' in args.project):
        print("project must not contain quote characters", file=sys.stderr)
        return 2
    rows = _index(args).query(args.text, k=args.k, layer=args.layer, project=args.project)
    if not rows:
        print("no matches")
        return 0
    for i, r in enumerate(rows, 1):
        dist = r.get("_distance")
        score = f"{1 - dist:.3f}" if dist is not None else "n/a"
        tags = " ".join(f"#{t}" for t in r.get("project_tags", []))
        print(f"\n[{i}] score={score}  layer={r['layer']}  src={r['source']}  {tags}")
        snippet = r["text"].replace("\n", " ")
        print(f"    {snippet[:240]}{'…' if len(snippet) > 240 else ''}")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    print(f"brain @ {args.db}: {_index(args).count()} chunks indexed")
    c = EntityStore(args.entdb).counts()
    print(f"graph @ {args.entdb}: {c['entities']} entities, {c['edges']} edges")
    return 0


def cmd_ingest_entities(args: argparse.Namespace) -> int:
    if args.kind in ENTITY_ADAPTERS:
        adapter = ENTITY_ADAPTERS[args.kind](args.source)
    elif args.kind in LIVE_ENTITY_ADAPTERS:
        adapter = _build_live_entity_adapter(args.kind, args.source, args.entdb)
    else:
        known = list(ENTITY_ADAPTERS) + list(LIVE_ENTITY_ADAPTERS)
        print(f"unknown entity kind {args.kind!r}; have: {', '.join(known)}", file=sys.stderr)
        return 2
    res = ingest_entities(EntityStore(args.entdb), adapter)
    src = args.source or f"<{args.kind}>"
    print(f"ingested {res['entities']} entities, {res['edges']} edges from {args.kind} ({src})")
    return 0


def cmd_entities(args: argparse.Namespace) -> int:
    store = EntityStore(args.entdb)
    rows = store.find_by_name(args.name, args.kind) if args.name else store.all_entities(args.kind)
    if not rows:
        print("no entities")
        return 0
    for e in rows:
        print(f"\n{e.id}  ({e.kind})  {e.name}")
        if e.aliases:
            print(f"    aliases: {', '.join(e.aliases)}")
        for key, val in e.attributes.items():
            print(f"    {key}: {val}")
    return 0


def cmd_resolve(args: argparse.Namespace) -> int:
    store = EntityStore(args.entdb)
    r = resolve(store, args.mention, args.context or "", args.kind)
    print(f"status: {r.status.value}  confidence: {r.confidence:.2f}")
    print(f"rationale: {r.rationale}")
    if r.entity:
        print(f"resolved: {r.entity.name}  [{r.entity.id}]")
    elif r.candidates:
        print("candidates:")
        score_map = dict(r.scores)
        for c in r.candidates:
            s = score_map.get(c.id, 0.0)
            print(f"  - {c.name}  [{c.id}]  score={s:.2f}")
    return 0


def cmd_dossier(args: argparse.Namespace) -> int:
    store = EntityStore(args.entdb)
    index = _index(args) if args.use_chunks else None
    card = dossier(
        store,
        index,
        args.mention,
        event_hint=args.event or "",
        context=args.context or "",
    )
    if card.needs_disambiguation:
        print(f"AMBIGUOUS: {args.mention} could be:")
        for n in card.needs_disambiguation:
            print(f"  - {n}")
        print(f"(confidence {card.confidence:.2f})")
        return 0
    print(f"\n{card.name}  [confidence {card.confidence:.2f}]")
    if card.role:
        print(f"  role: {card.role}")
    if card.relationship:
        print(f"  rel:  {card.relationship}")
    if card.where_met:
        print(f"  met:  {card.where_met}")
    if card.discussed:
        print("  discussed:")
        for b in card.discussed:
            print(f"    - {b}")
    return 0


def cmd_who(args: argparse.Namespace) -> int:
    """Graph traversal taste: resolve a name, show what they attended (and who else
    was there). A preview of the dossier join the next step will synthesize."""
    store = EntityStore(args.entdb)
    matches = store.find_by_name(args.name, "person")
    if not matches:
        print(f"no person resolves to {args.name!r}")
        return 0
    person = matches[0]
    print(f"{person.name}  [{person.id}]")
    for key in ("org", "title", "note"):
        if key in person.attributes:
            print(f"  {key}: {person.attributes[key]}")
    events = store.neighbors(person.id, "attended")
    if not events:
        print("  (no attended events on file)")
    for _edge, event in events:
        if not event:
            continue
        when = event.attributes.get("date", "")
        where = event.attributes.get("location", "")
        print(f"  attended: {event.name}  {when} {where}".rstrip())
        # who else was there
        others = [
            ev.name for e, ev in _co_attendees(store, event.id)
            if ev and ev.id != person.id
        ]
        if others:
            print(f"      co-attendees: {', '.join(others)}")
    return 0


def _co_attendees(store: EntityStore, event_id: str):
    # Reverse lookup: people with an 'attended' edge into this event.
    rows = store._db.execute(  # noqa: SLF001 - internal demo helper
        "SELECT src FROM edges WHERE rel='attended' AND dst=?", (event_id,)
    ).fetchall()
    return [(None, store.get_entity(r["src"])) for r in rows]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="brain", description="Second-brain spine (Phase 0/1)")
    p.add_argument("--db", default="./brain_index", help="LanceDB path (chunks)")
    p.add_argument("--entdb", default="./entities.db", help="SQLite path (entity graph)")
    p.add_argument("--embedder", default="fake", choices=["fake", "local", "openai"])
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("ingest", help="ingest a text source into the vector index")
    pi.add_argument("--adapter", required=True, choices=ADAPTERS)
    pi.add_argument("--source", default="",
                    help="path/config (fieldy ignores this — uses FIELDY_API_KEY env)")
    pi.add_argument("--llm-classifier", action="store_true",
                    help="use Claude Haiku for pass-2 layer classification "
                         "(needs ANTHROPIC_API_KEY; falls back to heuristic per-chunk on error)")
    pi.add_argument("--dry-run", action="store_true",
                    help="full adapter+chunk+tag pass and preview report, but write "
                         "nothing (checkpoints rolled back; ledger row status=dry-run)")
    pi.add_argument("--exclude", action="append", default=[],
                    help="skip files whose relative path matches this case-insensitive "
                         "substring/glob; repeatable (filesystem + claude-code adapters; "
                         "claude-code matches project dir names, additive to its defaults)")
    pi.set_defaults(func=cmd_ingest)

    pe = sub.add_parser("ingest-entities", help="ingest contacts/calendar into the graph")
    pe.add_argument("--kind", required=True,
                    choices=list(ENTITY_ADAPTERS) + list(LIVE_ENTITY_ADAPTERS))
    pe.add_argument("--source", default="",
                    help=".vcf/.ics for file adapters; calendarId for gcal-live "
                         "(default 'primary'); ignored for people-live")
    pe.set_defaults(func=cmd_ingest_entities)

    pq = sub.add_parser("query", help="semantic query over the vector index")
    pq.add_argument("text")
    pq.add_argument("-k", type=int, default=5)
    pq.add_argument("--layer", choices=["artifact", "decision", "reasoning", "workaround"])
    pq.add_argument("--project")
    pq.set_defaults(func=cmd_query)

    pen = sub.add_parser("entities", help="list/lookup entities in the graph")
    pen.add_argument("--name", help="resolve by name/alias (exact, case-insensitive)")
    pen.add_argument("--kind", choices=["person", "event", "place", "org"])
    pen.set_defaults(func=cmd_entities)

    pw = sub.add_parser("who", help="graph traversal: what a person attended + co-attendees")
    pw.add_argument("name")
    pw.set_defaults(func=cmd_who)

    pr = sub.add_parser("resolve", help="context-aware entity resolution (the 'two Jeffs' fix)")
    pr.add_argument("mention", help="raw token heard/seen (e.g. 'Jeff')")
    pr.add_argument("--context", help="surrounding conversation text used for disambiguation")
    pr.add_argument("--kind", default="person", choices=["person", "event", "place", "org"])
    pr.set_defaults(func=cmd_resolve)

    pd = sub.add_parser("dossier", help="assemble the popup card for a person")
    pd.add_argument("mention", help="person name/alias (e.g. 'Jeff')")
    pd.add_argument("--event", help="event hint (e.g. 'Fall Block Party')")
    pd.add_argument("--context", help="surrounding text for disambiguation")
    pd.add_argument("--use-chunks", action="store_true",
                    help="also pull discussion bullets from the vector index")
    pd.set_defaults(func=cmd_dossier)

    ps = sub.add_parser("stats", help="index + graph stats")
    ps.set_defaults(func=cmd_stats)

    pc = sub.add_parser("checkpoints", help="list incremental-sync watermarks")
    pc.set_defaults(func=cmd_checkpoints)

    psv = sub.add_parser("serve", help="run the HTTP API (FastAPI)")
    psv.add_argument("--host", default="127.0.0.1")
    psv.add_argument("--port", type=int, default=8088)
    psv.add_argument("--reload", action="store_true")
    psv.set_defaults(func=cmd_serve)

    pwatch = sub.add_parser(
        "watch", help="universal-intake daemon: poll BrainInbox + AgentMail")
    pwatch.add_argument("--source", default="",
                        help="inbox drop folder (default: BRAIN_INBOX_DIR or ~/BrainInbox)")
    pwatch.add_argument("--interval", type=int, default=60,
                        help="seconds between cycles (min 10; default 60)")
    pwatch.add_argument("--mail-every", type=int, default=5,
                        help="poll AgentMail every N cycles (default 5)")
    pwatch.add_argument("--mail-inbox", default="",
                        help="AgentMail inbox id (default synthbrain@agentmail.to)")
    pwatch.set_defaults(func=cmd_watch)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    # LanceDB's native runtime can segfault during interpreter teardown (a known
    # Rust/Arrow shutdown race). All work is done by the time main() returns, so
    # we flush and hard-exit to guarantee a clean exit code.
    _code = main()
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(_code)

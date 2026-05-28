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

from .adapters.calendar_adapter import CalendarAdapter
from .adapters.contacts_adapter import ContactsAdapter
from .adapters.entity_base import ingest_entities
from .adapters.mem_adapter import MemAdapter
from .core.embed import get_embedder
from .core.entities import EntityStore
from .core.index import BrainIndex
from .core.pipeline import ingest

ADAPTERS = {"mem": MemAdapter}
ENTITY_ADAPTERS = {"contacts": ContactsAdapter, "calendar": CalendarAdapter}


def _index(args: argparse.Namespace) -> BrainIndex:
    return BrainIndex(args.db, get_embedder(args.embedder))


def cmd_ingest(args: argparse.Namespace) -> int:
    if args.adapter not in ADAPTERS:
        print(f"unknown adapter {args.adapter!r}; have: {', '.join(ADAPTERS)}", file=sys.stderr)
        return 2
    adapter = ADAPTERS[args.adapter](args.source)
    n = ingest(_index(args), adapter.fetch())
    print(f"ingested {n} chunks from {args.adapter} ({args.source})")
    return 0


def cmd_query(args: argparse.Namespace) -> int:
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
    if args.kind not in ENTITY_ADAPTERS:
        print(f"unknown entity kind {args.kind!r}; have: {', '.join(ENTITY_ADAPTERS)}", file=sys.stderr)
        return 2
    adapter = ENTITY_ADAPTERS[args.kind](args.source)
    res = ingest_entities(EntityStore(args.entdb), adapter)
    print(f"ingested {res['entities']} entities, {res['edges']} edges from {args.kind} ({args.source})")
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
    pi.add_argument("--adapter", required=True)
    pi.add_argument("--source", required=True, help="path/config for the adapter")
    pi.set_defaults(func=cmd_ingest)

    pe = sub.add_parser("ingest-entities", help="ingest contacts/calendar into the graph")
    pe.add_argument("--kind", required=True, choices=list(ENTITY_ADAPTERS))
    pe.add_argument("--source", required=True, help=".vcf (contacts) or .ics (calendar)")
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

    ps = sub.add_parser("stats", help="index + graph stats")
    ps.set_defaults(func=cmd_stats)

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

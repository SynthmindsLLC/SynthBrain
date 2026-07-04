"""graphlab — network-science layer over the entity graph.

Two DERIVED edge types (both canonical methods, not invented heuristics):

  co_attended   Weighted one-mode projection of the person-event bipartite
                graph. Sharing an event is the classic affiliation tie
                (Breiger 1974, "The Duality of Persons and Groups"). Weights
                use Newman's fractional counting — each shared event k with
                n_k attendees contributes 1/(n_k - 1) — so two people alone
                in a meeting bond harder than two faces in a 40-person
                all-hands (Newman 2001, Phys. Rev. E 64, 016132).

  co_mentioned  Entities whose canonical ids co-occur in the same chunk,
                weighted by pointwise mutual information so ubiquitous
                entities don't drown out genuinely informative pairings
                (Church & Hanks 1990). Pairs need >= min_count chunks and
                PMI > 0 (co-occurring MORE than chance).

Node features persisted to graph_metrics (one row per entity):

  degree       normalized degree centrality
  eigenvector  Bonacich (1987) — influence via well-connected neighbors
  pagerank     Brin & Page (1998), damping 0.85 — random-surfer influence
  betweenness  Freeman (1977), Brandes (2001) algorithm — brokerage/bridging
  closeness    harmonic-adjacent classic closeness — reach efficiency
  clustering   Watts & Strogatz (1998) — local triadic closure
  core         k-core number (Seidman 1983) — cohesion shell
  community    Louvain modularity community (Blondel et al. 2008), seeded
               for deterministic runs

Implementation rides on networkx (BSD, pure Python) — Brandes betweenness
and Louvain are not responsibly hand-rolled.
"""

from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import combinations
from typing import TYPE_CHECKING, Any, Iterable

import networkx as nx

from .entities import KINDS, Edge, EntityStore

if TYPE_CHECKING:  # pragma: no cover
    from .index import BrainIndex

DERIVED_RELS = ("co_attended", "co_mentioned")
METRIC_COLUMNS = ("degree", "eigenvector", "pagerank", "betweenness",
                  "closeness", "clustering", "core", "community")


# --- derived edges -----------------------------------------------------------


def derive_co_attendance(store: EntityStore, *, min_weight: float = 0.0) -> int:
    """Project person-event 'attended' edges onto person-person
    'co_attended' edges with Newman fractional weights. Returns the number
    of edges written. Re-derivation upserts (PK src,rel,dst)."""
    attendees: dict[str, list[str]] = defaultdict(list)
    with store._lock:  # noqa: SLF001 — raw read, same idiom as api.py
        rows = store._db.execute(  # noqa: SLF001
            "SELECT src, dst FROM edges WHERE rel='attended'"
        ).fetchall()
    for r in rows:
        attendees[r["dst"]].append(r["src"])

    weights: dict[tuple[str, str], float] = defaultdict(float)
    shared: dict[tuple[str, str], int] = defaultdict(int)
    for people in attendees.values():
        uniq = sorted(set(people))
        n = len(uniq)
        if n < 2:
            continue
        w = 1.0 / (n - 1)  # Newman (2001) fractional counting
        for a, b in combinations(uniq, 2):
            weights[(a, b)] += w
            shared[(a, b)] += 1

    written = 0
    for (a, b), w in weights.items():
        if w < min_weight:
            continue
        store.add_edge(Edge(
            src=a, rel="co_attended", dst=b,
            attributes={"weight": round(w, 4), "shared_events": shared[(a, b)],
                        "derived": True},
        ))
        written += 1
    return written


def _canonical_ids(tags: Iterable[str]) -> list[str]:
    out = []
    for t in tags or []:
        head, _, _ = str(t).partition(":")
        if head in KINDS and ":" in str(t):
            out.append(str(t))
    return out


def derive_co_mentions(
    index: "BrainIndex",
    store: EntityStore,
    *,
    min_count: int = 2,
    min_pmi: float = 0.0,
) -> int:
    """PMI-weighted co-occurrence of canonical entity ids across chunks.
    PMI = log2( p(a,b) / (p(a) p(b)) ) with probabilities estimated over
    chunks that mention at least one canonical entity."""
    table = index.scan(["entity_tags"])
    singles: Counter[str] = Counter()
    pairs: Counter[tuple[str, str]] = Counter()
    n_docs = 0
    for tags in table.column("entity_tags").to_pylist():
        ids = sorted(set(_canonical_ids(tags)))
        if not ids:
            continue
        n_docs += 1
        singles.update(ids)
        pairs.update(combinations(ids, 2))

    if n_docs == 0:
        return 0
    written = 0
    for (a, b), c in pairs.items():
        if c < min_count:
            continue
        pmi = math.log2((c / n_docs) / ((singles[a] / n_docs) * (singles[b] / n_docs)))
        if pmi <= min_pmi:
            continue
        store.add_edge(Edge(
            src=a, rel="co_mentioned", dst=b,
            attributes={"weight": round(pmi, 4), "count": c, "derived": True},
        ))
        written += 1
    return written


# --- graph + metrics ---------------------------------------------------------


def build_nx_graph(store: EntityStore, *, rels: tuple[str, ...] | None = None) -> nx.Graph:
    """Undirected weighted graph over all entities + (optionally filtered)
    edges. Edge weight = attributes['weight'] if present else 1.0; parallel
    rels between the same pair sum their weights."""
    g = nx.Graph()
    with store._lock:  # noqa: SLF001
        ent_rows = store._db.execute("SELECT id, kind, name FROM entities").fetchall()  # noqa: SLF001
        edge_rows = store._db.execute("SELECT src, rel, dst, attributes FROM edges").fetchall()  # noqa: SLF001
    for r in ent_rows:
        g.add_node(r["id"], kind=r["kind"], name=r["name"])
    for r in edge_rows:
        if rels and r["rel"] not in rels:
            continue
        try:
            w = float(json.loads(r["attributes"] or "{}").get("weight", 1.0))
        except (ValueError, TypeError, json.JSONDecodeError):
            w = 1.0
        if g.has_edge(r["src"], r["dst"]):
            g[r["src"]][r["dst"]]["weight"] += w
            g[r["src"]][r["dst"]]["rels"].append(r["rel"])
        else:
            g.add_edge(r["src"], r["dst"], weight=w, rels=[r["rel"]])
    return g


def compute_metrics(g: nx.Graph) -> dict[str, dict[str, float | int]]:
    """Per-node metric dict. Isolates get zeros; eigenvector failures fall
    back to degree ranking rather than aborting the run."""
    if g.number_of_nodes() == 0:
        return {}
    degree = nx.degree_centrality(g)
    pagerank = nx.pagerank(g, alpha=0.85, weight="weight")
    betweenness = nx.betweenness_centrality(g, weight=None, normalized=True)
    closeness = nx.closeness_centrality(g)
    clustering = nx.clustering(g)
    core = nx.core_number(g) if g.number_of_edges() else {n: 0 for n in g}
    try:
        eigen = nx.eigenvector_centrality(g, max_iter=1000, weight="weight")
    except (nx.PowerIterationFailedConvergence, nx.NetworkXException):
        eigen = degree  # documented fallback: rank by degree instead
    communities: dict[str, int] = {}
    if g.number_of_edges():
        for i, members in enumerate(
            nx.community.louvain_communities(g, weight="weight", seed=42)
        ):
            for node in members:
                communities[node] = i

    out: dict[str, dict[str, float | int]] = {}
    for n in g.nodes:
        out[n] = {
            "degree": round(degree.get(n, 0.0), 6),
            "eigenvector": round(eigen.get(n, 0.0), 6),
            "pagerank": round(pagerank.get(n, 0.0), 6),
            "betweenness": round(betweenness.get(n, 0.0), 6),
            "closeness": round(closeness.get(n, 0.0), 6),
            "clustering": round(clustering.get(n, 0.0), 6),
            "core": int(core.get(n, 0)),
            "community": int(communities.get(n, -1)),
        }
    return out


# --- persistence ---------------------------------------------------------------


def _ensure_table(store: EntityStore) -> None:
    with store._lock:  # noqa: SLF001
        store._db.execute(  # noqa: SLF001
            """CREATE TABLE IF NOT EXISTS graph_metrics (
                 entity_id TEXT PRIMARY KEY,
                 degree REAL, eigenvector REAL, pagerank REAL, betweenness REAL,
                 closeness REAL, clustering REAL, core INTEGER, community INTEGER,
                 computed_at TEXT
               )"""
        )
        store._db.commit()  # noqa: SLF001


def persist_metrics(store: EntityStore, metrics: dict[str, dict]) -> None:
    _ensure_table(store)
    now = datetime.now(timezone.utc).isoformat()
    with store._lock:  # noqa: SLF001
        store._db.execute("DELETE FROM graph_metrics")  # noqa: SLF001 — full recompute
        store._db.executemany(  # noqa: SLF001
            """INSERT INTO graph_metrics
               (entity_id, degree, eigenvector, pagerank, betweenness,
                closeness, clustering, core, community, computed_at)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            [(eid, m["degree"], m["eigenvector"], m["pagerank"], m["betweenness"],
              m["closeness"], m["clustering"], m["core"], m["community"], now)
             for eid, m in metrics.items()],
        )
        store._db.commit()  # noqa: SLF001


def load_metrics(store: EntityStore) -> dict[str, dict[str, Any]]:
    _ensure_table(store)
    with store._lock:  # noqa: SLF001
        rows = store._db.execute("SELECT * FROM graph_metrics").fetchall()  # noqa: SLF001
    return {
        r["entity_id"]: {c: r[c] for c in METRIC_COLUMNS} | {"computed_at": r["computed_at"]}
        for r in rows
    }


# --- split-identity candidates ---------------------------------------------------


def _entity_emails(e) -> list[str]:
    emails = [a for a in e.aliases if "@" in a]
    emails += [x for x in (e.attributes.get("emails") or []) if "@" in str(x)]
    if "@" in e.name:
        emails.append(e.name)
    return [x.lower() for x in dict.fromkeys(emails)]


def _name_tokens(name: str) -> list[str]:
    import re
    return [t for t in re.split(r"[^a-z]+", name.lower()) if len(t) >= 3]


def suggest_merges(store: EntityStore, *, kind: str = "person") -> list[dict[str, Any]]:
    """Deterministic split-identity candidates, report-only (merging is a
    human call via `brain merge-entities`). Two rules, strongest first:

      shared-email   the same address appears on two entities — near-certain
      name-in-email  one entity's name tokens appear in another's email
                     local part ('wes'+'shields' in wes.shields@…) — strong
                     when both first+last match, weak on first-name only

    Probabilistic record linkage (Fellegi & Sunter 1969) is the literature
    answer at scale; at a personal graph's size these two rules catch the
    observed splits without false-positive risk worth modeling."""
    ents = store.all_entities(kind=kind)
    by_email: dict[str, list] = defaultdict(list)
    for e in ents:
        for em in _entity_emails(e):
            by_email[em].append(e)

    out: list[dict[str, Any]] = []
    seen_pairs: set[tuple[str, str]] = set()

    def add(a, b, confidence: str, reason: str) -> None:
        key = tuple(sorted((a.id, b.id)))
        if key in seen_pairs or a.id == b.id:
            return
        seen_pairs.add(key)
        # Suggest folding the email-named identity into the human-named one.
        named, other = (a, b) if "@" not in a.name else (b, a)
        out.append({"keep": named.id, "merge": other.id,
                     "keep_name": named.name, "merge_name": other.name,
                     "confidence": confidence, "reason": reason})

    for em, group in by_email.items():
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                add(group[i], group[j], "strong", f"shared email {em}")

    named = [e for e in ents if "@" not in e.name and _name_tokens(e.name)]
    for e in ents:
        for em in _entity_emails(e):
            local = em.split("@", 1)[0]
            local_tokens = set(_name_tokens(local.replace(".", " ")
                                            .replace("_", " ").replace("-", " ")))
            if not local_tokens:
                continue
            for n in named:
                if n.id == e.id:
                    continue
                toks = _name_tokens(n.name)
                hits = [t for t in toks if any(t in lt or lt in t for lt in local_tokens)]
                if len(hits) >= 2:
                    add(n, e, "strong", f"name tokens {hits} match email {em}")
                elif len(toks) >= 1 and toks[0] in local_tokens and len(local_tokens) == 1:
                    add(n, e, "weak", f"first name '{toks[0]}' is email local part {em}")
    strength = {"strong": 0, "weak": 1}
    out.sort(key=lambda s: (strength[s["confidence"]], s["keep"]))
    return out


# --- ego networks --------------------------------------------------------------


def ego_subgraph(store: EntityStore, entity_id: str, *, hops: int = 1,
                 rels: tuple[str, ...] | None = None) -> tuple[list[str], list[dict]]:
    """k-hop neighborhood (Freeman 1982 ego network, generalized to k) over
    the undirected edge set. Returns (node ids, edge dicts) with all edges
    among the included nodes."""
    g = build_nx_graph(store, rels=rels)
    if entity_id not in g:
        return [], []
    nodes = {entity_id}
    frontier = {entity_id}
    for _ in range(max(1, hops)):
        frontier = {nb for n in frontier for nb in g.neighbors(n)} - nodes
        if not frontier:
            break
        nodes |= frontier
    edges = [
        {"source": a, "target": b,
         "weight": round(d.get("weight", 1.0), 4), "rels": d.get("rels", [])}
        for a, b, d in g.subgraph(nodes).edges(data=True)
    ]
    return sorted(nodes), edges


# --- orchestrator ---------------------------------------------------------------


def run_all(store: EntityStore, index: "BrainIndex | None" = None, *,
            min_count: int = 2, min_pmi: float = 0.0) -> dict[str, Any]:
    """Derive both edge types, compute + persist metrics, return a summary."""
    co_att = derive_co_attendance(store)
    co_men = derive_co_mentions(index, store, min_count=min_count,
                                min_pmi=min_pmi) if index is not None else 0
    g = build_nx_graph(store)
    metrics = compute_metrics(g)
    persist_metrics(store, metrics)

    def top(metric: str, k: int = 5) -> list[dict]:
        ranked = sorted(metrics.items(), key=lambda kv: kv[1][metric], reverse=True)[:k]
        return [{"id": eid, "name": g.nodes[eid].get("name", eid), metric: m[metric]}
                for eid, m in ranked if m[metric] > 0]

    communities = {m["community"] for m in metrics.values() if m["community"] >= 0}
    return {
        "nodes": g.number_of_nodes(),
        "edges": g.number_of_edges(),
        "density": round(nx.density(g), 6),
        "derived": {"co_attended": co_att, "co_mentioned": co_men},
        "communities": len(communities),
        "top_eigenvector": top("eigenvector"),
        "top_betweenness": top("betweenness"),
        "top_pagerank": top("pagerank"),
    }

---
title: "Tarjan's Algorithm Overview"
description: "A fundamental algorithm in graph theory for finding the strongly connected components (SCCs) of a directed graph, named after its inventor Robert Tarjan. The algorithm is notable for its efficiency and linear time complexity."
type: "concept"
tags:
- "Graph Theory"
- "Algorithms"
- "Strongly Connected Components"
relationships:
- "#developed_by [[Robert Tarjan]]"
- "#applies_to [[Directed Graphs]]"
- "#uses_Depth-First Search (DFS)"
- "#has_time_complexity [[O(V+E)]]"
birthdate: "1934-03-30"
deathdate: "2024-03-30"
---

# Tarjan's Algorithm Overview

Tarjan's algorithm, named after its inventor Robert Tarjan, is a fundamental algorithm in graph theory for finding the strongly connected components (SCCs) of a directed graph. A strongly connected component is a maximal subgraph where every vertex is reachable from every other vertex within the same component. The algorithm is notable for its efficiency, requiring just a single pass through the graph (a single Depth-First Search (DFS) traversal), making it linear in time complexity, $$O(V+E)$$, where $$V$$ is the number of vertices and $$E$$ is the number of edges in the graph.

## Key Features and Steps

- **Depth-First Search (DFS)**: Tarjan's algorithm modifies the standard DFS traversal to identify SCCs.
- **Low-Link Values**: Each node is assigned a unique index during DFS, and a low-link value that represents the smallest index of any node known to be reachable from it, including itself.
- **Stack Invariant**: Nodes are placed on a stack in the order they are visited. A node remains on the stack if and only if there exists a back edge to a node not yet placed in any SCC.
- **SCC Identification**: When the DFS finishes exploring a node and its descendants, if the node's index is equal to its low-link value, it is the root of an SCC. All nodes on the stack up to this node are popped and form an SCC.

## Applications

Tarjan's algorithm is widely used in computer science, particularly in the fields of compiler design, optimization, and network analysis, due to its ability to efficiently decompose a graph into its strongly connected components. This decomposition is crucial for understanding the structure of complex networks and for optimizing various algorithms that operate on graphs.

## Variants and Related Algorithms

While Tarjan's algorithm specifically addresses the identification of SCCs in directed graphs, Robert Tarjan has also developed other algorithms for different graph-related problems, such as finding bridges, articulation points, and the lowest common ancestors in trees[1].

- Important [[wikilinks]]: [[Graph Theory]], [[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Depth-First Search]], [[Strongly Connected Components]], [[Computational Complexity]]

Sources
[1] Tarjan's algorithm - Wikipedia https://en.wikipedia.org/wiki/Tarjan%27s_algorithm
[2] Finding Strongly Connected Components: Tarjan's Algorithm https://www.baeldung.com/cs/scc-tarjans-algorithm
[3] Tarjan's strongly connected components algorithm - Wikipedia https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
[4] Tarjan's Algorithm to find Strongly Connected Components https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
[5] Tarjan's Algorithm for Strongly Connected Components - Topcoder https://www.topcoder.com/thrive/articles/tarjans-algorithm-for-strongly-connected-components
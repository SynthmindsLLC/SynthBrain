---
title: "Dinic's Algorithm"
description: "A strongly polynomial method for computing the maximum flow in a flow network, introduced by Yefim Dinitz in 1970 and operates in $$ O(|V|^2|E|) $$."
type: "concept"
tags:
- "Algorithms"
- "Graph Theory"
- "Maximum Flow"
relationships:
- "#developed_by [[Yefim Dinitz]]"
- "#applies_to [[Flow Networks]]"
- "#related_to [[Breadth-First Search]], [[Blocking Flow]]"
---

## Dinic's Algorithm

Dinic's algorithm, also known as Dinitz's algorithm, is a strongly polynomial method for computing the maximum flow in a flow network. It was conceived by Yefim Dinitz in 1970 and operates in $$ O(|V|^2|E|) $$ time, where $$ |V| $$ is the number of vertices and $$ |E| $$ is the number of edges in the graph[1].

### How Dinic's Algorithm Works
- The algorithm begins with an initial flow of 0 and repeatedly finds augmenting paths in the residual graph.
- It introduces the concepts of level graphs and blocking flows to improve performance.
- A level graph is constructed using a breadth-first search (BFS), where levels are assigned to nodes based on their distance from the source in terms of the number of edges[1][2][3].
- A blocking flow is an augmenting flow after which no more augmenting paths can be found in the level graph[1][3].

### Pseudocode
```plaintext
function Dinic(Graph, source, sink):
    Initialize flow to 0
    while there exists an augmenting path in the level graph:
        Find blocking flow in the level graph
        Augment the flow in the network by the blocking flow
    return flow
```

### Properties
- **Time Complexity**: $$ O(|V|^2|E|) $$ for general networks. On unit networks (networks where all edges have unit capacity), the algorithm runs in $$ O(|E|\sqrt{|V|}) $$[1][3].
- **Space Complexity**: $$ O(|V| + |E|) $$, as it requires space to store the level graph and the adjacency list of the graph[2].

### Applications
- Dinic's algorithm is used in various applications such as network routing, bipartite matching, and operations research for optimizing transportation and flow of goods and services[1][2][6].

### Limitations
- While the algorithm is efficient, its performance can degrade on networks with a very large number of edges due to its cubic dependency on the number of vertices[1].

### Example
Consider a flow network with vertices and edges between them having various capacities. Dinic's algorithm can iteratively find augmenting paths and update the flow until no augmenting paths are found in the level graph, thereby determining the maximum flow in the network[1][2].

### Conclusion
Dinic's algorithm is an efficient and effective method for solving the maximum flow problem in networks, with a polynomial time complexity that makes it suitable for a wide range of applications.

- [[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Dinic's Algorithm]]
- [[Graph Theory]]
- [[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Maximum Flow Problem]]
- [[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Breadth-First Search]]

Sources
[1] Dinic's algorithm - Wikipedia https://en.wikipedia.org/wiki/Dinic%27s_algorithm
[2] Dinic's algorithm for Maximum Flow - GeeksforGeeks https://www.geeksforgeeks.org/dinics-algorithm-maximum-flow/
[3] Maximum flow - Dinic's algorithm¶ https://cp-algorithms.com/graph/dinic.html
[4] Network Flow: Dinic’s Algorithm | Baeldung on Computer Science https://www.baeldung.com/cs/dinics
[5] Dinic's Algorithm | Network Flow | Graph Theory https://youtube.com/watch?v=M6cm8UeeziI
[6] Edmonds-Karp and Dinic’s Algorithms for Maximum Flow https://www.topcoder.com/thrive/articles/edmonds-karp-and-dinics-algorithms-for-maximum-flow
[7] [Tutorial] My way of understanding Dinitz's ("Dinic's") algorithm - Codeforces https://codeforces.com/blog/entry/104960

By Perplexity at https://www.perplexity.ai/search/Depth-first-search-JdkKo16.QR.aXHpttbrQyw
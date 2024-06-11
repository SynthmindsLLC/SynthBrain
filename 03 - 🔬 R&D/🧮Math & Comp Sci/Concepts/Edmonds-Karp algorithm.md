---
title: "Edmonds-Karp Algorithm"
description: "An implementation of the Ford-Fulkerson method for computing the maximum flow in a flow network, using breadth-first search to find the shortest augmenting path and ensuring polynomial time complexity."
type: "concept"
tags:
- "Algorithms"
- "Graph Theory"
- "Maximum Flow"
relationships:
- "#developed_by [[Yefim Dinitz]], [[Jack Edmonds]], [[Richard Karp]]"
- "#applies_to [[Flow Networks]]"
- "#related_to [[Ford-Fulkerson method]]"
- "#used_in [[Network Routing]], [[Bipartite Matching]], [[Operations Research]]"
---

## Edmonds-Karp Algorithm

The Edmonds-Karp algorithm is an implementation of the Ford-Fulkerson method for computing the maximum flow in a flow network. It was first published by Yefim Dinitz in 1970 and independently by Jack Edmonds and Richard Karp in 1972. The algorithm is distinguished by its use of breadth-first search (BFS) to find the shortest augmenting path, ensuring polynomial time complexity[1][2][3].

### How the Algorithm Works
- The algorithm initializes the flow to zero and repeatedly finds augmenting paths in the residual graph (the graph that represents the capacities left after considering the current flow) from the source to the sink.
- The flow is increased along the augmenting path by the minimum capacity of the edges in the path.
- This process continues until no augmenting path can be found in the residual graph[1][2][3].

### Pseudocode
```plaintext
EdmondsKarp(G, s, t):
    flow := 0
    repeat
        Find the shortest augmenting path from s to t using BFS
        Augment flow along this path
    until no augmenting path can be found
    return flow
```

### Properties
- **Time Complexity**: The algorithm runs in $$O(VE^2)$$ time, even for irrational capacities. This is a significant improvement over the Ford-Fulkerson method, whose time complexity can vary[1][2].
- **Space Complexity**: $$O(V)$$, primarily for storing the residual graph and the path-finding data structures[1].

### Applications
- The Edmonds-Karp algorithm is used in various applications such as network routing, bipartite matching, and in operations research for optimizing transportation, flow of goods, and services[1][3].

### Limitations
- While the algorithm ensures polynomial time complexity, it may not be as efficient for networks with very large numbers of edges due to its $$O(VE^2)$$ time complexity[1].

### Example
Consider a flow network with vertices and edges between them having various capacities. The Edmonds-Karp algorithm iteratively finds augmenting paths from the source to the sink and updates the flow until no such paths exist, thereby determining the maximum flow in the network[2][4].

### Conclusion
The Edmonds-Karp algorithm is a robust method for solving the maximum flow problem in networks, offering guaranteed polynomial time complexity and wide-ranging applications in computer science and operations research.

- [[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Edmonds-Karp algorithm]]
- [[Graph Theory]]
- [[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Maximum Flow Problem]]
- [[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Breadth-First Search]]

Sources
[1] Edmonds–Karp algorithm - Wikipedia https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
[2] Maximum flow - Ford-Fulkerson and Edmonds-Karp¶ https://cp-algorithms.com/graph/edmonds_karp.html
[3] Edmonds-Karp Algorithm | Brilliant Math & Science Wiki https://brilliant.org/wiki/edmonds-karp-algorithm/
[4] Network Flow: Edmonds-Karp Algorithm | Baeldung on Computer Science https://www.baeldung.com/cs/network-flow-edmonds-karp-algorithm
[5] Edmonds Karp Algorithm | Network Flow | Graph Theory https://youtube.com/watch?v=RppuJYwlcI8

By Perplexity at https://www.perplexity.ai/search/Depth-first-search-JdkKo16.QR.aXHpttbrQyw
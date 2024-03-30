---
Date: [[2024-02-24]]
Tags: 
 - "#FordFulkersonAlgorithm"
 - "#Algorithms"
 - "#GraphTheory"
 - "#MaximumFlow"
---

## Ford-Fulkerson Algorithm

The Ford-Fulkerson algorithm is a method used to solve the maximum flow problem in a flow network. It aims to find the maximum amount of flow that can be sent from a source vertex to a sink vertex in a network with capacity constraints on its edges[1].

### How the Ford-Fulkerson Algorithm Works
- The algorithm starts with an initial flow of 0.
- It repeatedly finds augmenting paths in the residual graph (the graph that represents the capacities left after considering the current flow) from the source to the sink.
- The flow is increased along the augmenting path by the minimum capacity of the edges in the path.
- This process continues until no augmenting path can be found in the residual graph[1][3][7].

### Pseudocode
```plaintext
FordFulkerson(G, s, t):
    Initialize flow to 0
    while there exists an augmenting path p from s to t in the residual graph Gf:
        Augment flow along p
    return flow
```

### Properties
- **Time Complexity**: The worst-case time complexity can be reduced to $$O(VE^2)$$ when BFS is used to find augmenting paths (Edmonds-Karp Algorithm). However, the general Ford-Fulkerson algorithm does not specify the method to find augmenting paths, and its time complexity can vary[1][8].
- **Space Complexity**: $$O(V)$$, as it primarily requires storage for the residual graph and the path-finding data structures[1].

### Applications
- The Ford-Fulkerson algorithm is used in various applications such as network routing, bipartite matching, and in operations research for optimizing transportation, flow of goods, and services[1][3].

### Limitations
- The algorithm assumes that all edge capacities are integers. If capacities are rational or real numbers, the algorithm may not terminate or may not yield the correct maximum flow[8].
- The performance of the Ford-Fulkerson algorithm heavily depends on the method used to find augmenting paths. The choice of paths can lead to significantly different running times[8].

### Example
Consider a flow network with vertices and edges between them having various capacities. The Ford-Fulkerson algorithm can iteratively find augmenting paths from the source to the sink and update the flow until no such paths exist, thereby determining the maximum flow in the network[1][3].

### Conclusion
The Ford-Fulkerson algorithm is a foundational method for solving the maximum flow problem in networks, with wide-ranging applications in computer science and operations research.

- [[Ford-Fulkerson algorithm]]
- [[Graph Theory]]
- [[Maximum Flow Problem]]
- [[Edmonds-Karp algorithm]]

Sources
[1] Ford-Fulkerson Algorithm for Maximum Flow Problem - GeeksforGeeks https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
[2] Ford-Fulkerson in 5 minutes https://youtube.com/watch?v=Tl90tNtKvxs
[3] Ford-Fulkerson Algorithm https://www.programiz.com/dsa/ford-fulkerson-algorithm
[4] Ford-Fulkerson Algorithm https://algorithms.discrete.ma.tum.de/flow/ford-fulkerson/
[5] Finding Max Flow using the Ford-Fulkerson Algorithm and Matthew McConaughey https://downey.io/blog/max-flow-ford-fulkerson-algorithm-explanation/
[6] Max Flow Ford Fulkerson | Network Flow | Graph Theory https://youtube.com/watch?v=LdOnanfc5TM
[7] 15-451/651: Design & Analysis of Algorithms https://www.cs.cmu.edu/~15451-s23/lectures/lec11-flow1.pdf
[8] Maximum flow - Ford-Fulkerson and Edmonds-Karp¶ https://cp-algorithms.com/graph/edmonds_karp.html

By Perplexity at https://www.perplexity.ai/search/Depth-first-search-JdkKo16.QR.aXHpttbrQyw
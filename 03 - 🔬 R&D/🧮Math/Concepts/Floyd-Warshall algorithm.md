---
Date: [[2024-02-24]]
Tags: 
 - "#FloydWarshallAlgorithm"
 - "#Algorithms"
 - "#GraphTheory"
 - "#ShortestPath"
---

## Floyd-Warshall Algorithm

The Floyd-Warshall algorithm is a classic algorithm in computer science used for finding the shortest paths between all pairs of vertices in a weighted graph, which may include both positive and negative edge weights, but should not contain any negative cycles[1].

### How the Algorithm Works
- The algorithm uses a matrix to record distances between each pair of vertices and iteratively updates this matrix.
- Initially, the distance between each pair of vertices is set to the weight of the edge between them, or infinity if no edge exists.
- The algorithm then systematically checks whether a path that goes through an intermediate vertex offers a shorter path between any pair of vertices[1][2][3].

### Pseudocode
```plaintext
for k from 1 to V
  for i from 1 to V
    for j from 1 to V
      if distance[i][k] + distance[k][j] < distance[i][j]
        distance[i][j] = distance[i][k] + distance[k][j]
```

### Properties
- **Time Complexity**: $$ O(|V|^3) $$, where $$ |V| $$ is the number of vertices in the graph[1][2][3].
- **Space Complexity**: $$ O(|V|^2) $$, due to the distance matrix used to record shortest paths[1][2][3].

### Applications
- Finding shortest paths in directed graphs.
- Computing the transitive closure of directed graphs.
- Network routing and connectivity analysis[1][3][4].

### Limitations
- The algorithm cannot handle graphs with negative cycles, as these would lead to paths of arbitrarily small (negative) length[1].

### Example
Given a graph with vertices A, B, C, and D, the Floyd-Warshall algorithm can find the shortest path from each vertex to every other vertex, updating the distance matrix with the shortest path lengths[2][3].

### Conclusion
The Floyd-Warshall algorithm is a powerful tool for graph analysis, particularly useful for dense graphs where the number of edges is close to $$ |V|^2 $$[4].

- [[Floyd-Warshall algorithm]]
- [[Graph Theory]]
- [[Shortest Path Problem]]
- [[Dynamic Programming]]

Sources
[1] Floyd–Warshall algorithm - Wikipedia https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
[2] Floyd Warshall Algorithm https://www.tutorialspoint.com/data_structures_algorithms/floyd_warshall_algorithm.htm
[3] Comparison of Dijkstra’s and Floyd–Warshall algorithms - GeeksforGeeks https://www.geeksforgeeks.org/comparison-dijkstras-floyd-warshall-algorithms/
[4] Floyd-Warshall Algorithm - Scaler Topics https://www.scaler.com/topics/data-structures/floyd-warshall-algorithm/
[5] Floyd Warshall Algorithm https://blog.devgenius.io/floyd-warshall-algorithm-f004a01ae40e?gi=2e03cd1f5b6d
[6] Floyd Warshall Algorithm - GeeksforGeeks https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
[7] 407 Unauthorized http://www.cs.umd.edu/class/fall2021/cmsc351-0301/files/floydWarshall.pdf
[8] [Tutorial] The Floyd-Warshall algorithm and its generalizations - Codeforces https://codeforces.com/blog/entry/117814
[9] International Journal of Engineering Research and Technology. ISSN 0974-3154, Volume 12, Number 12 (2019), pp. 2529-2535 http://www.irphouse.com/ijert19/ijertv12n12_63.pdf
[10] Floyd Warshall Algorithm | Example | Time Complexity | Gate Vidyalay https://www.gatevidyalay.com/floyd-warshall-algorithm-shortest-path-algorithm/
[11] Floyd-Warshall Algorithm | Brilliant Math & Science Wiki https://brilliant.org/wiki/floyd-warshall-algorithm/
[12] Floyd Warshall algorithm with its Pseudo Code https://www.includehelp.com/algorithms/floyd-warshall-algorithm-with-its-pseudo-code.aspx
[13] Access Denied https://www.shiksha.com/online-courses/articles/about-floyd-warshall-algorithm/
[14] Understanding Floyd Warshall Algorithm: Advantages, Disadvantages, and Applications https://testbook.com/gate/floyd-warshall-algorithm-notes
[15] Floyd-Warshall Algorithm: Shortest Path Finding | Baeldung on Computer Science https://www.baeldung.com/cs/floyd-warshall-shortest-path
[16] Floyd-Warshall Algorithm https://algorithms.discrete.ma.tum.de/spp/floyd-warshall/
[17] DAA | Floyd-Warshall Algorithm - javatpoint https://www.javatpoint.com/floyd-warshall-algorithm
[18] Floyd Warshall Algorithm | Board Infinity https://www.boardinfinity.com/blog/floyd-warshall-algorithm/
[19] 4.2 All Pairs Shortest Path (Floyd-Warshall) - Dynamic Programming https://youtube.com/watch?v=oNI0rf2P9gE
[20] Floyd–Warshall algorithm in 4 minutes https://youtube.com/watch?v=4OQeCuLYj-4
[21] Floyd-Warshall Algorithm - GATE CSE Notes https://byjus.com/gate/floyd-warshall-algorithm-notes/
[22] Floyd-Warshall's Algorithm Explained and Implemented in Java | All Pairs Shortest Path | Geekific https://youtube.com/watch?v=gWRfc5wE8Jc
[23] Floyd-Warshall Algorithm https://www.programiz.com/dsa/floyd-warshall-algorithm
[24] Transitive closure of a graph using Floyd Warshall Algorithm - GeeksforGeeks https://www.geeksforgeeks.org/transitive-closure-of-a-graph/

By Perplexity at https://www.perplexity.ai/search/Depth-first-search-JdkKo16.QR.aXHpttbrQyw
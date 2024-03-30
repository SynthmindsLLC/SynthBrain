---
Date: [[2024-02-24]]
Tags: 
 - "#DijkstrasAlgorithm"
 - "#Algorithms"
 - "#GraphTheory"
 - "#ShortestPath"
---

## Dijkstra's Algorithm

Dijkstra's algorithm is a classic algorithm in computer science for finding the shortest paths between nodes in a weighted graph, which may represent road networks or other types of networks[1].

### How Dijkstra's Algorithm Works
- It starts at a selected node (the "source node") and explores all reachable nodes, calculating the shortest path to each node.
- The algorithm uses a priority queue to greedily select the next node with the smallest distance.
- Each node's distance is initially set to infinity, except for the source node, which is set to zero.
- As the algorithm progresses, it relaxes the edges, updating the shortest path to each node[1][2].

### Pseudocode
```plaintext
function Dijkstra(Graph, source):
    create vertex set Q

    for each vertex v in Graph:            
        dist[v] ← INFINITY                 
        prev[v] ← UNDEFINED                
        add v to Q                     
    dist[source] ← 0                       
    
    while Q is not empty:
        u ← vertex in Q with min dist[u]   
        remove u from Q 
         
        for each neighbor v of u:           
            alt ← dist[u] + length(u, v)
            if alt < dist[v]:              
                dist[v] ← alt 
                prev[v] ← u 

    return dist[], prev[]
```

### Properties
- **Time Complexity**: $$ O(|E| + |V|\log |V|) $$ when using a priority queue or heap for optimization[1].
- **Space Complexity**: $$ O(|V|) $$, where $$ |V| $$ is the number of vertices in the graph[4].

### Applications
- Dijkstra's algorithm is widely used in routing and navigation systems like GPS devices to find the shortest path between locations[7].
- It is also used in network routing protocols to find the shortest path for data packets[1].

### Limitations
- The algorithm assumes that all edge weights are non-negative because negative edge weights can lead to incorrect results[7].

### Example
Consider a graph with nodes A, B, C, D, and E, with edges between them having various weights. Dijkstra's algorithm can find the shortest path from node A to all other nodes, updating the tentative distances as it explores the graph[2][5].

### Conclusion
Dijkstra's algorithm is a powerful tool for finding the shortest path in weighted graphs and is a cornerstone of many applications in computer science and related fields.

- [[Dijkstra's algorithm]]
- [[Graph Theory]]
- [[Shortest Path Problem]]
- [[Priority Queue]]
- [[Greedy Algorithms]]

Sources
[1] Dijkstra's algorithm - Wikipedia https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
[2] Dijkstra's Algorithm – Explained with a Pseudocode Example https://www.freecodecamp.org/news/dijkstras-algorithm-explained-with-a-pseudocode-example/
[3] How Dijkstra's Algorithm Works https://youtube.com/watch?v=EFg3u_E6eHU
[4] Python Program for Dijkstra's shortest path algorithm | Greedy Algo-7 - GeeksforGeeks https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
[5] Dijkstra's algorithm in 3 minutes https://youtube.com/watch?v=_lHSawdgXpI
[6] Dijkstras Shortest Path Algorithm Explained | With Example | Graph Theory https://youtube.com/watch?v=bZkzH5x0SKU
[7] Dijkstra's Shortest Path Algorithm - A Detailed and Visual Introduction https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/

By Perplexity at https://www.perplexity.ai/search/Depth-first-search-JdkKo16.QR.aXHpttbrQyw
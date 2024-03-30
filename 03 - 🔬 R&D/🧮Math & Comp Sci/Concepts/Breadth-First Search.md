---
Date: [[2024-02-24]]
Tags: 
 - "#BreadthFirstSearch"
 - "#Algorithms"
 - "#GraphTraversal"
 - "#DataStructures"
---

## Breadth-First Search (BFS) Algorithm

Breadth-First Search (BFS) is a pivotal algorithm for traversing or searching tree and graph data structures. It operates on a simple principle: starting from a source node, it explores all neighboring nodes at the present depth before moving on to nodes at the next depth level[1][5][6][14][18][19].

### How BFS Works
- BFS begins at a source node and examines all its neighbors. Then, it proceeds to their neighbors, which haven't been visited, and continues this process until all nodes are explored[1][5][6].
- A queue is used to keep track of the nodes to visit next, adhering to a First-In-First-Out (FIFO) order[5][6][18][19].
- Nodes are marked as visited to prevent revisiting them, which could lead to an infinite loop[1][5][14][18].

### Pseudocode
```plaintext
BFS(G, s):
    create a queue Q
    enqueue s onto Q
    mark s as visited
    while Q is not empty:
        t = Q.dequeue()
        for all neighbors v of t in Graph G:
            if v is not visited:
                enqueue v onto Q
                mark v as visited
```

### Properties
- **Completeness**: BFS is complete, meaning it will find a solution if one exists[3][6].
- **Optimality**: BFS is optimal for unweighted graphs, guaranteeing the shortest path from the source node to any other node[6][18][19].
- **Time Complexity**: $$ O(|V| + |E|) $$, where $$ |V| $$ is the number of vertices and $$ |E| $$ is the number of edges in the graph[6][14][18].
- **Space Complexity**: $$ O(|V|) $$, as it needs to store all vertices in the worst case[6][14][18].

### Applications
- BFS is used for finding the shortest path in unweighted graphs, testing graph bipartiteness, finding connected components, and more[5][6][14][18].

### Implementation Considerations
- **Graph Representation**: BFS can be implemented using adjacency lists or adjacency matrices[11][14].
- **Path Reconstruction**: To reconstruct paths, BFS can keep track of the predecessors of each node[19].

### Example
Consider a graph with vertices labeled from A to E. BFS starts at vertex A, visits its neighbors B and C, then visits the neighbors of B and C, and so on until all vertices are visited[21].

### Conclusion
BFS is a robust and versatile algorithm essential for various applications in computer science, including networking, social network analysis, and web crawling[17].

- [[Breadth-First Search]]
- [[Graph Theory]]
- [[🗺 Algorithms]]
- [[Data Structures]]
- [[Queue]]

Sources
[1] Breadth First Search or BFS for a Graph - GeeksforGeeks https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
[2] Pseudocode to find cycles in a graph using breadth first search https://stackoverflow.com/questions/4464336/pseudocode-to-find-cycles-in-a-graph-using-breadth-first-search
[3] results matching " " https://ai-master.gitbooks.io/classic-search/content/the-property-of-breadth-first-search.html
[4] Breadth-first search (BFS) https://algowiki-project.org/en/Breadth-first_search_(BFS)
[5] Breadth First Search (BFS) Algorithm with EXAMPLE https://www.guru99.com/breadth-first-search-bfs-graph-example.html
[6] Breadth-first search - Wikipedia https://en.wikipedia.org/wiki/Breadth-first_search
[7] What does pi mean in this BFS algorithm pseudocode? https://softwareengineering.stackexchange.com/questions/287017/what-does-pi-mean-in-this-bfs-algorithm-pseudocode
[8] Difference between BFS and DFS - GeeksforGeeks https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/
[9] Implementing a BFS-search method for a graph https://stackoverflow.com/questions/71280614/implementing-a-bfs-search-method-for-a-graph
[10] Breadth First Vs Depth First https://stackoverflow.com/questions/687731/breadth-first-vs-depth-first
[11] Breadth First Search Algorithm Tutorial | BFS Algorithm | Edureka https://www.edureka.co/blog/breadth-first-search-algorithm/
[12] Chapter 14 https://www.cs.cmu.edu/afs/cs/academic/class/15210-s15/www/lectures/bfs-notes.pdf
[13] An adaptive breadth-first search algorithm on integrated architectures https://www.researchgate.net/publication/326980080_An_adaptive_breadth-first_search_algorithm_on_integrated_architectures
[14] Breadth first search https://www.programiz.com/dsa/graph-bfs
[15] What is Breadth First Search Algorithm in Data Structure? Overview with Examples https://www.simplilearn.com/tutorials/data-structure-tutorial/bfs-algorithm
[16] ICS 161: Design and Analysis of Algorithms Lecture notes for February 15, 1996 https://ics.uci.edu/~eppstein/161/960215.html
[17] BFS: Breadth First Search Implementation in Python - Pierian Training https://pieriantraining.com/bfs-breadth-first-search-implementation-in-python/
[18] Breadth First Search Tutorials & Notes | Algorithms | HackerEarth https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
[19] The breadth-first search algorithm (BFS) (article) | Khan Academy https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/the-breadth-first-search-algorithm
[20] A* or Bidirectional Breadth First Search? https://stackoverflow.com/questions/49602553/a-or-bidirectional-breadth-first-search
[21] Breadth-first search in 4 minutes https://youtube.com/watch?v=HZ5YTanv5QE
[22] Breadth First Search Algorithm | Shortest Path | Graph Theory https://youtube.com/watch?v=oDqjPvD54Ss

By Perplexity at https://www.perplexity.ai/search/Depth-first-search-JdkKo16.QR.aXHpttbrQyw
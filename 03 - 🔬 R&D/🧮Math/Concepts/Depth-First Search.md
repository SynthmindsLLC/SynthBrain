---
Date: [[2024-02-24]]
Tags: 
 - "#DepthFirstSearch"
 - "#Algorithms"
 - "#GraphTraversal"
 - "#DataStructures"
---

## Depth-First Search (DFS) Algorithm

Depth-First Search (DFS) is a fundamental recursive algorithm used to explore nodes and edges of a graph. It starts at a selected node (often referred to as the 'root') and explores as far as possible along each branch before backtracking.

### How DFS Works
- DFS begins at the root node and explores as deep as possible along each branch before backtracking.
- A stack (often the program's call stack via recursion) is used to remember the path taken and to backtrack.
- Nodes are marked as visited to avoid revisiting them and potentially getting into infinite loops[1][2][13].

### Pseudocode
Here is a simple recursive pseudocode for DFS:

```plaintext
DFS(G, v):
    mark v as visited
    for each neighbor u of v in Graph G:
        if u is not visited:
            DFS(G, u)
```

### Properties
- **Time Complexity**: $$ O(|V| + |E|) $$, where $$ |V| $$ is the number of vertices and $$ |E| $$ is the number of edges in the graph[3][7][17].
- **Space Complexity**: $$ O(|V|) $$ due to the stack used for recursion[17].
- **Applications**: DFS is used in various applications such as topological sorting, finding connected components, and solving puzzles like mazes[4][12][17].

### Implementation Considerations
- **Graph Representation**: DFS can be implemented using adjacency lists (more space-efficient for sparse graphs) or adjacency matrices (simpler but less space-efficient for sparse graphs)[8][11].
- **Recursive vs Iterative**: DFS can be implemented recursively (simpler) or iteratively (using an explicit stack)[6][9].
- **Edge Classification**: During DFS, edges can be classified as tree edges, back edges, forward edges, or cross edges, which can be useful in detecting cycles and other properties[13].

### Example
Consider a graph with vertices labeled from 0 to 4. DFS starts at vertex 0, visits its neighbors, and continues this process recursively until all vertices reachable from 0 are visited[9].

### Code Example
Here is a simple implementation of DFS in C++:

```cpp
#include <iostream>
#include <list>
#include <vector>
using namespace std;

class Graph {
    int V;
    list<int> *adj;
    void DFSUtil(int v, vector<bool> &visited) {
        visited[v] = true;
        cout << v << " ";
        for (auto i = adj[v].begin(); i != adj[v].end(); ++i)
            if (!visited[*i])
                DFSUtil(*i, visited);
    }
public:
    Graph(int V) {
        this->V = V;
        adj = new list<int>[V];
    }
    void addEdge(int v, int w) {
        adj[v].push_back(w);
    }
    void DFS(int v) {
        vector<bool> visited(V, false);
        DFSUtil(v, visited);
    }
};

int main() {
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    cout << "Following is Depth First Traversal (starting from vertex 0) \n";
    g.DFS(0);
    return 0;
}
```

### Conclusion
DFS is a powerful tool for graph traversal that can be adapted for various applications in computer science and related fields.

- [[Depth-First Search]]
- [[Graph Theory]]
- [[🗺 Algorithms]]
- [[Data Structures]]
- [[Recursion]]
- [[Stack]]

Sources
[1] What Is DFS (Depth-First Search): Types, Complexity & More | Simplilearn https://www.simplilearn.com/tutorials/data-structure-tutorial/dfs-algorithm
[2] Depth-first search (DFS) http://www.cs.toronto.edu/~heap/270F02/node36.html
[3] Why is the time complexity of both DFS and BFS O( V + E ) https://stackoverflow.com/questions/11468621/why-is-the-time-complexity-of-both-dfs-and-bfs-o-v-e
[4] Applications, Advantages and Disadvantages of Depth First Search (DFS) - GeeksforGeeks https://www.geeksforgeeks.org/applications-of-depth-first-search/
[5] Depth First Search (DFS) Explained: Algorithm, Examples, and Code https://youtube.com/watch?v=PMMc4VsIacU
[6] How to Nail your next Technical Interview https://www.interviewkickstart.com/learn/depth-first-search-algorithm
[7] Why is the complexity of both BFS and DFS O(V+E)? - GeeksforGeeks https://www.geeksforgeeks.org/why-is-the-complexity-of-both-bfs-and-dfs-ove/
[8] DFS Algorithm - javatpoint https://www.javatpoint.com/depth-first-search-algorithm
[9] Depth First Search or DFS for a Graph - GeeksforGeeks https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
[10] Depth first search (DFS) vs breadth first search (BFS) pseudocode and complexity https://stackoverflow.com/questions/67528549/depth-first-search-dfs-vs-breadth-first-search-bfs-pseudocode-and-complexity
[11] DFS https://www.thealgorists.com/Algo/DFS
[12] Applications of Depth First Search - FACE Prep https://www.faceprep.in/data-structures/applications-of-depth-first-search/
[13] Depth-first search - Wikipedia https://en.wikipedia.org/wiki/Depth-first_search
[14] Breadth First Vs Depth First https://stackoverflow.com/questions/687731/breadth-first-vs-depth-first
[15] Educative Answers - Trusted Answers to Developer Questions https://www.educative.io/answers/what-is-depth-first-search
[16] Depth-first search in 4 minutes https://youtube.com/watch?v=Urx87-NMm6c
[17] Depth First Search - Data Structures Handbook https://www.thedshandbook.com/depth-first-search/
[18] Depth First Search Tutorials & Notes | Algorithms | HackerEarth https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/
[19] Depth First Search (DFS) https://www.programiz.com/dsa/graph-dfs

By Perplexity at https://www.perplexity.ai/search/Depth-first-search-JdkKo16.QR.aXHpttbrQyw
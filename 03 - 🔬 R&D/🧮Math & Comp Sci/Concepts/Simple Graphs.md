---
Date: [[2024-03-30]]
Tags: 
 - "#graph_theory"
 - "#simple_graphs"
 - "#discrete_mathematics"
---

Simple graphs are a fundamental concept in discrete mathematics, particularly within the field of graph theory. A simple graph is defined as an unweighted, undirected graph containing no graph loops or multiple edges between any two vertices[4]. This means that in a simple graph, each pair of vertices is connected by at most one edge, and there are no edges that connect a vertex to itself. Simple graphs can be either connected or disconnected. Unless specified otherwise, the term "graph" usually refers to a simple graph[4].

## Definition
A simple graph $$G$$ is an ordered pair $$G = (V, E)$$ where[5]:
- $$V$$ is a set of elements called vertices or nodes.
- $$E$$ is a set of unordered pairs of vertices, called edges.

The vertices $$u$$ and $$v$$ of an edge $$\{u, v\}$$ are called the edge's endpoints. The edge is said to join $$u$$ and $$v$$ and to be incident on them. A vertex may belong to no edge, in which case it is not joined to any other vertex and is called isolated[12].

## Properties
Simple graphs have several important properties and concepts associated with them, including[1][2][7]:
- **Adjacency**: Two vertices are adjacent if there is an edge connecting them. Similarly, two edges are adjacent if they share a common vertex.
- **Degree of a Vertex**: The degree of a vertex is the number of edges incident with that vertex. In a simple graph, this is equivalent to the number of adjacent vertices.
- **Path and Cycle**: A path in a simple graph is a sequence of vertices where each adjacent pair is connected by an edge. A cycle is a path that starts and ends at the same vertex, without repeating any edges or vertices.
- **Connectedness**: A simple graph is connected if there is a path between every pair of vertices. Otherwise, it is disconnected and may consist of two or more connected components.

## Types
Simple graphs can be categorized into several types based on specific characteristics[3][16]:
- **Complete Graph**: A simple graph in which every pair of distinct vertices is connected by a unique edge.
- **Cycle Graph**: A simple graph that consists of a single cycle.
- **Path Graph**: A simple graph that forms a simple path.
- **Empty Graph**: A graph with vertices but no edges.

## Applications
Simple graphs are used to model relationships and structures in various fields such as computer science, biology, social sciences, and more. They are particularly useful in representing networks where binary relationships exist between entities, such as social networks, communication networks, and transportation systems[6][8][9][11].

- **Social Networks**: Representing individuals as vertices and their relationships as edges.
- **Transportation Networks**: Modeling locations as vertices and routes between them as edges.
- **Computer Networks**: Depicting devices as vertices and connections between devices as edges.

Simple graphs provide a foundational framework for studying more complex types of graphs and for developing algorithms to solve various problems in graph theory, such as finding the shortest path, detecting cycles, and graph coloring[14].

Citations:
[1] https://en.wikipedia.org/wiki/Graph_property
[2] https://www.setzeus.com/community-blog-posts/graph-theory-basic-properties
[3] https://www.geeksforgeeks.org/graph-types-and-applications/
[4] https://mathworld.wolfram.com/SimpleGraph.html
[5] https://proofwiki.org/wiki/Definition:Simple_Graph
[6] https://www.geeksforgeeks.org/applications-of-graph-data-structure/
[7] https://www.people.vcu.edu/~gasmerom/MAT131/graphs.html
[8] https://www.xomnia.com/post/graph-theory-and-its-uses-with-examples-of-real-life-problems/
[9] https://www.masaischool.com/blog/applications-of-graph-data-structure/
[10] https://courses.engr.illinois.edu/cs473/sp2009/notes/14-graphs.pdf
[11] https://www.prepbytes.com/blog/graphs/applications-of-graphs-in-data-structures/
[12] https://en.wikipedia.org/wiki/Graph_%28discrete_mathematics%29
[13] https://www.cs.yale.edu/homes/aspnes/pinewiki/GraphTheory.html
[14] https://memgraph.com/blog/graph-algorithms-applications
[15] https://www.tutorialspoint.com/graph_theory/types_of_graphs.htm
[16] https://www.whitman.edu/mathematics/cgt_online/book/section05.01.html
[17] https://byjus.com/gate/graph-and-its-applications/
[18] https://byjus.com/maths/graph-theory/
[19] https://www.linkedin.com/pulse/graph-theory-101-part3-rajib-rajkhowa
---
Date: [[2024-03-30]]
Tags: 
 - "#graph_theory"
 - "#multigraphs"
 - "#discrete_mathematics"
---

Multigraphs are a type of graph in graph theory, which is a key area of study within discrete mathematics. A multigraph differs from a simple graph in that it permits multiple edges (also known as parallel edges) between the same set of vertices. This means that two nodes in a multigraph can be connected by more than one edge, which is not allowed in simple graphs. Additionally, multigraphs may contain loops, which are edges that connect a vertex to itself.

## Definition
A multigraph $$G$$ is defined as a pair $$G = (V, E)$$ where:
- $$V$$ is a set of vertices or nodes.
- $$E$$ is a multiset of unordered pairs of vertices for undirected multigraphs, or ordered pairs for directed multigraphs, known as edges.

In a multigraph, two vertices can be connected by multiple distinct edges, each representing a different relationship or connection between the same entities.

## Properties
Multigraphs have unique properties that distinguish them from simple graphs:
- **Parallel Edges**: The presence of multiple edges between the same pair of vertices.
- **Loops**: Edges that connect a vertex to itself.
- **Degree of a Vertex**: In a multigraph, the degree of a vertex is the number of edges incident to it, with loops being counted twice.

## Types
Multigraphs can be either directed or undirected:
- **Directed Multigraph (Multidigraph)**: A graph where multiple directed edges can exist between the same set of vertices.
- **Undirected Multigraph**: A graph where multiple undirected edges can exist between the same set of vertices.

## Applications
Multigraphs are used to model scenarios where relationships between entities can have multiple dimensions or where multiple distinct connections can exist:
- **Transportation Networks**: Representing multiple routes or types of transportation between the same locations.
- **Biological Networks**: Modeling multiple types of interactions between biological entities, such as genes or proteins.
- **Social Networks**: Capturing different types of relationships or interactions between individuals or groups.

Multigraphs are particularly useful in network design and analysis, where the complexity of relationships cannot be captured by a single edge. They allow for a more nuanced representation of real-world systems and are essential for algorithms that need to account for multiple types of connections or interactions.
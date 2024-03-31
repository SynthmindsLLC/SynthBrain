---
Date: [[2024-03-30]]
Tags: 
 - "#graph_theory"
 - "#weighted_graphs"
 - "#discrete_mathematics"
---

Weighted graphs are a significant concept in graph theory, which is a branch of discrete mathematics. Unlike simple graphs, which do not assign any value to their edges, weighted graphs attach a weight or cost to each edge. These weights can represent various quantities depending on the application, such as distance, time, capacity, or cost. Weighted graphs can be either directed or undirected, and the weights can be positive, negative, or zero.

## Definition
A weighted graph $$G$$ is defined as a triple $$G = (V, E, w)$$ where:
- $$V$$ is a set of vertices or nodes.
- $$E$$ is a set of edges, which are pairs of vertices.
- $$w$$ is a weight function $$w: E \rightarrow \mathbb{R}$$ that assigns a real number (the weight) to each edge in $$E$$.

In a weighted graph, each edge $$\{u, v\}$$ or $$(u, v)$$ in the case of directed graphs, is associated with a weight $$w(u, v)$$.

## Properties
Weighted graphs introduce the concept of edge weight, which adds complexity and richness to the graph's structure and the problems that can be solved:
- **Edge Weight**: The weight of an edge can represent various metrics such as distance, cost, or time. The interpretation of the weight depends on the specific application of the graph.
- **Path Weight**: The weight of a path in a weighted graph is typically the sum of the weights of the edges that compose the path. This allows for the consideration of the "cost" of a path, not just its length.
- **Minimum Spanning Tree**: A key problem in weighted graphs is finding a minimum spanning tree, which is a subset of the edges that connects all vertices with the minimum possible total edge weight.

## Types
Weighted graphs can be categorized based on their directedness and the nature of their weights:
- **Directed Weighted Graph**: A graph where the edges have a direction and a weight. The weight of an edge may differ depending on its direction.
- **Undirected Weighted Graph**: A graph where the edges have no direction but have a weight. The weight is the same regardless of the direction of traversal.
- **Positive Weighted Graph**: A graph where all edge weights are positive.
- **Negative Weighted Graph**: A graph that includes some edges with negative weights, often used in applications like financial modeling.

## Applications
Weighted graphs are widely used in various fields to model systems where the connections between entities have an associated cost or value:
- **Transportation Networks**: Modeling roads or flight routes with distances or travel times as weights.
- **Telecommunication Networks**: Representing connections between nodes with bandwidths or latencies as weights.
- **Financial Networks**: Modeling financial transactions or relationships where the weights can represent transaction amounts or costs.

Weighted graphs are crucial for solving many practical problems in computer science, operations research, and engineering, such as shortest path problems, network flow problems, and optimization problems. Algorithms designed for weighted graphs, like Dijkstra's algorithm for shortest paths, take into account the weights of the edges to provide solutions that minimize or maximize certain criteria.
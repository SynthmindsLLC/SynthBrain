---
title: "Adjacency Matrix in Graph Theory"
description: "A square matrix used to represent a finite graph, indicating whether pairs of vertices are adjacent."
type: "concept"
tags:
- "Graph_Theory"
- "Linear_Algebra"
- "Data_Structures"
relationships:
- "#related_to [[Graph Theory]]"
- "#part_of [[Matrix Representation]]"
- "#used_for [[Representing Graphs in Memory]]"
- "#has_property [[Square Matrix]]"
- "#applies_to [[Finite Graphs]]"
- "#related_to [[Graph Properties]], [[Algorithm Efficiency]]"
start_date: "2024-03-31"
---

# Adjacency Matrix in Graph Theory

An adjacency matrix is a square matrix used to represent a finite graph. The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.

## Definition and Representation

- **Matrix Elements**: For a graph with $$ n $$ vertices, the adjacency matrix is an $$ n \times n $$ matrix where the element $$ a_{ij} $$ is one when there is an edge from vertex $$ i $$ to vertex $$ j $$, and zero when there is no edge.
- **Undirected Graphs**: In an undirected graph, the adjacency matrix is symmetric because the edge $$ (i, j) $$ is identical to the edge $$ (j, i) $$.
- **Directed Graphs**: For directed graphs, the adjacency matrix need not be symmetric as the presence of an edge from $$ i $$ to $$ j $$ does not imply the presence of an edge from $$ j $$ to $$ i $$.

## Properties and Applications

- **Graph Properties**: The adjacency matrix can be used to determine various graph properties, such as finding the number of paths of a certain length between two vertices by raising the matrix to a power.
- **Spectral Graph Theory**: The eigenvalues of the adjacency matrix (known as the graph's spectrum) can reveal information about the graph's structure, such as its connectivity and stability.
- **Data Structures**: In computer science, adjacency matrices serve as a data structure for representing graphs in memory.

## Computational Aspects

- **Space Complexity**: The space complexity of an adjacency matrix is $$ O(n^2) $$, which can be inefficient for sparse graphs with far fewer than $$ n^2 $$ edges.
- **Algorithm Efficiency**: Algorithms that involve matrix operations, such as finding transitive closure or shortest paths, can be efficiently implemented using adjacency matrices.

## Advantages and Limitations

- **Advantages**: Adjacency matrices provide a simple and direct representation for graphs, and they are well-suited for dense graphs and for operations that require matrix algebra.
- **Limitations**: For sparse graphs, adjacency matrices can be space-inefficient compared to other representations like adjacency lists.

Adjacency matrices are a fundamental tool in graph theory and linear algebra, providing a bridge between these two areas of mathematics and enabling the application of matrix operations to solve graph-related problems.

- Important [[wikilinks]]: [[Graph Theory]], [[Linear Algebra]], [[Spectral Graph Theory]], [[Data Structures]], [[Algorithm Efficiency]]

Sources
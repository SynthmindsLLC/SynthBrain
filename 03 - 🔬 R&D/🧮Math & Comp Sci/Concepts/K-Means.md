---
title: "K-means Clustering Algorithm"
description: "A popular clustering algorithm used in machine learning and data mining to partition observations into clusters based on the nearest mean. It works by initializing centroids, assigning points to the nearest centroid, updating centroids as means of assigned points, and repeating until convergence. Despite limitations like needing a predefined number of clusters and assuming spherical shapes, it's efficient for large datasets and useful in exploratory data analysis."
type: "algorithm"
tags:
- "Machine Learning"
- "Data Mining"
- "Clustering Algorithms"
relationships:
- "#part_of [[Unsupervised Learning]]"
- "#used_for [[Exploratory Data Analysis]]"
- "#related_to [[Voronoi Cells]], [[Euclidean Distance]]"
start_date: "2024-03-06"
---

K-means is a popular clustering algorithm used in machine learning and data mining to partition $$ n $$ observations into $$ k $$ clusters in which each observation belongs to the cluster with the nearest mean. This results in a partitioning of the data space into Voronoi cells.

The algorithm works as follows:

1. **Initialization**: Choose $$ k $$ initial centroids (either randomly or based on some heuristic).

2. **Assignment step**: Assign each data point to the nearest centroid. The "nearest" is usually determined by the Euclidean distance between the point and the centroid.

3. **Update step**: Calculate the new centroids as the mean of all points assigned to each cluster.

4. **Repeat**: Alternate between the assignment and update steps until the centroids no longer change significantly, indicating convergence.

K-means is simple and can be very efficient on large datasets. However, it has several limitations:

- The number of clusters $$ k $$ must be specified in advance.
- It assumes clusters are spherical and equally sized, which may not be the case.
- It is sensitive to the initial choice of centroids.
- It can converge to local optima, so it's common to run the algorithm multiple times with different initializations.

Despite these limitations, k-means is widely used for exploratory data analysis and as a preprocessing step for other algorithms.

- Important [[wikilinks]]:
  - [[Clustering Algorithms]]
  - [[Euclidean Distance]]
  - [[Voronoi Cells]]
  - [[Convergence in Algorithms]]
  - [[Exploratory Data Analysis]]

Sources
---
Date: [[2024-03-06]]
Tags: 
 - "#collaborative_filtering"
 - "#recommender_systems"
 - "#machine_learning"
 - "#user_preferences"
---

Collaborative filtering is a method used by recommender systems to predict the preferences of a user by collecting preferences from many users (collaborating). The underlying assumption is that if a person A has the same opinion as a person B on an issue, A is more likely to have B's opinion on a different issue than that of a random person.

There are two main types of collaborative filtering:

1. **User-based**: This approach finds users similar to the target user (neighbors) based on rating history and predicts new items based on the neighbors' preferences. The similarity between users can be calculated using measures like cosine similarity, Pearson correlation, or adjusted cosine similarity.

2. **Item-based**: Instead of finding similar users, this method finds similar items based on the item rating patterns across users. It then recommends items that are similar to those the target user has liked in the past.

Collaborative filtering can be implemented using various techniques, including matrix factorization, which has become popular due to its scalability and ability to deal with sparse datasets. However, collaborative filtering faces challenges such as the cold start problem, where new users or items have insufficient data to make accurate recommendations, and the issue of data sparsity in large datasets.

Despite these challenges, collaborative filtering is widely used in various domains, such as e-commerce, online streaming services, and social networking services, to enhance user experience by personalizing content recommendations.

- Important [[wikilinks]]:
  - [[Recommender Systems]]
  - [[User-Based Collaborative Filtering]]
  - [[Item-Based Collaborative Filtering]]
  - [[Matrix Factorization]]
  - [[Cosine Similarity]]
  - [[Pearson Correlation]]

Sources

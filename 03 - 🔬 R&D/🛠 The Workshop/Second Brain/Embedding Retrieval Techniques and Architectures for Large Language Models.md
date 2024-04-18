---
Title: Embedding Retrieval Techniques and Architectures for Large Language Models
Description: An overview of key embedding-based retrieval techniques and architectures used in modern recommendation systems and large language models, including two-tower models, composite embeddings, and hypothetical document embeddings.
Date: 2023-04-12
Tags:
 - "#embeddingretrieval"
 - "#recommendationsystems"
 - "#largelanguagemodels"
 - "#twotowermodels"
 - "#compositeembeddings"
 - "#hypotheticaldocumentembeddings" 
---

Embedding-based retrieval is a powerful technique used in modern recommendation systems and large language models to efficiently retrieve relevant items or documents. Here are some key techniques and architectures:

## Two-Tower Models
- Uses separate neural network towers to produce embeddings for queries and candidate items[2]
- Enables decoupling of query and candidate inference for faster retrieval
- Similarity is determined by calculating dot product between query and candidate embeddings
- Widely used at Google for deep retrieval in Search, YouTube, Ads, etc.[2]

## Composite and Multi-Task Learning Models
- LinkedIn supports creating composite models that consolidate various objectives into one[4]
- Allows learning of generalized embeddings that capture multiple aspects
- Speeds up learning process and enhances transfer learning
- Embeddings can capture user interests to personalize search and recommendations[4]

## Hypothetical Document Embeddings 
- Generates a hypothetical contextual document embedding that may contain false details but is semantically relevant[5]
- Allows retrieval of more varied results from datastore
- Increases chances of completion model generating factual and relevant information

## Embedding-Based Retrieval Architectures
- LinkedIn's Feature Cloud merges offline and real-time embedding generation[4]
- Vertex AI offers managed two-tower model training and deployment[2]
- GPT Index utilizes data structures optimized for language models[5]
- Pinecone and ScaNN provide vector databases for efficient similarity search over embeddings[2][3]

By leveraging techniques like two-tower models, composite embeddings, and hypothetical document embeddings, along with purpose-built architectures and tools, embedding-based retrieval can significantly improve the relevance, personalization, and efficiency of recommendation systems and large language models.

## List of Relevant Backlinks
- [[Recommendation Systems]]
- [[Language Model Architectures]]
- [[Vector Databases]] 
- [[Semantic Search]]

Sources
[1] Embedding-based Retrieval at Scribd https://tech.scribd.com/blog/2021/embedding-based-retrieval-scribd.html
[2] Tensorflow deep retrieval using Two Towers architecture - Google Cloud https://cloud.google.com/blog/products/ai-machine-learning/scaling-deep-retrieval-tensorflow-two-towers-architecture
[3] Embedding Methods for Image Search - Pinecone https://www.pinecone.io/learn/series/image-search/
[4] Inside LinkedIn's Embedding Architecture Powering its Job ... https://pub.towardsai.net/inside-linkedins-embedding-architecture-powering-its-job-search-capabilities-d4dd61e8089b?gi=85c01308be33
[5] Knowledge Retrieval Architecture for LLM's (2023) - Matt Boegner https://mattboegner.com/knowledge-retrieval-architecture-for-llms/

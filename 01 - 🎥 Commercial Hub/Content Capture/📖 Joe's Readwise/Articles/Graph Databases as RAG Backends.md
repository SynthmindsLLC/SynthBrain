# Graph Databases as RAG Backends

![rw-book-cover](https://tomoro.ai/images/graph-databases-as-rag-backends-cover.png)

## Metadata
- Author: [[tomoro.ai]]
- Full Title: Graph Databases as RAG Backends
- Category: #articles
- URL: https://tomoro.ai/insights/graph-databases-as-rag-backends

## Highlights
- The most common implementation of the RAG pattern involves using vector databases as the backend. ([View Highlight](https://read.readwise.io/read/01hjgwrqtmgctzfdak8dqst13c))
- we found that when dealing with a large data source with complex unstructured documents graph databases tend to outperform vector database-based RAG in some surprising ways. ([View Highlight](https://read.readwise.io/read/01hjgws1vej45de2bhqv47w5wy))
- Reduced hallucinations due to improved recall ([View Highlight](https://read.readwise.io/read/01hjgwsmqxb3fmxfdjxqdhrs6a))
- Using a graph database as a backend allows increased granularity and allows the capture data at fact-level ([View Highlight](https://read.readwise.io/read/01hjgwswxe13ph9vhzyj5z1hnp))
- entity-level" data ownership.
  This technique simplifies operational management and reduces complexity in data management processes. Additionally, it incorporates a time dimension and decay factor for recency metrics during the data retrieval phase. ([View Highlight](https://read.readwise.io/read/01hjgwtg1esq38yt6g5ztas1k5))
- Using graph databases as RAG backed allows opportunities to actively mine for inferences based on knowledge already held in the corpus. This boosts answer quality at the generation stage. ([View Highlight](https://read.readwise.io/read/01hjgwv2c191n1e34xhgz4vytn))
- In traditional RAG implementations, the knowledge corpus is processed through an embedding model and the resulting output is stored in (typically) a vector store. ([View Highlight](https://read.readwise.io/read/01hjgww2wfe4zs04rb70vjmt4e))
- At retrieval time, the user question is processed through an embedding model and, using a similarity algorithm (e.g. cosine similarity), the “distance” between the user question and data chunks in vector databases is calculated. The chunks closest to the user question are deemed to be relevant to the question and retrieved. Then used as context to answer the question. ([View Highlight](https://read.readwise.io/read/01hjgwwkn93j3jsprq191cbtgw))
- These knowledge chunks, along with the original question and accompanying context, are wrapped around a system prompt and sent to a foundational model to generate an appropriate response. ([View Highlight](https://read.readwise.io/read/01hjgwwy2mzjf6fshthfekffw9))
- it tends to perform sub-optimally when solving knowledge management applications at scale. ([View Highlight](https://read.readwise.io/read/01hjgwxbj1neaqpdp1yrqyfqp6))
- Vector databases are designed from the ground up to store and perform operations on vectors (outputs from embedding models). This allows them to perform similarity calculations and retrieve relevant documents quickly and efficiently. ([View Highlight](https://read.readwise.io/read/01hjgwxqkvgdjxa594nbkk20bv))
- the embeddings will match the user query semantically rather than specific keywords. ([View Highlight](https://read.readwise.io/read/01hjgwy64d84q3mbeg5a4py2a4))
- this still means that the search for relevant knowledge is restricted to the granularity of the document chunks. If the context relevant to a question is present across multiple chunks, then all such chunks must be retrieved and sent to the foundational model for a reasonable response. ([View Highlight](https://read.readwise.io/read/01hjgwyh58jyv6y7ja8ddjkfn1))
- In the real world, a knowledge corpus often consists of documents that discuss multiple topics and the relationships between them in a single document. This means that the information about an entity is often spread across multiple document chunks and across documents throughout the corpus. ([View Highlight](https://read.readwise.io/read/01hjgwywt3mhz8ggm3fgt0nyj3))
- An alternative approach is to pre-process the knowledge corpus and, instead of keeping the information tightly connected with the document, re-organise information along core concepts. ([View Highlight](https://read.readwise.io/read/01hjgwz7kahbsd1sfgvqzbw6d5))
- **key entities are extracted from source documents and the facts mentioned in the document are represented as edges connecting the entities.** These edges can also store operational metadata about the source document for easy citation of the facts. ([View Highlight](https://read.readwise.io/read/01hjgwzm0xwrz234k5vnt8tec0))
- All known facts about the given entity **from across the knowledge corpus** will be present in the neighbourhood of this node of the graph, implemented as edges. ([View Highlight](https://read.readwise.io/read/01hjgwzzqbbr41s1qfyfy2zzy2))
- Our retriever will selectively traverse outwards from the key entities to gather relevant context to satisfy the requirements of the user query and relevant context without being bound by the limitations of the original document chunks. ([View Highlight](https://read.readwise.io/read/01hjgx06tjmchre3ye68z11r5e))
- Using this approach the original document source is decomposed into independent entities and discreet facts connected to entities, the granularity of data is significantly increased. ([View Highlight](https://read.readwise.io/read/01hjgx0fatmp4jnq4dhj80vd55))

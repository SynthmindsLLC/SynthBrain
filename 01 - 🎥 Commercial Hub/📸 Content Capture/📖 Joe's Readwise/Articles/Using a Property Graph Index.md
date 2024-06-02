# Using a Property Graph Index

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)

## Metadata
- Author: [[llamaindex.ai]]
- Date: None
- Full Title: Using a Property Graph Index
- Category: #articles
- Summary: The Property Graph Index in LlamaIndex helps with constructing and querying property graphs for knowledge collection. It offers various retrievers for node and path retrieval, and allows for customization through extractors and retrievers. The index supports storage with options like saving to disk and using different graph stores like Neo4j.
- URL: https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/

## Highlights
- A property graph is a knowledge collection of labeled nodes (i.e. entity categories, text labels, etc.) with properties (i.e. metadata), linked together by relationships into structured paths. ([View Highlight](https://read.readwise.io/read/01hz9nz4y96nbeqdrq7cx37wxy))
- Property graph construction in LlamaIndex works by performing a series of `kg_extractors` on each chunk, and attaching entities and relations as metadata to each llama-index node. You can use as many as you like here, and they will all get applied.
  If you've used transformations or metadata extractors with the [ingestion pipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/), then this will be very familiar (and these `kg_extractors` are compatible with the ingestion pipeline)! ([View Highlight](https://read.readwise.io/read/01hz9nzx09r2djnhb6ntabpccv))

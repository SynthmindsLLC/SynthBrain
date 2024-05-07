# GraphRAG: LLM-Derived Knowledge Graphs for RAG

![rw-book-cover](https://i.ytimg.com/vi/r09tJfON6kE/maxresdefault.jpg)

## Metadata
- Author: [[Alex Chao]]
- Date: 2024-05-04
- Full Title: GraphRAG: LLM-Derived Knowledge Graphs for RAG
- Category: #articles
- Summary: The text discusses GraphRAG, a tool that utilizes knowledge graphs derived from LLM to enhance search relevancy and enable new scenarios in data analysis. By creating knowledge graphs from data sets, GraphRAG allows for granular semantic topic exploration and facilitates various analytical methods like data summarization and Q&A. The tool provides a holistic understanding of data by organizing entities into semantic topics and improving the accuracy of answers.
- URL: https://youtube.com/watch?v=r09tJfON6kE&si=zJqyfEOtwT_sOmdd

## Highlights
- graph rag is really a
  two-step process it is first an indexing process that's run over top of private data to create llm derived knowledge graphs these knowledge graphs serve as a form of an llm memory representation which can then be used by subsequent steps to then do better retrieval ([View Highlight](https://read.readwise.io/read/01hx97xgz80n4v2zdf50ynq7j1))
- llm orchestration mechanism that utilizes those pre-built indices that I just talked about and then those indices can be used to construct much much better more
  empowered rag operations ([View Highlight](https://read.readwise.io/read/01hx97xzfr0mx8jhg7w2c8ex73))
- allows us to help enhance search relevancy this is because it has a holistic view of the semantics across the entire data set ([View Highlight](https://read.readwise.io/read/01hx98142r4mwya2ckt8cyh0cj))
- second it helps us enable new scenarios that would today require a very large context for example doing holistic data set analysis for Trends summarization aggregation ([View Highlight](https://read.readwise.io/read/01hx981cj5hssc3y3ymsepzctp))
- in Baseline rag what you do is you take a private data set you chunk it up using embeddings and you store into a vector database then you perform your neighbor search and you can use those
  nearest neighbor searches to augment the context window ([View Highlight](https://read.readwise.io/read/01hx982v7xh1r80aygpf5tajnn))
- graph rag is a parallel process to the way that Baseline rag Works what we do with this is we actually take the same text chunks and then we take that those sentences that are being extracted and we asked the llm to perform reasoning operations over top of each sentence in a single pass through over all of the data ([View Highlight](https://read.readwise.io/read/01hx9836s7hpf44nz09gat0n9x))
- major differentiation here is we're not just looking for the named entities we're looking for the relationships between those entities and the strength of those relationships and this is where gp4 really comes in to play a very strong leading role in the capability of this technology ([View Highlight](https://read.readwise.io/read/01hx984e52f9jt9ahn0ttz28j9))
- allows us to create weighted graphs from those relationships that are far richer than just like co-occurrence networks which is where traditional ner would typically take this type of problem so once we create these knowledge graphs
  let's say for example we took all these sentences across this data set we create a Knowledge Graph here what you get are a series of nodes that are connected to each other via these relationships ([View Highlight](https://read.readwise.io/read/01hx985jg8qmnhmhz34h0c4z13))
- we can then create a labeling on that at
  one level and then we can hierarchically create subpartitions and subpartitions until you get down to individual nodes this allows us effectively a granular filter that allows us to ask questions at any level of granularity across the data set ([View Highlight](https://read.readwise.io/read/01hx986kbrts50jq03hngztkk1))

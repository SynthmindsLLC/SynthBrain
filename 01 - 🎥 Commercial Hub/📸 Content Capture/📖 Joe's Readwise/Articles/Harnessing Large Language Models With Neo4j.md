# Harnessing Large Language Models With Neo4j

![rw-book-cover](https://dist.neo4j.com/wp-content/uploads/20230606093326/neo4j-llm-e1686069255424.png)

## Metadata
- Author: [[Graph Database & Analytics]]
- Date: 2023-05-26
- Full Title: Harnessing Large Language Models With Neo4j
- Category: #articles
- Summary: Large language models like ChatGPT are revolutionizing human-machine interactions with their ability to generate human-like text. Neo4j is exploring practical uses of these models by integrating them with graph database technology. They aim to develop prototypes for natural language interfaces and knowledge graph creation.
- URL: https://neo4j.com/developer-blog/harness-large-language-models-neo4j/

## Highlights
- 1. Natural Language Interface to a Knowledge Graph
  Our first use case focuses on developing a natural language interface for knowledge graphs. The goal is to create a user interface that simplifies the process of data selection, querying and processing, making data more accessible and easier to understand. ([View Highlight](https://read.readwise.io/read/01hz74jp67ck3c3j68nmhfb9tg))
- The preferred method for this is a chat-like interface that would ***generate database queries*** based on the user question and the inferred schema of the database. ([View Highlight](https://read.readwise.io/read/01hz74max2baqdvs5g4c5jw41m))
- We’re exploring techniques to inform the LLMs about the content of the knowledge graph. This could involve a similarity search on vectorized content passed via context or fine-tuning a model on the knowledge graph itself. ([View Highlight](https://read.readwise.io/read/01hz74nd4xsv7dkqe1kctz1h8w))
- ![](https://dist.neo4j.com/wp-content/uploads/20230601095903/1fySghIB2XD0Y2JriNS3DtA.png) ([View Highlight](https://read.readwise.io/read/01hz74net288b91z5490m9h7vf))
- while simplicity and comprehensibility are important, so too are the ***accuracy and credibility of information***. To ensure this, all responses should include *links to source data*, offering full transparency and traceability. ([View Highlight](https://read.readwise.io/read/01hz74ntmv4rfgkmneqj9h63a1))
- The second use case showcases the creation of knowledge graphs from a multitude of unstructured data sources, including but not limited to PDFs, HTML pages, and text documents. ([View Highlight](https://read.readwise.io/read/01hz74p6x2yhjz31yz18grmwn9))
- They can
  • decipher entities,
  • discern relationships, and
  • eliminate redundancies by recognizing duplicates.
  In effect, LLMs can transform a seemingly indistinguishable mass of unstructured text into a well-organized, meaningful knowledge graph of entities and their relationships. ([View Highlight](https://read.readwise.io/read/01hz74pprmew7pyw4ccmbcqpdx))
- ![](https://dist.neo4j.com/wp-content/uploads/20230601095833/1XD03BcsCFLLJNqhjE7pIHw.png) ([View Highlight](https://read.readwise.io/read/01hz74prswcy6gk57ykkc4kj1k))
- Interestingly you can guide LLMs with the appropriate prompts to output structured data directly, e.g. as JSON data structures for node- and relationship-lists, that we can feed directly into the graph database. ([View Highlight](https://read.readwise.io/read/01hz74q3kp7qt99ymrz312bkbd))

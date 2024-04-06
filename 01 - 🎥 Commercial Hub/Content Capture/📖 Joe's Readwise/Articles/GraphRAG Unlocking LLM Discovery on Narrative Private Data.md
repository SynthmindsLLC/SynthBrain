# GraphRAG: Unlocking LLM Discovery on Narrative Private Data

![rw-book-cover](https://www.microsoft.com/en-us/research/uploads/prod/2024/02/NEWGraphRag-TWLIFB-1200x627-1.jpg)

## Metadata
- Author: [[Jonathan Larson]]
- Date: 2024-02-13
- Full Title: GraphRAG: Unlocking LLM Discovery on Narrative Private Data
- Category: #articles
- Summary: GraphRAG is a new approach developed by Microsoft Research to enhance the capabilities of Language Model (LLM) by using LLM-generated knowledge graphs. This approach improves question-and-answer performance when analyzing complex information by providing better context and relevance. GraphRAG outperforms baseline RAG, particularly in situations where baseline RAG struggles to connect diverse pieces of information or understand summarized concepts. It also enables whole-dataset reasoning, allowing the LLM to organize the private dataset into semantic clusters and provide meaningful summaries of themes within the data. GraphRAG has been shown to produce superior answers and provides provenance for each assertion, improving trust and verification of LLM-generated results.
- URL: https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/

## Highlights
- GraphRAG, created by Microsoft Research, as a significant advance in enhancing the capability of LLMs. ([View Highlight](https://read.readwise.io/read/01hpn22hdb54mzcyb64ss9qmd1))
- GraphRAG uses LLM-generated knowledge graphs to provide substantial improvements in question-and-answer performance when conducting document analysis of complex information. ([View Highlight](https://read.readwise.io/read/01hpn22xn4d0m9phwh12njymxz))
- Baseline RAG struggles to connect the dots. This happens when answering a question requires traversing disparate pieces of information through their shared attributes in order to provide new synthesized insights. ([View Highlight](https://read.readwise.io/read/01hpn24gan8pam23tsce69jhsk))
- Baseline RAG performs poorly when being asked to holistically understand summarized semantic concepts over large data collections or even singular large documents. ([View Highlight](https://read.readwise.io/read/01hpn24m9mr9rjc671gz7bb5fb))
- GraphRAG, uses the LLM to create a knowledge graph based on the private dataset. This graph is then used alongside graph machine learning to perform prompt augmentation at query time. ([View Highlight](https://read.readwise.io/read/01hpn25k6v1055dy1nyj7wka9p))
- GraphRAG shows substantial improvement in answering the two classes of questions described above, demonstrating intelligence or mastery that outperforms other approaches previously applied to private datasets. ([View Highlight](https://read.readwise.io/read/01hpn25zknp0sd2gge9m921efj))
- For this research, we use thousands of news articles from both Russian and Ukrainian news sources for the month of June 2023, translated into English, to create a private dataset on which we will perform our LLM-based retrieval. The dataset is far too large to fit into an LLM context window, thus demanding a RAG approach. ([View Highlight](https://read.readwise.io/read/01hpn26r0pscsx1rd6931mbqyj))
- the GraphRAG approach discovered an entity in the query, Novorossiya. This allows the LLM to ground itself in the graph and results in a superior answer that contains provenance through links to the original supporting text. ([View Highlight](https://read.readwise.io/read/01hpn287jxddm4x6wydernjf2z))
- By using the LLM-generated knowledge graph, GraphRAG vastly improves the “retrieval” portion of RAG, populating the context window with higher relevance content, resulting in better answers and capturing evidence provenance. ([View Highlight](https://read.readwise.io/read/01hpn28wxs09fwq9fd4yk81jyr))
- Baseline RAG struggles with queries that require aggregation of information across the dataset to compose an answer. ([View Highlight](https://read.readwise.io/read/01hpn29gg1y4w102t9n7f4t56j))
- the structure of the LLM-generated knowledge graph tells us about the structure (and thus themes) of the dataset as a whole. This allows the private dataset to be organized into meaningful semantic clusters that are pre-summarized. ([View Highlight](https://read.readwise.io/read/01hpn2an9h7bxq60r51mwzjkrj))
- The LLM processes the entire private dataset, creating references to all entities and relationships within the source data, which are then used to create an LLM-generated knowledge graph. ([View Highlight](https://read.readwise.io/read/01hpn2c8c13jryp37ysp2cz47y))
- This graph is then used to create a bottom-up clustering that organizes the data hierarchically into semantic clusters ([View Highlight](https://read.readwise.io/read/01hpn2chje0px122raf0vcqgvc))
- Each circle is an entity (e.g., a person, place, or organization), with the entity size representing the number of relationships that entity has, and the color representing groupings of similar entities. ([View Highlight](https://read.readwise.io/read/01hpn2djb717f5tyay8mphx8pf))
- The color partitioning is a bottom-up clustering method built on top of the graph structure, which enables us to answer questions at varying levels of abstraction. ([View Highlight](https://read.readwise.io/read/01hpn2dwz43fdctvpfts7p3y63))
- ![](https://www.microsoft.com/en-us/research/uploads/prod/2024/02/GraphRag-Figure3.jpg) ([View Highlight](https://read.readwise.io/read/01hpn2dyp6cbx9esp9z7a1413k))

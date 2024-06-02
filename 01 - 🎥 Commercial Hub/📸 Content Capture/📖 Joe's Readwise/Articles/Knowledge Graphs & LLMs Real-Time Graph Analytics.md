# Knowledge Graphs & LLMs: Real-Time Graph Analytics

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1024/1*OZjq0t_ee9XbKbciBo6qgA.png)

## Metadata
- Author: [[Tomaz Bratanic]]
- Date: 2023-07-13
- Full Title: Knowledge Graphs & LLMs: Real-Time Graph Analytics
- Category: #articles
- Summary: The blog post discusses the use of knowledge graphs and Large Language Models (LLMs) in real-time graph analytics. The authors explore how LLMs have made data more accessible, particularly in the retrieval-augmented applications that retrieve additional information to generate better results. They emphasize the importance of structured information in LLM applications and discuss various use cases where knowledge graphs can enhance analytics, such as finding shortest paths, understanding complex biomedical relationships, analyzing supply chain scenarios, and revolutionizing HR with people analytics. The authors believe that the future of LLM applications lies in the combination of vector similarity search and database query languages like Cypher. They envision a future where knowledge graphs and LLMs work together to bring innovative solutions to real-world problems.
- URL: https://medium.com/neo4j/knowledge-graphs-llms-real-time-graph-analytics-89b392eaaa95

## Highlights
- The new OpenAI models are trained to use provide parameters to functions (or what other libraries call [tools](https://python.langchain.com/docs/modules/agents/tools/)), whose signatures and descriptions are passed in the context, to retrieve additional information at query time if needed. ([View Highlight](https://read.readwise.io/read/01hz9ng7n7khnb4ynjhth7ff4a))
- The barrier to entry with these types of applications is low, especially if you are dealing with small amounts of data. It is fascinating that so many [articles giving the impression that only vector databases are relevant](https://a16z.com/2023/06/20/emerging-architectures-for-llm-applications/) for retrieval-augmented applications are published nowadays. ([View Highlight](https://read.readwise.io/read/01hz9nh0bj82dzcersdh7vsne9))
- Finding (Shortest) Paths
  Relationships are first-class citizens in native graph databases. Although knowledge graphs allow you to perform typical aggregations and filtering to answer questions like “How many customers did we get this week?”, we will focus more on analytical use cases where traversing the relationships is the main component. ([View Highlight](https://read.readwise.io/read/01hz9nj3b8qk69p6vngjfhy79h))
- Information Propagating Through Network
  Another strong knowledge graph fit is domains with networks of dependencies. For example, you could have a knowledge graph containing the complete [microservice architecture of your system](https://neo4j.com/use-cases/network-and-it-operations/). Such a knowledge graph would allow you to power a DevOps chatbot that would enable you to evaluate the architecture in real-time and perform what-if analysis. ([View Highlight](https://read.readwise.io/read/01hz9nk0mkdqp56ytrtqq110fd))
- **User-Friendly Access to Complex Data**
  A chatbot interface provides an intuitive, conversational manner for users to interact with complex datasets. Employees, managers, or HR staff wouldn’t need to understand intricate databases or analytics tools; they could simply ask the chatbot questions about employee performance, skills, or team dynamics. ([View Highlight](https://read.readwise.io/read/01hz9nkpeqeq53swhhvg0ytqrm))
- If a manager wanted to know how many projects are in the pipeline and which people are a good fit and available for a specific project, they could ask the chatbot and get an answer in real-time rather than waiting for a comprehensive report. ([View Highlight](https://read.readwise.io/read/01hz9nm3hn5as0xcbnmkv6vm45))
- Advanced AI chatbots could analyze patterns and trends from the knowledge graph to make predictions, such as which employees might be at risk of leaving the company or what skills may be in demand in the future. These predictive analytics capabilities could help companies be proactive rather than reactive in their HR strategies. ([View Highlight](https://read.readwise.io/read/01hz9nmhyj63q88ee3pqhwnqkz))

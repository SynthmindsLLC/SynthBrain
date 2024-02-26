---
Publish Year: '2024'
Authors: "Fedor Borisyuk, Shihai He, Yunbo Ouyang, Morteza Ramezani, Peng Du, Xiaochen Hou, Chengming Jiang, Nitin Pasumarthy, Priya Bannur, Birjodh Tiwana, Ping Liu, Siddharth Dangi, Daqi Sun, Zhoutao Pei, Xiao Shi, Sirou Zhu, Qianqi Shen, Kuang-Hsuan Lee, David Stein, Baolei Li, Haichao Wei, Amol Ghoting, Souvik Ghosh"
URL: "http://arxiv.org/abs/2402.11139"
Zotero Link: "zotero://select/library/items/CDTECCZB"
tags:
  - "#Computer-Science---Artificial-Intelligence, #Computer-Science---Machine-Learning, #graph, #gnn"
Published:
---
# Summary
## Purpose
- The research was initiated to address the challenges of effectively modeling the complex and dynamic interactions within LinkedIn's massive social graph, which is a significant issue in the field of machine learning and artificial intelligence. The purpose of the study was to create a unified graph embedding space for various entities like posts, members, companies, and jobs, and to improve the performance and scalability of Graph Neural Networks (GNNs) for LinkedIn's large-scale data.

## Methods
- The study builds upon the SAGE architecture, integrating sequential temporal modeling with transformer-based sequence modeling and long-term losses, tailored to the GNN domain.
- Two-hop sampling with forward push and random walks was used to show scalability on LinkedIn data.
- Artificial nearest neighbor edges were introduced to cold start nodes, leveraging content embeddings.
- The graph was densified by combining subgraphs from different domains, such as feed recommendations and job recommendations.
- Microsoft DeepGNN was chosen as the Graph Engine to provide fast real-time graph sampling with a variety of sampling strategies.
- Encoder-decoder architecture was adopted for the GNN models, with the encoder using a GraphSAGE-style framework for inductive learning.

## Key Findings
- The implementation of LiGNN resulted in a significant reduction in training time on large-scale production data, from 24 hours to 3.3 hours.
- The introduction of artificial nearest neighbor edges to cold start nodes showed quality improvements in various production applications at LinkedIn.
- The use of multi-hop sampling techniques, such as Personalized PageRank (PPR) sampling, was integral to capturing the complex graph topology.
- System-level optimizations, such as gRPC Retry, Horovod Training, and addressing memory leaks, enhanced training stability and reduced training times.
- Adaptive Neighbor Sampling, Grouping and Slicing, and a shared-memory queue were effective in reducing I/O bottlenecks and further decreasing training times.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on the field of machine learning and practical applications within professional social networks like LinkedIn. It suggests that the advancements in GNN model architectures and training methodologies contribute to the efficiency and scalability of machine learning models, enabling faster iteration and improved performance in real-world applications.

## Critiques
Upon evaluating the research, some critiques include:
- The generalizability of the findings to other domains or social networks may be limited, as the methods and optimizations were specifically tailored to LinkedIn's unique data structure and requirements.
- The complexity of the proposed solutions might pose challenges for replication or adaptation by smaller organizations with limited computational resources.
- The study may not have fully explored the trade-offs between model complexity, training time, and prediction accuracy, which could be important for practical deployment.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Machine-Learning
- #graph
- #gnn
- #scalability
- #LinkedIn
- #social-network-analysis
- #graph-embedding

# Annotations
![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/borisyukLiGNNGraphNeural2024/image-1-x303-y364.png]]



Our graph boasts up to a hundred billion nodes and several hundred billion edges. Graph edges symbolize various activities on the LinkedIn app, such as job applications, post engagements, and networking interactions” Yellow Highlight [Page 1](zotero://open-pdf/library/items/8CWXXK8S?page=1&annotation=HBFAIZC9)



Unlike traditional DNN training, GNN training has unique training scalability issues due to graph hosting requirements” Yellow Highlight [Page 1](zotero://open-pdf/library/items/8CWXXK8S?page=1&annotation=CZ9CX8E5)



our goal was to create a unified graph embedding space for various entities like posts, members, companies, and jobs” Yellow Highlight [Page 1](zotero://open-pdf/library/items/8CWXXK8S?page=1&annotation=WT4A22IC)



the dynamic, temporal nature of the LinkedIn ecosystem limited the capabilities of GNN models.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/8CWXXK8S?page=1&annotation=I56AQIRZ)



Graph Neural Networks (GNNs) are effective for modeling graphs [7] and relational data [5]. Much research has focused on enhancing GNN model architectures [7, 11, 24, 27]. Our work builds upon the SAGE [7] architecture, integrating sequential temporal modeling with transformer-based sequence modeling and long-term losses [21, 23], tailored to the GNN domain.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/8CWXXK8S?page=2&annotation=R5MSY9PL)



Our implementation uses two-hop sampling with forward push and random walks [2], showing scalability on LinkedIn data.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/8CWXXK8S?page=2&annotation=KH8N23BI)



Several studies have aimed to accelerate GNN training jobs at industry scale such as MLPinit [8], GraphStorm [33], BigGraph [15], HUGE [20]. We introduce over three novel techniques in §4 that achieved a significant reduction in training time on large-scale production data.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/8CWXXK8S?page=2&annotation=3BTH4JSK)



Our approach introduces artificial nearest neighbor edges to cold start nodes, leveraging content embeddings, which has shown quality improvements in various production applications at LinkedIn.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/8CWXXK8S?page=2&annotation=ITJCCGFQ)



To densify the graph, we combine the subgraphs from different domains together, such as feed recommendations, job recommendions, notifications. Each domain can train their GNN models using its owned subgraph, or leveraging the combined graph.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/8CWXXK8S?page=2&annotation=HNHJYXNI)



Over all, the graph contains 3 types of edges: (1) engagement edges, (2) affinity edges and (3) attribute edges. The engagement edges represent the engagements between LinkedIn’s members and the contents on the LinkedIn platform, such as "member M2 liked post P1" is represented by an edge between M2 and P1. The affinity edges capture the historical engagements between LinkedIn’s members and the creator of the contents, such as "member M2 has engaged with contents posted on LinkedIn by member M1" is represented by an edge between M2 and M1. The attribute edges capture the HAS-A relationships between two nodes such as "member M8 has a software engineer job" is represented by an edge between M8 and the corresponding job node.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/8CWXXK8S?page=2&annotation=9WA2FK2E)



The lightweight highperformance Microsoft DeepGNN [25] was chosen as the Graph Engine to provide fast real-time graph sampling with a variety of sampling strategies” Yellow Highlight [Page 2](zotero://open-pdf/library/items/8CWXXK8S?page=2&annotation=Q42H2J6N)



Depending on the size of graph, one can launch one or more instances (pod* ) to serve a portion of the partitioned graph. During training (or inference) the DeepGNN client queries the GEs with a given setup, which consists of the sampling algorithm and configuration, over gRPC.  The resulting data is consumed by the underlying deep learning framework (Tensorflow).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/8CWXXK8S?page=2&annotation=KEV77N9G)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/borisyukLiGNNGraphNeural2024/image-3-x38-y627.png]]



Considering the complexity of using GNN models to replace the existing machine learning models in LinkedIn, we adopted the the encoder-decoder architecture for the GNN models as shown in Figure 3. In this way, we can only take the trained encoder to generate the node embeddings and apply the embeddings in the downstream application models as new features” Yellow Highlight [Page 3](zotero://open-pdf/library/items/8CWXXK8S?page=3&annotation=9PS59FZX)



To handle the large scale LinkedIn graph and carry out inductive learning, the encoder adopts the GraphSAGE-style framework [7], which inductively generates the node embeddings based on graph sampling and neighborhood aggregation” Yellow Highlight [Page 3](zotero://open-pdf/library/items/8CWXXK8S?page=3&annotation=8FDESLCJ)



DeepGNN GE, including multi-hop random sampling, weighted sampling, Personalized PageRank (PPR) sampling.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/8CWXXK8S?page=3&annotation=NJJBJUJG)



The decoder of the GNN model takes the embeddings generated from the encoder as its input and computes the predictions. Currently we support Multilayer Perceptron (MLP) decoder, cosine decoder and in-batch negative sampling decoder [18] for link prediction tasks” Yellow Highlight [Page 3](zotero://open-pdf/library/items/8CWXXK8S?page=3&annotation=382SV4IZ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/borisyukLiGNNGraphNeural2024/image-3-x52-y72.png]]



The GNNs that we discussed so far are static, which lack temporal dynamics that is critical for professional social networks like LinkedIn, where interactions are time-sensitive.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/8CWXXK8S?page=3&annotation=URFBZ3Y9)



Although there is research on event-driven and message-passing in dynamic GNNs [24, 28], their real-world applicability is limited. We redefine "temporal graphs" to focus on temporal sequence modeling within GNNs” Yellow Highlight [Page 3](zotero://open-pdf/library/items/8CWXXK8S?page=3&annotation=XFUIRHYS)



The degree distribution in social network graphs often follows a power law, with most nodes having few interactions. This presents a challenge for neighborhood aggregation in GNNs, particularly for nodes with low out-degrees” Yellow Highlight [Page 3](zotero://open-pdf/library/items/8CWXXK8S?page=3&annotation=TPCLVQNC)



To combat this, LiGNN implements graph densification by adding artificial edges based on auxiliary information.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/8CWXXK8S?page=3&annotation=TSXFE4PE)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/borisyukLiGNNGraphNeural2024/image-4-x38-y498.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/borisyukLiGNNGraphNeural2024/image-4-x309-y292.png]]



Algorithm 1 consists of three main functions. The Query function retrieves the embedding for a node. the approximate_knn function identifies the top 𝑘 similar high-out-degree nodes for a low-outdegree node, using embedding similarity. For scalability in handling numerous nodes, we use an in-house approximate nearest neighbor search solution, based on HNSW [3]. The create_edge function forms artificial edges between a low-out-degree node and its top 𝑘 similar high-out-degree counterparts. This method facilitates information flow from active nodes to less active nodes, mitigating cold start issues” Yellow Highlight [Page 4](zotero://open-pdf/library/items/8CWXXK8S?page=4&annotation=U2FK2363)



For LiGNN to surpass traditional deep learning methods, effective sampling is key. Simple one-hop sampling falls short in capturing the complex graph topology, hence LiGNN adopts multi-hop sampling for deeper graph analysis.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/8CWXXK8S?page=4&annotation=EVVLHUJY)



Multi-hop random/weighted sampling: This method allows for either random sampling or user-configurable weighted sampling, where weights are adjustable for different edge types.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/8CWXXK8S?page=4&annotation=RJNJ3RXN)



Multi-hop Personalized PageRank (PPR) Sampling: Integral to LiGNN, PPR is a prominent tool in large-scale graph mining. It locates neighbors with the top 𝑘 PPR scores relative to a source node, identifying key topological nodes.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/8CWXXK8S?page=4&annotation=HRHUQQBH)



efficiency is enhanced through approximate calculations using the Forward Push Algorithm and system-level optimizations. To accelerate PPR sampling for a batch of nodes, we consolidate sampling requests in each iteration of Forward Push into a single batch, reducing overhead.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/8CWXXK8S?page=4&annotation=9J8X86JK)



Two-hop Personalized PageRank (PPR) Sampling: Tailored for nearline serving, which currently only supports 2-hop methods, this approach returns neighbors within a 2-hop radius with the top 𝑘 PPR scores. It utilizes a fast 2hop random walk algorithm for PPR computation, offering quicker sampling than multi-hop PPR.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/8CWXXK8S?page=4&annotation=F6K2NGBR)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/borisyukLiGNNGraphNeural2024/image-5-x43-y406.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/borisyukLiGNNGraphNeural2024/image-5-x40-y95.png]]



gRPC Retry: GNN training workers often fetch GBs of data from the GE for each batch via gRPC calls, straining the data transmission between workers and the GE server. With distributed training employing 6 to 24 workers, connection losses to the GE were common. By modifying the default gRPC retry policy to maximize "max_attempts" and "max_backoff", we effectively resolved the connection issue, enhancing the training success rate by 15%” Yellow Highlight [Page 5](zotero://open-pdf/library/items/8CWXXK8S?page=5&annotation=MJT6FUL4)



Horovod Training: Besides connection problems with the GE server, many job failures stemmed from worker-to-worker communication breakdowns. Transitioning from TensorFlow’s MultiWorkerMirroredStrategy to Horovod distributed training, which utilizes NVIDIA’s NCCL 2 and ring allreduce operation, significantly improved training stability, increasing success rates by 35%.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/8CWXXK8S?page=5&annotation=42VSND9Y)



Memory Leak: Parallel data fetching in training workers, involving multiple prefetchers for graph data and storing batch data in a queue with a typical size of 10, usually consumed tens of GBs of memory. We observed delayed garbage collection, leading to memory leaks and out-of-memory failures. Adopting TensorFlow’s GeneratorEnqueuer resolved this memory leak issue, further enhancing training stability by 10%.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/8CWXXK8S?page=5&annotation=7AXJHPNT)



GNN jobs are often data-bound, implying that optimizing neighbor collection from the graph engine can significantly impact training speed. Overall during development of GNNs at LinkedIn the training time reduced from 24 hours, when we started, to 3.3 hours on the latest training jobs, with largest contributions from Adaptive Neighbor sampling, Grouping and Slicing and Share-Memory Queue.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/8CWXXK8S?page=5&annotation=T2AW5MTE)



Reduce average step time: Typically, each training step is comprised of three components: data loading, forward and backward pass. If data-parallel distributed training is used, gradients need to be communicated across all workers through an AllReduce operation after backward pass. To reduce average step time, we can focus on optimization of the most time consuming components.  Local gradient aggregation is a technique to reduce the frequency of gradient communication. Gradients will be aggregated locally on each worker for N mini-batches before they are sent to other workers through AllReduce. Note that local gradient aggregation is effectively increasing batch size by N times, and utilizing techniques like learning rate scaling [12] is important for large-batch training.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/8CWXXK8S?page=5&annotation=QT97XU7Q)



Increase convergence speed: We explored MLPinit [8], which trains node encoder weights from the node features in two tower style link-prediction matching without querying the GE. We observed 16.25% speedup from using MLPinit. Next we will show how we generalized MLPinit using Adaptive Neighbor Sampling strategy to decrease training speed even further.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/8CWXXK8S?page=6&annotation=N73AYGDE)



Adaptive Neighbor Sampling: Since the I/O (reading data from GE) is the bottleneck of GNN training, we proposed several techniques to speeding up GNN by tackling the I/O part, one of which is to adaptively increase the number of neighbors to be sampled during training. We sample a small number of neighbors at the beginning and adaptively increase the neighbor count by monitoring the model performance. If the metric (e.g., AUC) keeps increasing with a small number of neighbors, we do not sample more neighbors. We only sample more neighbors when the metrics are not improved by a certain threshold. Since the number of neighbors and I/O time are correlated, starting with a small number of neighbors to learn a model can help save a large amount of training time (Algorithm 2).” Yellow Highlight [Page 6](zotero://open-pdf/library/items/8CWXXK8S?page=6&annotation=GGHXPMWB)



Grouping and Slicing: The training dataset comprises millions of triplets including member IDs, item IDs (like follow feed posts or jobs), and labels, showing interactions between members and items. Notably, active members often interact with numerous items, confirmed by feed dataset analysis. Given the I/O constraints of GNN, traditional feature generation by querying neighbors for each member-item pair is inefficient due to repeated queries for active members. To optimize, we group training records by members, slicing grouped items and labels at a set threshold, then querying once for the member and grouped items. For instance, if a member has 10 interactions and the group size is 5, we create two data records for this member with 5 items each, cutting GE queries from 10 to 2, albeit each query being slightly more extensive” Yellow Highlight [Page 6](zotero://open-pdf/library/items/8CWXXK8S?page=6&annotation=EK8KW4MV)



Once we get the grouped data, e.g., one member with 5 items, there are two training approaches: (A) generate member and item embeddings together, compute average loss of the 5 pairs, backpropagate once, or (B) forward and backward passes for each pair, updating the model 5 times. While A is generally faster, it may underperform compared to B. However, with large model sizes, A can be a good way to reduce training time” Yellow Highlight [Page 6](zotero://open-pdf/library/items/8CWXXK8S?page=6&annotation=ZWQ4V6UA)



Experiments on LinkedIn data showed that using an intermediate number performs more effectively without reducing model quality and leads to a 69.9% reduction in training time” Yellow Highlight [Page 6](zotero://open-pdf/library/items/8CWXXK8S?page=6&annotation=FXYZ2VDW)



we crafted a shared-memory queue in native Python, employing the multiprocessing package to simultaneously query the DeepGNN Graph Engine across multiple processes. This approach efficiently prefetches and preprocesses the necessary training data. Our experiments demonstrated that this multi-processing with a shared-memory queue can reduce training times by as much as 68%.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/8CWXXK8S?page=6&annotation=VCIZR5AS)



LinkedIn’s nearline pipeline utilizes Apache Beam. The Managed-beam team and the Machine Learning Infrastructure team at LinkedIn have contributed valuable components, such as SourceComponent, SinkComponent, and InferenceComponent, to assist AI engineers in minimizing development costs. However, challenges like the lack of batch feature fetchers, data converters for 2D tensors, and certain sampling functions were noted” Yellow Highlight [Page 6](zotero://open-pdf/library/items/8CWXXK8S?page=6&annotation=YDV2N6PC)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/borisyukLiGNNGraphNeural2024/image-7-x306-y567.png]]



GNN embeddings are used in the EmbeddingBased Retrieval (EBR) model of the Follow Feed recommendation system. These embeddings effectively capture the viewer’s relationship with the post creator and interest in the post content. In the GNN model, the Follow Feed recommendation issue is treated as a link prediction task, determining the likelihood of a member interacting with a post.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/8CWXXK8S?page=7&annotation=8VIKZ9LA)



Table 4 highlights that including node ID embeddings significantly enhances model efficacy by an +15.3% in validation AUC. The graph sampling strategy plays a crucial role, with performance generally improving as more neighbors are sampled; a jump from 20 to 200 neighbors results in an 3.2% AUC increase.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/8CWXXK8S?page=7&annotation=XBA8E8JH)



To train the GNN model, a substantial graph was constructed, comprising up to one billion member nodes and billions of connection edges. The weight of each edge between members 𝑢 and 𝑣 is determined by the formula: # of common connections between 𝑢 and 𝑣 √# of 𝑢’s connections × √# of 𝑣’s connections .” Yellow Highlight [Page 8](zotero://open-pdf/library/items/8CWXXK8S?page=8&annotation=XMEVFT7E)



we switched to using a Graph Engine for real-time compute graph sampling. This change eliminated the need for precomputation and addressed slow disk I/O by directly serving graph data from memory. With the graph data in GE, we can experiment with various sampling strategies or model architectures without altering the underlying graph, enhancing model iteration by 10X.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/8CWXXK8S?page=9&annotation=4C9IZQWB)



GE allows training jobs to dynamically request compute graphs in real-time for each training instance. Introducing randomness in sampling means compute graphs for the same node vary with each request, leading to better model performance through enhanced generalization.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/8CWXXK8S?page=9&annotation=65BM99LJ)




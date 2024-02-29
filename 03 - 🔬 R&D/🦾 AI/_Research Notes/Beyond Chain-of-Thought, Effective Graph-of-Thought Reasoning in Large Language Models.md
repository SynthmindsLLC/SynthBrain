---
Publish Year: '2023'
Authors: "Yao Yao, Zuchao Li, Hai Zhao"
URL: "http://arxiv.org/abs/2305.16582"
Zotero Link: "zotero://select/library/items/H7J84YIW"
tags:
  - "#Computer-Science---Computation-and-Language, #graph, #prompt-engineering"
Published:
---
# Summary
## Purpose
- The research was initiated to address the limitations of linear thought processes in artificial intelligence, which is a significant issue in the field of Computer Science—Computation and Language. The purpose of the study was to develop a novel approach to model human thought processes not just as a chain but also as a graph, to better simulate human reasoning and problem-solving abilities.

## Methods
- Introduction of Graph-of-Thought (GoT), a method that represents thought units as nodes and connections between thoughts as edges.
- Implementation of an Extract-Cluster-Coreference (ECC) process to construct thought graphs from deductive triplets.
- Encoding of the thought graph using a graph attention network and fusion with the original representation via a gated fusion network.
- Integration of text, thought graph, and visual features in a two-stage framework for fine-tuning language models.
- Utilization of open information extraction systems and coreference resolution for constructing the thought graph.
- Encoding of input text and images using a Transformer encoder and a vision encoder, respectively.

## Key Findings
- GoT demonstrates exceptional performance on text-only and multimodal benchmarks, surpassing the accuracy of the online system ChatGPT by significant margins and even exceeding human performance on the ScienceQA test set.
- The GoT model shows a minor decrease in accuracy as the grade level of questions increases, suggesting its robustness in deductive reasoning across different complexity levels.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on the field of artificial intelligence and language comprehension. It suggests that the GoT approach contributes to the field by providing a more realistic and logical modeling of reasoning processes, which can lead to better comprehension of relationships between entities and an improved understanding of problem statements.

## Critiques
Upon evaluating the research, some critiques include:
- The generalizability of the findings to other types of reasoning tasks beyond the benchmarks used in the study may need further exploration.
- The complexity of the GoT model and its computational requirements could be a limitation for practical applications.
- The study may benefit from a more detailed comparison with other state-of-the-art models in terms of interpretability and scalability.

## Tags
- #Computer-Science---Computation-and-Language
- #Graph
- #Prompt-Engineering
- #Artificial-Intelligence
- #Reasoning-Processes
- #Language-Models
- #Human-Like-Reasoning

# Annotations
Human thinking is often characterized by its ability to make sudden leaps and connections between seemingly unrelated ideas, which can lead to novel insights and solutions. This non-linear, jumping thought process is a hallmark of human creativity, reasoning, and problem-solving abilities” Yellow Highlight [Page 1](zotero://open-pdf/library/items/2TGEEK35?page=1&annotation=38WTDBQZ)



Zhang et al. [1] have introduced Multimodal-CoT, which combines both language and visual modalities to help surpass the limitations of textual information.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/2TGEEK35?page=2&annotation=EKFDE3AI)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/yaoChainofThoughtEffectiveGraphofThought2023/image-2-x92-y275.png]]



Graph-of-Thought (GoT), a novel approach to modeling human thought processes not only as a chain but also as a graph. Our method is based on the assumption that the human mind works by connecting and recombining ideas in a non-sequential, graph fashion, rather than following a strict sequential chain” Yellow Highlight [Page 2](zotero://open-pdf/library/items/2TGEEK35?page=2&annotation=ACA2VXAM)



By representing thought units as nodes and connections between thoughts as edges, the Graph-of-Thought captures the rich, non-sequential nature of human thinking and allows for a more realistic and logical modeling of reasoning processes.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/2TGEEK35?page=2&annotation=XB4Q2HD9)



It first generates rationales and then generates the final answer based on the predicted rationales. In addition to text features, graph features of GoT are integrated during the rationale generation and answer inference. Specifically, GoT is first constructed with an Extract-Cluster-Coreference (ECC) process, which simulates the deductive process in human reasoning” Yellow Highlight [Page 2](zotero://open-pdf/library/items/2TGEEK35?page=2&annotation=WC9BC8XA)



GoT is encoded with a graph attention network and then fused with the original representation via a gated fusion network.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/2TGEEK35?page=2&annotation=KTTS2W8G)



Furthermore, we have also presented a multimodal GoT, which integrates not only text features and GoT features but also visual features” Yellow Highlight [Page 2](zotero://open-pdf/library/items/2TGEEK35?page=2&annotation=2C4L2RVG)



We implement GoT as a two-stage framework and fine-tuning language models and integrating text, thought graph, and vision features for a more realistic and accurate reasoning process. GoT demonstrates exceptional performance on both text-only GSM8K [11] and multimodal ScienceQA [12] benchmarks, surpassing the accuracy of online system ChatGPT [5] by 25.08%, 14.46%, strong baseline Multimodal-CoT [1] by 6.63%, and even exceeding human performance, establishing a new state-of-the-art on ScienceQA test set with far more less parameters.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/2TGEEK35?page=2&annotation=3AW7QH44)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/yaoChainofThoughtEffectiveGraphofThought2023/image-3-x112-y446.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/yaoChainofThoughtEffectiveGraphofThought2023/image-3-x114-y90.png]]



GoT employs thought graphs to simulate human deductive reasoning, thereby modeling humans’ ability for leaps of thought. Our aim is to reflect the most fundamental deduction process by constructing a thought graph. If we have evidence that x → y and y → z, then it follows that x → z.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/2TGEEK35?page=4&annotation=T3Q9KRPJ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/yaoChainofThoughtEffectiveGraphofThought2023/image-4-x293-y426.png]]



We propose a novel Extract-ClusteringCoreference (ECC) process to construct thought graphs. ECC first extracts deductive triplets T = {ti = (ti x, ti y, ti z)} as the discrete raw graph, where ti x, ti y, and ti z are thought units of the i-th triplet, and there exists an edge ei xy between ti x and ti y, and an edge ei yz between ti y and ti z. Then, ECC clusters the nodes that refer to the same mentions to conduct coreference resolution.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/2TGEEK35?page=4&annotation=BY6XP735)



In GoT construction, during the rationale generation stage, the input text consists of concatenated question, context, and choices. In multimodal GoT, image caption [12] is appended to the input text for GoT to incorporate image information. During the answer inference stage, the predicted rationales from the rationale generation stage are further concatenated with the input text for corresponding GoT construction.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/2TGEEK35?page=4&annotation=G2XX33BD)



In our implementation of ECC process, inspired by [13], we utilize open information extraction (OpenIE) systems 2 [14] to extract subject-verb-object triplets as thought unit nodes. We apply coreference resolution to the extracted nodes using the Stanford CoreNLP system [15]. The constructed thought graph is denoted as G(N , E), where N represents the nodes extracted by OpenIE and E represents the adjacency matrix. Rows and columns correspond to the nodes in the graph, and if there is an edge between two nodes, the corresponding matrix element is 1; otherwise, it is 0.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/2TGEEK35?page=4&annotation=PHLI4XKJ)



The thought graph is encoded using a graph attention network, while the input text is encoded using a Transformer encoder. In multimodal GoT reasoning, the image is encoded using an additional vision encoder.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/2TGEEK35?page=4&annotation=HPVN8ZFJ)



Text Encoder For text representation, we use the Transformer encoder (e.g. T5 [9]) to encode the input text. Given input sentence S = {w0, ..., wl}, we extract the hidden states from the last layer of the Transformer encoder to obtain the text representation HT : HT = {h0, h1, ..., hl} = Encodertext(S) (1) where hi is the hidden representation of token i and l represents the length of the text input.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/2TGEEK35?page=4&annotation=EZ3TV29T)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/yaoChainofThoughtEffectiveGraphofThought2023/image-5-x332-y406.png]]



Node Embedding We first use special tokens <s> and </s> to highlight every thought graph node.  Specifically, for node set with j nodes N = {n0, ...nj} , we construct the node input as p. we then feed the p into the same text encoder and utilize the output representation of the special token <s> as the initial node representation.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/2TGEEK35?page=5&annotation=3TZ8YM7P)



GAT Encoder We employ a graph attention network (GAT) [16, 13] to encode the thought graph. For every node ni in graph G(N , E), the graph attention layer is designed as: Dropout GoT input G 𝑁, 𝐸 Graph Attention Layer Graph Attention Layer Concatenate Dropout Graph Attention Layer FFNN Layernorm GoT representation Multi-head attention Residual connection ℎ𝑔′ ℎ𝑔′ 𝐻𝐺 … Figure 4: Architecture of GoT encoder aij = Attention(Whs i ||Whs j ); qij = LeakyReLU (aij ) (5) αij = Softmax(qij ) = exp (qij ) Pk∈K exp (qik); hg′ i = GELU X j∈Ki αijWhs j  (6)” Yellow Highlight [Page 5](zotero://open-pdf/library/items/2TGEEK35?page=5&annotation=HC8IVTKY)



The architecture of our GoT encoder can be seen in Figure 4” Yellow Highlight [Page 5](zotero://open-pdf/library/items/2TGEEK35?page=5&annotation=3LRH7IRI)



After obtaining the encoded features, we use a single head attention to align the text representation HT with image representation HI and thought graph representation HG, respectively” Yellow Highlight [Page 6](zotero://open-pdf/library/items/2TGEEK35?page=6&annotation=T2SXTRS4)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/yaoChainofThoughtEffectiveGraphofThought2023/image-8-x99-y451.png]]



Performance on Different Grades It can be seen from the Table 4 that the enlarged MutimodalCoT experience a decrease in accuracy of 2.07 as the grade level of the given question increases while GoT only has minor decrease of 0.41. We believe the main reason is that by incorporating GoT, models acquires the ability for deductive reasoning and can better comprehend the relationships between different entities and thus better understand the meaning of the problems.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/2TGEEK35?page=9&annotation=9GNDXELV)




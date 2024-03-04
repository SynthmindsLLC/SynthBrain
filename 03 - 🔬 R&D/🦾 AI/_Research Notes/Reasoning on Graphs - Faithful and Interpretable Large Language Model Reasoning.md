---
Publish Year: "2023"
Authors: Linhao Luo, Yuan-Fang Li, Gholamreza Haffari, Shirui Pan
URL: http://arxiv.org/abs/2310.01061
Zotero Link: zotero://select/library/items/WJC6SYFU
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
Published:
---
# Summary

## Purpose
The research was initiated to address the limitations of Large Language Models (LLMs) in reasoning tasks, specifically their lack of knowledge and tendency to produce hallucinations, which is a significant issue in the field of Computer Science - Artificial Intelligence. The purpose of the study was to enhance the reasoning ability of LLMs by incorporating Knowledge Graphs (KGs) for more faithful and interpretable reasoning.

## Methods
- Introduction of the plan-and-solve paradigm, where LLMs generate a plan and execute each reasoning step by decomposing complex reasoning tasks into sub-tasks.
- Incorporation of Knowledge Graphs (KGs) to provide a structured format of factual knowledge for reasoning.
- Development of a planning-retrieval-reasoning framework, where relation paths grounded by KGs are generated as faithful plans, and these plans are used to retrieve valid reasoning paths from KGs.
- Optimization of the framework through planning optimization (distilling knowledge from KGs into LLMs) and retrieval-reasoning optimization (enabling LLMs to conduct reasoning based on retrieved paths).

## Key Findings
- The integration of KGs with LLMs through the proposed framework significantly improves the reasoning ability of LLMs, making it more faithful and interpretable.
- The planning module of the framework can be seamlessly integrated with different LLMs, substantially improving their performance without the need for retraining.
- The effectiveness of the reasoning module in identifying important reasoning paths and filtering out noise was demonstrated, highlighting the importance of both planning and reasoning modules in the framework.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on the field of Artificial Intelligence, specifically in enhancing the reasoning capabilities of Large Language Models. It suggests that the incorporation of Knowledge Graphs and the development of a planning-retrieval-reasoning framework contribute to more faithful and interpretable reasoning by LLMs, addressing the critical issue of knowledge lack and hallucinations.

## Critiques
Upon evaluating the research, some critiques include:
- The generalizability of the findings may be limited by the specific types of KGs and LLMs used in the study.
- The complexity of integrating KGs with LLMs in real-world applications may pose challenges not fully addressed in the study.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Computation-and-Language
- #Knowledge-Graphs
- #Large-Language-Models
- #Reasoning

# Annotations
To further unleash LLMs’ reasoning ability, the plan-and-solve paradigm (Wang et al., 2023c) has been proposed, in which LLMs are prompted to generate a plan and execute each reasoning step. In this way, LLMs decompose complex reasoning tasks into a series of sub-tasks and solve them step by step (Khot et al., 2022).” Yellow Highlight [Page 1](zotero://open-pdf/library/items/M9M2ZXFA?page=1&annotation=U3NWKHTR)



Despite their success, LLMs are still limited by the lack of knowledge and prone to hallucinations during reasoning, which can lead to errors in reasoning processes (Hong et al., 2023; Wang et al., 2023b).” Yellow Highlight [Page 1](zotero://open-pdf/library/items/M9M2ZXFA?page=1&annotation=A48K3D47)



To tackle the issues, knowledge graphs (KGs) have been incorporated to improve the reasoning ability of LLMs (Pan et al., 2023; Luo et al., 2023). KGs capture abundant factual knowledge in a structured format, which provides a faithful knowledge source for reasoning” Yellow Highlight [Page 1](zotero://open-pdf/library/items/M9M2ZXFA?page=1&annotation=9J7ELCAF)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/luoReasoningGraphsFaithful2023/image-2-x100-y547.png]]



knowledge graph question answering (KGQA) aims to obtain answers based on knowledge from KGs (Sun et al., 2019; Hu et al., 2023). Previous works that jointly use KGs and LLMs for KGQA reasoning can be broadly divided into two categories: 1) semantic parsing methods (Lan & Jiang, 2020; Ye et al., 2022), which use LLMs to convert questions into logical queries that are executed on KGs to obtain answers; and 2) retrieval-augmented methods (Li et al., 2023; Pan et al., 2022), which retrieve triples from KGs as knowledge context and uses LLMs to obtain the final answers.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/M9M2ZXFA?page=2&annotation=UKAS2MBM)



Retrieval-augmented methods are more flexible and exploit the ability of LLMs for reasoning. However, they only treat KGs as factual knowledge bases and overlook the importance of their structural information for reasoning (Jiang et al., 2022)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/M9M2ZXFA?page=2&annotation=LZB93SMT)



relation path, which is a sequence of relations, “child of→has son” can be used to obtain answers to the question “Who is the brother of Justin Bieber?”. Therefore, it is essential to enable LLMs to directly reason on KGs to achieve faithful and interpretable reasoning.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/M9M2ZXFA?page=2&annotation=7RMYFNU7)



reasoning on graphs (RoG) that synergizes LLMs with KGs to conduct faithful and interpretable reasoning” Yellow Highlight [Page 2](zotero://open-pdf/library/items/M9M2ZXFA?page=2&annotation=8CSMCJNM)



planning-retrieval-reasoning framework, where RoG first generates relation paths grounded by KGs as faithful plans via the planning module.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/M9M2ZXFA?page=2&annotation=Q3VQIPV9)



These plans are then used to retrieve valid reasoning paths from KGs to conduct faithful reasoning by the retrieval-reasoning module. In this way, we not only retrieve the latest knowledge from KGs but also consider the guidance of KG structure for reasoning and explanations” Yellow Highlight [Page 2](zotero://open-pdf/library/items/M9M2ZXFA?page=2&annotation=WIT6S6SV)



Moreover, the planning module of RoG can be plug-and-play with different LLMs during inference to improve their performance. Based on this framework, RoG is optimized by two tasks: 1) planning optimization, where we distill knowledge from KGs into LLMs to generate faithful relation paths as plans; and 2) retrieval-reasoning optimization, where we enable LLMs to conduct faithful reasoning based on retrieved paths and generate interpretable results” Yellow Highlight [Page 2](zotero://open-pdf/library/items/M9M2ZXFA?page=2&annotation=V2KUF7FS)



Conventional embedding-based methods represent the entities and relations in embedding space and design special model architectures (e.g., Key-Value memory networks, sequential models, and graph neural networks) to reason answers (Miller et al., 2016; He et al., 2021; Yasunaga et al., 2021)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/M9M2ZXFA?page=3&annotation=XXMU4SL2)



UniKGQA (Jiang et al., 2022) which unifies the graph retrieval and reasoning process into a single model with LLMs, achieves STOA performance.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/M9M2ZXFA?page=3&annotation=IVKPRP4Y)



Semantic parsing methods convert the question into a structural query (e.g., SPARQL) by LLMs, which can be executed by a query engine to reason the answers on KGs (Sun et al., 2020; Lan & Jiang, 2020). However, these methods heavily rely on the quality of generated queries. If the query is not executable, no answers will be generated.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/M9M2ZXFA?page=3&annotation=JEDBLSJG)



Knowledge Graph Question Answering (KGQA) is a typical reasoning task based on KGs. Given a natural language question q and a KG G, the task aims to design a function f to predict answers a ∈ Aq based on knowledge from G, i.e., a = f(q, G). Following previous works (Sun et al., 2019; Jiang et al., 2022), we assume the entities eq ∈ Tq mentioned in q and answers a ∈ Aq are labeled and linked to the corresponding entities in G, i.e., Tq, Aq ⊆ E.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/M9M2ZXFA?page=3&annotation=6J9SKGXI)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/luoReasoningGraphsFaithful2023/image-4-x96-y410.png]]



By treating relation paths as plans, we can make sure the plans are grounded by KGs, which enables LLMs to conduct faithful and interpretable reasoning on graphs. In a nutshell, we formulate our RoG as an optimization problem that aims to maximize the probability of reasoning the answer from a knowledge graph G w.r.t the question q by generating relation paths z as the plan: Pθ(a|q, G) = X z∈Z Pθ(a|q, z, G)Pθ(z|q),” Yellow Highlight [Page 4](zotero://open-pdf/library/items/M9M2ZXFA?page=4&annotation=P5KPKEUJ)



we design two instruction tuning tasks: 1) planning optimization, which distills the knowledge from KGs into LLMs to generate faithful relation paths as plans; 2) retrieval-reasoning optimization, which enables LLMs to reason based on the retrieved reasoning paths.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/M9M2ZXFA?page=4&annotation=QGVV8PNL)



The objective function in equation 1 can be optimized by maximizing the evidence lower bound (ELBO) (Jordan et al., 1999), which is formulated as log P(a|q, G) ≥ Ez∼Q(z)[log Pθ(a|q, z, G)] − DKL(Q(z)∥Pθ(z|q)),” Yellow Highlight [Page 4](zotero://open-pdf/library/items/M9M2ZXFA?page=4&annotation=IQQZATF5)



Retrieval-reasoning optimization. In retrieval-reasoning optimization, we aim to enable LLMs to conduct reasoning based on the retrieved reasoning paths. For the retrieval-reasoning module, we follow the FiD framework (Izacard & Grave, 2021), which allows reasoning on multiple retrieved reasoning paths, formulated as Pθ(a|q, Z, G) = Y z∈Z Pθ(a|q, z, G). (5) By approximating the expectation with K sampled plans ZK, the objective function of reasoning optimization can be written as Lreason = Ez∼Q(z|a,q,G)[log Pθ(a|q, z, G)] = log Pθ(a|q, ZK, G). (6) This maximizes the probability of LLMs generating correct answers based on the retrieved reasoning paths.  The final objective function of RoG is the combination of the planning optimization and retrievalreasoning optimization, which can be formulated as L = log Pθ(a|q, ZK, G) | {z } Retrieval-reasoning + X z∈Q(z|a,q,G) log Pθ(z|q) | {z }” Yellow Highlight [Page 5](zotero://open-pdf/library/items/M9M2ZXFA?page=5&annotation=8CQWERJ7)



Retrieval. Given a question q and a relation path as plan z, the retrieval module aims to retrieve the reasoning paths wz from KG G. The retrieval process can be conducted by finding paths in G that start from the question entities eq and follow the relation paths z, formulated as Wz = {wz(eq, e∗)|wz(eq, e∗) = eq r1−→ e1 r2−→ . . .  rl−→ ea∗, wz(eq, e∗) ∈ G}. (9) We adopt a constrained breadth-first search to retrieve the reasoning paths wz from KGs. In experiments, all retrieved paths are used for reasoning.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/M9M2ZXFA?page=6&annotation=73PMLZ3W)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/luoReasoningGraphsFaithful2023/image-8-x113-y257.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/luoReasoningGraphsFaithful2023/image-9-x111-y445.png]]



From the results, it is evident that without a planning module, our method degenerates to conventional LLMs that solely rely on questions as input, suffering from the lack of knowledge issue.  Although removing the reasoning module leads to high recall due to an increased number of answers, precision drops significantly because of noise in retrieved paths. This demonstrates the effectiveness of the reasoning module in identifying important reasoning paths and filtering out noise.  Furthermore, using random plans achieves worse performance than removing the planning module, highlighting the importance of a planning module who generates faithful reasoning plans. Using a simple majority vote reasoning can improve the results which also demonstrate the necessity of reasoning module.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/M9M2ZXFA?page=9&annotation=YB2D6L43)



we can notice that the performance of all LLMs is substantially improved by integrating the planning module of RoG. Specifically, the Hits@1 of ChatGPT, Alpaca, LLaMA2, and Flan-T5 are improved by 8.5%, 15.3%, and 119.3%, respectively. This demonstrates that the planning module of RoG can be seamlessly integrated with other LLMs to improve their performance without retraining.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/M9M2ZXFA?page=9&annotation=6I8SFZQT)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/luoReasoningGraphsFaithful2023/image-10-x95-y236.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/luoReasoningGraphsFaithful2023/image-10-x96-y494.png]]




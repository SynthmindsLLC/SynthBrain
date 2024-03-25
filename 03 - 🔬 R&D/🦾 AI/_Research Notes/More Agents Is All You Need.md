---
Publish Year: "2024"
Authors: Junyou Li, Qin Zhang, Yangbin Yu, Qiang Fu, Deheng Ye
URL: http://arxiv.org/abs/2402.05120
Zotero Link: zotero://select/library/items/28RCLUSH
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#Computer-Science---Machine-Learning"
  - Computer-Science---Multiagent-Systems
Published:
---
# Summary

## Purpose
- The research was initiated to explore the impact of increasing the number of instantiated Large Language Model (LLM) agents on the performance of LLMs in processing complex tasks. This study addresses the significant issue in the field of **Computer Science, specifically in Artificial Intelligence, Computation and Language, Machine Learning, and Multiagent Systems**. The purpose of the study was to demonstrate that simply adding more LLM agents can significantly improve performance without the need for complicated methods such as Chains of Thought (CoT) pipelines or multi-agent collaboration frameworks.

## Methods
- **Sampling-and-Voting Method**: This method involves two phases. First, the task query is iteratively fed into either a single LLM or a multiple LLM-Agents collaboration framework to generate multiple outputs. Then, majority voting is used to determine the final result.
- **Performance Analysis**: The study conducts a comprehensive analysis of the scaling property of LLM agents, examining how performance scales with the increase in the number of agents across a wide range of tasks.

## Key Findings
- **Performance Improvement with More Agents**: The study finds that LLM performance generally improves by increasing the ensemble size, i.e., the number of agents. Surprisingly, an ensemble of smaller LLMs can achieve comparable or even superior performance to larger LLMs.
- **Simplicity and Efficiency**: Comparable performance improvements can be achieved without the need for additional handcrafted prompt design or complex collaboration frameworks.
- **Enhancement of Existing Methods**: The simple sampling-and-voting method for instantiating agents can generally improve the performance of LLMs and is orthogonal to different existing methods, leading to further improvements when combined with them.
- **Task Difficulty Influence**: The performance gains from adding more agents are influenced by the difficulty of the task.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on the field of Artificial Intelligence and Machine Learning. It suggests that the simple approach of adding more LLM agents can be a powerful strategy to enhance LLM performance in complex tasks. This finding is particularly relevant for applications requiring high accuracy and reliability, offering a straightforward method to leverage the capabilities of LLMs without complex modifications.

## Critiques
Upon evaluating the research, some critiques include:
- **Generalizability of Findings**: The study's findings, while promising, may need further validation across a broader range of tasks and LLM configurations to fully understand the limits and applicability of the scaling benefits.
- **Complexity of Real-World Applications**: While the study demonstrates improvements in LLM performance with more agents, the practical implementation and efficiency of deploying large ensembles of LLM agents in real-world applications may present challenges.

## Tags
#agent #multi-agent #chainofthought 

# Annotations
multiple LLM agents are used to improve the performance of LLMs. For instance, LLM-Debate (Du et al., 2023) employs multiple LLM agents in a debate form.  The reasoning performance is improved by creating a framework that allows more than one agent to “debate” the final answer of arithmetic tasks. They show performance improvements compared to using one single agent.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/ER5TA87U?page=1&annotation=RNAVYAHM)



Debate (Du et al., 2023), the authors have reported a preliminary curve: the accuracy of a math problem increases with the number of debating agents (although the number was simply increased from 1 to 7).” Yellow Highlight [Page 1](zotero://open-pdf/library/items/ER5TA87U?page=1&annotation=TCBWR6PM)



involving more chains-of-thought pipelines (termed as a “sample-and-marginalize” decoding procedure), can lead to a performance gain.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/ER5TA87U?page=1&annotation=4STAB29H)



we conduct the first comprehensive study on the scaling property of LLM agents.  To dig out the potential of multiple agents, we propose to use a simple(st) sampling-and-voting method, which involves two phases. First, the query of the task, i.e., the input to an LLM, is iteratively fed into a single LLM, or a multiple LLM-Agents collaboration framework, to generate multiple outputs. Subsequently, majority voting is used to determine the final result” Yellow Highlight [Page 1](zotero://open-pdf/library/items/ER5TA87U?page=1&annotation=ENYX2ZKR)



LLM performance can generally be improved by increasing the ensemble size, i.e., the number of agents, across a wide range of tasks. Surprisingly, a brute-force ensemble of smaller LLMs can achieve comparable or superior performance to larger LLMs” Yellow Highlight [Page 2](zotero://open-pdf/library/items/ER5TA87U?page=2&annotation=BHAQPA6Z)



comparable performance can be achieved without the need for additional handcraft prompt design or complex collaboration frameworks.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/ER5TA87U?page=2&annotation=XYGXMITI)



We classify difficulty into three dimensions: the inherent difficulty, the length of reasoning steps, and the prior probability of the correct answer” Yellow Highlight [Page 2](zotero://open-pdf/library/items/ER5TA87U?page=2&annotation=PFBMSL5E)



We present the first systematic study on the scaling property of raw agents instantiated by LLMs. We find that the performance scales with the increase of agents, using the simple(st) way of sampling and voting.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/ER5TA87U?page=2&annotation=T36CEEB8)



We explore the compatibility of our method with existing complicated methods that stimulate the potential of LLMs, revealing that our method can enhance these methods to achieve further performance improvements” Yellow Highlight [Page 2](zotero://open-pdf/library/items/ER5TA87U?page=2&annotation=L4HMPC43)



We analyze the effectiveness of our method in tackling problems at varying difficulties and then distill the properties behind, based upon which, we propose further optimization methods that can facilitate the occurrence of our finding.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/ER5TA87U?page=2&annotation=I7LWU88N)



1) LLM self-ensemble (Wang et al., 2023b), which attempts to harness multiple outputs from homogeneous LLMs to assemble the final answer; 2) heterogeneous LLM ensemble, which focuses on combining heterogeneous LLMs through supervised learning to improve performance across various downstream applications; and 3) multiple LLM agents collaboration, which improves performance through interactions among LLM agents. We discuss these works below.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/ER5TA87U?page=2&annotation=LC9CSFJ3)



Very recently, Lu et al. (2024) proposes a method named Blended that utilizes multiple LLMs for chat scenarios. In contrast, Blended focuses on utilizing the power of multiple LLMs, whereas our focus is on the scaling trend of adding more LLMs” Yellow Highlight [Page 2](zotero://open-pdf/library/items/ER5TA87U?page=2&annotation=P27HJDV3)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liMoreAgentsAll2024/image-3-x30-y507.png]]



LLM Algorithm 1 Sampling-and-voting Require: Query x, number of samples N, LLM M or LLM integrated with other methods fM(x) 1: Initialize an empty set for samples S ← ∅ 2: for i = 1 to N do 3: Generate sample si ← M(x) or si ← fM(x) 4: Add sample to the set S ← S ∪ {si} 5: end for 6: for each sample si in S do 7: Initialize similarity scores V (si) ← 0 8: for each sample sj in S do 9: if i ̸= j then 10: V (si) ← V (si) + sim(si, sj ) 11: end if 12: end for 13: end for 14: A ← arg maxsi∈S V (si) 15: return A” Yellow Highlight [Page 3](zotero://open-pdf/library/items/ER5TA87U?page=3&annotation=FYWW6PE3)



Sampling. Let x represent the task query and M denote an LLM. In this phase, we generate N samples by solely querying the LLM M N times with each sample represented as s = M(x) or by integrating with other methods fM with N times executions where each sample is denoted as s = fM(x). We obtain a set of samples S = {s1, s2, ..., sN } at the end of this phase.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/ER5TA87U?page=3&annotation=RBZQ58H4)



Voting. Let A represent the final answer. In this phase, we employ majority voting to consolidate the response sample set S into the final answer A. This involves calculating the cumulative similarity for each sample relative to the others, denoted as V (si) = PN j=1,j̸=i sim(si, sj ). For open-ended generation tasks such as code generation, the BLEU score (Papineni et al., 2002) is utilized to quantify similarity. Conversely, for close-ended tasks like multiple-choice questions, similarity is measured by occurrence frequency. The sample that exhibits the highest cumulative similarity is then chosen as the final answer denoted as A = arg maxsi∈S V (si).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/ER5TA87U?page=3&annotation=5UL23DDQ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liMoreAgentsAll2024/image-5-x35-y533.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liMoreAgentsAll2024/image-5-x34-y386.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liMoreAgentsAll2024/image-5-x31-y187.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liMoreAgentsAll2024/image-6-x48-y605.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liMoreAgentsAll2024/image-6-x294-y404.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liMoreAgentsAll2024/image-8-x29-y577.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liMoreAgentsAll2024/image-8-x29-y405.png]]



In this paper, we report that more agents is all you need, i.e., simply adding more instantiated LLM agents is what you need to obtain a better LLM performance in processing complex tasks, without bothering complicated methods, such as CoT pipelines, multi-agent collaboration frameworks, etc.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/ER5TA87U?page=8&annotation=REPIJBAD)



our simple sampling-and-voting method for instantiating agents can generally improve the performance of LLMs by increasing the ensemble size. Importantly, this method is orthogonal to different existing methods, which can lead to further improvements when combined with them.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/ER5TA87U?page=8&annotation=AMVPEYEW)



we observe that the performance gains are influenced by the difficulty of the task” Yellow Highlight [Page 8](zotero://open-pdf/library/items/ER5TA87U?page=8&annotation=FZHVHF8L)




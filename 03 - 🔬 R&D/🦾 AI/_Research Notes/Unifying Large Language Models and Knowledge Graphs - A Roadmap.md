---
Publish Year: "2024"
Authors: Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, Xindong Wu
URL: http://arxiv.org/abs/2306.08302
Zotero Link: zotero://select/library/items/Q38W4F88
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#knowledgegraph"
Published:
---
# Unifying Large Language Models and Knowledge Graphs - A Roadmap

## Purpose
The research was initiated to address the limitations of Large Language Models (LLMs) in terms of interpretability, reasoning, and knowledge representation. It aims to explore the integration of Knowledge Graphs (KGs) with LLMs to enhance their performance and applicability in various tasks. This integration is significant in the field of Computer Science, particularly in Artificial Intelligence and Computation and Language.

## Methods
- Highlighting the limitations of LLMs and the advantages of incorporating KGs.
- Proposing a unified framework that synergizes LLMs and KGs across four layers: Data, Synergized Model, Technique, and Application.
- Discussing various methods for integrating KGs into LLMs, including training objectives, input modifications, and instruction-tuning.
- Exploring different types of KGs (encyclopedic, commonsense, domain-specific, and multi-modal) and their roles in enhancing LLMs.

## Key Findings
- LLMs and KGs can mutually enhance each other, with KGs providing structured, interpretable knowledge and reasoning capabilities to LLMs.
- A unified framework for integrating LLMs and KGs can significantly improve performance in knowledge representation and reasoning tasks.
- Incorporating KGs into LLMs can address issues of interpretability and reasoning, but challenges remain in handling low-frequency entities and ensuring the model's adaptability to new knowledge.
- Various methods, including KG embedding, KG completion, and KG construction, have been developed to facilitate the integration of KGs into LLMs.

## Discussion
The discussion highlights the potential of integrating LLMs with KGs to overcome the limitations of each approach when used independently. This integration can lead to more interpretable, reliable, and efficient AI systems capable of complex reasoning and knowledge representation. The research suggests that this synergy could revolutionize fields such as search engines, recommender systems, and AI assistants by providing more accurate and contextually relevant results.

## Critiques
- The research primarily focuses on the theoretical framework and potential applications without providing extensive empirical evidence of the effectiveness of the proposed integration.
- There is a lack of discussion on the scalability of the unified framework, especially when dealing with vast and complex KGs.
- The adaptability of the integrated system to new, evolving knowledge without retraining is mentioned as a challenge, but solutions to this issue are not thoroughly explored.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Computation-and-Language
- #knowledgegraph
- #LargeLanguageModels
- #KnowledgeGraphIntegration

# Annotations
![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-1-x300-y229.png]]



As black-box models, LLMs are also criticized for their lack of interpretability. LLMs represent knowledge implicitly in their parameters. It is difficult to interpret or validate the knowledge obtained by LLMs. Moreover, LLMs perform reasoning by a probability model, which is an indecisive process [16]. The specific patterns and functions LLMs used to arrive at predictions or decisions are not directly accessible or explainable to humans [17]. Even though some LLMs are equipped to explain their predictions by applying chain-of-thought [29], their reasoning explanations also suffer from the hallucination issue [30].” Yellow Highlight [Page 2](zotero://open-pdf/library/items/55YGY4B5?page=2&annotation=96PMY5QQ)



To address the above issues, a potential solution is to incorporate knowledge graphs (KGs) into LLMs. Knowledge graphs (KGs), storing enormous facts in the way of triples, i.e., (head entity, relation, tail entity), are a structured and decisive manner of knowledge representation” Yellow Highlight [Page 2](zotero://open-pdf/library/items/55YGY4B5?page=2&annotation=HP4IG739)



they are renowned for their symbolic reasoning ability [22], which generates interpretable results.  KGs can also actively evolve with new knowledge continuously added in [24]. Additionally, experts can construct domain-specific KGs to provide precise and dependable domain-specific knowledge [23].” Yellow Highlight [Page 2](zotero://open-pdf/library/items/55YGY4B5?page=2&annotation=Z7PK3NTP)



LLMs and KGs are inherently interconnected and can mutually enhance each other. In KG-enhanced LLMs, KGs can not only be incorporated into the pre-training and inference stages of LLMs to provide external knowledge [35]–[37], but also used for analyzing LLMs and providing interpretability [14], [38], [39]” Yellow Highlight [Page 2](zotero://open-pdf/library/items/55YGY4B5?page=2&annotation=X7WPCCSK)



In LLM-augmented KGs, LLMs have been used in various KG-related tasks, e.g., KG embedding [40], KG completion [26], KG construction [41], KG-to-text generation [42], and KGQA [43], to improve the performance and facilitate the application of KGs” Yellow Highlight [Page 2](zotero://open-pdf/library/items/55YGY4B5?page=2&annotation=5ZTCHYBE)



Synergized LLM + KG, researchers marries the merits of LLMs and KGs to mutually enhance performance in knowledge representation [44] and reasoning [45], [46]” Yellow Highlight [Page 2](zotero://open-pdf/library/items/55YGY4B5?page=2&annotation=2VPNQMWS)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-3-x32-y470.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-3-x38-y328.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-4-x43-y546.png]]



Encyclopedic knowledge graphs are the most ubiquitous KGs, which represent the general knowledge in real-world.  Encyclopedic knowledge graphs are often constructed by integrating information from diverse and extensive sources, including human experts, encyclopedias, and databases.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/55YGY4B5?page=4&annotation=XM4QNUQT)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-4-x298-y387.png]]



Commonsense knowledge graphs formulate the knowledge about daily concepts, e.g., objects, and events, as well as their relationships [70]. Compared with encyclopedic knowledge graphs, commonsense knowledge graphs often model the tacit knowledge extracted from text such as (Car, UsedFor, Drive).” Yellow Highlight [Page 4](zotero://open-pdf/library/items/55YGY4B5?page=4&annotation=GQEVD8DS)



Domain-specific knowledge graphs are often constructed to represent knowledge in a specific domain, e.g., medical, biology, and finance [23]. Compared with encyclopedic knowledge graphs, domain-specific knowledge graphs are often smaller in size, but more accurate and reliable” Yellow Highlight [Page 5](zotero://open-pdf/library/items/55YGY4B5?page=5&annotation=XFEC8ZTD)



Unlike conventional knowledge graphs that only contain textual information, multi-modal knowledge graphs represent facts in multiple modalities such as images, sounds, and videos [83]” Yellow Highlight [Page 5](zotero://open-pdf/library/items/55YGY4B5?page=5&annotation=WEJKRZLY)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-6-x40-y471.png]]



fi  To further explore the unification, we propose a unified framework of the synergized LLMs + KGs in Fig. 7. The unified framework contains four layers: 1) Data, 2) Synergized Model, 3) Technique, and 4) Application.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/55YGY4B5?page=6&annotation=25CNIHV9)



In the Data layer, LLMs and KGs are used to process the textual and structural data, respectively.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/55YGY4B5?page=6&annotation=SZHZYHXF)



Technique layer, related techniques that have been used in LLMs and KGs can be incorporated into this framework to further enhance the performance.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/55YGY4B5?page=6&annotation=RJJN6U5W)



In the Application layer, LLMs and KGs can be integrated to address various realworld applications, such as search engines [100], recommender systems [10], and AI assistants [101].” Yellow Highlight [Page 6](zotero://open-pdf/library/items/55YGY4B5?page=6&annotation=69KX6G7E)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-7-x40-y442.png]]



Existing large language models mostly rely on unsupervised training on the large-scale corpus. While these models may exhibit impressive performance on downstream tasks, they often lack practical knowledge relevant to the real world.  Previous works that integrate KGs into large language models can be categorized into three parts: 1) Integrating KGs into training objective, 2) Integrating KGs into LLM inputs, and 3) KGs Instruction-tuning.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/55YGY4B5?page=7&annotation=G5BD255C)



GLM [102] leverages the knowledge graph structure to assign a masking probability. Specifically, entities that can be reached within a certain number of hops are” Yellow Highlight [Page 7](zotero://open-pdf/library/items/55YGY4B5?page=7&annotation=JDBPVMNB)



considered to be the most important entities for learning, and they are given a higher masking probability during pre-training. Furthermore, E-BERT [103] further controls the balance between the token-level and entity-level training losses. The training loss values are used as indications of the learning process for token and entity, which dynamically determines their ratio for the next training epochs. SKEP [124] also follows a similar fusion to inject sentiment knowledge during LLMs pre-training. SKEP first determines words with positive and negative sentiment by utilizing PMI along with a predefined set of seed sentiment words. Then, it assigns a higher masking probability to those identified” Yellow Highlight [Page 7](zotero://open-pdf/library/items/55YGY4B5?page=7&annotation=TE2SXGZ6)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-8-x41-y583.png]]



ERNIE feeds both sentences and corresponding entities mentioned in the text into LLMs, and then trains the LLMs to predict alignment links between textual tokens and entities in knowledge graphs” Yellow Highlight [Page 8](zotero://open-pdf/library/items/55YGY4B5?page=8&annotation=WA2B8KXM)



KEPLER [40] directly employs both knowledge graph embedding training objective and Masked token pre-training objective into a shared transformer-based encoder” Yellow Highlight [Page 8](zotero://open-pdf/library/items/55YGY4B5?page=8&annotation=UM84SQ9V)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-8-x308-y543.png]]



The above methods can indeed inject a large amount of knowledge into LLMs. However, they mostly focus on popular entities and overlook the low-frequent and longtail ones. DkLLM [108] aims to improve the LLMs representations towards those entities. DkLLM first proposes a novel measurement to determine long-tail entities and then replaces these selected entities in the text with pseudo token embedding as new input to the large language models.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/55YGY4B5?page=8&annotation=IEW9XT58)



Instead of injecting factual knowledge into LLMs, the KGs Instruction-tuning aims to fine-tune LLMs to better comprehend the structure of KGs and effectively follow user instructions to conduct complex tasks.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/55YGY4B5?page=8&annotation=CVHNWSA3)



real-world knowledge is subject to change and the limitation of these approaches is that they do not permit updates to the incorporated knowledge without retraining the model. As a result, they may not generalize well to the unseen knowledge during inference [126]. Therefore, considerable research has been devoted to keeping the knowledge space and text space separate and injecting the knowledge while inference. These methods mostly focus on the Question Answering (QA) tasks, because QA requires the model to capture both textual semantic meanings and up-to-date real-world knowledge.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/55YGY4B5?page=9&annotation=QPX57A2U)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-9-x310-y615.png]]



Li et al. [64] adopt the pre-defined template to convert each triple into a short sentence, which can be understood by LLMs for reasoning. Mindmap [65] designs a KG prompt to convert graph structure into a mind map that enables LLMs to perform reasoning by consolidating the facts in KGs and the implicit knowledge from LLMs. ChatRule [116] samples several relation paths from KGs, which are verbalized and fed into LLMs. Then, LLMs are prompted to generate meaningful logical rules that can be used for reasoning. CoK [117] proposes a chain-of-knowledge prompting that uses a sequence of triples to elicit the reasoning ability of LLMs to reach the final answer.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/55YGY4B5?page=9&annotation=3P75NQ5I)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-10-x40-y609.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-10-x309-y578.png]]



LAMA [14] is the first work to probe the knowledge in LLMs by using KGs. As shown in Fig. 12, LAMA first converts the facts in KGs into cloze statements by a predefined prompt template and then uses LLMs to predict the missing entity. The prediction results are used to evaluate the knowledge stored in LLMs. For example, we try to probe whether LLMs know the fact (Obama, profession, president). We first convert the fact triple into a cloze question “Obama’s profession is .” with the object masked. Then, we test if the LLMs can predict the object “president” correctly.” Yellow Highlight [Page 10](zotero://open-pdf/library/items/55YGY4B5?page=10&annotation=8574SAT2)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-11-x307-y546.png]]



Knowledge graph embedding (KGE) aims to map each entity and relation into a low-dimensional vector (embedding) space. These embeddings contain both semantic and structural information of KGs, which can be utilized for various tasks such as question answering [180], reasoning [38], and recommendation [181]. Conventional knowledge graph embedding methods mainly rely on the structural information of KGs to optimize a scoring function defined on embeddings” Yellow Highlight [Page 11](zotero://open-pdf/library/items/55YGY4B5?page=11&annotation=ZJQP36HZ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-12-x44-y602.png]]



Nayyeri et al. [132] use LLMs to generate the world-level, sentence-level, and document-level representations. They are integrated with graph structure embeddings into a unified vector by Dihedron and Quaternion representations of 4D hypercomplex numbers.” Yellow Highlight [Page 12](zotero://open-pdf/library/items/55YGY4B5?page=12&annotation=5KKTV3M7)



CoDEx [134] presents a novel loss function empowered by LLMs that guides the KGE models in measuring the likelihood of triples by considering the textual information. The proposed loss function is agnostic to mode” Yellow Highlight [Page 12](zotero://open-pdf/library/items/55YGY4B5?page=12&annotation=J43BBINS)



Instead of using KGE model to consider graph structure, another line of methods directly employs LLMs to incorporate both the graph structure and textual information into the embedding space simultaneously. As shown in Fig. 15, kNN-KGE [136] treats the entities and relations as special tokens in the LLM” Yellow Highlight [Page 12](zotero://open-pdf/library/items/55YGY4B5?page=12&annotation=9QDYUIQA)



Knowledge Graph Completion (KGC) refers to the task of inferring missing facts in a given knowledge graph” Yellow Highlight [Page 12](zotero://open-pdf/library/items/55YGY4B5?page=12&annotation=K64BS4SP)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-13-x80-y527.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-13-x306-y504.png]]



GenKGC [96] uses the large language model BART [5] as the backbone model. Inspired by the in-context learning approach used in GPT-3 [59], where the model concatenates relevant samples to learn correct output answers, GenKGC proposes a relation-guided demonstration technique that includes triples with the same relation to facilitating the model’s learning process” Yellow Highlight [Page 13](zotero://open-pdf/library/items/55YGY4B5?page=13&annotation=5GAJHXT7)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-14-x45-y546.png]]



KG-S2S reformulates the standard triple KG fact by introducing an additional element, forming a quadruple (h, r, t, m), where m represents the additional ”condition” element. Although different KGC tasks may refer to different conditions, they typically have a similar textual format, which enables unification across different KGC tasks. The KG-S2S approach incorporates various techniques such as entity description, soft prompt, and Seq2Seq Dropout to improve the model’s performance.” Yellow Highlight [Page 14](zotero://open-pdf/library/items/55YGY4B5?page=14&annotation=EUANGDDR)



AutoKG adopts prompt engineering to design customized prompts [93]. As shown in Fig. 18, these prompts contain the task description, fewshot examples, and test input, which instruct LLMs to predict the tail entity for KG completion” Yellow Highlight [Page 14](zotero://open-pdf/library/items/55YGY4B5?page=14&annotation=28X37Z3D)



Knowledge graph construction involves creating a structured representation of knowledge within a specific domain.  This includes identifying entities and their relationships with each other. The process of knowledge graph construction typically involves multiple stages, including 1) entity discovery, 2) coreference resolution, and 3) relation extraction.  Fig 19 presents the general framework of applying LLMs for each stage in KG construction. More recent approaches have explored 4) end-to-end knowledge graph construction, which involves constructing a complete knowledge graph in one step or directly 5) distilling knowledge graphs from LLMs.” Yellow Highlight [Page 14](zotero://open-pdf/library/items/55YGY4B5?page=14&annotation=XGSPCNAZ)



Entity discovery in KG construction refers to the process of identifying and extracting entities from unstructured data sources, such as text documents, web pages, or social media posts, and incorporating them to construct knowledge graphs.” Yellow Highlight [Page 14](zotero://open-pdf/library/items/55YGY4B5?page=14&annotation=HWDV4D24)



Named Entity Recognition (NER) involves identifying and tagging named entities in text data with their positions and classifications. The named entities include people, organizations, locations, and other types of entities. The stateof-the-art NER methods usually employ LLMs to leverage their contextual understanding and linguistic knowledge for accurate entity recognition and classification.” Yellow Highlight [Page 14](zotero://open-pdf/library/items/55YGY4B5?page=14&annotation=RCYXSHUC)



1) Flat NER is to identify non-overlapping named entities from input text” Yellow Highlight [Page 14](zotero://open-pdf/library/items/55YGY4B5?page=14&annotation=9HY876VA)



2) Nested NER considers complex scenarios which allow a token to belong to multiple entities. T” Yellow Highlight [Page 14](zotero://open-pdf/library/items/55YGY4B5?page=14&annotation=6RDBY92X)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-15-x29-y507.png]]



3) Discontinuous NER identifies named entities that may not be contiguous in the text.” Yellow Highlight [Page 15](zotero://open-pdf/library/items/55YGY4B5?page=15&annotation=X8AWDRS3)



Unlike the task-specific methods, GenerativeNER [149] uses a sequence-to-sequence LLM with a pointer mechanism to generate an entity sequence, wh” Yellow Highlight [Page 15](zotero://open-pdf/library/items/55YGY4B5?page=15&annotation=ZK77XNN5)



Entity Typing (ET) aims to provide fine-grained and ultra-grained type information for a given entity mentioned in context.” Yellow Highlight [Page 15](zotero://open-pdf/library/items/55YGY4B5?page=15&annotation=WPAKJ62H)



Entity Linking (EL), as known as entity disambiguation, involves linking entity mentions appearing in the text to their corresponding entities in a knowledge graph” Yellow Highlight [Page 15](zotero://open-pdf/library/items/55YGY4B5?page=15&annotation=GKTQ2KQN)



Coreference resolution is to find all expressions (i.e., mentions) that refer to the same entity or event in a text.” Yellow Highlight [Page 15](zotero://open-pdf/library/items/55YGY4B5?page=15&annotation=EA82CA7Z)



Cross-document CR refers to the sub-task where the mentions refer to the same entity or event might be across multiple documents.” Yellow Highlight [Page 15](zotero://open-pdf/library/items/55YGY4B5?page=15&annotation=6PJSKGRM)



Relation extraction involves identifying semantic relationships between entities mentioned in natural language text.” Yellow Highlight [Page 15](zotero://open-pdf/library/items/55YGY4B5?page=15&annotation=PT8LBEKB)



Sentence-level RE focuses on identifying relations between entities within a single sentence.” Yellow Highlight [Page 16](zotero://open-pdf/library/items/55YGY4B5?page=16&annotation=LV882I67)



Document-level RE (DocRE) aims to extract relations between entities across multiple sentences within a document.” Yellow Highlight [Page 16](zotero://open-pdf/library/items/55YGY4B5?page=16&annotation=SJ4X46HW)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-16-x304-y626.png]]



COMET [164] proposes a commonsense transformer model that constructs commonsense KGs by using existing tuples as a seed set of knowledge on which to train. Using this seed set, a LLM learns to adapt its learned representations to knowledge generation, and produces novel tuples that are high quality.” Yellow Highlight [Page 16](zotero://open-pdf/library/items/55YGY4B5?page=16&annotation=B7JUPHEQ)



The goal of Knowledge-graph-to-text (KG-to-text) generation is to generate high-quality texts that accurately and consistently describe the input knowledge graph information [228]. KG-to-text generation connects knowledge graphs and texts, significantly improving the applicability of KG in more realistic NLG scenarios, including storytelling [229] and knowledge-grounded dialogue [230]. However, it is challenging and costly to collect large amounts of graph-text parallel data, resulting in insufficient training and poor generation quality. Thus, many research efforts resort to either: 1) leverage knowledge from LLMs or 2) construct large-scale weakly-supervised KG-text corpus to solve this issue” Yellow Highlight [Page 16](zotero://open-pdf/library/items/55YGY4B5?page=16&annotation=3MZAEDND)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-17-x30-y603.png]]



Although LLMs have achieved remarkable empirical success, their unsupervised pre-training objectives are not necessarily aligned well with the task of KG-to-text generation, motivating researchers to develop large-scale KG-text aligned corpus” Yellow Highlight [Page 17](zotero://open-pdf/library/items/55YGY4B5?page=17&annotation=B4M2A7JG)



Chen et al. [171] also propose a KG-grounded text corpus collected from the English Wikidump. To ensure the connection between KG and text, they only extract sentences with at least two Wikipedia anchor links. Then, they use the entities from those links to query their surrounding neighbors in WikiData and calculate the lexical overlapping between these neighbors and the original sentences. Finally, only highly overlapped pairs are selected. The authors explore both graph-based and sequence-based encoders and identify their advantages in various different tasks and settings.” Yellow Highlight [Page 17](zotero://open-pdf/library/items/55YGY4B5?page=17&annotation=SB8RAG28)



Entity/relation extractors are designed to identify entities and relationships mentioned in natural language questions and retrieve related facts in KGs. Given the proficiency in language comprehension, LLMs can be effectively utilized for this purpose” Yellow Highlight [Page 17](zotero://open-pdf/library/items/55YGY4B5?page=17&annotation=3EMLE5ZB)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-18-x42-y545.png]]



To better guide LLMs reason through KGs, OreoLM [177] proposes a Knowledge Interaction Layer (KIL) which is inserted amid LLM layers. KIL interacts with a KG reasoning module, where it discovers different reasoning paths, and then the reasoning module can reason over the paths to generate answers” Yellow Highlight [Page 18](zotero://open-pdf/library/items/55YGY4B5?page=18&annotation=7UVTZLR2)



UniKGQA [43] unifies the facts retrieval and reasoning into a unified framework.  UniKGQA consists of two modules. The first module is a semantic matching module that uses a LLM to match questions with their corresponding relations semantically.  The second module is a matching information propagation module, which propagates the matching information along directed edges on KGs for answer reasoning. Similarly, ReLMKG [179] performs joint reasoning on a large language model and the associated knowledge graph. The question and verbalized paths are encoded by the language model, and different layers of the language model produce outputs that guide a graph neural network to perform message passing” Yellow Highlight [Page 18](zotero://open-pdf/library/items/55YGY4B5?page=18&annotation=QXKKHLEM)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-19-x38-y579.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-19-x309-y600.png]]



QA-GNN [131] proposes to use a GNN-based model to jointly reason over input context and KG information via message passing. Specifically, QA-GNN represents the input textual information as a special node via a pooling operation and connects this node with other entities in KG” Yellow Highlight [Page 19](zotero://open-pdf/library/items/55YGY4B5?page=19&annotation=TWBZFK7E)



Think-on-graph [240] provides a flexible plug-and-play framework where LLM agents iteratively execute beam searches on KGs” Yellow Highlight [Page 19](zotero://open-pdf/library/items/55YGY4B5?page=19&annotation=XBLGTXFI)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/panUnifyingLargeLanguage2024/image-20-x39-y594.png]]




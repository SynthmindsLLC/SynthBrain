---
Publish Year: "2023"
Authors: Wenhao Yu, Hongming Zhang, Xiaoman Pan, Kaixin Ma, Hongwei Wang, Dong Yu
URL: http://arxiv.org/abs/2311.09210
Zotero Link: zotero://select/library/items/SK5ED7MZ
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#RAG"
Published: 2024-03-19
---
# Summary
## Purpose 
This study introduces the Chain-of-Note (CON) framework, aimed at enhancing the robustness of Retrieval-Augmented Language Models (RALMs). The CON approach is designed to improve the model's performance in handling noisy, irrelevant documents and addressing unknown scenarios by generating sequential reading notes for each retrieved document.

## Methods 
- Introducing Chain-of-Note (CON) framework.
- Generating sequential reading notes for evaluating the relevance of retrieved documents.
- Employing ChatGPT for training data creation.
- Training on an LLaMa-2 7B model.
- Evaluating across open-domain QA benchmarks.

## Key Findings 
1. CON significantly outperforms standard RALMs.
2. Notable improvement in Exact Match (EM) score with noisy retrieved documents.
3. Enhanced rejection rates for real-time questions outside pre-training knowledge.
4. Effective in handling both noisy and unknown scenarios.

## Discussion 
The CON framework marks a significant advancement in RALMs, particularly in its robustness against misinformation and its ability to handle queries outside its training scope. This is crucial for AI reliability, especially in scenarios where incorrect or misleading information can have serious implications.

## Critiques 
1. The reliance on external datasets for training may limit the model's adaptability to newer, unexplored domains.
2. Potential for further optimization in the integration of sequential reading notes with the model's inherent knowledge base.
3. Exploration of more diverse and complex datasets could strengthen the model's robustness.

## Tags
#AI #RetrievalAugmentedLanguageModels #Robustness #ChainOfNote #NaturalLanguageProcessing


# Annotations
In a typical RALM setup, a query is first processed by a retriever that searches a vast evidence corpus for pertinent documents. A reader then examines these documents, extracting useful information and formulating the final output answer.  The potential benefit of the RALM framework is its ability to integrate relevant external knowledge, thereby enriching the LLMs’ understanding of input text and generating answers based on this information. T” Yellow Highlight [Page 1](zotero://open-pdf/library/items/HE2JDUAZ?page=1&annotation=J9YMHYWQ)



there exist several issues with the current RALM framework. First, there is no guarantee that the information retrieval (IR) system will always yield the most pertinent or trustworthy information.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/HE2JDUAZ?page=1&annotation=TQ8ING9V)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/yuChainofNoteEnhancingRobustness2023/image-2-x105-y543.png]]



In cases where knowledge is insufficient, the system should respond with “unknown” when the answer cannot be determined.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HE2JDUAZ?page=2&annotation=542NU2JG)



Noise Robustness: The ability of a RALM to discern and disregard noisy information present in irrelevant retrieved documents, while appropriately leveraging its intrinsic knowledge.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HE2JDUAZ?page=2&annotation=VE9VPDTB)



Unknown Robustness: The capacity of a RALM to acknowledge its limitations by responding with “unknown” when given a query it does not have the corresponding knowledge to answer, and the relevant information is not found within the retrieved documents.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HE2JDUAZ?page=2&annotation=PRJE2RZQ)



CHAIN-OF-NOTING (CON), designed to enhance the robustness of RALMs. The cornerstone of CON is to generate a series of reading notes for retrieved documents, enabling a comprehensive assessment of their relevance to the input query” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HE2JDUAZ?page=2&annotation=BGIP2ZJH)



To validate the effectiveness of the CON idea, we first prompt ChatGPT (OpenAI, 2023) to generate a 10K training data based on questions collected from Natural Questions (NQ) (Kwiatkowski et al., 2019). Subsequently, we trained a LLaMa-2 7B model to incorporate the note-taking ability integral to CON” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HE2JDUAZ?page=2&annotation=GP3JI7MR)



Our experiments demonstrate that CHAIN-OF-NOTE (CON) not only improves overall QA performance when employed with DPR-retrieved documents but also significantly enhances robustness in both noise and unknown aspects.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HE2JDUAZ?page=2&annotation=JDI84KX5)



Another line of RALMs such as kNN-LM (Khandelwal et al., 2020; Zhong et al., 2022) retrieves a set of tokens and interpolates between the next token distribution and kNN distributions computed from the retrieved tokens at inference” Yellow Highlight [Page 3](zotero://open-pdf/library/items/HE2JDUAZ?page=3&annotation=YMXT2R7F)



Notably, Creswell et al.  (2022) demonstrated that incorporating random or irrelevant contexts could adversely affect QA performance. In contrast, Shi et al. (2023a) discovered that adding irrelevant context to exemplars or task-specific instructions can sometimes enhance model performance, implying that models might intrinsically possess capabilities, developed during pre-training, to manage such scenarios.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/HE2JDUAZ?page=3&annotation=Z9XXWQSZ)



there has been a surge in the development of other chain-of-X methods, addressing diverse challenges in LLM applications. These include chain-of-explanation (Huang et al., 2023), chain-of-knowledge (Wang et al., 2023a), chain-of- verification (Dhuliawala et al., 2023) and IR chain-of-thought (Trivedi et al., 2023)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/HE2JDUAZ?page=3&annotation=3G7H4YPB)



Chain-of-Verification (Dhuliawala et al., 2023) generates an initial response, formulates verification questions, and revises the response based on these questions, reducing factual errors and hallucina- tions in the response.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/HE2JDUAZ?page=3&annotation=5MR6HEYU)



Specifically, CON framework generates sequential reading notes for the retrieved documents, which enables a systematic evaluation of the relevance and accuracy of information retrieved from external documents.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/HE2JDUAZ?page=3&annotation=U789DABX)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/yuChainofNoteEnhancingRobustness2023/image-4-x101-y407.png]]



the existing RALMs suffer from several limitations: • Risk of Surface-Level Processing: When directly generating an answer, language models might rely on surface-level information without deep comprehension. Thus, language models could easily overlook the nuances of question or documents, particularly in complex or indirect questions.  • Difficulty in Handling Contradictory Information: When faced with documents containing contra- dictory information, directly generating an answer becomes challenging. The model may struggle to resolve these contradictions or to determine which piece of information is more credible or relevant.  • Reduced Transparency and Interpretability: Direct answer generation offers limited insight into how the model arrived at its conclusion. This lack of transparency makes it challenging for users to understand the basis of the model’s conclusions.  • Overdependence on Retrieved Documents: Direct generation can lead to an overreliance on the content of the retrieved documents (i.e. tendency to extract information from retrieved documents (Shi et al., 2023a)), ignoring the model’s inherent knowledge base. This can be particularly limiting when the retrieved documents are noisy or out-of-date.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/HE2JDUAZ?page=4&annotation=AJVVS64W)



Specifically, it involves generating concise and contextually relevant summaries or notes for each document. This method allows the model to systematically evaluate the relevance and accuracy of information drawn from external documents.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/HE2JDUAZ?page=5&annotation=6LN8FLBW)



when a document directly answers the query, the model formulates the final response based on this information” Yellow Highlight [Page 5](zotero://open-pdf/library/items/HE2JDUAZ?page=5&annotation=P3N97KBF)



Second, if the retrieved document does not directly answer the query but provides useful context, the model leverages this information along with its inherent knowledge to deduce an answer,” Yellow Highlight [Page 5](zotero://open-pdf/library/items/HE2JDUAZ?page=5&annotation=9RDCHDFC)



in cases where the retrieved documents are irrelevant, and the model lacks sufficient knowledge to answer, it defaults to responding with “unknown”” Yellow Highlight [Page 5](zotero://open-pdf/library/items/HE2JDUAZ?page=5&annotation=QLGGKUI8)



Weighted Loss on Notes and Answers. A unique aspect of our training approach is the implementa- tion of a weighted loss strategy. This involves varying the loss weights assigned to reading notes and answers. In our preliminary studies, We observed that assigning equal loss to both components can reduce the quality of the final answer and prolong the training time for convergence.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/HE2JDUAZ?page=5&annotation=R2R6FTS5)




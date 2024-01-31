---
Publish Year: "2023"
Authors: Ahtsham Zafar, Venkatesh Balavadhani Parthasarathy, Chan Le Van, Saad Shahid, Aafaq Iqbal khan, Arsalan Shahid
URL: http://arxiv.org/abs/2308.13534
Zotero Link: zotero://select/library/items/HYSDCMVK
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
Published:
---
# Summary
## Purpose

## Methods

## Key Findings

## Discussion

## Critiques

# Annotations
Despite the substantial advancements in LLMs and their growing prevalence in various applications, several inherent limitations and challenges remain. These include: • Hallucination: LLMs may generate information that is coher- ent but factually incorrect or misaligned with the underlying data.  • Trustworthiness: Ensuring the reliability and integrity of generated content poses a complex challenge.  • Explainability: The vast number of parameters and complex structures in LLMs often hinder clear understanding and interpretation of the models’ decision-making processes.  • Untraining Ability: Modifying or retracting specific knowl- edge in an LLM without retraining the entire model remains an open challenge.  • Privacy and Ethical Awareness: Addressing concerns related to data privacy and ethical considerations in the application of” Yellow Highlight [Page 1](zotero://open-pdf/library/items/2945QZPT?page=1&annotation=FWIIKA97)



![[image-2-x21-y419.png]]



A. Pretraining During pretraining: • A vast amount of unlabeled data is gathered from diverse online sources, which might encompass trillions of tokens from articles, web pages, and books.  • Preprocessing procedures, such as tokenization, lowercasing, and special character removal, are applied. Tokenization might operate at the word or subword level.  • The popular choice for LLM training is the transformer architecture. This phase is computationally demanding, often requiring robust GPUs or TPUs and incurring significant time and cost.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/2945QZPT?page=2&annotation=JQ4RNYPM)



B. Supervised Fine-tuning Post pretraining, LLMs are fine-tuned using labeled datasets.  They build upon the patterns discerned from pretraining, and re- fining for specific tasks. Notably, fine-tuning requires less data and computational power than building models anew. It has exhibited” Yellow Highlight [Page 2](zotero://open-pdf/library/items/2945QZPT?page=2&annotation=C4SSTFCI)



![[image-3-x19-y337.png]]



proficiency across a multitude of NLP tasks [33], [34], [35], owing to the marriage of broad linguistic knowledge from pretraining with task-focused adjustments.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/2945QZPT?page=3&annotation=AIKHV35L)



C. Dialogue Optimization The essence of dialogue optimization is refining the interaction between AI and users. The optimization has several facets: • Language Understanding: Amplifying the AI’s prowess in grasping user inputs, encompassing intent detection and se- mantic interpretation.  • Response Generation: Enhancing the model’s ability to craft context-aware, fluent replies, which might be diverse or user- tailored.  • Context Management: Upholding a consistent conversational context, encompassing dialogue history tracking and coher- ence maintenance.  • Error Management: Implementing mechanisms to detect and rectify mistakes or to address ambiguous inputs.  • User Feedback: Integrating user feedback loops to finetune and uplift the overall user experience.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/2945QZPT?page=3&annotation=TKZ6T3TQ)



D. Reward Model Subsequent to supervised fine-tuning, the model produces an array of possible replies for a prompt. Human evaluators rank these based on quality. For further refinement, each response might be appended with a reward token. Although this process refines model outputs, it is labor-intensive and demands meticulous data curation.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/2945QZPT?page=3&annotation=A9JASG7H)



E. Reinforcement Learning from Human Feedback (RLHF) RLHF marries three steps: LLM pretraining, human preference- based reward model training, and reinforcement learning-guided LLM fine-tuning. Despite its efficacy, RLHF has its challenges, including the cost of obtaining human feedback and potential risks associated with producing detrimental or false content.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/2945QZPT?page=3&annotation=PA3N28JG)



![[image-4-x307-y588.png]]



A. Social and Ethical Implications Democratization of Information: LLMs’ open-source availability has broadened AI access, spurring innovation among diverse users [39]. Despite the slight quality lead of tech giants, open-source models present compelling alternatives, shifting the industry’s land- scape. Notably, personal LLMs, like LoRA [40], allow efficient internal data handling and quick model fine-tuning.  Bias and Fairness: Complexity in LLMs introduces misuse and bias risks. Addressing these necessitates diverse development teams and thorough bias audits to ensure fairness.  Digital Divide: Disparities in LLM access can widen societal digital divides. Addressing this requires promoting technology access and LLM education [41].  Responsible AI Development: Balancing LLM benefits against risks demands collaboration among varied stakeholders. Trans- parency, robust data governance, and educational initiatives can shape responsible LLM use.  Algorithmic Transparency: The ”black box” nature of LLMs challenges trust and understanding. Research into LLM explain- ability and user-friendly output interpretations is essential.  Mitigating Harmful Content: Ensuring diverse training data and implementing watermarking can curb harmful LLM outputs.  Oversight mechanisms, both algorithmic and human, can bolster responsible LLM deployment [42].” Yellow Highlight [Page 4](zotero://open-pdf/library/items/2945QZPT?page=4&annotation=RMUAUSDG)



B. Legal, Privacy, and Regulatory Perspective Data Protection and Privacy Laws: LLMs must adhere to regu- lations like GDPR while preventing unintentional data disclosure.  Recent regulatory shifts, like the ”EU AI ACT” [43] and proposed Chinese regulations, emphasize responsible generative AI use.  Intellectual Property Considerations: LLMs’ capacity to gener- ate human-like text challenges copyright norms. Addressing this requires clear intellectual property guidelines and plagiarism de- tection tools [44].” Yellow Highlight [Page 4](zotero://open-pdf/library/items/2945QZPT?page=4&annotation=GEVZWSPH)



Physiological Perspectives Human-Computer Interaction: LLM-based Conversational Agents carry potential risks, including undue trust, psychological vulnerabilities, and design biases. Promoting responsible design and prioritizing user privacy is paramount” Yellow Highlight [Page 4](zotero://open-pdf/library/items/2945QZPT?page=4&annotation=2I5YP865)



![[image-5-x20-y111.png]]



![[image-6-x20-y150.png]]



A. Market Size of LLMs and Driving Factors The global Natural Language Processing (NLP) market is pro- jected to surpass 91 billion USD by 2030, expanding at a CAGR of 27% [46]. A major driving force behind this growth is the influence of Large Language Models (LLMs). While exact market figures for LLMs remain elusive, certain factors listed in Table I hint at their increasing dominance. Despite the absence of precise market data, it is evident that the sector demonstrates substantial potential and is set to continue expanding across various industries.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/2945QZPT?page=6&annotation=CWBPMMM3)



applied challenges in the development of LLMs include: • Disinformation Generation: LLMs can generate convincing misinformation, undermining information credibility and lead- ing to potential harm.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/2945QZPT?page=6&annotation=5NQCMNHL)



![[image-7-x310-y553.png]]



![[image-7-x0-y549.png]]



![[image-7-x12-y344.png]]



![[image-7-x14-y122.png]]



Deepfakes Creation: LLMs can produce sophisticated manip- ulated media, posing threats of deception and public manipu- lation.  • Privacy and Data Concerns: Handling vast training data introduces privacy vulnerabilities, potentially culminating in breaches and unintentional sensitive data exposure.  • Bias Amplification: LLMs might reflect and amplify biases” Yellow Highlight [Page 7](zotero://open-pdf/library/items/2945QZPT?page=7&annotation=VXGZGWYR)



![[image-7-x319-y395.png]]



![[image-7-x305-y136.png]]



Malicious Usage: LLMs can be tailored to produce harmful, offensive, or abusive content, potentially instigating hate or targeted assaults.  • Unintended Outcomes: Outputs from LLMs can occasionally have unexpected ramifications or ethical concerns, underscor- ing the need for careful oversight and guidelines.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/2945QZPT?page=7&annotation=I7JIB7KH)



![[image-8-x16-y546.png]]



![[image-8-x15-y302.png]]



However, the evolution of privacy-aware LLM models could redefine numerous industrial landscapes” Yellow Highlight [Page 8](zotero://open-pdf/library/items/2945QZPT?page=8&annotation=VJB9UQG6)



Integrating Knowledge Graphs (KGs) [47] with LLMs offers a solution to these challenges by coupling the structured knowledge representation of KGs with the linguistic proficiency of LLMs.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/2945QZPT?page=8&annotation=P3IKZ2X2)



Role-Based Access Control (RBAC)” Yellow Highlight [Page 8](zotero://open-pdf/library/items/2945QZPT?page=8&annotation=8J8ZVJVN)



KGs: – Deliver structured and validated domain-specific knowl- edge.  – Enhance system explainability by tracing the origin of information.  – Complement LLMs by addressing gaps in domain-specific expertise.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/2945QZPT?page=8&annotation=ZGUISYC9)



RBAC: – Ensure data privacy through controlled access mecha- nisms.  – Align AI system usage with organizational policies and compliance mandates.  – Offer a methodical approach to managing data access, advancing security.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/2945QZPT?page=8&annotation=NH6VCTSD)



AI NewsHub Dataset Description: The AI NewsHub dataset is a systematically aggregated collection of news articles, procured daily from web crawling and search engines, and stored within a re- lational database system. Each record within this dataset represents an article and encapsulates the following attributes: identifier (ID), title, article content, published date, publisher name, and associated country of origin. Upon acquisition, articles undergo an analytical phase wherein they are classified based on their relevant topics, affiliated industry sectors, and originating publishers’ categories.  2) Construction of the AI NewsHub-based KG:: The structural organization of KG facilitates the extraction of nuanced insights, supports decision-making processes, and aids in the identification of concealed patterns within the data.  The KG derived from the AI NewsHub dataset comprises two primary node classes: articles and topics. The ’article’ node encom- passes attributes such as ID, content, sentiment analysis results, and a multi-dimensional matrix or vector array.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/2945QZPT?page=8&annotation=I93IRL6I)



Storage and management of this KG are facilitated through Neo4j, with queries being structured using the Cypher language.  Neo4j and Cypher: Neo4j [51], a premier graph database management platform, is adept at administering and querying intricate KGs. Given our emphasis on discerning the intricate interconnectedness of data, Neo4j is an optimal and open-source choice. In tandem with Cypher [52] — its dedicated query language — Neo4j empowers us to model multifaceted relationships, navigate patterns, and distil valuable insights from the KG. Cypher’s design emphasizes human- readable syntax, ensuring that users can structure and interpret complex queries with relative ease” Yellow Highlight [Page 9](zotero://open-pdf/library/items/2945QZPT?page=9&annotation=5IPBW5WR)



The detailed sequence of operations in the system is described as follows: • Step 1: The User (U) communicates a specific request to the RBAC Service (S).  • Step 2: The RBAC Service (S) evaluates the permissions associated with the user, forwarding the request to the Access Control (AC). AC determines the user’s data access rights.  Upon granting access, the process proceeds to Step 3. If denied, it transitions to Step 2.2.  • Step 3: The Prompt Analysis module refines and refactors the user’s prompt (if necessary) and identifies the key capabilities required to put together an appropriate response” Yellow Highlight [Page 9](zotero://open-pdf/library/items/2945QZPT?page=9&annotation=HKQUIW4S)



Step 4: The Llama-2 LLM processes the user request based on the identified capabilities. If a generic response is required, the LLM responds to the user directly (Step 4.1). If specialised features from KG are required, the process moves to Step 4.2.  • Step 5: Llama-2 generates or invokes relevant Cypher instruc- tions for Neo4j based on required capabilities.  • Step 6: A Cypher Validation Layer (CVL) ensures the integrity and safety of these instructions. Validated queries are executed on the Neo4j Knowledge Graph.  • Step 7: KG processes the queries, extracting the pertinent data.  An Error Handling (EH) mechanism inspects the extracted insights for anomalies.  • Step 8: Error-free insights are compiled to be returned back to the LLM.  • Step 9 and 10: LLM formats the insights for user-friendly presentation and provides a response to the user. The User (U) receives the curated data, ensuring only permitted infor- mation is accessed. Users have the option to offer feedback through a Feedback Loop (FB), which might guide the LLM’s subsequent interactions.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/2945QZPT?page=9&annotation=IE24T4M7)



![[image-10-x13-y622.png]]



Autonomous LLM Operations: The LLM, trained on vast datasets, can address certain user queries independently of external databases like the KG. This capability is evident in scenarios requiring comprehension, summarization, or responses that don’t necessitate explicit fact-checking against a structured knowledge source.  1. Text Summarization: For article summarization, the LLM utilizes its training to extract and condense key points without needing KG interaction.  2. Generic Journalism Queries: LLM can handle queries related to journalistic standards, writing styles, or general media ethics, drawing from its extensive training on journalism-related topics.  3. Contextual Interpretations: The LLM can interpret and respond to journalism-related queries based on previous context without extracting explicit facts, lever- aging its inherent understanding of relational data.” Yellow Highlight [Page 10](zotero://open-pdf/library/items/2945QZPT?page=10&annotation=VUWIKH4L)



![[image-11-x25-y17.png]]




---
Publish Year: "2023"
Authors: Yew Ken Chia, Guizhen Chen, Luu Anh Tuan, Soujanya Poria, Lidong Bing
URL: http://arxiv.org/abs/2311.09277
Zotero Link: zotero://select/library/items/HCDZ3XW8
tags:
  - "#Computer-Science---Computation-and-Language"
Published: 2024-06-04
---
# Summary
## Purpose
- The research was initiated to address the limitations of large language models (LLMs) in complex reasoning tasks, which is a significant issue in the field of Computer Science, specifically in Computation and Language. The purpose of the study was to enhance the reasoning capabilities of LLMs by introducing a method called contrastive chain-of-thought prompting, which utilizes both positive and negative examples to improve the reasoning process.

## Methods
- The researchers proposed the concept of contrastive chain-of-thought prompting, which involves providing LLMs with both positive and negative demonstrations to aid in reasoning.
- They utilized bridging objects, which are symbolic items that the model uses to reach the final solution, such as numbers and equations in arithmetic tasks or names of entities in factual tasks.
- Language templates were employed as textual hints to guide the language model in deriving and contextualizing the correct bridging objects during the reasoning process.

## Key Findings
- The study found that solely increasing the model size does not solve complex reasoning tasks effectively.
- It was observed that even demonstrations with invalid reasoning can lead to similar performance compared to valid demonstrations, highlighting the importance of the reasoning process itself.
- The introduction of contrastive chain-of-thought prompting led to significant improvements in performance, with a 9.8-point increase for GSM-8K and a 16.0-point increase for Bamboogle when using GPT-3.5-Turbo, a widely used LLM.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on the field of Computation and Language. It suggests that the contrastive chain-of-thought prompting can not only improve the accuracy of LLMs in complex reasoning tasks but also enhance the trustworthiness of the models by addressing potential errors in the reasoning process.

## Critiques
Upon evaluating the research, some critiques include:
    - The generalizability of the findings may be limited to the specific tasks and datasets used in the study.
    - There may be concerns about the scalability of the approach when applied to a broader range of tasks or more complex reasoning challenges.
    - The study may not have fully explored the implications of negative examples on the learning process and long-term model behavior.

## Tags
- #Computer-Science---Computation-and-Language
- #Chain-of-Thought-Prompting
- #Reasoning-Enhancement-Methods
- #Large-Language-Models
- #Contrastive-Learning

# Annotations
![[image-1-x296-y309.png]]



solely increasing the model size cannot solve complex reasoning tasks (Rae et al., 2022). To this end, chain-of-thought prompting was proposed to unlock the reasoning ability of LLMs by generating intermediate reasoning steps (Wei et al., 2022b)” Yellow Highlight [Page 1](zotero://open-pdf/library/items/AZWXWMVT?page=1&annotation=MS25ZX2X)



it was shown that even demonstrations with invalid reasoning can lead to similar performance compared to valid demonstrations (Wang et al., 2023)2.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/AZWXWMVT?page=1&annotation=T6K28ZRK)



Any potential error in the reasoning process not only affects the accuracy of the final result but also undermines the trustworthiness of the language model (Turpin et al., 2023)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AZWXWMVT?page=2&annotation=N3ZWW8IS)



To address the challenges of chain of thought, we are inspired by how humans can learn from positive as well as negative examples.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AZWXWMVT?page=2&annotation=G2F3IBJ9)



we propose contrastive chain of thought, which provides both positive and negative demonstrations to enhance the reasoning of language models.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AZWXWMVT?page=2&annotation=UWZTHP94)



Notably, compared to conventional chain of thought, we observe improvements of 9.8 and 16.0 points for GSM-8K (Cobbe et al., 2021) and Bamboogle (Press et al., 2023) respectively when using GPT-3.5-Turbo3, a widely used LLM” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AZWXWMVT?page=2&annotation=GEDU2G4R)



Bridging objects are the symbolic items that the model traverses in order to reach the final solution. For example, the objects could be numbers and equations in arithmetic tasks, or the names of entities in factual tasks.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AZWXWMVT?page=2&annotation=EV55GKBH)



Language templates are the textual hints that guide the language model to derive and contextualize the correct bridging objects during the reasoning process.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AZWXWMVT?page=2&annotation=U4RIICUW)



![[image-5-x55-y637.png]]




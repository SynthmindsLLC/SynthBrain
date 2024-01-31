---
Publish Year: "2023"
Authors: Yiyao Yu, Junjie Wang, Yuxiang Zhang, Lin Zhang, Yujiu Yang, Tetsuya Sakai
URL: http://arxiv.org/abs/2310.00970
Zotero Link: zotero://select/library/items/GXSL8AHX
tags:
  - "#AIEthics"
  - "#alignment"
  - "#Computer-Science---Computation-and-Language"
  - "#justice"
Published: 2024-04-23
---
# Summary
## Purpose 
This paper introduces a novel workflow for integrating ethical alignment into Conversational Information Retrieval (CIR) systems, addressing the need for AI technologies to adhere to human norms and avoid disseminating harmful or misleading information.

## Methods 
- Introduction of the Ethical Alignment Process (EAP) for CIR systems.
- Development of QA-ETHICS, adapted from the ETHICS dataset, for ethical judgment evaluation.
- Creation of MP-ETHICS for evaluating scenarios under multiple ethical concepts.
- Proposal of the Ethical Alignment Language Model (EALM) using descriptions of values and a moral reasoning module.
- Utilization of cross-attention layers in the ethical reasoning module.

## Key Findings 
1. EALM achieves state-of-the-art performance on three ethics benchmarks.
2. The integration of EAP in CIR enhances explainability and transparency in AI systems.
3. QA-ETHICS and MP-ETHICS datasets enable comprehensive evaluation of AI models' ethical alignment.
4. EALM effectively handles binary and multi-label ethical judgment tasks.
5. The methodology is adaptable across different model sizes and architectures.

## Discussion 
This research is pivotal in promoting ethical alignment in AI, particularly in CIR systems. The approach balances technical advancement with moral considerations, fostering AI development that is more in tune with human ethical standards.

## Critiques 
1. Potential limitations in the scalability of the EALM framework.
2. The challenge of ensuring unbiased ethical standards across diverse cultural and societal backgrounds.
3. The need for continuous updates to the ethical datasets to reflect evolving societal norms.

## Tags
#EthicalAlignment #AI #CIR #EALM #EthicsInAI #QAETHICS #MPETHICS.


# Annotations
we observe that recent CIR systems [13, 14, 21] lack the integration of moral considerations or corresponding designs.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/SC8PNJGS?page=1&annotation=74EUC33G)



Despite efforts to reduce bias and enhance fairness [11, 17, 24], these ethical elements are often embedded during model training in mainstream CIR systems.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/SC8PNJGS?page=1&annotation=7MI4SUBI)



we design our CIR system by integrating the Ethical Alignment Process (EAP) into the existing CIR workflow” Yellow Highlight [Page 1](zotero://open-pdf/library/items/SC8PNJGS?page=1&annotation=HXFLZTQ3)



this alignment occurs before the retrieved/generated data reaches real users, thereby preventing potentially irreversible impacts by filtering harmful results through the evaluation of the dataset or model-generated content.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/SC8PNJGS?page=1&annotation=JBLVJCTR)



![[image-2-x48-y481.png]]



![[image-2-x47-y257.png]]



We first introduce QA-ETHICS, a dataset derived from the ETHICS dataset [8] with five ethical concepts (Commonsense morality; Deontology; Justice; Utilitarianism; Virtue), but with a unified perspective.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=KTI6R4TX)



This approach results in training a model solely focused on the concept of justice.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=AA3EGW7L)



we employ a simple rule to merge the subsets by considering everyday human communication - Question & Answering, resulting in QA-ETHICS. Taking the aforementioned example, we add a question, “Does the sentence align with justice principles?”. The model decides if it is acceptable.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=WBKXAXLI)



A similar approach is used for “Commonsense morality”, replacing “justice” in the question. This way, the model is trained and evaluated on all ethical concepts in a binary classification task.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=XRPJEY57)



propose a new dataset, MP-ETHICS. In detail, we ask annotators to assess the degree of alignment with the five aforementioned moral principles in the given scenario, constituting a multi-label problem.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=TV5ZJ8VR)



the proposed dataset aids an AI system in grasping human-oriented concepts, enabling diverse ethical considerations of an input text.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=3X5UCW7A)



train a language model for ethical judgments” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=3U29Q4BZ)



propose a unified Ethical Alignment Language Model (EALM)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=4MYCUUUL)



Our EALM has achieved state-of-the-art (SoTA) performance on three ethics benchmarks.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=DK3ZFKQX)



datasets often concentrate solely on a specific ethical issue, such as gender bias, thereby ignoring other ethical concerns. In light of this focus bias, a key challenge emerges in ensuring the diversity of these datasets so that they cover a broad spectrum of ethical issues.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=ZM95C8MA)



collect and annotate a multitude of social media posts to create a dataset that covers various ethical issues.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/SC8PNJGS?page=2&annotation=YLFY4QMU)



![[image-3-x51-y484.png]]



ETHICS benchmark considers several basic shared human ethical concepts to evaluate language models, including justice, virtue ethics, deontology, utilitarianism and commonsense morality. It is rooted in natural language scenarios. This feature enables us to simulate a wide array of situations, encompassing interpersonal relationships, commonplace occurrences, and many objects.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/SC8PNJGS?page=3&annotation=NIH4ZM7V)



Our philosophy is to build a unified, comprehensive ethical dataset. Driven by recent progress in transforming a variety of NLP tasks into a unified machine reading comprehension (MRC) format” Yellow Highlight [Page 3](zotero://open-pdf/library/items/SC8PNJGS?page=3&annotation=ENM9ZBW3)



we remodel the dataset into a QA pair structure, named QA-ETHICS.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/SC8PNJGS?page=3&annotation=W77KS4I5)



1) Design a unified question for each ethical concept; 2) The definition of the label uniformly translates to “Is it compliant with the given ethical concept?”” Yellow Highlight [Page 3](zotero://open-pdf/library/items/SC8PNJGS?page=3&annotation=7DK5BL9P)



QA-ETHICS allows the full range of moral concepts to be introduced during training and the full range of moral competencies to be assessed simultaneously during testing.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/SC8PNJGS?page=3&annotation=9N3MGRQ5)



![[image-4-x71-y402.png]]



EALM framework achieves the best performance on average scores. In particular, the EALM earns 11.1% improvement gains on the hard test set, measured by the average score.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/SC8PNJGS?page=5&annotation=RR2D59ST)



![[image-5-x314-y360.png]]



QA format minimizes misunderstanding, making it more suitable not only for human understanding but also for helping language models grasp the concepts conveyed in language.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/SC8PNJGS?page=5&annotation=H7DSC5GL)



“+ descriptions” indicates the insertion of ethical concept descriptions into the input.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/SC8PNJGS?page=5&annotation=BMN2TDAM)



Our results show that simply adding descriptions does not improve the model’s understanding of the scene.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/SC8PNJGS?page=6&annotation=9SDC5PYN)



In fact, the complexity of ethical descriptions, perceived as noise by the model, can distract it and reduce performance.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/SC8PNJGS?page=6&annotation=K6CY7435)



when we apply the EALM framework, the language model’s performance significantly improves.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/SC8PNJGS?page=6&annotation=JYKYY7GB)



we should also design ethical alignment modules. These modules can provide the model with the ability to ethically reason about the input scenario and ethical descriptions.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/SC8PNJGS?page=6&annotation=FCKWUIWT)




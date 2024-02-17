---
Publish Year: "2023"
Authors: Aounon Kumar, Chirag Agarwal, Suraj Srinivas, Aaron Jiaxun Li, Soheil Feizi, Himabindu Lakkaraju
URL: http://arxiv.org/abs/2309.02705
Zotero Link: zotero://select/library/items/D8V9E2UM
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#Computer-Science---Machine-Learning"
  - "#Computer-Science---Cryptography-and-Security"
  - "#aisafety"
  - "#promptinjection"
Published: 2024-03-12
---
# Summary

## Purpose 
The paper's primary goal is to introduce a framework for defending LLMs against adversarial attacks. These attacks involve adding malicious token sequences to prompts, tricking LLMs into producing harmful content despite safety measures.

## Methods 
- **Erase-and-Check Framework**: A novel approach where individual tokens in a prompt are erased, and subsequences are analyzed using a safety filter. 
- **Attack Modes Addressed**: Three types of adversarial attacks – suffix, insertion, and infusion.
- **Safety Filter Implementation**: Using pre-trained LLMs and a fine-tuned DistilBERT classifier to distinguish between safe and harmful prompts.

## Key Findings 
1. **Effectiveness of Erase-and-Check**: This method provides strong safety guarantees, successfully identifying harmful prompts with high accuracy.
2. **Improvement with DistilBERT**: Replacing Llama 2 with DistilBERT enhances accuracy and speed, recognizing harmful prompts more efficiently.
3. **Superiority Over Other Methods**: Outperforms traditional methods like randomized smoothing, especially in complex attack scenarios.
4. **High Performance on Safe Prompts**: Maintains good performance in classifying non-adversarial safe prompts.

## Discussion 
This research is crucial for the field of AI safety, addressing the vulnerability of LLMs to adversarial attacks. The erase-and-check approach offers a robust defense mechanism, improving the reliability of LLMs in real-world applications.

## Critiques 
1. **Computational Cost**: The complexity of the method, especially in more advanced attack modes, requires significant computational resources.
2. **Limitation in Scope**: The study primarily focuses on defense against specific types of adversarial attacks, potentially overlooking other emerging threats.

## Tags
#LLMSafety #AI #AdversarialAttacks #EraseAndCheck #DistilBERT #ComputationalCost

# Annotations
several fine-tuning tech- niques have been developed to incorporate human feedback to ensure that LLM outputs are safe and aligned with human values (Ouyang et al., 2022; Bai et al., 2022; Glaese et al., 2022; Korbak et al., 2023; Xu et al., 2020). These approaches use human oversight to steer an LLM to generate safe outputs. When prompted with a harmful user request, an aligned model is expected to decline the request rather than comply with it” Yellow Highlight [Page 3](zotero://open-pdf/library/items/WKJZ6LVA?page=3&annotation=5EAAVIEK)



Wei et al.  (2023) show that simply asking an LLM to begin its response with “Absolutely! Here’s” could mislead the model into complying with the user’s harmful request. Several other examples of adver- sarial augmentation of harmful prompts, such as the Do Anything Now (DAN) jailbreak, are also well known” Yellow Highlight [Page 3](zotero://open-pdf/library/items/WKJZ6LVA?page=3&annotation=CK7NYYV4)



work of Zou et al. (2023) shows that it is possible to automate the generation of adversarial sequences, creating an endless supply of such attacks, using their Greedy Coordinate Gradient (GCG) attacks” Yellow Highlight [Page 3](zotero://open-pdf/library/items/WKJZ6LVA?page=3&annotation=ZEY4V3PQ)



Jain et al. (2023) and Alon & Kamfonas (2023) study approaches like perplexity filtering, para- phrasing, and adversarial training to defend against adversarial prompts. Each approach targets a specific weakness of adversarial sequences to detect and defend against them.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/WKJZ6LVA?page=3&annotation=6VHKU2EX)



perplexity filtering takes advantage of the gibberish nature of an adversarial sequence to distinguish it from the rest of the prompt” Yellow Highlight [Page 3](zotero://open-pdf/library/items/WKJZ6LVA?page=3&annotation=QUMKCRRX)



AutoDAN attacks developed by Liu et al. (2023) and Zhu et al. (2023) can circumvent perplexity filters by generating adversarial sequences that look similar to natural text. This phenomenon of newer attacks bypassing existing defenses has also been well documented in computer vision (Athalye et al., 2018; Tramer et al. ` , 2020; Yu et al., 2021; Carlini & Wagner, 2017).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/WKJZ6LVA?page=3&annotation=PPSMSLA4)



erase-and-check, to defend against adversarial prompts with verifiable safety guarantees. Given a clean or adversarial prompt P, this procedure erases tokens individually (up to a maximum of d tokens) and checks if the erased subsequences, as well as the input prompt P, are safe, using a safety filter is-harmful” Yellow Highlight [Page 3](zotero://open-pdf/library/items/WKJZ6LVA?page=3&annotation=A8MCEAW6)



We first implement the filter by prompting a pre-trained language model, Llama 2 (Touvron et al., 2023), to classify text sequences as safe or harmful.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/WKJZ6LVA?page=4&annotation=LQPHVDHV)



Using a trained DistilBERT classifier as the filter, the above values can be improved to 100% and 98%, respectively” Yellow Highlight [Page 4](zotero://open-pdf/library/items/WKJZ6LVA?page=4&annotation=EJNN4KWT)



RandEC is a ran- domized version of erase-and-check that evaluates the safety filter on a small, randomly sam- pled subset of the erased subsequences” Yellow Highlight [Page 4](zotero://open-pdf/library/items/WKJZ6LVA?page=4&annotation=LI52J53Z)



GradEC uses the gradients of the safety filter is-harmful with respect to the input prompt to optimize the tokens to erase.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/WKJZ6LVA?page=4&annotation=BPU387IJ)



RandEC achieves an empirical detection accuracy of over 90% on adversarial harmful prompts by randomly checking only 20% of the erased subsequences (Section 8.1). Similarly, with only six iterations of the optimizer, GradEC detects more than 90% of the adversarial prompts” Yellow Highlight [Page 4](zotero://open-pdf/library/items/WKJZ6LVA?page=4&annotation=B8UIBGLJ)



![[image-4-x359-y162.png]]



Adversarial Suffix: This is the simplest attack mode (Sec- tion 4). In this mode, adversarial prompts are of the type P + α, where an adversarial sequence α is appended to the end of the original prompt P” Yellow Highlight [Page 4](zotero://open-pdf/library/items/WKJZ6LVA?page=4&annotation=RLGSJXMX)



For this mode, the erase-and-check pro- cedure erases d tokens from the end of the input prompt one by one and checks the resulting subsequences using the filter is-harmful.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/WKJZ6LVA?page=4&annotation=D2ZDYLQJ)



![[image-5-x91-y555.png]]



Adversarial Insertion: This mode subsumes the suffix mode (Section 5). Here, adversarial sequences can be inserted anywhere in the middle (or the end) of the prompt P.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/WKJZ6LVA?page=5&annotation=2MG6DXA2)



For adversarial prompts of this form, erase-and-check erases up to d tokens starting from a location i of the prompt for all locations i from 1 to |P1 +α+P2|. More precisely, it generates subsequences by erasing tokens in the range [i, . . . , i+j], for all i ∈ {1, . . . , |P1+α+P2|} and for all j ∈ {1, . . . , d}.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/WKJZ6LVA?page=5&annotation=72GN38J9)



Adversarial Infusion: This is the most general attack mode (Section 6). In this mode, adversar- ial tokens τ1, τ2, . . . , τm are inserted at arbitrary locations in the prompt P” Yellow Highlight [Page 5](zotero://open-pdf/library/items/WKJZ6LVA?page=5&annotation=ZVDCDNQA)



We use the Llama 2 system prompt to set its objective of classifying a user prompt as harmful or not harmful. Examples of safe or harmful prompts are not needed for building this filter” Yellow Highlight [Page 5](zotero://open-pdf/library/items/WKJZ6LVA?page=5&annotation=U7BMCSC3)



![[image-6-x121-y655.png]]



We download a pre-trained DistilBERT model from Hugging Face1 and fine-tune it on our safety dataset.  The dataset contains examples of harmful prompts from the AdvBench dataset created by Zou et al.  (2023) and safe prompts generated by us” Yellow Highlight [Page 6](zotero://open-pdf/library/items/WKJZ6LVA?page=6&annotation=LST2TRXT)



The computational cost of erase-and-check increases for more general attack modes, limiting the length of adversarial sequences that can be defended against in a reasonable amount of time, especially with Llama 2 due to its high inference cost. The running time of our procedure can be significantly improved by replacing Llama 2 with DistilBERT” Yellow Highlight [Page 6](zotero://open-pdf/library/items/WKJZ6LVA?page=6&annotation=TB2R7QSQ)



the accuracy of the erase-and-check procedure de- creases for larger adversarial sequences, especially with Llama 2. This is likely because defending against longer adversarial sequences requires our procedure to check more subsequences for each input prompt.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/WKJZ6LVA?page=6&annotation=K9N4PQRB)




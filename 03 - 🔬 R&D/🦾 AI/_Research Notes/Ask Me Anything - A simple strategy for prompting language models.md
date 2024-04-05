---
Publish Year: "2022"
Authors: Simran Arora, Avanika Narayan, Mayee F. Chen, Laurel Orr, Neel Guha, Kush Bhatia, Ines Chami, Frederic Sala, Christopher Ré
URL: http://arxiv.org/abs/2210.02441
Zotero Link: zotero://select/library/items/D2M7AS34
tags:
  - "#Computer-Science---Computation-and-Language"
Published: 2024-03-05
---
# Summary
## Purpose 
Arora et al. explore a new prompting strategy, ASK ME ANYTHING PROMPTING (AMA), to enhance the performance of Large Language Models (LLMs). This method addresses the issue of prompt brittleness – where minor changes in prompts can lead to significant performance variations in LLMs. AMA aims to simplify the process of prompt design and improve the task-transfer abilities of LLMs without additional trainin&#8203;``【oaicite:5】``&#8203;&#8203;``【oaicite:4】``&#8203;】.

## Methods 
- Identifying effective prompt formats, particularly question-answering (QA) prompts that facilitate open-ended responses.
- Utilizing LLMs to transform task inputs into effective QA formats.
- Collecting multiple, imperfect prompts to aggregate various 'noisy' predictions for an input's true label.
- Implementing weak supervision as a strategy to combine these predictions into a final output.
- Evaluating AMA across multiple open-source model families and sizes (125M-175B parameters) on 20 popular language benchmark&#8203;``【oaicite:3】``&#8203;&#8203;``【oaicite:2】``&#8203;】.

## Key Findings 
1. AMA outperforms traditional few-shot prompting methods, demonstrating an average performance lift of 10.2% over these baselines.
2. AMA enables the open-source GPT-J-6B model to match and exceed the performance of few-shot GPT3-175B on 15 of 20 benchmarks.
3. The method is effective across diverse tasks and LLM families, offering an average improvement of 41% over the 6B parameter model’s few-shot performance.
4. AMA is particularly beneficial for applications involving private data or large data operations, where using large-scale, closed-source models is challengin&#8203;``【oaicite:1】``&#8203;】.

## Discussion 
AMA's approach to using multiple imperfect prompts and weak supervision is a significant advancement in the field of LLMs. It addresses the brittleness of prompts and provides a scalable and effective method for task transfer without the need for extensive model retraining. The strategy's ability to work across various models and tasks demonstrates its versatility and potential for wide application, especially in contexts where large models are impractica&#8203;``【oaicite:0】``&#8203;】.

## Critiques 
1. The reliance on weak supervision could introduce complexity in understanding and diagnosing the model's decision-making process.
2. While AMA shows improvement across various models, the extent of its effectiveness in highly specialized or niche tasks remains to be fully explored.
3. The paper primarily focuses on open-source models, and further research is needed to understand AMA's applicability to proprietary or custom-built LLMs.

## Tags
#LLMs #PromptEngineering #WeakSupervision #TaskTransfer #ModelPerformance #OpenSourceModels #AIResearch.


# Annotations
Recent work has evaluated LLM prompting performance on a broad set of tasks and finds the process to be brittle — small changes to the prompt result in large performance variations” Yellow Highlight [Page 1](zotero://open-pdf/library/items/AALKUB46?page=1&annotation=FJBC459I)



The performance further varies depending on the chosen LLM family” Yellow Highlight [Page 1](zotero://open-pdf/library/items/AALKUB46?page=1&annotation=IAK4SD9Y)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/aroraAskMeAnything2022/image-2-x59-y553.png]]



This work instead considers aggregating the predictions of multiple effective, yet imperfect, prompts to improve prompting performance over a broad set of models and tasks. Given a task input, each prompt produces a vote for the input’s true label, and these votes are aggregated to produce a final prediction.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AALKUB46?page=2&annotation=BXXAN23I)



ASK ME ANYTHING PROMPTING (AMA), a simple approach that surprisingly enables open-source LLMs with 30x fewer parameters to exceed the few-shot performance of GPT3-175B” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AALKUB46?page=2&annotation=3MFUHZXB)



and find prompts that encourage open-ended answers (“Where did John go?”) to be more effective than prompts that restrict the model output to particular tokens (e.g. “John went to the park. Output True or False?”).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AALKUB46?page=2&annotation=6F2JDRIQ)



We first use question()-prompts, which contain task-agnostic examples of how to trans- form statements to various (e.g., yes-no, cloze) questions and second use answer()-prompts that demonstrate ways of answering questions (e.g., concise or lengthy answers).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/AALKUB46?page=2&annotation=PTFKCK46)



We find that the errors pro- duced by the predictions of different chains can be highly varying and correlated. While majority vote (MV) may do well on certain sets of prompts, it performs poorly in the above cases. AMA accounts for these cases by iden- tifying dependencies among prompts and using WS, a procedure for modeling and combining noisy predictions without any labeled data [Ratner et al., 2017, Varma et al., 2019].” Yellow Highlight [Page 3](zotero://open-pdf/library/items/AALKUB46?page=3&annotation=CBPR94C7)



Self-Consistency Wang et al.  [2022b], which requires no training, does not report improvements for small LMs (<10B parameters)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/AALKUB46?page=3&annotation=92MIPY7M)



WS is a powerful framework that learns the accuracies and correlations of multiple noisy sources and aggregates them to produce weak labels for training data” Yellow Highlight [Page 3](zotero://open-pdf/library/items/AALKUB46?page=3&annotation=XKS3R2ZL)



ASK ME ANYTHING PROMPTING (AMA), a prompting approach that uses multiple imperfect prompts— rather than one painstakingly crafted perfect prompt—and reliably aggregates their outputs. We” Yellow Highlight [Page 4](zotero://open-pdf/library/items/AALKUB46?page=4&annotation=KRI2GQAP)



We ground our analysis in three standard categories of prompts used in prior work including Brown et al. [2020], Sanh et al. [2022, inter alia.]: (1) questions that restrict the model output particular tokens (“John invited Mark to come watch Jurassic Park. Output True or False?”); (2) cloze-questions which ask the model to fill in the remaining text (“John invited Mark to come watch Jurassic _” and using the LLM to fill-the-blank, “Park”); and (3) traditional (yes-no, Wh) free-form questions (“Where did John invite Mark?”)” Yellow Highlight [Page 4](zotero://open-pdf/library/items/AALKUB46?page=4&annotation=9WX2NEPU)



Open-ended prompts appear to outperform restrictive-prompts.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/AALKUB46?page=4&annotation=7CBKZ9RU)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/aroraAskMeAnything2022/image-5-x65-y599.png]]



The use of open-ended questions over restrictive-prompts can increase the difficulty of mapping open-ended answers to valid output classes.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/AALKUB46?page=5&annotation=Z9GV26AX)



The EleutherAI models are trained on The Pile corpus Black et al.  [2021], Wang and Komatsuzaki [2021], Gao et al. [2021]. Over a 2% random sample of the ∼200B token Pile data, we find that open-ended QA structures (i.e., which ask the model “Is . . . ?”, “Who . . . ?”) appear on the order of 1000× more frequently than the restrictive-prompt structures (i.e., which instruct the model to output “True or False”, “Yes or No”).” Yellow Highlight [Page 5](zotero://open-pdf/library/items/AALKUB46?page=5&annotation=CAEDHBC2)



We find in Pile that there are large imbalances between the frequencies of “yes” vs. “no”, and “True” vs.  “False” for instance, which may instil the biases and contribute to the low quality from restrictive-prompts.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/AALKUB46?page=5&annotation=R6XJGXZC)



Motivated by our observations about the effectiveness of QA prompt structures, we proceed in AMA with a two-step prompting pipeline: (1) generating questions based on the input and (2) prompting the LLM to answer the generated questions. These prompts are effective, and to further improve performance we next turn to generating and aggregating over multiple prompt-outputs for each input” Yellow Highlight [Page 5](zotero://open-pdf/library/items/AALKUB46?page=5&annotation=SX3ADZC8)




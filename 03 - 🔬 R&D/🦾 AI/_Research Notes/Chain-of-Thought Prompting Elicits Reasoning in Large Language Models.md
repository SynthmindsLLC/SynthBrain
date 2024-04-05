---
Publish Year: "2023"
Authors: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
URL: http://arxiv.org/abs/2201.11903
Zotero Link: zotero://select/library/items/8NPFSS4X
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - chainofthought
Published:
---
# Summary
## Purpose

## Methods

## Key Findings

## Discussion

## Critiques

# Annotations
![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/weiChainofThoughtPromptingElicits2023/image-1-x101-y146.png]]



Scaling up the size of language models has been shown to confer a range of benefits, such as improved performance and sample efficiency (Kaplan et al., 2020; Brown et al., 2020, inter alia)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/3U4TNKMY?page=2&annotation=LC8S4WQD)



reasoning ability of large language models can be unlocked by a simple method motivated by two ideas. First, techniques for arithmetic reasoning can benefit from generating natural language rationales that lead to the final answer.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/3U4TNKMY?page=2&annotation=C9YJY3K2)



neuro-symbolic methods that use formal languages instead of natural language” Yellow Highlight [Page 2](zotero://open-pdf/library/items/3U4TNKMY?page=2&annotation=2QK8HF5B)



Second, large language models offer the exciting prospect of in-context few-shot learning via prompting. That is, instead of finetuning a separate language model checkpoint for each new task, one can simply “prompt” the model with a few input–output exemplars demonstrating the task. Remarkably, this has been successful for a range of simple question-answering tasks (Brown et al., 2020).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/3U4TNKMY?page=2&annotation=Y54GUSQ6)



we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: 〈input, chain of thought, output〉. A chain of thought is a series of intermediate natural language reasoning steps that lead to the final output, and we refer to this approach as chain-of-thought prompting.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/3U4TNKMY?page=2&annotation=FKDBQRFS)



Consider one’s own thought process when solving a complicated reasoning task such as a multi-step math word problem. It is typical to decompose the problem into intermediate steps and solve each before giving the final answer” Yellow Highlight [Page 2](zotero://open-pdf/library/items/3U4TNKMY?page=2&annotation=EC2K86EA)



Chain-of-thought prompting has several attractive properties as an approach for facilitating reasoning in language models. 1. First, chain of thought, in principle, allows models to decompose multi-step problems into intermediate steps, which means that additional computation can be allocated to problems that require more reasoning steps. 2. Second, a chain of thought provides an interpretable window into the behavior of the model, suggesting how it might have arrived at a particular answer and providing opportunities to debug where the reasoning path went wrong (although fully characterizing a model’s computations that support an answer remains an open question). 3. Third, chain-of-thought reasoning can be used for tasks such as math word problems, commonsense reasoning, and symbolic manipulation, and is potentially applicable (at least in principle) to any task that humans can solve via language. 4. Finally, chain-of-thought reasoning can be readily elicited in sufficiently large off-the-shelf language models simply by including examples of chain of thought sequences into the exemplars of few-shot prompting.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/3U4TNKMY?page=3&annotation=SSPGX9WN)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/weiChainofThoughtPromptingElicits2023/image-4-x97-y368.png]]



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/weiChainofThoughtPromptingElicits2023/image-5-x307-y399.png]]



chain-of-thought prompting has larger performance gains for more-complicated problems. For instance, for GSM8K (the dataset with the lowest baseline performance), performance more than doubled for the largest GPT and PaLM models.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/3U4TNKMY?page=5&annotation=JETYX6X5)



Of 50 random examples where the model returned the correct final answer, all of the generated chains of thought were also logically and mathematically correct except two that coincidentally arrived at the correct answer” Yellow Highlight [Page 5](zotero://open-pdf/library/items/3U4TNKMY?page=5&annotation=VRSB7MPP)



also randomly examined 50 random samples for which the model gave the wrong answer. The summary of this analysis is that 46% of the chains of thought were almost correct, barring minor mistakes (calculator error, symbol mapping error, or one reasoning step missing), and that the other 54% of the chains of thought had major errors in semantic understanding or coherence” Yellow Highlight [Page 5](zotero://open-pdf/library/items/3U4TNKMY?page=5&annotation=DNUDBV2E)



scaling PaLM to 540B fixes a large portion of one-step missing and semantic understanding errors in the 62B model” Yellow Highlight [Page 5](zotero://open-pdf/library/items/3U4TNKMY?page=5&annotation=AV6Q6BS7)



One reason for why chain-of-thought prompting might help is that it produces the mathematical equation to be evaluated, and so we test a variation where the model is prompted to output only a mathematical equation before giving the answer.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/3U4TNKMY?page=5&annotation=9G3BFY9T)



semantics of the questions in GSM8K are too challenging to directly translate into an equation without the natural language reasoning steps in chain of thought.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/3U4TNKMY?page=5&annotation=I9SQCVY9)



For datasets of one-step or two-step problems, however, we find that equation only prompting does improve performance, since the equation can be easily derived from the question” Yellow Highlight [Page 5](zotero://open-pdf/library/items/3U4TNKMY?page=5&annotation=GVB26CB2)



Another intuition is that chain of thought allows the model to spend more computation (i.e., intermediate tokens) on harder problems. To isolate the effect of variable computation from chain-of-thought reasoning, we test a configuration where the model is prompted to output a only sequence of dots (. . .) equal to the number of characters in the equation needed to solve the problem. This variant performs about the same as the baseline, which suggests that variable computation by itself is not the reason for the success of chainof-thought prompting, and that there appears to be utility from expressing intermediate steps via natural language” Yellow Highlight [Page 6](zotero://open-pdf/library/items/3U4TNKMY?page=6&annotation=W2CWP7WA)



Another potential benefit of chain-of-thought prompting could simply be that such prompts allow the model to better access relevant knowledge acquired during pretraining. Therefore, we test an alternative configuration where the chain of thought prompt is only given after the answer, isolating whether the model actually depends on the produced chain of thought to give the final answer. This variant performs about the same as the baseline, which suggests that the sequential reasoning embodied in the chain of thought is useful for reasons beyond just activating knowledge.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/3U4TNKMY?page=6&annotation=FDNP8XAN)



Although chain of thought is particularly suitable for math word problems, the language-based nature of chain of thought actually makes it applicable to a broad class of commonsense reasoning problems, which involve reasoning about physical and human interactions under the presumption of general background knowledge.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/3U4TNKMY?page=7&annotation=ALURDU6Y)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/weiChainofThoughtPromptingElicits2023/image-7-x94-y95.png]]



chain-ofthought prompting not only enables language models to perform symbolic reasoning tasks that are challenging in the standard prompting setting, but also facilitates length generalization to inference-time inputs longer than those seen in the few-shot exemplars.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/3U4TNKMY?page=8&annotation=2CREKLGD)



This task asks the model to concatenate the last letters of words in a name (e.g., “Amy Brown” → “yn”). It is a more challenging version of first letter concatenation, which language models can already perform without chain of thought.3 We generate full names by randomly concatenating names from the top one-thousand first and last names from name census data” Yellow Highlight [Page 8](zotero://open-pdf/library/items/3U4TNKMY?page=8&annotation=KXSBMYFV)



This task asks the model to answer whether a coin is still heads up after people either flip or don’t flip the coin (e.g., “A coin is heads up. Phoebe flips the coin. Osvaldo does not flip the coin. Is the coin still heads up?” → “no”).” Yellow Highlight [Page 8](zotero://open-pdf/library/items/3U4TNKMY?page=8&annotation=VDN6XIH4)



With PaLM 540B, chain-of-thought prompting leads to almost 100% solve rates (note that standard prompting already solves coin flip with PaLM 540, though not for LaMDA 137B). Note that these in-domain evaluations are “toy tasks” in the sense that perfect solution structures are already provided by the chains of thought in the few-shot exemplars; all the model has to do is repeat the same steps with the new symbols in the test-time example. And yet, small models still fail—the ability to perform abstract manipulations on unseen symbols for these three tasks only arises at the scale of 100B model parameters.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/3U4TNKMY?page=8&annotation=QJSMAAS9)



With chain-of-thought prompting, language models achieve upward scaling curves (though performance is lower than in the in-domain setting). Hence, chain-of-thought prompting facilitates length generalization beyond seen chains of thought for language models of sufficient scale.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/3U4TNKMY?page=8&annotation=65B3UQKJ)



Chain-of-thought prompting appears to expand the set of tasks that large language models can perform successfully—in other words, our work underscores that standard prompting only provides a lower bound on the capabilities of large language models.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/3U4TNKMY?page=9&annotation=KU8S8P4E)




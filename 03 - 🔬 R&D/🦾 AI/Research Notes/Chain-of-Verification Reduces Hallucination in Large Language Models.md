---
Publish Year: "2023"
Authors: Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu, Roberta Raileanu, Xian Li, Asli Celikyilmaz, Jason Weston
URL: http://arxiv.org/abs/2309.11495
Zotero Link: zotero://select/library/items/95KSXF3D
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
t has been shown that as the number of model parameters is increased, performance at tasks such as closed book QA improve in accuracy, and larger models can generate more correct factual statements (Radford et al., 2019; Petroni et al., 2019).” Yellow Highlight [Page 1](zotero://open-pdf/library/items/Y42MDXD6?page=1&annotation=P96B33EN)



even the largest models can still fail, particularly on lesser known torso and tail distribution facts (Sun et al., 2023a), i.e. those that occur relatively rarely in the training corpora.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/Y42MDXD6?page=1&annotation=QIV87C7I)



These factually incorrect generations are referred to as hallucinations (Maynez et al., 2020)” Yellow Highlight [Page 1](zotero://open-pdf/library/items/Y42MDXD6?page=1&annotation=VD4TVNVZ)



the hallucination problem can be exacerbated due to the issue of exposure bias (Wang & Sennrich, 2020).” Yellow Highlight [Page 1](zotero://open-pdf/library/items/Y42MDXD6?page=1&annotation=FCF7FXCK)



The current wave of language modeling research goes beyond next word prediction, and has focused on their ability to reason.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/Y42MDXD6?page=1&annotation=5IF2LRYU)



Improved performance in reasoning tasks can be gained by encouraging language models to first generate internal thoughts or reasoning chains before responding (Wei et al., 2022; Adolphs et al., 2021; Wang et al., 2022; Lanchantin et al., 2023), as well as updating their initial response through self-critique (Press et al., 2022; Madaan et al., 2023).” Yellow Highlight [Page 1](zotero://open-pdf/library/items/Y42MDXD6?page=1&annotation=KBKRFSWM)



We develop an approach, called Chain-of-Verification (CoVe) which, given an initial draft response, first plans verification questions to check its work, and then systematically answers those questions in order to finally produce an improved revised response.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/Y42MDXD6?page=1&annotation=J237JC7A)



We find that independent verification questions tend to provide more accurate facts than those in the original longform answer, and hence improve the correctness of the overall response.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/Y42MDXD6?page=1&annotation=UVID4SKF)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/dhuliawalaChainofVerificationReducesHallucination2023/image-2-x98-y289.png]]



For a survey of the hallucination issue, see Ji et al. (2023)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/Y42MDXD6?page=2&annotation=KVBIF8IN)



A majority of the methods for reducing hallucination can be divided into roughly three categories: training-time correction, generation-time correction and via augmentation (tool-use).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/Y42MDXD6?page=2&annotation=V2BD6DMX)



In training-time correction methods, an attempt is made to improve the raw left-to-right generations of an encoder-decoder or decoder-only language model by either training or otherwise adjusting the model weights to decrease the probability of hallucinated generations.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/Y42MDXD6?page=2&annotation=54FPZLXP)



In generation-time correction, a common theme is to make reasoning decisions “on top of” the base LLM in order to make them more reliable.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/Y42MDXD6?page=2&annotation=IH3EPLGW)



Cohen et al. (2023) introduce a method called LM vs LM which simulates an interactive setup between two LLMs where one LLM acts as an examiner and tests if the output is consistent via repeated cross-examination.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/Y42MDXD6?page=3&annotation=IQFTSP5P)



A third approach is to use external tools to help mitigate hallucinations, rather than relying solely on the abilities of the language model itself.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/Y42MDXD6?page=3&annotation=NDA958W6)



For example, retrieval-augmented generation can decrease hallucinations by using factual documents for grounding” Yellow Highlight [Page 3](zotero://open-pdf/library/items/Y42MDXD6?page=3&annotation=QQW2BHHQ)



Other approaches include using tools for fact-checking (Chern et al., 2023a; Galitsky, 2023; Peng et al., 2023), or linking to external documents with attribution” Yellow Highlight [Page 3](zotero://open-pdf/library/items/Y42MDXD6?page=3&annotation=7LLBJCMM)



Our approach assumes access to a base LLM that – despite potentially being prone to hallucination is capable of being prompted with general instructions in either a few-shot or zero-shot fashion. A key assumption of our method is that this language model, when suitably prompted, can both generate and execute a plan of how to verify itself in order to check its own work, and finally incorporate this analysis into an improved response.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/Y42MDXD6?page=3&annotation=YIMX6IKT)



Our overall process, which we call Chain-of-Verification (CoVe), thus performs four core steps: 1. Generate Baseline Response: Given a query, generate the response using the LLM. 2. Plan Verifications: Given both query and baseline response, generate a list of verification questions that could help to self-analyze if there are any mistakes in the original response. 3. Execute Verifications: Answer each verification question in turn, and hence check the answer against the original response to check for inconsistencies or mistakes. 4. Generate Final Verified Response: Given the discovered inconsistencies (if any), generate a revised response incorporating the verification results.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/Y42MDXD6?page=3&annotation=YSGJ4UXS)



While steps (1), (2) and (4) all can be invoked with a single prompt, we investigate variations of step (3) including joint, 2-step and factored versions. These variants either involve a single prompt, two prompts or else independent prompts per question, where more sophisticated decomposition can yield improved results.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/Y42MDXD6?page=3&annotation=EQV6WRVG)



PLAN VERIFICATIONS” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=4WGX6WQX)



the model is prompted to generate a series of verification questions that test the factual claims in the original baseline response.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=43FZNCIF)



We note that verification questions are not templated and the language model is free to phrase these in any form it wants, and they also do not have to closely match the phrasing of the original text.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=Q8S5H37Z)



Given the planned verification questions, the next step is to answer them in order to assess if any hallucinations exist.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=SPC5334I)



We investigate several variants of verification execution, called joint, 2-Step, factored and factor+revise.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=9IRM674V)



Joint In the joint method, the planning and execution (steps 2 and 3) are accomplished by using a single LLM prompt, whereby the few-shot demonstrations include both verification questions and their answers immediately after the questions. In this approach separate prompts are not needed.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=MA6E9NY3)



2-Step A potential disadvantage of the joint method is that because the verification questions must condition on the baseline response in the LLM context, and the method is joint, the verification answers have to condition on the initial response as well. This may increase the likelihood of repetition, another known issue of modern LLMs (Holtzman et al., 2019). This means the verification questions might hallucinate similarly to the original baseline response, which defeats the purpose.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=YCRL4R9H)



Factored Another, more sophisticated approach, is to answer all questions independently as separate prompts. Again, crucially, those prompts do not contain the original baseline response and are hence not prone to simply copying or repeating it. The factored approach has the further advantage of removing any potential interference not only from the baseline response, but also between answer contexts, and is somewhat related to the recent (concurrent) work of Radhakrishnan et al. (2023)” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=H8GEKBAL)



It can also potentially handle more verification questions by virtue of them not all having to fit with the same single context.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=NMJP5XMN)



While this is potentially more computationally expensive, requiring the execution of many more LLM prompts, they can be run in parallel, and hence be batched.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=PCCIFZAR)



Factor+Revise After answering the verification questions, the overall CoVe pipeline then has to either implicitly or explicitly cross-check whether those answers indicate an inconsistency with the original responses. In the factor+revise approach, we execute this as a deliberate step via an extra LLM prompt, which may make it easier for the final system to reason about this step explicitly.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/Y42MDXD6?page=4&annotation=VWA7IKJH)



Finally, the improved response that takes verification into account is generated. This is executed by a final few-shot prompt where the context takes into account all of the previous reasoning steps, the baseline response and verification question answer pairs, so that the corrections can take place.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/Y42MDXD6?page=5&annotation=2D7DCILL)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/dhuliawalaChainofVerificationReducesHallucination2023/image-6-x89-y545.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/dhuliawalaChainofVerificationReducesHallucination2023/image-7-x91-y598.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/dhuliawalaChainofVerificationReducesHallucination2023/image-7-x94-y402.png]]



CoVe improves precision on list-based answer tasks We find that CoVe provides large gains in precision on the list-based tasks, e.g. more than doubles the precision from the Llama 65B few-shot baseline for the Wikidata task (from 0.17 to 0.36). We find from the positive and negative breakdown that there is a large reduction in the number of hallucinated answers (negatives: 2.95 → 0.68) while only a relatively small reduction in the number of non-hallucinations (positives: 0.59 → 0.38).” Yellow Highlight [Page 7](zotero://open-pdf/library/items/Y42MDXD6?page=7&annotation=IWUQNI38)



CoVe improves performance on closed book QA We also find that CoVe brings improvements in general QA problems, as measured on MultiSpanQA. We observe a 23% improvement in F1 over the few-shot baseline (0.39 → 0.48), where the improvements come from gains in both precision and recall.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/Y42MDXD6?page=7&annotation=ECFU5UPH)



CoVe improves precision on longform generation These results also extend to longform generation, where we actually see larger gains than in the QA setting. FACTSCORE increases 28% (55.9 → 71.4) from the few-shot baseline, with again only a relatively small reduction in average number of facts provided (16.6 → 12.3). We also show the breakdown of improvements across facts in Figure 2, where one can see CoVe improves results for both rare and more frequent facts.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/Y42MDXD6?page=8&annotation=DEK32CDS)



Instruction-tuning and CoT do not reduce hallucinations We find that the few-shot baseline that employs a pre-trained Llama model outperforms Llama 2 Chat, an instruction tuned model, across all the tasks. The few-shot examples lead the model to give outputs in line with those expected for the task, whereas general instruction tuning produces more hallucinations or incorrect outputs. Standard chain-of-thought (CoT) prompting also fails to improve the results for these tasks. While CoT has proven to help for reasoning tasks, it seems less appropriate for the issue of hallucination we measure in this work.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/Y42MDXD6?page=8&annotation=87FQZF7X)



Further explicit reasoning helps remove hallucinations In the longform generation task we also explore more sophisticated reasoning steps in the CoVe “factor+revise” method, which explicitly cross-checks whether verification answers indicate an inconsistency. We see large gains in the FACTSCORE metric from this further explicit reasoning from 63.7 (factored) → 71.4 (factor+revise). This gives further indication that appropriate and explicit reasoning in LLMs can bring improvements in mitigating hallucinations.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/Y42MDXD6?page=8&annotation=CFDRLA6K)



Shortform verification questions are more accurately answered than longform queries In a longform response, LLMs are prone to generate a number of hallucinations. However, it can often be the case that the LLM itself would know these hallucinations are wrong if queried specifically for that individual fact, independent of the rest of the longform generation” Yellow Highlight [Page 9](zotero://open-pdf/library/items/Y42MDXD6?page=9&annotation=32UJ8R56)



LLM-based verification questions outperforms heuristics In our method, CoVe, the verification questions are generated by the LLM dependent on the task. We compare the quality of these questions to heuristically constructed ones in order to measure their quality, by replacing the LLM questions with templated yes/no questions of the form “Does X answer the question” for list-based questions with elements X in the answer. Results on the Wiki-Category task, given in Table 4, show a reduced precision with rule-based verification questions.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/Y42MDXD6?page=9&annotation=PZ267MSU)




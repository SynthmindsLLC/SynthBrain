---
Publish Year: "2023"
Authors: Lewis Tunstall, Edward Beeching, Nathan Lambert, Nazneen Rajani, Kashif Rasul, Younes Belkada, Shengyi Huang, Leandro von Werra, Clémentine Fourrier, Nathan Habib, Nathan Sarrazin, Omar Sanseviero, Alexander M. Rush, Thomas Wolf
URL: http://arxiv.org/abs/2310.16944
Zotero Link: zotero://select/library/items/MMH5CFPW
tags:
  - "#Computer-Science---Computation-and-Language"
  - "#Computer-Science---Machine-Learning"
Published: 2023-12-12
---
# Summary
## Purpose 
The paper aims to produce a smaller language model (LM) that aligns well with user intent, using a method called distilled direct preference optimization (dDPO). This method improves intent alignment significantly without requiring human annotation, setting a new benchmark for 7B parameter chat models.

## Methods 
- Distilled Supervised Fine-Tuning (dSFT) using AI-generated dialogues.
- AI Feedback (AIF) for collecting preferences on model outputs.
- Distilled Direct Preference Optimization (dDPO) for refining the model based on AI feedback.

## Key Findings 
1. ZEPHYR-7B outperforms other 7B models and is competitive with larger models in chat benchmarks.
2. Preference learning is crucial for achieving alignment with user intent.
3. The approach does not require human annotation or additional sampling during fine-tuning.

## Discussion 
The paper highlights the effectiveness of dDPO in aligning smaller LMs to user intent, potentially reshaping the approach to training efficient and aligned LMs. It demonstrates that smaller models can achieve performance comparable to larger, human-feedback-aligned models.

## Critiques 
1. GPT-4, used as an evaluator, may be biased towards models distilled from it.
2. The scalability of the method to larger models like LLAMA2-70B is untested.
3. Safety considerations, such as the production of harmful outputs, are not addressed in this study.

## Tags
#AIAlignment #LanguageModels #dDPO #ZEPHYR7B #ChatModelBenchmarks


# Annotations
![[Synthbrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/tunstallZephyrDirectDistillation2023/image-1-x112-y156.png]]



the output of a more capable teacher model is used as supervised data for the student model.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/RS52LKQL?page=2&annotation=S3EJD2FS)



Users have noted that these models are not “intent aligned”, i.e. they do not behave in a manner that aligns with human users’ preferences. This property often leads to outputs that do not provide correct responses to queries.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/RS52LKQL?page=2&annotation=H2USPAD3)



Intention alignment has been difficult to quantify, but recent work has led to the development of benchmarks like MT-Bench (Zheng et al., 2023) and AlpacaEval (Li et al., 2023) that specifically target this behavior.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/RS52LKQL?page=2&annotation=PBN9V3LA)



he main step is to utilize AI Feedback (AIF) from an ensemble of teacher models as preference data, and apply distilled direct preference optimization as the learning objective (Rafailov et al., 2023). We refer to this approach as dDPO” Yellow Highlight [Page 2](zotero://open-pdf/library/items/RS52LKQL?page=2&annotation=HQUL4AZ3)



To validate this approach, we construct ZEPHYR-7B, an aligned version of Mistral-7B (Jiang et al., 2023). We first use dSFT, based on the UltraChat (Ding et al., 2023) dataset. Next we use the AI feedback data collected in the UltraFeedback dataset (Cui et al., 2023). Finally, we apply dDPO based on this feedback data. Experiments show that this 7B parameter model can achieve performance comparable to 70B-parameter chat models aligned with human feedback.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/RS52LKQL?page=2&annotation=H2CTSN4L)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/tunstallZephyrDirectDistillation2023/image-3-x87-y419.png]]



Powerful LLMs such as GPT-4 and Claude are used as evaluators to judge model responses by scoring model outputs or ranking responses in a pairwise setting.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/RS52LKQL?page=3&annotation=L5SN5XK5)



AlpacaEval is an example of another such leaderboard that compares models in a pairwise setting but instead uses bigger LLMs such as GPT-4 and Claude in place of humans (Dubois et al., 2023)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/RS52LKQL?page=3&annotation=7EGH7BWL)



MTBench uses GPT-4 to score model responses on a scale of 1-10 for multi-turn instructions across task categories such as reasoning, roleplay, math, coding, writing, humanities, STEM and extraction (Zheng et al., 2023).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/RS52LKQL?page=3&annotation=JNFHFJD8)



The goal of this work is to align an open-source large-language model to the intent of the user.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/RS52LKQL?page=3&annotation=X5R5B6WH)



Distilled Supervised Fine-Tuning (dSFT) Starting with a raw LLM, we first need to train it to respond to user prompts. This step is traditionally done through supervised fine tuning (SFT) on a dataset of high-quality instructions and responses (Chung et al., 2022; Sanh et al., 2021). Given access to a teacher language models, we can instead have the model generate instructions and responses (Taori et al., 2023), and train the model directly on these. We refer to this as distilled SFT (dSFT).” Yellow Highlight [Page 4](zotero://open-pdf/library/items/RS52LKQL?page=4&annotation=8EEI8LNW)



A dataset is constructed through iterative self-prompting where the teacher is used to both respond to an instruction and refine the instruction based on the response.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/RS52LKQL?page=4&annotation=BMVPQFPJ)



AI Feedback through Preferences (AIF) Human feedback (HF) can provide additional signal to align LLMs. Human feedback is typically given through preferences on the quality of LLM responses (Ouyang et al., 2022). For distillation, we instead use AI preferences from the teacher model on generated outputs from other models.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/RS52LKQL?page=4&annotation=R9ML27KH)



Distilled Direct Preference Optimization (dDPO) The goal of the final step is to refine the πdSFT by maximizing the likelihood of ranking the preferred yw over yl in a preference model. The preference model is determined by a reward function rθ(x, y) which utilizes the student language model πθ.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/RS52LKQL?page=4&annotation=ZR34EK8I)



Past work using AI feedback has primarily focused on using RL methods such as proximal policy optimization (PPO) to optimize θ with respect to this reward. These approaches optimize θ by first training the reward and then sampling from the current policy to compute updates. Direct preference optimization (DPO) uses a simpler approach to directly optimize the preference model from the static data (Rafailov et al., 2023). The key observation is to derive the optimal reward function in terms of the optimal LLM policy π∗ and the original LLM policy πdSFT.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/RS52LKQL?page=4&annotation=MGZHVFPY)



1. Compute the probability for (x, yw) and (x, yl) from the dSFT model (forward-only). 2. Compute the probability for (x, yw) and (x, yl) from the dDPO model. 3. Compute Eq 1 and backpropagate to update. Repeat.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/RS52LKQL?page=4&annotation=GFGABXSU)



We use the Transformer Reinforcement Learning (TRL) library for fine-tuning (von Werra et al., 2020), in conjunction with DeepSpeed ZeRO3 (Rajbhandari et al., 2020) and FlashAttention-2 (Dao, 2023) to optimize memory and improve training speed.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/RS52LKQL?page=5&annotation=5CDR8BNL)



We did not experiment with parameter-efficient techniques such as LoRA (Hu et al., 2021), but expect similar results to hold with these methods.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/RS52LKQL?page=5&annotation=S5H7AWKE)



For the full set of hyperparameters and instructions on how to train the models, see: https://github.com/huggingface/alignment-handbook.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/RS52LKQL?page=5&annotation=J66NK74V)



UltraChat (Ding et al., 2023) is a self-refinement dataset consisting of 1.47M multi-turn dialogues generated by GPT-3.5-TURBO over 30 topics and 20 different types of text material. We initially ran dSFT over the whole corpus, but found the resulting chat model had a tendency to respond with incorrect capitalization and would preface its answers with phrases such as “I don’t have personal experiences”, even for straightforward questions like “How do I clean my car?”. To handle these issues in the training data, we applied truecasing heuristics to fix the grammatical errors (approximately 5% of the dataset), as well as several filters to focus on helpfulness and remove the undesired model responses. The resulting dataset contains approximately 200k examples.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/RS52LKQL?page=5&annotation=NX6MJHX5)



UltraFeedback (Cui et al., 2023) consists of 64k prompts, each of which have four LLM responses that are rated by GPT-4 according to criteria like instruction-following, honesty, and helpfulness.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/RS52LKQL?page=5&annotation=UNXJ23LQ)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/tunstallZephyrDirectDistillation2023/image-6-x95-y152.png]]



Compared to other open 7B models, ZEPHYR-7B sets a new state-of-the-art and performs significantly better than dSFT models across both benchmarks.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/RS52LKQL?page=6&annotation=PM3TFPEU)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/tunstallZephyrDirectDistillation2023/image-7-x104-y355.png]]



show that without an initial SFT step (dSFT), models are not able to learn at all from feedback and perform terribly. Using dSFT improves model score significantly on both chat benchmarks.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/RS52LKQL?page=7&annotation=IH9XTQVG)



we see that the full Zephyr models (dDPO+dDSFT) gives a large increase in both benchmarks.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/RS52LKQL?page=7&annotation=ZLS25G3W)



In the process of training ZEPHYR-7B we observed that after one epoch of DPO training, the model would strongly overfit,” Yellow Highlight [Page 7](zotero://open-pdf/library/items/RS52LKQL?page=7&annotation=IEXFW9SN)



Surprisingly, this did not harm downstream performance on MT-Bench and AlpacaEval” Yellow Highlight [Page 7](zotero://open-pdf/library/items/RS52LKQL?page=7&annotation=U5EQW7ND)



the strongest model was obtained with one epoch of SFT followed by three epochs of DPO. However, we do observe that if the SFT model is trained for more than one epoch, the DPO step actually induces a performance regression with longer training.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/RS52LKQL?page=7&annotation=WJYLUM7R)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/tunstallZephyrDirectDistillation2023/image-8-x61-y386.png]]




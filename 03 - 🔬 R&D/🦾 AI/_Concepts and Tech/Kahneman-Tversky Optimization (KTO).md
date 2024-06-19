---
Title: Kahneman-Tversky Optimization (KTO) A Novel Approach for Aligning Language Models
Description: An overview of Kahneman-Tversky Optimization (KTO), a new method for aligning language models with human preferences using binary feedback signals, based on insights from prospect theory.
Date: 2024-06-10
Tags:
 - "#LanguageModelAlignment"
 - "#KahnemanTverskyOptimization" 
 - "#ProspectTheory"
 - "#BehavioralEconomics"
---

Kahneman-Tversky Optimization (KTO) is a novel approach for aligning language models with human preferences, introduced by researchers at Contextual AI.[4][7][10] KTO builds upon the seminal work of Daniel Kahneman and Amos Tversky on prospect theory, which describes how humans perceive and evaluate gains and losses in a biased but well-defined manner.[5][8][13]

## Key Insights of KTO

- KTO directly optimizes the utility of language model outputs based on a binary signal of whether an output is desirable or undesirable for a given input.[4][7][10]
- This contrasts with existing alignment methods like RLHF and DPO, which rely on preference data (e.g., output A is better than output B for input X).[4][7][10]
- KTO leverages a Kahneman-Tversky model of human utility, accounting for cognitive biases such as loss aversion.[7][10][11]
- Empirical results show that KTO matches or exceeds the performance of preference-based methods across model scales from 1B to 30B parameters.[4][7][10]

## Advantages of KTO

The key advantage of KTO is that it does not require expensive and scarce preference data. Instead, it can learn from abundant binary feedback signals that are easier to collect in real-world settings.[4][7][10] This makes KTO more practical and scalable compared to preference-based alignment methods.

Furthermore, KTO has been shown to work well even with significantly fewer desirable examples (up to 90% less), suggesting it is not overly reliant on preference pairs.[7] In some cases, KTO can even eliminate the need for supervised fine-tuning when the pre-trained model is already of high quality.[7]

## Implications and Future Directions

The success of KTO highlights the importance of interdisciplinary insights from behavioral economics and psychology for advancing AI alignment research.[7][10][17] It opens up new possibilities for efficiently gathering and utilizing human feedback in the development of safe and beneficial language models.

As research in this area progresses, we can expect further refinements and extensions to the KTO framework, as well as its application to a broader range of tasks and domains. Exploring the optimal settings for KTO in different scenarios and investigating other cognitive biases that could be modeled to improve alignment remain promising avenues for future work.[7][17]

## List of Relevant Backlinks
- [[Prospect Theory]]
- [[Language Model Alignment]]
- [[Reinforcement Learning from Human Feedback (RLHF)]]
- [[Direct Preference Optimization (DPO)]]

Sources
[1] RLHF and alternatives: KTO - Argilla https://argilla.io/blog/mantisnlp-rlhf-part-7/
[2] Prospect Theory in Psychology: Loss Aversion Bias https://www.simplypsychology.org/prospect-theory.html
[3] The Impact of Cognitive Biases on Professionals' Decision-Making https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8763848/
[4] Better, Cheaper, Faster LLM Alignment with KTO - Contextual AI https://contextual.ai/better-cheaper-faster-llm-alignment-with-kto/
[5] Prospect theory - Wikipedia https://en.wikipedia.org/wiki/Prospect_theory
[6] Cognitive Bias – Everything You Need to Know - InsideBE https://insidebe.com/articles/cognitive-bias/
[7] KTO: Model Alignment as Prospect Theoretic Optimization https://www.emergentmind.com/papers/2402.01306
[8] Kahneman and Tversky's Prospect Theory - San Jose State University https://www.sjsu.edu/faculty/watkins/prospect.htm
[9] [PDF] Judgment under Uncertainty: Heuristics and Biases Amos Tversky https://www2.psych.ubc.ca/~schaller/Psyc590Readings/TverskyKahneman1974.pdf
[10] KTO: Model Alignment as Prospect Theoretic Optimization https://huggingface.co/papers/2402.01306
[11] [PDF] Prospect Theory: An Analysis of Decision under Risk https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Behavioral_Decision_Theory/Kahneman_Tversky_1979_Prospect_theory.pdf
[12] KTO: Model Alignment as Prospect Theoretic Optimization - arXiv https://arxiv.org/abs/2402.01306
[13] Prospect theory | Psychology, Decision Making & Risk Analysis https://www.britannica.com/topic/prospect-theory
[14] Optimizing Decision Making - Opportunities in Neuroscience ... - NCBI https://www.ncbi.nlm.nih.gov/books/NBK207973/
[15] Prospect Theory: An Analysis of Decision under Risk - jstor https://www.jstor.org/stable/1914185
[16] [PDF] KTO: Model Alignment as Prospect Theoretic Optimization - arXiv https://arxiv.org/pdf/2402.01306.pdf
[17] Prospect Theory - an overview | ScienceDirect Topics https://www.sciencedirect.com/topics/psychology/prospect-theory
[18] Kawin Ethayarajh on X: "This also means that instead of directly ... https://twitter.com/ethayarajh/status/1732837528317862105
[19] Prospect Theory - an overview | ScienceDirect Topics https://www.sciencedirect.com/topics/social-sciences/prospect-theory

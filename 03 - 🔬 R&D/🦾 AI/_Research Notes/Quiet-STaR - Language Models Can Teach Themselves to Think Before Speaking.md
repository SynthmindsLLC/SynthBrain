---
Publish Year: "2024"
Authors: Eric Zelikman, Georges Harik, Yijia Shao, Varuna Jayasiri, Nick Haber, Noah D. Goodman
URL: http://arxiv.org/abs/2403.09629
Zotero Link: zotero://select/library/items/FBBL2CPZ
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#Computer-Science---Machine-Learning"
  - "#reasoning"
Published:
---
# Summary

## Purpose
The research was initiated to explore how language models (LMs) can improve their performance on various tasks by reasoning about the implications of text to predict future text. This study aims to extend the capabilities of LMs beyond solving individual or predefined sets of tasks, focusing on general reasoning from large internet text corpora.

## Methods
- The study builds on the Self-Taught Reasoner (STaR) approach, extending it to train LMs to generate reasoning that helps infer future text from a large internet text corpus.
- It introduces Quiet-STaR, a technique that trains the model to "think before it speaks" by generating rationales after every token, mixing future-text predictions with and without rationales, and learning to generate better rationales using a REINFORCE-based reward.
- A parallel sampling algorithm is proposed for scalable training, generating rationales from all token positions in a given string.
- Custom meta-tokens are introduced to signal the start and end of a rationale, and a mixing head is applied to determine how much to incorporate the next-token prediction from a given thought into the current next-token prediction.
- A non-myopic loss function is used, including multiple tokens ahead for language modeling, to improve the effect of thinking.

## Key Findings
- Quiet-STaR, without dataset-specific fine-tuning, significantly improves zero-shot direct reasoning abilities on CommonsenseQA and GSM8K, with improvements consistently increasing with the number of tokens used in the LM’s internal thoughts.
- The approach generalizes STaR to learn reasoning from diverse unstructured text data, marking the first explicit training of LMs to reason generally from text rather than on curated reasoning tasks.
- The study demonstrates that thinking allows the LM to predict difficult tokens better than one trained on the same web text, with improvements observed with longer thoughts.

## Discussion
The discussion highlights the significance of enabling LMs to self-improve their reasoning capabilities through self-generated rationales and the potential impact on various fields requiring natural language understanding and reasoning. It suggests that Quiet-STaR represents a significant step forward in teaching LMs to leverage their own generated thoughts to reason more thoroughly about inputs, potentially leading to more coherent and structured outputs.

## Critiques
- The study acknowledges the substantial overhead introduced by Quiet-STaR, as it generates many tokens before generating every additional token, which could impact efficiency.
- It raises ethical questions regarding the faithfulness of the model's expressed reasoning and the potential for harmful or biased reasoning patterns if the model finds them useful.
- The effectiveness of these techniques when applied to models trained from scratch or to models with different parameters remains to be fully explored.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Computation-and-Language
- #Computer-Science---Machine-Learning
- #reasoning

# Annotations
Reasoning about implications of text to predict later text has consistently been shown to improve LM performance on a variety of tasks, but methods for allowing LMs to learn from their reasoning (e.g., Zelikman et al. 2022) have focused on solving individual tasks or predefined sets of tasks (e.g., Wei et al. 2021b).” Yellow Highlight [Page 1](zotero://open-pdf/library/items/FCTSP5YC?page=1&annotation=CC275KI4)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zelikmanQuietSTaRLanguageModels2024/image-2-x106-y515.png]]



the Self-Taught Reasoner (STaR, Zelikman et al. 2022) showed that LMs can bootstrap their reasoning ability on question-answering (QA) datasets by sampling rationales to attempt to answer questions, training on rationales if they led to a correct final answer, and then repeating this to iteratively solve more difficult problems.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=5CM3V46N)



we extend STaR – instead of the LM learning to reason on particular tasks like mathematical QA, we train an LM to generate reasoning that helps it infer future text from a large internet text corpus.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=77AK3FPS)



”language models are unsupervised multitask learners” (Radford et al., 2019)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=W7Z6B7ZB)



as in STaR, we leverage the LM’s pre-existing reasoning ability to generate rationales and train the LM on them with a REINFORCE-based reward (Williams, 1992). We refer to this technique as Quiet-STaR, as it can be understood as applying STaR “quietly”, training the model to think before it speaks.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=WMQ9FLSK)



Broadly, Quiet-STaR proceeds by generating rationales after every token to explain future text (think), mixing the future-text predictions with and without rationales (talk), and then learning to generate better rationales using REINFORCE (learn).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=VBCQWNBZ)



even without dataset-specific fine-tuning, Quiet-STaR results in improvements to zero-shot directreasoning abilities on CommonsenseQA (36.3%→47.2%) and GSM8K (5.9%→10.9%), and that these improvements consistently increase with the number of tokens used in the LM’s internal thoughts.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=4EZEKW7B)



We generalize STaR to learn reasoning from diverse unstructured text data. To our knowledge, this is the first work explicitly training LMs to reason generally from text, rather than on curated reasoning tasks or collections of reasoning tasks.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=G5IENI8Z)



We propose and implement a parallel sampling algorithm that makes our training procedure scalable, generating rationales from all token positions in a given string.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=Z3PHH7YZ)



We introduce custom meta-tokens at the start and end of each thought to allow the LM to learn that it should be generating a rationale and when it should make a prediction based on that rationale.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=HNXN6BP4)



We apply a mixing head to retrospectively determine how much to incorporate the next-token prediction from a given thought into the current next-token prediction.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=AEKEYXCU)



We show that a non-myopic loss, including multiple tokens ahead for language modeling, improves the effect of thinking.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=NSJ6TPSS)



On multiple tasks, we demonstrate that thinking allows the LM to predict difficult tokens better than one trained on the same web text, improving with longer thoughts.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/FCTSP5YC?page=2&annotation=T7I3HM2J)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zelikmanQuietSTaRLanguageModels2024/image-3-x98-y488.png]]



Rajani et al. (2019) demonstrated that a pre-trained language model fine-tuned to output on human reasoning traces before answering multiple-choice commonsense reasoning questions outperformed one trained directly on answers.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/FCTSP5YC?page=3&annotation=X2CYYDDL)



Shwartz et al. (2020) demonstrated that language models, when provided with some scaffolding, can generate these helpful chain-of-thought solutions without additional supervision.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/FCTSP5YC?page=3&annotation=NJ8I8C42)



Nye et al. (2021) demonstrated that “scratchpads” required less scaffolding when the language models were more capable, a result later reinforced by Wei et al. (2022b), emphasizing informal tasks, and further strengthened by Kojima et al. (2022), demonstrating this behavior could be accomplished zero-shot.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/FCTSP5YC?page=3&annotation=HY4EDM2E)



Wang & Zhou (2024) showed further that for commonsense-question answering, one could force a language model to leverage chain-of-thought reasoning by preventing it from emitting any valid answer tokens unless it was confident.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/FCTSP5YC?page=3&annotation=W5DAQ5Y7)



One direction that researchers have used to train language models to reason or improve their reasoning is training the language model on mined reasoning traces or reasoning-like data (Rajani et al., 2019; Wei et al., 2021a; Lewkowycz et al., 2022; Chung et al., 2022; Gunasekar et al., 2023).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/FCTSP5YC?page=3&annotation=J4SHJSJI)



It requires either manual annotation, which is sensitive to the capability of the annotators and is off-policy for the language model (i.e., the distribution of reasoning is not text that the language model would otherwise likely have generated).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/FCTSP5YC?page=3&annotation=ZDT2DMVZ)



Another direction for teaching reasoning relies on a language model’s own generated reasoning, which can be seen as building on a large body of literature on self-play (Silver et al., 2017; Anthony et al., 2017; Polu & Sutskever, 2020).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/FCTSP5YC?page=3&annotation=HZHE6IR6)



Algorithm 1: Quiet Self-Taught Reasoner (Quiet-STaR) Input: Language model θ0, training steps num steps, sequence length l, thought length t, learning rate α, batch size b, number of thoughts nthoughts, number of ground truth tokens used for supervising each thought ntrue Output: Language model θ that generates rationales to predict future text for i = 0 to num steps do Sample batch of sequences X of length l hinit ← hidden statesθi (X) for j = 1 to l in parallel using attention mask do log pinit j:j+ntrue ← lm headθi (hinit j:j+ntrue ) // Predict next tokens Tj ← generate tokensθi ([X:j; <start thought>], t, nthoughts) // Generate thought Tj ← [Tj; <end thought>] hthought j:j+ntrue ← hidden statesθi ([X:j; Tj; Xj:j+ntrue ]) log pthought j:j+ntrue ← lm headθi (hthought j:j+ntrue ) // Predict next tokens w/ thought wj:j+ntrue ← mixing headθi (hthought j:j+ntrue , hinit j:j+ntrue ) log ptalk j ← wj:j+ntrue · log pinit j:j+ntrue + (1 − wj:j+ntrue ) · log pthought j:j+ntrue // Mix logits LNLL j ← − log ptalk j:j+ntrue (Xj+1:j+ntrue+1) rj = log ptalk j:j+ntrue (Xj+1:j+ntrue+1) − log ptalk j:j+ntrue (Xj+1:j+ntrue+1) ∇θ LREINFORCE j ← −rj1[rj > 0] · ∇θ log pθi (Tj|[X:j; <start thought>]) ∇θ Lj ← ∇θ LNLL j + ∇θ LREINFORCE j θi+1 ← θi − α ∑lj=1 ∇θ Lj // Update model parameters return θnum steps” Yellow Highlight [Page 4](zotero://open-pdf/library/items/FCTSP5YC?page=4&annotation=2FLKW7LX)



Self-Taught Reasoner (Zelikman et al., 2022), which demonstrated that a language model iteratively trained on its reasoning that led to correct answers could solve increasingly difficult problems.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/FCTSP5YC?page=4&annotation=6YZFBPXE)



Huang et al. (2022) which demonstrated that the algorithm proposed in STaR could still work if one assumed that the majority-vote answer was correct (although this has a lower ultimate performance).” Yellow Highlight [Page 4](zotero://open-pdf/library/items/FCTSP5YC?page=4&annotation=LJXRGPZ8)



recently VSTaR (Hosseini et al., 2024) that demonstrates that training a verifier to guide generation also improves performance, as well as TRICE (Hoffman et al., 2024) which maximizes the marginal likelihood of the correct answer given several reasoning traces per problem.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/FCTSP5YC?page=4&annotation=QN5U6RU4)



Recently, a growing body of work has demonstrated the usefulness of custom tokens optimized to perform specific functions in the context of a neural network – for this reason, they have also been referred to as “function vectors.” (Todd et al., 2023).” Yellow Highlight [Page 4](zotero://open-pdf/library/items/FCTSP5YC?page=4&annotation=NM8JCC6T)



One of the original instantiations of this was prompt-tuning (Lester et al., 2021) (and relatedly prefix-tuning (Li & Liang, 2021)), where the embeddings corresponding to the tokens of a prompt could be optimized to better accomplish a task.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/FCTSP5YC?page=4&annotation=AKT3M8LX)



Others have applied meta-tokens to compress long prompts (Li et al., 2023; Jung & Kim, 2023) for efficiency. Most relevant to this work, Mu et al. (2024) optimized a token such that, when the tokens after it could not attend to the tokens before it (i.e., a context compression token), it would provide sufficient information to future tokens.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/FCTSP5YC?page=4&annotation=7Q75AMRT)



one related work, Goyal et al. (2023) show that learning a single ”pause” token (essentially representing each token as two tokens) improves LM performance. However, unlike the thought tokens in our work, this pause token does not initialize a thought – instead, it can be seen as acting as the entirety of the thought.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/FCTSP5YC?page=5&annotation=JUTNMQPG)



we introduce an auxiliary ‘rationale’ variable between each pair of observed tokens of the sequence.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/FCTSP5YC?page=5&annotation=DIKJ54SJ)



Some work has aimed to explain the effects of chain-of-thought reasoning, namely attributing it to “locality of experience” (Prystawski et al., 2024). More broadly, reasoning allows a model to decompose a challenging computation into smaller steps.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/FCTSP5YC?page=5&annotation=HKZ3A4HZ)



we train the model to learn which decomposition and planning steps are effective in predicting future text.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/FCTSP5YC?page=5&annotation=BZ5MTBE5)



we find that the non-myopic formulation leads to a more effective loss for learning rationales.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/FCTSP5YC?page=5&annotation=CESRIM2C)



Quiet-STaR operates with three main steps (Figure 1): 1. Parallel rationale generation (think, Subsection 4.2): In parallel across n tokens xi in an input sequence x0:n, we generate r rationales of length t: ci = (ci1, . . . , cit), resulting in n × r rationale candidates. We insert learned <|startofthought|> and <|endofthought|> tokens to mark each rationale’s start and end. 2. Mixing post-rationale and base predictions (talk, Subsection 4.3): From the hidden state output after each rationale, we train a ”mixing head” – a shallow MLP producing a weight determining how much the post-rationale next-token predicted logits should be incorporated compared to the base language model predicted logits. This approach eases distribution shift early in finetuning, due to introducing rationales. 3. Optimizing rationale generation (learn, Subsection 4.4): We optimize the rationale generation parameters (start/end tokens and LM weights) to increase the likelihood of rationales that make future text more probable. We use REINFORCE to provide a learning signal to rationales based on their impact on future-token prediction. To reduce variance, we apply a teacher-forcing trick to include in the loss the likelihood of predicting not only the token after the thought but also later tokens” Yellow Highlight [Page 5](zotero://open-pdf/library/items/FCTSP5YC?page=5&annotation=9LUK5SGV)



We allow for highly parallel generation by first observing that an inference pass of a language model produces a probability distribution over the next tokens for all input tokens. Naturally, this allows us to sample one next token from each token in the input. If one has generated a successor from each token, it is not possible to simply continue with the original sequence. For example, imagine predicting the next token after each token of “< bos > the cat sat” one might generate “yes orange saw down” –” Yellow Highlight [Page 5](zotero://open-pdf/library/items/FCTSP5YC?page=5&annotation=GHE3JS2Y)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zelikmanQuietSTaRLanguageModels2024/image-6-x101-y521.png]]



We can, however, leverage these continuations to generate hidden thoughts for each observed token.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/FCTSP5YC?page=6&annotation=3BH97N9N)



When starting with a pre-trained model, thoughts will initially be out of distribution, and hence harm language modeling performance. To smooth the transition to thinking, we introduce a learned interpolation between the LM predictions with and without thoughts. Given the end-of-thought token’s hidden state and the hidden state of the original text token, the mixing head outputs a weight that determines the extent to which the postthought prediction logits will be used.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/FCTSP5YC?page=6&annotation=MMBSVANF)



The <|startofthought|> and <|endofthought|> tokens serve as learned meta-tokens that control the model’s rationale generation. Optimizing the representation of these tokens, especially the <|startofthought|> token, is crucial but challenging due to the discrete nature of the rationale tokens.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/FCTSP5YC?page=6&annotation=8LI49W7V)



We initialize the start and end token embeddings to the embedding corresponding to the em dash, ”−−−”” Yellow Highlight [Page 6](zotero://open-pdf/library/items/FCTSP5YC?page=6&annotation=NGE94K86)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zelikmanQuietSTaRLanguageModels2024/image-7-x100-y517.png]]



we use the parallel attention mask to compute the log probabilities of the true next tokens, applying teacher forcing by assuming the model selected the correct next ground-truth token (as implicit in normal language modeling with transformers).” Yellow Highlight [Page 7](zotero://open-pdf/library/items/FCTSP5YC?page=7&annotation=7QYDNKVK)



We use REINFORCE to optimize the likelihoods of the rationales based on their usefullness: the log-likelihood of the ntrue true next tokens Xj+1:j+ntrue+1 under the language model given previous observed tokens and a particular rationale (ptalk j:j+ntrue as shorthand for the mixed prediction probabilities after thinking, see Algorithm 1).” Yellow Highlight [Page 7](zotero://open-pdf/library/items/FCTSP5YC?page=7&annotation=7XI2E9SG)



This loss term encourages the model to generate rationales that improve its predictions of future tokens compared to the average prediction across all generated rationales for that token.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/FCTSP5YC?page=7&annotation=BNMC9S4W)



Intuitively, not all tokens require equal amounts of thought. For example, consider the sentence “the person is run-”: although there is inevitably some probability of the token being something other than “ing”2, as a standalone sentence without context, additional thinking is unlikely to improve a well-trained model’s prediction. Indeed, we conjecture that for most chunks of most online text, additional thought has little to no impact.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/FCTSP5YC?page=8&annotation=924GZJ6I)



Quiet-STaR does not benefit all tokens equally.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/FCTSP5YC?page=8&annotation=FT2UXB2C)



we design our experiments to investigate whether our approach is useful in predicting tokens that do require thought.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/FCTSP5YC?page=8&annotation=9ND3JIW9)



On CommonsenseQA, we find that Quiet-STaR improves performance by 10.9% compared to the base language model.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/FCTSP5YC?page=8&annotation=LJSNH3HF)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zelikmanQuietSTaRLanguageModels2024/image-9-x101-y503.png]]



We can compare these improvements to those offered by pause tokens (Goyal et al., 2023), which can be seen as a constrained version of Quiet-STaR where each token is represented by two tokens and the second ”pause” token acts as the entirety of the thought.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/FCTSP5YC?page=9&annotation=PGQ8CQND)



Goyal et al. (2023) found that pause token fine-tuning harms performance. Moreover, on both tasks (and the majority of their evaluated tasks), they observed that additional thought tokens harmed performance.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/FCTSP5YC?page=9&annotation=P9PEHN8S)



“lukewarm effect of pause-finetuning a standard-pretrained model” (Goyal et al., 2023). This suggests that allowing the model to generate multi-token rationales leads to more effective reasoning compared to the single-token ”pauses”.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/FCTSP5YC?page=9&annotation=5BZ8NMAJ)



these downstream results validate that training a language model to predict the subtext between the lines of general text data can substantially improve its reasoning capabilities, even on datasets it was not explicitly trained on. The fact that longer rationales consistently lead to better outcomes, and that Quiet-STaR outperforms the constrained pause token approach, supports the notion that Quiet-STaR is successfully teaching the model to leverage its own generated thoughts to reason more thoroughly about the input.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/FCTSP5YC?page=9&annotation=8AAVS3Z9)



We note that while there are natural parallels between chain-of-thought prompting and our approach, they are essentially orthogonal. In chain-of-thought a user actively prompts the model to think ‘out loud’, otherwise using its ordinary production distribution; Quiet-STaR instead thinks quietly at every token, with a distribution trained to be useful.” Yellow Highlight [Page 11](zotero://open-pdf/library/items/FCTSP5YC?page=11&annotation=SLLLZ4DV)



internal rationales may allow the model to generate more structured and coherent chains of though” Yellow Highlight [Page 11](zotero://open-pdf/library/items/FCTSP5YC?page=11&annotation=S5MVXM2A)



it would be valuable to understand whether these techniques work when a model is trained from scratch. We have also only applied Quiet-STaR to a 7 billion parameter model, albeit a powerful one. The same techniques applied to a better model would likely yield disproportionately better results, as has often been observed for gains from reasoning (Wei et al., 2022a).” Yellow Highlight [Page 11](zotero://open-pdf/library/items/FCTSP5YC?page=11&annotation=5FWXTPF8)



Quiet-STaR results in a substantial overhead, generating many tokens before generating every additional token.” Yellow Highlight [Page 11](zotero://open-pdf/library/items/FCTSP5YC?page=11&annotation=LZFW3K6W)



This work raises some important ethical questions, many of which also apply to STaR. For example, it is impossible to know that the reasoning expressed by the model in language accurately represents the internal processing of the model (i.e., faithfulness).” Yellow Highlight [Page 12](zotero://open-pdf/library/items/FCTSP5YC?page=12&annotation=Q9YUZXDH)



here are no safeguards against harmful or biased reasoning patterns if the model finds them useful.” Yellow Highlight [Page 12](zotero://open-pdf/library/items/FCTSP5YC?page=12&annotation=KEWL7N28)




---
Publish Year: '2023'
Authors: "Jason Weston, Sainbayar Sukhbaatar"
URL: "http://arxiv.org/abs/2311.11829"
Zotero Link: "zotero://select/library/items/DMWT4WWQ"
tags:
  - "#Computer-Science---Artificial-Intelligence, #Computer-Science---Computation-and-Language, #Computer-Science---Machine-Learning, #ai, #system-2"
---
# Summary
## Purpose

## Methods

## Key Findings

## Discussion

## Critiques

## Citations 

# Annotations
that the underlying problem is inherent in the way the transformer itself is built, and in particular its attention mechanism. That is, soft attention tends to assign probability to a large portion of the context, including irrelevant portions, tends to overly focus on repeated tokens partly due to the way it is trained” Yellow Highlight [Page 1](zotero://open-pdf/library/items/L9ALS3IJ?page=1&annotation=IJRZ9S9W)



(Holtzman et al., 2019; Welleck et al., 2019), and partly due to the position encoding mechanism is also inclined to treat the context as a bag-of-words when it should not (Sinha et al., 2021; 2020).” Yellow Highlight [Page 1](zotero://open-pdf/library/items/L9ALS3IJ?page=1&annotation=2LPZM3M2)



performing attention by using the LLM as a natural language reasoner” Yellow Highlight [Page 1](zotero://open-pdf/library/items/L9ALS3IJ?page=1&annotation=5U4UZUD6)



we leverage the ability of LLMs to follow instructions, and prompt them to generate the context that they should pay attention to, such that it contains only relevant material that will not skew its reasoning.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/L9ALS3IJ?page=1&annotation=S85XZI9Z)



System 2 Attention (S2A)” Yellow Highlight [Page 1](zotero://open-pdf/library/items/L9ALS3IJ?page=1&annotation=6ENJ4ZQS)



System 2, allocating effortful mental activity, takes over in humans when we need to pay deliberate attention to a task, especially in situations where System 1 is likely to make errors” Yellow Highlight [Page 1](zotero://open-pdf/library/items/L9ALS3IJ?page=1&annotation=9QASUUXJ)



(Sloman, 1996)” Yellow Highlight [Page 1](zotero://open-pdf/library/items/L9ALS3IJ?page=1&annotation=7LZA4X5M)



![[image-2-x101-y468.png]]



S2A increases factuality from 62.8% to 80.3% compared to LLaMA-2-70B-chat, and on longform generation of arguments that contain distractor input sentiment it increases objectivity by 57.4%, and remains largely unaffected by the inserted opinions.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/L9ALS3IJ?page=2&annotation=MJQKYN6L)



t is known that the probability of a repeated phrase increases with each repetition, creating a positive feedback loop (Holtzman et al., 2019)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/L9ALS3IJ?page=2&annotation=I7HP9D2D)



models tend to repeat related topics in the context as well, not just specific tokens, because the latent representation is likely predictive of more tokens from that same topic space.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/L9ALS3IJ?page=2&annotation=EXRR85F9)



When the context contains opinion that the model copies this is termed sycophancy (Perez et al., 2022)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/L9ALS3IJ?page=2&annotation=XEW7JY9D)



Even the most powerful LLMs change their answer to a simple factual question when the context contains irrelevant sentences, which inadvertently upweight the token probability of incorrect answers by virtue of those tokens appearing in the context.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/L9ALS3IJ?page=2&annotation=6TBVWQBV)



System 2 Attention (S2A) is a simple two-step process: 1. Given the context x, S2A first regenerates the context x′ such that irrelevant parts of the context that will adversely affect the output are removed. We denote this x′ ∼ S2A(x). 2. Given x′, we then produce the final response from the LLM using the regenerated context instead of the original one: y ∼ LLM (x′).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/L9ALS3IJ?page=3&annotation=CZXBXS58)



This S2A instruction requires the LLM to regenerate the context, extracting the part that is beneficial for providing relevant context for a given query.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/L9ALS3IJ?page=3&annotation=4653VAWG)



n S2A, after the context is regenerated, with all necessary elements that should be attended to contained therein, the model then responds given only the regenerated context” Yellow Highlight [Page 3](zotero://open-pdf/library/items/L9ALS3IJ?page=3&annotation=PNVJ7IY5)



![[image-4-x105-y531.png]]



Suggest Correct Answer: “I think the answer is [correct answer], but I’m really not sure.” This statement tends to skew standard models to answer correctly more often than the fact-seeking question baseline alone.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/L9ALS3IJ?page=4&annotation=SN646ZKD)



Suggest Incorrect Answer: “I think the answer is [incorrect answer], but I’m really not sure.” or Refute Correct Answer: “I don’t think the answer is [correct answer], but I’m really not sure.”. These statements tends to skew standard models to answer incorrectly often compared to the baseline.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/L9ALS3IJ?page=4&annotation=BKKWRJTT)



Like: “I like this argument.” or Wrote: “I wrote this argument”. These statements tend to skew standard models to provide more positive comments. • Dislike: “I dislike this argument.” or Didn’t Write: “I didn’t write this argument.”. These statements tends to skew standard models to provide more negative comments.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/L9ALS3IJ?page=5&annotation=8QW6G4BB)



![[image-7-x98-y497.png]]



![[image-7-x98-y304.png]]



S2A, in contrast, has little or no degredation for all categories, and is not easily swayed by opinion, suffering only a slight loss on the Suggest Incorrect category.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/L9ALS3IJ?page=7&annotation=5QRYYY5Q)



This effect is even larger when the irrelevant sentences are on the same topic as the problems Figure 7 (right)” Yellow Highlight [Page 8](zotero://open-pdf/library/items/L9ALS3IJ?page=8&annotation=252RAKYU)



When S2A is used to extract relevant parts from the problem text before solving it, the accuracy jumps up about 12% for random distractors, and 10% for in-topic distractors.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/L9ALS3IJ?page=8&annotation=YSSQHXGI)



Adding a debiasing prompt to standard LLMs (“Instructed Prompting”) can bring improved performance over the baseline LLM (from 62.8% to 71.7%), but not as much as S2A (80.3%), and this method still shows sycophancy.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/L9ALS3IJ?page=9&annotation=ZLD88EWU)



Our method can be viewed as a type of (hard-)attention mechanism as it removes attention away from irrelevant parts of the input.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/L9ALS3IJ?page=9&annotation=8EV74G3Y)



Sycophancy is a phenomenon “where a model seeks human approval in unwanted ways”, as termed by Perez et al. (2022), and several works have shown that opinion inherent in a prompt will tend to make the model agree with the input, which they try to alleviate with training procedures (Sharma et al., 2023; Wei et al., 2023)” Yellow Highlight [Page 10](zotero://open-pdf/library/items/L9ALS3IJ?page=10&annotation=HJ2I3EKH)



The authors termed this “Nontrivial Repetition”, where the name emphasizes that this has more to do with overly upweighted token probabilities in the transformer attention mechanism (and hence, related to the standard repetition problem (Holtzman et al., 2019)), rather than to higher order concepts that imply agency such as seeking approval.” Yellow Highlight [Page 10](zotero://open-pdf/library/items/L9ALS3IJ?page=10&annotation=U5BXJQS8)



several works have shown that irrelevant context can adversely affect predictions (Jia & Liang, 2017; Cho et al., 2023; Shi et al., 2023).” Yellow Highlight [Page 10](zotero://open-pdf/library/items/L9ALS3IJ?page=10&annotation=VXEUDM55)




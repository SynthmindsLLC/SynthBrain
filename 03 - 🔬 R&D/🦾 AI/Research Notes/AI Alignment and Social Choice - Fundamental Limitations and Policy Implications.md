---
Publish Year: "2023"
Authors: Abhilash Mishra
URL: http://arxiv.org/abs/2310.16048
Zotero Link: zotero://select/library/items/2RVWUC98
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#Computer-Science---Computers-and-Society"
  - "#Computer-Science---Human-Computer-Interaction"
  - "#Computer-Science---Machine-Learning"
Published:
---
# Summary
## Purpose 
The paper addresses the challenge of aligning AI agents with human intentions and values, focusing on the limitations of Reinforcement Learning with Human Feedback (RLHF) in the context of democratic norms and social choice theory.

## Methods 
- Exploration of RLHF and its application in aligning AI agents.
- Analysis of Arrow-Sen impossibility theorems within the context of RLHF.
- Examination of the implications for AI governance and policy.

## Key Findings 
1. No unique voting protocol can universally align AI systems using RLHF through democratic processes.
2. Aligning AI agents with the values of all individuals violates certain private ethical preferences.
3. Transparent voting rules are needed for model builder accountability.
4. Focus should be on developing AI agents narrowly aligned to specific user groups.
5. Universal AI alignment using RLHF is impossible.

## Discussion 
The findings highlight a significant challenge in AI alignment, emphasizing the complexity of integrating human ethics and values in AI systems democratically. The research underscores the need for transparency in AI governance and the impracticality of achieving universal AI alignment.

## Critiques 
1. The paper could benefit from more diverse perspectives on AI alignment beyond RLHF.
2. There's a need for empirical evidence supporting the theoretical claims.
3. The paper may oversimplify the complexity of human values and ethical considerations.

## Tags
#AIAlignment #SocialChoiceTheory #RLHF #AIethics #AIgovernance.


# Annotations
In his seminal article Some Moral and Technical Consequences of Automation, Norbert Wiener [1] highlighted the need to ensure that the “purpose put into the machine is the purpose which we really desire.”” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=ETSQBE8W)



But how can we embed human intentions and values in machines? And whose values should be embedded?” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=W63TD4AB)



Machine Behavior [3] and Machine Ethics [4] which have explored how machines can be “taught” to learn human norms.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=LD4IVHVG)



Building on Rawlsian ideas of fairness [5], Dwork et al. [6] suggested that machine norms need to be “an approximation as agreed upon by society.”” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=4C9JLEGB)



Awad et al. [7] operationalized this idea for the case of autonomous vehicles by crowd-sourcing moral decisions from millions of online participants through the Moral Machine Experiment.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=8Y3CNEN5)



Noothigattu et al. [8] used data from the Moral Machine Experiment to build a model of aggregated moral preferences using tools from computational social choice [9, 10].” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=A4HKKEEL)



Reinforcement learning using human feedback (RLHF) has been the key technical innovation that has led to remarkable progress in developing aligned AI agents [12, 13, 14]” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=7V7KXNZE)



there remain open questions about how such alignment can be realized practically and at scale. More broadly, whose norms or values should they be aligned with? And how can we align AI systems by respecting democratic norms?” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=EEX69N9J)



Casper et. al. [19] provide an exhaustive review of fundamental limitations and open challenges in RLHF for AI alignment. In particular, they highlight the limitation of selecting “representative humans” to act as reinforcers during the training process.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=NP72PXVE)



OpenAI restricts human reinforcers who agree with “expert” researcher preferences [20].” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=RPZTD7X8)



Additionally, the demographics of reinforcers are not representative of end users.1” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PJRUKDQK?page=2&annotation=25VCTIZE)



we ask whether it is possible to design voting rules that allow a group of reinforcers, representative of a population of diverse users, to train an AI model using RLHF.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/PJRUKDQK?page=3&annotation=73VN27N8)



Using two widely known results from social choice theory, we show that there exist no unique voting rules that allow a group of reinforcers to build an aligned AI system by respecting democratic norms i.e. by treating all users and reinforcers the same.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/PJRUKDQK?page=3&annotation=8Y2IHFQH)



we show that it is impossible to build a RLHF model democratically that respects the private preferences of each user in a population simultaneously” Yellow Highlight [Page 3](zotero://open-pdf/library/items/PJRUKDQK?page=3&annotation=JSBL3PUX)



Our key result borrows from two widely known theorems in social choice theory - the impossibility theorems by Arrow and Sen - which are widely known constraints in voting theory.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/PJRUKDQK?page=3&annotation=S8SWYPYJ)



specifying a well-defined reward function to achieve alignment for AI language agents is impossible.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/PJRUKDQK?page=3&annotation=U5XN3VNZ)



The key innovation in RLHF is training AI agents to be aligned with humans without knowing the explicit reward function. Instead, the reward function is “discovered” via human feedback.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/PJRUKDQK?page=3&annotation=A6VMHYJA)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/mishraAIAlignmentSocial2023 1/image-4-x166-y535.png]]



test 2







plurality rule would choose a preference that has the largest number of votes, even when a preference does not have a clear majority (> 50%) votes” Yellow Highlight [Page 4](zotero://open-pdf/library/items/PJRUKDQK?page=4&annotation=622JH8PI)



alternative is the simple majority rule that which chooses a preference with the majority of votes in a ranked choice.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/PJRUKDQK?page=4&annotation=6KJYH4RC)



Arrow [24] posited four axioms that any reasonable aggregation/voting rule should satisfy. The axioms are:” Yellow Highlight [Page 4](zotero://open-pdf/library/items/PJRUKDQK?page=4&annotation=UJXLYEMM)



• Pareto or Consensus: an aggregation function f satisfies Pareto if, whenever every individual i ∈ N strictly prefers σ1 to σ2, the function f ranks σ1 strictly higher than σ 2. • Independence of irrelevant alternatives (IIA): the group members’ preferences about some alternative σ3 does not affect how the aggregation rule f ranks two different alternatives, σ1 6= σ3 and σ2 6= σ3. • Transitivity: If f produces an ordering in which σ1   σ2 and σ2   σ3, then it must also be the case that σ1   σ3. • No Dictator: a rule f is dictatorial when there exists one voter i such that every time σ1 ≻i σ2 (i.e., the dictator i strictly prefers σ1 to σ2), the aggregation rule f produces a strict ranking σ1 ≻ σ2. An aggregation rule f satisfies no dictator if it is not dictatorial.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/PJRUKDQK?page=5&annotation=IJ66N4T4)



To understand the implications of Arrow’s theorem for RLHF, suppose we want to design an AI agent through a democratic process. Arrow’s theorem implies that any voting rule that is Pareto efficient, transitive, and independent of irrelevant alternatives must grant all decision-making authority to a single individual/reinforcer.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/PJRUKDQK?page=5&annotation=4IMK2MJC)



Sen summarized this impossibility result in the following way: “given other things in the society, if you prefer to have pink walls rather than white, then society should permit you to have this, even if a majority of the community would like to see your walls white.”” Yellow Highlight [Page 5](zotero://open-pdf/library/items/PJRUKDQK?page=5&annotation=7SMS2VUU)



The theorem demonstrates that protecting the preferences of multiple individuals is at odds with the most basic notions of utilitarian ethics.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/PJRUKDQK?page=6&annotation=6L57KPNP)



Consider two reinforcers, A and B, and three outputs from an AI model (in the pre-RLHF stage). The three outputs correspond to normative statements about a political party X: • Output-1: Political party X is fascist • Output-2: Political party X is not fascist • Output-3: Political party X has a complicated agenda but it does not neatly fall into the above two categories.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/PJRUKDQK?page=6&annotation=RADRQP82)



Reinforcer A, who is very anti-X, prefers output 1, but given the choice between revealing their political bias and staying neutral, they would prefer to stay neutral over revealing their political affiliation.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/PJRUKDQK?page=6&annotation=C2J8GDNW)



In decreasing order of preference, their ranking is 3, 1, 2. Reinforcer-B, however, does not mind revealing their political beliefs and would rather assert Output 2 over staying neutral.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/PJRUKDQK?page=6&annotation=BLMKNCJ9)



If the choice is between Outputs 1 and 3, a liberal - someone who cares about individual rights above all else - might argue that Reinforcer-B’s preference should count; since Reinforcer-A would be OK not revealing their preference, and should not be forced to. Thus the final output after RLHF would lead to Output-3.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/PJRUKDQK?page=6&annotation=2XQGXEY6)



respecting individual preferences or liberal values would lead to preferring Output-3 over Output-1 and Output-2 over Output-3. Choosing the outputs from only one Reinforcer will break the Pareto axiom. We are thus left with an inconsistency.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/PJRUKDQK?page=7&annotation=3LVH82QM)



Arrow’s impossibility theorem implies that there is no unique voting rule that can allow us to train AI agents through RLHF while respecting democratic norms i.e., treating each reinforcer equally.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/PJRUKDQK?page=7&annotation=DT9MIEVV)



As Sen argued in his original paper, “liberal values conflict with the Pareto principle.”” Yellow Highlight [Page 7](zotero://open-pdf/library/items/PJRUKDQK?page=7&annotation=JTBE6SXS)



include the voting rule in a model card [26]” Yellow Highlight [Page 7](zotero://open-pdf/library/items/PJRUKDQK?page=7&annotation=ZX3MF4HH)



the simplest solution is for all AI model builders to agree on a specific voting rule.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/PJRUKDQK?page=7&annotation=SMS6TJHZ)



a user of an AI conversational agent in a classroom might prefer not to encounter language deemed racist by them. Sen’s theorem implies that it is impossible to build an RLHF model via democratic methods, such that every individual’s private preferences are respected.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/PJRUKDQK?page=8&annotation=GMW95LTT)



we cannot build artificial general intelligence aligned with all users’ intentions.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/PJRUKDQK?page=8&annotation=4PFE6STB)



any AI agent built using RLHF will be misaligned with every user in some dimension.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/PJRUKDQK?page=8&annotation=XATVAF7F)



we will have a family of aligned models for specific tasks/groups but not generally aligned models.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/PJRUKDQK?page=8&annotation=E27QDCSD)




---
Publish Year: "2023"
Authors: Mohammad Gheshlaghi Azar, Mark Rowland, Bilal Piot, Daniel Guo, Daniele Calandriello, Michal Valko, Rémi Munos
URL: http://arxiv.org/abs/2310.12036
Zotero Link: zotero://select/library/items/4IB3VX3Z
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Machine-Learning"
  - "#Statistics---Machine-Learning"
Published: 2024-01-23
---
# Summary
## Purpose   
Exploring a general theoretical framework for learning from human preferences, particularly focusing on how this approach can address the limitations of existing methods like [[Reinforcement Learning from Human Feedback]] (RLHF) and [[Direct Preference Optimization]] (DPO).  
  
## Methods   
- Analysis of RLHF and DPO within a new theoretical framework.  
- Introduction of [[Ψ-preference optimization]] (ΨPO) objective.  
- Development of [[Identity-Preference Optimization]] (IPO) method to avoid overfitting.  
- Empirical comparison of ΨPO, IPO, and traditional methods using illustrative examples.  
  
## Key Findings   
1. ΨPO offers a broader theoretical basis for preference learning, generalizing RLHF and DPO.  
2. IPO, a variant of ΨPO, effectively addresses overfitting issues inherent in RLHF and DPO.  
3. Empirical examples demonstrate the stability and robustness of IPO against overfitting.  
4. The paper highlights the importance of considering overfitting in preference-based learning models.  
  
## Discussion   
This research is pivotal for AI alignment, offering a fresh perspective on learning from human preferences. The IPO's ability to avoid overfitting is particularly relevant for developing AI systems that are better aligned with complex human values and preferences.  
  
## Critiques   
1. The practical applicability of these theoretical models in real-world scenarios remains to be thoroughly tested.  
2. Further research is needed to evaluate the scalability of IPO in more complex settings, such as large language models.  
3. The paper could benefit from more diverse empirical testing to substantiate its theoretical claims.  
  
## Tags  
#AIAlignment #HumanPreferences #ReinforcementLearning #PreferenceOptimization #Overfitting

# Annotations
Learning from human preferences (Christiano et al., 2017) is a paradigm adopted in the natural language processing literature to better align pretrained (Radford et al., 2018; Ramachandran et al., 2016) and instruction-tuned (Wei et al., 2022) generative language models to human desiderata.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/PCHB3ED2?page=1&annotation=J2G5DEAI)



We frame the problem of learning from human preferences as an offline contextual bandit problem (Lu et al., 2010). The goal of this bandit problem is that given a context to choose an action (playing the role of the generation) which is most preferred by a human rater under the constraint that the resulting bandit policy should be close to some known reference policy.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/PCHB3ED2?page=1&annotation=AB3X2LQK)



A prominent approach to tackle the problem of learning from human preferences is through reinforcement learning from human feedback (RLHF, Ouyang et al., 2022; Stiennon et al., 2020) in which first a reward model is trained in the form of a classifier of preferred and dispreferred actions. Then the bandit policy is trained through RL to maximize this learned reward model while minimizing the distance with the reference policy.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/PCHB3ED2?page=1&annotation=IJ47G5IU)



Furthermore recent works such as direct preference optimisation (DPO, Rafailov et al., 2023) and (SLiC-HF, Zhao et al., 2023) have shown that it is possible to optimize the bandit policy directly from human preferences without learning a reward model.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/PCHB3ED2?page=1&annotation=TZ985TYF)



In particular, we show that it is possible to characterise the objective functions of RLHF and DPO as special cases of a more general objective exclusively expressed in terms of pairwise preferences. We call this objective Ψ-preference optimisation (ΨPO) objective, where Ψ is an arbitrary non-deceasing mapping.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PCHB3ED2?page=2&annotation=35B93RFB)



Our theoretical investigation of RLHF and DPO reveals that in principle they can be both vulnerable to overfitting. This is due to the fact that those methods rely on the strong assumption that pairwise preferences can be substituted with ELo-score (pointwise rewards) via a Bradley-Terry (BT) modelisation (Bradley and Terry, 1952)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PCHB3ED2?page=2&annotation=BRAT95LH)



Identity-PO (IPO) and by construction bypasses the BT modelisation assumption for preferences” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PCHB3ED2?page=2&annotation=6WVZGS52)



The standard RLHF paradigm (Christiano et al., 2017; Stiennon et al., 2020) consists of two main stages: (i) learning the reward model; (ii) policy optimisation using the learned reward.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/PCHB3ED2?page=2&annotation=8GV4ANAV)



Learning a reward model consists in training a binary classifier to discriminate between the preferred and dispreferred actions using a logistic regression loss.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/PCHB3ED2?page=3&annotation=Z7PCNHWF)



Using the reward (Elo-score) r(x, y) the RLHF objective is simply to optimize for the policy π ∈ ∆YX that maximizes the expected reward while minimizing the distance between π and some reference policy πref ∈ ∆YX” Yellow Highlight [Page 3](zotero://open-pdf/library/items/PCHB3ED2?page=3&annotation=HEBKA3HZ)



An alternative approach to the RL paradigm described above is direct preference optimisation (DPO; Rafailov et al., 2023), which avoids the training of a reward model altogether.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/PCHB3ED2?page=3&annotation=C7I8USFG)



We have observed in the previous section that DPO is prone to overfitting, and this stems from a combination of the unboundedness of Ψ, together with not training an explicit reward function. Not training a reward function directly is a clear advantage of DPO, but we would like to avoid the problems of overfitting as well.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/PCHB3ED2?page=5&annotation=8SDTW9JK)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/azarGeneralTheoreticalParadigm2023/image-8-x32-y457.png]]



DPO always converges to the deterministic policy for all values of τ . In other word DPO completely ignores the reference policy, no matter how strong is the regularisation term, and converges to the action which is preferred in the dataset. On the other hand, IPO prevent the policy from becoming greedy when the regularisation is strong.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/PCHB3ED2?page=8&annotation=EBRIC25W)



IPO Does not Exclude Actions In the first example DPO converges to a deterministic policy because one action strictly dominates all others and the loss continues to push up its likelihood until it saturates.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/PCHB3ED2?page=8&annotation=SDZVAEF5)



whenever the action space is large but the dataset small, some actions will necessarily be sampled rarely or only once, making it likely to never observe a victory.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/PCHB3ED2?page=8&annotation=Q5V6MPAP)




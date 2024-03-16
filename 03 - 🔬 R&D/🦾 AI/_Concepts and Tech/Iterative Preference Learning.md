---
Date: [[2024-03-11]]
Tags: 
 - "#IterativePreferenceLearning"
 - "#MachineLearning"
 - "#ReinforcementLearning"
 - "#PolicyIteration"
 - "#QualitativeFeedback"
---

Iterative preference learning is a process in machine learning where an agent learns to make decisions based on qualitative feedback rather than numerical rewards. This approach is particularly useful in scenarios where numerical feedback is not naturally available or is difficult to define. Iterative preference learning integrates preference learning and reinforcement learning (RL), allowing agents to learn from qualitative reward signals such as pairwise preferences between actions in a given state.

The key idea is to equip the RL agent with qualitative policy models, like ranking functions, which can sort available actions from most to least promising. These models are learned from qualitative feedback, such as pairwise preferences, which indicate that one action is preferred over another in a specific state. This approach can be more natural and less challenging to acquire, especially in applications where the environment does not provide numerical rewards.

For example, in preference-based policy iteration, the agent may use a method called label ranking to learn from qualitative feedback. This method is advantageous because it allows the agent to make optimal decisions based on comparisons between pairs of actions, which can be more intuitive to provide than precise numerical gains.

Iterative preference learning can be applied in various domains, including those where feedback comes from human experts who provide qualitative assessments, such as medical treatment scenarios or game playing contexts. By focusing on qualitative comparisons, this approach can potentially reduce the complexity and increase the efficiency of the learning process.

- Important [[wikilinks]]:
  - [[Preference Learning]]
  - [[Reinforcement Learning]]
  - [[Policy Iteration]]
  - [[Qualitative Feedback]]
  - [[Label Ranking]]

Sources
[1] Preference-Based Policy Iteration: Leveraging Preference Learning for ... https://link.springer.com/chapter/10.1007/978-3-642-23780-5_30
[2] [2312.11456] Iterative Preference Learning from Human Feedback: Bridging Theory and Practice for RLHF under KL-Constraint - arXiv https://arxiv.org/abs/2312.11456
[3] [PDF] Iterative Learning: Leveraging the Computer as an On-Demand Expert ... https://homes.cs.washington.edu/~althoff/docs/iterative_learning.pdf
[4] A Preliminary Study on the Relationship Between Iterative Learning Control and Reinforcement Learning - ScienceDirect https://www.sciencedirect.com/science/article/pii/S2405896319326187
[5] Preference learning - Wikipedia https://en.wikipedia.org/wiki/Preference_learning
[6] Learning Trajectory Preferences for Manipulators via Iterative Improvement - NIPS papers https://proceedings.neurips.cc/paper/2013/hash/c058f544c737782deacefa532d9add4c-Abstract.html
[7] [PDF] AUTOMATIC PREFERENCE LEARNING ON SEMANTIC ... https://webs-deim.urv.cat/~itaka/itaka2/PDF/acabats/KallolNaha%20_TFM.pdf
[8] [PDF] Efficient Preference-Based Reinforcement Learning Using Learned Dynamics Models - arXiv https://arxiv.org/pdf/2301.04741.pdf
[9] [PDF] Bridging Theory and Practice for RLHF under KL-Constraint - arXiv https://arxiv.org/pdf/2312.11456.pdf
[10] [PDF] A Survey of Preference-Based Reinforcement Learning Methods https://jmlr.org/papers/volume18/16-634/16-634.pdf
[11] [PDF] SuperHF: Supervised Iterative Learning from Human Feedback - OpenReview https://openreview.net/pdf?id=QGrCoyplHu
[12] Preference-based reinforcement learning: a formal framework and a ... https://link.springer.com/article/10.1007/s10994-012-5313-8
[13] [PDF] Learning Trajectory Preferences for Manipulators via Iterative Improvement - Cornell CS https://www.cs.cornell.edu/people/tj/publications/jain_etal_13a.pdf
[14] [PDF] Preference Learning: An Introduction - CiteSeerX https://citeseerx.ist.psu.edu/document?doi=140198257948f50dd4fc8ca5b4f80fa897c473b1&repid=rep1&type=pdf
[15] Active preference learning in product design decisions - ScienceDirect.com https://www.sciencedirect.com/science/article/pii/S221282712100531X/pdf?md5=99a0a585763585f3e62940a13c6d30f8&pid=1-s2.0-S221282712100531X-main.pdf
[16] [PDF] Preference Learning: A Tutorial Introduction https://www2.cs.uh.edu/~ceick/ML/PL-Tutorial.pdf
[17] [PDF] Preference-Based Policy Iteration ... - Weiwei Cheng's Homepage https://www.weiweicheng.com/research/papers/cheng-ecml11a.pdf

---
Publish Year: '2023'
Authors: "Eduardo C. Garrido-Merchán, Sara Lumbreras-Sancho"
URL: "http://arxiv.org/abs/2307.11119"
Zotero Link: "zotero://select/library/items/SDQGBJ3Z"
tags:
  - "#Computer-Science---Computers-and-Society, #ethics"
Published:
---
# Summary
The research was initiated to explore the intersection of computational methods and ethical decision-making, addressing the significant issue of how technology can aid in understanding and applying ethical principles in the field of Computer Science, specifically within the Computers and Society and ethics subfields. The purpose of the study was to formalize and evaluate ethical decision-making through computational models.

## Methods
- Cultural evolution and multilevel selection theories to understand the evolution of cultural and ethical traits.
- Ethical realism and moral relativism to frame the philosophical underpinnings of ethical decision-making.
- Computational Ethics for formalizing and evaluating ethical decisions using mathematical and computational models.
- Reinforcement learning (RL) and Q-learning as computational methods to model ethical decision-making processes.

## Key Findings
- Ethical realism supports the possibility of a global ethic, suggesting shared moral values can be universally applied.
- Computational Ethics can formalize ethical guidelines and assess moral behavior through simulations and experiments.
- Reinforcement learning, specifically Q-learning, can model ethical decision-making by training agents to make decisions based on rewards.
- The dopamine reward hypothesis provides a biological basis for understanding rewards in human behavior, supporting the modeling of ethical decisions in computational terms.
- The existence of an optimal policy (objective ethic) for ethical decision-making can be formalized and is learnable through computational models.

## Discussion
The discussion in the research article highlights the potential of computational models, particularly reinforcement learning, to contribute to the understanding and application of ethics. It suggests that computational ethics offers a promising avenue for formalizing ethical decision-making processes and evaluating moral behavior through technology. The findings imply that there is an objective policy for ethical decision-making that can be discovered and applied universally, challenging the notion of ethical relativism and supporting the concept of a global ethic.

## Critiques
Upon evaluating the research, some critiques include:
- The oversimplification of ethical reasoning in computational models, which may not fully capture the complexity of human moral decision-making.
- The assumption that the world can be modeled as a Markov Decision Process (MDP), which may oversimplify the complexity of human experiences and ethical dilemmas.
- The potential challenge in defining a universal reward function that accurately represents ethical values across different cultures and individuals.

## Tags
- #Computer-Science---Computers-and-Society
- #ethics
- #ComputationalEthics
- #ReinforcementLearning
- #Q-learning
- #EthicalRealism
- #MoralRelativism

# Annotations
Cultural evolution is based on the idea that cultural traits, such as ideas, beliefs, and behaviors, can be passed down from one generation to the next and can evolve over time through various mechanisms” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HC6SPB5J?page=2&annotation=5595PBQA)



These ideas have been further refined by the introduction of multilevel selection [26], which explains that not only the individual traits are se- lected for, but also the group ones” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HC6SPB5J?page=2&annotation=UWD2I2S4)



Ethical realism is a philosophical stance that asserts the existence of moral truths that are independent of subjec- tive human opinions or beliefs. It proposes that ethical statements can be true or false and are founded on objective aspects of the world” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HC6SPB5J?page=2&annotation=W285QZYK)



This perspective differs from moral relativism, which refutes the existence of objective moral truths and claims that moral values and principles are contingent on cultural, historical, or per- sonal contexts.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HC6SPB5J?page=2&annotation=6MY3IWFS)



The supporters of ethical realism have paved the ground to the elicitation of a global ethic which seeks to identify shared moral values that can be universally applied across cultures and religions” Yellow Highlight [Page 2](zotero://open-pdf/library/items/HC6SPB5J?page=2&annotation=9PCX7TIU)



In our metaphor for human decision-making, policies will be used to represent ethical guidelines, as they are the mathematical expression of ”if under situation s, the agent should do action a”.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/HC6SPB5J?page=3&annotation=PPYRYIBP)



Computational Ethics is concerned with the creation and utilization of technological means to formalize and appraise ethical decision-making. This entails the applica- tion of ethical decision-making processes, the deployment of mathemat- ical and computational models to represent moral tenets, and the use of simulations and experiments to assess moral behavior.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/HC6SPB5J?page=3&annotation=CLR46X7E)



Reinforcement learning (RL) is a subfield of machine learning that focuses on training agents to make decisions by interacting with an environment. It is fundamentally rooted in the Markov Decision Process (MDP) framework, which is defined by a tuple (S, A, P, R, γ), where S is the state space, A is the action space, P represents the state transition probabilities, R is the reward function, and γ is the discount factor.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/HC6SPB5J?page=4&annotation=JZVVRE9W)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/garrido-merchanComputationalEthicsMorality2023/image-4-x94-y161.png]]



Critically, Q-learning is a widely-used, model-free (this means that it is free from any assumptions about the working of the outside world)” Yellow Highlight [Page 4](zotero://open-pdf/library/items/HC6SPB5J?page=4&annotation=4UNQMWTW)



The Bellman optimality equation characterizes Q⋆ as follows: Q ⋆ (s, a) = E[R(s, a) + γmaxa′Q ⋆ (s ′ , a′)], where s ′ is the successor state after taking action a in state s. Q-learning iteratively updates the estimated action-value function, Q(s, a), based on observed transitions (s, a, r, s′) using the update rule: Q(s, a) = Q(s, a) + α[r + γmaxa′Q(s ′ , a′) − Q(s, a)], where α is the learning rate. The Q-learning algorithm guarantees convergence to the optimal action-value function Q⋆ under certain conditions, such as using a sufficiently small learning rate and exploring the state-action space infinitely often.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/HC6SPB5J?page=5&annotation=AUXSWZ6D)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/garrido-merchanComputationalEthicsMorality2023/image-5-x100-y350.png]]



Although the model, as described above, is overly simplistic, it should be noted by the reader that it is sufficiently flexible to account for most of the relevant features of ethical reasoning” Yellow Highlight [Page 5](zotero://open-pdf/library/items/HC6SPB5J?page=5&annotation=MZGKIHLY)



First, the definition of the reward function is key. A very useful attempt at understanding the reward function in human behavior is dopamine reward hypothesis.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/HC6SPB5J?page=5&annotation=IV85A5DX)



the dopamine reward hypothesis posits that dopamine, a neurotransmitter, plays a crucial role in mediating the experience of reward and reinforcement, as well as driving motivated behaviors in animals and humans” Yellow Highlight [Page 6](zotero://open-pdf/library/items/HC6SPB5J?page=6&annotation=CVTYPFWZ)



This hypothesis is supported by a wealth of experimental evidence, including the observation that dopamine neurons in the ventral tegmental area (VTA) and substantia nigra (SN) project to regions involved in processing rewards, such as the nucleus accumbens (NAc) and the prefrontal cortex (PFC) [7]. Electrophysiological studies have demonstrated that dopamine neurons exhibit phasic activity in response to both unexpected rewards and reward-predicting cues, consistent with a role in encoding reward prediction errors” Yellow Highlight [Page 6](zotero://open-pdf/library/items/HC6SPB5J?page=6&annotation=DL4IBVP6)



Under a consequentialist view, the morally right action is the one that produces the best overall outcome or consequence. This means that the end justifies the means, and the focus is on maximizing good consequences while minimizing bad consequences.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/HC6SPB5J?page=6&annotation=WC75LXP5)



Now, the reward function can be defined in a global manner by taking into account the full humanity. This would lead to utilitarianism, which holds that the morally right action is the one that maximizes overall happiness or pleasure. On the contrary, if the reward function is defined based only on parameters that pertain to the individual, we can formalize ethical egoism, which argues that individuals should act in their own selfinterest to maximize their own well-being.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/HC6SPB5J?page=6&annotation=U5NPE82D)



Theorem 1. Assume |A| < ∞, |S| < ∞ and |r| < ∞ with probability one. For any infinite horizon discounted MDP, there always exists a deterministic stationary policy that is optimal.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/HC6SPB5J?page=7&annotation=DNKD6XGD)



The philosophical assumption that the world can be modeled as a Markov Decision Process (MDP) perceived by human agents suggests that the complexity of human experience can be reduced to a series of states, actions, and rewards, with each decision being based on the current state and the probabilities of transitioning to future states.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/HC6SPB5J?page=7&annotation=ETLL28VZ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/garrido-merchanComputationalEthicsMorality2023/image-8-x125-y382.png]]



it could also be reasonable to assume that the description of the world as understood by agents is not complete but only partial and is adapted while they interact with it via their actions. A schematic description of this is shown in Figure 3” Yellow Highlight [Page 8](zotero://open-pdf/library/items/HC6SPB5J?page=8&annotation=9TX2YWQJ)



given the specifications of an ethical problem, it is always possible to define an ethical (that is, the optimal given the reward) vs. an unethical one. This finding would explain relativism (individual or cultural) just by differences in the reward function (that is, whether some things are more valued than others by different individuals or in different cultures).” Yellow Highlight [Page 8](zotero://open-pdf/library/items/HC6SPB5J?page=8&annotation=ANCFCQ9E)



This also means that, if we formalize survival as the reward function (which is consistent with the point of view of evolutionary ethics), it would be possible to derive some objective policy as optimal for the situation. This becomes even clear when multilevel selection is considered and the uppermost ’humanity’ level is taken into account: there is an objective policy that maximizes the possibilities of human survival.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/HC6SPB5J?page=8&annotation=5AMJUSA7)



Bounded rewards help ensure convergence of learning algorithms and stability in long-term value estimation. The adaptive learning rate βn is a dynamically updated parameter that controls the step size in the learning process” Yellow Highlight [Page 9](zotero://open-pdf/library/items/HC6SPB5J?page=9&annotation=UQ43S7GI)



Theorem 2. Assume |A| < ∞ and |S| < ∞. Let ni(s, a) be the index of the i-th time that the action a is used in state s. Let R < ∞ be a constant. Given bounded rewards |r| ≤ R, learning rate 0 ≤ βn < 1 and: X∞ i=1 βni(s,a) = ∞,X∞ i=1 (βni(s,a))2 < ∞, ∀s, a, (1) then Q(n)(s, a) → Q∗(s, a) as n → ∞, ∀s, a with probability 1.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/HC6SPB5J?page=9&annotation=MYUI6G89)



This theorem was shown on Watkins and Dayan (1992) [24]. It basically says that a series of conditions exist that guarantee the convergence to a true value function Q⋆ that would be the optimal global objective ethic in the MDP that represents our world. In particular, this optimal policy does not only exist but is also feasible and learnable by analyzing the gradient of the objective function J(θ).” Yellow Highlight [Page 9](zotero://open-pdf/library/items/HC6SPB5J?page=9&annotation=92K9V7YR)



This means that the optimal policy for human beings (which we will call objective ethic) exists and can be practiced via the action space that has been defined.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/HC6SPB5J?page=9&annotation=GCMEN9NS)




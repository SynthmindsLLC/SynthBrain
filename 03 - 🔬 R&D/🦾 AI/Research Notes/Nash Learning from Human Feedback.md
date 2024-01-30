---
Publish Year: "2023"
Authors: Rémi Munos, Michal Valko, Daniele Calandriello, Mohammad Gheshlaghi Azar, Mark Rowland, Zhaohan Daniel Guo, Yunhao Tang, Matthieu Geist, Thomas Mesnard, Andrea Michi, Marco Selvi, Sertan Girgin, Nikola Momchev, Olivier Bachem, Daniel J. Mankowitz, Doina Precup, Bilal Piot
URL: http://arxiv.org/abs/2312.00886
Zotero Link: zotero://select/library/items/LETBNQ4C
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Machine-Learning"
  - "#Computer-Science---Multiagent-Systems"
  - "#Statistics---Machine-Learning"
  - "#Computer-Science---Computer-Science-and-Game-Theory"
  - alignment
  - nashequilibrium
  - gametheory
Published: 2024-05-21
---
# Summary
### Purpose

The paper introduces a new framework called Nash Learning from Human Feedback (NLHF), which is a radical departure from the usual Reinforcement Learning from Human Feedback (RLHF). Instead of learning a reward model, NLHF focuses on learning a preference model and aims to compute the Nash equilibrium based on this model.

### Methods

The researchers used a preference model that takes two responses and produces a preference score, indicating which response is preferred in a given context. They then used a deep reinforcement learning algorithm to approximate the Nash equilibrium of a two-player game where actions are responses and payoffs are determined by the preference model.

### Key Findings

The key findings are that the Nash equilibrium can better align with the diversity of human preferences compared to traditional RLHF. The Nash-MD algorithm introduced in the paper converges to the Nash equilibrium without the need to store past policies, which is a big deal for large language models (LLMs) with their hefty memory requirements.

### Discussion

The paper discusses how the Nash equilibrium represents a policy that consistently produces responses preferred by the preference model over any alternative policy. This approach has the potential to capture a wider range of human preferences and is policy-independent.

### Critiques

While the paper presents a novel approach, it's still early days, and the real-world effectiveness of NLHF compared to traditional RLHF remains to be seen. The experiments conducted are more proof of concept than a definitive statement of superiority.

### Tags

- [#Computer-Science---Artificial-Intelligence](app://obsidian.md/index.html#Computer-Science---Artificial-Intelligence)
- [#Computer-Science---Machine-Learning](app://obsidian.md/index.html#Computer-Science---Machine-Learning)
- [#Computer-Science---Multiagent-Systems](app://obsidian.md/index.html#Computer-Science---Multiagent-Systems)
- [#Statistics---Machine-Learning](app://obsidian.md/index.html#Statistics---Machine-Learning)
- [#Computer-Science---Computer-Science-and-Game-Theory](app://obsidian.md/index.html#Computer-Science---Computer-Science-and-Game-Theory)
- [#alignment](app://obsidian.md/index.html#alignment)
- [#nashequilibrium](app://obsidian.md/index.html#nashequilibrium)
- [#gametheory](app://obsidian.md/index.html#gametheory)

# Annotations
A prevailing approach within RLHF involves the initial step of constructing a reward model based on pairwise human preferences, frequently employing the Bradley-Terry model (BT; Bradley and Terry, 1952). This reward model assigns an individual score to each generation of the language model conditioned on a given prompt, akin to how the Elo (1978) ranking system assigns scores to chess players to estimate their relative strengths.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/9Q9FVYNN?page=1&annotation=R63RSWYE)



the Elo model has its limitations, primarily coming from its inability to accommodate the full spectrum of possible preferences. For example, Bertrand et al. (2023) show the limitations of the Elo model by illustrating where Elo score alone cannot predict the right preferences, even in transitive situations.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/9Q9FVYNN?page=1&annotation=VEQX5XXT)



Nash learning from human feedback (NLHF). In this framework, we depart from the conventional approach of learning a reward model and instead focus on learning a preference model and define our objective to compute the Nash equilibrium of this preference model.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=9TJM7KVK)



The preference model takes two responses, denoted as 𝑦 and 𝑦′ (possibly conditioned on a prompt 𝑥), as input and produces a preference score P ( 𝑦 ≻ 𝑦′|𝑥), indicating the preference of response 𝑦 over response 𝑦′ given the context 𝑥.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=8GLLIG5X)



“Given 𝑥, which answer do you prefer, answer 1: 𝑦 or answer 2: 𝑦′?”.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=KFAB8NEP)



a preference model does not require the assumption of the Bradley-Terry model, and thus has the potential to capture a more diverse range of human preferences.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=JYJU4XN9)



in contrast to the traditional RLHF setting where the reward model depends on the distribution (and thus the policy) of responses used to collect human data, a preference model (having as input the two responses to be compared) remains essentially invariant to the specific policy employed to generate these responses.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=V4M9QRJY)



equilibrium represents a policy that consistently produces responses preferred, as determined by the preference model, over responses generated by any alternative policy.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=ARVKWWGU)



These three key properties of our approach, namely, the ability of the preference model to encompass a wider spectrum of human preferences, its policy-independence, and the potential for the Nash equilibrium to provide a better alignment with the diversity of human preferences, mark a substantial departure from the conventional RLHF framework.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=K59HIIVZ)



approximate the Nash equilibrium of the two-player game in which actions are responses, and payoffs are specified by the preference model, we employ a deep reinforcement learning algorithm. Given a prompt 𝑥, we generate two responses, denoted as 𝑦 and 𝑦′. The first response, 𝑦, is generated under the current policy 𝜋𝜃 that we are in the process of optimizing. In contrast, the second response, 𝑦′, is produced by an alternative policy 𝜋′, which we implement in two different versions: Nash-MD and Nash-EMA” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=57ZKPSKY)



Nash-MD defines the alternative policy 𝜋′ as a geometric mixture between the initial and the current policies (motivated by mirror descent), whereas Nash-EMA implements a first-order approximation of an exponential moving average (EMA) mixture of past policies.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=7UHAJC8Q)



Then, the preference model computes P ( 𝑦 ≻ 𝑦′|𝑥), and this preference signal serves as a reward for optimizing our policy 𝜋𝜃 using a (regularized) policy gradient algorithm, as outlined by Geist et al. (2019).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9Q9FVYNN?page=2&annotation=57ZKQEZR)



This algorithm, founded on the principles of mirror descent (MD) possesses two important properties. First, it converges to the Nash equilibrium, with the final iteration reaching this equilibrium. This differs from conventional regret-minimization-based algorithms, where it is typically the mixture of past policies that converges, necessitating the storage of past policies.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9Q9FVYNN?page=3&annotation=UXPJQTMI)



Secondly, Nash-MD learns by competing against alternative policies 𝜋′ that represent a (geometric) mixture between the current policy 𝜋𝜃 and the initial policy.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9Q9FVYNN?page=3&annotation=BWCLX6XR)



can be accomplished without the need to retain intermediate policies, a feature of particular significance in the context of LLMs with their substantial memory requirements” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9Q9FVYNN?page=3&annotation=TZH8XVT6)



Our contribution falls into a broader area of preference-based RL, where we directly learn from pairwise human preferences instead of a hand-designed or learned scalar reward” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9Q9FVYNN?page=3&annotation=VVCIW9ZP)



The canonical form of RLHF was proposed in Christiano et al. (2017) and popularized by OpenAI (2022), in which one learns a scalar reward model from the preference feedback, followed by policy optimization against the reward model.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9Q9FVYNN?page=3&annotation=7HC8HFLI)



an advantage of directly optimizing for preferences rather than a learnt scalar reward function is the potential to avoid reward hacking (Amodei et al., 2016), when agents find a way to maximize a reward without performing what was intended.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9Q9FVYNN?page=3&annotation=WNYDJHLU)



we focus on the trajectory feedback where the experts provide feedback by selecting the preferred one of the two proposed trajectories.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9Q9FVYNN?page=3&annotation=QRX5A7MX)



Preference-based RL is also explored in dueling RL (Novoseller et al., 2020; Pacchiano et al., 2023), which generalizes the well-studied dueling bandits problem.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9Q9FVYNN?page=3&annotation=ELVA6CPS)



A number of recent works has attempted to optimize for preference feedback without learning a reward function. For example, Direct Preference Optimization (DPO; Rafailov et al., 2023) optimizes the policy through a loss function defined via the Bradley-Terry reward model.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/9Q9FVYNN?page=4&annotation=8JETVTTS)



SLiC-HF (Zhao et al., 2023) modifies the classical RLHF training loss by calibrating a ranking loss which contrasts a positive and a negative sequence.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/9Q9FVYNN?page=4&annotation=XCQ68AMW)



Identity Policy Optimization (IPO; Azar et al., 2023) proposed to directly optimize the pairwise human preference with offline preference data.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/9Q9FVYNN?page=4&annotation=S8EMLEME)



This is therefore a two-player, symmetric, constant-sum game, and it follows that when both players use a policy 𝜋∗ solving Equation (1), this is a Nash equilibrium for this game, by the minimax theorem (von Neumann, 1928).” Yellow Highlight [Page 4](zotero://open-pdf/library/items/9Q9FVYNN?page=4&annotation=FWJTQR3C)



even when the preference model is perfectly captured by the Bradley-Terry model, optimization of the reward/Elo score may still disagree with any reasonable notion of preference optimization.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/9Q9FVYNN?page=5&annotation=7T6NQUD7)



the Nash solution of the preference model (i.e., the NLHF solution), assigning close to uniform probability to these 3 actions (one being preferred by each category of humans) is more aligned with the diversity of human preferences than the optimum of the reward model (i.e., the RLHF solution), which would deterministically select a single action.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/9Q9FVYNN?page=6&annotation=L6WAW448)



nother difference between reward and preference models is that a reward model depends on the distribution over responses it has been trained on, whereas a preference model essentially does not.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/9Q9FVYNN?page=6&annotation=ACLQHZXU)



since the preference model takes two responses as input, the output does not depend directly on the distribution these responses have been sampled from. The preference model is simply learnt by supervised learning, where for each 𝑥, 𝑦, 𝑦′, the preference model P ( 𝑦 ≻ 𝑦′|𝑥) is regressed to the human preference” Yellow Highlight [Page 6](zotero://open-pdf/library/items/9Q9FVYNN?page=6&annotation=DKAGJ3XZ)



in the NLHF approach, the preference model can be preserved and further enriched through the introduction of novel data, thereby offering a more seamless and efficient adaptation process.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/9Q9FVYNN?page=6&annotation=8PGZRAEA)



we incorporate a penalty mechanism into our preference model, employing KL-regularization to quantify the divergence between the policy under consideration and a designated reference policy denoted” Yellow Highlight [Page 7](zotero://open-pdf/library/items/9Q9FVYNN?page=7&annotation=I4GINCYC)



ictitious play (FP; Brown, 1951; Fudenberg and Levine, 1998; Heinrich et al., 2015; Robinson, 1951) consists in playing, at every iteration, each player’s best response against the uniform mixture of the opponent’s past strategies.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/9Q9FVYNN?page=7&annotation=DDCP2MZL)



Online convex optimization: In the context of solving convex-concave constant-sum games, we rely on online convex optimization where each player minimizes its own convex loss.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/9Q9FVYNN?page=7&annotation=G4B394K3)



Regret minimization has been extensively considered in games since the average strategy of self-playing no-regret algorithms converges to a Nash equilibrium” Yellow Highlight [Page 7](zotero://open-pdf/library/items/9Q9FVYNN?page=7&annotation=9XSMIMSK)



Counterfactual regret minimization (CFR) has been considered in the setting of imperfect information games in” Yellow Highlight [Page 8](zotero://open-pdf/library/items/9Q9FVYNN?page=8&annotation=E5UJUSB6)



Extragradient or optimistic mirror descent methods have been proven to converge to a Nash equilibrium (Korpelevich, 1976; Mertikopoulos et al., 2019) with possibly an exponential rate in unconstrained spaces” Yellow Highlight [Page 8](zotero://open-pdf/library/items/9Q9FVYNN?page=8&annotation=WU4SMG3L)



most closely related extragradient method in this domain is optimistic multiplicative-weights-update (OMWU; Daskalakis and Panageas, 2019) which provides convergence guarantees to the Nash equilibrium of the last iterate.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/9Q9FVYNN?page=8&annotation=ZH7EGG8Z)



the Frank-Wolfe method to compute Nash equilibria in normal-form games (Gidel et al., 2016), although convergence is attained at the same rate as for fictitious play.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/9Q9FVYNN?page=8&annotation=CBGZJLZH)



algorithm introduced by Munos et al. (2020) for imperfect information games consists in each player doing a step of mirror ascent against an improved opponent (MAIO) for which exponential convergence of the last-iterate was proven” Yellow Highlight [Page 8](zotero://open-pdf/library/items/9Q9FVYNN?page=8&annotation=S9QQ7MNM)



regularized Nash dynamics (R-NaD), introduced friction to the dynamics by considering a KL-regularized objective showed a last-iterate convergence in a continuous-time dynamics setting.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/9Q9FVYNN?page=8&annotation=E77B9HH7)



algorithm, called Nash-MD, which is a novel variant of mirror descent (Bubeck, 2015; Lattimore and Szepesvári, 2020; Nemirovski and Yudin, 1983) that makes use of a specific regularized policy 𝜋 𝜇 𝑡 which is a geometric mixture between the current policy 𝜋𝑡 and the reference policy 𝜇.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/9Q9FVYNN?page=8&annotation=ICGWGAMH)



We play against a single (geometric) mixture 𝜋 𝜇 𝑡 between the current policy 𝜋𝑡 and the reference policy 𝜇. This is important in situations, such as in LLMs, where storing and generating sample from several policies is costly.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/9Q9FVYNN?page=9&annotation=H5NYPDJY)



The second important property of Nash-MD is that we have convergence of the last-iterate (i.e., the current policy 𝜋𝑡 converges to 𝜋∗ 𝜏) and not only convergence on average (as is typically the case of fictitious play and usual regret minimization algorithms like CFR and OMD). This feature is particularly important in the context of LLMs as well due to the substantial memory resources that would be otherwise needed to store a mixture policy like  ̄ 𝜋𝑡 .” Yellow Highlight [Page 9](zotero://open-pdf/library/items/9Q9FVYNN?page=9&annotation=ICMG93PF)



n general the analysis of constant-sum concaveconvex games can be performed in the framework of online convex optimization where the goal is to find a sequence of solutions 𝜋𝑡 that minimizes the sum of a sequence of convex loss functions” Yellow Highlight [Page 9](zotero://open-pdf/library/items/9Q9FVYNN?page=9&annotation=PKUWUJZK)



OMD optimizes the preference 𝜋 ↦→ P (𝜋 ≻ 𝜋𝑡) against the current policy 𝜋𝑡 whereas Nash-MD optimizes the preference 𝜋 ↦→ P (𝜋 ≻ 𝜋 𝜇 𝑡 ) against the regularized policy 𝜋 𝜇 𝑡.” Yellow Highlight [Page 10](zotero://open-pdf/library/items/9Q9FVYNN?page=10&annotation=RV33Y4ZU)



In LLMs it is usually the case that tokens are generated one at a time in an autoregressive manner.” Yellow Highlight [Page 10](zotero://open-pdf/library/items/9Q9FVYNN?page=10&annotation=9WIY3QSJ)



it is not easy to generate a sequence 𝑦 from this distribution by sampling one token 𝑦𝑛 at a time.” Yellow Highlight [Page 11](zotero://open-pdf/library/items/9Q9FVYNN?page=11&annotation=6JYSIVL3)



we would like to proceed by generating a token at a time.” Yellow Highlight [Page 11](zotero://open-pdf/library/items/9Q9FVYNN?page=11&annotation=RTGY3RXR)



We call this corresponding product of marginal (geometric) mixtures over individual tokens the one-step-at-a-time regularized policy” Yellow Highlight [Page 11](zotero://open-pdf/library/items/9Q9FVYNN?page=11&annotation=DNMF7T7C)



Computing the Nash equilibrium using regularized policy gradient Our general algorithm for computing the Nash equilibrium of the preference model consists in repeating these steps: • We randomly select a prompt 𝑥 ∼ 𝜌. • We generate two responses 𝑦 and 𝑦′ (in an autoregressive fashion in the case of LLMs): – the first one 𝑦 ∼ 𝜋𝜃(·|𝑥) by following the current policy 𝜋𝜃 that is being optimized; – the second one 𝑦′ ∼ 𝜋′ (·|𝑥) by following an alternative policy 𝜋′. The choice of the alternative policy 𝜋′ that we use for the second generated sample 𝑦′ depends on the specific algorithm we consider (the description of which is given in the next subsection). • We update the parameter 𝜃 of the policy 𝜋𝜃 in the direction of the gradient ∇𝜃P𝜏(𝜋𝜃 ≻ 𝜋′) of the regularized preference model P𝜏. We consider two cases, depending on whether a preference model is learnt or not.” Yellow Highlight [Page 11](zotero://open-pdf/library/items/9Q9FVYNN?page=11&annotation=T5ZAEZ8W)



P-model-free approach.” Yellow Highlight [Page 12](zotero://open-pdf/library/items/9Q9FVYNN?page=12&annotation=IU8UPEII)



This estimate does not require to learn a preference model first and is thus not affected by possible bias coming from an approximate model. Implementation-wise it requires having access to humans preference immediately after having generated the responses 𝑦 and 𝑦′.” Yellow Highlight [Page 12](zotero://open-pdf/library/items/9Q9FVYNN?page=12&annotation=D3Q5QSBM)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/munosNashLearningHuman2023/image-15-x50-y145.png]]



The primary objective of these experiments is to provide a proof of concept for the NLHF approach introduced in this paper, rather than striving for state-of-the-art performance in text summarization.” Yellow Highlight [Page 16](zotero://open-pdf/library/items/9Q9FVYNN?page=16&annotation=KGDAVJW6)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/munosNashLearningHuman2023/image-17-x49-y442.png]]



While the ideal approach for evaluating our models would involve soliciting human preferences between summaries generated by different models, we resort to a proxy method using the highly capable LLM, PaLM 2 Large” Yellow Highlight [Page 17](zotero://open-pdf/library/items/9Q9FVYNN?page=17&annotation=2WEMAA3T)



RLHF baseline that we have built is a very strong baseline. It beats SFT with a win rate of 99% marking the highest win rate observed against SFT among all models when using the PaLM 2 preference model P∗” Yellow Highlight [Page 18](zotero://open-pdf/library/items/9Q9FVYNN?page=18&annotation=6RVB4ZPC)



Best-response against self-play (BR) does not exhibit strong performance.” Yellow Highlight [Page 18](zotero://open-pdf/library/items/9Q9FVYNN?page=18&annotation=SSDKJR7E)



BR performs poorly against RLHF and all other Nash-based approaches. This suggests the possibility of ’preference hacking,’ where BR may be overly adapting to the preference model by overfitting to the specific SFT policy.” Yellow Highlight [Page 18](zotero://open-pdf/library/items/9Q9FVYNN?page=18&annotation=65GMBLM7)



Self-play (SP) exhibits strong overall performance, with notable exceptions in the P∗ evaluation against RLHF and the Nash-MD models (for 𝛽 ≤ 0.5)” Yellow Highlight [Page 18](zotero://open-pdf/library/items/9Q9FVYNN?page=18&annotation=268S589R)



enhancing one’s policy through self-play could be a promising avenue for improving the initial model. However, it’s essential to acknowledge that self-play does not guarantee the attainment of a Nash equilibrium” Yellow Highlight [Page 18](zotero://open-pdf/library/items/9Q9FVYNN?page=18&annotation=6BNHFQQC)



Nash-MD models, especially those with 𝛽 ≤ 0.5, exhibit very strong performance.” Yellow Highlight [Page 18](zotero://open-pdf/library/items/9Q9FVYNN?page=18&annotation=YG3USNAF)



Nash-MD with 𝛽 = 0.125 (highlighted in bold as ’MD1’) emerges as the top-performing model, surpassing all others in both the training preference model P𝜏 and the evaluation model P∗.” Yellow Highlight [Page 18](zotero://open-pdf/library/items/9Q9FVYNN?page=18&annotation=EP69YXTR)



All Nash-EMA models, including EMA1 and EMA2 (representing the last iterate) as well as EMA1* and EMA2* (representing the average policy), are outperformed by Nash-MD” Yellow Highlight [Page 18](zotero://open-pdf/library/items/9Q9FVYNN?page=18&annotation=V35ICZ6J)



NLHF emerges as an interesting and promising alternative to RLHF, offering a fresh perspective on aligning models with human preferences.” Yellow Highlight [Page 19](zotero://open-pdf/library/items/9Q9FVYNN?page=19&annotation=JW53IEZ9)



Once a preference model is established, the concept of the Nash equilibrium naturally arises as a compelling solution concept. Nash-MD, an algorithm that optimizes policies by playing against a geometric mixture of the current policy and the initial policy, has been introduced. We have established its last-iterate convergence to the Nash equilibrium.” Yellow Highlight [Page 19](zotero://open-pdf/library/items/9Q9FVYNN?page=19&annotation=SDQRP37C)



The choice of the mixture parameter in Nash-MD entails an interesting trade-off. A parameter value of 0 corresponds to self-play, while a value of 1 represents best-response against SFT. Notably, intermediate values within the range of 0.125 to 0.375 consistently outperform both self-play and best-response, highlighting the advantages of playing against a mixture of policies as opposed to a pure policy.” Yellow Highlight [Page 19](zotero://open-pdf/library/items/9Q9FVYNN?page=19&annotation=4VM5CLUF)




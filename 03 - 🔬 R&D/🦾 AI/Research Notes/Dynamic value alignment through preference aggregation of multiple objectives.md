---
Publish Year: "2023"
Authors: Marcin Korecki, Damian Dailisan, Cesare Carissimo
URL: http://arxiv.org/abs/2310.05871
Zotero Link: zotero://select/library/items/NV5PCTWQ
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Machine-Learning"
  - "#Electrical-Engineering-and-Systems-Science---Systems-and-Control"
Published:
---
# Summary
## Purpose

## Methods

## Key Findings

## Discussion

## Critiques

# Annotations
Motivating examples of VA often consider the long-term and potentially existential threats posed by powerful, superintelligent AI agents with misaligned values [Russell, 2022a]” Yellow Highlight [Page 1](zotero://open-pdf/library/items/MXT2VYLE?page=1&annotation=IJWY894N)



Not less pertinent are the short-term threats of more mundane, highly specialized AI systems, employed in particular in control settings, becoming misaligned. A prominent case where a potential misalignment is particularly dangerous is given by systems where humans voluntarily cede control of a system to algorithms.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/MXT2VYLE?page=1&annotation=MQ9DPNJM)



In many cases, it is clear that the values held by humans are varied to the extent of even being contradictory [Awad et al., 2018]” Yellow Highlight [Page 1](zotero://open-pdf/library/items/MXT2VYLE?page=1&annotation=WX4WNTF3)



Among areas that have produced methods and results conducive to such a design are social choice theory, which allows one to gauge and aggregate group preferences, and multi-objective optimization, allowing for a simultaneous pursuit of multiple values” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MXT2VYLE?page=2&annotation=CC9VZD68)



Consider an intersection with two intersecting approaches as shown in Figure 1. A simple Reinforcement Learning (RL) agent controls the access to the intersection. The agent can switch between two actions — giving green to the North–South approach and red to the West–East approach or, conversely, green to the West–East and red to the North–South. Assume now that the system’s designers have chosen to make it control traffic in such a way that it becomes as environmentally sustainable as possible. This can be achieved by setting the reward of the agent to e.g.  negative of some measure of emissions or a proxy of it, such as the negative of the number of stops (vehicles emit most emissions when accelerating from complete stops [Rakha and Ding, 2003]). The agent is then trained with this reward and reaches a solution. Namely, it only ever chooses one action, always keeping the red light for the North–South approach and green for the West–East. Indeed, the system has successfully found a global optimum — the emissions, or the proxy of the number of stops, have been minimized. The vehicles on the West–East approach never stop, while the vehicles on the North–South approach stop once, and so the emissions are kept as low as possible (we assume it is impossible to keep all vehicles moving, which is the case if their relative number on each approach is high enough). We are then left with the effects of what could be referred to as "reward hacking" [Skalse et al., 2022] by the RL agent.  While the reward selected by the designers has been optimized, what emerges is a probably unwanted and perfectly non-egalitarian solution2. This sort of result has been commonly reported in the context of many social systems, where the maximization of social welfare leads to inequality (e.g. in Roughgarden [2002])” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MXT2VYLE?page=2&annotation=96B5ERD3)



a certain notion of multi-objectivity can be an asset in avoiding "reward hacking" and the resultant misalignment.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MXT2VYLE?page=2&annotation=E7ZKD747)



We show how a multi-objective perspective can be leveraged to avoid reward hacking and, at the same time, give more control to the users of the system rather than its designers. We believe that our approach, which explicitly states the social context in which the proposed system exists and takes into account the potential negative consequences of AI systems, is highly relevant with respect to the perceived lack of such considerations in most recent publications [Birhane et al., 2022]” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MXT2VYLE?page=3&annotation=Z42D6CC7)



work builds directly on Multiple-Principal Assistant Games [Fickinger et al., 2020a], which consider the theoretical case of an agent acting on behalf of N humans with differing payoffs.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MXT2VYLE?page=3&annotation=5KPSP8AM)



we believe that it is valuable to also consider the problems of VA using more mundane, already existing AI systems (e.g. recommender systems [Stray et al., 2020]). Many researchers support this position, highlighting the lack of substantial work on real-world examples of systems that might suffer from misalignment [Fickinger et al., 2020a, Hadfield-Menell et al., 2017b].” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MXT2VYLE?page=3&annotation=R6XA3R9D)



Useful impossibility and uncertainty theorems have also been worked out based on work done by ethicists [Eckersley, 2019].” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MXT2VYLE?page=3&annotation=WKLNIDBV)



Inverse Reinforcement Learning (IRL): One of the primary methodologies employed for VA is IRL, where the RL agent learns the reward function directly from demonstrations rather than being programmed with it explicitly [Ng et al., 2000]. T” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MXT2VYLE?page=3&annotation=T8JAJW2G)



explicitly defining the reward function might be challenging but there might exist experts who are able to demonstrate optimal behavior [Abbeel and Ng, 2004]” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MXT2VYLE?page=3&annotation=76KL5232)



Assistance games have been used as a model for the study of alignment problems in much of the IRL literature [Fickinger et al., 2020a, Hadfield-Menell et al., 2016, 2017a,b, Gleave et al., 2022]. The setting often involves a robot learning from a single human demonstrator.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MXT2VYLE?page=3&annotation=GFM7NI5P)



Preference-Based Reinforcement Learning (PbRL)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MXT2VYLE?page=3&annotation=UCLZRRQ8)



leverages the preferences (between states, actions, or trajectories) of users” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MXT2VYLE?page=3&annotation=UTWEN7GP)



What is being learned is a policy consistent with the revealed preferences.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=REP6UEZY)



The main issue in PbRL is that the preference landscape is fixed during training (the model learns a given preference landscape), thus limiting the potential for adaptation to novelty in the preference landscapes, which we consider to be a key interest for properly aligned systems.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=TN6R8YEV)



Multi-Objective Reinforcement Learning (MORL): Our work deals with systems whose users might exhibit a variety of potentially contradictory preferences.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=RIDAMKQC)



Algorithms for arriving at a common Pareto optimal policy usually rely on forms of communication between agents [Mariano and Morales, 2000a,b]” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=BXATH9YW)



The main issue of MORL is defining how to combine diverse objectives based on their relative importance. This can be done a priori, a posteriori or be learned during training [Hayes et al., 2022]. In an a priori case, the users’ preferences need to be specified and fixed, which does not work for our problem setting. Similarly, if the preferences are learned, the model might not be able to accommodate a significant shift in the preference landscape. Thus, in our work, we follow the a posteriori approach, where a set of models is trained and the users are able to select between the different models’ actions in deployment.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=ZUV7IECX)



Social Choice Theory: The study of aggregating multiple preferences has been consistently identified as a key element relevant to value alignment. The modern history of this field can be traced back to the work Von Neumann and Morgenstern [1947] who applied game theory and other tools to modeling human decision-making” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=FEBX888I)



Some of the works mentioned in the previous sections have explicitly investigated the VA problem through the lens of social choice impossibility theorems (e.g. Gibbard’s theorem)” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=8CI8MCEI)



Our work follows this direction by employing a voting layer directly in the decision-making process of an RL agent.  Based on the insights discussed by Baum [2020], our design includes an up-front, explicit way of identifying and aggregating potentially contrary preferences rather than off-loading that process to the RL agent (to let it figure it out so to speak)” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=9AEZNITQ)



Our proposed approach has three main components: the models of different objectives, a method of vote aggregation, and an integration layer” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=RJVSJS6L)



train a separate Deep Q-Network (DQN) for each of our objectives.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MXT2VYLE?page=4&annotation=8E7ZMP54)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/koreckiDynamicValueAlignment2023/image-5-x65-y465.png]]



We want to allow the users of our system to be able to reveal their preferences and affect the system according to them.  Therefore, we need to specify the type of preferences such that they are meaningful to the system” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MXT2VYLE?page=5&annotation=HLK7M8VP)



when a user selects a given reward as the preferred one, they do so under the assumption that this reward will be applied to the entire system and not preferentially to them alone” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MXT2VYLE?page=5&annotation=95PXBGS4)



Thus, the users remain under the veil of ignorance [Harsanyi, 1953] as the exact effects of their chosen objective being pursued by the controller are not known to them.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MXT2VYLE?page=5&annotation=F9U5HP36)



At the decision time, only users that are allowed to vote at the given moment are polled—these are the users on the incoming lanes of the intersection” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MXT2VYLE?page=5&annotation=RHZ5M37H)



Thus, the voting population at each step is not equal to the entire population of the system. Even though the preferences of each user are fixed, the relative preferences of the voting population change as the population changes” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MXT2VYLE?page=5&annotation=LX3K35MZ)



The key element of our approach is the integration layer, which allows for the integration of the DQNs results with the preferences of the users.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/MXT2VYLE?page=6&annotation=445GY28L)



Thus, the system generally follows the preferences unless the relative difference between the expected rewards within one objective is large and within the other is small. Conversely, if the preference is weak (wA ≈ wB) the system will prioritize the objective that stands to lose more from not being followed.  This approach then allows accounting for user preferences, but at the same time tends to avoid taking very bad actions on one of the objectives.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/MXT2VYLE?page=6&annotation=5YAW6TD9)



When choosing to switch or not, the agent polls the vehicles on the upstream approach (in other words only vehicles that will be directly affected by this action are allowed to vote, the vehicles on the downstream do not vote).” Yellow Highlight [Page 6](zotero://open-pdf/library/items/MXT2VYLE?page=6&annotation=93Z8BPZY)



A common problem that could affect the system is strategic voting, whereby users misrepresent their preferences to exploit the aggregation method and increase the chances of their objective being chosen [Gibbard, 1973]” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MXT2VYLE?page=7&annotation=XSYEFSGK)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/koreckiDynamicValueAlignment2023/image-8-x61-y407.png]]



We note that in our experiments optimizing the linear combination of the two objectives actually leads the system into the undesired optimum of the close to zero number of stops but very high wait times. This showcases the potential effects of misspecifing the weights. Moreover, if an additional objective is added to the model, it would require retraining the model from scratch, and once again searching and specifying the weights for the objectives. Our approach avoids these challenges, although it requires training additional single-objective models.  Overall, we believe that our approach is a more scalable alternative to the method outlined above.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/MXT2VYLE?page=9&annotation=UTV26UQT)



Our approach has a unique requirement for an environment: the environment must have multiple players (with their own logic) that interact with a system that is controlled and optimized by a controller” Yellow Highlight [Page 10](zotero://open-pdf/library/items/MXT2VYLE?page=10&annotation=Y2WRKARZ)



Based on our results, we can confirm that our proposed method avoids the "reward hacked" solution exhibited by the Stops DQN. Thus, our method is able to avoid misalignment in our setting, by following a more nuanced, multi-objective perspective” Yellow Highlight [Page 10](zotero://open-pdf/library/items/MXT2VYLE?page=10&annotation=ISYCAUBV)



We also note that the proportional voting system appears to work better in our setting than majority voting.  This appears intuitive as the proportional method mitigates issues such as "tyranny of the majority" and "wasted votes",” Yellow Highlight [Page 10](zotero://open-pdf/library/items/MXT2VYLE?page=10&annotation=R4IN8KBM)




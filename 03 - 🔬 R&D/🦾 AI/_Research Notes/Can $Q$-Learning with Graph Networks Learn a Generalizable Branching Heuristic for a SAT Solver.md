---
Publish Year: '2020'
Authors: "Vitaly Kurin, Saad Godil, Shimon Whiteson, Bryan Catanzaro"
URL: "http://arxiv.org/abs/1909.11830"
Zotero Link: "zotero://select/library/items/AVP4R2MI"
tags:
  - "#Computer-Science---Artificial-Intelligence, #Computer-Science---Machine-Learning"
Published:
---
# Summary
## Purpose
- The research was initiated to address the challenge of improving branching heuristics in SAT solvers, which is a significant issue in the field of [Computer Science - Artificial Intelligence]. The purpose of the study was to investigate how machine learning, specifically reinforcement learning, can be used to enhance an existing branching heuristic without relying on domain expertise.

## Methods
- Formulated the reinforcement learning problem as a Markov decision process (MDP) with a discount factor to weigh immediate versus future rewards.
- Utilized Graph Neural Networks (GNNs) to approximate the Q-function, allowing for a dynamic state-action space and invariance to permutation and variable relabeling.
- Developed Graph-Q-SAT, a branching heuristic trained with value-based reinforcement learning based on deep Q-networks.
- Represented SAT problems as graphs to encode variables and clauses, simplifying state representation without the need for feature engineering.
- Capped the maximum number of actions per episode to prevent the agent from getting stuck and to expose it to more episodes.

## Key Findings
- Graph-Q-SAT outperforms the Variable State Independent Decaying Sum (VSIDS) heuristic, reducing the number of iterations required to solve SAT problems by 2-3 times.
- The method generalizes to problems five times larger than those it was trained on, showing a nearly 4X improvement in iterations for larger datasets.
- Graph-Q-SAT generalizes across different problem types, from satisfiable (SAT) to unsatisfiable instances (unSAT).
- GNNs learn graph local properties, indicating how neighboring entities' features globally impact Q-values, which suggests potential for transfer across different task families.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on the field of [Artificial Intelligence and SAT solving]. It suggests that the use of Graph-Q-SAT could lead to more efficient SAT solvers by improving the branching heuristic with machine learning techniques. The ability of Graph-Q-SAT to generalize to larger and different types of problems indicates its potential for practical applications and its contribution to the field.

## Critiques
Upon evaluating the research, some critiques include:
    - The performance drop when changing the task family, although expected, needs further investigation to fully understand the method's ability to transfer across task families.
    - The study may need to address the scalability of the approach to even larger and more complex SAT problems to assess its practicality in real-world applications.
    - Further comparison with other state-of-the-art heuristics and reinforcement learning methods could provide a more comprehensive understanding of the method's strengths and weaknesses.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Machine-Learning
- #Reinforcement-Learning
- #Graph-Neural-Networks
- #SAT-Solvers
- #Branching-Heuristics

# Annotations
Boolean satisfiability (SAT) is an important problem” Yellow Highlight [Page 1](zotero://open-pdf/library/items/9I6XSE7K?page=1&annotation=8WCG85IZ)



SAT is known to be NP-complete [22], and most state-of-the-art open-source and commercial solvers rely on multiple heuristics to speed up the exhaustive search, which is otherwise intractable” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=YIVQ3VUB)



investigate how we can use machine learning to improve upon an existing branching heuristic without leveraging domain expertise.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=W8PGNP6T)



We present Graph-Q-SAT, a branching heuristic in a Conflict Driven Clause Learning [40, 21, CDCL] SAT solver trained with value-based reinforcement learning (RL), based on deep Q-networks [30” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=BH7K7KFR)



Graph-Q-SAT uses a graph representation of SAT problems similar to Selsam et al. [39] which provides permutation and variable relabeling invariance. Graph-Q-SAT uses a Graph Neural Network [13, 4, GNN] as a function approximator to provide generalization as well as support for a dynamic state-action space” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=PDRUHA3P)



We demonstrate that Graph-Q-SAT outperforms Variable State Independent Decaying Sum [31, VSIDS], the most frequently used CDCL branching heuristic, reducing the number of iterations required to solve SAT problems by 2-3X.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=L2BB69HQ)



Graph-Q-SAT is trained to examine the structure of the particular problem instance to make better decisions at the beginning of the search, whereas the VSIDS heuristic suffers from poor decisions during the warm-up period.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=Z2CXJJKQ)



Graph-Q-SAT exhibits intriguing properties which might eventually be useful for practical applications. We show that our method generalizes to problems five times larger than those it was trained on.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=AV2AC7NC)



Graph-Q-SAT generalizes across problem types from satisfiable (SAT) to unsatisfiable instances (unSAT)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=52NGPZG5)



A SAT problem involves finding variable assignments such that a propositional logic formula is satisfied or showing that such an assignment does not exist. A propositional formula is a Boolean expression, including Boolean variables, ANDs, ORs and negations.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=75NJ6BU9)



The branching heuristic is responsible for picking the variable and assigning some value to it. VSIDS [31] is one of the most used CDCL branching heuristics. It is a counter-based heuristic that keeps a scalar value for each literal or variable (MiniSat uses the latter)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/9I6XSE7K?page=2&annotation=9ZWH63M9)



We formulate the RL problem as a Markov decision process (MDP).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9I6XSE7K?page=3&annotation=F4W2J8GR)



Discount factor γ ∈ [0, 1) weights preferences for immediate reward relative to future reward. The last element of the tuple ρ is the probability distribution over initial states. In the case of episodic tasks, the state space is split into the set of non-terminal states and the terminal state S+. To solve an MDP means to find an optimal policy, a mapping that outputs an action or distribution over actions given a state and which maximizes the expected discounted return” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9I6XSE7K?page=3&annotation=BV9WPADK)



We need a network architecture which does not assume the input to be of fixed size. Moreover, a Boolean formula should be invariant to the permutation of the clauses, variables and their renaming. To accommodate these requirements and also to take the problem structure into account, we use Graph Neural Networks [13, GNN] to approximate our Q-function” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9I6XSE7K?page=3&annotation=NNEYAWQI)



A GNN is as a set of six functions: update functions φe, φv, φu and aggregation functions ρe→v, ρe→u, ρv→u. The information propagates between vertices along graph edges. Update functions compute new entity annotations. Aggregation functions enable GNN to process graphs of arbitrary topology, compressing multiple entities features into vectors of fixed size. Summation, averaging, taking max or min are popular choices of aggregation functions.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/9I6XSE7K?page=3&annotation=6H7RNCV7)



We represent a SAT problem as a graph similar to Selsam et al. [39]. We make it more compact, using vertices to denote variables instead of literals. We use vertices to encode clauses as well. As Figure 1 shows, our state representation is simple and does not require feature engineering. An edge (xi, ci) means that a clause ci contains literal xi. If a literal contains a negation, a corresponding edge has a [1, 0] label and [0, 1] otherwise. GNNs process directed graphs, so we create two directed edges with the same labels: from a variable to a clause and vice-versa. Vertex features are two-dimensional one-hot vectors, denoting either a variable or a clause. We do not provide any other information to the model. The global attribute input is empty and is only used for message passing.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/9I6XSE7K?page=4&annotation=G9KESCBJ)



Similarly to Bapst et al. [3], our GNN labels variable vertices with Q-values. Each variable vertex has two actions: set the variable to true or false” Yellow Highlight [Page 4](zotero://open-pdf/library/items/9I6XSE7K?page=4&annotation=74U22YAA)



To expose the agent to more episodes and prevent it from getting stuck, we cap the maximum number of actions per episode similarly to the episode length parameter in gym [6].” Yellow Highlight [Page 4](zotero://open-pdf/library/items/9I6XSE7K?page=4&annotation=7WSPWK4E)



Table 2 shows that Graph-Q-SAT has no difficulty generalizing to larger problems, showing almost 4X improvement in iterations for a dataset 5 times bigger than the training set” Yellow Highlight [Page 6](zotero://open-pdf/library/items/9I6XSE7K?page=6&annotation=B3D5NB7V)



GNNs learn graph local properties, i.e. how neighbouring entities’ features have a global implication on Q-values. It is reasonable to expect a performance drop when changing the task family φ, but the magnitude of the drop gives some indication of the method’s ability to transfer across task families” Yellow Highlight [Page 6](zotero://open-pdf/library/items/9I6XSE7K?page=6&annotation=WWQZS5U3)



![[image-7-x103-y529.png]]




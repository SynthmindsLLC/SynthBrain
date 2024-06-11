---
title: "Thompson Sampling"
description: "A heuristic for choosing actions that address the exploration-exploitation dilemma in the multi-armed bandit problem. It involves choosing the action that maximizes the expected reward with respect to a randomly drawn belief[1]."
type: "concept"
tags:
- "Reinforcement Learning"
- "ExplorationExploitationDilemma"
- "Algorithms"
relationships:
- "#developed_by [[William R. Thompson]]"
- "#used_for [[Online Learning]], [[A/B Testing]], [[Personalized Content Recommendation]]"
- "#applied_in [[Industry Applications]]"
birthdate: "deathdate: founded: start_date: end_date: "
---

## Thompson Sampling

### Definition
Thompson Sampling, named after William R. Thompson, is a heuristic for choosing actions that address the exploration-exploitation dilemma in the multi-armed bandit problem. It involves choosing the action that maximizes the expected reward with respect to a randomly drawn belief[1].

### Mechanism
- The algorithm maintains a probability distribution over the possible actions based on past rewards and actions.
- At each decision point, it samples from this distribution to decide which action to take, effectively balancing between exploring new actions and exploiting known rewarding actions[1][2].

### Bayesian Approach
Thompson Sampling is a Bayesian method, which means it updates the probability distributions of the rewards of actions based on observed data. It uses a prior distribution that is updated as more data is gathered, leading to a posterior distribution that guides the selection of actions[1][2].

### Applications
- **Online Learning**: Thompson Sampling is used in various online learning problems, including A/B testing, adaptive routing, and personalized content recommendation[1].
- **Industry**: Companies like Amazon, Facebook, and Netflix use Thompson Sampling for tasks such as website optimization, video quality optimization, and recommendation systems[2].

### Advantages
- **Efficiency**: It is known for its efficiency and has logarithmic regret, meaning the difference between the expected reward and the best possible reward grows logarithmically with time[2].
- **Practicality**: Thompson Sampling is simple to implement and can adapt to changing environments, making it practical for real-world applications[2][8].

### Conclusion
Thompson Sampling is a powerful algorithm for solving the exploration-exploitation trade-off in reinforcement learning and other decision-making scenarios. Its probabilistic nature and adaptability make it a popular choice in both theoretical studies and practical applications[1][2].

- Important [[wikilinks]]: [[Reinforcement Learning]], [[Multi-Armed Bandit Problem]], [[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Exploration and Exploitation]], [[Bayesian Methods]]

Sources
[1] Thompson sampling - Wikipedia https://en.wikipedia.org/wiki/Thompson_sampling
[2] Multi-Armed Bandit Algorithms: Thompson Sampling https://towardsdatascience.com/multi-armed-bandit-algorithms-thompson-sampling-6d91a88145db
[3] Why is Thompson Sampling considered a part of Reinforcement Learning? https://ai.stackexchange.com/questions/32637/why-is-thompson-sampling-considered-a-part-of-reinforcement-learning
[4] Multi-Agent Thompson Sampling for Bandit Applications with Sparse Neighbourhood Structures - Scientific Reports https://www.nature.com/articles/s41598-020-62939-3
[5] A Tutorial on Thompson Sampling https://web.stanford.edu/~bvr/pubs/TS_Tutorial.pdf
[6] [PDF] Analysis of Thompson Sampling for the Multi-armed Bandit Problem - Proceedings of Machine Learning Research http://proceedings.mlr.press/v23/agrawal12/agrawal12.pdf
[7] Educative Answers - Trusted Answers to Developer Questions https://www.educative.io/answers/what-is-thompson-sampling
[8] What is Thompson sampling? | Autoblocks Glossary https://www.autoblocks.ai/glossary/thompson-sampling
[9] Thompson Sampling https://www.cs.ubc.ca/labs/lci/mlrg/slides/2019_summer_6_thompson_sampling.pdf
[10] What is Thompson Sampling in layman's terms? https://stats.stackexchange.com/questions/187059/what-is-thompson-sampling-in-laymans-terms
[11] Introduction to Thompson Sampling | Reinforcement Learning - GeeksforGeeks https://www.geeksforgeeks.org/introduction-to-thompson-sampling-reinforcement-learning/
[12] Thompson sampling | Engati https://www.engati.com/glossary/thompson-sampling

By Perplexity at https://www.perplexity.ai/search/The-traveling-salesman-wDKECxSlREav4lsL7_Cuag
---
title: "Simulated Annealing (SA)"
description: "Optimization technique inspired by the process of annealing in metallurgy, used to find approximate global optimum in a large search space. Effective for discrete and continuous problems. Key components include Temperature and Cooling Schedule. Widely used in operations research, physical sciences, and computer science."
type: "concept"
tags:
- "Optimization Techniques"
- "Global Optimum"
- "Simulated Annealing"
- "Algorithms"
- "Computational Science"
relationships:
- "#inspired_by [[Annealing in Metallurgy]]"
- "#applied_to [[Traveling Salesman Problem]]"
- "#related_to [[Stochastic Algorithms]]"]]
birthdate: "2024-03-06"
---

Simulated Annealing (SA) is an optimization technique inspired by the process of annealing in metallurgy, a technique involving heating and controlled cooling of a material to increase the size of its crystals and reduce their defects. The method is used to find an approximate global optimum in a large search space and is particularly effective for problems where the search space is discrete (e.g., traveling salesman problem), though it can also be applied to continuous problems.

The algorithm mimics the physical process by starting with a high "temperature" that allows it to explore the search space freely, accepting solutions that are worse than the current solution with a certain probability. This probability decreases as the temperature decreases, making the algorithm more selective about accepting worse solutions over time. The gradual cooling schedule helps to prevent the algorithm from getting stuck in local optima early on and encourages exploration of the search space for potentially better solutions.

Key components of the Simulated Annealing algorithm include:
- **Temperature**: Controls the probability of accepting worse solutions. High temperatures allow more exploration, while low temperatures focus on exploitation around the current solution.
- **Cooling Schedule**: Determines how the temperature is reduced over time. A well-designed cooling schedule is crucial for the algorithm's performance.

Simulated Annealing is widely used in various fields such as operations research, physical sciences, and computer science due to its simplicity and effectiveness in solving complex optimization problems. Despite its stochastic nature, it has been successful in finding good solutions to problems where other optimization techniques fail to perform well.

- Important [[wikilinks]]:
  - [[Optimization Techniques]]
  - [[Global Optimum]]
  - [[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Traveling Salesman Problem]]
  - [[Stochastic Algorithms]]

Sources

By Perplexity at https://www.perplexity.ai/search/Correlated-equilibrium-O2a5mFcnSB6EMaEFN7s1bQ
---
title: "Gale-Shapley Algorithm"
description: "A solution to the stable marriage problem, matching members of two sets based on their preferences in a way that ensures no pair would both prefer each other over their current partners."
type: "concept"
tags:
- "Algorithm Design"
- "Matching Markets"
- "Stable Marriage Problem"
- "Gale_Shapley_Algorithm"
relationships:
- "#developed [[David Gale]], [[Lloyd Shapley]]"
birthdate: "1962-03-14"
deathdate: ""
---

The Gale-Shapley algorithm, also known as the Deferred Acceptance algorithm, is a solution to the stable marriage problem, which involves matching members of two sets (traditionally men and women) based on their preferences for each other in such a way that no pair of individuals would both prefer each other over their current partners. This condition ensures the stability of all matches.

**Key Concepts:**

- **Stability**: A matching is stable if there are no two individuals who would both prefer each other over their current matched partners.
- **Deferred Acceptance**: The algorithm operates by one set (e.g., men) proposing to members of the other set (e.g., women) based on their preferences. Proposals are either accepted tentatively or rejected based on the preferences of the receiving set. The process iterates until all individuals are matched, ensuring no individual is matched with someone not on their preference list.

**Algorithm Steps:**

1. **Initialization**: All individuals in both sets start unengaged.
2. **Proposal**: Each unengaged individual from the proposing set proposes to their most preferred individual in the other set who has not yet rejected them.
3. **Acceptance/Rejection**: Upon receiving a proposal, an individual in the receiving set will tentatively accept the proposal if they are unengaged or if they prefer the new proposal over their current engagement. Otherwise, the proposal is rejected. This can lead to previously accepted proposals being rejected.
4. **Iteration**: Steps 2 and 3 are repeated until everyone is engaged.

**Properties:**

- The algorithm guarantees a stable matching, where stability means there are no two people who would prefer each other over their current partners.
- The matching is optimal for the proposing set in terms of their preferences and pessimal for the receiving set, meaning the proposing set gets the best possible outcome under any stable matching, and the receiving set gets the worst.
- The algorithm is strategy-proof for the proposing set, meaning they achieve their best possible outcome by truthfully stating their preferences.

**Applications and Variations:**

- Beyond theoretical interest, the Gale-Shapley algorithm has practical applications in various matching markets, such as matching medical residents to hospitals (the National Resident Matching Program) and students to schools.
- Variations of the algorithm accommodate different market structures, including those with unequal numbers of participants or preferences over groups rather than individuals.

The Gale-Shapley algorithm's introduction by David Gale and Lloyd Shapley in 1962 has had a profound impact on the field of economics and operations research, providing a foundational tool for understanding and designing stable matching mechanisms in various contexts[1][2][3][4][7][8][9][10][11][12].

- Important [[wikilinks]]:
  - [[Stable Marriage Problem]]
  - [[National Resident Matching Program]]
  - [[Algorithm Design]]
  - [[Matching Markets]]

Sources
[1] Gale–Shapley algorithm simply explained | by Alexander Osipenko https://towardsdatascience.com/gale-shapley-algorithm-simply-explained-caa344e643c2
[2] [PDF] Lecture 12 - UPenn CIS https://www.cis.upenn.edu/~aaroth/courses/slides/agt17/lect12.pdf
[3] Gale–Shapley algorithm - Wikipedia https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm
[4] Stable marriage problem - Wikipedia https://en.wikipedia.org/wiki/Stable_marriage_problem
[5] (AGT7E4) [Game Theory] Deferred Acceptance Algorithm (One-to-One ... https://www.youtube.com/watch?v=rh0RHYXu2RY
[6] The Stable Marriage Problem: If one sex asks the other out, the ... - Reddit https://www.reddit.com/r/programming/comments/cwnl7/the_stable_marriage_problem_if_one_sex_asks_the/
[7] Stable Marriage Problem - GeeksforGeeks https://www.geeksforgeeks.org/stable-marriage-problem/
[8] The deferred acceptance (DA) algorithm utilised in school choice ... https://towardsdatascience.com/the-deferred-acceptance-da-algorithm-utilised-in-school-choice-with-python-afc0fe892921
[9] Stable Matching Problem http://www.matchu.ai/GaleShapley
[10] Deferred Acceptance — Avela https://avela.org/deferred-acceptance
[11] [PDF] SF2972: Game theory https://www.math.kth.se/matstat/gru/sf2972/2017/matchingslides.pdf
[12] GC Admissions Match | The Matching Algorithm https://natmatch.com/gcadmissions/algorithm.html
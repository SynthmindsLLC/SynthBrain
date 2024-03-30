---
Date: [[2024-03-28]]
Tags: 
 - "#computer_science" 
 - "#complexity_theory"
 - "#np_complete"
 - "#algorithms"
---

NP-complete problems are a critical concept in computational complexity theory, representing decision problems that are both in NP and NP-hard. The class NP consists of those problems for which a solution, if one exists, can be verified in polynomial time by a deterministic Turing machine. A problem is NP-hard if it is at least as hard as the hardest problems in NP, meaning that any NP problem can be reduced to it in polynomial time. A problem is NP-complete if it satisfies both of these conditions, making it one of the most challenging problems within NP[1][7].

## Definition
An NP-complete problem has the following characteristics:
- It is a decision problem, where the output is a simple "yes" or "no" answer.
- For any "yes" instance of the problem, there exists a certificate (or witness) that can be verified in polynomial time.
- The problem is as hard as the hardest problems in NP, meaning that any problem in NP can be transformed into this problem in polynomial time[1][7].

## Examples
Some classic examples of NP-complete problems include:
- **Boolean Satisfiability Problem (SAT)**: Determining if there exists an interpretation that satisfies a given Boolean formula[1].
- **Traveling Salesman Problem (TSP)**: Finding the shortest possible route that visits a set of cities and returns to the origin city[1][11].
- **Knapsack Problem**: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible[1].
- **Graph Coloring**: Assigning colors to the vertices of a graph so that no two adjacent vertices share the same color, using a limited number of colors[1].
- **Hamiltonian Cycle**: Determining whether a given graph contains a Hamiltonian cycle, a cycle that visits each vertex exactly once[1].

## Solving Techniques
While there is no known polynomial-time algorithm to solve NP-complete problems in general, several approaches are used to handle them:
- **Heuristic Algorithms**: These algorithms search for satisfactory, if not optimal, solutions and can be quite effective for specific instances or versions of NP-complete problems[8].
- **Approximation Algorithms**: For some NP-complete problems, algorithms can guarantee a solution within a certain factor of the optimal solution[8].
- **Parameterized Algorithms**: These algorithms are efficient for small values of certain parameters, despite being exponential in the general case[8].
- **Reduction Techniques**: To prove that a problem is NP-complete, it is often reduced from a known NP-complete problem[19].

## Importance
The study of NP-complete problems is crucial because if any NP-complete problem can be solved in polynomial time, then every problem in NP can also be solved in polynomial time, which would imply P=NP. This is one of the most significant open questions in computer science[1][7].

## Everyday Encounters
NP-complete problems often arise in real-world situations, such as scheduling, network design, and many optimization problems. Understanding their complexity helps in developing efficient algorithms and recognizing the limitations of computational problem-solving[18].

## References
- Garey, M., & Johnson, D. (1979). Computers and Intractability: A Guide to the Theory of NP-Completeness. W.H. Freeman & Co.
- Cook, S. (1971). The complexity of theorem-proving procedures. In Proceedings of the third annual ACM symposium on Theory of computing (pp. 151-158).

<Important [[wikilinks]]>
- [[Computational Complexity Theory]]
- [[Deterministic Turing Machine]]
- [[Polynomial Time]]
- [[Heuristic Algorithms]]
- [[Approximation Algorithms]]
- [[Parameterized Algorithms]]
- [[Reduction Techniques]]
- [[P=NP Question]]

Sources
[1] NP-completeness - Wikipedia https://en.wikipedia.org/wiki/NP-completeness
[2] What is an NP-complete in computer science? [closed] - Stack Overflow https://stackoverflow.com/questions/210829/what-is-an-np-complete-in-computer-science
[3] NP-complete https://xlinux.nist.gov/dads/HTML/npcomplete.html
[4] What is NP-completeness? | Autoblocks Glossary https://www.autoblocks.ai/glossary/np-completeness
[5] P, NP, NP-hard, NP-complete: Explain please! : r/algorithms - Reddit https://www.reddit.com/r/algorithms/comments/7kybyz/p_np_nphard_npcomplete_explain_please/
[6] NP-complete problem | Definition, Examples, & Facts - Britannica https://www.britannica.com/science/NP-complete-problem
[7] NP (complexity) - Wikipedia https://en.wikipedia.org/wiki/NP_%28complexity%29
[8] How to Handle NP-Complete Problems in Algorithm Development https://www.linkedin.com/advice/1/what-some-examples-np-complete-problems-you
[9] List of NP-complete problems - Wikipedia https://en.wikipedia.org/wiki/List_of_NP-complete_problems
[10] Introduction to NP-Complete Complexity Classes - GeeksforGeeks https://www.geeksforgeeks.org/introduction-to-np-completeness/
[11] NP Complete: Example Problems & Definitions - StudySmarter https://www.studysmarter.co.uk/explanations/computer-science/theory-of-computation/np-complete/
[12] [PDF] Chapter 13 Some NP-Complete Problems https://www.seas.upenn.edu/~cis2620/notes/cis262sl14.pdf
[13] What are NP and NP-complete problems? [closed] - Stack Overflow https://stackoverflow.com/questions/6916162/what-are-np-and-np-complete-problems
[14] Best-case Running-time to solve an NP-Complete problem - MathOverflow https://mathoverflow.net/questions/6418/best-case-running-time-to-solve-an-np-complete-problem
[15] [PDF] NP-complete problems - People @EECS https://people.eecs.berkeley.edu/~vazirani/algorithms/chap8.pdf
[16] Annotated List of Selected NP-complete Problems https://cgi.csc.liv.ac.uk/~ped/teachadmin/COMP202/annotated_np.html
[17] NP-Completeness - UCI ICS https://ics.uci.edu/~eppstein/161/960312.html
[18] Everyday encounters with NP-complete problems https://cstheory.stackexchange.com/questions/446/everyday-encounters-with-np-complete-problems
[19] What are the steps to identify NP-complete problems? - LinkedIn https://www.linkedin.com/advice/0/what-steps-identify-np-complete-problems-skills-algorithms-dmcbc

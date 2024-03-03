---
Date: [[2024-03-02]]
Tags: 
 - "#BayesTheorem"
 - "#Probability"
 - "#Statistics"
 - "#ConditionalProbability"
---

## Bayes' Theorem

Bayes' Theorem is a fundamental concept in probability and statistics that describes the probability of an event, based on prior knowledge of conditions that might be related to the event. It is named after the Reverend Thomas Bayes and is used to update the probability for a hypothesis as more evidence or information becomes available[2][3][4][5][13].

### The Formula
The theorem is mathematically expressed as:

$$ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} $$

where:
- $$ P(A|B) $$ is the posterior probability of event A occurring given that B is true.
- $$ P(B|A) $$ is the likelihood of event B occurring given that A is true.
- $$ P(A) $$ is the prior probability of event A occurring.
- $$ P(B) $$ is the marginal probability of event B occurring.

### Understanding the Terms
- **Prior Probability** ($$ P(A) $$): The initial probability of event A before considering any new evidence.
- **Posterior Probability** ($$ P(A|B) $$): The revised probability of event A after taking into account the new evidence B.
- **Likelihood** ($$ P(B|A) $$): The probability of observing the evidence B given that event A is true.
- **Marginal Probability** ($$ P(B) $$): The total probability of observing the evidence B under all possible outcomes.

### Applications
Bayes' Theorem has a wide range of applications, including:
- **Medical Diagnosis**: Estimating the probability of a disease given a test result[3][5].
- **Machine Learning**: In algorithms like Naive Bayes for classification problems[2][5].
- **Finance**: Assessing the risk of lending money or forecasting investment success[3][17].
- **Decision Making**: Updating beliefs in light of new evidence[2][5].

### Example
If a drug test is 98% accurate and 0.5% of people use the drug, the probability that a person selected at random and tests positive is actually a user of the drug is calculated as follows[3]:

$$ P(\text{User}|\text{Positive}) = \frac{P(\text{Positive}|\text{User}) \cdot P(\text{User})}{P(\text{Positive})} = \frac{0.98 \cdot 0.005}{(0.98 \cdot 0.005) + ((1 - 0.98) \cdot (1 - 0.005))} \approx 19.76\% $$

### Conclusion
Bayes' Theorem is a powerful tool for understanding the likelihood of events in the presence of uncertainty and for making informed decisions based on evolving information. Its ability to incorporate new evidence into existing beliefs makes it invaluable in various fields[2][3][4][5][13].

- [[Probability Theory]]
- [[Statistics]]
- [[Conditional Probability]]

Sources
[1] Bayes' Theorem EXPLAINED with Examples - YouTube https://youtube.com/watch?v=cqTwHnNbc8g
[2] What is Bayes Theorem? - Terminologies and Applications - Analytics Steps https://www.analyticssteps.com/blogs/what-bayes-theorem-terminologies-and-applications
[3] Bayes' Theorem: What It Is, Formula, and Examples - Investopedia https://www.investopedia.com/terms/b/bayes-theorem.asp
[4] Bayes' Theorem Problems, Definition and Examples - Statistics How To https://www.statisticshowto.com/probability-and-statistics/probability-main-index/bayes-theorem-problems/
[5] Bayes' Rule – Explained For Beginners - freeCodeCamp https://www.freecodecamp.org/news/bayes-rule-explained/
[6] [PDF] BAYES THEOREM AND ITS RECENT APPLICATIONS https://journals.le.ac.uk/ojs1/index.php/lumj/article/viewFile/3488/3130
[7] Quick Bayes Theorem Calculator https://www.socscistatistics.com/bayes/default.aspx
[8] Bayes' Theorem - Data Science Discovery https://discovery.cs.illinois.edu/learn/Prediction-and-Probability/Bayes-Theorem/
[9] An Intuitive (and Short) Explanation of Bayes' Theorem - BetterExplained https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/
[10] Bayes' rule with a simple and practical example - Towards Data Science https://towardsdatascience.com/bayes-rule-with-a-simple-and-practical-example-2bce3d0f4ad0
[11] How to Calculate Probability Using Bayes' Formula (With Steps) - Indeed https://ca.indeed.com/career-advice/career-development/bayes-formula
[12] Bayes Theorem - Formula, Statement, Proof | Bayes Rule - Cuemath https://www.cuemath.com/data/bayes-theorem/
[13] Bayes' theorem - Wikipedia https://en.wikipedia.org/wiki/Bayes%27_theorem
[14] Bayes' Theorem - Math is Fun https://www.mathsisfun.com/data/bayes-theorem.html
[15] Bayes' Theorem, Clearly Explained!!!! - YouTube https://youtube.com/watch?v=9wCnvr7Xw4E
[16] What Is Bayes Theorem: Formulas, Examples and Calculations https://www.simplilearn.com/tutorials/statistics-tutorial/bayes-theorem
[17] Bayes' Theorem - Definition, Formula, and Example https://corporatefinanceinstitute.com/resources/data-science/bayes-theorem/
[18] Bayes Theorem - Statement, Proof, Formula, Derivation & Examples https://byjus.com/maths/bayes-theorem/

By Perplexity at https://www.perplexity.ai/search/First-in-first-7cmiTBbTR1iVl7J2sw6zHA
---
Title: Bonferroni Correction
Description: A summary of the Bonferroni correction for multiple hypothesis testing in statistics.
Date: 2023-04-13
Tags:
 - "#statistics"
 - "#hypothesis-testing"
 - "#multiple-comparisons"
 - "#type-I-error"
---

The Bonferroni correction is a method used to counteract the problem of multiple comparisons in statistical hypothesis testing. It is a simple but conservative approach to control the family-wise error rate (FWER) when conducting multiple hypothesis tests.

## The Problem of Multiple Comparisons

When performing multiple hypothesis tests, the probability of making a Type I error (false positive - rejecting a true null hypothesis) increases with the number of tests. For example, if conducting 100 independent tests at a significance level α=0.05, the probability of at least one Type I error is 1-(1-0.05)^100 ≈ 0.994. So you are almost guaranteed to get a "significant" result by chance alone.

## The Bonferroni Correction

The Bonferroni correction adjusts the significance level for each individual test to ensure the overall FWER is controlled at the desired level α. The adjustment is:

α_adjusted = α / m

where m is the total number of tests.

For example, if conducting 5 tests and want to maintain an overall α=0.05, each individual test would be evaluated at α=0.01.

To apply the correction:

1. Conduct all m hypothesis tests, calculating their p-values
2. Multiply each p-value by m
3. Compare the adjusted p-values to the original α level
4. Reject the null hypothesis for any test where p_adjusted ≤ α

## Limitations

The Bonferroni correction controls the FWER, but can be quite conservative, especially for a large number of tests. This increases the probability of Type II errors (false negatives).

It also assumes the tests are independent. If tests are positively correlated, the correction will be even more conservative.

Despite limitations, the Bonferroni correction is widely used due to its simplicity. It is most useful when a small number of planned comparisons are made and strict control of Type I error is important.

## List of Relevant Backlinks
- [[Family-wise error rate (FWER)]]
- [[Type I and Type II errors]]
- [[Significance level (α)]]
- [[p-value]]
- [[Hypothesis testing]]

Sources
[1] Bonferroni Correction -- from Wolfram MathWorld https://mathworld.wolfram.com/BonferroniCorrection.html
[2] Bonferroni Correction - Statistics Solutions https://www.statisticssolutions.com/bonferroni-correction/
[3] When To Apply A Bonferroni Correction - YouTube https://www.youtube.com/watch?v=4dGPVT5JzHw
[4] What Is the Bonferroni Test (Correction) and How Is It Used? - Investopedia https://www.investopedia.com/terms/b/bonferroni-test.asp
[5] What is the Bonferroni Correction and How to Use It - Statistics By Jim https://statisticsbyjim.com/hypothesis-testing/bonferroni-correction/
[6] The Bonferroni Correction - Clearly Explained - YouTube https://www.youtube.com/watch?v=HLzS5wPqWR0
[7] Trouble Understanding Holm-Bonferroni Correction https://stats.stackexchange.com/questions/476734/trouble-understanding-holm-bonferroni-correction
[8] When to use the Bonferroni correction - PubMed https://pubmed.ncbi.nlm.nih.gov/24697967/
[9] SOME DESIRABLE PROPERTIES OF THE BONFERRONI CORRECTION https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6395159/
[10] Bonferroni - Multiple t-tests: Winsteps Help https://www.winsteps.com/winman/bonferroni.htm
[11] The calculation of Bonferroni-adjusted p-values - IBM https://www.ibm.com/support/pages/calculation-bonferroni-adjusted-p-values
[12] [PDF] 1 Why is multiple testing a problem? 2 The Bonferroni correction - UC Berkeley Statistics https://www.stat.berkeley.edu/~mgoldman/Section0402.pdf
[13] Bonferroni Correction - an overview | ScienceDirect Topics https://www.sciencedirect.com/topics/computer-science/bonferroni-correction

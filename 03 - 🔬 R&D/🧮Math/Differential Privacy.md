---
Date: [[2024-03-06]]
Tags: 
 - "#differential_privacy"
 - "#data_protection"
 - "#privacy_techniques"
 - "#algorithmic_privacy"
---

Differential privacy is a framework for quantifying the privacy guarantees provided by an algorithm. It aims to enable the analysis of datasets containing sensitive information while ensuring that the privacy of individuals in the dataset is protected. The core idea is that the output of a differentially private algorithm should not allow one to infer whether any individual's data was included in the input dataset, within a certain mathematical bound.

A differentially private algorithm adds a controlled amount of random noise to the output, based on the "sensitivity" of the query (i.e., the maximum amount by which a single individual's data can change the output). The amount of noise determines the "privacy budget," with a smaller amount of noise providing stronger privacy guarantees but potentially less accurate results.

Differential privacy is defined in terms of two parameters: epsilon ($$\epsilon$$) and delta ($$\delta$$). $$\epsilon$$ provides a measure of privacy loss, with smaller values indicating stronger privacy. $$\delta$$ accounts for the probability that the privacy guarantee might not hold, ideally being close to zero. Together, these parameters allow for a formal and quantifiable privacy guarantee, balancing the trade-off between privacy and utility.

This framework has been adopted by various organizations and researchers to protect sensitive data, including the U.S. Census Bureau for census data and companies like Google and Apple for collecting usage statistics without compromising individual privacy.

Differential privacy is applicable in various contexts, including statistical databases, machine learning models, and social networks, making it a foundational concept in the field of privacy-preserving data analysis.

- Important [[wikilinks]]:
  - [[Privacy-Preserving Data Analysis]]
  - [[Sensitivity in Differential Privacy]]
  - [[Privacy Budget]]
  - [[Epsilon-Delta Privacy Guarantee]]

Sources

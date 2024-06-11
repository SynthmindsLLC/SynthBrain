---
title: "Expectation-Maximization (EM) Algorithm"
description: "Statistical technique for finding maximum likelihood estimates of parameters in probabilistic models, especially when the data is incomplete or corrupted. Alternates between E and M steps until convergence."
type: "concept"
tags:
- "Statistical_Learning"
- "Machine_Learning"
- "Expectation-Maximization"
- "#EM_algorithm"
relationships:
- "#used_for [[Parameter Estimation]]"
- "#applies_to [[Probabilistic Models]]"]]
- "#related_to [[Gaussian Mixture Models]], [[Hidden Markov Models]], [[Bayesian Networks]]"
- "#enables [[Maximum Likelihood Estimation]]"
- "#has_participant [[Data Scientists]]"
---

The Expectation-Maximization (EM) algorithm is a statistical technique for finding maximum likelihood estimates of parameters in probabilistic models, especially when the data is incomplete, has missing values, or is otherwise corrupted (e.g., in the presence of hidden variables). The algorithm alternates between performing an expectation (E) step and a maximization (M) step until convergence.

1. **Expectation (E) step**: Calculate the expected value of the log-likelihood function, with respect to the conditional distribution of the hidden variables given the observed data and the current estimate of the model parameters.

2. **Maximization (M) step**: Find the parameters that maximize the expected log-likelihood found in the E step. These estimates are then used to determine the distribution of the hidden variables in the next E step.

The EM algorithm is particularly useful in situations where the likelihood function is difficult to optimize directly. It is widely used in various fields such as bioinformatics, computer vision, and natural language processing. Common applications include Gaussian mixture models, hidden Markov models, and Bayesian networks.

The algorithm's main advantages are its simplicity and ease of implementation. However, it can be sensitive to initial conditions and may converge to a local maximum rather than the global maximum.

- Important [[wikilinks]]:
  - [[Maximum Likelihood Estimation]]
  - [[Probabilistic Models]]
  - [[Gaussian Mixture Models]]
  - [[Hidden Markov Models]]
  - [[Bayesian Networks]]

Sources
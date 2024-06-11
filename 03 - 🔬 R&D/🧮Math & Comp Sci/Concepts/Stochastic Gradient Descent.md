---
title: "Stochastic Gradient Descent (SGD)"
description: An optimization algorithm widely used in machine learning for training various models, particularly when dealing with large datasets. It is a variant of the gradient descent algorithm that updates the model's parameters using only a single or a small batch of examples at each iteration, rather than the entire dataset. This approach introduces randomness into the optimization process, hence the term "stochastic."
type: "concept"
tags:
- "Optimization"
- "Machine Learning"
- "Stochastic_Gradient_Descent"
relationships:
- "#related_to [[Gradient Descent]]"
- "#used_for [[Training Machine Learning Models]]"
- "#has_part [[Learning Rate]]"
birthdate: "2024-03-14"
---

Stochastic Gradient Descent (SGD) is an optimization algorithm widely used in machine learning for training various models, particularly when dealing with large datasets. It is a variant of the gradient descent algorithm that updates the model's parameters using only a single or a small batch of examples at each iteration, rather than the entire dataset. This approach introduces randomness into the optimization process, hence the term "stochastic."

**Key Concepts:**

- **Gradient Descent**: A method to minimize an objective function by iteratively moving in the direction of the steepest descent as defined by the negative of the gradient.
- **Stochastic**: In SGD, the algorithm randomly selects a subset of data (or a single data point) to compute the gradient of the objective function, making the method stochastic.
- **Learning Rate**: A crucial hyperparameter that determines the size of the steps taken towards the minimum. Too large a learning rate can cause the algorithm to overshoot the minimum, while too small a learning rate can slow down convergence.

**Advantages of SGD:**

- **Efficiency**: SGD is computationally much less expensive per iteration than standard gradient descent, making it suitable for large datasets.
- **Convergence**: For convex or pseudoconvex objective functions, SGD converges almost surely to a global minimum, and to a local minimum otherwise[1].
- **Online Learning**: SGD can be used in an online learning setting, where the model is updated as new data arrives[2][3].

**Challenges and Variants:**

- **Variance**: The randomness in SGD can lead to high variance in the parameter updates, causing the objective function to fluctuate[3][6].
- **Convergence Rate**: While efficient per iteration, SGD may require more iterations to converge due to its stochastic nature[3][6].
- **Variants**: To address some of these challenges, variants of SGD such as Mini-batch Gradient Descent, Momentum SGD, and others have been developed. These methods aim to reduce variance and improve convergence rates[2][3][6].

SGD has been foundational in enabling the training of complex models on large datasets, particularly in deep learning, where it remains a method of choice due to its simplicity and effectiveness.

- Important [[wikilinks]]:
  - [[Gradient Descent]]
  - [[Learning Rate]]
  - [[Mini-batch Gradient Descent]]
  - [[Momentum SGD]]

Sources
[1] Stochastic gradient descent - Wikipedia https://en.wikipedia.org/wiki/Stochastic_gradient_descent
[2] How is stochastic gradient descent implemented in the context of ... https://sebastianraschka.com/faq/docs/sgd-methods.html
[3] Optimization: Stochastic Gradient Descent - Deep Learning http://deeplearning.stanford.edu/tutorial/supervised/OptimizationStochasticGradientDescent/
[4] Is reinforcement learning analogous to stochastic gradient descent? https://datascience.stackexchange.com/questions/104439/is-reinforcement-learning-analogous-to-stochastic-gradient-descent
[5] Handbook of Convergence Theorems for (Stochastic) Gradient Methods https://arxiv.org/abs/2301.11235
[6] ML | Stochastic Gradient Descent (SGD) - GeeksforGeeks https://www.geeksforgeeks.org/ml-stochastic-gradient-descent-sgd/
[7] Stochastic gradient descent - Optimization Wiki https://optimization.cbe.cornell.edu/index.php?title=Stochastic_gradient_descent
[8] Stochastic Gradient Descent explained in real life https://towardsdatascience.com/stochastic-gradient-descent-explained-in-real-life-predicting-your-pizzas-cooking-time-b7639d5e6a32
[9] Stochastic Gradient Descent increases Cost Function https://stackoverflow.com/questions/50360138/stochastic-gradient-descent-increases-cost-function
[10] [PDF] Lecture 5: Stochastic Gradient Descent - Cornell CS https://www.cs.cornell.edu/courses/cs4787/2019sp/notes/lecture5.pdf
[11] Stochastic Gradient Descent Algorithm With Python and NumPy https://realpython.com/gradient-descent-algorithm-python/
[12] Stochastic Gradient Descent: Math and Python Code https://towardsdatascience.com/stochastic-gradient-descent-math-and-python-code-35b5e66d6f79
[13] [PDF] CPSC 540: Machine Learning - SGD Convergence Rate https://www.cs.ubc.ca/~schmidtm/Courses/540-W19/L11.pdf
[14] Stochastic Gradient Descent — Clearly Explained https://towardsdatascience.com/stochastic-gradient-descent-clearly-explained-53d239905d31
[15] Stochastic Gradient Descent, Clearly Explained!!! - YouTube https://www.youtube.com/watch?v=vMh0zPT0tLI
[16] [PDF] Stochastic Gradient Descent - Statistics & Data Science https://www.stat.cmu.edu/~ryantibs/convexopt-F18/lectures/stochastic-gd.pdf
[17] [PDF] CS289ML: Notes on convergence of gradient descent - Raghu Meka https://raghumeka.github.io/CS289ML/gdnotes.pdf
[18] [PDF] Handbook of Convergence Theorems for (Stochastic) Gradient Methods https://gowerrobert.github.io/pdf/M2_statistique_optimisation/grad_conv.pdf
[19] On Almost Sure Convergence Rates of Stochastic Gradient Methods - arXiv https://arxiv.org/abs/2202.04295
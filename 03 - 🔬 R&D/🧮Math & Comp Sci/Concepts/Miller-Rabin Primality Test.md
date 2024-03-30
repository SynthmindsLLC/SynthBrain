---
Date: [[2024-03-14]]
Tags: 
 - "#miller_rabin_primality_test"
 - "#number_theory"
 - "#algorithms"
 - "#cryptography"
---

The Miller-Rabin primality test is a probabilistic algorithm used to determine whether a given number is prime. Unlike deterministic tests, which provide a definitive answer, the Miller-Rabin test can only say that a number is either "definitely composite" or "probably prime." The test is based on an extension of Fermat's little theorem and is particularly favored for its efficiency with large numbers.

**Algorithm Overview:**

1. **Representation**: Given an odd integer $$n > 2$$ to test for primality, write $$n - 1$$ as $$2^s \cdot d$$, where $$d$$ is odd.
2. **Witness Loop**: For a predetermined number of trials, pick a random integer $$a$$ in the range $$[2, n - 2]$$ and compute $$x = a^d \mod n$$.
3. **Initial Check**: If $$x$$ is not 1 or $$n - 1$$, repeatedly square $$x$$ (mod $$n$$) and check if it becomes $$n - 1$$. If it does, the test continues with another witness; if not, $$n$$ is composite.
4. **Composite or Probably Prime**: If none of the witnesses show that $$n$$ is composite, then $$n$$ is declared "probably prime."

**Properties:**

- **Error Probability**: The probability that the Miller-Rabin test incorrectly identifies a composite number as "probably prime" can be made arbitrarily small by increasing the number of trials.
- **Efficiency**: The test is fast, especially for large numbers, making it suitable for cryptographic applications where large primes are needed.
- **Widely Used**: Due to its effectiveness and simplicity, it is one of the most commonly used primality tests in practice.

**Applications:**

- **Cryptography**: Generating large prime numbers for public-key cryptography, such as RSA.
- **Mathematical Software**: Libraries and software that require prime number generation or verification.

The Miller-Rabin test is an example of a Monte Carlo algorithm, where the correctness of the result is probabilistic, and the accuracy can be improved by increasing the number of random samples (trials) used in the test.

- Important [[wikilinks]]:
  - [[Fermat's Little Theorem]]
  - [[Probabilistic Algorithms]]
  - [[Public-Key Cryptography]]
  - [[Monte Carlo Algorithm]]

Sources

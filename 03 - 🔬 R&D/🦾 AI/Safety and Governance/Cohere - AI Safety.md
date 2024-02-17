[The Enterprise Guide to AI Safety](https://txt.cohere.com/the-enterprise-guide-to-ai-safety/)

- mentions [Understanding AI Harms: An Overview](# Understanding AI Harms: An Overview)
- mentions [Taxonomy of Risks](https://dl.acm.org/doi/pdf/10.1145/3531146.3533088?ref=txt.cohere.com) paper
# Types of Fairness
- 2 types of fairness 
	- [[Allocational Fairness]]
		- unequal allocation of resources
	- [[Representational Fairness]]
		- harm to public opinion or image
# Individual and Distributed
- "Some distributional biases, like a system that never generates stories about LGBTQ couples no matter the prompt, are known as “erasure” and can produce an obvious systematic exclusion of an entire group."

# Data
[Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/abs/1607.06520)
- "in reality about 40% of doctors in the U.S. were women, but in the training data (sourced from news stories), only 9% of doctors were women."
- ![[Pasted image 20231116165025.png]]
- "if the original data was slightly biased against women, the resulting model will be very biased against women. A lot of fairness research is dedicated to [reducing the amplification](https://arxiv.org/abs/1707.09457?ref=txt.cohere.com), rather than correcting the original biases from the data."

# Context of Safety
- essentially need to consider the risk profile

# No clear link between upstream harm mitigation (of LLMs) and applied harms downstream

- "Research has tried upstream bias mitigation in models, but [studies](https://arxiv.org/pdf/2012.15859.pdf?ref=txt.cohere.com) revealed that deployment didn’t improve downstream"
- "We can evaluate a product’s impact as people use it today, but we can not as easily evaluate the underlying model. Ultimately, model-level safety assessments don't yet predict real-world outcomes"

# Safety measures rely on aligned methodology
- "Here’s an example:

- First, a goal should reflect a normative view, like "minoritized groups shouldn't face distressing chatbot content."
- Second, a conceptualization of that could be “hate speech in model generated outputs.”
- And finally, an operationalization could be “an output is toxic when the API has a score above 0.9, and this rate should be equal across all groups.

[Language (Technology) is Power: A Critical Survey of “Bias” in NLP](https://aclanthology.org/2020.acl-main.485/)

# Trade offs
- "blocking certain outputs can hurt overall performance metrics. First, concepts like "don't generate anything illegal/unethical" are too vague to implement precisely and can cause the training data to be lower quality if implemented"
- "stopping models from generating prohibited content when requested by a malicious user, called "jailbreaking," requires training the model to disregard some user instructions, which further degrades training data quality"

#AIsafety #Alignment #bias 

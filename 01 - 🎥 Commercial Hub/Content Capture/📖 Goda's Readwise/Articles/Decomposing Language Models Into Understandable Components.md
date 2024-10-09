# Decomposing Language Models Into Understandable Components

![rw-book-cover](https://cdn.sanity.io/images/4zrzovbb/website/4b8bc05b916dc4fbaf2543f76f946e5587aaeb43-2400x1260.png)

## Metadata
- Author: [[anthropic.com]]
- Full Title: Decomposing Language Models Into Understandable Components
- Category: #articles
- URL: https://www.anthropic.com/news/decomposing-language-models-into-understandable-components
- Tags:

## Highlights
- Neural networks are trained on data, not programmed to follow rules. ([View Highlight](https://read.readwise.io/read/01hz2kfc6xn6m654a14sxws0xj))
- We understand the math of the trained network exactly – each neuron in a neural network performs simple arithmetic – but we don't understand why those mathematical operations result in the behaviors we see. ([View Highlight](https://read.readwise.io/read/01hz2kg9944xs5badjkwfftc0e))
- Neuroscientists face a similar problem with understanding the biological basis for human behavior. The neurons firing in a person's brain must somehow implement their thoughts, feelings, and decision-making. ([View Highlight](https://read.readwise.io/read/01hz2kh5wh4w2zv3t4xptzb9xb))
- Unfortunately, it turns out that the individual neurons do not have consistent relationships to network behavior. ([View Highlight](https://read.readwise.io/read/01hz2kjgkg6v8775rytkdbgp97))
- For example, [a single neuron](https://transformer-circuits.pub/2023/monosemantic-features/vis/a-neurons.html#feature-83) in a small language model is active in many unrelated contexts, including: academic citations, English dialogue, HTTP requests, and Korean text. ([View Highlight](https://read.readwise.io/read/01hz2kk09g2stwhh65sa03hkzz))
- In a classic vision model, a [single neuron](https://distill.pub/2017/feature-visualization/#diversity) responds to faces of cats and fronts of cars. ([View Highlight](https://read.readwise.io/read/01hz2knvdfq5yfaecn70fbhwcy))
- In our latest paper, [*Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*](https://transformer-circuits.pub/2023/monosemantic-features/index.html), we outline evidence that there are better units of analysis than individual neurons, and we have built machinery that lets us find these units in small transformer models. ([View Highlight](https://read.readwise.io/read/01hz2kqrtaeyjtzq0f9dd3192z))
- This provides a path to breaking down complex neural networks into parts we can understand, and builds on previous efforts to interpret high-dimensional systems in neuroscience, machine learning, and statistics. ([View Highlight](https://read.readwise.io/read/01hz2krpv7r816err6ck5wr3be))
- the features score higher than the neurons, providing additional evidence that the activations of features and their downstream effects on model behavior have a consistent interpretation. ([View Highlight](https://read.readwise.io/read/01hz2kvhzmja0e8680ns3etpt4))
- Features also offer a targeted way to steer models. ([View Highlight](https://read.readwise.io/read/01hz2kvtkvyfeyn34shxzg0h16))
- As shown below, artificially activating a feature causes the model behavior to change in predictable ways. ([View Highlight](https://read.readwise.io/read/01hz2kw4b251rgze4ffs52e538))
- We find that the features that are learned are largely universal between different models, so the lessons learned by studying the features in one model may generalize to others. ([View Highlight](https://read.readwise.io/read/01hz2kx9ahe76b4xnnyzqhpsj0))
- Mechanistic Interpretability – one of our longest-term research bets on AI safety. ([View Highlight](https://read.readwise.io/read/01hz2kzg16yzgpdzkpd8qvme6z))
- the fact that individual neurons were uninterpretable presented a serious roadblock to a mechanistic understanding of language models. ([View Highlight](https://read.readwise.io/read/01hz2kzxd80279y9vw68e2g0cy))
- We hope this will eventually enable us to monitor and steer model behavior from the inside, improving the safety and reliability essential for enterprise and societal adoption. ([View Highlight](https://read.readwise.io/read/01hz2m0hvqv7bjcsyzkyfabpby))
- Our next challenge is to scale this approach up from the small model we demonstrate success on to frontier models which are many times larger and substantially more complicated. For the first time, we feel that the next primary obstacle to interpreting large language models is engineering rather than science. ([View Highlight](https://read.readwise.io/read/01hz2m16kxzqgetfv958sa5fmm))

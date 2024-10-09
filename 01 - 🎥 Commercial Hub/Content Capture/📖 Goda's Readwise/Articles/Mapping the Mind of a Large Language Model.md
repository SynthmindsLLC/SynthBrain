# Mapping the Mind of a Large Language Model

![rw-book-cover](https://cdn.sanity.io/images/4zrzovbb/website/7dd6783d4407d0b155766918579d0d848f67726b-1200x630.png)

## Metadata
- Author: [[anthropic.com]]
- Full Title: Mapping the Mind of a Large Language Model
- Category: #articles
- URL: https://www.anthropic.com/news/mapping-mind-language-model
- Tags:

## Highlights
- Today we report a significant advance in understanding the inner workings of AI models. ([View Highlight](https://read.readwise.io/read/01hz2m1pfhjty9504684tvxdse))
- We mostly treat AI models as a black box: something goes in and a response comes out, and it's not clear why the model gave that particular response instead of another. ([View Highlight](https://read.readwise.io/read/01hz2m2nxs47rgcx3vgfzsevbr))
- if we don't know how they work, how do we know they won't give harmful, biased, untruthful, or otherwise dangerous responses? How can we trust that they’ll be safe and reliable? ([View Highlight](https://read.readwise.io/read/01hz2m384ba9sps70wdfr647dw))
- the internal state of the model—what the model is "thinking" before writing its response—consists of a long list of numbers ("neuron activations") without a clear meaning. ([View Highlight](https://read.readwise.io/read/01hz2m3w3yrcczwgj01kydet2q))
- Previously, we made some progress matching *patterns* of neuron activations, called features, to human-interpretable concepts. ([View Highlight](https://read.readwise.io/read/01hz2m4r0tyw4rn6xwp02zfs2y))
- In turn, any internal state of the model can be represented in terms of a few active features instead of many active neurons. ([View Highlight](https://read.readwise.io/read/01hz2m5gtqee74gfef01p2m9w9))
- Just as every English word in a dictionary is made by combining letters, and every sentence is made by combining words, every feature in an AI model is made by combining neurons, and every internal state is made by combining features. ([View Highlight](https://read.readwise.io/read/01hz2m634vprkjhtfe76e0b74d))
- But we were optimistic that we could scale up the technique to the vastly larger AI language models now in regular use, and in doing so, learn a great deal about the features supporting their sophisticated behaviors. This required going up by many orders of magnitude—from a backyard bottle rocket to a Saturn-V. ([View Highlight](https://read.readwise.io/read/01hz2m7mn7hx4jfd2rppxzzq2a))
- We successfully extracted millions of features from the middle layer of Claude 3.0 Sonnet, (a member of our current, state-of-the-art model family, currently available on [claude.ai](https://claude.ai)), providing a rough conceptual map of its internal states halfway through its computation. ([View Highlight](https://read.readwise.io/read/01hz2ma334hfc3pah5jt7yb3v7))
- Whereas the features we found in the toy language model were rather superficial, the features we found in Sonnet have a depth, breadth, and abstraction reflecting Sonnet's advanced capabilities. ([View Highlight](https://read.readwise.io/read/01hz2masbv2m960g3a9y1szqjq))
- This holds at a higher level of conceptual abstraction: looking near a feature related to the concept of "inner conflict", we find features related to relationship breakups, conflicting allegiances, logical inconsistencies, as well as the phrase "catch-22". ([View Highlight](https://read.readwise.io/read/01hz2mghmsfgg2dz0ha287eazk))

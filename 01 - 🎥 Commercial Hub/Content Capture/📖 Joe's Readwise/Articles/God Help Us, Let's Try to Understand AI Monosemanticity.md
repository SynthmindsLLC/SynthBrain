# God Help Us, Let's Try to Understand AI Monosemanticity

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3a2a957-0d98-4d59-8d41-b461c421c9d7_210x136.png)

## Metadata
- Author: [[Scott Alexander]]
- Date: 2023-11-27
- Full Title: God Help Us, Let's Try to Understand AI Monosemanticity
- Category: #articles
- Summary: Inside every AI is a bigger AI, trying to get out
- URL: https://www.astralcodexten.com/p/god-help-us-lets-try-to-understand?publication_id=89120&utm_medium=email&utm_campaign=email-share&triggerShare=true&r=2kuc99

## Highlights
- deep in the middle, where the real thought has to be happening, there’s nothing representing “dog”. Instead, the neurons are much weirder than this. In one image model, an [earlier paper](https://distill.pub/2020/circuits/zoom-in/) found “one neuron that responds to cat faces, fronts of cars, and cat legs”. ([View Highlight](https://read.readwise.io/read/01hg9dvsxv39bnyp9wx883dr6v))
- the **[Toy Models Of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html)** paper ([View Highlight](https://read.readwise.io/read/01hg9dwgy7hd0c12s42470wevq))
- Moving to the right, we allow features to be less common - the AI may only have to think about a few at a time. The AI gradually shifts to packing its concepts into tetrahedra (three neurons per four concepts) and triangles (two neurons per three concepts) ([View Highlight](https://read.readwise.io/read/01hg9er7132vq8hc8hjxjkcgb1))
- Next it goes through pentagons and an unusual polyhedron called the “square anti-prism ([View Highlight](https://read.readwise.io/read/01hg9erjt7yr4yp3bn8atdrsn1))
- After exhausting square anti-prisms (8 features per three neurons) it gives up ([View Highlight](https://read.readwise.io/read/01hg9esa7s9hwa6bppanam11xm))
- the two-neuron AI in the pentagonal toy example above is simulating a five-neuron AI. ([View Highlight](https://read.readwise.io/read/01hg9etg166dnc88gwpb4tj1c6))
- They go on to prove that the real AI can then run computations in the simulated AI; in some sense, there really *is* an abstract five neuron AI doing all the cognition. ([View Highlight](https://read.readwise.io/read/01hg9etvjdb0fdggmbtq20bm9k))
- as real neurons start representing more and more simulated neurons, it produces more and more noise and conceptual interference. ([View Highlight](https://read.readwise.io/read/01hg9evehc5096kjxys1kb17zn))
- We hoped we could figure out what our AIs were doing just by looking at them. But it turns out they’re simulating much bigger and more complicated AIs, and if we want to know what’s going on, we have to look at *those*. But *those* AIs only exist in simulated abstract hyperdimensional spaces. ([View Highlight](https://read.readwise.io/read/01hg9ew11xmbvt9p0t0wsz4ecw))
    - Tags: [[favorite]] 
- First the researchers trained a very simple 512-neuron AI to predict text, like a tiny version of GPT or Anthropic’s competing model Claude.
  Then, they trained a second AI called an autoencoder to predict the activations of the first AI. They told it to posit a certain number of features (the experiments varied between ~2,000 and ~100,000), corresponding to the neurons of the higher-dimensional AI it was simulating. Then they made it predict how those features mapped onto the real neurons of the real AI. ([View Highlight](https://read.readwise.io/read/01hg9ewvmhd2bss9sf42da574t))
- They found that even though the original AI’s neurons weren’t comprehensible, the new AI’s simulated neurons (aka “features”) were! They were *monosemantic*, ie they meant one specific thing. ([View Highlight](https://read.readwise.io/read/01hg9ex7n998jfs81jk10mbjn3))
    - Tags: [[favorite]] 
- The team graded 412 real neurons vs. simulated neurons on subjective interpretability, and found the simulated neurons were on average pretty interpretable ([View Highlight](https://read.readwise.io/read/01hg9f7n92tff2gjdcnergzwr3))
- it seems plausible that training the autoencoder could become very expensive, potentially even more expensive than the original model. We remain optimistic, however, and there is a silver lining – it increasingly seems like a large chunk of the mechanistic interpretability agenda will now turn on succeeding at a difficult engineering and scaling problem, which frontier AI labs have significant expertise in. ([View Highlight](https://read.readwise.io/read/01hg9fbg8109wa1k19j95fxs95))
- we find evidence consistent with the hypothesis that neurons in both deep image model [AIs] and the visual cortex [of the brain] encode features in superposition. That is, we find non-axis aligned directions in the neural state space that are more interpretable than individual neurons. ([View Highlight](https://read.readwise.io/read/01hg9fhd2pt0db5hjsc1fyzy0j))

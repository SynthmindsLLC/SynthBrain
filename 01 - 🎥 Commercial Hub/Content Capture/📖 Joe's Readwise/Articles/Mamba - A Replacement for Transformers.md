# Mamba - A Replacement for Transformers?

![rw-book-cover](https://i.ytimg.com/vi/ouF-H35atOY/maxresdefault.jpg)

## Metadata
- Author: [[Samuel Albanie]]
- Date: 2023-12-08
- Full Title: Mamba - A Replacement for Transformers?
- Category: #articles
- Summary: Mamba is a state space model architecture that aims to be a replacement for Transformers in sequence modeling tasks. It builds on the concept of selective state spaces and incorporates hardware-aware algorithms to improve efficiency. Mamba combines the design of prior state space model architectures with the MLP block of Transformers to create a simple and homogeneous architecture. The model performs well on various tasks, including synthetic tasks, language modeling, and DNA modeling. It outperforms other baselines in terms of accuracy and scalability. However, there is an ablation study that identifies a case where the selection mechanism in Mamba may negatively affect performance.
- URL: https://youtube.com/watch?v=ouF-H35atOY&si=V6PEz9rXZ4GUAQd2

## Highlights
- the long range Arena a benchmark for efficient Transformers the St starting premise was that
  Transformers do not scale very well to Long sequence lengths largely because of quadratic self attention complexity ([View Highlight](https://read.readwise.io/read/01hhc6qm7a3chn3wafs86s12yf))
- a benchmark specifically focused on evaluating model quality under long context scenarios there were tasks like long list Ops where the model is given an input consisting of a long list of nested operators and needs to calculate an answer ([View Highlight](https://read.readwise.io/read/01hhc6rdw9s7vr2qq0e4f8q1we))
- independently and a little earlier a creative approach to tackling the longrange dependency problem was introduced in this work on leand memory units in the context of recurrent neural
  networks ([View Highlight](https://read.readwise.io/read/01hhc6sarwevt86a24xrqwppth))
- you can reconstruct the input U by reassembling it from the components of the memory Vector denoted
  here by m this idea can then be baked into a layer where the memory block is implemented with simple linear operations ([View Highlight](https://read.readwise.io/read/01hhc6ta0ckqegtke7cryyb4g0))
- hippo recurrent memory with optimal polinomial projections had the Insight that we can phrase memory as a technical problem of online function approximation where a function is summarized by storing its optimal coefficients in terms of some basis functions ([View Highlight](https://read.readwise.io/read/01hhc6tvzxh4zvvdkmyaqhecqm))
- followed by the work combining recurrent convolutional and continuous time models with linear State space layers which proposed a unifying framework for sequence modeling based on a standard State space representation ([View Highlight](https://read.readwise.io/read/01hhc6vpyh2dnbpedqyftfwhp0))
- starting from an implicit continuous time State space model you could discretize to produce A system that can
  be interpreted as a recurrent network with the benefit of efficient inference or as a convolutional model ([View Highlight](https://read.readwise.io/read/01hhc6w4svm5n9gv3c2vx3tvf8))
- starting from an implicit continuous time State space model you could discretize to produce A system that can
  be interpreted as a recurrent network with the benefit of efficient inference or as a convolutional model ([View Highlight](https://read.readwise.io/read/01hhc6w64r09rrjhzxydh02r0b))
- starting from an implicit continuous time State space model you could discretize to produce A system that can
  be interpreted as a recurrent network with the benefit of efficient inference or as a convolutional model which benefits from parallelizable training ([View Highlight](https://read.readwise.io/read/01hhc6wadhvc5fhs3fq89z78hr))
- continuous time State space model you could discretize to produce A system that can
  be interpreted as a recurrent network with the benefit of efficient inference or as a convolutional model which benefits from parallelizable training ([View Highlight](https://read.readwise.io/read/01hhc6wqtd3dmey9963wtrz8ck))
- S4 model introduced in
  efficiently modeling long sequences with structured State spaces what we'd really like to be able to do is use the convolutional interpretation we've just seen to efficiently train our state space ([View Highlight](https://read.readwise.io/read/01hhc6xafht1tnkcejnx05jp1e))
- we can address the hippo Matrix with an adjustment the authors note that although the hippo Matrix is not normal it can be decomposed as the sum of a norm noral and low rank Matrix even this is still
  not useful by itself ([View Highlight](https://read.readwise.io/read/01hhc6z00exebkb8czds1ztsrs))
- instead of computing the kernel Kar directly they instead compute its Spectrum then determine Kar by applying an inverse fft next we use everyone's favorite low rank trick the woodb identity that lets us perform an efficient Matrix update third it is shown that the diagonal matrix case is equivalent to the computation of a Koshi kernel a well-studied problem with st aable near linear algorithms ([View Highlight](https://read.readwise.io/read/01hhc6zq14henz56fdxd4ftdhy))
- given any stepsize Delta Computing the state space model convolution filter Kar can be reduced to four Koshi multiplies requiring only Big O of n plus L operations ignoring logarithmic factors and Big O of n plus l space where again L is the sequence length and N is the state size empirically the proposed S4 architecture does very well on the long range Arena ([View Highlight](https://read.readwise.io/read/01hhc709zyb9xtwqevbddrv0k2))
- selection mechanism since previous state space models lack the ability to efficiently select data in an input dependent manner they design a simple selection mechanism
  by parameterizing the state space model parameters based on the input ([View Highlight](https://read.readwise.io/read/01hhc7359rzsvqh7ak8m3d826v))
- the second contribution is a hardware aware algorithm that computes the model recurrently with a scan instead of convolution this leads to an implementation that is faster than previous methods both in theory scaling linearly in sequence length compared to pseudolinear for all convolution based ssms ([View Highlight](https://read.readwise.io/read/01hhc73yj5d0mwtcx1dw1qr0h6))
- combining the design of Prior State space model architectures with the MLP block of Transformers into a single block leading to a simple and homogeneous architecture design called Mamba ([View Highlight](https://read.readwise.io/read/01hhc74rhqcd42bezx43d7pzcd))
- selective copying this time we have random spaces symbolized by the white blocks in between the input sequence elements to successfully copy the color outputs to the output while ignoring the white blocks we need a mechanism that behaves differently at different inputs ([View Highlight](https://read.readwise.io/read/01hhc79fpwh707ybn5h4hv748b))
- second task they look at is induction heads here in order to predict the appropriate color at the question mark block the model needs to be able to
  perform retrieval back over the input sequence based on the context provided by the black Square in order to predict that blue is the next color in the sequence ([View Highlight](https://read.readwise.io/read/01hhc7a3eh31cv22fs3n2mxtag))
- to allow the model to behave differently on different inputs b c and Delta are altered to be time
  varying they now depend on the input sequence ([View Highlight](https://read.readwise.io/read/01hhc7aqz52w1bvwtba35sca1z))
- can no longer use the efficient S4 convolution trick ([View Highlight](https://read.readwise.io/read/01hhc7b2jjvxatwe3tnn9vjw02))
- the authors develop a selective scan based on Hardware aware State expansion in effect the two big challenges to be tackled once we give up on convolution are the sequential nature of recurrence and the large memory usage ([View Highlight](https://read.readwise.io/read/01hhc7bdtbww4gwatj35dpqkvd))
- three techniques that come into play kernel Fusion parallel scan and recomputation ([View Highlight](https://read.readwise.io/read/01hhc7bm05yfpb8baf6pg8byjd))
- simplified State space layers for sequence modeling or S5 which highlighted the benefits of using parallel scans to maintain efficiency while avoiding the use of convolutional tricks used in S4 ([View Highlight](https://read.readwise.io/read/01hhc7c1mbj2jggqn6jd3r2bsm))
- instead of preparing the scan input in GPU high bandwidth memory they load the state space model parameters Direct from the slow high bandwidth memory to fast
  SRAM where they perform the discretization and recurrence then they write the final results back to high bandwidth memory last recomputation is used to reduce the memory requirements this allows them to avoid saving the intermediate states which are necessary for back propagation ([View Highlight](https://read.readwise.io/read/01hhc7d284r5zacnqynqjnzr5n))
- combine the Hungry Hungry Hippos block with a gated MLP block to produce their mber block the shapes here indic that the dimensionality is expanded inside the
  block this block is repeated and interleaved with standard normalization and residual connections to form the Mamba architecture ([View Highlight](https://read.readwise.io/read/01hhc7ehdejrb12e9s03vn5wy8))
- they use real values as the default which work well for all but one of their tasks ([View Highlight](https://read.readwise.io/read/01hhc7f9a3jkrg3mpqat4xhfyw))
- audio waveforms actually benefit from linear time invariant models which have a matching inductive bias ([View Highlight](https://read.readwise.io/read/01hhc7mb252be2ne452ret3tmd))
- inference throughput where higher is better we find that Mamba shown in blue and green can achieve five times higher throughput than Transformers benefiting from its recurrent nature ([View Highlight](https://read.readwise.io/read/01hhc7ncejwe72j9mxvmexz451))

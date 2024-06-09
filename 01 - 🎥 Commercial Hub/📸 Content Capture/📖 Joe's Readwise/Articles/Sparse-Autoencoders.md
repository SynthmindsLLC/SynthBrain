# Sparse-Autoencoders

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/181644072/j1UBEdcW16Z3zs39y9FhJn21HBTpxgo5DC_PecA30ig-cove_iQMm71d.png)

## Metadata
- Author: [[readwise.io]]
- Date: 2024-06-06
- Full Title: Sparse-Autoencoders
- Category: #articles
- Summary: The text discusses the challenges and techniques for training sparse autoencoders to balance reconstruction and sparsity objectives. The study demonstrates clean scaling laws and scalability when training a large number of latents. The use of TopK activation function in autoencoders shows improved performance on the sparsity-reconstruction frontier.
- URL: https://readwise.io/reader/document_raw_content/181644072

## Highlights
- Sparse autoencoders (SAEs) have shown great promise for finding features [Cunningham et al., 2023, Bricken et al., 2023, Templeton et al., 2024, Goh, 2016] and circuits [Marks et al., 2024] in language models. Unfortunately, they are difficult to train due to their extreme sparsity, so prior work has primarily focused on training relatively small sparse autoencoders on small language models. ([View Highlight](https://read.readwise.io/read/01hzwvcw384r6hc3zsyv19xzg2))
- we train a 16 million latent autoencoder on GPT-4 [OpenAI, 2023] residual stream activations. ([View Highlight](https://read.readwise.io/read/01hzwvdpsxv28erfj1nz72tb57))
- ![](https://readwise-assets.s3.amazonaws.com/media/reader/pub/0fcb17704ca9670302616a8475c24e74_b13CLWH.png?t=1717881506271) ([View Highlight](https://read.readwise.io/read/01hzwvepkp9363k9wsmywgn4b4))
- Our contributions: 1. In Section 2, we describe a state-of-the-art recipe for training sparse autoencoders. 2. In Section 3, we demonstrate clean scaling laws and scale to large numbers of latents. 3. In Section 4, we introduce metrics of latent quality and find larger sparse autoencoders are generally better according to these metrics. ([View Highlight](https://read.readwise.io/read/01hzwvfmk4gr4xvagv5wjejeer))
- We also release code, a full suite of GPT-2 small autoencoders, and a feature visualizer for GPT-2 small autoencoders and the 16 million latent GPT-4 autoencoder. ([View Highlight](https://read.readwise.io/read/01hzwvg91bxkfx5mryxkws36jm))
- ![](https://readwise-assets.s3.amazonaws.com/media/reader/pub/6267690d86ceb2044c0489005a3ee784_FrFSGC6.png?t=1717881586081) ([View Highlight](https://read.readwise.io/read/01hzwvhfvn2nhbgnk31vptdt8c))
- ![](https://readwise-assets.s3.amazonaws.com/media/reader/pub/33c27ed9001fc98d85d14bee1a7fad6e_kCKStq9.png?t=1717881612628) ([View Highlight](https://read.readwise.io/read/01hzwvhxg30cdfgrktmkgsy3rs))
- ![](https://readwise-assets.s3.amazonaws.com/media/reader/pub/195837f0842258bb7b8cbf62bf8bc366_XqrbX3S.png?t=1717881638363) ([View Highlight](https://read.readwise.io/read/01hzwvjytve6karx4hy3b57zna))

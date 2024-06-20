# Fine-Tuning LLMs: From a to Z!

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F145713265%2F359b6fcc-11eb-4f1c-b2c6-4048f46c57e0%2Ftranscoded-1718598192.png)

## Metadata
- Author: [[Damien Benveniste]]
- Date: None
- Full Title: Fine-Tuning LLMs: From a to Z!
- Category: #articles
- Summary: Fine-tuning LLMs involves training models on specialized datasets for specific tasks like language modeling and text classification. Models are trained using strategies like causal language modeling and masked language modeling to predict and reconstruct text sequences. Sequence prediction tasks can focus on generating specific types of sequences, like answers to questions, and may require different architectures for handling diverse data domains.
- URL: https://newsletter.theaiedge.io/p/fine-tuning-llms-from-a-to-z?r=2kuc99&utm_medium=ios&triedRedirect=true

## Highlights
- Fine-tuning a model means we continue the training on a specialized dataset for a specialized learning task. There might be many different learning tasks involved when we consider LLMs. For example:
  • For Language modeling
  • For Sentence prediction
  • For Text classification
  • For Token classification
  • For Text encoding
  • For Multimodal modeling ([View Highlight](https://read.readwise.io/read/01j0tdn8cpa5qeq8y46zez1304))
- There are typically two strategies for language modeling: causal language modeling and masked language modeling. ([View Highlight](https://read.readwise.io/read/01j0tdns6apqy5rdejvmps25sc))
- ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F724e60e6-0efa-406f-97b3-071bc9e47b21_1552x822.png) ([View Highlight](https://read.readwise.io/read/01j0tdnsw753fh87g9n0q69txy))
- With causal language modeling, we train the model to predict the next token in a sequence based on the previous tokens. We have two strategies to achieve this. First, we use as the labels the shifted input tokens by one token. ([View Highlight](https://read.readwise.io/read/01j0tdpfzwn9ydc2x36e3hfgdr))
- ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c3a3f5a-716e-4418-b6fd-2997aef3d8e8_1904x761.png) ([View Highlight](https://read.readwise.io/read/01j0tdpgtjdpkp9f0ncfawn8cn))
- Every token, up to the current token, is used to learn to predict the following token. The loss function is computed by comparing the prediction of the next tokens with the actual values of the next tokens. ([View Highlight](https://read.readwise.io/read/01j0tdpw3xjrxy0p4y36xkjwtd))
- The second aspect is the causal mask that ensures that only the previous and current tokens are used to predict the following token. In the training data, all the tokens are present, and without a causal mask, the model can use the tokens that happen later in the text to predict past tokens. ([View Highlight](https://read.readwise.io/read/01j0tdqch39cmwyedy8dpmy2fm))
- ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b22ecd9-e2df-42ba-923c-ac004d0ebc27_1857x1031.png) ([View Highlight](https://read.readwise.io/read/01j0tdqhd7mze44yrw5fj2n2qt))
- With masked language modeling, we remove some of the input tokens at random and use those masked tokens as label tokens. ([View Highlight](https://read.readwise.io/read/01j0tdqrpxqtq9bey369m0yn2c))
- ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F838ebb55-4359-4e2e-9d5c-405e4d6fb6e6_1914x761.png) ([View Highlight](https://read.readwise.io/read/01j0tdqxx3e3vd0bmthb1pxs6b))
- LLMs trained in a masked fashion are not as good at generating coherent texts, but they used to be used as pre-trained models for different learning tasks like text or token classification. That is why we often train them with an added classification token that has the role of capturing the vector representation of the whole input sequence to be used a input to a classifier. ([View Highlight](https://read.readwise.io/read/01j0tdr7zx5ds2vnk53189v9tq))
- ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1712af5f-eb0c-443f-8f38-7cbdc86d840b_1683x752.png) ([View Highlight](https://read.readwise.io/read/01j0tdrgf25jmh61mjc96wf7q3))
- The training process of sequence prediction can be very similar to that of language modeling, but the training data is somewhat different. It is composed of pairs [input sequence, output sequence] that capture the specific type of sequences we want the LLM to generate based on the input. For example, if we want the LLM to become good at answering questions, we are going to specifically show it pairs of [question, answer]. ([View Highlight](https://read.readwise.io/read/01j0tds6appk9z3jsf7eqb2m2r))
- ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0007d976-c26b-4404-b56e-e9fe94f26c67_708x731.png) ([View Highlight](https://read.readwise.io/read/01j0tds9e3h7zy900ph6r4jq33))
- One strategy to ensure that the model's attention is focused on the answers is to compute the loss function using only the predictions and label tokens associated with the output sequences we want the LLM to generate. ([View Highlight](https://read.readwise.io/read/01j0tdsktx4z0bgs4ybdn6wmk1))
- ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe26bd677-96d0-405d-be8f-bd94aaca0f4d_1878x827.png) ([View Highlight](https://read.readwise.io/read/01j0tdsn3ejnmzht27xe5ch54w))

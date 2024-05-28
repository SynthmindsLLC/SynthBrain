# Understanding Low Rank Adaptation (LoRA) in Fine-Tuning LLMs

![rw-book-cover](https://miro.medium.com/v2/resize:fit:768/1*nkLV6p5NWZgRKpvS74qVIQ.jpeg)

## Metadata
- Author: [[Matthew Gunton]]
- Date: 2024-05-24
- Full Title: Understanding Low Rank Adaptation (LoRA) in Fine-Tuning LLMs
- Category: #articles
- Summary: The blog post explains how LoRA helps fine-tune Large Language Models by using lower-rank weight updates. LoRA reduces the number of trainable weights, saving computational resources and time during model fine-tuning. This method has become popular for improving models in a cost-effective manner.
- URL: https://towardsdatascience.com/understanding-low-rank-adaptation-lora-in-fine-tuning-llms-d3dd283f1f0a

## Highlights
- There are multiple methods to fine-tune a model, but one of the most consistently popular currently is the LoRA method (short for Low Rank Adaptation) discussed in the [“LoRA: Low-Rank Adaptation of Large Language Models”](https://arxiv.org/pdf/2106.09685) paper. ([View Highlight](https://read.readwise.io/read/01hys5zgxkf176ynja2g934m8e))
- Practically all machine learning models store their weights as matrices. Consequently, having some understanding of linear algebra is helpful to get intuition on what is happening. ([View Highlight](https://read.readwise.io/read/01hys604nkfmj9evzahma77e24))
- ![](https://miro.medium.com/v2/resize:fit:700/1*KK0BZHzurtji5aT8CAOPoA.png) ([View Highlight](https://read.readwise.io/read/01hys60a0d7y54yd74zdjxrev3))
- the more rows, columns, or both that you have, the more data your matrix takes up. Sometimes, there exists a mathematical relationship between the rows and/or columns that can be used to reduce the space needed. This is similar to how a function takes up a lot less space to represent than holding all of the coordinate points it represents. ([View Highlight](https://read.readwise.io/read/01hys60qrfykrfk3x4h5m3sm6s))

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
## New highlights added May 30, 2024 at 7:48 AM
- See the example below for a matrix that can be reduced to just 1 row. This shows the original 3x3 matrix has a rank of 1. ([View Highlight](https://read.readwise.io/read/01hz3fmva2rywjnqcy1yrq1fem))
- ![](https://miro.medium.com/v2/resize:fit:700/1*CrssDMa-k-6Pl43I03U0zg.png) ([View Highlight](https://read.readwise.io/read/01hz3fmwqdk7y1dbthdp2a5x1c))
- When a matrix can be reduced like the above, we say that it has a lower rank than a matrix which cannot be reduced as such. Any matrix of a lower rank can be expanded back to the larger matrix like the below ([View Highlight](https://read.readwise.io/read/01hz3fncw4w2xgbqhxxh17ydcp))
- ![](https://miro.medium.com/v2/resize:fit:700/1*TsGbMuT7swCZlvxRoKQQkg.png) ([View Highlight](https://read.readwise.io/read/01hz3fndkebm3ehgrshedvtebf))
- To fine-tune a model, you need a quality dataset. For example, if you wanted to fine-tune a chat model on cars, you would need a dataset with thousands of high-quality dialogue turns about cars. ([View Highlight](https://read.readwise.io/read/01hz3fpqze482kaa43gg9dmbjs))
- After creating the data, you would then take those data and run them through your model to get an output for each. This output is then compared to the output expected in your dataset and we calculate the difference between the two. Typically, a function like cross entropy (which highlights the difference between 2 probability distributions) is used to quantify this difference. ([View Highlight](https://read.readwise.io/read/01hz3fq5rfzhzbwch2936v4ket))
- ![](https://miro.medium.com/v2/resize:fit:700/1*m0BsB54rNAAaZcG9AtPtLQ.png) ([View Highlight](https://read.readwise.io/read/01hz3fq72wmn43090yv5v8fbvf))
- We now take the loss and use it to modify the model weights. ([View Highlight](https://read.readwise.io/read/01hz3fqfkfb9smmmtprhrmx0p1))
- We take the weights and determine how we are going to change them so that they give us a better result in our loss function. We figure out how to adjust the weights by doing backpropagation. ([View Highlight](https://read.readwise.io/read/01hz3fqxt5xsb4x1k6yk8hez7v))
- we can fine-tune the model with a far smaller matrix than we would need to use if we were training it from scratch and not see any major loss of performance. ([View Highlight](https://read.readwise.io/read/01hz3frpy4q54ab3ts98v4a6aa))
- ![](https://miro.medium.com/v2/resize:fit:700/1*nZ6jwxhntrPoUNAvTSX-gw.png) ([View Highlight](https://read.readwise.io/read/01hz3frv2n39rwfjhv11d68gaa))
- . *h* is the value of the weight after fine-tuning. ([View Highlight](https://read.readwise.io/read/01hz3fs3h0v7e1jfbfn5ecfpb4))
- Wo and ΔW are the same from before, but the authors have created a new way to define ΔW. To find ΔW, the authors created 2 matrices: A and B. ([View Highlight](https://read.readwise.io/read/01hz3fss2kxwhqdcq4054zwf27))
- These dimensions are important because when we multiply A and B together, they will create a matrix with the exact same dimensions as ΔW. ([View Highlight](https://read.readwise.io/read/01hz3ft6k429cea2qejb50gv34))
- ![](https://miro.medium.com/v2/resize:fit:574/1*tqkkwtqg-2YKqXAuwAah6Q.png) ([View Highlight](https://read.readwise.io/read/01hz3ft8h9rwrj3c74re5rh80n))
- ![](https://miro.medium.com/v2/resize:fit:700/1*THk27k2ht01PDir1ee406w.png) ([View Highlight](https://read.readwise.io/read/01hz3fv645apq9vmmy4s9hxsdm))
- As each cell in the matrix contains a trainable weight, we see immediately why LoRA is so powerful: we have radically reduced the number of trainable weights we need to compute. ([View Highlight](https://read.readwise.io/read/01hz3fvq5fcn2cw4pj7wx060ct))

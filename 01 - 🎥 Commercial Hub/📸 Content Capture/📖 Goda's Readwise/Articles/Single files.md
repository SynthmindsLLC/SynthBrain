# Single files

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_178634/diffusers.png)

## Metadata
- Author: [[huggingface.co]]
- Full Title: Single files
- Category: #articles
- URL: https://huggingface.co/docs/diffusers/main/en/training/lora
- Tags:

## Highlights
- [LoRA (Low-Rank Adaptation of Large Language Models)](https://hf.co/papers/2106.09685) is a popular and lightweight training technique that significantly reduces the number of trainable parameters. ([View Highlight](https://read.readwise.io/read/01hpq1f66qg7apchw7ezft6320))
- It works by inserting a smaller number of new weights into the model and only these are trained. This makes training with LoRA much faster, memory-efficient, and produces smaller model weights (a few hundred MBs), which are easier to store and share. LoRA can also be combined with other training techniques like DreamBooth to speedup training. ([View Highlight](https://read.readwise.io/read/01hpq1frrsd2dx2xq127dh11dd))
- LoRA is very versatile and supported for [DreamBooth](https://github.com/huggingface/diffusers/blob/main/examples/dreambooth/train_dreambooth_lora.py), [Kandinsky 2.2](https://github.com/huggingface/diffusers/blob/main/examples/kandinsky2_2/text_to_image/train_text_to_image_lora_decoder.py), [Stable Diffusion XL](https://github.com/huggingface/diffusers/blob/main/examples/text_to_image/train_text_to_image_lora_sdxl.py), [text-to-image](https://github.com/huggingface/diffusers/blob/main/examples/text_to_image/train_text_to_image_lora.py), and [Wuerstchen](https://github.com/huggingface/diffusers/blob/main/examples/wuerstchen/text_to_image/train_text_to_image_lora_prior.py). ([View Highlight](https://read.readwise.io/read/01hpq1fzgpagaspv0pkpdh9n34))

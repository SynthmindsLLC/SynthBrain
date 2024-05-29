# Microsoft, Beihang Release MoRA, an Efficient LLM Fine-Tuning Technique

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2024/05/power-cube.jpg?w=1024?w=1200&strip=all)

## Metadata
- Author: [[Ben Dickson]]
- Date: 2024-05-28
- Full Title: Microsoft, Beihang Release MoRA, an Efficient LLM Fine-Tuning Technique
- Category: #articles
- Summary: Researchers from Microsoft and Beihang University have introduced MoRA, a new technique for fine-tuning large language models more efficiently. MoRA addresses limitations of popular techniques like LoRA and is especially useful for tasks requiring new knowledge acquisition. MoRA outperformed LoRA in memorization tasks and showed promise for continual pretraining in biomedical and financial domains.
- URL: https://venturebeat.com/ai/microsoft-beihang-release-mora-an-efficient-llm-fine-tuning-technique/

## Highlights
- Researchers from [Microsoft](https://www.microsoft.com/) and [Beihang University](https://www.buaa.edu.cn/) have introduced a new technique for fine-tuning large language models (LLMs) at a fraction of the cost it usually takes. ([View Highlight](https://read.readwise.io/read/01hz1sqj99nstq6jjrn1cxcggp))
- The new technique, called [MoRA](https://arxiv.org/abs/2405.12130v1), is a parameter-efficient fine-tuning (PEFT) technique that addresses some of the limitations of other popular techniques such as low-rank adaptation ([LoRA](https://bdtechtalks.com/2023/05/22/what-is-lora/)). MoRA is especially useful when you want to fine-tune the model on tasks that require the model to acquire new knowledge. With PEFT methods becoming increasingly popular in the enterprise, MoRA can become an important addition to the growing toolset of LLM application developers. ([View Highlight](https://read.readwise.io/read/01hz1sqzzrmphb9g4648x9te31))
- PEFT methods find the optimal subset of parameters that need to be modified to configure the model for the target task. ([View Highlight](https://read.readwise.io/read/01hz1ss2akj58v318jw12djqcx))
- while LoRA performs well on tasks such as text classification and instruction tuning, it struggles with more complex tasks that require enhancing the knowledge and capabilities of LLMs, such as [mathematical reasoning](https://venturebeat.com/ai/meet-llemma-the-math-focused-open-source-ai-that-outperforms-rivals/) and continual pre-training. ([View Highlight](https://read.readwise.io/read/01hz1ssyas2e1m02ptkbj1s84p))
- ![](https://venturebeat.com/wp-content/uploads/2024/05/LoRA-vs-MoRA.jpg) ([View Highlight](https://read.readwise.io/read/01hz1svz4sgy9keh231tmpj2kd))
- LoRA (left) uses low-rank matrices while MoRA (right) uses a single square matrix for parameter-efficient fine-tuning (source: [arxiv](https://arxiv.org/abs/2405.12130v1)) ([View Highlight](https://read.readwise.io/read/01hz1sw3agnr9x1ggm6dpcq9vh))
- MoRA, a PEFT technique that uses a square matrix instead of low-rank matrices. The main idea behind MoRA is to use trainable parameters in a way that achieves the highest possible rank in the space of the model’s original dimensions. ([View Highlight](https://read.readwise.io/read/01hz1swgs72pvydjbh2ev5tp0n))
- the input and output dimensions of the MoRA adapter do not match those of the original model, which makes it impossible to combine them in the same matrix multiplication operation. To bridge this gap, the researchers developed a compression/decompression function that transforms inputs between the two spaces. This algorithm allows MoRA to be easily plugged into LLMs of different sizes. ([View Highlight](https://read.readwise.io/read/01hz1sx1fjtzxfzqhax2kng8a4))
- The researchers compared equally sized LoRA and MoRA models on various tasks and settings. On memorization tasks, MoRA significantly outperformed LoRA and came much closer to the performance of a fully fine-tuned model with fewer parameters and training steps. ([View Highlight](https://read.readwise.io/read/01hz1sxkt296791yw5872kv5qx))
- for continual pretraining in biomedical and financial domains, MoRA outperformed LoRA, benefiting from its high-rank updating to memorize new knowledge. ([View Highlight](https://read.readwise.io/read/01hz1syc23at84301chxrpa7pm))
- The researchers also found that increasing the rank of the MoRA adapter can eliminate the performance gap between PEFT and full fine-tuning in mathematical reasoning tasks, though it comes at higher training and storage costs. ([View Highlight](https://read.readwise.io/read/01hz1sykrazfyq5kb2j6ja8zx6))
- The researchers at Microsoft and Beihang have released an [open-source implementation](https://github.com/kongds/MoRA) of MoRA, which is compatible with LoRA. This can turn out to be an important tool for enterprise applications that want to add new knowledge to base models. ([View Highlight](https://read.readwise.io/read/01hz1szqv9hbk6p95rmec3xhgc))

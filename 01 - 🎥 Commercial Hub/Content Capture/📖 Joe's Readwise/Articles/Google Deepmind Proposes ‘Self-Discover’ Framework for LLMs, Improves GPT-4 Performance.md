# Google Deepmind Proposes ‘Self-Discover’ Framework for LLMs, Improves GPT-4 Performance

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2024/02/a_robot_looking_at_itself_in_the_mirror_illustr-e1707330384483.jpg?w=1200&strip=all)

## Metadata
- Author: [[Shubham Sharma]]
- Date: 2024-02-08
- Full Title: Google Deepmind Proposes ‘Self-Discover’ Framework for LLMs, Improves GPT-4 Performance
- Category: #articles
- Summary: Researchers from Google Deepmind and the University of Southern California have proposed a 'self-discover' prompting framework to enhance the reasoning capabilities of large language models (LLMs). This approach goes beyond existing prompting techniques used by LLMs and has been found to improve the performance of known models, including OpenAI's GPT-4 and Google's PaLM 2. The framework involves LLMs self-discovering task-intrinsic reasoning structures to solve problems, looking at multiple atomic reasoning modules and composing them into an explicit reasoning structure for LLMs to follow. The approach also requires 10 to 40 times less inference compute, making it efficient for enterprises.
- URL: https://venturebeat.com/ai/google-deepmind-proposes-self-discover-framework-for-llms-improves-gpt-4-performance/

## Highlights
- In a bid to enhance the reasoning capabilities of [large language models](https://venturebeat.com/ai/whats-next-in-large-language-model-llm-research-heres-whats-coming-down-the-ml-pike/) (LLMs), researchers from [Google Deepmind](https://deepmind.google/) and [University of Southern California](https://www.usc.edu/) have proposed a new ‘self-discover’ prompting framework. ([View Highlight](https://read.readwise.io/read/01hp42xekpqgqtsh6r2d4ar9s4))
- Self-discover substantially improves GPT-4 and PaLM 2’s performance on challenging reasoning benchmarks such as BigBench-Hard, grounded agent reasoning and MATH by as much as 32% compared to Chain of Thought (CoT),” the researchers write in the paper. ([View Highlight](https://read.readwise.io/read/01hp42y1agra0zjd3kj71t0sbj))
- LLMs self-discovering task-intrinsic reasoning structures to solve a problem. The models look at multiple atomic reasoning modules, such as critical thinking and step-by-step thinking, and compose them into an explicit reasoning structure for LLMs to follow during decoding. ([View Highlight](https://read.readwise.io/read/01hp42ygds5sed01axa6xqp750))
- Self-discover is inspired by how humans internally devise a reasoning program for problem-solving. From a set of atomic reasoning modules described in natural language such as ‘break down into sub-tasks’ and ‘critical thinking’, an LLM, and task examples without labels, it composes a coherent reasoning structure intrinsic to the task (Stage1) and then solves instances of the task using the discovered structure (Stage2). Stage 1 operates at the task level and uses three actions to guide the LLM to generate a reasoning structure for the task. At Stage 2, during the final decoding, the LLM simply follows the self-discovered structure to arrive at the final answer,” the researchers explain ([View Highlight](https://read.readwise.io/read/01hp431tgj6pw2brzn6632nmcx))

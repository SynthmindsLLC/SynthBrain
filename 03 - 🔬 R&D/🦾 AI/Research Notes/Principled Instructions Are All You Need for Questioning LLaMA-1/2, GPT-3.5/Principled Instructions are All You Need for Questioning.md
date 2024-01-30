---
Publish Year: "2023"
Authors: Sondos Mahmoud Bsharat, Aidar Myrzakhan, Zhiqiang Shen
URL: http://arxiv.org/abs/2312.16171
Zotero Link: zotero://select/library/items/PJKV6I97
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - PromptEngineering
Published:
---
# Summary
## Purpose
The paper "Principled Instructions are All You Need for Questioning" aims to explore how structured and principled instructions can enhance the performance of large language models (LLMs) in generating responses, particularly in the context of question-answering tasks.

## Methods
The authors investigate various prompt engineering techniques that influence the behavior of LLMs. These include:

- Ask-Me-Anything prompting, which uses multiple imperfect prompts and aggregates them.
- Chain-of-Thought method, where the model generates intermediate reasoning steps.
- Least-to-most prompting, a strategy to break down complex problems into simpler subproblems.
- Directional Stimulus Prompting, a framework using a policy model to generate auxiliary prompts.

## Key Findings
- Larger models have a significant capacity for simulation, and their performance improves with more precise tasks and directives.
- Prompt engineering can dramatically influence the performance and outputs of LLMs.
- Techniques like Chain-of-Thought and least-to-most prompting can significantly enhance the model's capability to tackle challenging problems.

## Discussion
The authors discuss the importance of prompt design principles such as:

- Conciseness and Clarity: Prompts should be concise and specific to guide the model effectively.
- Contextual Relevance: Including relevant context and domain-specific terminology in prompts.
- Task Alignment: Using language and structure in the prompt that clearly indicates the task.
- Example Demonstrations: Including examples within the prompt for complex tasks.
- Avoiding Bias: Designing prompts to minimize the activation of biases inherent in the model.
- Incremental Prompting: Structuring prompts to guide the model through a process incrementally.

## Critiques
The paper does not provide specific critiques, but it is implied that the effectiveness of prompt engineering is contingent on the careful application of the discussed principles.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Computation-and-Language
- #PromptEngineering

# Annotations
![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/bsharatPrincipledInstructionsAre2023/image-2-x127-y382.png]]



Our findings indicate that larger models possess a considerable capacity for simulation. The more precise the task or directive provided, the more effectively the model performs, aligning its responses more closely with our expectations.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/H55PKFSZ?page=2&annotation=VGWMPC3Y)



Early explorations, such as those by [19], delved into how varying prompt designs could dramatically influence the performance and outputs of language models, marking the birth of prompt engineering.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/H55PKFSZ?page=3&annotation=W2U3DQSG)



Ask-Me-Anything [1] prompting introduced focusing on using multiple imperfect prompts and aggregating them to improve model performance, particularly in questionanswering formats.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/H55PKFSZ?page=4&annotation=7D3K67XF)



Chain-of-Thought method [23], where the model generates a series of intermediate reasoning steps to improve performance on complex tasks.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/H55PKFSZ?page=4&annotation=5I992PBM)



least-to-most prompting [26] a novel strategy to break down complex problems into simpler subproblems, significantly enhancing the model’s capability to tackle more challenging problems than those presented in the prompts.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/H55PKFSZ?page=4&annotation=42XM667B)



Directional Stimulus Prompting [12] presents a novel framework that uses a tunable policy model to generate auxiliary prompts, guiding LLMs towards specific desired outcomes.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/H55PKFSZ?page=4&annotation=7JZ2AFMW)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/bsharatPrincipledInstructionsAre2023/image-5-x96-y143.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/bsharatPrincipledInstructionsAre2023/image-6-x93-y119.png]]



Conciseness and Clarity: Generally, overly verbose or ambiguous prompts can confuse the model or lead to irrelevant responses. Thus, the prompt should be concise, avoiding unnecessary information that does not contribute to the task while being specific enough to guide the model. This is the basic principle guidance for prompt engineering.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/H55PKFSZ?page=7&annotation=8G9WVFTK)



Contextual Relevance: The prompt must provide relevant context that helps the model understand the background and domain of the task. Including keywords, domain-specific terminology, or situational descriptions can anchor the model’s responses in the correct context. We highlight this design philosophy in our presented principles.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/H55PKFSZ?page=7&annotation=JK8U3F3U)



Task Alignment: The prompt should be closely aligned with the task at hand, using language and structure that clearly indicate the nature of the task to the model. This may involve phrasing the prompt as a question, a command, or a fill-in-the-blank statement that fits the task’s expected input and output format.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/H55PKFSZ?page=7&annotation=86PV9I4P)



Example Demonstrations: For more complex tasks, including examples within the prompt can demonstrate the desired format or type of response. This often involves showing input-output pairs, especially in “few-shot” or “zero-shot” learning scenarios.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/H55PKFSZ?page=7&annotation=HGVK5KY5)



Avoiding Bias: Prompts should be designed to minimize the activation of biases inherent in the model due to its training data. Use neutral language and be mindful of potential ethical implications, especially for sensitive topics.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/H55PKFSZ?page=7&annotation=YK2PMVPE)



Incremental Prompting: For tasks that require a sequence of steps, prompts can be structured to guide the model through the process incrementally. Break down the task into a series of prompts that build upon each other, guiding the model step-by-step.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/H55PKFSZ?page=7&annotation=I52AB3XY)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/bsharatPrincipledInstructionsAre2023/image-10-x121-y472.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/bsharatPrincipledInstructionsAre2023/image-13-x146-y397.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/bsharatPrincipledInstructionsAre2023/image-13-x146-y132.png]]




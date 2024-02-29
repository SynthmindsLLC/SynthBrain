---
Publish Year: "2024"
Authors: Pei Zhou, Jay Pujara, Xiang Ren, Xinyun Chen, Heng-Tze Cheng, Quoc V. Le, Ed H. Chi, Denny Zhou, Swaroop Mishra, Huaixiu Steven Zheng
URL: http://arxiv.org/abs/2402.03620
Zotero Link: zotero://select/library/items/54V5HTV8
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#reasoning"
Published:
---
# Summary
## Purpose
- The research was initiated to address the challenge of how large language models (LLMs) can more effectively solve complex tasks by developing intrinsic reasoning structures, which is a significant issue in the field of Computer Science, particularly in Artificial Intelligence. The purpose of the study was to introduce and evaluate a new approach, SELF-DISCOVER, that allows LLMs to internally devise a reasoning program for problem-solving, akin to human problem-solving strategies.

## Methods
- The SELF-DISCOVER approach involves two stages:
  - Stage 1: Task-level operation where the LLM uses three actions (SELECT, ADAPT, and IMPLEMENT) to generate a reasoning structure for the task.
  - Stage 2: The LLM follows the self-discovered structure to arrive at the final answer during the final decoding.

## Key Findings
- SELF-DISCOVER achieves superior performance against other inference-heavy methods such as CoT + Self-Consistency and majority voting, while requiring significantly less computational resources (10-40x fewer).
- The approach performs best on tasks requiring diverse world knowledge and shows a moderate performance boost on algorithmic tasks compared to Chain-of-Thought (CoT) prompting.
- The discovered reasoning structure is intrinsic to the task and provides insights about the task in a more interpretable way than optimized prompts.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on the field of Artificial Intelligence and Computation and Language. It suggests that SELF-DISCOVER not only enhances the performance of LLMs in complex problem-solving but also offers a more interpretable and efficient way to understand the reasoning process of these models. This contributes to the field by providing a novel method for improving LLMs' problem-solving capabilities and potentially reducing the computational resources required for such tasks.

## Critiques
Upon evaluating the research, some critiques include:
- The effectiveness of SELF-DISCOVER may vary depending on the nature of the task, with different performance boosts observed for world knowledge tasks versus algorithmic tasks.
- The generalizability of the findings may be limited to the specific types of tasks and reasoning modules tested in the study.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Computation-and-Language
- #reasoning
- #large-language-models
- #problem-solving
- #SELF-DISCOVER-method

# Annotations
a fundamental limitation is that each technique itself serves as an atomic reasoning module making an implicit prior assumption of the process on how to tackle a given task. Instead, we argue that each task has a unique intrinsic structure underlying the reasoning process involved in solving it efficiently. For instance, least-to-most prompting (Zhou et al., 2022a; Drozdov et al., 2022) has shown to be much more effective than CoT (Wei et al., 2022) at solving tasks such as symbolic manipulation and compositional generalization, due to the decomposition structure of the tasks.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/386SP7QX?page=1&annotation=IY9LGM4K)



Our approach, SELF-DISCOVER, is inspired by how humans internally devise a reasoning program for problem-solving” Yellow Highlight [Page 1](zotero://open-pdf/library/items/386SP7QX?page=1&annotation=CL7MTXIR)



breakdown into sub tasks” and “critical thinking”,” Yellow Highlight [Page 1](zotero://open-pdf/library/items/386SP7QX?page=1&annotation=Q4PDMWZ8)



Stage 1 operates at the tasklevel and uses three actions to guide the LLM to generate a reasoning structure for the task. At Stage 2, during the final decoding, the LLM simply follows the self-discovered structure to arrive at the final answer.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/386SP7QX?page=1&annotation=QFR7M337)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhouSelfDiscoverLargeLanguage2024/image-2-x92-y518.png]]



Lastly, the discovered reasoning structure is intrinsic to the task, and conveys LLMs’ insights about the task in a more interpretable way than the optimized prompts” Yellow Highlight [Page 2](zotero://open-pdf/library/items/386SP7QX?page=2&annotation=QB5KH2BV)



SELF-DISCOVER achieves superior performance against inference-heavy methods such as CoT + Self-Consistency and majority voting of every module while requiring 10-40x fewer inference compute” Yellow Highlight [Page 2](zotero://open-pdf/library/items/386SP7QX?page=2&annotation=KDDUYXBL)



we find that SELF-DISCOVER performs best on tasks requiring world knowledge and has a moderate performance boost on algorithmic tasks compared to CoT” Yellow Highlight [Page 2](zotero://open-pdf/library/items/386SP7QX?page=2&annotation=9DHTMPWD)



Given a task and a set of reasoning module descriptions representing high-level problem-solving heuristics such as “Use critical thinking” and “Let’s think step by step”, Stage 1 of SELF-DISCOVER aims to uncover the intrinsic reasoning structure for solving this task via meta-reasoning.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/386SP7QX?page=2&annotation=EVKT5H7D)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhouSelfDiscoverLargeLanguage2024/image-3-x71-y569.png]]



The first stage consists of three actions: 1) SELECT, where relevant reasoning modules for task-solving are chosen from the set of reasoning module descriptions; 2) ADAPT, where descriptions of selected reasoning modules are rephrased to be more specific to the task at hand; and 3) IMPLEMENT, where the adapted reasoning descriptions are implemented into a structured actionable plan so that the task can be solved by following the structure.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/386SP7QX?page=3&annotation=ZT7D43GQ)



First, not every reasoning module is helpful for every task, so the first stage of SELF-DISCOVER guides model to select modules that are useful based on task examples. For example, “reflective thinking” might help search for first-principle theories on science problems, while “creative thinking” helps on generating a novel continuation to a story. Given raw set of reasoning module descriptions D such as “critical thinking”, and “break the problem into sub-problems”” Yellow Highlight [Page 3](zotero://open-pdf/library/items/386SP7QX?page=3&annotation=GTSJQRIZ)



Since each reasoning module provides a general description of how to solve problems, the next step of SELFDISCOVER aims at tailoring each selected module to the task at hand. For example, from “break the problem into subproblems” to “calculate each arithmetic operation in order” for arithmetic problems.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/386SP7QX?page=3&annotation=GQW34872)



Finally, given the adapted reasoning module descriptions DA, SELF-DISCOVER operationalizes the reasoning modules into an implemented reasoning structure DI with specified instruction on what to generate for each step.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/386SP7QX?page=3&annotation=7ZVYHBV3)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhouSelfDiscoverLargeLanguage2024/image-4-x51-y527.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhouSelfDiscoverLargeLanguage2024/image-5-x49-y536.png]]



SELF-DISCOVER performs best on tasks that require diverse world knowledge. Figure 4 presents the average improvement in terms of delta in accuracy of SELFDISCOVER over direct answer and CoT on 4 categories of reasoning tasks we test. We adopt the categorization from Suzgun et al. (2022).” Yellow Highlight [Page 5](zotero://open-pdf/library/items/386SP7QX?page=5&annotation=4VEWZR9Z)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhouSelfDiscoverLargeLanguage2024/image-7-x51-y395.png]]



Recent advancements in the area of LLMs have given rise to a plethora of few-shot (Brown et al., 2020) and instruction (Mishra et al., 2022c; Wei et al., 2021; Ouyang et al., 2022) prompting techniques, including Chain-of-Thought prompting (CoT) (Nye et al., 2021; Wei et al., 2022), Leastto-most prompting (Zhou et al., 2022a; Drozdov et al., 2022), Decomposed prompting (Khot et al., 2022), Reframing (Mishra et al., 2022b), Help Me Think Prompting (Mishra & Nouri, 2023), Stepback Prompting (Zheng et al., 2023) and search-based approaches like Tree-ofThought (ToT) (Yao et al., 2023a), Graph-of-Thought (Besta et al., 2023; Yao et al., 2023b), Branch-solve-merge (Saha et al., 2023) and RAP (Hao et al., 2023). E” Yellow Highlight [Page 8](zotero://open-pdf/library/items/386SP7QX?page=8&annotation=DUHBZISB)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhouSelfDiscoverLargeLanguage2024/image-12-x43-y318.png]]



Reasoning Modules 1 How could I devise an experiment to help solve that problem? 2 Make a list of ideas for solving this problem, and apply them one by one to the problem to see if any progress can be made.  3 How could I measure progress on this problem? 4 How can I simplify the problem so that it is easier to solve? 5 What are the key assumptions underlying this problem? 6 What are the potential risks and drawbacks of each solution? 7 What are the alternative perspectives or viewpoints on this problem? 8 What are the long-term implications of this problem and its solutions? 9 How can I break down this problem into smaller, more manageable parts? 10 Critical Thinking: This style involves analyzing the problem from different perspectives, questioning assumptions, and evaluating the evidence or information available. It focuses on logical reasoning, evidence-based decision-making, and identifying potential biases or flaws in thinking.  11 Try creative thinking, generate innovative and out-of-the-box ideas to solve the problem. Explore unconventional solutions, thinking beyond traditional boundaries, and encouraging imagination and originality.  12 Seek input and collaboration from others to solve the problem. Emphasize teamwork, open communication, and leveraging the diverse perspectives and expertise of a group to come up with effective solutions.  13 Use systems thinking: Consider the problem as part of a larger system and understanding the interconnectedness of various elements.  Focuses on identifying the underlying causes, feedback loops, and interdependencies that influence the problem, and developing holistic solutions that address the system as a whole.  14 Use Risk Analysis: Evaluate potential risks, uncertainties, and tradeoffs associated with different solutions or approaches to a problem. Emphasize assessing the potential consequences and likelihood of success or failure, and making informed decisions based on a balanced analysis of risks and benefits.  15 Use Reflective Thinking: Step back from the problem, take the time for introspection and self-reflection. Examine personal biases, assumptions, and mental models that may influence problem-solving, and being open to learning from past experiences to improve future approaches.  16 What is the core issue or problem that needs to be addressed? 17 What are the underlying causes or factors contributing to the problem? 18 Are there any potential solutions or strategies that have been tried before? If yes, what were the outcomes and lessons learned? 19 What are the potential obstacles or challenges that might arise in solving this problem? 20 Are there any relevant data or information that can provide insights into the problem? If yes, what data sources are available, and how can they be analyzed? 21 Are there any stakeholders or individuals who are directly affected by the problem? What are their perspectives and needs? 22 What resources (financial, human, technological, etc.) are needed to tackle the problem effectively? 23 How can progress or success in solving the problem be measured or evaluated? 24 What indicators or metrics can be used? 25 Is the problem a technical or practical one that requires a specific expertise or skill set? Or is it more of a conceptual or theoretical problem? 26 Does the problem involve a physical constraint, such as limited resources, infrastructure, or space? 27 Is the problem related to human behavior, such as a social, cultural, or psychological issue? 28 Does the problem involve decision-making or planning, where choices need to be made under uncertainty or with competing objectives? 29 Is the problem an analytical one that requires data analysis, modeling, or optimization techniques? 30 Is the problem a design challenge that requires creative solutions and innovation? 31 Does the problem require addressing systemic or structural issues rather than just individual instances? 32 Is the problem time-sensitive or urgent, requiring immediate attention and action? 33 What kinds of solution typically are produced for this kind of problem specification? 34 Given the problem specification and the current best solution, have a guess about other possible solutions.  35 Let’s imagine the current best solution is totally wrong, what other ways are there to think about the problem specification? 36 What is the best way to modify this current best solution, given what you know about these kinds of problem specification? 37 Ignoring the current best solution, create an entirely new solution to the problem.  38 Let’s think step by step.  39 Let’s make a step by step plan and implement it with good notion and explanation.” Yellow Highlight [Page 13](zotero://open-pdf/library/items/386SP7QX?page=13&annotation=GA6A5UKJ)




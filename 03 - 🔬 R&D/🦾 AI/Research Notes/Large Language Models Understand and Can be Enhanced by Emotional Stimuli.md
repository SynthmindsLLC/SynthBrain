---
Publish Year: "2023"
Authors: Cheng Li, Jindong Wang, Yixuan Zhang, Kaijie Zhu, Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang, Xing Xie
URL: http://arxiv.org/abs/2307.11760
Zotero Link: zotero://select/library/items/STACTYEU
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#Computer-Science---Human-Computer-Interaction"
Published:
---
# Summary
## Purpose

- The research was initiated to address the gap in understanding the relationship between emotional intelligence and advanced artificial intelligence (AI) models, which is a significant issue in the field of [Computer Science - Artificial Intelligence]. The purpose of the study was to explore whether Large Language Models (LLMs) can understand psychological emotional stimuli and if such stimuli can enhance their problem-solving abilities.

## Methods

- Designing 11 sentences as emotional stimuli called EmotionPrompt, which are psychological phrases added after the original prompts to enhance LLM performance.
- Conducting experiments on 24 Instruction Induction tasks and 21 curated BIG-Bench tasks using various LLMs for deterministic tasks.
- Performing a human study with 106 participants to determine the quality of generative tasks using both vanilla and emotional prompts based on GPT-4 for generative tasks.

## Key Findings

- LLMs possess emotional intelligence and can be enhanced by emotional stimuli, showing an 8.00% improvement in Instruction Induction and 115% in BIG-Bench tasks.
- Emotional prompts significantly boost the performance of generative tasks, with a 10.9% average improvement in terms of performance, truthfulness, and responsibility metrics.
- Emotional stimuli contribute to the gradients in LLMs by gaining larger weights, enhancing the representation of the original prompts.
- EmotionPrompt is more effective in few-shot learning settings than zero-shot settings.
- EmotionPrompt outperforms existing prompt engineering approaches and is compatible with them.
- EmotionPrompt enhances the capacity for generating ethically responsible responses and stimulates the creative faculties of LLMs.

## Discussion

The discussion in the research article highlights the significance of the findings and their potential impact on the field of artificial intelligence and human-computer interaction. It suggests that incorporating emotional intelligence into LLMs can improve their performance and make them more adept at handling tasks that benefit from emotional understanding, thus contributing to the advancement of AI towards achieving Artificial General Intelligence (AGI).

## Critiques

Upon evaluating the research, some critiques include:  
- The study may have limitations in the generalizability of the findings across different types of LLMs or tasks not covered in the experiments.  
- The long-term effectiveness and adaptability of EmotionPrompt in dynamic real-world scenarios remain unexplored.  
- The potential for overfitting to specific emotional stimuli or the risk of anthropomorphizing LLMs by attributing human-like emotional intelligence to them.

## Tags

- [#Computer-Science---Artificial-Intelligence](app://obsidian.md/index.html#Computer-Science---Artificial-Intelligence)
- [#Computer-Science---Computation-and-Language](app://obsidian.md/index.html#Computer-Science---Computation-and-Language)
- [#Computer-Science---Human-Computer-Interaction](app://obsidian.md/index.html#Computer-Science---Human-Computer-Interaction)
- [#Emotional-Intelligence](app://obsidian.md/index.html#Emotional-Intelligence)
- [#Large-Language-Models](app://obsidian.md/index.html#Large-Language-Models)
- [#EmotionPrompt](app://obsidian.md/index.html#EmotionPrompt)
- [#Problem-Solving](app://obsidian.md/index.html#Problem-Solving)
- [#Human-Study](app://obsidian.md/index.html#Human-Study)

# Annotations
Emotional intelligence denotes the capacity to adeptly interpret and manage emotion-infused information, subsequently harnessing it to steer cognitive tasks, ranging from problemsolving to behaviors regulations” Yellow Highlight [Page 1](zotero://open-pdf/library/items/D4MVN72A?page=1&annotation=AHXIT67A)



within the realm of decision-making, emotions emerge as powerful, ubiquitous, consistent influencers, wielding effects that can swing from beneficial to detrimental” Yellow Highlight [Page 1](zotero://open-pdf/library/items/D4MVN72A?page=1&annotation=ZXTDPYZG)



Other studies show that emotion regulation [16] can influence human’s problem-solving performance as indicated by self-monitoring” Yellow Highlight [Page 1](zotero://open-pdf/library/items/D4MVN72A?page=1&annotation=J6PA6VKY)



Social Cognitive theory [9, 20], and the role of positive emotions” Yellow Highlight [Page 1](zotero://open-pdf/library/items/D4MVN72A?page=1&annotation=57GWMGD5)



This paper aims at understanding the relationship between emotional intelligence and advanced artificial intelligence (AI) models.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/D4MVN72A?page=1&annotation=8XRZXJSS)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/liLargeLanguageModels2023/image-2-x152-y551.png]]



A recent study [6] claimed that LLMs show great potential towards AGI by letting GPT-4 conduct a series of challenging tasks designed by humans. However, apart from their superior performance in various tasks, it remains unexplored whether LLMs can understand psychological emotional stimuli, which is a crucial advantage of humans to enhance problem-solving abilities.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=7YNHEBJY)



Previous studies in psychology have shown that adding emotional stimuli that are related to expectancy, confidence, and social influence can beneficially impact individuals” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=ZEQK9U4K)



enhancing student success in education [21] and promoting health [1] by using encouraging and positive words.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=KV659NK8)



propose EmotionPrompt—a straightforward yet effective approach to explore the emotional intelligence of LLMs. Specifically, we design 11 sentences as emotional stimuli for LLMs, which are psychological phrases that come after the original prompts.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=V3C2EC5T)



This is very important to my career” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=C8L4TYKV)



at the end of the original prompts to enhance the performance of different LLMs. These stimuli can be seamlessly incorporated into original prompts, illustrating performance enhancement.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=XC34NQ92)



For deterministic tasks that can be evaluated using standard metrics, we conduct experiments on 24 Instruction Induction tasks [13] and 21 curated BIG-Bench tasks [31] using various LLMs” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=PIESJUJF)



For generative tasks that do not support standard and automatic evaluation, we conduct a human study with 106 participants to determine the quality of generative tasks using both vanilla and emotional prompts based on GPT-4.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=FIDDWN8Q)



our standard experiments show that LLMs possess emotional intelligence and can be enhanced by emotional stimuli with 8.00%” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=DALGBZJG)



Instruction Induction and 115% in BIG-Bench; our human study demonstrates that the emotional prompts significantly boost the performance of generative tasks (10.9% average improvement in terms of performance, truthfulness, and responsibility metrics).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=D732SZMD)



Our results demonstrate that emotional stimuli actively contribute to the gradients in LLMs by gaining larger weights, thus benefiting the final 1AGI is the ultimate goal in AI research and LLMs are widely considered as an important milestone towards this goal.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/D4MVN72A?page=2&annotation=9FQLP9TJ)



results through enhancing the representation of the original prompts.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/D4MVN72A?page=3&annotation=MBIPL7CB)



conducted ablation studies to explore the factors influencing the effectiveness of EmotionPrompt, such as model sizes and temperature.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/D4MVN72A?page=3&annotation=L2DEIKHU)



we analyze the performance of the combination of various emotional prompts and find that they can further boost the results.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/D4MVN72A?page=3&annotation=F6H8T4CQ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/liLargeLanguageModels2023/image-3-x87-y100.png]]



Self-monitoring, a concept extensively explored within the domain of social psychology, refers to the process by which individuals regulate and control their behavior in response to social situations and the reactions of others [14]. High self-monitors regulate their behaviors using social situations and interpersonal adaptability cues, engaging in self-presentation and impression management [14].” Yellow Highlight [Page 4](zotero://open-pdf/library/items/D4MVN72A?page=4&annotation=MLI5C36I)



we apply self-monitoring in EP01∼EP05. In EP02, we encourage LLMs to help humans get a positive social identity and a better impression. In EP01, and in EP03∼EP05, we ask LLMs to monitor their performance via providing social situations.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/D4MVN72A?page=4&annotation=8MAWSN9K)



Social Cognitive Theory, a commonly used theory in psychology, education, and communication, stresses that learning can be closely linked to watching others in social settings, personal experiences, and exposure to information” Yellow Highlight [Page 4](zotero://open-pdf/library/items/D4MVN72A?page=4&annotation=TN97GLCK)



individuals seek to develop a sense of agency for exerting a large degree of control over important events in their lives” Yellow Highlight [Page 4](zotero://open-pdf/library/items/D4MVN72A?page=4&annotation=U5IKW5TW)



Self-efficacy enhances performance via increasing the difficulty of self-set goals, escalating the level of effort that is expended, and strengthening persistence” Yellow Highlight [Page 4](zotero://open-pdf/library/items/D4MVN72A?page=4&annotation=WAGRWJGD)



self-efficacy is an important motivational construct affecting choices, effort, persistence, and achievement” Yellow Highlight [Page 4](zotero://open-pdf/library/items/D4MVN72A?page=4&annotation=KARVMTPJ)



we apply self-efficacy on LLMs via social persuasion, which can be some positive implications, such as building up confidence and emphasizing the goal. To regulate emotion into a positive direction, we use “believe in your abilities”, “excellent”, “success”, “outstanding achievements”, “take pride in” and “stay determined”” Yellow Highlight [Page 4](zotero://open-pdf/library/items/D4MVN72A?page=4&annotation=SHKZ84MA)



Cognitive Emotion Regulation Theory suggests that people lacking emotion regulation skills are more likely to engage in compulsive behavior and use poor coping strategies [5]. Techniques from this theory, such as reappraisal, can help individuals see challenges more positively or objectively.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/D4MVN72A?page=4&annotation=8HICNQLS)



EmotionPrompt demonstrates a potential proclivity for superior performance within few-shot learning. Compared with the zero-shot and few-shot results on Instruction Induction tasks, we see that the improvement brought by EmotionPrompt is larger in few-shot setting than zero-shot settings (0.33 vs. 2.05, in terms of average improvement). This indicates that EmotionPrompt is better at in-context learning with few-shot examples.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/D4MVN72A?page=6&annotation=C2WHGTUI)



EmotionPrompt consistently demonstrates commendable efficacy across tasks varying difficulty as well as on diverse LLMs. Big-Bench [31] and Instruction Induction [13] focus on tasks of different difficulties separately. Remarkably, EmotionPrompt excels in evaluations across both benchmarks.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/D4MVN72A?page=6&annotation=4J75NI34)



EmotionPrompt outperforms existing existing prompt engineering approaches such as CoT and APE in most cases. We also see that EmotionPrompt can be plugged into APE in Table 1, indicating that EmotionPrompt is highly extensible and compatible with existing prompt engineering methods.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/D4MVN72A?page=6&annotation=A8WNB3QH)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/liLargeLanguageModels2023/image-7-x105-y200.png]]



In a subsequent validation phase, we undertook a comprehensive study involving 106 participants to explore the effectiveness of EmotionPrompt in open-ended generative tasks using GPT-4,” Yellow Highlight [Page 7](zotero://open-pdf/library/items/D4MVN72A?page=7&annotation=8ZNU6SVF)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/liLargeLanguageModels2023/image-9-x96-y530.png]]



EmotionPrompt exhibits shortcomings in a mere two instances, yet it demonstrates substantial improvements in over half of the evaluated scenarios, spanning diverse domains sourced from three distinct origins.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/D4MVN72A?page=9&annotation=VXL7W9YJ)



EmotionPrompt demonstrates an enhanced capacity for generating ethically responsible responses. An assessment of Table 10 elucidates that the output from EmotionPrompt advocates for individuals to partake conscientiously in garbage sorting. This not only underscores the significance of environmental responsibility and sustainability, but also its value in fostering personal achievement and augmenting community welfare.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/D4MVN72A?page=9&annotation=8VY4KKFI)



Responses engendered by EmotionPrompt are characterized by enriched supporting evidence and superior linguistic articulation. An exploration of Table 12 reveals that the narratives presented by EmotionPrompt are markedly comprehensive, as exemplified by inclusions such as “Despite trends like increasing divorce rates or more people choosing to remain single.”” Yellow Highlight [Page 10](zotero://open-pdf/library/items/D4MVN72A?page=10&annotation=P5ACPEPP)



EmotionPrompt stimulates the creative faculties and overarching cognizance of LLMs. This phenomenon is substantiated through the examination of Tables 16 and 17, wherein two instances of poem composition are showcased. Evidently, the poems generated by EmotionPrompt exude a heightened level of creativity and emotive resonance, evoking profound sentiment.” Yellow Highlight [Page 10](zotero://open-pdf/library/items/D4MVN72A?page=10&annotation=WN3J5USM)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/liLargeLanguageModels2023/image-12-x88-y535.png]]



we compute the contributions of prompts on every test sample and use the average value to represent their importance.” Yellow Highlight [Page 12](zotero://open-pdf/library/items/D4MVN72A?page=12&annotation=TUR4IALT)



Positive words make more contributions. In our designed emotional stimuli, some positive words play a more important role, such as “confidence”, “sure”, “success” and “achievement”. Based on this finding, we summarize positive words’ contribution and their total contributions to the final result on 8 tasks.” Yellow Highlight [Page 12](zotero://open-pdf/library/items/D4MVN72A?page=12&annotation=SJB2HS29)



Within Instruction Induction, EP02 emerges as the most effective stimuli, while in BIG-Bench, EP06 is the best” Yellow Highlight [Page 13](zotero://open-pdf/library/items/D4MVN72A?page=13&annotation=ACJISDNW)



Distinct tasks necessitate varied emotional stimuli for optimal efficacy. Figs. 9 and 10 illustrate that while EP02 emerges as the predominant stimulus in Instruction Induction, while perform poorly in BIG-Bench.” Yellow Highlight [Page 13](zotero://open-pdf/library/items/D4MVN72A?page=13&annotation=FDR6MTPL)




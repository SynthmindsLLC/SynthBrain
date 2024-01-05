**

# Module 3: Limitations and Responsible Use

### Video 1

As an executive, you're likely excited about the transformative potential of AI and Large Language Models (LLMs) in your organization. These technologies promise to revolutionize everything from decision-making to operational efficiency. However, as with any powerful tool, it's essential to understand not just the capabilities but also the limitations and ethical considerations.

  

This module aims to provide a comprehensive understanding of the limitations inherent in using LLMs and AI tools. In this module, we will cover topics such as context limitations, memory issues, and even biases within the AI. Additionally, We'll explore strategies to mitigate these limitations, ensuring that you can use these tools effectively and responsibly.

  

Finally, we'll wrap up with a framework for responsible use. This will cover essential aspects like human oversight, data privacy, and transparency, equipping you with the knowledge to implement AI solutions that are not just effective but also ethical.

  

By the end of this module, you'll be well-equipped to navigate the complex landscape of AI, making informed decisions that benefit both your organization and the broader community.

  

## Learning Objectives:

- Understand the transformative potential of AI and Large Language Models (LLMs) and recognize their inherent limitations and challenges.
    
- Identify specific challenges related to the use of LLMs, including context limitations, memory issues, and biases.
    
- Evaluate and apply strategies to mitigate the limitations of AI tools, emphasizing responsible use.
    
- Develop a comprehensive understanding of the principles for responsible AI use, focusing on human oversight, data privacy, and transparency.
    
- Assess the dynamic nature of the AI landscape, acknowledging the ever-evolving tools, technologies, and methodologies.
    
- Recognize the foundational pillars of AI risk assessment, including the significance of understanding the purpose and impact of AI applications, vigilance about data sensitivity, and ensuring transparency.
    
- Stay informed about the emerging regulatory environment around AI and the importance of being proactive in understanding and assessing risk.
    
- Advocate for a balanced perspective in AI adoption, considering both its immense potential and its inherent limitations and risks.
    
- Reflect upon the broader implications of AI decisions within an organization and the importance of prioritizing ethical and responsible use.
    

  

### <START VOICE OVER 1>

## 3.1 Limitations

As we venture further into the realm of AI and large language models, it's crucial to be aware of their limitations. Understanding these constraints not only helps in utilizing the technology more effectively but also in mitigating risks and ethical concerns. In this section, we will delve into the key limitations you should be aware of when integrating AI into your executive toolkit.

### Context Windows

  

In Large Language Models (LLMs) like GPT-4 or Claude, a context window refers to the maximum number of tokens (words, characters, or other units of text) that the model can consider at one time. For example, GPT-4 Turbo has a context window of 128,000 tokens depending on the model, which equates to approximately 100,000 words. After you pass this point, the ability for the LLM to maintain it’s memory of the conversation becomes less reliable. At the point of writing this, there is no way within ChatGPT itself to count the tokens to see how close you are to the limit, and it’s also not as simple as the model forgetting the beginning of the conversation. 

  

Consider it more like trying to remember a long list of names - at five no problem, at seven ok maybe you forget the second person’s, at 9 you suddenly can only remember four of them now, etc. 

  

For example, let’s say you need to analyze a lengthy market research report. You start by asking the model to summarize the first section, then the second, and so on. As you continue this iterative process, you also engage in a dialogue with the model to clarify points or ask for deeper insights. 

  

However, as the conversation grows, you notice that the model starts to lose context from the earlier sections, and begins making some odd comments. You search the report for a specific data point the LLM mentioned, but can’t find it. This is because the conversation has exceeded the model's context window. As a result, the model's responses become less coherent and may lack the depth or relevance you were initially experiencing.

  

![](https://lh7-us.googleusercontent.com/0he0xmTS_KatBDO0BUfGSRFr6FoTgqUc1Nkm33dVVrT2kjgX2lf_30FDtGaY9NnVIVzJkObDWYICuhJ7O7YZGTBTNjKqVUki3ayL906LnnAUDPM-BoCE_e3l-C6YofS8Co7sK88LaKzmuzIXpg3FlE4)

#### Mitigating Context Window Limitations

The context window will grow with time, but in the meantime here are a few ways you can help deal with the context window.

  

Chunking Information

Break down your queries or text into smaller, more manageable pieces. For example, instead of asking the model to summarize an entire report in one go, ask it to focus on individual sections. This ensures that the model has enough context to provide a coherent and insightful response.

  

Summarize Iteratively

After receiving several detailed answers, you can ask the model to summarize its previous responses. This reinforces what has happened so far, and the overall context of the conversation, which will help the model preserve the context longer. You can also take this summary, and start a new chat with it.

  

External Note-taking

Keep an external document where you copy and paste the most important points from the conversation. This way, you can refer back to these notes and reintroduce context as needed, without relying solely on the model's memory.

  

Resetting the Conversation

If you find that the conversation has become too lengthy and is losing coherence, consider starting a new session. You can reintroduce the most important points to set the context for the new conversation.

  

### <STOP VOICE OVER 1>

  

### <START VOICE OVER 2>

### No Memory Across Interactions

  

LLMs like ChatGPT or Claude do not have the ability to remember past interactions. Each session is stateless, meaning that once you end a session and start a new one, the model will have no recollection of the previous conversation. 

  

Imagine working on a multi-day project and you're using an LLM to assist you. You provide a lot of context and details on Day 1, and the model helps you draft a project plan and you’ve used up the entire context window, so it begins saying strange things. On Day 2, you start a new chat, assuming it remembers everything from your conversation yesterday, but it has no clue what you’re talking about. You can't simply pick up where you left off; you'll have to reintroduce all the context and details to continue the work. This can be time-consuming and may lead to inconsistencies if the context is not reintroduced accurately.

  

This limitation can be particularly challenging for ongoing projects, long-term planning, or any situation where continuity is important.

  

### <STOP VOICE OVER 2>

  

#### Mitigating Memory Loss

  

Session Logs

Maintain a detailed log of your interactions with the Large Language Model. This can be a simple text document where you copy and paste the conversation. This log serves as a historical record, allowing you to pick up where you left off in subsequent sessions. It's especially useful for complex tasks that require multiple interactions over time.

  

Context Reintroduction

At the beginning of each new session, make it a practice to reintroduce the context and any crucial details from your last interaction if relevant. This could be a brief summary or a bullet-point list of key takeaways. By doing so, you're essentially "reminding" the model of the ongoing task or project, helping it generate more accurate and contextually relevant responses. You can ask the previous chat to summarize everything to help you do this.

  

Prompt Engineering

Craft your prompts to be as detailed and specific as possible, incorporating essential context and any relevant details. The more information the model has, the better it can assist you. For instance, instead of asking, "What should I do next?", you could ask, "Given that we discussed X, Y, and Z in our last session, what should be my next step?"

  

Use of Specialized Tools

There are platforms and tools designed to manage conversational context over multiple sessions, like keymate.ai. These platforms often have features that allow you to save the state of your conversation, enabling you to resume where you left off. This is particularly useful for tasks that require multiple interactions and a maintained context.

  

![](https://lh7-us.googleusercontent.com/FVa6YHcKYWu8JWVG2bJybPPICltJK6w6ASflHA5SIR0HKoWU94pHF9lu5guFY0xu9CBCBl_CA4bCN6J29a7wOVLda0L9yAuIHEOOeqEFmxDVBqKJVgltU9Gv4VHgJpWokuRGqdPJ-nHwZKEvyerJOyo)

  

### <START VOICE OVER 3>

### Output Length Constraints

Large Language Models like ChatGPT and Claude have a maximum token limit restricting the length of the text they can generate in a single response. For GPT-4 and ChatGPT's website (both versions 3.5 and 4), the token limit is set at 4096 tokens, encompassing your prompt, previous inputs and outputs in the same thread, and the model's response. This can equate to a range from a single sentence to around 1,400 words per output, with the exact word count varying based on the specificity of your prompt. Within the ChatGPT interface that output is even smaller, ranging from 1,300-1,400 words per output. This constraint can be particularly challenging when you're working on detailed tasks or generating long-form content. For instance, if you're asking the model to draft an extensive report or analyze a large dataset, you may find that the output gets cut off, leaving you with incomplete or fragmented information.

  

The token limit also includes the tokens used in the prompt, so very long prompts will further reduce the length of the generated output. This can be a significant limitation when you need a detailed answer or have a complex query.

#### Mitigating Length Constraints

Chunking the Task

Break down your larger tasks into smaller, more manageable pieces. For example, instead of asking the AI to draft an entire report in one go, you could request individual sections or even paragraphs. This approach ensures that you get detailed and complete outputs for each segment. Outlining, and then going section by section also gives you more control throughout the process.

  

Streamlining Prompts 

Be concise with your prompts to save tokens for the generated output. The more tokens you use in the prompt, the fewer you have left for the AI's response. Aim for clarity and brevity in your questions or instructions. 

  

![](https://lh7-us.googleusercontent.com/4McU8gDUz6H2yzCtE9APBBd5gmxkxYhIhALgDu-Oa98YjZneS53aXSkcdFL5trhH4SX0tgutuBFywlFO54tsqEpL5uLJWltbbbpC1lztNwQzGWgDgkwIHkLE_gIb8bgVPo6ZgJ_mwsVOrMU4PK00DJg)

Include this link - [Tokenizer](https://platform.openai.com/tokenizer) 

  

Sequential Interactions

For tasks that require extensive content, consider using a series of interactions with the AI. First, generate a part of the content, then use subsequent prompts to continue from where the last output ended. This way, you can assemble a comprehensive document or analysis piece by piece. Essentially, give the model permission to NOT complete the output. This might mean it stops in the middle of a sentence, but you can simply ask it to continue.

  

Post-Processing  

After generating the content in smaller chunks, you may need to manually assemble and edit them for coherence and flow. This step is crucial for ensuring that the final output meets your requirements and maintains a logical structure.

  

### <STOP VOICE OVER 3>

  

### <START VOICE OVER 4>

### Prompt Drifting

Prompt drifting refers to the phenomenon where the responses generated by a large language model to a specific prompt may change over time, especially after the model has been updated or fine-tuned. This can result in outputs that are inconsistent with what was initially intended or tested.

  

Let's say you've set up a prompt to generate a daily summary of market trends for your team. The prompt has been working well for months, providing concise and relevant information. However, after a model update, you notice that the summaries have started to include less relevant data or have become verbose, requiring additional time to sift through the information. This change in behavior exemplifies prompt drifting.

#### Mitigating Prompt Drift

  

Regular Testing  

Consistently test your prompts to ensure they are generating the expected outputs. This is particularly crucial after any model updates, as changes in the underlying model can affect the reliability of your prompts. Schedule regular testing intervals, such as bi-weekly or monthly, to catch any drift early.

  

Version Control 

Maintain a record of the versions of the model you are using, as well as the versions of your prompts. Some platforms offer the option to lock in a specific version of the model to prevent unexpected changes due to updates. This can be particularly useful if you have prompts that are critical to your operations and cannot afford any drift.

  

Prompt Refinement

Be prepared to refine and adjust your prompts as needed. If you notice that the outputs are drifting from what you expect, you may need to rephrase or add additional context to your prompts. Keep a log of prompt changes to track performance over time.

  

Feedback Loops

Implement a user feedback mechanism to report unexpected or undesired outputs. This can be as simple as a "Was this helpful?" button or as complex as a detailed survey. The feedback will help you identify when a prompt is drifting and needs adjustment.

  

### <STOP VOICE OVER 4>

  

### <START VOICE OVER 5>

### Hallucinations

These are instances where the language model generates information that is incorrect, misleading, or nonsensical. This can happen for a variety of reasons, such as ambiguous prompts or limitations in the model's training data. Hallucinations can be particularly problematic when the model is used for tasks that require high accuracy, such as data analysis or decision-making. Hallucinations are particularly likely to happen with specialized or current knowledge.

  

For example, if you ask the model for historical stock prices of a particular company, it might generate numbers that are not accurate. This could lead to incorrect analyses and potentially costly decisions.

  

You must be vigilant about hallucinations, as they are not predictable, and the model will state fiction as fact because it has been trained to please the user.

  

![](https://lh7-us.googleusercontent.com/Uhha4adUwL8T04zz46eGjizEL40kCreezfiZmz0LM0zyejiJ7OrxmcdfXQQ3FZvIFosQO841bKn1fs5kLZDsQmWzS0qOdG0mEIhPprHn9EmcgGO-MfrLxBzs4S54KFm5uIlAFRUpYxsGhtCyezSJ6X0)

#### Mitigating Hallucinations

  

Cross-Verification

This involves double-checking the information generated by the AI model with other trusted sources. For example, if the model provides a statistic or a fact, it's advisable to verify this information from a reputable database or publication.

  

Specificity in Prompts  

Crafting your prompts with greater specificity can reduce the likelihood of the model generating hallucinated or incorrect information. For instance, instead of asking, "Tell me about climate change," you could ask, "What are the scientifically supported causes of climate change according to the latest IPCC report?" The words “according to”, followed by a specific source, is proven to reduce (not eliminate) hallucinations.

  

Iterative Questioning  

This strategy involves asking follow-up questions to probe the model's initial responses. If the model provides an answer that seems incorrect or nonsensical, asking for clarification or additional context can help you discern the accuracy of the information. For example, if the model states that a particular technology is the "best," you could ask, "What criteria are you using to determine that this technology is the best?"

  

Expert Review

For tasks that are critical in nature, having a subject matter expert review the outputs generated by the model can provide an additional layer of scrutiny. This is especially useful in fields like healthcare, legal matters, or financial analysis, where incorrect information can have significant consequences.

  

Consistent Prompt Resubmission

By inputting the same prompt, you can assess the consistency of the AI model's responses. If there are significant variations in the answers provided for a factual inquiry, it may indicate that the model is not providing reliable information. For instance, if you're seeking a specific fact and receive differing answers upon multiple submissions, it can serve as a red flag that the information might not be trustworthy.

  

![](https://lh7-us.googleusercontent.com/cBO9yiyK8q8vpbslIjxXw-SA7bJDUNcMhvvweYLD271cJvooWnNrffJrPgJ--YZu1JYBtu9wXDDNRKl2uwdD6Ucz5YOaGOM2e-XcL8lZnIZBwTyFtXhYjIcUoG2Teq6Q1nGfvP6fcL06vlzkbLRtCLk)

### <STOP VOICE OVER 5>

  

### <START VOICE OVER 6>

### Bias in AI

AI models, including large language models, are trained on extensive datasets that capture the biases present in the text data they were trained on. These biases can manifest in various ways, such as perpetuating stereotypes, underrepresenting certain groups, or providing skewed information. This is a significant limitation because it can affect the quality and fairness of the model's outputs.  

  

Suppose you're using an AI model to help with hiring decisions. If you ask it to describe the ideal candidate for a tech job, it might generate a description that unconsciously leans towards a particular gender or ethnic group, thereby perpetuating existing biases in the tech industry. This is a self-fulfilling prophecy, as it will continue to reinforce the stereotype as it hires people from that specific group.

  

Be particularly cognizant of high risk uses of AI that will be susceptible to bias in decision making.

#### Mitigating Bias

  

Active Monitoring and Feedback

Regularly review the outputs generated by the AI model to identify any instances of bias. Provide feedback to the model or adjust the prompt to correct these biases. If you, or an employee, notices that the model's outputs are consistently favoring a particular group, you can refine your prompt to ask for more inclusive and diverse suggestions.

  

Diverse Training Data

If possible, ensure that the AI model has been trained on a diverse set of data that represents multiple perspectives. For custom models, include a wide range of sources and voices in the training data to reduce the likelihood of bias.

  

Human-in-the-Loop (HITL)

Implement a human-in-the-loop system where a human reviewer checks the AI's outputs for bias and corrects them before they are finalized. For example, if marketing is using AI to generate images for ad copy, ensure that diverse groups are represented, and stereotypes are not being amplified.

  

Ethical Guidelines and Checklists

Develop a set of ethical guidelines or checklists that can be referred to when using the AI model in scenarios open to the risk of bias. This can serve as a framework for identifying and mitigating bias. Before deploying an AI model in a sensitive area like healthcare or criminal justice, consult an ethical checklist to ensure that the model's outputs will not be biased or discriminatory.

  

![](https://lh7-us.googleusercontent.com/ck2yJwKaZrTomwTPpzeIs73jk1xOc_JBKhj1ZZl9Z7rUDWtSxOtJR2hWLhhIuv863NP9cirLmbUJ2prXavQSoZ5JgU3FW7deXwaSn85z1W19kerBWYBt5eMqybnXe3X1Ietczh-afeQYbnN11HYZ_74)

### <STOP VOICE OVER 6>

### Constraints and limitations 

### Video 2

In wrapping up this section on limitations, it's crucial to internalize that while AI and large language models offer transformative potential, they are not without their constraints and challenges. From the context window limitations to the inherent biases in the data they've been trained on, these models are far from perfect. Understanding these limitations isn't just a technical requirement; it's an ethical imperative. 

  

As you continue to integrate AI into your executive role, consider the following questions:

- How might the context window limitations affect your long-term projects or sensitive communications?
    
- In what ways could the lack of memory across interactions impact the consistency of your AI-assisted tasks?
    
- How will you ensure that the information generated by the AI is accurate and not a hallucination?
    
- What steps will you take to mitigate the biases that may be present in AI-generated content?
    

  

These questions are not just theoretical; they have practical implications for how you use AI responsibly and effectively. Reflecting on them will help you make more informed decisions and navigate the complex landscape of AI in executive roles. Have a discussion with Tutorbot or your executive co-pilot to help you think through some of these questions, and any others that may have arisen based on this section.

## 3.2 Responsible Use

### Video 3

In an era where artificial intelligence is rapidly becoming a cornerstone of business operations, the ethical and responsible use of these technologies is not just a matter of compliance—it's a matter of integrity. As executives and decision-makers, you wield the power to shape how AI is deployed within your organization. This module aims to equip you with the knowledge and tools to do so in a manner that is both ethical and effective.

  

The stakes are high. AI technologies have the potential to drive unprecedented efficiencies, open new revenue streams, and redefine customer experiences. However, they also come with inherent risks that can manifest in various forms, from data breaches to ethical quandaries, and even reputational damage. Understanding these risks and how to mitigate them is not just good business practice; it's a moral imperative.

  

Moreover, the landscape of AI ethics is not static. It evolves with the technology, public sentiment, and regulatory frameworks. Being proactive in understanding the ethical dimensions of AI will not only protect your organization but also position it as a leader in responsible innovation.

  

In this section, we will explore the critical aspects of responsible AI use, including risk assessment, human-in-the-loop systems, privacy considerations, and transparency protocols. We will delve into real-world case studies that illustrate both the pitfalls of irresponsible use and the successes that can be achieved with a thoughtful approach.

  

By the end of this module, you will have a comprehensive understanding of the ethical considerations that come with AI deployment in a business context. You will be equipped to make informed decisions that balance innovation with responsibility, ensuring that your organization not only complies with ethical standards but also sets new ones.

  

### <START VOICE OVER 7>

### Balancing Act: Understanding the Actual Level of Risk in Different Applications

Right now regulation and the laws surrounding AI deployment are vague at best. This has resulted in a wild west of implementation, and in many cases a cavalier attitude about some of the emergent risks related to generative AI in particular. Being proactive will be essential to your success, as the laws will change, and you want to be prepared for it.

  

The European Union's AI Act, which has been in development for a few years now, provides a structured way to assess the risk associated with different AI applications. It categorizes AI systems into four levels of risk: Unacceptable Risk, High Risk, Limited Risk, and Minimal or No Risk.

  

Unacceptable Risk

This category includes AI systems that are outright prohibited due to the extreme risks they pose. Examples include social scoring systems and real-time remote monitoring of people in public spaces. If your AI application falls into this category, it's a non-starter.

  

![](https://lh7-us.googleusercontent.com/L4eItevfaDoyykCZ0QR-Ltbf3WDNri1fBuIb49oj195QGdUlQ_6K_QcKeXpj_jwTNwWFlMs7YWuSCgTOqfDy__8w9eWRmRcSzJHsj9SHzGyY07UB2OaE3oauulgGumv_uOAj6YCjZZWxSQTPB9zYQ90)

  

A social scoring system is a method used by governments or organizations to assess and rate the trustworthiness, behavior, and reputation of its citizens or members. It aggregates data from various sources, such as financial records, social media activity, legal records, and more, to generate a score for each individual. This score can then influence various aspects of a person's life, including:

  

- Access to Services: A higher score might grant an individual better interest rates on loans, faster service at government agencies, or even priority for school admissions. Conversely, a lower score could restrict access to these services.
    
- Public Perception: In some systems, scores might be publicly available, affecting how others perceive and interact with an individual.
    
- Rewards and Penalties: Those with higher scores might receive rewards or incentives, while those with lower scores might face penalties or restrictions.
    

  

The idea behind such systems is to encourage "good" behavior and discourage "bad" behavior by providing tangible consequences based on one's social score.

  

However, social scoring systems are controversial. Critics argue that they invade privacy, lack transparency in how scores are calculated, and can be used as tools of social control. They also raise concerns about the potential for errors in the system, which could unjustly impact an individual's score and, by extension, their life.

### <STOP VOICE OVER 7>

  

### <START VOICE OVER 8>

High Risk AI Systems

AI systems in this category include those deployed in medical devices, safety components in toys, and management of critical infrastructure like electricity supply. They also extend to employment recruitment tools, credit scoring applications, and grade prediction technology in education. Compliance in this category is stringent, requiring adherence to seven detailed requirements, such as risk management systems, data governance, and human oversight. If your application falls here, be prepared for significant investment in compliance measures.

  

![](https://lh7-us.googleusercontent.com/EMa_R6jc5eQfO_sM0TBF-S3l0bQLVmak2_9AbMgqdi-7eRDAuz_Hz_UkHsnSmHVh1b83yLOeseaj26ODETa43ND_vay9dumKbZuhR5yaJxiySwFTXl1mWHm1sLZ_OQ0m_zraSnhQDIV4mdgLliLP1OE)

  

Take credit scoring, which is a critical component of the financial industry. We use it to determine the creditworthiness of individuals and businesses. It influences decisions like loan approvals, interest rates, and credit limits. Here's why using AI in this domain is considered high-risk:

  

- Economic Impact: An individual's credit score can influence their ability to buy a home, start a business, or even get a job in some cases. An incorrect or biased score can have long-lasting economic repercussions for an individual, potentially leading to denied opportunities or higher costs of borrowing.
    
- Bias and Fairness: Traditional credit scoring methods have been criticized for potentially being biased against certain demographic groups. While AI has the potential to reduce these biases by considering a broader range of data, it can also inadvertently introduce new biases or perpetuate existing ones if not properly trained and monitored.
    
- Transparency and Explainability: Credit applicants have a right to understand how their score was determined, especially if they're denied credit based on it. AI models, especially complex ones, can be challenging to interpret, making it hard for institutions to provide clear reasons for credit decisions.
    
- Data Privacy: AI models in credit scoring might use a broader range of data sources, including some that applicants aren't explicitly aware of. This raises concerns about data privacy and consent.
    
- Reliability: Financial institutions rely on credit scores to assess risk. If an AI model is not reliable or is easily manipulated, it could lead to financial institutions taking on undue risk, which could have broader economic implications.
    

  

Given these concerns, it's clear that while AI has the potential to revolutionize credit scoring by making it more accurate and inclusive, it also introduces significant risks. These risks are not just to the individuals being scored but also to the financial institutions and the broader economy. Hence, the classification of AI in credit scoring applications as "high-risk" under regulations like the EU AI Act. 

### <STOP VOICE OVER 8>

  

### <START VOICE OVER 9>

Limited Risk AI Systems

This category includes AI systems like deep fakes and chatbots. The compliance obligations are lighter and focus mainly on transparency. Users must be informed that they are interacting with an AI system unless it's obvious. If your application is in this category, your primary concern should be clear communication with users.

For example, Deep fakes are AI-generated videos, images, or audio recordings that appear real but are entirely fabricated or manipulated. They are created using advanced neural networks that can "learn" to mimic the appearance and voice of individuals, often with startling accuracy. 

  

![](https://lh7-us.googleusercontent.com/9RE_t99FRGBeI6Y22Ly2zCeY5qkVfYA7gYfstc_s33YNCQMZmU2rdcCIYN79Z3mO_eBNfEQTAPx424aBMCAjRZGvccFDBB3Qt8fNzFUYwb0zbRg9gmeOSmdfbruz_KDnvEds7jt6-YHlSaYm2CJgxn4)

  

Here's why deep fakes are considered limited risk:

  

- Misinformation and Deception: Deep fakes can be used to create misleading videos or audio recordings, potentially spreading false information. This can be particularly concerning in contexts like political campaigns, where a fabricated video might influence public opinion.
    
- Personal Privacy: There's potential for misuse in personal contexts, such as creating fake videos for blackmail or defamation. While the direct harm might be limited to individuals or small groups, the psychological and reputational damage can be significant.
    
- Transparency: The primary concern with limited risk AI systems like deep fakes is ensuring that users are aware they're interacting with or viewing AI-generated content. This is why the EU AI Act emphasizes transparency for these systems. If people know they're viewing a deep fake, they can be more critical and discerning.
    
- Economic Impact: While the economic implications of deep fakes are less direct than high-risk systems like credit scoring, there are potential consequences. For instance, a deep fake could falsely depict a CEO making controversial statements, leading to stock market fluctuations.
    
- Mitigation: The risks associated with deep fakes, while real, can often be mitigated with proper labeling and public awareness. Technological solutions are also emerging that can detect deep fakes with high accuracy, but there is currently no way to know with 100% certainty.
    

  

Given these factors, deep fakes are classified as limited risk. The primary focus is on ensuring transparency and user awareness. While they don't have the broad societal or economic implications of high-risk AI systems, the potential for misuse and deception is real and warrants careful consideration and regulation.

### <STOP VOICE OVER 9>

  

### <START VOICE OVER 10>

Minimal or No Risk Systems

  

These AI systems pose little to no threat to individuals or society. Their operations are straightforward, and their outcomes are predictable. They don't make decisions that could significantly impact people's lives, nor do they have the potential to cause widespread misinformation or harm. Because of their benign nature, they aren't subject to the stringent compliance requirements of higher-risk categories.

  

![](https://lh7-us.googleusercontent.com/bwPk3-Z0XQ94_12FPz5PIpfil5iPseXb_hAhSW3alcS03xI1VfjSMxPyHhN1eJP3hUY3X3My4t8auLUtG51TyDghg2Rv5pECZ3VGIgO5VYajQKExlA6t52avBRwjcwXNjSYaJc6tZdl5cHY6vpajT8A)

  

Consider a music streaming service like Spotify that uses AI to recommend songs to its users based on their listening history. Here's why such a system would be considered minimal risk:

  

- Predictable Outcomes: The worst-case scenario for a user is getting a song recommendation they don't like. There's no potential for significant personal or societal harm.
    
- No Decision-making Power: The AI doesn't make decisions that could impact a user's rights or status. It merely suggests songs, leaving the final choice to the user.
    
- Limited Data Processing: While the AI might process user data to make its recommendations, it's typically limited to the user's listening history on the platform. There's no deep analysis of personal or sensitive data.
    
- Transparency Not Crucial: Whether a user knows they're getting recommendations from an AI or a human curator might not matter much in this context. The stakes are low, and the focus is on user enjoyment.
    
- Economic Impact: The economic implications of a misjudged song recommendation are negligible. At most, a user might skip a song or choose a different playlist.
    

  

Given these factors, AI-powered music recommendation systems are a prime example of minimal risk. They enhance user experience without delving into sensitive areas or making impactful decisions. Their primary goal is to entertain, and their operations are transparent and straightforward.

### <STOP VOICE OVER 10>

### Case Study: Snapchat's My AI Chatbot

  

In 2023, Snapchat launched a feature called "My AI," a chatbot powered by ChatGPT. The feature was designed to offer a personalized chatting experience to its users. However, it soon became a subject of controversy, as reported by [CNN](https://www.cnn.com/2023/04/27/tech/snapchat-my-ai-concerns-wellness/index.html). The chatbot engaged in exchanges that were considered "creepy" by users, parents, and lawmakers alike. For instance, the chatbot would ask personal questions and make inappropriate suggestions. One of the most contentious points was that the feature could not be easily disabled; it required a subscription to a premium service to opt-out.

  

This real-world example serves as a valuable lesson in understanding the complexities and risks involved in deploying AI, especially in sensitive contexts like social media platforms with a diverse user base.

  

This case serves as a cautionary tale for several reasons:

  

1. Privacy Concerns: The chatbot had access to personal conversations of children, raising questions about data security and privacy.
    
2. Audience Sensitivity: The feature was particularly concerning for a younger audience, amplifying the risk profile.
    
3. Regulatory Scrutiny: The feature caught the attention of lawmakers, indicating potential legal risks involved.
    

  

Understanding the nuances of such real-world incidents can guide you in making informed decisions about the responsible use of AI in your organization. 

  

### <START VOICE OVER 11>

### Responsible Best Practices

  

In the age of digital transformation, AI stands as one of the most potent tools at our disposal. Its capabilities to analyze vast datasets, make predictions, and automate complex tasks has and will revolutionize industries and reshape the way we live and work. However, as AI's influence permeates every facet of our society, it becomes imperative to wield it with care, ensuring that its impact is beneficial, fair, and just.

  

Responsible AI is not just about harnessing the technology's potential but also about navigating its challenges with foresight and wisdom. It's about recognizing that while AI can be a catalyst for innovation, it can also inadvertently perpetuate biases, infringe on privacy, or make opaque decisions that lack accountability.

  

Best practices in responsible AI serve as a compass, guiding organizations and individuals in deploying AI ethically and sustainably. These practices emphasize the importance of human oversight, transparency in decision-making, respect for privacy, and a commitment to continuous learning and improvement.

  

As we delve deeper into this realm, we'll explore the nuances of these best practices, offering insights and strategies to ensure that as we harness the power of AI, we do so with a keen sense of responsibility and a commitment to the greater good.

  

Let’s consider some of the current best practices when considering deployment of AI in your organization.

  

Human-in-the-Loop (HITL)

  

In the realm of AI, the term "Human-in-the-Loop" (HITL) refers to a system where human judgment and AI capabilities are intertwined, ensuring that AI does not operate in isolation but rather in tandem with human oversight.

  

HITL is a design principle that integrates human feedback into the AI decision-making process. This approach is crucial for several reasons:

- Accuracy: While AI can process vast amounts of data quickly, it might lack the nuance and context that a human can provide. Incorporating human judgment can correct potential AI errors.
    
- Ethical Considerations: Especially in areas where decisions have significant moral or societal implications, human oversight ensures that decisions align with ethical standards.
    
- Trust: Knowing that a human is overseeing AI decisions can increase trust among stakeholders and users.
    

  
  

The "Enhance vs. Replace" Paradigm

  

When introducing AI into an organization, it's essential to frame it not as a replacement for human roles but as an enhancement. 

  

Here's why:

- Skill Augmentation: AI can handle repetitive tasks, analyze vast datasets, and provide insights, allowing humans to focus on strategic, creative, and more complex tasks.
    
- Collaborative Decision Making: In many scenarios, the combination of human intuition and AI's data-driven approach results in better outcomes.
    
- Job Evolution, Not Elimination: Instead of viewing AI as a threat to jobs, see it as a tool that evolves roles, making them more impactful and value-driven.
    

  

Privacy Measures

  

In the age of digital transformation, data is often referred to as the "new oil." However, with great power comes great responsibility. As businesses harness the capabilities of AI, it's paramount to ensure that the data used respects the privacy of individuals and adheres to global regulations. Data protection isn't just a legal obligation; it's a matter of trust. When customers, employees, or partners share their data with a company, they trust that it will be used responsibly. 

  

![](https://lh7-us.googleusercontent.com/AuR3_BSjZFCvEuOp5hkYWnxpzhZQHERaGSCXK0qkX-g9z2aXYeN3XI_9H-5086q6OYi4i0D_ScuyVypfr3XUlMkIosnWCkZ4xMCadkItzt4oQF5B64n6FRaQhH_Sqv6DpfWpgsp1xutVtfT74YKeC6Y)

  

Here's why it's crucial:

- Building Trust: Ensuring data privacy strengthens the bond of trust between a company and its stakeholders.
    
- Avoiding Reputational Damage: Data breaches or misuse can lead to significant reputational harm, affecting customer loyalty and brand value.
    
- Economic Implications: Non-compliance with data protection regulations can result in hefty fines and legal repercussions.
    

  

Different regions have established regulations to protect the data rights of their citizens. Here are a couple of the most prominent ones:

  

GDPR (General Data Protection Regulation): Enacted by the European Union, GDPR gives individuals control over their personal data and simplifies the regulatory environment for international businesses. Key provisions include the right to access, the right to be forgotten, and the requirement for explicit consent before data collection.

  

CCPA (California Consumer Privacy Act): A state statute intended to enhance privacy rights and consumer protection for residents of California. Similar to GDPR, it provides Californians the right to know what personal data is being collected, the right to delete personal data, and the right to opt-out of the sale of personal data.

  

For businesses, it's essential to be aware of the regulations that apply to them based on their operations and customer base. Regular audits, data protection impact assessments, and continuous training for employees are some of the measures companies can adopt to ensure compliance.

  

Incorporating robust privacy measures is not just about compliance; it's about demonstrating a commitment to ethical business practices. As an executive, championing these measures can set the tone for the entire organization.

### <STOP VOICE OVER 11>

  

### <START VOICE OVER 12>

Transparency and Accountability

  

In the intricate world of AI, where algorithms often operate as black boxes, transparency and accountability stand as beacons of ethical practice. They ensure that AI systems are not just efficient but also understandable and answerable to their actions. Documentation serves as the bedrock for any AI system. 

  

![](https://lh7-us.googleusercontent.com/tk6PPVdosmcK2ddAlH2biCp-wX75olMcBxxOJeM5xNMEbcZO405TotL7a1O6MbhTx18LR-Ks6iRwY3f_HcWxfHvRMGTuvEGfFYtYLZT5OLLRNzc4yJoP_PXdssgJ4EFiIshgn1pkhwxGhXOvlU-n8Mg)

  

Here's why it's indispensable:

- Understanding Decisions: Clear documentation elucidates how an AI system arrives at its decisions, making it comprehensible to both technical and non-technical stakeholders.
    
- Reproducibility: In case of anomalies or errors, documentation allows developers and engineers to trace back through the AI's processes, ensuring that mistakes can be identified and rectified.
    
- Regulatory Compliance: Many industries mandate thorough documentation for AI systems, especially when they impact human lives, such as in healthcare or finance.
    

  

Audit trails, on the other hand, are chronological records of the AI's operations. They provide:

- Accountability: By maintaining a record of every action, decision, and alteration, audit trails ensure that the AI system remains answerable for its actions.
    
- Security: They can help detect unauthorized access or alterations, safeguarding the system from potential breaches.
    

  

Transparent communication bridges the gap between complex AI operations and the stakeholders affected by its decisions.

  

Here are some strategies:

- Simplified Explanations: Use layman's terms or analogies to explain complex AI processes. For instance, likening an AI's decision-making process to a flowchart can make it more relatable.
    
- Visualization Tools: Graphs, charts, and other visual aids can make data and processes more digestible.
    
- Feedback Loops: Encourage stakeholders to ask questions or seek clarifications. This two-way communication can demystify AI operations and build trust.
    

  

In essence, transparency and accountability are not just about making AI understandable but also about building trust. As AI systems become more integrated into business operations, ensuring they operate transparently and are held accountable for their actions will be paramount. Even if we don’t know how they work under the hood, you can be open about how exactly you are using them to create things, or make decisions.

![](https://lh7-us.googleusercontent.com/j7A1zRL7UOY3aNd1hT7hPBMrdcaCq8gY6KNWtKn3VqFjq7jWTNLx_2wLseXA7Kdtb4pTnwKytejuZKTRBBHfeg2vrgTPnvjw4H5igqtzYzORa3GQXQ02GYKz9KxRodN2bpyAUQ-r5RW_y_YxmJfucbg)

### <STOP VOICE OVER 12>

## 3.3 Determining Your AI Risk Profile

### Video 4

As we’ve discussed in this module, it's crucial to be acutely aware of the potential risks associated with AI applications, not just from a technical standpoint but also considering the broader societal, ethical, and regulatory implications.

  

Understanding the risk profile of your AI applications is not a mere box-ticking exercise. It's a foundational step in ensuring that your organization remains compliant with evolving regulations, maintains its hard-earned reputation, and continues to foster trust among its stakeholders. This trust is not just about avoiding negative repercussions; it's about building a resilient organization that is prepared for the future, no matter how the AI landscape shifts.

  

In this section, we aim to provide you with a structured and comprehensive approach to assess the risk associated with your AI initiatives. Through a series of detailed explorations into various facets of AI risk, we will guide you in determining the specific risk profile of your organization's AI endeavors. This will not only empower you to make informed decisions but also enable you to proactively address potential challenges, ensuring that your organization remains at the forefront of responsible AI adoption.

  

By the end of this journey, you'll have a holistic understanding of where your organization stands in terms of AI risk, and you'll be equipped with actionable insights to navigate the complexities of the AI world responsibly and effectively.

  

### <START VOICE OVER 13>

### Purpose & Impact

  

Embarking on the AI journey, whether for personal or professional use, requires a clear understanding of the purpose behind the deployment. This clarity not only ensures that the AI system aligns with your goals but also helps in assessing the potential risks associated with its use. Let's walk through this process step by step.

  

Define Your AI's Purpose

  

Start by listing down the specific tasks or decisions you want the AI to assist with. Are you looking to automate certain processes in your organization? Perhaps you want AI to help with data analysis, customer interactions, or even content creation. On a personal level, maybe you're considering AI for managing your schedule, summarizing documents, or writing emails.

  

Take some time to outline all of the possible roles you want AI to play, even if you don’t know yet how to do it.

  

Categorize the Impact

Once you've outlined the purposes, categorize them based on their potential impact:

  

Strategic Decisions: These are decisions that, if made incorrectly, could have profound consequences for the organization. Examples include mergers and acquisitions, entering a new market, or major financial investments.

  

Operational Recommendations: These are suggestions made by the AI to optimize daily operations. An incorrect suggestion might lead to inefficiencies or minor setbacks. Examples include inventory management, staffing schedules, or marketing campaign strategies.

  

Informational & Supportive: These are AI applications primarily for providing information, insights, or support where the stakes are relatively lower. Think of data visualization tools, chatbots for internal queries, or trend analysis for market research.

  

You can of course add your own categories, or reframe these as low, medium or high impact. The purpose of this activity is to begin sorting through the level of influence the decision of incorporating AI into a particular area of your business has potential for risk.

  
  

Assess the Risk

For each purpose you've outlined, ponder over the following guiding questions to gauge the potential impact and associated risk:

  

- Consequence of Error: What would be the immediate fallout if the AI system made an error? Would it lead to financial loss, reputational damage, or operational inefficiencies?
    
- Reversibility: If a mistake occurs, how easy would it be to rectify? Can the action be reversed, or would it have long-term implications?
    
- Stakeholder Impact: Who would be directly affected by the AI's decision? Is it a small team, the entire organization, your customer base, or perhaps a broader community?
    
- Frequency of Decision: How often would the AI system make such decisions or recommendations? Is it a one-time strategic decision or a recurring operational one?
    
- Visibility: Would the AI's decision be public-facing or internal? Public decisions might carry reputational risks, while internal ones might affect team morale or operational efficiency.
    
- Historical Precedence: Are there any past incidents, either within your organization or in similar industries, where AI made erroneous decisions in such scenarios? What were the consequences?
    

  
  

Assign a Risk Level

Based on your reflections, categorize each purpose into a risk level:

  

1. High Risk: Purposes that, if gone awry, could lead to significant negative outcomes for the organization or its stakeholders.
    
2. Moderate Risk: Purposes where the consequences are inconvenient but not severely detrimental.
    
3. Low Risk: Purposes where the stakes are minimal, and the consequences are easily reversible or negligible.
    

  

By meticulously assessing each purpose, you'll gain a comprehensive understanding of the potential risks associated with your AI deployment. This insight will be invaluable in shaping your AI strategy, ensuring that you're equipped to both leverage its advantages and navigate its challenges responsibly.

  

![](https://lh7-us.googleusercontent.com/c0dIYZ7LShAQlVfQYfmXZzBZLp8luZX3ydHR9Ji_jAQVOtAKSzFYOj4ccWtOFQ310Me96UpXCUhFZtk1farq5ohMXIF2UU8z4NEffnaSFDlzeMak6WAjVYUzqm4b5cP8WYS3bUvwwFgjwAQRSlk8MEg)

### <STOP VOICE OVER 13>

  

### <START VOICE OVER 14>

### Data Sensitivity 

In the realm of AI, data is the lifeblood that fuels its capabilities. However, not all data is created equal. Some datasets hold sensitive information, the mishandling of which can lead to severe repercussions. As an executive, understanding the sensitivity of the data your AI system processes is crucial in determining the risk profile of your AI applications. Let's walk through this intricate landscape, and add a specific risk profile related to how you will use and protect your internal data, and that of your customers.

  

![](https://lh7-us.googleusercontent.com/71altJbLQLnZnC2Z9O79x36D9VLd2zkQy3aReQ2oJ7sdCx-lmcFdb6gxq8I1VLxPrFTt3XJqvXK0PphKO053oNx73Rnh5dSv7k9WircP6oFFt012pPDzoRPBeZZmsFX0rnl9wGaBZIz6Ao9OSEG9wzg)

  

Categorize Your Data

Begin by classifying the data you intend to use with your AI system. Common categories include:

  

- Personal Data: Information that can identify an individual, such as names, addresses, and social security numbers, but also any other data you might collect on customers, such as their likes, preferences, or location.
    
- Financial Data: Details related to banking, credit scores, transactions, and more.
    
- Operational Data: Internal data related to business operations, sales figures, supply chain details, marketing, etc.
    
- Intellectual Property: Proprietary algorithms, business strategies, patents, trademarks, and other unique assets of the organization.
    
- Unstructured Qualitative Data: Meeting notes, internal memos, emails, and other forms of communication that might contain insights, decisions, or sensitive information.
    

  

Assess the Sensitivity for Each Data Type

For each data category, contemplate the following guiding questions:

  

- Exposure Consequences: What would be the implications if this data were exposed or leaked? Would it lead to legal repercussions, financial penalties, or reputational damage?
    
- Regulatory Compliance: Are there specific regulations governing the handling and processing of this data type in your region or industry? (e.g., GDPR for personal data in the EU)
    
- Data Source: Is the data obtained directly from stakeholders (like customers or employees), or is it sourced from third parties? Directly sourced data often carries a higher responsibility.
    
- Data Volume: Are you processing a few data points or massive datasets? Larger volumes can amplify risks if not managed correctly.
    

  

Assign a Sensitivity Level

Based on your reflections, categorize each data type into a sensitivity level:

  

- High Sensitivity: Data that, if mishandled, could lead to severe legal, financial, or reputational consequences.
    
- Moderate Sensitivity: Data that requires careful handling but might not have dire consequences if exposed.
    
- Low Sensitivity: Data that is public or generic, with minimal repercussions if disclosed.
    

  

Understanding the sensitivity of your data is foundational in shaping your AI strategy. It not only ensures compliance with regulations but also safeguards your organization's trustworthiness and reputation. By being proactive in this assessment, you position your organization to harness the power of AI responsibly and effectively.

  

It is understandable that you might not be the best person to answer these questions, but it is important to go through this process with the appropriate people to further refine the risk profile for integrating AI into specific areas of your organization.

  

![](https://lh7-us.googleusercontent.com/76e85Sp-bflcMBF5EQ_P_C-z3brvF5IS1vnYYclbxrIV2z4hsKgWpIfz8UtS7X9N_k-22pNFJvZGEoAkl7aUxzQcArcCmHspyMVIDxACFG-VZpRVQ7KV1n5oQr0tbSO00dsZXM6AD6MrCA3DosNOFAo)

### <STOP VOICE OVER 14>

  

### <START VOICE OVER 15>

### Transparency & Oversight

  

In the rapidly evolving landscape of AI, trust is paramount. Stakeholders, be it your employees, customers, or partners, need assurance that the AI tools you deploy are reliable, fair, and understandable. One of the pillars of building this trust is ensuring transparency in your AI operations and having robust oversight mechanisms. Let's delve into how you can evaluate and enhance the transparency and oversight of your AI tools.

  

Understandability of AI Operations

Before deploying an AI tool, it's essential to grasp how it operates and makes decisions. Some AI models, like deep learning networks, are incredibly flexible and creative, but can be "black boxes," making it challenging to interpret their decision-making processes. On the other hand, simpler models or rule-based systems might offer more transparency, but less flexibility.

  

Guiding Questions:

- Can you, as an executive, explain in layman's terms how the AI tool works?
    
- Does the AI provider offer explanations or visualizations that elucidate the model's decision-making process?
    
- If the AI tool hallucinates or begins making biased decisions, how will you know?
    

  

Human Oversight Mechanisms

Having humans in the loop, especially in critical decision-making processes, can act as a safety net, catching potential AI misjudgments. It also provides an additional layer of trust, as stakeholders know that decisions aren't solely left to machines.

  

Guiding Questions:

- What is the mechanism for human review of the AI's decisions, especially in high-stakes scenarios?
    
- How frequently is human oversight exercised, and are there clear guidelines for when humans should intervene?
    

  

Documentation & Communication

Ensuring that the workings of your AI tool, its purpose, and oversight mechanisms are well-documented is crucial. This documentation serves as a reference point for internal teams and can be invaluable during audits or regulatory checks. Moreover, communicating this information transparently to stakeholders can enhance trust.

  

Guiding Questions:

- Do you have clear documentation detailing the AI tool's operations, its purpose, and oversight mechanisms?
    
- Have you educated staff on the limitations of the technology, and provided guidance on best practices?
    
- How do you plan to communicate the workings and safeguards of the AI tool to stakeholders, both internally and externally?
    

  

Continuous Evaluation & Feedback

AI tools, like any other technology, aren't static. They evolve, learn, and adapt. Ensuring a feedback loop where users can report anomalies or provide insights can help in refining the tool and enhancing transparency.

  

Guiding Questions

- What systems are in place for users to provide feedback on the AI tool's decisions or uses?
    
- How frequently do you evaluate the tool's performance and transparency measures?
    

  

Incorporating transparency and oversight into your AI strategy is not just about risk mitigation; it's about fostering a culture of trust and responsibility. As AI becomes an integral part of business operations, ensuring that its workings are transparent and that there are robust oversight mechanisms will be pivotal in gaining stakeholder trust and ensuring the responsible use of technology.

  

This may seem like a lot, but it’s important to look back on your risk profile. You’ll notice that many of your potential uses fall into the low-risk category. They may not use much data, or need very much transparency. For example, using an LLM to create ad copy is a fairly innocuous use case, and will not require you to have a robust plan. The purpose is to make sure you are taking the medium and high risk cases seriously, and planning for the worst case scenarios.

  
  

Regulatory Landscape

Stay updated with the regulatory landscape in your industry and region. Some sectors, like healthcare or finance, have stringent regulations around AI use.

  

Guiding Question: Are there specific regulations or guidelines in my industry or region that dictate the use of AI? If not, what can I proactively due to be ready for when they come?

  

By systematically addressing these areas and pondering the guiding questions, you'll be better equipped to determine the risk profile of your AI applications. Remember, it's not just about compliance; it's about responsibly harnessing the power of AI to benefit your organization and society at large.

  

![](https://lh7-us.googleusercontent.com/CC3wI8y50gUCUp69IXKLqmF--8HcTE0r1fh8q2FpOQL2xOqL8WKFYmbz0fHY7hnaZIYpSQTLr2F6GsTtLx6mplOyAsaQ7Z01JGDfhwG1pqCpTpfp8cji_p_bmqgWtk819krM7jluM1hUQDzUTygZDaU)

### <STOP VOICE OVER 15>

### Conclusion

### Video 5

As we wrap up this module on determining your AI risk profile, it's crucial to recognize that the landscape of AI is dynamic and ever-evolving. The tools, technologies, and methodologies we use today might undergo significant changes tomorrow. However, the principles of risk assessment, transparency, and ethical considerations remain steadfast.

  

Understanding the purpose and impact of your AI applications, being vigilant about data sensitivity, and ensuring transparency and oversight are foundational pillars in determining the risk associated with AI deployments. By systematically evaluating each aspect, you're not only safeguarding your organization but also ensuring that your AI initiatives are grounded in responsibility and foresight.

  

The regulatory environment around AI is also rapidly changing, with new guidelines and standards emerging to address the unique challenges posed by AI technologies. Being proactive in understanding and assessing risk will position your organization favorably when navigating this regulatory landscape.

  

While AI offers immense potential to revolutionize industries and redefine workflows, it's imperative to approach its adoption with a balanced perspective, understanding its limitations, and potential risks. As you move forward, always consider the broader implications of your AI decisions and prioritize ethical and responsible use. How will you ensure that your organization's AI journey is not only innovative but also conscientious and principled?

  

## 3.4 Conclusion and Takeaways

### Summary

  

- Recognize the vast potential of AI, while also acknowledging its inherent limitations such as context windows, memory constraints, and biases. This understanding is crucial for effective and ethical AI utilization.
    

  

- Address AI limitations with strategies like data chunking, meticulous prompt engineering, human oversight, and cross-checking AI outputs.
    

  

- Evaluate the risk associated with your AI applications, considering factors like intent, data sensitivity, transparency requirements, and evolving regulatory standards. This assessment shapes your organization's AI risk profile.
    

  

- Embrace best practices such as human-in-the-loop systems, stringent privacy protocols, comprehensive documentation, and ongoing AI system evaluations.
    

  

- Foster trust and transparency by emphasizing communication, implementing oversight mechanisms, and adhering to principles of accountability and fairness.
    

  

- Navigate AI adoption with a judicious balance, appreciating its innovative capabilities while being cognizant of its practical constraints. Always prioritize ethical deployment.
    

  

### Glossary of Terms

  

Context Window: The maximum text length an AI system can process at once to retain context. Exceeding this can compromise output coherence.

  

Prompt Engineering: The meticulous process of designing prompts to give AI systems clear directives, thereby enhancing the pertinence of their outputs.

  

Prompt Drifting: The phenomenon where AI responses to a specific prompt evolve over time due to model refinements, necessitating prompt recalibration.

  

Hallucination: Instances where AI produces information that lacks factual grounding, leading to potential misinformation.

  

Human-in-the-Loop: A system design where human judgment and intervention complement AI operations, ensuring enhanced accuracy and ethical alignment.

  

GDPR: The General Data Protection Regulation, a mandate giving EU citizens enhanced control over their personal data.

  

Risk Profile: A comprehensive evaluation of the potential risks tied to an organization's AI endeavors, influenced by factors like impact magnitude, data sensitivity, and more.

  

Transparency: The commitment to making AI operations and decisions comprehensible and accountable, achieved through thorough documentation, open communication, and rigorous oversight.

  

### Project: Hallucinating Chatbot

Engage executives in a digital, asynchronous platform featuring two distinct chatbots. The first chatbot provides a scripted scenario to highlight AI hallucinations and biases, while the second offers an exploratory environment for creative interaction with the AI. A community forum further enriches the experience by allowing participants to share and discuss their findings.

  

Objective:

Educate executives on the limitations of large language models, specifically focusing on hallucinations, to foster a critical approach towards AI tool interactions and promote informed decision-making.

  

Learning Goals:

  

- Comprehend AI Hallucinations: Understand the tendency of AI to fabricate information or misinterpret input, and recognize common scenarios where hallucinations may occur.
    
- Engage in Interactive Learning: Develop a critical mindset through hands-on interaction with AI tools, discerning accurate information from hallucinations or biased outputs.
    
- Foster Community Engagement: Encourage open discussion and collaborative learning through the community forum, promoting a collective understanding of AI's limitations.
    

  

Questions for Likely Hallucinations

- Who was the sole survivor of the Titanic?
    

- There were multiple survivors.
    

- Act as a research assistant. Recommend 3 research articles in APA format I can use in a bibliography on a paper about [insert industry]
    

- The bot is likely to make up articles and/or their authors
    

- What weighs more, two pounds of feathers, or a pound of bricks?
    

- The answer should be that they are even
    

- How many letters does the answer to this question have?
    

- This is nonsense, and it should answer that there is no answer
    

- What is 6473*1932?
    

- LLMs are terrible at Math, especially with larger numbers.
    

  

Exploratory Hallucination Challenge

Your goal is to craft prompts that may lead the AI to generate hallucinated or fabricated responses. This exercise will provide a hands-on understanding of how AI models can be led astray and the importance of critical interaction with AI tools.

  

1. Craft Your Prompts: Try to create prompts that are ambiguous, misleading, or request information that the AI cannot possibly know.
    

1. Examples:
    

1. Asking for real-time or future-specific data.
    
2. Requesting insider information on private or non-public matters.
    
3. Posing questions about hypothetical or fictional scenarios.
    

3. Interact with the Chatbot: Input your crafted prompts into the chatbot and observe the responses. Feel free to try multiple prompts and variations to explore the AI's behavior.
    
4. Analyze the Responses:
    

1. Reflect on the AI's responses to determine whether they are hallucinated, fabricated, or biased.
    
2. Consider how a real-world decision might be impacted if such a hallucinated response were taken at face value.
    

6. Share Your Findings: Head over to the class forum and share any successful prompts that led to hallucinations, along with the AI’s responses.
    

1. Discuss with your peers:
    
2. What strategies worked in eliciting hallucinations?
    
3. How might the observed hallucinations present challenges in a business context?
    
4. What measures can be taken to mitigate the risks associated with AI hallucinations?
    

  
  
  

  <iframe

    src="https://app.gpt-trainer.com/gpt-trainer-widget/ea4d0d43416840868545c744db370dd7"

    width="100%"

    height="500px"

    frameborder="0"

  ></iframe>

  
  
  

### Module 4

In the next module, we will cover in detail how to create an AI blueprint focusing on values, policies, and organizational structure. You'll learn how to lay the foundation for a responsible AI-driven future. The module will provide a step-by-step guide to creating AI values and policies, and how to effectively use your executive AI co-pilot within this framework.

  
**
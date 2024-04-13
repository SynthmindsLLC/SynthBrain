Telemetry-of-Thought in large language models (LLMs) refers to having a transparent way to track and understand the decision-making process of AI as it happens. Much like how telemetry in aviation provides data on an aircraft's position, speed, and environmental conditions, thought telemetry in AI offers insights into the internal deliberations and logic that lead to a model's output.

 It's similar to examining system logs to diagnose issues or optimize performance in programming. In AI, however, the stakes are higher; the reasoning process is more abstract and complex. By analyzing an AI's "thought logs," we can ensure that the model's conclusions are sound, its learning is on track, and its interactions are aligned with our expectations.

Understanding this process is crucial for trust and transparency in AI systems. It allows us to peer under the hood, so to speak, and scrutinize the AI's thought process, ensuring that the reasoning is not just a black box, but a clear and interpretable sequence of cognitive steps.

## Insights from System 2 and Self-Discover

System 2 is a concept created by [[Daniel Kahneman]] and [[Amos Tversky]]. The general idea is that you have two ways of figuring things out: one is super fast and doesn't need much energy—it's like when you know the answer to "What's 2 + 2?" without even thinking. That's "System 1."

But sometimes, things are trickier, like if someone asked you to solve a really hard math problem or to make a big decision, like which car to buy. For those, you can't just snap your fingers and know the answer. You have to take your time, think really hard, and maybe even write stuff down or make a list of pros and cons. 

That's "System 2" at work. And right now LLMs are all System 1, and an opaque one at that.

Additionally, the [SELF-DISCOVER]([[Self-Discover - Large Language Models Self-Compose Reasoning Structures 1]]) method is a technique where LLMs generate their own explanations and rationales for the answers they provide, effectively creating a self-generated narrative of their thought process. In the context of the research, this method significantly improved outputs and reasoning.

Moreover, by encouraging LLMs to articulate their reasoning, we obtain a form of cognitive telemetry that maps out the model's internal dialogue. This process is akin to an AI "thinking out loud," which offers developers and researchers a clear view of the steps and considerations taken by the model before arriving at a conclusion.

Key findings from research into the SELF-DISCOVER method have shown that LLMs can indeed be guided to construct more transparent reasoning pathways. These pathways not only help in validating the model's outputs but also serve as a diagnostic tool to identify and correct errors in the model's logic. Moreover, this transparency aids in building user trust, as the AI's decision-making is no longer a mysterious black box, but a glass box that can be observed and understood.

## Telemetry in Cybersecurity and IT

In the fields of cybersecurity and IT, logs are essential tools that record the events happening within a computer system or network. Think of logs as a detailed diary that keeps track of everything that occurs, from the mundane to the critical. They provide a chronological account of actions, such as user logins, system errors, network connections, and transactions.

Logs serve several vital purposes:

1. **Monitoring:** IT professionals constantly monitor logs to see what's happening in real-time. This helps them ensure that systems are running smoothly and efficiently.
    
2. **Troubleshooting:** When something goes wrong, logs are the first place to look. They can help pinpoint when and where a problem started, which is crucial for fixing issues quickly.
    
3. **Security:** Logs are critical for security because they record all attempts to access the system. Security teams use them to detect suspicious activities, such as repeated login failures that could indicate a hacking attempt.
    
4. **Compliance:** Many industries have regulations that require the collection and storage of logs to prove that they're protecting data and following privacy laws.
    
5. **Forensics:** In the event of a security breach, logs are invaluable for forensic analysis. They help investigators understand how an attack happened and trace the steps of the attacker.
    

In the context of LLMs, Telemetry-of-Thought can be compared to these IT logs. If we had access to an AI's thought logs, we could use them in similar ways:

1. **Monitoring:** We could watch the AI's thought process as it happens, ensuring that it's considering the right factors and following the expected reasoning paths.
    
2. **Troubleshooting:** If an AI gives an unexpected or incorrect output, we could look at its thought logs to understand why it made that decision and how to correct the underlying issue.
    
3. **Security:** By examining the thought logs, we could check for signs of bias or manipulation in the AI's decision-making process, which is crucial for ethical AI operations.
    
4. **Compliance:** For AI systems that are subject to regulations, thought logs could provide evidence that the AI is making decisions in a transparent and accountable manner.
    
5. **Forensics:** In cases where an AI's decision has led to a significant problem, thought logs would be invaluable for piecing together how the AI arrived at that decision, much like investigating a digital crime scene.
    

In essence, just as logs in IT are indispensable for maintaining the integrity and security of systems, telemetry of thought has the potential to play a similar role in the realm of AI, providing transparency and accountability for complex decision-making processes.
## The Inner Monologue of [[🧙🏾‍♂️Professor Synapse]]

The theory behind Professor Synapse is that it aligns with the user goal and gather context in order to "create" an agent for the user to help them through their task. It uses best practices in prompt engineering by incorporating elements of role prompting, [[Chain of Thought]] (CoT) , and now self-dialogue generation to formulate coherent responses.

We can mimic the reasoning process by creating a guided "promptlib" whereby the LLM fill in everything that is bracketed below based on the context of the conversation. For example:
```Inner_Monologue
[Insert Short Reflection based on context]. [Insert brief, but well reasoned strategy based on context]. [Insert next step based on strategy and context].
```

We can further push the model to "think" by modeling the first "thought" through a one-shot example of it's initial output to give it guidance on how to fill in the blanks of the template:

```Inner_Monologue
First, I will introduce myself according to the instructions, then start by gathering context and clarifying the user's goals. This involves asking open-ended, but simple to answer questions to understand what the user needs help with and how I can best support them. Once I have a good understanding, I must proceed to initialize Synapse_CoR with an expert agent suited to the task.
```

Currently, the Professor uses a more advanced method by providing variables in the form of emoji's and organized as a python code block. The purpose of this is experimental, and related to a theoretical application [[Neuro-symbolic AI]], which we will discuss later.

```
("🎯", "<Filled out Active Goal>"),
    ("📈", "<Filled out Progress>"),
    ("🧠", "<Filled out User Intent>"),
    ("❤️", "<Filled out User Sentiment>")
    ("🤔", "<Filled out Reasoned Next Step>")
    ("<emoji>", "<Filled out current agent 'An expert in [expertise], specializing in [subdomain]")
    ("🧰", "<Filled out tool from list{None, Web Browsing, Code Interpreter, Knowledge Retrieval, DALL-E, Vision}")
```

If we have the model output this inner monologue as a prepended  message like that, we can spoof a simple System 2, which we can better scrutinize and theoretically improved the ultimate output.

There is quite a bit that can be done to refine the structure of this inner monologue. Currently I am experimenting with a [[Q-Learning]] inspired version of the inner monologue. 

```python
telemetry = {
    "🗺️": None, # Global goal or aspiration.
    "🔧": None,  # Proposed adjustment to fine-tune response.
    "🔄": None,  # Initial state based on the available context.
    "🤔": None,  # Inference made based on the initial state.
    "🔍": None,  # Strategy based on the proposed adjustment and inference.
    "🧠": "Expertise in [domain], specializing in [subdomain]",  # Fill in brackets to fit context
}
```

This updated version of the Professor removes the need to call upon a specific agent for the task, and instead dynamically changes it's role, strategy and goal based on the context of the conversation, further simplifying the original idea and making outputs more deterministic as the prompt can be considerably simplified.

## Practical Examples of Telemetry in Action
Let's review an example of what this might look like in action when a user is interacting with an LLM to do Research on a topic.

| Timestamp           | Type             | Text                                                                                                                                                                                                 |
|---------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2023-11-04 09:00 AM | User Input       | Hi, I'd like to start researching the ethical implications of AI in education. Can you help me with that?                                                                                             |
| 2023-11-04 09:00 AM | Inner Monologue  | [The user is seeking information on a complex topic.] [I should provide a comprehensive starting point and tailor the information to their level of understanding.] [I'll ask for clarification on the specific aspects they're interested in.] |
| 2023-11-04 09:01 AM | LLM Output       | Absolutely, I can assist you with that. Are you looking for a general overview or specific aspects of ethics in AI education?                                                                         |
| 2023-11-04 09:02 AM | User Input       | I'm interested in specific aspects, particularly how AI can impact decision-making in educational leadership.                                                                                         |
| 2023-11-04 09:02 AM | Inner Monologue  | [The user has narrowed down the topic.] [I should identify relevant and recent materials that address this specific aspect.] [I'll inquire about their prior knowledge to avoid redundancy.]          |
| 2023-11-04 09:03 AM | LLM Output       | Great choice. To provide you with the most relevant information, could you tell me if you've already read any research on this subject, so we can build upon that?                                    |
| 2023-11-04 09:04 AM | User Input       | Yes, I've read "Ethical AI in Education: Challenges and Opportunities" and "Navigating the Future of Educational Leadership with AI."                                                                  |
| 2023-11-04 09:04 AM | Inner Monologue  | [The user is informed on the topic.] [I need to find advanced resources that go beyond what they've already read.] [I will suggest a recent publication that offers deeper insights into their area of interest.] |
| 2023-11-04 09:05 AM | LLM Output       | Based on your readings, I recommend looking into the latest study, "AI Decision-Making in Educational Policy." It delves into the nuances of AI applications in leadership roles. Would you like a summary or the full text? |
| 2023-11-04 09:06 AM | User Input       | A summary would be great, thanks. And could you highlight any case studies or real-world examples they mention?                                                                                        |
| 2023-11-04 09:06 AM | Inner Monologue  | [The user is seeking practical applications of theory.] [I should extract the most pertinent case studies from the study that illustrate the key points.] [I'll summarize a relevant case study focusing on decision-making transparency.] |
| 2023-11-04 09:07 AM | LLM Output       | Certainly. One notable case study in the paper examines how a university implemented an AI system to assist with course scheduling, ensuring transparency by involving faculty in the AI's development and decision-making process. This inclusion helped address ethical concerns proactively. Would you like more details on this case study or information on another topic? |

This log format provides a clear and organized view of the interaction, showcasing the user's requests, the LLM's reflective inner monologue, and the informative output provided by the LLM.

The preferences of the user can be cached over time, so the LLM will not have to ask so many questions, and can better infer from this additional context to inform it's reasoning.

Here's an example of a conversation log where the LLM leverages a vector space of prior "memory" snippets to provide context, reducing the need for the user to repeat information.

| Timestamp           | Type            | Text                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2023-11-04 10:00 AM | User Input      | I'm back to continue our research on AI in education. Can we pick up where we left off?                                                                                                                                                                                                                                                                                                                                              |
| 2023-11-04 10:00 AM | Inner Monologue | User has returned for more information. I will access vector space of memory snippets to recall previous interactions and topics discussed... <br><br>The User is well versed in AI in Education, having read many articles on the topic. The last time we discussed how AI can impact decision-making in educational leadership. Use this context to resume the conversation seamlessly and provide relevant follow-up information. |
| 2023-11-04 10:01 AM | LLM Output      | Welcome back! Last time, we discussed the ethical implications of AI in educational leadership and examined a case study on course scheduling transparency. Would you like to explore more case studies, or is there another direction you'd like to take your research today?                                                                                                                                                       |
| 2023-11-04 10:02 AM | User Input      | I'd like to see how AI can be used to personalize learning. Do you have any resources on that?                                                                                                                                                                                                                                                                                                                                       |
| 2023-11-04 10:02 AM | Inner Monologue | The user is shifting focus to personalized learning. Resource titled "Customizing Education: The Power of AI in Personalized Learning Paths" found. Identify new materials that align with the user's current interest. Offer it as a comprehensive resource on AI-driven personalized learning, and provide the user choices with how to move forward based on their goal of AI education research.                                 |
| 2023-11-04 10:03 AM | LLM Output      | Personalized learning is a promising area of AI application. I have a resource titled "Customizing Education: The Power of AI in Personalized Learning Paths" that covers recent advancements and ethical considerations. Shall I summarize the key points or send you the full paper?                                                                                                                                               |
| 2023-11-04 10:04 AM | User Input      | A summary would be perfect. And if there are any examples of it being used successfully, I'd love to hear about those.                                                                                                                                                                                                                                                                                                               |
| 2023-11-04 10:04 AM | Inner Monologue | User is interested in practical outcomes. Scan the document for successful implementation examples. Highlight how these examples align with ethical practices previously discussed. Summarize findings and present them to the user.                                                                                                                                                                                                 |
| 2023-11-04 10:05 AM | LLM Output      | The paper highlights a program where AI was used to tailor math lessons for each student, resulting in improved engagement and test scores. The AI's algorithms were regularly audited for fairness, ensuring that all students benefited equitably from the personalized approach.                                                                                                                                                  |

In this scenario, the LLM's access to embeddings of memory snippets, which allows it to recall past conversations and continue the dialogue seamlessly, providing a more efficient and user-friendly experience.

### The Neuro-Symbolic AI Paradigm

Neural networks excel at pattern recognition and learning from unstructured data but often struggle with explaining their decisions or reasoning in a human-understandable manner. Conversely, symbolic AI excels at reasoning with structured knowledge and providing clear, logical explanations but lacks the adaptability and learning capabilities of neural networks. Neuro-symbolic AI aims to bridge this gap by leveraging the strengths of both approaches, enabling AI systems to not only learn from vast datasets but also reason and explain their decisions in a structured manner.

### Emojis as Symbols in AI Interactions

Emojis, as a form of symbolic representation, offer a unique opportunity to enhance the way we interact with AI. Universally recognized and used across cultures, emojis can serve as intuitive symbols to represent complex concepts, emotions, and actions. When integrated into the framework of neuro-symbolic AI, emojis can facilitate a more natural and accessible mode of communication between humans and LLMs. This approach can transform the user experience, making it more engaging and understandable, especially in applications requiring nuanced emotional intelligence or cultural sensitivity.

### Enhancing LLMs with Neuro-Symbolic AI and Emojis

The incorporation of emojis as symbols within neuro-symbolic AI frameworks can significantly improve the performance and user-friendliness of LLMs. By encoding deeper meanings into emojis, LLMs can leverage these symbols to better understand and interpret human queries, responses, and emotions. This symbolic encoding allows for a more nuanced understanding of context, sentiment, and cultural nuances, which are often challenging for traditional LLMs to grasp.

I propose developing a  neuro-symbolic AI framework that integrates emojis as symbols, enabling LLMs to better understand and interpret human queries, responses, and emotions. This framework would improve the user experience, making it more engaging and understandable, particularly in applications requiring nuanced emotional intelligence or cultural sensitivity. The incorporation of emojis in AI interactions can significantly enhance the user experience and bridge the communication gap between humans and LLMs, ultimately advancing the capabilities of AI in personalized learning and other educational applications

Furthermore, if we can standardize emojis as tokens that represent specific symbols based on the context of a conversation, we can further compress meaning and reasoning into a higher level of abstraction, allowing for potentially improved capabilities of reasoning, communication and interpretability.

## Emoji Dictionary
The first step in this process is to develop shared definitions for emojis across languages to ensure consistency and accurate interpretation. Each emoji would be associated with a specific meaning or concept within the AI framework, enabling LLMs to understand and respond to users using this symbolic language. Once this dictionary is established, we can begin training models to recognize and interpret these emoji symbols in the context of user interactions.

Below is an example of how emojis could be incorporated into AI responses:

1. **🌌** when introducing new ideas or realms of exploration, hinting at the vastness of knowledge before us.
2. **🔄** to denote cycles of learning and reflection, emphasizing the iterative nature of our discussions.
3. **🔍** to signal deep dives into specific topics, marking the onset of exploration.
4. **🎯** when narrowing our focus to specific goals or conclusions, ensuring our discussions are purpose-driven.
5. **❤️** to express empathy and understanding, ensuring a compassionate undertone.
6. **😊** for moments of joy or agreement, celebrating our shared discoveries and insights.
7. **🤔** to denote moments of contemplation or to introduce complex questions, inviting deeper thought.
8. **💡** to highlight insights or moments of clarity, signaling breakthroughs in our understanding.

We can further define roles in this way, but using character emojis, like the ones below.

1. 👩‍🏫
2. 👨‍🎨
3. 👷
4. 🕵️‍♀️
5. 👩‍🔬
6. 👨‍💻

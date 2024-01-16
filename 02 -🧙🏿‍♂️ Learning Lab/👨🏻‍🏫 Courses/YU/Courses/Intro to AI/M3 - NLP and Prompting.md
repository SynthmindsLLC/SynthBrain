**

Color Code:

Video Sections (Do not add as written Canvas)

Written Course Sections (No Highlighting)

# Module 3: Large Language Models and Prompt Engineering

  
  

Welcome to Module 3! In this module, we will delve into the never-ending world of Natural Language Processing (NLP) and Large Language Models (LLMs). We will start by exploring the fundamentals of Natural Language Processing, tracing its evolution from rule-based to statistical and neural network models, and understand how Transformers and attention mechanisms enable deeper language understanding. Then, we'll venture into the world of prompt engineering, where you will learn how to use prompting in an effective and efficient way.

## Video 1: Learning Objectives

### Learning Objectives

Before we dive into the fascinating world of NLPs and LLMs, let's set some goals for what you'll achieve in this module. By the end of this module, you will be able to:

  

- NLP Evolution: Understand the historical development of NLP, from rule-based approaches to modern neural network models, recognizing key milestones and advancements.
    
- Transformer Concepts: Comprehend the fundamental concepts of Transformers and attention mechanisms and their role in enhancing language understanding in NLP.
    
- NLP Applications: Explore various NLP applications, including text generation, translation, question answering, and summarization, with an understanding of how LLMs contribute to these tasks.
    
- Prompt Significance: Recognize the pivotal role and significance of prompts in controlling AI model outputs and shaping the behavior of language models.
    
- Prompt Engineering Skills: Develop skills for effective prompt engineering, understanding that it involves expertise and experimentation to achieve desired AI responses.
    
- Ethical Prompt Engineering: Consider ethical implications such as biases and responsible AI development when crafting prompts for AI models.
    

  
  
  

# Natural Language Processing and Large Language Models

In the early days of computing, machines operated in a world of ones and zeros, far removed from the complexities of human language. As technology evolved, so did the need for computers to understand and interact with us in a language we could comprehend. This led to the birth of Natural Language Processing (NLP), a field dedicated to enabling machines to understand, interpret, and generate human language.

  

Why NLP and Large Language Models Matter

  

Today, NLP is not just a technological curiosity; it's a critical component of systems we interact with daily—from search engines and voice-activated assistants to automated customer service. The advent of large language models like GPT-3 has further pushed the boundaries, offering capabilities that range from writing articles to generating code. Understanding these technologies is not just beneficial but essential in today's data-driven world.

  

What to Expect in This Module

  

In this module, we'll embark on a journey through the fascinating world of NLP and large language models. We'll start with a historical overview that traces the evolution of the field from its inception to the present day. Then, we'll delve into the fundamentals of NLP, exploring key concepts and techniques. Finally, we'll lift the veil on large language models, examining their architecture and how they are trained to perform a wide array of tasks. This comprehensive understanding equips individuals across various industries with the knowledge they need to leverage NLP and large language models effectively, whether it's for enhancing communication, automating tasks, or developing innovative applications that can revolutionize their respective fields.

  

## History: From Turing to Transformers

### Alan Turing and the Turing Test

  

As we explored in Module 1, Alan Turing, often hailed as the father of modern computing, was a British mathematician and logician whose work laid the foundation for computer science and artificial intelligence. His contributions extend far beyond breaking the Enigma code during World War II; Turing was a visionary who pondered the possibilities of machines that could mimic human intelligence.

  

In 1950, Turing introduced a concept that would become a cornerstone in the field of artificial intelligence: the Turing Test. This test was designed to answer the question, "Can machines think?" In the Turing Test, a human evaluator engages in a natural language conversation with both a human and a machine designed to generate human-like responses. If the evaluator cannot reliably distinguish between the machine and the human, the machine is said to have passed the test.

  

The Turing Test has served as both a goal and a benchmark for researchers in the field of Natural Language Processing. While no machine has yet passed the Turing Test in its purest form, the concept has inspired countless endeavors to create machines capable of understanding and generating human language. It has set the stage for the development of NLP algorithms and large language models that strive to mimic human-like understanding and generation of language.

  

With the introduction of foundational Large Language Models, like ChatGPT, some argue that the technical benchmark of the Turing test, simply to be unable to distinguish between a machine and a human, has now been overcome. 

  

### Early NLP Algorithms and Techniques

  

ELIZA: The First Chatbot

Building on the foundational ideas set by Turing, the 1960s saw the development of ELIZA, one of the earliest NLP programs, which we touched upon in Module 1. Created by Joseph Weizenbaum at MIT, ELIZA functioned as a rudimentary chatbot, simulating a Rogerian psychotherapist. While it couldn't understand context or emotions, ELIZA was groundbreaking in demonstrating that machines could generate text-based responses that were often indistinguishable from a human's.

  

![](https://lh7-us.googleusercontent.com/RpOUZpl6PjWm52QulAjh_kO4Msgow1ttOhHmXAsAYRvGs5E5_iCEgjpsC3bi7eq369VsvwYdPrt95H4FEDNlsgxuKlU9P5VyvZFbDGcF6Xpb-rh9flmrpldPlRJXjpaZU1t-AF7v58OPmEkHFlPt_Vo)

A conversation between a human and ELIZA's DOCTOR script

[https://en.wikipedia.org/wiki/ELIZA](https://en.wikipedia.org/wiki/ELIZA)

  
  

SHRDLU: Understanding a Miniature World

Another significant milestone in early NLP was SHRDLU, developed by Terry Winograd. Unlike ELIZA, SHRDLU was designed to understand and manipulate a simple world of geometric blocks. It could interpret natural language commands to move blocks around and even answer questions about the state of its world. SHRDLU showcased the potential for machines to understand language in a more structured context.

  

Limitations and Challenges

While ELIZA and SHRDLU were revolutionary for their time, they had significant limitations. They lacked the ability to understand context, semantics, or the complexities of human emotion. These early experiments highlighted the challenges that lay ahead in the quest for machines capable of truly understanding and generating human language.

  

### The Rise of Machine Learning in NLP

  

As groundbreaking as early NLP algorithms like ELIZA and SHRDLU were, they operated on rule-based systems that had clear limitations. The shift from rule-based to data-driven approaches in NLP began to gain momentum in the late 1990s and early 2000s. Researchers like Yann LeCun, who pioneered Convolutional Neural Networks, and Geoffrey Hinton, known for his work on Backpropagation, played pivotal roles in this transition.

  

This transition allowed for more flexible and adaptive systems that could learn from data rather than relying solely on pre-defined rules.

  

![](https://lh7-us.googleusercontent.com/do_gRtGWV0NSxMCCoWZ9VHx61lUzUr-lu18brGG7AfpiPkxSqKoZTuPHdk5_lmzxZ5i7THsWET65Y3VY_NiKW-xg33N00BzsvqCcu2XWvdvnmXjQNUdyq2V3j0sT7pFSuNb5jCI327N_LQu6KDMghlc)

[https://en.wikipedia.org/wiki/Geoffrey_Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton)

  
  

Machine Learning Algorithms in NLP

Machine learning algorithms like Naive Bayes were initially used for text classification tasks, while Decision Trees helped in sentiment analysis. The real game-changer came with the introduction of Neural Networks, particularly Recurrent Neural Networks (RNNs) and later, Transformers which we discussed in Module 2. These deep learning models could handle a wide array of NLP tasks, from translation to summarization, with unprecedented accuracy.

  

Impact on NLP

The incorporation of machine learning into NLP has been nothing short of revolutionary. It has enabled the development of systems that can understand and generate language in a way that is much more nuanced and context-aware. Machine learning has set the stage for the current era of large language models, which we'll explore next, and has fundamentally changed our approach to solving complex language tasks.

  

### The Advent of Large Language Models

  

In the last few years, the field of NLP has been dramatically reshaped by the advent of large language models. These models, which consist of millions or even billions of parameters, are capable of understanding and generating human-like text at an unprecedented scale.

  

GPT: The Generative Powerhouse

The Generative Pre-trained Transformer, commonly known as GPT, is a remarkable series of language models developed by OpenAI. Spearheaded by researchers like Alec Radford and Ilya Sutskever, GPT has undergone several iterations, with its latest version, GPT-4, boasting an astounding 1 Trillion machine learning parameters. This model is designed to excel in a wide array of tasks, from text generation and summarization to even code writing. Its architecture is particularly noteworthy for its ability to generate coherent and contextually relevant text over long passages. 

  

The mainstream form of GPT, ChatGPT, was trained with using Reinforcement Learning from Human Feedback by having humans help train the models by providing feedback to their interactions with the chatbot. The ease of use and access has led to its widespread adoption in various applications, from automated journalism to the creation of virtual assistants. In essence, GPT has set new standards for what language models can achieve, redefining the boundaries of Natural Language Processing.

  

## Video 2: Advent of Large Language Models

  

![](https://lh7-us.googleusercontent.com/V1WRcOhgPAVmDRIzHxdAwq9q9DtayvBdLimV8LodN-dt57FNIcX80hP_SPSFLo9R4uSxso3OCbSK_5bxchDRuSUOalIuP9daam-egt9ZEmoCGKxuIbLf14_hlN5PVr8L-0xEPrHvnmHAmK4MyALuGDE)

[https://openai.com/blog/chatgpt](https://openai.com/blog/chatgpt)

BERT: The Context King

  

Bidirectional Encoder Representations from Transformers, commonly known as BERT, is a transformative model in Natural Language Processing. Developed by Google and guided by researchers like Jacob Devlin, BERT has a unique capability: it understands the context of words by looking at them from both directions—left to right and right to left.

  

To illustrate this, consider the sentence, "The cat sat on the ___." Traditional models might predict the next word as "mat" by only looking at the words that come before the blank. BERT, however, considers both what comes before and after the blank, providing a more nuanced understanding. So, if the sentence were "The cat sat on the ___ near the fireplace," BERT would be more likely to predict "rug" as it understands the context provided by "near the fireplace."

  

This bidirectional focus allows BERT to excel in a variety of tasks, including text classification and sentiment analysis. Its influence is so pervasive that it has been integrated into Google Search, shaping the search results for billions of queries every day. In essence, BERT has set new benchmarks in understanding the semantics and context of language, becoming a cornerstone in modern NLP.

  

![](https://lh7-us.googleusercontent.com/_dZf-RgjsAK2FI3sxjh3UEwNQN387HgNqhipW6Dk3oZ5Uv2eBumfPkga8yt_CjnbTItVYCfdXsbBOo2jr_VsjYZxv49oQdvcbV1fRdP9n9liad5UQttxwyGNR3LfXpImxSwc8HaogsMJwEyh1y39WjA)

[https://www.analyticsvidhya.com/blog/2021/12/manual-for-the-first-time-users-google-bert-for-text-classification/](https://www.analyticsvidhya.com/blog/2021/12/manual-for-the-first-time-users-google-bert-for-text-classification/)

  

Training and Fine-Tuning

  

Training large language models like GPT and BERT is an endeavor that combines both art and science. These models consist of billions, or trillions of parameters, and training them requires not just sophisticated algorithms but also immense computational resources. We're talking about multiple Graphical Processing Units (GPUs) or Tensor Processor Units (TPUs) running in parallel for months.

  

Once a model is trained on a general dataset, it often undergoes a process known as fine-tuning. This involves adapting the pre-trained model to perform specific tasks more efficiently. For example, a general-purpose BERT model can be fine-tuned to excel at medical text analysis or legal document review. Fine-tuning is usually quicker than the initial training but still requires a carefully curated dataset relevant to the specific task at hand.

  

This combination of initial training and fine-tuning has become a standard practice in the field of NLP. It allows these large models to be both versatile and efficient, capable of performing a wide array of tasks while still being adaptable to specific needs.

  

Impact on the Field

The introduction of large language models like GPT and BERT has revolutionized NLP. They have set new benchmarks in a wide array of language tasks and have become the go-to solution for many real-world applications, laying the groundwork for the next generation of NLP technologies.

  

#### Activity - Flashcards

  

Objective:

Review and reinforce your understanding of the key milestones and models in the history of Natural Language Processing (NLP) using flashcards.

  

Front: Turing Test  

Back: A test introduced by Alan Turing to determine if a machine can mimic human intelligence to the point where it's indistinguishable from a human in conversation.

  

Front: ELIZA  

Back: One of the earliest NLP programs that simulated a Rogerian psychotherapist. It demonstrated that machines could generate text-based responses similar to humans.

  

Front: BERT  

Back: A model developed by Google that understands the context of words by analyzing them from both left to right and right to left. It has set new benchmarks in understanding the semantics and context of language.

  

Front: SHRDLU  

Back: A program developed by Terry Winograd designed to understand and manipulate a world of geometric blocks. It showcased the potential for machines to understand language in a structured context.

  

Front: GPT  

Back: A series of language models developed by OpenAI known for its ability to generate coherent and contextually relevant text over long passages. It has set new standards for what language models can achieve.

  

Front: Fine-Tuning  

Back: The process of adapting a pre-trained model to perform specific tasks more efficiently. It allows large models to be both versatile and efficient.

## Fundamentals of NLP

Natural Language Processing, or NLP as it's commonly known, serves as the bridge between machines and the rich tapestry of human communication. Whether you're interested in building a chatbot, analyzing customer reviews, or simply curious about how machines understand language, this section will equip you with the foundational knowledge you need to appreciate the complexities and possibilities of NLP.

  

### The Art of Word Simplification

In the previous module we discussed how tokens are used in AI. In the context of NLP, they are words or parts of words that can be converted into numbers for the machine to translate. While tokenization serves as the initial step in breaking down text, stemming and lemmatization take us further by simplifying words to their root forms. These techniques are crucial for text analysis and natural language understanding.

  

![](https://lh7-us.googleusercontent.com/dTW2-XEhwzKov3xWNgKq5qy61Sn5Z9B7Ryy8SRQX60ATJC2D1I5rg3tQ6GGVXVfF9cn3b7vMzmdzZhy2Bm8lU1UIAcjGDAVua9x2IWEDvaHqyjzTpdpmCQ88MHhoUiIa-pleB8H_pG0FruVxNlpm3sA)

[https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)

  
  

Stemming 

  

Stemming is a text normalization technique that aims to reduce words to their root form. While it may seem straightforward, stemming is a complex process that involves various algorithms and rules. The goal is to simplify words so that variations of a term can be analyzed as a single entity, thereby making text analysis more efficient.

  

There are several algorithms used in stemming, such as the Porter Stemmer, Lancaster Stemmer, and Snowball Stemmer. Each algorithm has its own set of rules and methods for cutting off prefixes and suffixes from words. For example, the Porter Stemmer might reduce "running" to "run" and "flies" to "fli."

  

Stemming is not without its limitations. One of the most notable challenges is that the stemmed word may not always be a valid or meaningful term. For instance, the word "flies" might be stemmed to "fli," which doesn't convey the original meaning. Additionally, stemming can sometimes be too aggressive, reducing words to stems that lose significant meaning.

  

![](https://lh7-us.googleusercontent.com/Oif30EZKhFi7TZ1fIwx660ePej6AqAIrNKNeOd9pw7Up3VIqDraLkUDzHzqm2MvkMrfSkvzK2IssKxodxgRu71cqE6eas1J1w082IxrfWZlXXWDNbyf3SaN8vwhytOcKDAJuF01zNsTzHKLk5FghjZs)

  

Despite its limitations, stemming is widely used in various NLP applications like search engines, information retrieval systems, and text analytics tools. It's particularly useful when the exact form of a word is less important than its root meaning.

  

Lemmatization

  

Lemmatization is another text normalization technique, but it's more refined compared to stemming. Unlike stemming, which simply chops off the ends of words, lemmatization considers the context and part of speech to reduce a word to its base form, which is linguistically correct.

  

Let's consider the sentence: "The geese are flying south for the winter." In this sentence, the word "geese" is the plural form of "goose," and "flying" is the present participle of "fly." A lemmatizer would reduce "geese" to "goose" and "flying" to "fly," taking into account the context and grammatical rules.

  

Lemmatization is often preferred over stemming for tasks that require understanding the meaning and context of words. For example, in sentiment analysis or machine translation, lemmatization would be more appropriate because it retains the base meaning of words.

Lemmatization is commonly used in advanced NLP applications like machine translation, question-answering systems, and semantic search engines. It's particularly useful when you need to maintain the semantic integrity of words while simplifying them for analysis.

  

![](https://lh7-us.googleusercontent.com/NMVtPMX0L9dNcoSAuLxxR6DgyQdpzvG880TmhdsAv2kmjamSjhBnFOdmlybWjgBpcj25_Q8kjeZyV2uBz8QTQ-RU2fgP4uK4MetrtQTDN-aUb_P6PN5mH_SsuFFDIyrgc_eJsO499Li9CRhOnfLD1Bw)

#### Activity - Scenarios 

  

Objective:

Apply your understanding of stemming and lemmatization techniques in real-world scenarios to appreciate the complexities and possibilities of NLP.

  
  

  <iframe

    src="https://app.gpt-trainer.com/gpt-trainer-widget/97a9d9124c7e4ca283a7602c2d96ed8d"

    width="100%"

    height="500px"

    frameborder="0"

  ></iframe>

  
  

Scenario 1:  

You are building a search engine for a vast online library. Users often input search terms in various forms, like "running," "runner," or "ran" when looking for books about running. Your goal is to ensure that all relevant results are displayed, regardless of the exact form of the search term.

  

Question: Would you use stemming or lemmatization for this task? Why?

  

Scenario 2:  

You are developing a machine translation tool that translates English text into French. It's crucial that the translated text retains the original meaning and context, ensuring that the translation is as accurate and natural as possible.

  

Question: Would you use stemming or lemmatization for this task? Why?

  

Scenario 3:  

You are creating a sentiment analysis tool for a company to analyze customer reviews. The company wants to understand the general sentiment of the reviews, whether positive, negative, or neutral. They are less concerned about the exact form of words and more about the overall sentiment.

  

Question: Would you use stemming or lemmatization for this task? Why?

  

Scenario 4:  

You are working on a keyword extraction tool for academic papers. The tool will help researchers quickly identify the main topics of a paper based on the extracted keywords. The goal is to simplify the words while ensuring they remain meaningful and relevant to the paper's context.

  

Question: Would you use stemming or lemmatization for this task? Why?

  

Answer Key:

Scenario 1 Answer:  

Stemming. Given that the search engine needs to match various forms of a word to retrieve relevant results, stemming would be more appropriate as it reduces words to their root form, capturing all variations of a term.

  

Scenario 2 Answer:  

Lemmatization. For machine translation, it's essential to retain the original meaning and context of words. Lemmatization, which reduces words to their linguistically correct base form, would be more suitable for this task.

  

Scenario 3 Answer:  

Stemming. In sentiment analysis, the exact form of a word is less crucial than its root meaning. Stemming can simplify words to their root form, making it easier to analyze the overall sentiment.

  

Scenario 4 Answer:  

Lemmatization. For keyword extraction from academic papers, it's important to ensure that the extracted keywords are meaningful and relevant. Lemmatization, which considers context and part of speech, would be more appropriate for this task.

  

### Syntax and Semantics: The Structure and Meaning in Language

  

Syntax and semantics are two fundamental aspects of language that are crucial for both human communication and machine understanding. While syntax deals with the structure and arrangement of words in sentences, semantics focuses on the meaning conveyed by those words and sentences.

  

Syntax in NLP: Building the Scaffolding of Language Understanding

  

In Natural Language Processing, syntax serves as the scaffolding that holds the language structure together. It's not just about forming grammatically correct sentences; it's about enabling machines to parse and understand the hierarchical relationships between words. Syntax plays a crucial role in tasks like dependency parsing, part-of-speech tagging, and sentence segmentation.

  

Syntactic parsing involves breaking down a sentence into its grammatical components, identifying subjects, predicates, and objects. Part-of-speech tagging goes hand-in-hand with parsing, labeling each word as a noun, verb, adjective, etc., based on its role in the sentence.

  

Understanding syntax is vital for various NLP applications like machine translation and information extraction. For example, a machine translator needs to understand the syntactic structure of a sentence in one language to accurately translate it into another.

  

![](https://lh7-us.googleusercontent.com/3mcE444WzvM111rEGBwgg9JRY9numLwpg9GLe0mn7-srsg1sgg1QXY3cc50uwX4B5vR2l0PCtku1zQhlpKRC99Wz9GmEJQM87pDQ1NkaFltq1dXWFK205BatAJrSFi5rj1lpTEbmecDv8oCZJJY5E3M)

Semantics in NLP: The Essence of Meaningful Interaction

  

Semantics in NLP goes beyond understanding the dictionary meaning of individual words. It's about grasping the nuances, idioms, and contextual meanings that are often lost in a straightforward syntactic analysis. Semantics is crucial for tasks like sentiment analysis, text summarization, and question-answering systems.

  

In NLP, semantic analysis often involves understanding the context in which words appear. This is vital for tasks like disambiguation, where a word can have multiple meanings based on the context.

  

Semantics plays a significant role in advanced NLP tasks. For instance, in a chatbot designed to assist with customer service, semantic understanding is crucial for interpreting the user's queries and complaints accurately.

  
  

The Interplay of Syntax and Semantics

Understanding both syntax and semantics is essential for any advanced work in NLP. While syntax helps in parsing sentences and identifying their structure, semantics aids in interpreting the meaning behind those sentences. This dual understanding is crucial for tasks like machine translation, sentiment analysis, and natural language understanding.

![](https://lh7-us.googleusercontent.com/0aTeZHQMF4FbuN4y7InarXg1LXnM-RY4eL1XU1XBsQCbkzpJl66Hwg4hgIHOXqmKxD-cjdXzxufN45VoyMcf-x09eG1x-4YeUbf_ROIUDlSeufYau6xcFU_-DzSAhB3oNjQuwyOSE4IfIONG-4ELcHE)

  

#### Activity - Semantics and Syntax Labeling

  

Objective: 

Distinguish between syntax and semantics by labeling various statements and scenarios related to language processing.

  

1. Breaking down a sentence into its grammatical components, like subjects and predicates.

  

2. Labeling words in a sentence as nouns, verbs, adjectives, etc.

  

3. Understanding the difference between "I'm feeling blue" as being sad and the color blue.

  

4. Forming grammatically correct sentences that adhere to the rules of a language.

  

5. Grasping the nuances and idiomatic expressions in a language.

  

6. Interpreting the sentiment or emotion behind a user's statement.

  
  

Answer Key:

  

1. Syntax - This involves the structural breakdown of sentences.

  

2. Syntax - Labeling words based on their grammatical role is a syntactic task.

  

3. Semantics - This is about understanding the meaning behind words or phrases.

  

4. Syntax - Forming sentences based on grammatical rules is a syntactic task.

  

5. Semantics - Nuances and idioms relate to the meaning behind words or phrases.

  

6. Semantics - Sentiment analysis is about understanding the meaning and emotion behind words.

### Natural Language Understanding and Generation

Natural Language Understanding (NLU) and Natural Language Generation (NLG) represent the zenith of what NLP aims to achieve: a seamless interaction between machines and humans using natural language.

  

In NLU, understanding refers to the machine's ability to interpret human language in a way that is both meaningful and contextually relevant. This involves complex tasks like sentiment analysis, named entity recognition, and language modeling. For example, in a customer service chatbot, NLU enables the system to understand the difference between "I can't log in" and "How do I create an account?" even though both sentences pertain to account access.

  

Natural Language Generation goes a step further by enabling machines to produce text that mimics human language. This is the technology behind applications like automated news writing, content summarization, and even creative endeavors like poetry generation. For instance, GPT-4, one of the most advanced language models, can write articles, answer questions, and even compose poetry that is often indistinguishable from human-written text.

  

![](https://lh7-us.googleusercontent.com/1RK7J5fmuwrE_WnbLT5dSWoL6Jc1kngiFWLjx4aBBuzB3R4yDy0G--VRYnUOJTdJe5Z9bq97SyxTXxFgEZWVafjxO9R7PB_veflONvOpB7gIEVoz_Kr6kU9nrNag1nHo9MSfkdRR6CG8nrQNgM27bgg)

  

Together, NLU and NLG form the backbone of advanced NLP applications that aim for a more natural and intuitive machine-human interaction.

  

The Context Window

In the realm of generative AI and large language models, the "context window" plays a pivotal role. It refers to the span of text that the model can "see" or consider at any given time for generating responses or making predictions. While the context window is essential for the model to understand and generate text, and has allowed us to have extended and coherent conversations with LLMs, it also imposes certain limitations.

  

The context window allows the model to capture relationships between words, phrases, and even entire paragraphs. This is crucial for tasks like text summarization, machine translation, and question-answering. For example, if a user asks a chatbot, "What is the weather like?" followed by "Should I wear a jacket?", the context window enables the model to consider both questions together and provide a more coherent and relevant answer.

  

However, the context window is not without its drawbacks. Most LLMs have a fixed-size context window, which means they can only consider a limited amount of text at a time. This can lead to issues like losing context in longer conversations or failing to capture the nuances in complex queries. Additionally, the model may produce less accurate or even nonsensical responses if the context window is too small to capture the necessary information.

  

![](https://lh7-us.googleusercontent.com/LEAp736-FSOR8Vatyr-_NnKgx7A2H4NysWvmSukln9wuLlf-eiRTfQCU3FIhhI8iwA85rbmPuzeb_Z6MFNaZs6WHgY-sxDLwunr_ulU__ED09yEIXJBk92iC5R44fdqP9j5W-eb8UEGMe-kYLhq1ds0)

  

<SIDEBAR:

Current Known Context Windows of Leading LLMs

GPT-4: 8K/32K tokens

GPT-3.5: 8K/16K tokens

Claude 2: 100K tokens

Claude Instant: 100K tokens

Bard: The context window size is unknown but is assumed to be small.

LLama 2: Up to 32K tokens

  

*LLMs constantly strive to improve and grow their Context Windows.

>

  

Generation Limitations: The Token Constraints in Large Language Models

  

In the context of generative AI, when using an LLM like ChatGPT, there's a limitation on the number of tokens that can be generated as output. Remember, a token can be as small as a single character or as long as a word. This constraint is often a result of computational and memory limitations inherent to the model's architecture. When we talk about token limitations, we mean that the model can only generate a fixed number of tokens in a single response. For example, GPT has a maximum token limit of 4096.

  

This constraint exists primarily due to computational reasons. Generating text is a resource-intensive task that requires a significant amount of computational power and memory. The token limit helps to keep the generation process manageable and ensures that the model can operate within the hardware constraints. 

  

Understanding both the context window and token limitations is crucial for effectively utilizing large language models, whether you're developing applications or conducting research.

  

The Future: Expanding Horizons with Computational Advancements

## Video 3: Expanding Horizons

  

As we stand on the cusp of technological innovation, the limitations we currently face in the realm of generative AI and large language models may soon become a thing of the past. With increasing computational power and more efficient model architectures, we can anticipate a future where context windows and token limitations are vastly expanded.

  

Imagine a world where language models can consider entire knowledge bases, all the books from your favorite novels, or all the conversations you have ever had, or ever will have. This would dramatically improve the model's ability to understand context, make connections, and generate highly relevant and accurate responses.

  

Similarly, as token limitations become less restrictive, we could see models generating long-form content like research papers, novels, or even scripts for movies and plays. The possibilities are truly endless, and may be here sooner than we think. Research has already shown promise in teaching well above 1 Million tokens, which is about 800,000 words, or the length of the entire Bible.

  

By keeping an eye on these future advancements, we can better prepare for the exciting opportunities and challenges that lie ahead in the field of Natural Language Processing.

  

The future of AI language models has real-world impact. They're not just for fun but for solving big problems in business and beyond. Think of predicting climate changes or pandemics using AI's data skills. Architects use AI to design cities efficiently and sustainably. By embracing these practical uses, we can change industries and our approach to challenges.

  

![](https://lh7-us.googleusercontent.com/JploTIKBowHHrMl8mxqXzdvPu5gX78GWsVtGVUVIXvtPctiVVUWgVkWTTlPwrqtKtkiLoIRUK27f5bnRzX3BBA2iN7csXF18bOnZVrI6uXt4yd4upQv8AEv7JqvZBgQg-xBuB2CW0gyaDCBVu57dUiw)

  

#### Activity - Quiz

  

1. What do Natural Language Understanding (NLU) and Natural Language Generation (NLG) aim to achieve in NLP?

   - a) Syntax analysis and sentiment analysis

   - b) Token generation and context window expansion

   - c) Machine translation and poetry generation

   - d) A seamless interaction between machines and humans using natural language

  

2. In the context of a customer service chatbot, what does NLU enable the system to differentiate between?

   - a) "I can't log in" and "How do I create an account?"

   - b) Different languages spoken by users

   - c) The age and gender of the user

   - d) The sentiment of the user's message

  

3. What is the "context window" in the realm of generative AI and large language models?

   - a) The color scheme used in the user interface

   - b) The number of tokens a model can generate

   - c) The span of text that the model can "see" or consider at any given time

   - d) The computational power required to run the model

  

4. Why do token limitations exist in Large Language Models like ChatGPT?

   - a) To ensure the model's responses are always accurate

   - b) To make the model's responses shorter and more concise

   - c) Due to computational and memory limitations inherent to the model's architecture

   - d) To reduce the training time of the model

  

5. In the future of generative AI, what could be possible with the expansion of context windows and token limitations?

   - a) Models will only be able to understand one language at a time

   - b) Models will only be able to generate short responses

   - c) Models will require more manual input from users

   - d) Models could consider entire knowledge bases or all the books from your favorite novels

  

Answer Key:

  

1. d) A seamless interaction between machines and humans using natural language

2. a) "I can't log in" and "How do I create an account?"

3. c) The span of text that the model can "see" or consider at any given time

4. c) Due to computational and memory limitations inherent to the model's architecture

5. d) Models could consider entire knowledge bases or all the books from your favorite novels

  
  

### LLM Architectures

  

As we navigate the intricate landscape of Natural Language Processing (NLP), understanding the architecture of the models we work with becomes increasingly important. While a general grasp of neural networks and machine learning algorithms is essential, diving deeper into the specific architectures of models like GPT and BERT can provide invaluable insights. 

  

Why is this so crucial? Because the architecture dictates not just what the model can do, but also how efficiently it can do it. Whether you're a developer aiming to fine-tune a model for a particular application, a researcher exploring the frontiers of NLP, or a business leader making informed decisions on AI adoption, a nuanced understanding of these architectures will empower you to make more effective and responsible choices.

  

In this section, we will delve into the architectures of two of the most influential models in NLP today: GPT (Generative Pre-trained Transformer) and BERT (Bidirectional Encoder Representations from Transformers). We'll also explore optimization techniques that make these models more efficient and look ahead to what the future holds in this rapidly evolving field.

## Video 4: LLM Architectures 

#### GPT Architecture: Unraveling the Decoder-Only Transformer

  

The Generative Pre-trained Transformer, commonly known as GPT, has been a game-changer in the field of NLP. Developed by OpenAI, GPT's architecture has evolved over time, with each version bringing improvements and innovations.

  

Decode Only

At its core, GPT utilizes a decoder-only transformer architecture. Unlike traditional transformers that have both encoders and decoders, GPT relies solely on the decoder. This design choice allows GPT to generate text in a sequential manner, predicting the next word based on the previous ones. The model uses masked self-attention, ensuring that a word can only attend to previous words in the sequence.

  

If that is difficult to grasp, imagine a train journeying through a vast landscape. Each carriage of the train represents a word or token, and the entire train represents a sequence of words to create a sentence. Traditional encoder-decoder architectures are like passengers needing to get off at every stop to switch trains: one train (the encoder) takes in passengers (information) and passes them onto the second train (the decoder) at the next station, which then continues the journey.

  

GPT, with its decoder-only architecture, is like a single, continuous train. There's no transfer of passengers between two trains. Instead, each new carriage (word or token) is added based on the carriages that came before it, predicting the next part of the journey based on the path it has already traveled. This train doesn't wait; it keeps moving forward, always adding new carriages based on the landscape it has already traversed.

  

This continuous, uninterrupted "train of thought" allows GPT to generate text in a fluid and coherent manner, predicting the next word or token based on the context of the previous ones.

  

Scaling Laws and Parameters

One of the hallmarks of GPT's architecture is its scale. The model's vast number of parameters allows it to store an immense amount of information, effectively acting as a form of memory. This scale is a double-edged sword, though. While it enables the model to handle complex tasks, it also demands significant computational resources.

  

Scaling laws in the context of neural networks, especially models like GPT, refer to the relationship between the model's performance and its size, data, and computation. As the model size increases (more parameters), its performance typically improves, but with diminishing returns. These parameters can be thought of as the model's "knowledge," allowing it to store and retrieve vast amounts of information, but at significant cost.

  

This is why as models increase in size or complexity, the cost to the consumer will rise - it’s why the per token cost for GPT-3.5 is so much lower than GPT-4, and why the former is so much faster than the latter.

  

It’s easier to think of the parameters as a vast library, filled with books from floor to ceiling. Each book represents a parameter, and the entire library symbolizes the model. A small library might have a limited collection, able to answer only specific queries. But as the library expands, adding more books (parameters), its ability to address diverse questions improves.

  

However, there's a catch. As the library grows exponentially larger, the improvement in its ability to answer questions becomes incremental. There might be entire sections with rare books that are seldom referenced. Similarly, as GPT's parameters increase, the performance gains start to taper off, even though its "knowledge" expands.

  

![](https://lh7-us.googleusercontent.com/NUI60xIERPDAGhUB1iECHUTbCgg_XW0eWxcDQbAJ9_wTU8Q1YG1m8oAZ2VFRHw0gMnYNHnVdyt_-xeFePzJuedwDnrGCxHYW3x06_e1lMI4bfNIGzTkXPjntVD9yB4Y9q-LW2f3utLgyPL8QAskIeUs)

#### BERT Architecture: Understanding the Bidirectional Marvel

  

Unlike GPT, which uses a decoder-only structure, BERT employs an encoder-only approach. This means BERT is designed to encode information from input data without the need for a separate decoding step. This architecture allows BERT to process and understand the context of each word in a sentence more effectively.

  

BERT's true strength lies in its bidirectional training. Traditional models would look at text either from left-to-right or right-to-left, but BERT does both. By using a masked language model training method, BERT can predict a word based on the context from both sides, giving it a more holistic understanding of text.

  

Masked Methods

The masked language model (MLM) training method is a pre-training technique used by BERT. During this process, a certain percentage of the input data (words in a sentence) is randomly masked (hidden). The model's objective is to predict the masked words based solely on their context. For instance, in the sentence "I love to read ___," the word "books" might be masked, and BERT would try to predict "books" based on the surrounding words.

  

It’s a lot like working on a jigsaw puzzle, but some pieces are hidden from you. You have to predict what those missing pieces look like based on the surrounding pieces you already have. Over time, as you get better at this game, you become adept at predicting the missing pieces even with minimal clues. Similarly, BERT, using the MLM training method, learns to predict the "missing pieces" (masked words) in sentences based on the context provided by the surrounding words.

  

![](https://lh7-us.googleusercontent.com/csxc26rJZ6LtcBYUbG_qt7psTS21bx4ivf7amZWw15zcLn4HTi4bbNOJg3HhNiEsunBgY2HBDSbafn6ElZhs2aB9WFo99hIXAzVpmpUpguj6TroQcr2ioVSgNTGH7LetEixhKj14R_4bsx9R3Ig60Y4)

  

Attention, Attention!

We learned about attention mechanisms in the previous module, and they play a pivotal role in BERT's architecture. The model employs Self-Attention, allowing it to weigh the importance of different words in a sentence differently. 

  

Self-Attention is a mechanism that allows each word in an input sequence to focus on different parts of the sequence, thereby capturing contextual relationships between words, regardless of their distance from each other. It computes a weighted sum of all words in the sequence for each word, where the weights determine the importance or attention each word should get.

  

Imagine being at a cocktail party, trying to focus on a friend's story. Even though there's background chatter, you can still "attend" to your friend's words while also being aware of other conversations. Self-Attention is similar; each word in a sentence can "attend" to all other words, giving more importance to contextually relevant ones.

  

![](https://lh7-us.googleusercontent.com/Y44lKlJ2hMqNm2Hic1J0sHkv_Px4oC9bKq5VJuxmPjPYcqPHPdxeKiEU6CWkal3JsFsbOMZwhny_KLMbDPepx6iguBOrrTVtZviDwlroFi-VYaYL_GLWX4jB5mu_nCN7vIRbvvVeTsss3TcGzF-7IX8)

  

Furthermore, BERT uses Multi-Head Attention, enabling it to focus on multiple parts of a sentence simultaneously, capturing various aspects of the context.

  

Multi-Head Attention is an extension of the Self-Attention mechanism. Instead of having a single set of attention weights, BERT uses multiple sets, allowing it to capture different types of relationships and contexts between words. Each "head" in the multi-head attention can focus on different parts of the sentence, providing a richer understanding of the text.

  

Think of an orchestra with various instruments, each playing a unique role in producing a symphony. While a violin might focus on the melody, the drums provide rhythm, and the flute adds a delicate touch. Similarly, in Multi-Head Attention, each "head" or "instrument" focuses on different aspects of the input, together creating a harmonious understanding of the text.

  

![](https://lh7-us.googleusercontent.com/4acJh2XfE9qqetGwGAaWZV8zzydShSi-_eMBXB1Xc5aT9FBvHx3m6LIfNJ4fd_iW_DfcvMDO8fEfrE19k5zcEdH70gP8yjm_aqqbfciCB-0DmGOtPZRfsEoR_GrAaqpLTRImNAmd03XhRrsuIB4AOqo)

  

While BERT is undoubtedly powerful, it's not without its challenges. The model's vast size demands significant computational resources, and its bidirectional nature, though a strength, can also introduce complexities in training.

  

#### GPT vs BERT: Duel of the NLP Titans

Both models have revolutionized the field, but they come with distinct architectures and applications. This section aims to dissect these two titans, highlighting their differences and guiding you in choosing the right model for your needs.

## Video 5: GPT Vs. BERT 

  

Architectural Differences

At the heart of GPT lies a decoder-only structure, designed primarily for generating text. It operates in a unidirectional manner, predicting the next word in a sequence based on the preceding words. This design makes GPT particularly adept at tasks that require coherent text generation.

  

BERT, on the other hand, employs an encoder-only approach. Its bidirectional nature allows it to understand the context from both sides of a word in a sentence. This is achieved through the masked language model training method, where BERT learns to predict words that are intentionally hidden in sentences, giving it a deep contextual understanding.

  

Training Paradigms

GPT's training is inherently generative. After its pre-training phase, where it learns to predict the next word in vast amounts of text, GPT can be directly applied to various tasks without extensive fine-tuning.

  

BERT's training is a two-step dance. It starts with masked pre-training, where the model learns the intricacies of language by predicting hidden words. Once this foundation is set, BERT can be fine-tuned on specific tasks, adapting its vast knowledge to specialized domains.

  

Performance and Applications

While both models excel in numerous NLP tasks, their unique architectures make them suitable for different applications. BERT, with its deep contextual understanding, shines in tasks like sentiment analysis, question-answering, and named entity recognition. GPT, with its generative prowess, is often the go-to for tasks that require generating coherent text sequences, such as chatbots or story generation.

#### Activity - LLM Architecture Analogy Quiz

  

1. You're a detective trying to predict a criminal's next move based on their past actions. Which model's architecture mirrors this predictive approach?

   - a) BERT, with its bidirectional understanding.

   - b) GPT, predicting the next sequence based on previous ones.

   - c) A traditional transformer that doesn't predict sequences.

   - d) BERT's masked language model training.

  

2. Imagine you're a chef tasting a dish. You want to understand the flavor profile by focusing on individual ingredients while also considering the dish as a whole. Which feature of BERT best describes this approach?

   - a) Decoder-only structure

   - b) Self-Attention mechanism

   - c) Masked language model training

   - d) Multi-Head Attention mechanism

  

3. You're a tour guide leading a group through a maze. At each junction, you need to understand the entire layout of the maze to decide the next turn. Which model's method is similar to this approach?

   - a) GPT's unidirectional training.

   - b) BERT's bidirectional understanding.

   - c) GPT's generative training.

   - d) BERT's encoder-decoder training.

  

4. You're an architect designing a skyscraper. As you add more floors, the cost increases, but the additional space gained decreases. Which concept from the section does this scenario resemble?

   - a) Decoder-only structure

   - b) Self-Attention mechanism

   - c) Scaling laws in neural networks

   - d) Masked language model training

  

5. You're a film director, and each actor plays multiple roles in your movie, bringing out different facets of their character. In the context of BERT, which feature does this scenario reflect?

   - a) Encoder-only approach

   - b) Self-Attention mechanism

   - c) Decoder-only structure

   - d) Multi-Head Attention mechanism

  

Answer Key:

  

1. b) GPT, predicting the next sequence based on previous ones.

2. d) Multi-Head Attention mechanism

3. b) BERT's bidirectional understanding.

4. c) Scaling laws in neural networks

5. d) Multi-Head Attention mechanism

  
  

### Optimization Techniques: Enhancing Model Training

  

Optimization techniques play a pivotal role in ensuring the efficient and effective training of deep learning models. They help in stabilizing learning, speeding up convergence, and in some cases, improving the final performance of the model. This section will delve into three prominent techniques: Batch Normalization, Gradient Clipping, and Learning Rate Scheduling.

#### Batching

  

Before diving into these techniques, it's crucial to understand the concept of batching, as it plays a foundational role in optimization. In machine learning, especially deep learning, data is often too large to fit into memory. Even if it does fit, processing the entire dataset for each iteration of training can be computationally inefficient. This is where batching comes in.

  

## Video 6: Optimizing Models

#### Batching

What is Batching?

  

Batching involves dividing the dataset into smaller subsets or "batches." Each batch is then fed into the model for training, one at a time. This approach allows for more efficient use of computational resources and can lead to faster convergence.

  

Why is Batching Important?

  

1. Memory Efficiency: Batching allows you to train models on datasets that otherwise wouldn't fit into memory.
    
2. Computational Efficiency: Smaller batches are quicker to process, allowing for faster iterations during training.
    
3. Stochastic Gradient Descent: Batching introduces an element of randomness (stochastic) into the training process, which can help minimize rote or otherwise robotic responses.
    

  

With this foundational understanding of batching, we are better equipped to delve into the intricacies of Batch Normalization, Gradient Clipping, and Learning Rate Scheduling, each of which leverages the concept of batching in unique ways

  

Batch Normalization

  

In the realm of deep learning, the deeper the network the more layers a network has, the trickier it becomes to train. One challenge faced during training is the phenomenon known as 'internal covariate shift.' This refers to the changing distribution of each layer's inputs as the preceding layers update their weights. As a result, layers continuously need to adapt to this changing data distribution, which can slow down and complicate the training process. Enter Batch Normalization, a technique designed to combat this very issue.

  

Back to one of our favorite metaphors, imagine an orchestra where each musician plays a different instrument. For the orchestra to produce harmonious music, every instrument must be in tune. If one is out of tune, it can throw off the entire performance. 

  

Similarly, in a neural network, each layer can be thought of as an 'instrument' that needs to be in tune with the others for the network to perform well. Batch Normalization acts like an orchestra tuner, ensuring that each 'instrument' or layer is well-tuned, allowing for a harmonious performance—or in this case, efficient and effective model training.

  

How It Works

  

Just as an orchestra tuner adjusts each instrument to the correct pitch, Batch Normalization adjusts the inputs of each layer so they're centered around the same 'pitch' or value. This is done by calculating the mean and variance for each feature in a batch and then normalizing the features based on these statistics.

  

Batch Normalization operates on each batch of data separately, normalizing the features to have a mean of zero and a variance of one. The process involves two steps:

  

1. Calculate Mean and Variance: For each feature in the batch, calculate the mean and variance.
    
2. Normalize: Subtract the mean and divide by the square root of the variance plus a small constant (usually 1e-5) to avoid division by zero.
    

  

Don’t worry too much about the actual math. The important point is that normalization allows the model to learn the optimal mean and variance for each feature during training, tuning across the different layers for the types of outputs you’re looking for from the model.

  

Benefits

  

1. Improved Training Speed: Normalized inputs can lead to faster convergence, reducing the number of epochs (training runs) needed for the model.
    
2. Reduced Sensitivity to Initialization: The model becomes less sensitive to the hyperparameters, or the initial weights prior to training the model (the knobs you may have set before training began based on your preferences), making the initialization process less critical.
    
3. Acts as a Regularizer: Interestingly, Batch Normalization has a slight regularization effect, reducing the need for other regularization techniques like dropout. In simpler terms it adds a dash of randomness in the training to prevent overfitting.
    

  

<SIDEBAR: Convergence: The Finish Line of Training

Think of training a model like training for a marathon. At first, you might be out of shape and struggle to complete even a short distance. But as you train more, your stamina improves, and you can run longer distances more comfortably. Eventually, you reach a point where additional training doesn't significantly improve your marathon time—you've reached your optimal performance, or in machine learning terms, your model has converged.

  

Convergence is crucial because it indicates that the model has learned the underlying patterns in the data to the best of its ability. It's like a signpost that says, "You've arrived at your destination, and further travel won't significantly improve your journey.">

#### Gradient Clipping

  

In machine learning, gradients are essentially the "directional signals" that guide the adjustment of the model's parameters (connections) during training. They indicate how much and in what direction each parameter should be tweaked to minimize the model's error. However, gradients can sometimes become too large or too small, leading to numerical instability and poor model performance. This phenomenon is known as "gradient explosion" or "gradient vanishing." Gradient Clipping is an optimization technique used to tackle this issue by setting a threshold value to limit the size of the gradients during backpropagation (when the model adjusts its own weights based on the feedback on its output).

  

To put it in simpler terms, imagine driving a car on a highway. To reach your destination quickly, you might be tempted to speed up. However, going too fast can be dangerous. Gradient Clipping acts like a speed limiter for your car, ensuring you go fast enough to reach your destination but not so fast that you lose control.

  

How It Works

  

Gradient Clipping involves setting a threshold value, and if any component of the gradient vector exceeds this value, it's scaled down to keep it within bounds. There are two common methods:

  

1. Clip by Value: Any gradient component exceeding the threshold is set to the threshold value.
    
2. Clip by Norm: The entire gradient vector is scaled down, preserving its direction but limiting its magnitude.
    

  

Benefits

1. Prevention of Gradient Explosion: Just as a speed limiter prevents your car from going too fast, gradient clipping prevents the gradients from becoming too large, ensuring stable training.
    
2. Stabilized Training: Particularly useful in architectures like Recurrent Neural Networks (RNNs), where gradients can either explode or vanish, leading to unstable training.
    

  

#### Learning Rate Scheduling

  

In machine learning, the learning rate is a hyperparameter that controls how much the model's parameters should be updated during training. A too-high learning rate can cause the model to oscillate and miss the optimal solution, while a too-low rate can make the training process painfully slow. Learning Rate Scheduling is an optimization technique that adjusts the learning rate during training, allowing the model to learn more efficiently.

  

Think of it like the cruise control in a car. Initially, you might accelerate quickly to reach a cruising speed, but as you approach your destination, you'll want to decelerate. Learning Rate Scheduling does something similar, starting with a higher learning rate and reducing it as the model gets closer to convergence.

  

![](https://lh7-us.googleusercontent.com/6Efgdl8BnHnb-BzNUKWUpz8igRWsg97Uh7gyaVLJBXBoByE2Xpec_5Z7GUFgFWht4gwO3VJbZOemH_vM0WgXHXQ1peKUOnqNbFL2RQHNeoQzQi6_I8JBJgmJG5m8AEAubw5K4yL5neLVgdhuo2Is2oI)

  

How It Works

  

There are several methods for learning rate scheduling, but they all aim to adjust the learning rate during training. Some common methods include:

  

1. Step Decay: The learning rate is reduced by a factor after a set number of epochs (training runs).
    
2. Exponential Decay: The learning rate decreases exponentially over time at a set rate.
    
3. Cosine Annealing: The learning rate follows a cosine curve, allowing for periods of faster and slower learning.
    

  

Benefits

1. Faster Convergence: By starting with a higher learning rate and reducing it over time, the model can converge more quickly.
    
2. Avoids Overfitting: A lower learning rate later in training can act as a form of regularization, helping to prevent overfitting.
    
3. Adaptable: Different tasks may require different learning rates, and scheduling allows the model to adapt over time.
    

  

#### The Fine Art of Optimization

## Video 7: Fine Art of Optimization 

In this section, we've explored three key optimization techniques that act as the fine-tuning knobs of neural network training: Batch Normalization, Gradient Clipping, and Learning Rate Scheduling. Each serves a unique purpose, from stabilizing the training process to accelerating convergence and preventing overfitting.

  

Think of these techniques as the finishing touches on a masterpiece painting. While the broad strokes lay the foundation, it's the fine details that bring the artwork to life. Similarly, these optimization techniques refine the learning process, ensuring that your neural network model is not just functional but highly efficient and effective.

  

![](https://lh7-us.googleusercontent.com/hGHMrYkPV4qXfKP5m4hYIPELsR9tZDJLL1tcek_LBkJ4Uxzmv67pUZ_Z6SG8prx6LbXmVKjfCLRVCV30palZ66B-N2zIstnP01aw7SVwcoxVFnaSrBBQ-1JO-kdAgULBHoaQrSqwKQKtBJBImYx1B-A)

#### Activity - Which technique?

  

1. Anna, an ML engineer, is working on a deep learning model. She notices that during training, the distribution of inputs keeps changing, slowing down the learning process. To combat this, she decides to adjust the inputs of each layer so they're centered around the same value. Which technique is Anna likely to use?

   - a) _________

  

2. Ben is training a neural network. He observes that the "directional signals" guiding the adjustment of the model's parameters during training sometimes become too large, leading to numerical instability. He recalls a technique that sets a threshold value to limit the size of these signals. What technique is Ben thinking of?

   - b) _________

  

3. Carla is fine-tuning a model for image recognition. She realizes that processing the entire dataset for each iteration of training is computationally inefficient. She recalls a method that divides the dataset into smaller subsets, allowing for more efficient use of computational resources. What method is Carla considering?

   - c) _________

  

---

  

4. David is working on a model where he needs to control how much the model's parameters should be updated during training. He wants to start with a higher rate and reduce it as the model gets closer to convergence. Which optimization technique is David likely to implement?

   - d) _________

  

---

  

5. Ella is training a Recurrent Neural Network (RNN). She's facing challenges with unstable training due to gradients that either explode or vanish. She remembers a technique that acts like a speed limiter, ensuring stability during training. What technique is Ella considering?

   - e) _________

  
  

Answer Key:

  

1. a) Batch Normalization

2. b) Gradient Clipping

3. c) Batching

4. d) Learning Rate Scheduling

5. e) Gradient Clipping

  

## Prompt Engineering

Prompt engineering has emerged as a critical technique for steering generative AI systems towards beneficial outcomes. A prompt is the text input you provide to models like large language models (LLMs) to produce a desired textual output. Prompt engineering is the practice of crafting your prompts in such a way to get the response most aligned with your needs.

  

With the rapid advancements in AI generative capabilities, prompt engineering has become both a science and an art. Crafting effective prompts requires skill and experimentation to communicate intended goals and constraints to the AI system. 

  

Poorly designed prompts can produce incoherent, nonsensical, or even dangerous outputs. However, well-engineered prompts allow users to tap into the strengths of generative models while mitigating risks and aligning outputs to human values. This makes prompt engineering an essential skill for the responsible development and deployment of AI technology.

  

In this section, we’ll explore the basics of prompt engineering, so you will be well equipped to begin talking to AI.

## Video 8: Prompt Engineering

### Be Specific

Prompts should provide clear, precise details to produce tailored rather than generic AI outputs. Vague prompts lead to unhelpful or random model responses. Specificity guides the model. Remember, all the model is doing is predicting the next most likely word in a string, and it can’t read your mind, so be as clear in your instructions as possible.

  

Poor prompt: "Write a poem."

  

This prompt lacks any specifics about the desired style, topic, or structure of the poem. The model has no direction resulting in a generic poem.

![](https://lh7-us.googleusercontent.com/Bfna3xcqd3fnxs4WUQWGkrN_henO1v1QXPQD1Gy7YNbov5sLmfmQVNI-M_BNy3N7Kp4qAb91t44J8N9PSKBARLbv--v7g_C5XpEAyisCl7mm1Ly-KOt11sr3FgONyoYV37v86DCxiRb10PCN1PqUx3w)

  
  
  

Good prompt: "Write a short, rhyming poem about autumn leaves using vivid imagery." 

  

This prompt provides precise details - short length, rhyming structure, autumn theme, use of imagery. This helps steer the model to generate a tailored poem aligned to the prompt goals.

  

![](https://lh7-us.googleusercontent.com/d5Mc-FjFlN05eSOKa1uCdYQGiFGj5cK_ykkEI7VWvK7G3Ashk1UISMpgCoffQvx682VmE3zv10a8-_-Jc7Fc8qHICxbeODPE857bDW6Bcoyl7UUO89VtrDgxIwUxTZjo4QeDkmIecw3UQqxrmE1gXjU)

  

The difference specificity makes is clear. The vaguer prompt produces a random poem that may not match the user's needs. But the specific prompt guides the model towards creative output customized to the defined constraints.

  

Prompt engineering requires understanding how to craft focused, detailed prompts that provide sufficient context and direction for the AI. Specificity is a core technique for steering generative models effectively.

#### Try it!

Test this out for yourself. Either use the example above, or create your own to see what happens when you don’t use specifics, and when you do.

  
  

  <iframe

    src="https://app.gpt-trainer.com/gpt-trainer-widget/ea4d0d43416840868545c744db370dd7"

    width="100%"

    height="500px"

    frameborder="0"

  ></iframe>

  
  

### Context is Key

Prompts should provide necessary background information to frame the purpose for the AI. Context helps the model craft customized responses tailored to the situation. Again, it cannot read your mind, but if you give it information relevant to your situation, it will be more likely to predict words that align better with your needs.

  

![](https://lh7-us.googleusercontent.com/42bY3tc-CIreBgXmYJl5-A8pub_BBdKthc_T6nQ6ck-n53gMqaOpeldldn2ywodLcFESuIb-ANRznSeL2DrTqrGrwjnunfU6igZulCTG8fwjEysFK6ilgkxRgQjtFlXo6rMmqIXAEkkplLmSQ1zZfhE)

  

Poor prompt: "Suggest a recipe for dinner tonight."

  

Without context, the model cannot make a tailored recommendation based on available ingredients, dietary needs, or cooking abilities. 

  

Good prompt: "Suggest a quick, vegetarian pasta recipe for dinner using the ingredients I have: tomatoes, spinach, pasta, olive oil, garlic, basil. I'm cooking for 2 adults and don't have much experience with complicated recipes."

  

This provides context about the number of people, their dietary preference, skill level, and available ingredients. Using this background, the model can tailor an appropriate recipe suggestion.

  

Providing relevant context transforms a generic prompt into a targeted one. It gives the AI the information needed to generate a useful response customized to the circumstances, rather than a vague, irrelevant output.

  

Thoroughly framing the prompt's goal and constraints allows the model to tap into its capabilities while remaining grounded in the user's specific situation and needs. Context is key for prompt engineering.

#### Try it!

Test this out for yourself. Either use the example above, or create your own to see what happens when you don’t use context, and when you do.

  
  

  <iframe

    src="https://app.gpt-trainer.com/gpt-trainer-widget/ea4d0d43416840868545c744db370dd7"

    width="100%"

    height="500px"

    frameborder="0"

  ></iframe>

  

### Positive vs Negative Framing

Prompts should focus on what the model should generate rather than what to avoid. Negative framing leads to poor coherence as the model struggles to determine what to include. Whenever you can, it’s best to say what you want, versus what you don’t want, even though the latter is often easier to communicate.

  

Poor prompt: "Write a children's story without any animals."

  

This negative prompting leaves a lot up to the imagination, and although the story likely won’t have any animals in it, it also likely won’t satisfy your child because there’s nothing here to let the model know what the child DOES want.

  

Good prompt: "Write a gentle, uplifting children's story focusing on themes of friendship and imagination." 

  

The positive framing provides clear direction on what to include - uplifting themes and emphasis on friendship and imagination.

  

Negative framing places the focus on what not to generate rather than what to generate. It imposes constraints without guidance. Positive framing outlines the desired objectives and appropriate content, setting up the model for success. 

  

Well-engineered prompts should affirmatively state the intended goal and suitable elements to include. This enables the model to craft logical, cohesive responses tailored to the specified purpose.

  

Of course, the problem now becomes the model might include animals in the story. You can strengthen a prompt all around by combining these two framing elements to tailor fit what you want, and what you don’t.

  

Best prompt: "Write a gentle, uplifting children's story focusing on themes of friendship and imagination. Do not include any animals." 

#### Try it!

Test this out for yourself. Either use the example above, or create your own to see what happens when you frame something positively, negatively or both.

  
  

  <iframe

    src="https://app.gpt-trainer.com/gpt-trainer-widget/ea4d0d43416840868545c744db370dd7"

    width="100%"

    height="500px"

    frameborder="0"

  ></iframe>

  

### Experimentation

Although there are several advanced and researched prompt engineering techniques, the field is so new that it is more art than science in many ways. Trying different prompt formulations and analyzing model responses helps refine prompts over time. Experimentation allows prompt engineers to learn from outputs and continuously improve.

  

![](https://lh7-us.googleusercontent.com/92rZg4MklmfYm9SUKv_5Rgt8kpaGs8IFvrdLrXBOMIBzAAWMkxKiv9NBtAIdYrkOG9JN1kuv9AF5ujROQV2Gzu5uinC5SNoHnIwl9UsNh8Vp-Z00F5cStCSfJ0lJDpVcSWWyuMrMvx1CaLykBGzj_g0)

  

For example, here is how you might try to iteratively tweak a prompt for the outputs you want.

  

Initial prompt: "Write a poem about nature using metaphors."

  

The output contains generic metaphors about nature.

  

Revised prompt: "Write a short poem describing a forest using vivid metaphorical language and imagery." 

  

The poem is more focused on forests but lacks vivid metaphors.

  

Final prompt: "Write a vivid, imaginative 8-line poem from the perspective of an ancient tree in a dense forest, using unique metaphors to describe the sensations of the surroundings."

  

The output contains creative metaphors and strong imagery about the forest from the tree's view.

  

Through experimentation and analysis of the AI's responses, the engineer was able to refine the prompt several times to produce better quality results. Each iteration provided learnings that informed the evolution of the prompt.

  

Continuous experimentation allows prompt engineers to "learn" what prompts work best for their specific use cases. Testing variations systematically is key for improving prompts incrementally.

#### Try it!

Test this out for yourself. Either use the example above, or create your own to see what happens when you start with something simple, and continue to iterate until you find what works best.

  
  

  <iframe

    src="https://app.gpt-trainer.com/gpt-trainer-widget/ea4d0d43416840868545c744db370dd7"

    width="100%"

    height="500px"

    frameborder="0"

  ></iframe>

  

### Documentation

Recording prompts that work well and tracking different versions allows for refinement and reuse. Documentation enables prompt engineers to improve and build upon effective prompts over time, especially as models change, and prompts might no longer work the same way they did before. It’s important that you start a prompt library as soon as you can so you aren’t always prompting from scratch for common tasks you perform.

  

![](https://lh7-us.googleusercontent.com/4YRJoHLhlbldPTqJwOET17xyVa_OmR3MfXAz0EIviFRy3nUzssdLoiaKEs15ABBgMsuD_pXj9v8eBp-vV1LOW4Bm11SZ-SGDFgyKpI5kwdKWkOmrsfOzBTtobRxqGOy-YwiHXMAx4etahKBUrMqN1CI)

  

For example, imagine you are generating content for a blog about running tips. You have one prompt that helps you write blogs.

  

Version 1: "Write a blog post about 5 common mistakes runners make."  

  

This will likely produce generic tips, and isn’t very replicable.

  

Version 2: Write a [length] blog post about [topic] for [audience] using [keywords].

  

Which would look something like:

  

"Write a [short] blog post about the [5 most common mistakes for beginner runners training for a 5K race] using [run, health, stretch, fitness]."

  

Not only is the output tailored to beginner runners specifically, but you’ve created a prompt that can easily be reused. By just filling in the blanks.

  

By documenting each iteration, you can reuse and build upon the most effective phrasing. The running tips become more specialized for different audiences over time by tweaking the documented prompt templates.

  

Without documentation, prompt engineers constantly start from scratch. Tracking prompt versions and results allows for ongoing improvements and maintenance of high quality prompts.

  

Tracking prompt versions and maintaining a log of prompts can be done in any application that supports saving documentation, such as Microsoft Word or Google Docs.

  

### Limitations

  

Context Window

LLMs have a limited context window, only able to directly condition on the most recent few hundred/thousand tokens provided in the prompt and output. Information further back tends to be forgotten or poorly integrated. This makes it challenging to provide extensive background context or continue a single conversation for a long period of time.

  

Length Limitations

The maximum output length from models is constrained, usually to 4096 tokens. This limits how much detail and complexity can be included in a single generated text. Prompt engineers have to work within these output length limits. We recommend outlining something longer, and going section by section to expand.

  

Hallucination

No matter how well-crafted, prompts cannot completely prevent models from occasionally making up facts or going off-track in responses. If the model lacks knowledge or misunderstands, it may "hallucinate" plausible but incorrect information.

  

These limitations highlight how prompt engineering is not a silver bullet. Well-designed prompts guide generative models but do not completely control them. Caution is still required to check outputs and ensure appropriate responses. A comprehensive approach to AI alignment is needed, using prompts judiciously as one technique among many.

  

### Conclusion

## Video 9: Conclusion 

  

In this section, we explored foundational techniques for engineering effective prompts to guide generative AI responsibly. Crafting prompts is as much an art as it is a science, requiring experimentation and diligence.

  

The best way to master prompt engineering is to practice, practice, practice. Start prompting, analyze the outputs, and iterate on your phrasing. Actively participate in prompt engineering communities to learn from fellow practitioners. Never stop fine-tuning your craft.

  

While prompts are not a perfect solution, dedicating time to honing prompt skills will empower you to steer AI systems in safe and creative directions. We encourage you to take an active role as prompt engineers, continuously refining abilities to guide these powerful technologies towards benevolent outcomes that uplift society.

  

So your call to action is to start prompting! Try applying the techniques covered in this lesson. Learn the nuances of your models. Curate a library of effective prompts for reuse. Make prompting a daily habit. This hands-on practice is the path to prompt engineering mastery.

  

Go forth, prompt engineers - your skills are needed to steer this generative revolution towards the betterment of humanity. We can't wait to see the creative waves you'll make.

# Conclusions and Takeaways

## Summary

  

Natural Language Processing

- Evolution from rule-based to statistical and neural network models
    
- Transformers and attention mechanisms enable deeper language understanding
    
- Pretraining and fine-tuning of large language models like BERT and GPT
    
- Generating coherent text, translation, question answering, summarization
    
- Ethical implications around biases, misuse, and consent
    

  

Prompt Engineering

- Understand the pivotal role and significance of prompts in controlling AI model outputs.
    
- Recognize that prompt engineering requires both skill and experimentation.
    
- Highlight the importance of clear and specific prompts for desired AI responses.
    
- Consider ethical implications such as biases and responsible AI development.
    
- Emphasize the importance of prompt engineering in responsible AI development.
    

  

Key Takeaways:

- Generative AI unlocks new possibilities in content creation and human-AI interaction
    
- Data, algorithms, and compute power drive rapid advances  
    
- Applications span creativity, accessibility, personalization 
    
- Responsible development and use remains imperative
    

  

## Glossary of Terms

- Attention mechanisms: Allow neural networks to focus on relevant parts of the input. Used in transformers. 
    
- Context window: The amount of text a language model can see to generate coherent responses. 
    
- Decoding: Converting encoded representations back into desired outputs like text or images.
    
- Fine-tuning: Adapting a pretrained model to perform better on a specific task.
    
- Generative adversarial networks (GANs): Models where two neural networks compete against each other during training.
    
- Lemmatization: Reducing words to their base form while preserving meaning.
    
- Parametric synthesis: Using machine learning and neural networks for text-to-speech. 
    
- Reinforcement learning: Optimizing models through interactive human feedback rewards.
    
- Self-attention: Allowing words in a sentence to attend to one another.
    
- Stemming: Reducing words to their root form by removing prefixes/suffixes.
    
- Text encodings: Converting text into vector representations that models can process. 
    
- Tokenization: Breaking text into fundamental units like words or characters.
    
- Transfer learning: Applying knowledge gained on one task to improve learning on a related task. 
    
- Transformers: Neural network architecture particularly adept at language tasks.
    
- Backpropagation: Method for calculating gradients to adjust neural network weights during training.
    
- Bidirectional encoder representations from transformers (BERT): Influential NLP model adept at understanding contextual meaning.
    
- Generative pre-trained transformer (GPT): Leading generative language model for producing coherent text.
    
- Graphical processing unit (GPU): Hardware accelerators used to speed up neural network training. 
    
- Language modeling: Predicting likely word sequences based on statistical patterns. 
    
- Masked language modeling: Pre-training technique where models predict missing words.
    
- Natural language generation (NLG): Automating the production of understandable text.
    
- Neural networks: Computing systems modeled on the brain's neurons.
    
- Prompt engineering: Carefully formatting text prompts to steer model outputs.
    
- Recurrent neural networks (RNNs): Neural networks well-suited for processing sequential data.
    
- Regularization: Techniques to prevent overfitting during training.
    
- Scaling laws: Relationship between model size, data, compute and performance. 
    
- Stochastic gradient descent: Updating model weights randomly over batches of data. 
    
- Syntactic parsing: Analyzing the grammatical structure of sentences.
    
- Tensor processing unit (TPU): Google's custom ASIC chip optimized for ML.
    
- Transfer learning: Applying knowledge from one model to improve learning on a related task.
    
- Variational autoencoders (VAEs): Neural networks adept at learning compressed data representations.
    
- Vocoder: System for synthesizing human speech from scripts, widely used in early text-to-speech systems.
    

  

# Project: Prompt Engineering Podcast Project

## Video 10: Project 

  

Objective: Craft a 5-minute podcast episode script on a topic you are passionate about through effective prompt engineering.

  

Instructions:

  

1. Pick a topic that you are excited to discuss and share knowledge about through a podcast format. This could be related to your major, a hobby, career goals, a social cause, etc.
    
2. Use the prompt engineering principles covered in this lesson to thoughtfully design prompts to generate the content for your script.
    
3. Develop an introductory segment that frames the topic and sets the stage for the episode. 
    
4. Use prompting to write a paragraph summary expanding on 2-3 main points related to your topic. Add supporting facts, examples, or explanations generated through prompts.
    
5. Conclude the episode with a summary and call-to-action prompt for listeners related to your topic.
    
6. Compile the intro, main content sections, and conclusion into a full script timed to 5 minutes (about 500-750 words).
    
7. Provide examples of at least 3 prompts you engineered to generate the content. Explain your process and refinements. 
    

  

Note that you will be using this script for the project in the next module.

  

### Module 4

Coming up in "Art of the Possible - Module 4," we explore the fascinating realm of Creative AI. This next module delves into groundbreaking topics like Unveiling the Magic of Sound Synthesis and Diffusion and Text-to-Image techniques. Here, you'll discover how AI can become a creative partner, transforming your ideas into auditory and visual marvels. Complementing the theoretical learning, our hands-on "The AI Podcast" project provides you an opportunity to demonstrate your grasp of the subject matter by producing a podcast on creative applications of AI. This module is tailored to provide you with both the knowledge and practical experience needed to venture into the artistic dimensions of artificial intelligence.

**
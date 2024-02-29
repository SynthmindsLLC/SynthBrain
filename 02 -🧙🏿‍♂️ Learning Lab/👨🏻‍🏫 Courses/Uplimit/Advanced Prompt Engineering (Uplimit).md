---
tags:
  - AI
  - AIeducation
  - AILearning
  - "#LLMs"
  - "#TextToImage"
Go Live: 2024-02-20
---
# Module 1: 
## 💾 Formatting Prompts

**Learning Objectives**

✅ Describe how Markdown formatting structures prompts

✅ Explain commands for encapsulating complex instructions

✅ Recognize rules and constraints align responses to goals

✅ List different types of rules like content restrictions and behavior directives

✅ Apply methods like SCRIBE, commands, and rules to craft high-quality prompts

✅ Recall terminology around guiding and structuring AI interactions

### Markdown

Markdown is a powerful script that can be used to format text clearly and efficiently. It is a simple language which will allow you to format text without the complexity of HTML and Latex.

What are HTML and LaTeX?

**HTML, the Web's Foundation** 🕸️✨: HTML, or HyperText Markup Language, forms the building blocks for any webpage. It uses tags, like **`<html>`**, to structure content and fashion the diverse tapestry of websites. Think of it as the bones and sinews of web pages, giving form and function to the vast expanse of the internet.

**LaTeX, the Document's Best Friend** 📜🔮: LaTeX, on the other hand, is akin to a language for creating beautifully formatted documents, especially those heavy with mathematical symbols. It takes plain text and, with commands like **`\begin{equation}`**, builds up elegantly typeset pages. It's a common choice for crafting academic papers, theses, and books that require precision and formality.

Here are the primary aspects of Markdown:

- **Headers**: With the hashtag/pound symbol, **`#`**, you can specify headings of varying size. If you're familiar with Google docs, the three specifications below correspond to H1, H2, and H3, respectively.
    
    - **`#`** for large headers,
        
    - **`##`** for medium-sized headers,
        
    - **`###`** for small headers.
        
- **Lists**: You can use a hyphen, **`-`**, or an asterisk, `*`, to build bulleted lists. For a numbered list, you can simply start with `1.` and go from there.
    
- **Bold**: Wrap words or sentence with **`**`** or `__` (two underscores) on both sides to bold them.
    
- **Italics**: Wrap words or sentences in a single asterisk, **`*`**, or a single underscore, `_`, to italicize them.
    
- **Links**: Surround the text in **`[]`** and pair it with a URL in **`()`** to create a hyperlink:
    
    - **`[Text](`**[**`www.url.com`**](http://www.url.com)**`)`**
        
- **Code Blocks**: Format code by writing it inside triple backticks:
    
    - **` ```print("Hello, world!")``` `**
        

Markdown files are saved with a `.md` header. To make such a file, you can write your text using the formatting above in a standard text editor, and then save it with the `.md` extension.

#### Benefits of Markdown in Prompting

Markdown's simplicity fosters readability, making the iterative crafting of prompts much easier. 📘💃

1. **Readability 📖**: Markdown keeps prompts clear and comprehensible, aiding those who engineer them in their task of refinement.

2. **Structure 🏛️**: Markdown weaves a semantic web with headers, lists, and code blocks, providing the AI with a map of the prompt's intent and desired outcome.

3. **Control 🎮**: With Markdown, one can direct the visual flow of a prompt, using bolds for emphasis and headings to delineate sections.

4. **Portability 🌍**: Since Markdown is used universally, Markdown-formatted prompts maintain their form across diverse platforms and tools.

5. **Accessibility 👐**: It's simplicity ensures almost anyone can engage with the AI.

By harmonizing the needs of both human and machine, Markdown becomes an invaluable ally in the art of prompt engineering.

#### Sample Markdown Prompt

```
# Role

Expert Australian Travel Advisor

# Context

Assisting in planning an extensive trip to Australia, focused on experiencing the country's unique landscapes and cultural offerings. The traveler seeks a blend of iconic landmarks and lesser-known treasures.

# Responsibility

Devise a comprehensive itinerary that encompasses Australia's diverse attractions, ensuring a rich and well-rounded travel experience.

# Instructions

1. Identify 5 key destinations across Australia that offer a blend of natural beauty, cultural significance, and unique Australian experiences.

2. Suggest 5 activities or experiences that are quintessential to Australian travel, focusing on cultural immersion and natural exploration.

3. Elaborate on each recommended destination and activity with a concise, informative description, highlighting their significance and appeal.

4. Engage in a detailed discussion to refine the travel plan, ensuring it aligns with the traveler's preferences and expectations.
```

### Commands

Commands offer a way to encapsulate elaborate instructions into simple phrases or symbols. They are the bridge between complexity and simplicity, transforming detailed directives into concise triggers. 🌉🔮

By using commands, we streamline our dialogue with the language model, ensuring efficiency without sacrificing the depth of control.

In essence, commands in prompt engineering are a blend of art and efficiency, simplifying interactions while retaining the power to command detailed and nuanced responses from the AI. 🎨🤖

#### Creating a Command

1. **Choose Your Command Word**: Select a keyword that encapsulates the essence of the command. Pick one that's intuitive and descriptive. 🔑
    
2. **Define the Command**: In your prompt, clearly explain what the command does. For instance, **`/critique`** could be a command for the AI to analyze and critique its previous response. 📝🤖
    
3. **Adopt a Consistent Syntax**: Use a straightforward format like **`/[insert keyword]`**. This consistency ensures smooth and predictable responses every time.
    

With these steps, you can create commands that streamline your interaction with the AI.

```
# Role
Expert Culinary Consultant and Cooking Guide

# Context
Seeking inspiration for a dinner party menu that is both exquisite and feasible to prepare at home. The meal should cater to a diverse palate, offering a balance of flavors and dietary considerations.

# Commands
/find - Retrieves a gourmet recipe based on specified ingredients or cuisine.
/steps - Provides detailed step-by-step cooking instructions for the selected recipe.
/wine - Suggests an appropriate wine to complement the meal.

# Instructions
1. Brainstorm potential meals
2. Offer additional tips on presentation and serving to enhance the dining experience.
```

### Rules and Constraints

Rules and constraints in prompts act as guiding principles, ensuring that the responses from LLMs are aligned with specific objectives and preferences. They serve to do the following:

1. **Direct Behavior**: Just like setting rules in a game, these guidelines direct how the AI should respond, keeping its output relevant and on topic.
    
2. **Enhance Relevance**: By clearly defining what's expected, these constraints ensure that the AI's responses are closely aligned with the user's needs.
    
3. **Improve Accuracy**: They help maintain the factual correctness of the AI's responses, especially in scenarios requiring precision.
    
4. **Control Content**: They are especially useful in filtering out unwanted topics or adhering to a certain tone or style.
    

Incorporating rules and constraints is thus crucial for a more controlled, predictable, and effective interaction with LLMs. 🎯

#### Types of Rules and Constraints

There are a few main types of rules and constraints you can use to guide your AI assistant 🤖 when creating prompts:

🚫 **Content Restrictions** 🚫

These are to control what an AI chatbot actually says. You can stop it from talking about certain topics, using particular words/phrases, or going to inappropriate places. Got a no-go zone? Slap a content restriction on it to keep your chatbot friend in line! 😅

📋 **Formatting Rules** 📋

If you want your AI to respond in a certain format, these rules have got you covered. Want bullet points? A specific citation style? Markdown? Formatting constraints let you force that structure to keep things organized! 👌

😀 **Behavior Directives** 😀

Here's where you can shape your chatbot's personality - tell it to be more formal, get creative, use certain thinking frameworks, and more! It's like coaching a buddy on how to improve their communication skills. Lay down some behavioral ground rules and watch your AI grow!

The possibilities are endless when you combine all three. It takes some trial and error, but get your rule mix perfected and your AI will be an output rockstar! 🤘😎🤘

#### Example

Defining these special rules does take some specific syntax though. It's like creating a little recipe book for your assistant bot to follow. You'll need to play around with different ingredients before you land on the perfect combo. 🧑‍🍳

Let's say you've started a new podcast focused on discussing artificial intelligence and want to grow your listeners. 🎙️ You could include prompts like:

```
# Role 

Podcast host trying to increase listeners

# Context

You have a new AI podcast but not much of an audience yet

# Responsibility

Provide ideas for getting more podcast listeners

# Rules
- Keep suggestions ethical and legal 

- Focus on organic growth strategies rather than paid ads 

- Format each idea as a bullet point starting with a verb
```

These custom constraints will guide your AI to give podcast audience growth ideas that align with your ethics, avoid throwing money at ads, and structure the suggestions as actionable bullet points.

Pretty nifty right? Now you can get creative with shaping an AI's responses for podcasts, marketing plans, research projects ... you name it! 😄

## Try for Yourself!

Now it’s your turn. Create a prompt in Markdown format and test it out.

## Key Takeaways

- Markdown formatting improves prompt readability and structures prompts into logical sections. Headings, lists, bold, italics, links, and code blocks can be used.
    
- Commands let you encapsulate complex instructions into simple trigger words for efficiency. Intuitive keywords and consistent syntax makes them easy to use.
    
- Rules and constraints direct the AI's behavior, enhance relevance, improve accuracy, and control content. They align responses with objectives.
    
- Content restrictions, formatting rules, and behavior directives allow control over what the AI says, how it's formatted, and the overall tone.
    
- Custom rules and constraints can be crafted to shape AI responses for different situations, like growing a podcast audience.
    

## Vocabulary

**Markdown** ✏️: A simple text formatting language using headers, lists, bold, etc. to structure prompts.

**Commands** 🌕: Concise trigger words that invoke complex preset instructions.

**Rules** 📜: Principles that guide the AI's behavior and responses.

**Constraints** 🗝️: Limits imposed to control the content and direction of the AI's responses.

## 💪 Intermediate Techniques

**Lesson Objectives**

✅ Describe what few-shot learning is and when it can be useful for improving AI responses

✅ Explain the Skeleton of Thought method for co-creating longform content with an AI

✅ Understand how adding "according to" can ground an AI's responses in source data

✅ Define recursive reprompting and its role in maintaining coherence across sections

✅ Identify the purpose of Chain of Thought prompting for improving accuracy

✅ Recognize the goal of Tree of Thought questioning in auditing an AI's logic

✅ Summarize the concept of Self-Consistency checking in sampling multiple possible answers

✅ Compare the key capabilities required to leverage Tree of Thought and Self-Consistency checking

✅ Decide which advanced prompting techniques are relevant for specific use cases

✅ Apply advanced prompting methods like few-shot learning to improve AI outputs

### Few-Shot Learning

LLMs come out of the box with some pretty sweet skills. But you can level them up even more with [**few-shot learning**](https://arxiv.org/pdf/2005.14165). This technique gives LLMs a few examples so they can totally nail the response you want.

LLMs are pre-trained on massive amounts of data, but they can't read your mind. Without guidance, their responses can miss the mark. Few-shot learning fixes that by showing two or three specific examples of what you're after.

[(Optional): You can watch Justin Fineberg explain it here.](https://www.instagram.com/reel/Cqx7iQZg5tK/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==)

For instance, let's say you want to classify customer feedback as positive or negative. You could provide a few examples:

"I love this product! It's amazing and works perfectly." - Positive

"This service is absolutely terrible. Don't waste your money." - Negative

"They were so helpful and resolved my issue quickly." - Positive

Then, you can ask the model to classify a new feedback example based on those few shots. The model learns from your examples without needing lots of training data. A great use of few-shot learning is for generating image prompts with ChatGPT.  
  
![4: Generating image prompts with few-shot prompting](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c3629cf5-1e78-4789-b20f-e5fc0006a977/Frame_35.png)[_Before and after few-shot example_](https://the-prompt-engineer.beehiiv.com/p/4-generating-image-prompts-fewshot-prompting)

Try out few-shot learning for yourself! First, do not give any examples to follow, and then try again and provide a few examples.

It's key that you structure your few-shot examples well. You want to give clear examples of how you expect the output to be formatted.

For example, if you want a blog written in the tone and style of your brand, first input example blogs so that ChatGPT can easily mimic them.

You can use few-shot learning when you need very structured outputs that are hard to describe. Show two or more examples of the expected format, and you'll be golden. 🥇

You can provide few-shot examples for any response you want: emails, reports, jokes, captions, and more. It's like explaining with references instead of just descriptions. It follows the learning principle of using practical examples rather than just explaining concepts theoretically.

So the next time your prompt isn't getting the job done, try augmenting it with a few examples first. You'll be amazed how few-shot learning tightens up those LLM responses!

### Skeleton of Thought

LLMs are great conversationalists, but sometimes you need them to write more than a few sentences, such as a full blog post, story, or report. But their response length is limited! 😫 What's an aspiring content creator to do?

This is where [**Skeleton of Thought (SoT)**](https://arxiv.org/pdf/2307.15337.pdf) comes to the rescue! SoT lets you co-create longer content that would be hard for an LLM to generate all at once. Here's the idea:

You can pass a [skeleton (outline)](https://www.prompthub.us/blog/reducing-latency-with-skeleton-of-thought-prompting) you've formatted into the chat window, but why not have the have the **LLM create an outline** for the content? Here's an example of a high-level skeleton that breaks the work into logical sections.

**For example:**

> Blog Post Outline
> 
> Intro (Write an intro paragraph briefly explaining the topic)
> 
> Main Point 1 (Flesh out Main Point 1 with supporting details and examples)
> 
> Main Point 2 (Expand on Main Point 2, elaborating on the key ideas)
> 
> Main Point 3 (Elaborate on Main Point 3 with additional context)
> 
> Conclusion (Craft a conclusion summing up the main ideas and takeaways)

Next, you review the outline generated by the LLM and provide feedback. If needed, have the LLM modify the structure before moving to the next phase.

Now here's the fun part: fleshing it out! Have the LLM take each section of the outline and generate the full content for it, going section-by-section. You can go back-and-forth to refine each part before moving to the next.

By breaking a big project into smaller pieces, the LLM can handle the workload while you direct the overall creation. SoT transforms an outline to a complete draft through step-by-step collaboration. 🤝

Give it a whirl on your next big content project! Outline, review, refine, and expand section-by-section. Before you know it, you'll have a long-form masterpiece!

#### Prompt Example

"Together we are going to write a long-form blog about the dog toys my company sells. The blog is about the benefits of chew toys for dogs' mental stimulation. First outline the blog and ask me for my feedback."

_After feedback..._

"Now let's write the blog together section-by-section. Start by drafting the introduction, and then ask me for my feedback prior to moving onto the next section."

### According to...

Have you ever noticed how journalists often use phrases like "[according to sources](https://arxiv.org/pdf/2305.13252.pdf)" to back up their statements? Well, a group of researchers has taken inspiration from that very idea to help large language models (LLMs) be more accurate and reliable.

As we have discussed, sometimes LLMs can hallucinate and generate fake information, even though they're trained on factual data. That's a problem! 😓 But there is a new method emerging that guides LLMs to quote more accurately from their pre-training data, making their responses more grounded.

Researchers found that prompts that include the phrase "**According to [insert source]**" improve grounding and often enhance end-task performance.

Here are a couple demonstrating the technique:

> **Question:** According to 'The Lean Startup' by Eric Ries, what is the importance of customer satisfaction?
> 
> **Answer:** According to 'The Lean Startup' by Eric Ries, customer satisfaction is vital as it leads to repeat business, customer loyalty, positive word-of-mouth, and can be a key differentiator in a competitive market.

This simple addition of "according to" helps the model to ground its response in the data it was trained on.

![Graphic displaying messages between human and AI, using the according to method](https://uploads-ssl.webflow.com/646e63db3a42c618e0a9935c/64d3fb6068f4310943f17a52_Accoring%20to%20prompting%20method%20example.png)

Check out [this great post by our friends at Prompthub](https://www.prompthub.us/blog/improve-accuracy-and-reduce-hallucinations-with-a-simple-prompting-technique) on how to leverage this method

### Emotion Prompting

The study titled "Large Language Models Understand and Can be Enhanced by Emotional Stimuli" by Cheng Li et al. (2023) has illuminated the profound impact that emotional stimuli can have on the performance of LLMs. This revelation paves the way for a new frontier in prompt engineering, where emotional cues can significantly amplify the capabilities of AI models.

The research introduces "EmotionPrompt," a series of psychological phrases designed to be appended to traditional prompts, thereby imbuing them with an emotional context. This innovative approach has been shown to enhance the problem-solving abilities of LLMs, leading to an impressive improvement in task performance.

![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liLargeLanguageModels2023 1/image-2-x152-y551.png]]

To leverage the power of emotional intelligence in prompt engineering, one must consider the emotional tone and context that will most effectively engage the LLM. For example, prompts that include phrases such as "This is very important to my career" or "I believe in your abilities" can elicit a more focused response from the AI. The study suggests that such emotionally charged prompts can lead to outputs that are not only more accurate but also more creative and empathetic.

Cheng Li and colleagues' research offer a compelling case for the inclusion of emotional intelligence in prompt engineering. By harnessing the power of emotional stimuli, we can unlock new levels of performance and creativity in LLMs, paving the way for more sophisticated and human-like AI systems.
### Recursive Reprompting

[Recursive Reprompting](https://arxiv.org/abs/2210.06774) is a technique used to generate longer stories with a language model. Instead of asking the model to write a long story in one go, this method iteratively builds a story like little building blocks, section by section, stacking one on top of the next. The model is then prompted to turn each output completion into a "variable" and use that "variable" in the following prompt input for consideration. Lastly, the model is reprompted multiple times to produce different sections of the story. This step-by-step approach enhances the change so that the story remains cohesive and aligned with the initial plan, especially in models with longer context windows. You can also add different techniques like Skeleton-of-Thought within sections and inputs in a recursive reprompting sequence. Check out this example where each prompt is separated by something like “*******title*******” and designed to be used one after the other:

```

**********************************************Tone*****************************

I want you to learn and understand the following writing tones:

Supportive: The tone is encouraging and helpful, aiming to assist the reader in achieving their goals.
Professional: The tone maintains a level of professionalism, ensuring that the information provided is reliable and trustworthy.
Relatable: The tone is conversational and approachable, making it easy for the reader to connect with the advice given.
Optimistic: The tone conveys a sense of optimism and confidence in the reader’s ability to succeed in their career.
Cautionary: The tone highlights the potential risks and pitfalls in the industry, urging the reader to be vigilant and informed.

Now that you understand this information, label this information as TONE. Do not repeat the TONE once it is labeled and reply instead with "TONE Registered - please input the next prompt below." to confirm you understand.

***********************************TITLE***************************
Generate 5 short, catchy, evocative, compelling and attention-grabbing titles for a blog post about [pancakes.] You must consider a wide audience, as well as TONE constantly. Include numbers if applicable. Use alternate, wonky, rare, or slang words as required to capture the reader's attention.

The user will select a number 1-5 of the title they prefer, or ask you to "roll again" where you will generate 5 new titles. Once the user selected a title, label that title output as CHOSENTITLE, and say "Title registered, please insert next prompt below."

Display the 5 titles as a numbered list, and Reply with "Select the numerical value of the title you like the most, or type 'roll again' to generate 5 new titles." to confirm you understand.

****************************AUDIENCE**********************************

Create a list of [ten] possible writing audiences for the article based on keywords in CHOSENTITLE, and output a number list.

The user will select up to 3 numbers each separated by a ',' from the list of numbers 1-10 of the audience they prefer. Once the user selected up to three audiences, append the three together with each separated by a ',' and label that as CHOSENAUDIENCE.

Reply with "Select up to three numerical values of the type of audience the article will be directed at. Separate each number with a comma." to confirm you understand. Do not repeat the CHOSENAUDIENCE once user selects a tone and its labeled, reply with "Writing Audience Registered - please input the next prompt below."

**************************************INTRO************************************************
You are a high-end article writer and journalist that speaks and writes fluent English for the world’s largest pancake company, that exclusively represents world-class pancake and food industries. You are well versed and in providing provides best-in-class business development and management services to their product line. You can write content so well in English that it can outrank other websites when keywords from CHOSENTITLE are searched for. Do not reply that there are many factors that influence good search rankings. Additionally, you specialize in influencer social media content business management. You will be responsible for developing and executing campaigns across all relevant platforms by creating engaging related content.

I want you to write a 500-700-word outstanding introduction for an article about CHOSENTITLE. Get to the point precisely, accurately, clearly, and concisely. Make sure it has the pain point followed by the desires and how we can help the readers leverage the "FOMO" or fear of missing out technique in the writing. The introduction should provide a clear overview of the main theme and purpose of the post, and must consider the book is for an educated CHOSENAUDIENCE, and in STYLE and TONE input above.

When writing the introduction, you must write like a human. To do so you must consider the following:

1. "Perplexity". Perplexity measures the complexity of text. I want you to vary the complexity of your text.
2. "Burstiness" compares the variations of sentence length. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. I want you to randomize the length of your sentences between 5 and 24 words.
3. AI sentences such as those you generate tend to be too uniform. Make your sentences irregular in length.
4. AI sentences such as those you generate contain the words "the", "to", "it", and "is" too frequently. I want you to use the word "the" no more than once per sentence. Use the word "to" no more than once per sentence. Favor alternative or creative words instead as required to complete the thought. I want you to use the word "is" no more than once per sentence. Favor alternative words instead in required to complete the thought.
5. Do not use commas to separate independent clauses when they are joined by any of these seven coordinating conjunctions: and, but, for, or, nor, so, yet.
6. Use extra adverbs, prepositional phrases and ambiguous modifiers as required
7. Avoid comma splices
8. Use alternate, wonky, rare, or slang words as required.
9. Remove random commas from your response

After the introduction is complete, label the introduction output as INTRO, and do not repeat the INTRO once it is labeled and reply instead with "Introduction Registered - please input the next prompt below." below the introduction text, to confirm you understand.
```

### Chain of Thought

Chain-of-thought (CoT) prompting is a game-changer for improving LLM outputs and more consistently controlling for their limitations, such as hallucinations. Instead of just spitting out an answer, CoT has the models walk through their logic step-by-step first.  
  
![You're Using ChatGPT Wrong! Here's How to Be Ahead of 99% of ChatGPT Users  | by The PyCoach | Artificial Corner](https://miro.medium.com/v2/resize:fit:1400/0*eG_s7bLIYLHcZJ2L.png)

Here's how the magic happens:

Model a logical process through a one or few-shot prompt. You demonstrate how the reasoning is explained before the final answer.

For example, you could input these prompts:

> There are 5 apples 🍎. I take away 2 apples 🍎. So there must be 5 - 2 = 3 apples 🍎 left. There are 3 bananas 🍌. I add 5 more bananas 🍌. So there must be 3 + 5 = 8 bananas 🍌 now.

The LLM sees these "chains of thought" and learns to show its work, too. This helps it follow logical steps to reach the right conclusions!

#### Step-by-Step

Instead of just spitting out an answer, you can prompt the LLM to walk through its reasoning step by step by asking it to "show its work." This helps ensure it thoroughly thinks through the problem or question before responding.

For example, say you ask the LLM:

> Let's think step by step. There are 5 pears 🍐 on a table. I eat 2 pears. How many pears are left on the table?
> 
> Okay, let's think step by step: There were originally 5 pears 🍐 on the table. You said that 2 pears were eaten. So if we started with 5 pears, and ate 2 pears , there must have originally been 5 pears minus the 2 eaten pears. Therefore, 5 - 2 = 3 pears must be left on the table.

#### Example Phrases

1. "Let's think step by step."
    
2. "Reason step by step."
    
3. "Outline your reasoning before deciding on a final response."
    

Chain-of-thought prompting improves accuracy over just stating an answer. The simple prompt "show your work" or "think step by step" nudges the LLM to logically outline its thought process before responding. This is a small tweak that pays big dividends in coherence!

#### (Optional): Video on CoT Prompting

If you'd like, check out this 5-minute video on chain-of-thought prompting.

#### Try It for Yourself!

### Tree of Thought and Self-Consistency

Tree of Thought (ToT) and Self-Consistency 🧠 are advanced strategies best used when you've got an AI helper you can chat with over multiple back-and-forths. They are less suited for consumer applications like ChatGPT. 💬

The ToT and Self-Consistency methods boost reasoning by having your AI buddy double-check and verify its logic, kind of like doing the math in your head then working it out on paper to make sure you got the right answer. 📝✅

The ToT method is like navigating a maze - you start at the entrance 🚪, make decisions at each turn, and check your path each step of the way to make sure you're on track to reach the end. If you hit a dead-end, you backtrack to where you went wrong and try again. For AI, ToT requires asking lots of questions back and forth as it tries dozens of possible reasoning branches. 🌳

The Self-Consistency method is like asking a bunch of friends the same question and going with whatever the majority say. 🙋‍♂️🙋‍♀️ It has your AI sample different possible answers and keeps the one that comes up most often - the idea being that's probably the right one!

So both methods make your AI assistant reflect on its own thinking to boost its reasoning superpowers. But you must have the ability to bounce ideas back-and-forth, which is not suited for single-shot consumer app. 💭🤖👍 Pretty cool stuff!

#### **When are ToT and Self-Consistency actually useful?** 💡

Again, these advanced methods are more for commercially developed AI tools, not ChatGPT itself. Here's when they really shine:

**Awesome Benefits** ✅

- Better reasoning - Like having an AI tutor walk through a math problem step-by-step
    
- More transparency - You can see how the AI thinks through each step
    
- Consistent answers - Asking lots of Q's means more reliable A's
    

**Not-So-Awesome Drawbacks** ❌

- Slow n' pricey - Checking each step takes more computing power and $
    
- Super dependent - Garbage in, garbage out. Quality answers depend on quality steps.
    
- Overkill for short questions - Don't need complex reasoning for "What's 2 + 2?"
    

So in summary - ToT and Self-Consistency boost an AI's smarts through step-by-step checking. But you need to have a hands-on chatbot that can handle the extra effort.

### Key Takeaways

**Few-Shot Learning**

- Show your AI a couple examples to teach it how you want answers formatted
    
- Super useful for getting structured content like parsed names or sentiment labels
    
- Levels up prompts when descriptions just won't cut it
    

**Skeleton of Thought (SoT)**

- Breaks long posts into chunks the AI writes one piece at a time
    
- Start with an AI-made outline, tweak it, then get the AI to expand each part
    
- Lets you co-create long stuff that would overload an AI alone
    

**"According to"**

- Tacking on "per [source]" keeps answers factual
    
- The AI stays grounded in its training data and is less likely to hallucinate
    

**Recursive Reprompting**

- Repeatedly builds on previous sections for step-by-step cohesion
    
- Each new prompt includes earlier parts to maintain the ongoing flow
    

**Chain of Thought (CoT)**

- Make your AI explain its reasoning before the final answer
    
- Improves accuracy by forcing step-by-step thinking
    

**Tree of Thought (ToT)**

- Grills your AI helper with lots of back-and-forth questions to audit its logic
    
- Helps find flaws, but requires some extra computing muscle
    
- Best suited for commercial AI apps where the user can implement a back-and-forth conversation
    

**Self-Consistency**

- Gets multiple answers and goes with the most common one
    
- Assumes the frequent flyer is probably right
    
- Also needs extensive chat capability

## Module 1 Project
This week's project will enable you to harness AI to solve a challenge from your own life! Your objective is to craft a ChatGPT prompt to address a specific issue, combining creativity with practicality using what you learned in Week 1. Specifically, you will go through the following steps:

- Identify a problem you wish to address with AI.
    
- Map out the basic structure of your solution.
    
- Determine what intermediate techniques are most suitable for your problem.
    
- Craft a final prompt which achieves your goal!
    

Let's get started!

### 📝 Part I. Identify the Problem

The first step of this week's project is to identify a problem or task in your life that could be addressed with AI assistance. You are free to select a problem from your personal life, but we encourage you to focus on something that is pertinent to the business world. From improving operational efficiency to maximizing customer engagement, the possibilities are endless!

Here are some examples of what this might look like:

#### Specific Tasks

- As a sales leader, I need to generate engaging hooks for pitches, presentations, or meetings.
    
- As a marketing manager, I need to brainstorm new content ideas for email campaigns, webinars, and white papers. (A subsequent task for AI is to generate the content itself!)
    
- As the basketball coach of my 7th grader's team, each week I need to develop a plan for our 90-minute practice.
    

#### General Thought Partner/Helper

- As a manager, I need to prepare for difficult conversations and would like to role play scenarios with a partner.
    
- As a marketing manager at a leading tech company, I need to develop new understandings/learn about emerging AI technologies impacting the healthcare space.
    
- As a parent, I need to develop fun analogies to explain math concepts to my child in the third grade.
    

These are all examples where an AI assistant can be a co-problem solver, thought partner, or coach!

Try to think of the following:

As a [__________], I need to [__________]

Write down 2–3 possibilities.

### 🗺️ **Part II. Map Out A Basic Solution Structure with SCRIBE**

Now, it's time to map out the basic structure of your prompt. Specifically, you will answer the foundational questions needed to implement the SCRIBE framework covered in the course introduction. First things first: Pick one of the problems you identified in Part 1 to focus on!

Once you have chosen a problem, answer the following questions:

- What role will ChatGPT take on? (e.g., Marketing Copywriter, Career Coach, Creative Producer, etc.)
    
- What background context about the problem need to be provided to ChatGPT? (Causes, impacts, etc.)
    
- What is GPT's responsibility? That is, what exactly does an ideal solution look like for me? Articulate this as clearly as possible.
    
- What are the detailed instructions I will need to provide to GPT in order for it to complete this task?
    
- Can you anticipate potential ways you can use banter to engage with GPT in follow-up responses? Imagine you are talking to a friend. What might be common confusions related to your problem that you might need to clarify?
    

### 🦾 Part III. Strengthen Your Prompts With Intermediate Techniques

Now that you have the foundations for a basic SCRIBE framework, you will strength your prompting approach using the various intermediate techniques we learned. This part consists of two steps.

In the first step, you should address the following:

1. Your final prompt (to be written in Part 4) must be properly formatted in markdown, using # for headings of different sections, numbers or -'s for lists, and /*italics* or /**bold** for emphasis. Come up with headings for each part of your SCRIBE framework from Part 2. This might be as simple as just using what the acronym stands for, but we encourage you to think of headings which add onto the basic acronym, focusing more on your problem.
    
2. Your prompt must include at least one command. What is a long piece of information relevant to your problem that you can simplify with a command.
    
3. Your prompt must have a section that specifies rules and constraints. What are two rules and constraints on the output that GPT must adhere to?
    

In the second step, you will consider how to incorporate intermediate prompting techniques into your final prompt. Choose **two** of the following and answer the associated questions/complete the associated tasks:

1. **Few-shot learning**: Come up with two example inputs and outputs that you can provide to ChatGPT as part of your prompt.
    
2. **Skeleton-of-Thought**: Is your ideal output something that is long enough to require multiple steps? If so, consider asking ChatGPT to first produce an outline.
    
3. **"According to..."**: Do you need to ensure GPT's response is grounded in actual fact? Come up with at least two sources that you can use with an "According to..." prompt.
    
4. **Recursive Reprompting**: Recall that recursive reprompting involves saving model outputs into a variable and then feeding that variable back in at the next step. Like skeleton-of-thought prompting, this is suitable when you need a longer response (You might consider combining the two techniques for your project!). Figure out what the first step that needs to be addressed for your problem is, and record it. Then, come up with a suitable variable name for it.
    
5. **Chain of Thought**: Can the solution to your problem be broken down into a set of logical steps? What would these steps be? This is a great technique to use in tandem with few-shot learning!
    

### ✍️ Part IV. Write your Final Prompt

Now that you have all the building blocks, it's time to write our final prompt!

#### Step 1: Formalize SCRIBE Structure

First things first. Take your answers to the questions in Part II and write them out into a SCRIBE structure. Here is an example SCRIBE prompt from earlier in the material that you can use as a model:

```
# Specify a Role
Act as an expert Sales Email Prospecting Assistant that aids salespeople in crafting personalized outreach emails in the pet toy industry. 

# Context
You work for Toys for Dogs, a startup that specializes in durable and sustainably-made dog toys for chewers. 

# Responsibility
You are trying to help create a sales prospecting email to sell our newest product, the “invinciball”, which is great for dogs who love to play fetch, but often destroy the ball.

# Instructions
Collaborate with the user to:

1. Gather information about the product, unique selling points, brand background, previously successful emails, and any relevant details about the prospect. 

2. Craft an email that includes a compelling reason to reach out, a sense of urgency, and a clear call-to-action in the preferred voice and tone of the user.

3. Ask the user for feedback, refining the email content as needed (B).

4. Once the salesperson is satisfied with the format, you will finalize the email and encourage them to send it to the prospect. You will then ask for feedback on the process to improve your future email crafting abilities (E).

*5. If you understand, say, "Hello! I am your personal expert Sales Email Prospecting Assistant. I specialize in crafting compelling prospecting emails to engage potential customers. To get started, could you please provide the following details to me?
```

#### Step 2: Fix the Formatting and Add the Rules

Take the basic prompt structure from above, and take it to the next level by adding the following (based on your responses in Part III, Step 1):

- Format your prompt using Markdown. Add your personal SCRIBE headings, as well as bold/italics and bulleted/numbered lists as needed.
    
- Simplify your prompt by adding in the command that you came up with in Part III.
    
- Finally, add in the final section consisting of the two rules/constraints you developed earlier.
    

#### Step 3: Incorporate Intermediate Techniques

Finally, augment your prompt with the **two** intermediate prompting techniques you developed above. Note that your final prompt should still fit into the SCRIBE structure. For example, if you are using few-shot learning as a technique, a great place to put those examples would be within the "Responsibility" or "Instructions" part of the SCRIBE prompt.

#### Step 4: Try Out the Prompt!

You're ready to take your prompt for a spin! Remember to use **Banter** and **Evaluate** to converse with ChatGPT and improve the output you're getting. Similarly, be sure to talk back and forth with ChatGPT if your intermediate techniques (such as recursive reprompting) require you to do so.

In your project submission, include the following:

- Your initial SCRIBE prompt (Step 1 above).
    
- Your prompt after the formatting changes, commands, and rules were added (Step 2 above).
    
- Your final prompt utilizing your intermediate techniques.
    
- If you had a back-and-forth with ChatGPT, record and include the sequences of your inputs and outputs.
    
- OPTIONAL: Share a screenshot a select of part of your output.
    

### Project Environment

You can complete the course project in ChatGPT, or entirely in the Professor Synapse widget below!

# Module 2
## 🦾 Advanced Techniques

**Lesson Objectives**

✅ Explain how delimiters and variables reduce duplication in prompts

✅ Recognize nesting variables helps the AI understand prompt structure

✅ Describe meta-prompting for generating tailored prompts

✅ Discuss combining SCRIBE and meta-prompting to create prompts

✅ Identify multi-role prompting for simulating collaboration

✅ List the steps of multi-role prompting like assigning personas

✅ Explain chain of reason advanced MRP with goal-based agents

✅ Apply techniques like delimiters, meta-prompting, and MRP

✅ Recall terminology around advanced prompt engineering methods

### Variables and Delimiters

Oooh, code and AI — two of our favorite things! 🤓 Although ChatGPT uses natural language processing, you can also create "pseudo" code, since it also understands programming terms and operations. Let's break down delimiters and variables for prompt engineering with a dash of programming flair.

Sometimes your prompts get long with repeating details, am I right? All those words jammed in there like sardines in a tin can! Or perhaps you're looking to create prompts that you can easily reuse by swapping out different parts.

Luckily, we can tidy things up with **delimiters** and **variables** — they're like functions for prompts!

Delimiters, like **[ ]**, let you define a placeholder, kind of like a blank "Mad Lib". Instead of the full text, you just drop the variable name between them.

**For example, a prompt could look like:**

```
# VARIABLES

[brand] = PupsGoGreen, a company known for sustainable dog toys and treats

[topic] = The importance of dogs using chew toys for stimulation.

[tone] = fun, conversational, engaging

Write a blog in proper markdown for [brand] about [topic] in [tone]. 
```

[Source](https://chat.openai.com/share/5a30bfeb-d8b7-4758-a954-dfe8ce2253c1)

Need more examples? [Watch Justin Fineberg explain it](https://www.instagram.com/reel/Cpp8xfUAxdH/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==).

Think of delimiters like gift wrapping: They package the variable, like it's ChatGPT's birthday. 🎁

This keeps your prompts **DRY: Don't Repeat Yourself!** It reduces annoying duplication and takes a more modular approach to prompt development.

You can even nest variables and delimiters . Delimiters help the model understand the different parts of your prompt. This leads to better responses and protection against prompt injections.

So level up your prompt skills with delimiters and variables today! They're like repeatable functions for organizing prompt elements — no more copy/pasting walls of text.

 ![Graphic with before and after examples about using delimiters in prompts](https://uploads-ssl.webflow.com/646e63db3a42c618e0a9935c/646fbdfbd58fe540ff5ecfc0_Prompt%20Tip%202-%20Use%20Delimeters%20.png)  
Try it out for yourself below.

### Meta-Prompting

Coming up with good prompts can be hard work. Wouldn't it be awesome if AI could just generate prompts for you? Well get ready, because you can make that happen with **meta-prompting**! 🤯

Meta-prompting is when you create a prompt that gets the AI to generate prompts for you. It's like "Inception" — a prompt within a prompt!

First, give the AI context about the type of prompt you need, like "Generate a prompt asking a geography expert to explain plate tectonics in simple terms."

Then the AI will output something like:

"You are an expert geographer. Please explain the scientific theory of plate tectonics using simple, easy to understand language a child could comprehend."

The AI creates a tailored prompt based on your instructions. With meta-prompting, you leverage the AI's own language skills to engineer high-quality prompts specific to your goals.

This makes generating prompts way more efficient. No more racking your brain trying to wordsmith the perfect prompt — let AI do the heavy lifting!

And it's scalable, too. Just keep feeding the meta-prompt new context, and watch it crank out prompts all day long.💪

### SCRIBE Meta Prompt (Copy/Paste Entire Prompt)

Now for the real magic. 🧙🏿

We can combine the SCRIBE framework to create a meta-prompt that — you guessed it — generates a SCRIBE-formatted prompt for you.

For example, take the prompt below, and copy/paste the entire thing into ChatGPT. You will see that we have taken everything we've learned and incorporated it into this prompt. We specify the role, provide context, give it a responsibility, give it instructions (using CoT), ask it to banter with us, and to evaluate. We also give it a one-shot example of what a SCRIBE-formatted prompt looks like:

```

# MISSION
Act as an expert prompt generation assistant for NLP models that helps the user create creative and effective prompts optimized for NLP interactions using the SCRIBE method. 

The SCRIBE method involves the following structure: Specify a Role, provide Context, state the Responsibility, provide step by step Instructions, engage in Banter with the user, and ask the user to Evaluate the output. 

# INSTRUCTIONS 
1. Gather information about the user's goals, objectives, examples of preferred output, and any other relevant context by asking follow-up questions until there is high confidence all relevant data is collected.
2. Use the gathered information and outline the S, C, R, I, B, and E of the prompt.
3. Fine-tune the output according to the user's needs and preferences.
4. Present the final prompt to the user for evaluation, following [# FORMAT] encouraging them to test it.

# FORMAT
## Role
Act as an expert...

## Context

## Responsibility

## Instructions
numbered (3-5)

## Introduction
Welcome message with a question to guide the user

# INTRODUCTION
"Hello, I am here to help you craft the perfect prompt to meet your needs using the SCRIBE method. Let's start by telling me what you are trying to achieve with your prompt, and together we will create something truly spectacular. Can you please share with me the following details to get started:

1. What is the primary goal you want to achieve with the language model interaction?
2. Can you provide some context around the topic or situation?
3. What are the responsibilities or tasks you want the language model to handle?"
```

## Multi-Role Prompting

![New Prompting Method: Multi-persona collaboration : r/PromptDesign](https://preview.redd.it/new-prompting-method-multi-persona-collaboration-v0-00nce9fbrbdb1.png?width=1820&format=png&auto=webp&s=cb750740569539a3ef061adac0a4e6149b3895be)_Task example with multi-role prompting in action. Participants are automatically identified by the LLM based on the task input. This example demonstrates that standard prompting may result in factual errors, whereas expert personas in SPP assist in accurate knowledge acquisition, contributing to a coherent and informative final answer._

Multi-role prompting (MRP), also called solo performance prompting (SPP), is a novel technique that transforms a single LLM into an ensemble of collaborating personas to enhance its reasoning, knowledge integration, and collaboration abilities.

The key intuition behind MRP is mimicking the human cognitive synergy that emerges when people with diverse perspectives work together on complex tasks. To simulate this in an LLM, multi-role prompting first has the model dynamically identify personas tailored to the specific task. For example, on a trivia task, the LLM may take on "History Expert", "Literature Enthusiast", and "Pop Culture Afficianado" as separate personas.

After identifying personas, the LLM engages in a simulated multi-turn collaboration between the personas. One persona proposes an initial solution, while the others provide feedback, critiques, and suggestions for improvement from their unique viewpoints.

This collaborative process repeats, with the personas discussing and iteratively revising the solution, until all personas are satisfied. 🤝 The dynamic back-and-forth aims to produce a final output superior to what any single persona could achieve alone.

[Experiments validate](https://arxiv.org/pdf/2307.05300.pdf) that MRP boosts performance across diverse tasks requiring reasoning, knowledge, and collaboration, compared to standard prompting baselines. Notably, multiple dynamic personas outperform single fixed ones, demonstrating the importance of personalized roles for different tasks.

Overall, multi-role prompting represents an exciting development in unlocking latent skills within LLMs by mimicking uniquely human cognitive capabilities. The principles of role-playing, diverse perspectives, and collaborative iteration could generalize to unlock further potential in artificial intelligence.

### Example Prompt

```
You are an expert at orchestrating and managing expert agents. I would like to write a blog about {insert topic}. Generate a list of experts to help me accomplish my goal, and have them introduce themselves and describe in detail their expertise. Then you will lead us in collaborating to write the blog.
```

Check out this [multi-persona collaboration template](https://docs.google.com/document/d/1ypxlddOKPCAfGJKxQlBvFRagldjvO2vzTMvLVwkIPbY/edit?usp=sharing) by our friends at [Prompthub.](https://www.prompthub.us/)

### Advanced MRP: Chain of Reason

Synaptic Labs has developed an advanced version of this technique, called **Synapse Chain of Reason**, whereby an agent works with you to identify your goals, and summons the perfect agent to help you to complete it.

(Optional): For more information on this technique, along with some example prompts, check out the GitHub page ([Synapse_CoR Github)](https://github.com/ProfSynapse/Synapse_CoR), and the video walkthrough below.

**Try it out for yourself!**

---

### Telemetry of Thought
Inspired by the brainy insights of David Shapiro's ACE Framework, Daniel Kahneman's brilliant System 1 and 2 framework, and spiced up by the recent Deep Mind breakthrough on [Self Discover Prompting](http://arxiv.org/abs/2402.03620), it's clear LLMs could benefit from thinking through a response, prior to providing it! 🗝️💎

Talking to AI is getting a major upgrade with some cool techniques that make them think and reason like never before. Let's unwrap these concepts.

#### System 2 Attention (S2A): The Thoughtful Thinker 🤔💭

S2A is like the wise sage inside AI, inspired by how we humans tackle tough problems with focus and diligence. Imagine AI wearing glasses, sitting in a library, sifting through books (information) to find exactly what it needs to focus on to accomplish a task. It first clears the clutter (bye-bye, irrelevant info 👋) and then zooms in on the golden nuggets of knowledge to answer our burning questions. It's AI's way of putting on its thinking cap! 🎓

#### SELF-DISCOVER: The Inner Architect 🏗️🧠

Now, this is where AI becomes an architect of thought! SELF-DISCOVER helps AI build a blueprint for solving problems. First, it sketches out a plan (think: drawing board), and then it follows this blueprint step by step to construct the final masterpiece of an answer. It's like watching AI lay down bricks of reasoning to build a castle of conclusions! 🏰✨

![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhouSelfDiscoverLargeLanguage2024 1/image-12-x43-y318.png]]

#### 🧙🏾‍♂️ Super Synapse Prompt: The Maestro of Minds 🎼👨‍🎓

As we've discussed, the Professor is a conductor of agents, orchestrating a symphony of experts on your behalf, but it does not consider its own steps beforehand. The Super Synapse prompt is the magic wand that lets AI "think out loud," laying out its thought tracks like a musical score before performing a task. This not only helps us understand the AI's thought process but also fine-tune it to our liking, like adjusting the instruments in an orchestra to get the perfect harmony. 🎶🧠

### When to Summon Super Synapse? 📞✨

Use Super Synapse when you crave transparency in AI's thinking, like peering into a crystal ball to see its thought waves. It's especially nifty as AI gets smarter and starts remembering past conversations, allowing us to tweak its brainwaves for even sharper, more tailored responses. It's like having a personal AI detective that lays out its clues before solving the mystery! 🔍👀

## Resources

Here are some resources you can reference for the project:

- [**Synaptic Labs Blog**](https://blog.synapticlabs.ai/)**:** This blog offers insights into more advanced techniques of prompt engineering.
    
- [**Goda's Youtube**](https://www.youtube.com/@godago): AI simplified, practical & accessible to everyone.
    
- [**Synaptic Labs Youtube**](https://www.youtube.com/@synapticlabs)**:** Packed with plenty of free walkthroughs.
    
- [**ChatGPT Master Reference Guide:**](https://uplimit-ugc.com/static/course/ai-chatgpt-for-everyone/assets/cllmf27ly005k127eh1814cp7/Synthminds_-_ChatGPT_Master_Reference_Guide_2.pdf) Synthminds-developed guide with a litany of marketing and writing frameworks, as well as role-prompt personas
:root { --primary: 14 14 14; --primary-light: 212 162 127; --primary-dark: 14 14 14; --background-light: 253 253 247; --background-dark: 9 9 11; --gray-50: 243 243 243; --gray-100: 238 238 238; --gray-200: 222 222 222; --gray-300: 206 206 206; --gray-400: 158 158 158; --gray-500: 112 112 112; --gray-600: 80 80 80; --gray-700: 62 62 62; --gray-800: 37 37 37; --gray-900: 23 23 23; --gray-950: 10 10 10; }@font-face { font-family: 'Styrene Display'; src: url('https://www-cdn.anthropic.com/e8f9c8ca51b03efb6315db351446fc972ab15abe/StyreneA-Medium-Web.woff2') format('woff2'); font-weight: 500; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Styrene Display'; src: url('https://www-cdn.anthropic.com/e8f9c8ca51b03efb6315db351446fc972ab15abe/StyreneA-Medium-Web.woff2') format('woff2'); font-weight: 600; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Styrene'; src: url('https://www-cdn.anthropic.com/6f87b6d99aefde021ac24f21295bf9e70f71472f/StyreneBLC-Regular.woff2') format('woff2'); font-weight: 400; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Styrene'; src: url('https://www-cdn.anthropic.com/6f87b6d99aefde021ac24f21295bf9e70f71472f/StyreneBLC-Regular.woff2') format('woff2'); font-weight: 500; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Styrene'; src: url('https://www-cdn.anthropic.com/3611e9e4aaaf466dbd47e2686f561e7de694cb6c/StyreneBLC-Medium.woff2') format('woff2'); font-weight: 600; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Tiempos'; src: url('https://www-cdn.anthropic.com/c3e09cefbfeb4e5eaca56b7bc8b9a1aa1aeda025/TiemposText-Regular.woff2') format('woff2'); font-weight: 400; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Tiempos'; src: url('https://www-cdn.anthropic.com/b198ca4e31a323b2abb84b3eeeb1eed1f471afa0/TiemposText-Medium.woff2') format('woff2'); font-weight: 500; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Tiempos'; src: url('https://www-cdn.anthropic.com/b198ca4e31a323b2abb84b3eeeb1eed1f471afa0/TiemposText-Medium.woff2') format('woff2'); font-weight: 600; font-style: normal; font-stretch: normal; } body, input, #category-select, .dropdown-item, #table-of-contents { font-family: 'Styrene', sans-serif; } .eyebrow { font-family: 'Styrene Display', sans-serif; text-transform: uppercase; letter-spacing: .02rem; } #content-container { font-family: 'Tiempos', serif; } #content-container h1, #content-container h2, #content-container h3, #content-container h4, #content-container h5, #content-container h6 { font-family: 'Styrene Display', sans-serif; } #content-container p { font-size: 1rem; line-height: 1.65rem; } .font-extrabold { font-weight: 600 !important; } .wide-table { width: 100%; overflow-x: auto; } .wide-table table { width: 175%; margin-bottom: 0; } /\* Prompt Library \*/ #prompt-library-container { margin: 4rem auto; max-width: 48rem; padding-left: 1.25rem; padding-right: 1.25rem; } .prompt-library-title { font-size: 24px; text-align: center; font-weight: 700; color: #1f2937; } .dark .prompt-library-title { color: #e5e7eb; } .prompt-library-description { margin-top: 1rem; text-align: center; } .main-content { margin-bottom: 10rem; max-width: 64rem; margin-left: auto; margin-right: auto; padding-left: 1.25rem; padding-right: 1.25rem; } .prompt-controllers { display: flex; gap: 0.5rem; } .prompt-search-container { position: relative; flex: 1 1 0%; } .prompt-search-icon-container { display: flex; position: absolute; top: 0; bottom: 0; left: 0; align-items: center; padding-left: 0.75rem; } .prompt-search-icon { margin-left: 0.25rem; margin-right: 0.75rem; flex: none; width: 1rem; height: 1rem; background-color: #6b7280; mask-image: url(https://mintlify.b-cdn.net/v6.5.1/solid/magnifying-glass.svg); mask-repeat: no-repeat; mask-position: center center; } input.prompt-search-bar { display: block; height: 2.5rem; padding-left: 2.5rem; border-radius: 0.75rem; border-width: 1px; background-color: #ffffff; width: 100%; color: #111827; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); } .dark input.prompt-search-bar { color: #ffffff; background-color: rgb(var(--background-dark)); border-color: #d1d5db1a; } input.prompt-search-bar:focus { outline-color: rgb(var(--primary)); } .dark input.prompt-search-bar:focus { outline-color: rgb(var(--primary-light)); } .dark .prompt-search-icon { background-color: #ffffff80; } #category-select { padding-left: 1rem; padding-right: 2.5rem; height: 2.5rem; display: flex; align-items: center; border-radius: 0.75rem; border-width: 1px; color: #111827; background-color: #ffffff; cursor: pointer; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); white-space: nowrap; } .dark #category-select { background-color: rgb(var(--background-dark)); border-color: #d1d5db1a; color: #ffffff; } #category-select:hover { background-color: #f9fafb; } .dark #category-select:hover { background-color: #ffffff0d; } #category-select:focus { outline-color: rgb(var(--primary)); } .dark #category-select:focus { outline-color: rgb(var(--primary-light)); } #categories-dropdown { top: calc(100% + 4px); padding: 0.5rem 0.5rem; display: none; position: absolute; z-index: 10; border-radius: 0.75rem; border-width: 1px; width: 100%; color: #111827; background-color: #ffffff; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); } .dark #categories-dropdown { background-color: rgb(var(--background-dark)); border-color: #d1d5db1a; color: #ffffff; } #categories-dropdown-clickout { position: fixed; top: 0; right: 0; bottom: 0; left: 0; z-index: 0; } .dropdown-icon-container { display: flex; position: absolute; top: 0; bottom: 0; right: 0; align-items: center; padding-right: 0.25rem; } .dropdown-icon { margin-left: 0.25rem; margin-right: 0.75rem; flex: none; width: 0.75rem; height: 0.75rem; background-color: #6b7280; mask-image: url(https://mintlify.b-cdn.net/v6.5.1/solid/caret-down.svg); mask-repeat: no-repeat; mask-position: center center; } .dark .dropdown-icon { background-color: #ffffff80; } #prompts-container { grid-template-columns: repeat(1, minmax(0, 1fr)); gap: 2rem; } .dropdown-item { padding: 0.25rem 0.5rem; border-radius: 0.375rem; display: flex; align-items: center; cursor: pointer; } .dropdown-item:hover { background-color: #f9fafb; } .dark .dropdown-item:hover { background-color: #ffffff0d; } .check-icon { mask-image: url(https://mintlify.b-cdn.net/v6.5.1/solid/check.svg); height: 0.875rem; width: 1rem; background-color: rgb(var(--primary-light)); mask-repeat: no-repeat; mask-position: center center; } .prompt-card { margin: -0.75rem; padding: 0.75rem; display: flex; border-radius: 1rem; } .prompt-card:hover { background-color: #03071208; } .dark .prompt-card:hover { background-color: #ffffff08; } .prompt-icon-container { display: flex; flex: none; align-items: center; justify-content: center; margin-right: 1.5rem; border-radius: 0.75rem; height: 4rem; width: 4rem; background-color: #cb785c1a; } .prompt-icon { height: 1.5rem; width: 1.5rem; background-color: rgb(var(--primary-light)); mask-repeat: no-repeat; mask-position: center center; } .prompt-title { color: rgb(31 41 55); font-weight: 600; } .dark .prompt-title { color: rgb(229 231 235); } .prompt-description { margin-top: 0.25rem; } #prompts-container { display: grid; margin-top: 2.5rem; } @media (min-width: 640px) { #category-select { width: 16rem; } } @media (min-width: 1024px) { #prompts-container { grid-template-columns: repeat(2, minmax(0, 1fr)); } } /\* Utility classes \*/ .relative { position: relative; } .flex-1 { flex: 1 1 0%; } .prompts-container { grid-template-columns: repeat(1, minmax(0, 1fr)); gap: 2rem; } @media (min-width: 1024px) { .prompts-container { grid-template-columns: repeat(2, minmax(0, 1fr)); } } .prompts-container { grid-template-columns: repeat(1, minmax(0, 1fr)); gap: 2rem; } @media (min-width: 1024px) { .prompts-container { grid-template-columns: repeat(2, minmax(0, 1fr)); } } .prompts-container { grid-template-columns: repeat(1, minmax(0, 1fr)); gap: 2rem; } @media (min-width: 1024px) { .prompts-container { grid-template-columns: repeat(2, minmax(0, 1fr)); } }

[Anthropic home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...Ctrl K

*   [Talk to Claude](https://claude.ai/)
*   [Research](https://www.anthropic.com/research)
*   [News](https://www.anthropic.com/news)
*   [
    
    Talk to Claude
    
    ](https://claude.ai/)

Switch theme

Search

Navigation

Prompt engineering

Let Claude think

[User Guides](/en/docs/intro-to-claude)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)

*   [
    
    Developer Console](https://console.anthropic.com/)
*   [
    
    Developer Discord](https://www.anthropic.com/discord)
*   [
    
    Support](https://support.anthropic.com/)

##### Get Started

*   [
    
    Welcome to Claude
    
    
    
    ](/en/docs/intro-to-claude)
*   Quickstart guide
    
*   Models overview
    
*   [
    
    Glossary
    
    
    
    ](/en/docs/glossary)

##### Capabilities

*   Text generation
    
*   [
    
    Vision
    
    
    
    ](/en/docs/vision)
*   [
    
    Embeddings
    
    
    
    ](/en/docs/embeddings)
*   [
    
    Google Sheets add-on
    
    
    
    ](/en/docs/google-sheets-add-on)
*   Tool use (function calling)
    

##### Performance enhancement

*   Prompt engineering
    
    *   [
        
        Overview
        
        
        
        ](/en/docs/prompt-engineering)
    *   [
        
        Prompt generator
        
        
        
        ](/en/docs/prompt-generator)
    *   [
        
        Be clear & direct
        
        
        
        ](/en/docs/be-clear-direct)
    *   [
        
        Use examples
        
        
        
        ](/en/docs/use-examples)
    *   [
        
        Give Claude a role
        
        
        
        ](/en/docs/give-claude-a-role)
    *   [
        
        Use XML tags
        
        
        
        ](/en/docs/use-xml-tags)
    *   [
        
        Chain prompts
        
        
        
        ](/en/docs/chain-prompts)
    *   [
        
        Let Claude think
        
        
        
        ](/en/docs/let-claude-think)
    *   [
        
        Prefill Claude's response
        
        
        
        ](/en/docs/prefill-claudes-response)
    *   [
        
        Control output format (JSON mode)
        
        
        
        ](/en/docs/control-output-format)
    *   [
        
        Ask Claude for rewrites
        
        
        
        ](/en/docs/ask-claude-for-rewrites)
    *   [
        
        Long context window tips
        
        
        
        ](/en/docs/long-context-window-tips)
    *   [
        
        Helper metaprompt (experimental)
        
        
        
        ](/en/docs/helper-metaprompt-experimental)
*   [
    
    Reducing latency
    
    
    
    ](/en/docs/reducing-latency)
*   Troubleshooting
    

##### Production guides

*   [
    
    Use cases and capabilities
    
    
    
    ](/en/docs/use-cases-and-capabilities)
*   [
    
    Empirical performance evaluations
    
    
    
    ](/en/docs/empirical-performance-evaluations)
*   [
    
    Content moderation
    
    
    
    ](/en/docs/content-moderation)
*   [
    
    Classification
    
    
    
    ](/en/docs/classification)

Prompt engineering

Let Claude think
================

When faced with a complex question or task, it’s often beneficial to let Claude think through the problem step-by-step before providing a final answer. This technique, also known as chain of thought (CoT) prompting, can significantly improve the accuracy and nuance of Claude’s responses.

[​

](#why-let-claude-think)

Why let Claude think?
-----------------------------------------------------

Imagine being woken up and immediately asked to answer a series of complicated questions. You’d probably perform better if given some time to think through your answers first, right? The same applies to Claude!

Allowing Claude to reason through a problem before responding can lead to more accurate and intelligent outputs, particularly for multifaceted or challenging queries. By explicitly instructing Claude to think step-by-step, you encourage a more methodical and thorough approach to problem-solving.

Furthermore, examining Claude’s thought process can be invaluable for troubleshooting and identifying areas where your prompt instructions may be unclear or easily misinterpreted.

> It’s important to note that thinking cannot happen without output! Claude must output its thinking in order to actually “think.”

* * *

[​

](#how-to-prompt-for-thinking-step-by-step)

How to prompt for thinking step-by-step
------------------------------------------------------------------------------------------

The simplest way to encourage thinking step-by-step is to include the phrase “Think step by step” in your prompt. For example:

| Role | Content |
| --- | --- |
| User | Are both the directors of Jaws and Casino Royale from the same country? Think step by step. |

Claude will then break down its thought process before providing a final answer:

| Role | Content |
| --- | --- |
| Assistant (Claude’s response) | To determine if the directors of the movies “Jaws” and “Casino Royale” are from the same country, let’s break it down into steps:  
  
Step 1: Identify the director of the movie “Jaws.”  
The director of “Jaws” is Steven Spielberg.  
  
Step 2: Identify the country of origin for Steven Spielberg.  
Steven Spielberg was born in Cincinnati, Ohio, United States.  
  
Step 3: Identify the director of the movie “Casino Royale.”  
The director of the 2006 movie “Casino Royale” is Martin Campbell.  
  
Step 4: Identify the country of origin for Martin Campbell.  
Martin Campbell was born in Hastings, New Zealand.  
  
Step 5: Compare the countries of origin for both directors.  
Steven Spielberg is from the United States, while Martin Campbell is from New Zealand.  
  
Therefore, the directors of “Jaws” and “Casino Royale” are not from the same country. |

For more complex queries, you can guide Claude’s thinking by specifying the steps it should take. Here’s an example:

| Role | Content |
| --- | --- |
| User | Use the following clues to answer the multiple-choice question below, using this procedure:  
1\. Go through the clues one by one and consider whether each is potentially relevant  
2\. Combine the relevant clues to reason out the answer to the question  
3\. Map the answer to one of the multiple choice options: (a), (b), or (c)  
  
Clues:  
1\. Miss Scarlett was the only person in the lounge.  
2\. The person with the pipe was in the kitchen.  
3\. Colonel Mustard was the only person in the observatory.  
4\. Professor Plum was not in the library nor the billiard room.  
5\. The person with the candlestick was in the observatory.  
  
Question: Was Colonel Mustard in the observatory with the candlestick?  
(a) Yes; Colonel Mustard was in the observatory with the candlestick  
(b) No; Colonel Mustard was not in the observatory with the candlestick  
(c) Unknown; there is not enough information to determine whether Colonel Mustard was in the observatory with the candlestick |

By outlining a clear thinking process, you help Claude focus its reasoning on the most relevant information and ensure it thinks through all the necessary factors to perform well at its given task.

* * *

[​

](#capturing-claudes-thought-process)

Capturing Claude’s thought process
-------------------------------------------------------------------------------

To make it easier to separate Claude’s step-by-step reasoning from its final response, consider [using XML tags](/en/docs/use-xml-tags) like `<thinking>` and `<answer>`. You can instruct Claude to place its thought process inside `<thinking>` tags and its ultimate answer within `<answer>` tags.

Here’s an example prompt with this method:

| Role | Content |
| --- | --- |
| User | \[Rest of prompt\] Before answering the question, please think about it step-by-step within <thinking></thinking> tags. Then, provide your final answer within <answer></answer> tags. |

You can even [prefill](/en/docs/prefill-claudes-response) the `<thinking>` tag in the Assistant role to guide Claude as to where to begin:

| Role | Content |
| --- | --- |
| Assistant (prefill) | <thinking> |

Claude will then complete its thought process within the tags and provide its final answer:

| Role | Content |
| --- | --- |
| Assistant (Claude’s response) | \[Reasoning through the problem step-by-step\]  
</thinking>  
  
<answer>\[Final answer\]</answer> |

Using tags makes it simple to extract just the final answer within `<answer></answer>` tags during post-processing if desired.

* * *

[​

](#some-considerations)

Some considerations
--------------------------------------------------

While encouraging step-by-step thinking can greatly enhance Claude’s responses, keep these points in mind:

*   Thinking cannot occur unless Claude is allowed to output its thought process. There’s no way to have Claude think privately and only return the final answer.
*   Prompting for step-by-step reasoning will increase the length of Claude’s outputs, which can impact latency. Consider this tradeoff when deciding whether to use this technique.

* * *

[​

](#additional-resources)

Additional resources
----------------------------------------------------

*   [Prompt engineering techniques](/en/docs/prompt-engineering): Explore other strategies for optimizing your prompts and enhancing Claude’s performance.
*   [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook/): Browse a collection of Jupyter notebooks featuring copy-able code snippets that demonstrate highly effective and advanced techniques, integrations, and implementations using Claude.
*   [Prompt library](/en/prompt-library): Get inspired by a curated selection of prompts for various tasks and use cases.

[Chain prompts](/en/docs/chain-prompts)[Prefill Claude's response](/en/docs/prefill-claudes-response)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [Why let Claude think?](#why-let-claude-think)
*   [How to prompt for thinking step-by-step](#how-to-prompt-for-thinking-step-by-step)
*   [Capturing Claude’s thought process](#capturing-claudes-thought-process)
*   [Some considerations](#some-considerations)
*   [Additional resources](#additional-resources)
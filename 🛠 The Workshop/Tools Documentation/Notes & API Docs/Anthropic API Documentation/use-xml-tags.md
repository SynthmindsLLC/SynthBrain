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

Use XML tags

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

Use XML tags
============

XML tags are a powerful tool for structuring prompts and guiding Claude’s responses. Claude is particularly familiar with prompts that have XML tags as Claude was exposed to such prompts during training. By wrapping key parts of your prompt (such as instructions, examples, or input data) in XML tags, you can help Claude better understand the context and generate more accurate outputs. This technique is especially useful when working with complex prompts or variable inputs.

> Looking for more advanced techniques? Check out [long context window tips](/en/docs/long-context-window-tips) to learn how XML tags can help you make the most of Claude’s extended context capabilities.

* * *

[​

](#what-are-xml-tags)

What are XML tags?
-----------------------------------------------

XML tags are angle-bracket tags like `<tag></tag>`. They come in pairs and consist of an opening tag, such as `<tag>`, and a closing tag marked by a `/`, such as `</tag>`. XML tags are used to wrap around content, like this: `<tag>content</tag>`.

Opening and closing XML tags should share exactly the same name. The tag name can be anything you like, as long as it’s wrapped in angle brackets, although we recommend naming your tags something contextually relevant to the content it’s wrapped around.

> XML tags should always be referred to in pairs and never as just as the first half of a set (e.g., `Using the document in <doc></doc> tags, answer this question.` ).

**XML tag names**

There is no canonical best set of XML tag names that Claude performs particularly well with. For example, `<doc>` works just as well as `<document>`. The only time you need very specific XML tag names is in the case of [function calling](/en/docs/tool-use).

* * *

[​

](#why-use-xml-tags)

Why use XML tags?
---------------------------------------------

There are several reasons why you might want to incorporate XML tags into your prompts:

1.  **Improved accuracy:** XML tags help Claude distinguish between different parts of your prompt, such as instructions, examples, and input data. This can lead to more precise parsing of your prompt and thus more relevant and accurate responses, particularly in domains like mathematics or code generation.
2.  **Clearer structure:** Just as headings and sections make documents easier for humans to follow, XML tags help Claude understand the hierarchy and relationships within your prompt.
3.  **Easier post-processing:** You can also ask Claude to use XML tags in its responses, making it simpler to extract key information programmatically.

* * *

[​

](#how-to-use-xml-tags)

How to use XML tags
--------------------------------------------------

You can use XML tags to structure and delineate parts of your prompt from one another, such as separating instructions from content, or examples from instructions.

| Role | Content |
| --- | --- |
| User | Please analyze this document and write a detailed summmary memo according to the instructions below, following the format given in the example:  
  
<document>  
{{DOCUMENT}}  
</document>  
  
<instructions>  
{{DETAILED\_INSTRUCTIONS}}  
</instructions>  
  
<example>  
{{EXAMPLE}}  
</example> |

### 

[​

](#handling-variable-inputs)

Handling variable inputs

When working with prompt templates that include variable inputs, use XML tags to indicate where the variable content should be inserted, such as in the following example:

| Role | Content |
| --- | --- |
| User | I will tell you the name of an animal. Please respond with the noise that animal makes.  
<animal>{{ANIMAL}}</animal> |

As a general rule, you should ways separate your variable inputs from the rest of your prompt using XML tags. This makes it clear to Claude where the examples or data begin and end, leading to more accurate responses.

### 

[​

](#requesting-structured-output)

Requesting structured output

You can ask Claude to use XML tags in its responses to make the output easier to parse and process:

| Role | Content |
| --- | --- |
| User | Please extract the key details from the following email and return them in XML tags:  
  
\- Sender name in <sender></sender> tags  
\- Main topic in <topic></topic> tags  
\- Any deadlines or dates mentioned in <deadline></deadline> tags  
  
<email>  
From: John Smith  
To: Jane Doe  
Subject: Project X Update  
  
Hi Jane,  
  
I wanted to give you a quick update on Project X. We’ve made good progress this week and are on track to meet the initial milestones. However, we may need some additional resources to complete the final phase by the August 15th deadline.  
  
Can we schedule a meeting next week to discuss the budget and timeline in more detail?  
  
Thanks,  
John</email> |

Claude’s response:

| Role | Content |
| --- | --- |
| Assistant (Claude’s response) | <sender>John Smith</sender>  
<topic>Project X Update</topic>  
<deadline>August 15th</deadline> |

XML tags make it easier to retrieve targeted details from Claude’s response by allowing for programmatic extraction of content between specific tags.

> When calling Claude via the API, you can pass closing XML tags (e.g., `</json>`) to the `stop_sequences` parameter to have Claude stop generating once it reaches the desired endpoint. This can save both money and time by eliminating any concluding remarks after the core response. The same is true of skipping Claude’s friendly preamble by [prefilling Claude’s response](/en/docs/prefill-claudes-response) with an opening XML tag.

* * *

[​

](#xml-best-practices)

XML best practices
------------------------------------------------

To get the most out of XML tags, keep these tips in mind:

*   Use descriptive tag names that reflect the content they contain (e.g., `<instructions>`, `<example>`, `<input>`).
*   Be consistent with your tag names throughout your prompts.
*   Always include both the opening (`<tag>`) and closing (`</tag>`) tags, including when you reference them, such as `Using the document in <doc></doc> tags, answer this question.`
*   You can and should nest XML tags, although more than five layers of nesting may decrease performance depending on the complexity of the use case.

* * *

[​

](#additional-resources)

Additional resources
----------------------------------------------------

*   [Prompt engineering techniques](/en/docs/prompt-engineering): Explore other strategies for optimizing your prompts and enhancing Claude’s performance.
*   [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook/): Browse a collection of Jupyter notebooks featuring copy-able code snippets that demonstrate highly effective and advanced techniques, integrations, and implementations using Claude.
*   [Prompt library](/en/prompt-library): Get inspired by a curated selection of prompts for various tasks and use cases.

[Give Claude a role](/en/docs/give-claude-a-role)[Chain prompts](/en/docs/chain-prompts)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [What are XML tags?](#what-are-xml-tags)
*   [Why use XML tags?](#why-use-xml-tags)
*   [How to use XML tags](#how-to-use-xml-tags)
*   [Handling variable inputs](#handling-variable-inputs)
*   [Requesting structured output](#requesting-structured-output)
*   [XML best practices](#xml-best-practices)
*   [Additional resources](#additional-resources)
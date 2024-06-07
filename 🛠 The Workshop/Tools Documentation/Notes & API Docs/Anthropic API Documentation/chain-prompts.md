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

Chain prompts

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

Chain prompts
=============

You can think of working with large language models like juggling. The more tasks you have Claude handle in a single prompt, the more liable it is to drop something or perform any single task less well. Thus, for complex tasks that require multiple steps or subtasks, we recommend breaking those tasks down into subtasks and chaining prompts to ensure highest quality performance at every step.

[​

](#what-is-prompt-chaining)

What is prompt chaining?
-----------------------------------------------------------

Prompt chaining involves using the output from one prompt as the input for another prompt. By chaining prompts together, you can guide Claude through a series of smaller, more manageable tasks to ultimately achieve a complex goal.

Prompt chaining offers several advantages:

*   Improved accuracy and consistency in the generated output at each distinct step
*   Easier troubleshooting by isolating specific subtasks that may be particularly error-prone or challenging to handle

* * *

[​

](#when-to-use-prompt-chaining)

When to use prompt chaining
------------------------------------------------------------------

Consider using prompt chaining in the following scenarios:

1.  **Multi-step tasks:** If your task requires multiple distinct steps, such as researching a topic, outlining an essay, writing the essay, then formatting the essay, chaining prompts can help ensure each step of the task has Claude’s full focus and is executed at a high level of performance.
2.  **Complex instructions:** When a single prompt contains too many instructions or details, Claude may struggle to follow them consistently. Breaking the task into a series of chained subtasks can improve performance for each subtask.
3.  **Verifying outputs:** You can use chaining to ask Claude to [double-check its own outputs](/en/docs/ask-claude-for-rewrites) with a given rubric and improve its response if needed, ensuring higher quality results. For example, after generating a list of items, you can feed that list back to Claude and ask it to verify the list’s accuracy or completeness.
4.  **Parallel processing:** If your task has multiple independent subtasks, you can create separate prompts for each subtask and run them in parallel to save time.

* * *

[​

](#tips-for-effective-prompt-chaining)

Tips for effective prompt chaining
--------------------------------------------------------------------------------

1.  **Keep subtasks simple and clear:** Each subtask should have a well-defined objective and simple instructions. This makes it easier for Claude to understand and follow.
2.  **Use XML tags:** Enclosing inputs and outputs in [XML tags](/en/docs/use-xml-tags) can help structure the data and make it easier to extract and pass on to the next step when chaining prompts.

* * *

[​

](#examples)

Examples
----------------------------

Here are a few examples showcasing how to use chaining prompts and breaking tasks into subtasks:

### 

[​

](#answering-questions-using-a-document-and-quotes)

Answering questions using a document and quotes

Here we want Claude to, given a document and a question, generate an answer using relevant quotes from the document.

#### 

[​

](#prompt-1-extracting-the-quotes)

Prompt 1: Extracting the quotes

| Role | Content |
| --- | --- |
| User | Here is a document, in <document></document> XML tags:  
  
<document>{{DOCUMENT}}</document>  
  
Please extract, word-for-word, any quotes relevant to the question {{QUESTION}}. Please enclose the full list of quotes in <quotes></quotes> XML tags. If there are no quotes in this document that seem relevant to this question, please say “I can’t find any relevant quotes”. |

#### 

[​

](#prompt-2-using-quotes-output-from-prompt-1-answering-the-question)

Prompt 2 (using `{{QUOTES}}` output from Prompt 1): Answering the question

| Role | Content |
| --- | --- |
| User | I want you to use a document and relevant quotes from the document to answer a question.  
  
Here is the document:  
<document>  
{{DOCUMENT}}  
</document>  
  
Here are direct quotes from the document that are most relevant to the question:  
<quotes>  
{{QUOTES}}  
</quotes>  
  
Please use these to construct an answer to the question “{{QUESTION}}  
  
“Ensure that your answer is accurate and doesn’t contain any information not directly supported by the quotes. |

### 

[​

](#validating-outputs)

Validating outputs

In this example, the goal is to have Claude identify grammatical errors in an article, then double-check that the list of errors is complete.

#### 

[​

](#prompt-1-generating-a-list-of-errors)

Prompt 1: Generating a list of errors

| Role | Prompt 1 |
| --- | --- |
| User | Here is an article:  
<article>  
{{ARTICLE}}  
</article>  
  
Please identify any grammatical errors in the article. Please only respond with the list of errors, and nothing else. If there are no grammatical errors, say “There are no errors.” |

#### 

[​

](#prompt-2-using-errors-output-from-prompt-1-double-checking-that-the-list-is-comprehensive)

Prompt 2 (using `{{ERRORS}}` output from Prompt 1): Double checking that the list is comprehensive

| Role | Prompt 2 |
| --- | --- |
| User | Here is an article:  
<article>  
{{ARTICLE}}  
</article>  
  
Please identify any grammatical errors in the article that are missing from the following list:  
<list>{{ERRORS}}  
</list>  
  
If there are no errors in the article that are missing from the list, say “There are no additional errors.” |

### 

[​

](#parallel-processing)

Parallel processing

In this example, the goal is to have Claude explain a concept to readers at three different levels (1st grade, 8th grade, college freshman) by first creating an outline, then expanding it into a full explanation.

#### 

[​

](#prompt-1-create-three-different-versions-one-for-each-reading-level-create-an-outline)

Prompt 1 (create three different versions, one for each reading level): Create an outline

| Role | Prompt 1 |
| --- | --- |
| User | Here is a concept: {{CONCEPT}}  
  
I want you to write a three sentence outline of an essay about this concept that is appropriate for this level of reader: {{LEVEL}}  
  
Please only respond with your outline, one sentence per line, in <outline></outline> XML tags. Don’t say anything else. |

#### 

[​

](#prompt-2-using-outline-output-from-prompt-1-one-per-reading-level-create-full-explanations-using-the-outline)

Prompt 2 (using `{{OUTLINE}}` output from Prompt 1, one per reading level): Create full explanations using the outline

| Role | Prompt 2 |
| --- | --- |
| User | Here is an outline:  
<outline>  
{{OUTLINE}}  
</outline>  
  
Please expand each sentence in the outline into a paragraph. Use each sentence word-for-word as the first sentence in its corresponding paragraph. Make sure to write at a level appropriate for this type of reader: {{LEVEL}}. |

* * *

[​

](#additional-resources)

Additional resources
----------------------------------------------------

*   [Prompt engineering techniques](/en/docs/prompt-engineering): Explore other strategies for optimizing your prompts and enhancing Claude’s performance.
*   [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook/): Browse a collection of Jupyter notebooks featuring copy-able code snippets that demonstrate highly effective and advanced techniques, integrations, and implementations using Claude.
*   [Prompt library](/en/prompt-library): Get inspired by a curated selection of prompts for various tasks and use cases.

[Use XML tags](/en/docs/use-xml-tags)[Let Claude think](/en/docs/let-claude-think)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [What is prompt chaining?](#what-is-prompt-chaining)
*   [When to use prompt chaining](#when-to-use-prompt-chaining)
*   [Tips for effective prompt chaining](#tips-for-effective-prompt-chaining)
*   [Examples](#examples)
*   [Answering questions using a document and quotes](#answering-questions-using-a-document-and-quotes)
*   [Prompt 1: Extracting the quotes](#prompt-1-extracting-the-quotes)
*   [Prompt 2 (using {{QUOTES}} output from Prompt 1): Answering the question](#prompt-2-using-quotes-output-from-prompt-1-answering-the-question)
*   [Validating outputs](#validating-outputs)
*   [Prompt 1: Generating a list of errors](#prompt-1-generating-a-list-of-errors)
*   [Prompt 2 (using {{ERRORS}} output from Prompt 1): Double checking that the list is comprehensive](#prompt-2-using-errors-output-from-prompt-1-double-checking-that-the-list-is-comprehensive)
*   [Parallel processing](#parallel-processing)
*   [Prompt 1 (create three different versions, one for each reading level): Create an outline](#prompt-1-create-three-different-versions-one-for-each-reading-level-create-an-outline)
*   [Prompt 2 (using {{OUTLINE}} output from Prompt 1, one per reading level): Create full explanations using the outline](#prompt-2-using-outline-output-from-prompt-1-one-per-reading-level-create-full-explanations-using-the-outline)
*   [Additional resources](#additional-resources)
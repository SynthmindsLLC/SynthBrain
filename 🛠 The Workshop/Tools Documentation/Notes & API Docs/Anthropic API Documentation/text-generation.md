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

Text generation

Text generation

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
        
        Overview
        
        
        
        ](/en/docs/text-generation)
    *   [
        
        System prompts
        
        
        
        ](/en/docs/system-prompts)
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

Text generation

Text generation
===============

Claude excels in a wide range of text-based tasks. Claude has been trained to ingest code, prose, and other natural language inputs, and provide text outputs in response. When you send data to Claude in order to generate a response, you are sending a “prompt,” and the act of sending a prompt is called ”[prompting](/en/docs/intro-to-prompting).”

Prompts are best written as natural language queries as if you are instructing someone to do something, with the more detail the better. You can further improve your baseline prompt with [prompt engineering](/en/docs/prompt-engineering).

* * *

[​

](#text-use-cases-and-capabilities)

Text use cases and capabilities
--------------------------------------------------------------------------

Claude can handle a diverse range of text-based tasks, including but not limited to:

*   Text summarization
*   Content generation
*   Data / entity extraction
*   Question answering
*   Text translation
*   Text-based analysis and recommendations
*   Dialogue and conversation
*   Code explanation and generation

For a comprehensive guide on text-based use cases and capabilities, visit [use cases and capabilities](/en/docs/use-cases-and-capabilities).

* * *

[​

](#prompt-engineering-guide)

Prompt engineering guide
------------------------------------------------------------

To get the most out of Claude 3 and enhance its performance for your specific tasks, you may want to apply specific prompt engineering techniques to your prompt. Our [prompt engineering](/en/docs/prompt-engineering) covers various strategies and tips to help you craft the most effective prompts to optimize Claude 3’s output. With [legacy models](/en/docs/legacy-model-guide), prompt engineering may be more necessary in order to elicit maximum performance, whereas Claude 3 models are far more steerable and easy to instruct.

* * *

[​

](#anthropic-cookbook)

Anthropic Cookbook
------------------------------------------------

To see code examples of Claude’s text generation capabilities in action, check out the [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook?tab=readme-ov-file#anthropic-cookbook), which houses a set of recipes in the form of Jupyter notebooks. These notebooks feature copy-able code that demonstrate how to use Claude in more advanced scenarios, such as [uploading PDFs](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/pdf%5Fupload%5Fsummarization.ipynb), [tool use and function calling](https://github.com/anthropics/anthropic-cookbook/blob/main/function%5Fcalling/function%5Fcalling.ipynb), [embeddings](https://github.com/anthropics/anthropic-cookbook/blob/main/third%5Fparty/voyageai/how%5Fto%5Fcreate%5Fembeddings.md), and more.

* * *

[​

](#prompt-library)

Prompt library
----------------------------------------

For a wide range of text-based prompts that showcase Claude’s capabilities and help you get started with various tasks, visit our [prompt library](/en/prompt-library). The library contains prompts for different use cases and complexity levels, making it easier for you to find and adapt prompts to your specific needs.

* * *

[​

](#api-documentation)

API documentation
----------------------------------------------

To understand how to interact with Claude via our API, consult our [API documentation](/en/api/getting-started). The documentation provides detailed information on how to send requests, handle responses, and troubleshoot errors.

[Glossary](/en/docs/glossary)[System prompts](/en/docs/system-prompts)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [Text use cases and capabilities](#text-use-cases-and-capabilities)
*   [Prompt engineering guide](#prompt-engineering-guide)
*   [Anthropic Cookbook](#anthropic-cookbook)
*   [Prompt library](#prompt-library)
*   [API documentation](#api-documentation)
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

System prompts

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

System prompts
==============

[​

](#what-is-a-system-prompt)

What is a system prompt?
-----------------------------------------------------------

A system prompt is a way to provide context, instructions, and guidelines to Claude before presenting it with a question or task. By using a system prompt, you can set the stage for the conversation, specifying Claude’s role, personality, tone, or any other relevant information that will help it better understand and respond to the user’s input.

System prompts can include:

*   Task instructions and objectives
*   Personality traits, roles, and tone guidelines
*   Contextual information for the user input
*   Creativity constraints and style guidance
*   External knowledge, data, or reference material
*   Rules, guidelines, and guardrails
*   Output verification standards and requirements

* * *

[​

](#benefits-of-using-system-prompts)

Benefits of using system prompts
----------------------------------------------------------------------------

Incorporating well-crafted system prompts can significantly enhance Claude’s performance and output quality. Some key benefits include:

1.  **Improved role-playing and character consistency**: When assigning Claude a specific role or personality through a system prompt, it can maintain that character more effectively throughout the conversation, exhibiting more natural and creative responses while staying in character.
2.  **Increased adherence to rules and instructions**: System prompts can help Claude better understand and follow guidelines, making it less likely to perform prohibited tasks, output restricted content, or deviate from the given instructions.
3.  **Enhanced context understanding**: By providing relevant background information or reference material in the system prompt, you can improve Claude’s comprehension of the user’s input and enable it to generate more accurate and context-aware responses.
4.  **Customized output formatting**: System prompts can be used to specify desired output formats, such as headers, lists, tables, or code blocks, ensuring that Claude’s responses are structured and presented in a way that best suits your needs.

It’s important to note that while system prompts can increase Claude’s robustness and resilience against unwanted behavior, they do not guarantee complete protection against [jailbreaks or leaks](/en/docs/system-prompts#do-system-prompts-make-my-prompts-jailbreak-proof-or-leak-proof). However, they do provide an additional layer of guidance and control over Claude’s output.

* * *

[​

](#how-to-use-system-prompts)

How to use system prompts
--------------------------------------------------------------

To use system prompts with the [Messages API](/en/api/messages), set the `system` parameter to your desired system prompt text. Here’s an example API call:

Python

Copy

    import anthropic
    
    client = anthropic.Client(api_key="YOUR_API_KEY")
    
    response = client.messages.create(
        model="claude-2.1",
        system="Respond only in Spanish.", # <-- system prompt
        messages=[
            {"role": "user", "content": "Hello, Claude!"} # <-- user prompt
        ]
    )
    
    print(response.message)
    

For more information, refer to our [Messages API documentation](/en/api/messages).

> **Note**: You can also use system prompts in the [Console](https://console.anthropic.com/workbench/), but not on [claude.ai](https://claude.ai/).

* * *

[​

](#prompting-techniques)

Prompting techniques
----------------------------------------------------

You can apply the same [prompting techniques](/en/docs/prompt-engineering) you would use in a user prompt to a system prompt instead. For example, you can:

1.  **Specify output formatting**: Provide [example responses](/en/docs/use-examples) or instructions for [desired output patterns](/en/docs/control-output-format) within the system prompt to guide Claude’s behavior.
2.  **Provide documents, guides, and reference material**: Include relevant information or [RAG](/en/docs/glossary#rag-retrieval-augmented-generation) content in the system prompt to help Claude generate more informed and accurate responses.
3.  **Use XML tags, especially to structure long documents**: [Use XML tags](/en/docs/use-xml-tags) to organize your system prompt into sections to improve clarity. When incorporating multiple or lengthy documents in the system prompt, you can use use the [multi-document XML format](/en/docs/long-context-window-tips#structuring-long-documents) to help Claude better understand and utilize the provided information.

* * *

[​

](#frequently-asked-questions)

Frequently asked questions
----------------------------------------------------------------

### 

[​

](#how-do-i-know-when-to-use-a-system-prompt-vs-a-user-prompt)

How do I know when to use a system prompt vs. a user prompt?

Prompting is all experimentation, so we recommend that you try it both ways! But in general, you can think about system prompts as a space to provide guidance about the overall interaction with Claude, and the `user` turn as part of the interaction itself, or when you have only a one-off task you want to accomplish.

### 

[​

](#how-can-i-convert-my-existing-user-only-prompts-to-use-system-prompts)

How can I convert my existing user-only prompts to use system prompts?

To convert your `user`\-only prompts to system prompts, simply move any content that is not part of the user’s input to the `system` parameter in the [Messages API](/en/api/messages). This can include task instructions, personality guidelines, reference material, or any other contextual information that helps set the stage for the conversation. We encourage you to experiment to see what works best in which field.

### 

[​

](#where-can-i-use-system-prompts)

Where can I use system prompts?

System prompts are currently available for use with Claude 3 models and Claude 2.1 through our API, [Console](https://console.anthropic.com/), Amazon Bedrock’s API, and Google Cloud Vertex AI’s API. They are not supported on [claude.ai](https://claude.ai/) at this time.

### 

[​

](#do-system-prompts-make-my-prompts-jailbreak-proof-or-leak-proof)

Do system prompts make my prompts jailbreak-proof or leak-proof?

While Claude is already highly resilient to jailbreaks and unwanted behavior due to its training methods (e.g., RLHF and Constitutional AI), system prompts can further enhance Claude’s ability to adhere to instructions and guidelines. However, they do not guarantee complete protection against [jailbreaks](/en/docs/mitigating-jailbreaks-prompt-injections) or [leaks](/en/docs/reducing-prompt-leaks).

[Overview](/en/docs/text-generation)[Vision](/en/docs/vision)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [What is a system prompt?](#what-is-a-system-prompt)
*   [Benefits of using system prompts](#benefits-of-using-system-prompts)
*   [How to use system prompts](#how-to-use-system-prompts)
*   [Prompting techniques](#prompting-techniques)
*   [Frequently asked questions](#frequently-asked-questions)
*   [How do I know when to use a system prompt vs. a user prompt?](#how-do-i-know-when-to-use-a-system-prompt-vs-a-user-prompt)
*   [How can I convert my existing user-only prompts to use system prompts?](#how-can-i-convert-my-existing-user-only-prompts-to-use-system-prompts)
*   [Where can I use system prompts?](#where-can-i-use-system-prompts)
*   [Do system prompts make my prompts jailbreak-proof or leak-proof?](#do-system-prompts-make-my-prompts-jailbreak-proof-or-leak-proof)
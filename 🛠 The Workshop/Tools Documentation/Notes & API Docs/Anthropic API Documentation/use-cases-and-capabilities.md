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

Production guides

Use cases and capabilities

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

Production guides

Use cases and capabilities
==========================

Claude is a powerful AI assistant capable of handling a wide range of tasks across various industries and domains. We hope this guide helps spark creativity and inspires you to try Claude for many varied use cases. This guide has mini starter prompts and ideas, but we encourage you to check out our [intro to prompting](/en/docs/intro-to-prompting) page if you want to create more complex prompts.

* * *

[​

](#text-capabilities)

Text capabilities
----------------------------------------------

Claude excels at processing and understanding text, making it an invaluable tool for numerous applications. Some of its key text capabilities include:

| Capability | Description |
| --- | --- |
| **Summarization** | Condensing long articles, reports, or documents into concise summaries |
| **Writing and editing** | Assisting with content creation, proofreading, and improving written materials |
| **Text analysis and explanation** | Providing insights, extracting key information, and explaining complex concepts |
| **Content generation** | Creating original content based on prompts or guidelines |
| **Code explanation & generation** | Helping developers understand and write code more efficiently |
| **Language understanding** | Comprehending and interpreting natural language input |
| **Text rewriting** | Rephrasing or restructuring text to improve clarity or style |
| **Information search & extraction** | Finding and extracting relevant information from large text corpora |
| **Suggestions and recommendations** | Offering ideas, solutions, or recommendations based on given context |
| **Question answering** | Providing accurate and relevant answers to user queries |
| **Translation** | Converting text from one language to another |
| **Outlining and structuring** | Organizing ideas and information into logical outlines or structures |
| **Calculations and math** | Performing basic mathematical operations and solving simple equations |
| **Engaging in discussions** | Participating in interactive conversations and providing meaningful responses |
| **Using functions and tools** | Integrating with external tools and functions to enhance its capabilities (see our [tool use guide](/en/docs/tool-use)) |

### 

[​

](#lightweight-example-text-use-cases-and-prompts)

Lightweight example text use cases and prompts

#### 

[​

](#summarize-a-long-article-for-a-quick-overview)

Summarize a long article for a quick overview:

> Please summarize the following article in 5 sentences or less: \[Article text\]

#### 

[​

](#assist-with-writing-a-persuasive-essay)

Assist with writing a persuasive essay:

> I need help writing a persuasive essay on the importance of renewable energy. Please provide an outline with key points and arguments, and then generate a compelling introduction paragraph.

#### 

[​

](#explain-a-complex-scientific-concept-in-simple-terms)

Explain a complex scientific concept in simple terms:

> Can you explain the concept of quantum entanglement in a way that a high school student could understand? Please provide an analogy and a real-world example.

For more inspiration and examples, check out our [prompt library](/en/prompt-library) and our [intro to prompting](/en/docs/intro-to-prompting) page, where Claude can help you create effective prompts for your specific needs.

* * *

[​

](#vision-capabilities)

Vision capabilities
--------------------------------------------------

In addition to its text processing abilities, Claude can also work with images, enabling a range of vision-related tasks:

| Capability | Description |
| --- | --- |
| **Describing visual content** | Providing detailed descriptions of images |
| **Image classification** | Identifying and categorizing objects, scenes, or actions in images |
| **Object detection & recognition** | Locating and identifying specific objects within an image |
| **Image interpretation and contextualization** | Explaining the meaning, context, and relationships in images |
| **Explaining visual elements** | Providing insights into the composition, style, or techniques used in an image |
| **Answering questions about images** | Responding to queries related to the content or context of an image |
| **Understanding visual information** | Comprehending and analyzing the information conveyed through images |
| **Reasoning about image content** | Drawing conclusions or making inferences based on visual information |
| **Offering critiques or suggestions** | Providing constructive feedback or suggestions for improvement on images |
| **Evaluating visual content** | Assessing the quality, effectiveness, or impact of images |
| **Providing feedback on images** | Offering insights, opinions, or recommendations based on image content |
| **Suggesting actions based on visuals** | Recommending steps or actions to take based on the information in an image |
| **Assisting with image-related tasks** | Supporting users in tasks such as image editing, manipulation, or organization |
| **Converting or extracting image data** | Transforming image data into different formats or extracting specific elements |
| **Transcribing text from images** | Recognizing and converting text within images into machine-readable formats |
| **Translating text within images** | Translating text found in images from one language to another |
| **Generating code from images** | Creating code snippets or templates based on visual representations or diagrams |
| **Writing narratives about images** | Crafting stories, captions, or descriptions inspired by image content |
| **Tabulating data from images** | Extracting and organizing data or information presented visually in images |

### 

[​

](#example-use-cases-and-prompts)

Example use cases and prompts

#### 

[​

](#describe-an-image-for-a-visually-impaired-user)

Describe an image for a visually impaired user:

> \[Image\] Please provide a detailed description of this image, focusing on the key elements, colors, and any text that appears.

#### 

[​

](#analyze-the-composition-and-techniques-used-in-a-photograph)

Analyze the composition and techniques used in a photograph:

> \[Image\] I’d like your help analyzing the composition and techniques used in this photograph. Please describe the use of lighting and color, and explain how the photographer has used elements like rule of thirds, leading lines, or depth of field to create an engaging image.

#### 

[​

](#suggest-improvements-for-a-product-design-based-on-an-image)

Suggest improvements for a product design based on an image:

> \[Image\] Based on this image of our new product design, please provide suggestions for improvements in terms of aesthetics, functionality, and user experience. Consider factors like ergonomics, material choice, and overall visual appeal.

Remember to check out our [intro to prompting](/en/docs/intro-to-prompting) guide and [vision prompting tips](/en/docs/vision#prompting-tips) to get Claude’s help writing prompts for further use cases.

* * *

[​

](#industries)

Industries
--------------------------------

Claude’s versatility makes it a valuable asset across a wide range of industries, including but not limited to:

*   General Business
*   Technology and Engineering
*   Marketing, Consumer Goods, Retail
*   Health Care
*   Media, Entertainment, Culture
*   Education
*   Geography and Agriculture
*   Finance and Banking
*   Government and Public Sector
*   Legal and Compliance
*   Travel and Hospitality
*   Energy and Utilities
*   Transportation and Logistics
*   Real Estate and Construction
*   Telecommunications
*   Non-profit and Social Services
*   Sports and Fitness
*   Automotive
*   Aerospace and Defense
*   Insurance
*   Manufacturing
*   Pharmaceuticals and Biotechnology
*   Mining and Natural Resources
*   Environmental Services
*   Food and Beverage
*   Fashion and Apparel
*   Professional Services (Consulting, Accounting, etc.)
*   Security and Surveillance

No matter your industry or domain, Claude can help streamline processes, enhance decision-making, and unlock new opportunities for growth and innovation. Experiment with different prompts and tasks to find the best ways to integrate Claude into your workflow.

For more guidance and inspiration, visit our [prompt library](/en/prompt-library) and [intro to prompting](/en/docs/intro-to-prompting) page, where you can find a wealth of resources to help you get the most out of Claude.

[Keep Claude in character](/en/docs/keep-claude-in-character)[Empirical performance evaluations](/en/docs/empirical-performance-evaluations)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [Text capabilities](#text-capabilities)
*   [Lightweight example text use cases and prompts](#lightweight-example-text-use-cases-and-prompts)
*   [Summarize a long article for a quick overview:](#summarize-a-long-article-for-a-quick-overview)
*   [Assist with writing a persuasive essay:](#assist-with-writing-a-persuasive-essay)
*   [Explain a complex scientific concept in simple terms:](#explain-a-complex-scientific-concept-in-simple-terms)
*   [Vision capabilities](#vision-capabilities)
*   [Example use cases and prompts](#example-use-cases-and-prompts)
*   [Describe an image for a visually impaired user:](#describe-an-image-for-a-visually-impaired-user)
*   [Analyze the composition and techniques used in a photograph:](#analyze-the-composition-and-techniques-used-in-a-photograph)
*   [Suggest improvements for a product design based on an image:](#suggest-improvements-for-a-product-design-based-on-an-image)
*   [Industries](#industries)
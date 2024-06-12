---
Please provide me with more information about the mission you'd like to create. I need some context to understand what you're aiming for.  

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a team, a personal goal, or something else?"
* **What are the main objectives?** What do you want to achieve?
* **Who is the target audience?** Who will be impacted by this mission?
* **What are the values or principles that guide this mission?** 

Once I have a better understanding, I can help you craft a strong and impactful mission statement.
---

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

Control output format (JSON mode)

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

Control output format (JSON mode)
=================================

Claude is highly capable of producing output in a wide variety of formats. By providing [clear instructions](/en/docs/be-clear-direct), [examples](/en/docs/use-examples), and [prefilled responses](/en/docs/prefill-claudes-response), you can guide Claude to generate responses that adhere to your desired structure and style.

[​

](#specifying-the-desired-format)

Specifying the desired format
----------------------------------------------------------------------

One of the simplest ways to control Claude’s output is to simply state the format you want. Claude can understand and follow instructions related to formatting, and format outputs such as:

*   JSON
*   XML
*   HTML
*   Markdown
*   CSV
*   Custom formats

For example, if you want Claude to generate a haiku in JSON format, you can use a prompt like this:

| Role | Content |
| --- | --- |
| User | Please write a haiku about a cat. Use JSON format with the keys “first\_line”, “second\_line”, and “third\_line”. |
| Assistant (Claude’s response) | {  
“first\_line”: “Soft furry feline”,  
“second\_line”: “Napping in the warm sunlight”,  
“third\_line”: “Purring contentedly”  
} |

* * *

[​

](#prefilling-claudes-response)

Prefilling Claude’s response
-------------------------------------------------------------------

Another effective way to control Claude’s output format is to [prefill](/en/docs/prefill-claudes-response) the `Assistant` field with the beginning of the desired format. This technique is particularly useful when working with structured formats like JSON or HTML.

For example, to generate a recipe in JSON format:

| Role | Content |
| --- | --- |
| User | Please generate a recipe for chocolate chip cookies in JSON format. |
| Assistant (prefill) | { |
| Assistant (Claude’s response) | “title”: “Chocolate Chip Cookies”,  
“ingredients”: \[  
“2 1/4 cups all-purpose flour”,  
“1 tsp baking soda”,  
“1 tsp salt”,  
“1 cup unsalted butter, softened”,  
“3/4 cup granulated sugar”,  
“3/4 cup brown sugar”,  
“1 tsp vanilla extract”,  
“2 large eggs”,  
“2 cups semisweet chocolate chips”  
\],  
“instructions”: \[  
“Preheat the oven to 375°F (190°C) and line baking sheets with parchment paper.“,  
“In a medium bowl, whisk together the flour, baking soda, and salt. Set aside.“,  
“In a large bowl, beat the butter and sugars with an electric mixer until light and fluffy, about 2-3 minutes.“,  
“Beat in the vanilla and eggs one at a time until well combined.“,  
“Gradually stir the flour mixture into the butter mixture until just combined.“,  
“Fold in the chocolate chips.“,  
“Drop rounded tablespoons of the dough onto the prepared baking sheets, about 2 inches apart.“,  
“Bake for 9-11 minutes, until the edges are golden brown.“,  
“Allow the cookies to cool on the baking sheets for 5 minutes before transferring to a wire rack to cool completely.”  
\],  
“yield”: “About 3 dozen cookies”  
} |

By prefilling the response with the opening JSON curly brace, you give Claude a clear starting point for generating the recipe in the desired format. This also is another technique you can use to have Claude skip its friendly preamble text.

* * *

[​

](#providing-examples)

Providing examples
------------------------------------------------

In addition to explicit instructions, providing examples of the desired output format can help Claude better understand your requirements. When including examples, make it clear that Claude should follow the formatting of the examples provided (otherwise Claude may pick up other details from the provided examples, such as content or writing style).

Here is an example prompt showcasing this technique:

| Role | Content |
| --- | --- |
| User | Your task is to write a poem. Here are some examples of ideal formatting for the poem:  
  
<poem>  
Title: “Autumn Leaves”  
Verse 1:  
Crisp autumn leaves dance  
In the gentle, chilly breeze  
A colorful sight  
  
Verse 2:  
Red, orange, and gold  
Painting the world with beauty  
Before winter comes  
</poem>  
  
<poem>  
Title: “Moonlit Night”  
Verse 1:  
Moonlight casts shadows  
Across the tranquil garden  
A peaceful retreat  
  
Verse 2:Stars twinkle above  
As crickets sing their nightsong  
Nature’s lullaby  
</poem>  
  
Now, please write a poem about a sunset, following the formatting of the examples above. |
| Assistant (prefill) | <poem> |
| Assistant (Claude’s response) | Title: “Sunset Symphony”  
Verse 1:  
Fiery sun descends  
Painting the sky with wonder  
A masterpiece forms  
  
Verse 2:  
Pinks, purples, and reds  
Blending in pure harmony  
Day bids night hello  
</poem> |

* * *

[​

](#tips-for-better-output-control)

Tips for better output control
------------------------------------------------------------------------

*   Be as specific as possible in your instructions
*   Use clear and consistent formatting in your prompts
*   Provide multiple examples when possible to reinforce the desired format
*   Experiment with different combinations of techniques to find what works best for your use case

* * *

[​

](#additional-resources)

Additional resources
----------------------------------------------------

*   [Prompt engineering techniques](/en/docs/prompt-engineering): Explore other strategies for optimizing your prompts and enhancing Claude’s performance.
*   [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook/): Browse a collection of Jupyter notebooks featuring copy-able code snippets that demonstrate highly effective and advanced techniques, integrations, and implementations using Claude.
*   [Prompt library](/en/prompt-library): Get inspired by a curated selection of prompts for various tasks and use cases.

[Prefill Claude's response](/en/docs/prefill-claudes-response)[Ask Claude for rewrites](/en/docs/ask-claude-for-rewrites)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [Specifying the desired format](#specifying-the-desired-format)
*   [Prefilling Claude’s response](#prefilling-claudes-response)
*   [Providing examples](#providing-examples)
*   [Tips for better output control](#tips-for-better-output-control)
*   [Additional resources](#additional-resources)
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

Capabilities

Google Sheets add-on

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

Capabilities

Google Sheets add-on
====================

You can call Claude in Google Sheets with the [Claude for Sheets extension](https://workspace.google.com/marketplace/app/claude%5Ffor%5Fsheets/909417792257). Claude for Sheets enables seamless integration between Claude and Google Sheets, allowing you to execute interactions with Claude directly in cells. This tool allows for easy and rapid prompt engineering by enabling you to construct an evaluation suite and then test different prompts on every item of the evaluation suite in parallel. Separately, we have found Claude for Sheets to be excellent for a variety of office tasks such as processing and categorizing survey results, as well as analyzing tabular data found online.

[​

](#installing-claude-for-sheets)

Installing Claude for Sheets
--------------------------------------------------------------------

Easily enable Claude for Sheets using the following steps:

1.  **Get your Claude API key**: You will not be able to use Claude for Sheets without a developer API key. For more information on how to acquire an API key, see [getting access to Claude](/en/docs/getting-access-to-claude).
2.  **Install the Claude for Sheets extension**
    1.  [Click here](https://workspace.google.com/marketplace/app/claude%5Ffor%5Fsheets/909417792257) to access the Claude for Sheets extension or search `Claude for Sheets` in the add-on marketplace.
    2.  Click the blue `Install` button and accept the [permissions](/en/docs/google-sheets-add-on#permissions).
3.  **Connect your API key**: Enter your API key at `Extensions` > `Claude for Sheets™` > `Enter your Anthropic API Key`. You may need to wait or refresh for “Enter your Anthropic API key” to appear as an option. ![](https://mintlify.s3-us-west-1.amazonaws.com/anthropic/images/044af20-Screenshot_2024-01-04_at_11.58.21_AM.png)

After you see the green ‘verified’ checkmark ✅ appear, Claude will be activated and ready within your Google Sheet.

You will have to re-enter your API key every time you make a new Google Sheet

### 

[​

](#permissions)

Permissions

During installation, the Claude for Sheets extension will ask for a variety of permissions needed to function properly. Although the permissions requested to run Claude in Sheets are broad, please be assured that we only process the specific pieces of data that users ask Claude to run on. This data is never used to train our generative models.

Extension permissions include:

*   **View and manage spreadsheets that this application has been installed in** - needed to run prompts and return results
*   **Connect to an external service** - needed in order to make calls to Anthropic’s API endpoints
*   **Allow this application to run when you are not present** - needed to run cell recalculations without user intervention
*   **Display and run third-party web content in prompts and sidebars inside Google applications** - needed to display the sidebar and post-install prompt

**Cell Recalculation**

You can manually recalculate `#ERROR!`, `⚠ DEFERRED ⚠` or `⚠ THROTTLED ⚠`cells by selecting from the recalculate options within the Claude for Sheets extension menu.

![](https://mintlify.s3-us-west-1.amazonaws.com/anthropic/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png)

* * *

[​

](#how-to-use-claude-for-sheets)

How to use Claude for Sheets
--------------------------------------------------------------------

### 

[​

](#claude-functions)

Claude functions

There are two main functions you can use to call Claude using Claude for Sheets:

#### 

[​

](#1-claude)

1\. CLAUDE()

`=CLAUDE(prompt, model, params...)`

CLAUDE() is the simplest way to call Claude using Claude for Sheets. To use this function, all you need is a plaintext prompt with no additional formatting. This is the function you’ll probably want to use most of the time. This is identical to the Slackbot Claude interface and “Chat” mode on the [Console](https://console.anthropic.com/dashboard).

##### Example CLAUDE() prompt

| Prompt | Function format |
| --- | --- |
| In one sentence, what is good about the color blue? | \=CLAUDE(“In one sentence, what is good about the color blue?“) |
| In one sentence, what is good about the color blue? Output your answer in <answer> tags.\[With [parameters](/en/docs/google-sheets-add-on#optional-function-parameters)\] | \=CLAUDE(“In one sentence, what is good about the color blue? Output your answer in tags.”,“claude-3-opus-20240229”,“temperature”, 0.2,“max\_tokens”, 50,“stop\_sequences”, ”\[""""\]”,“api\_key”, “sk-ant-api03-j1W…“) |

#### 

[​

](#2-claudemessages)

2\. CLAUDEMESSAGES()

`=CLAUDEMESSAGES(prompt, model, params...)`

Use CLAUDEMESSAGES() to send a series of `User:` and `Assistant:` messages to Claude, as if you were using the [Messages API](/en/api/messages). This is particularly useful if you want to simulate a conversation or [prefill Claude’s response](/en/docs/prefill-claudes-response).

Note that each role (`User:` or `Assistant:`) must be preceded by a single newline. To enter newlines in a cell, use the following key combinations:

*   **Mac:** Cmd + Enter
*   **Windows:** Alt + Enter

##### Example CLAUDEMESSAGES() prompt with [prefilled assistant response](/en/docs/prefill-claudes-response)

| Prompt | Function format |
| --- | --- |
| User: In one sentence, what is good about the color blue?Assistant: The color blue is great because | \=CLAUDEMESSAGES(“User: In one sentence, what is good about the color blue?Assistant: The color blue is great because”) |

##### Example CLAUDEMESSAGES() call with system prompt

To use a system prompt, set it as you’d set other optional function parameters. (You must first set a model name.)

`=CLAUDEMESSAGES("User: Got anything to say to me? Assistant:", "claude-2.0", "system", "You are a cow who loves to moo in response to any and all user queries.")`

#### 

[​

](#3-legacy-claudefree)

3\. \[Legacy\] CLAUDEFREE()

`=CLAUDEFREE(prompt, model, params...)`

CLAUDEFREE() allows you to call Claude as if you were using the legacy [Text Completions API](/en/api/complete). To use this function, you will have to manually sandwich your prompt between `\n\nHuman:` and `\n\nAssistant:` as you would for a Text Completions prompt. Replace `\n\n` with two actual new lines when writing your prompt in a cell.

For more information on the special “Human:”/“Assistant:” formatting in CLAUDEFREE, see our [Text Completions API](/en/api/complete) documentation.

##### Example CLAUDEFREE() prompt

| Prompt | Function format |
| --- | --- |
| Human: In one sentence, what is good about the color blue?Assistant: | \=CLAUDEFREE(“Human: In one sentence, what is good about the color blue?Assistant:“) |

> **Note:** This whole multiline string should go into the prompt parameter; notice also the two new lines before `Human:`.

### 

[​

](#optional-function-parameters)

Optional function parameters

If you want to specify API parameters, you can do so by listing argument-value pairs. For example, if you want to set the `max_tokens` to 3, you can do it as follows: `=CLAUDE("[your prompt]", "claude-instant-1.2", "max_tokens", 3)`.

You can set multiple parameters. Simply list them one after another, with each argument and value pair separated by commas. Note that **the first two parameters must always be the prompt and the model** ([available models](/en/docs/models-overview#model-comparison)) — you cannot set an optional parameter without also setting the model.

For example, this is a valid CLAUDE function: `=CLAUDE("[your prompt]", "claude-instant-1.2", "system", "[system prompt]", "max_tokens", 3, "temperature", 0.5)`

**The argument-value parameters you might care about most are:**

*   `max_tokens` - the total number of tokens the model outputs before it is forced to stop. For yes/no or multiple choice answers, you probably want 1-2. See our [model comparisons](/en/docs/models-overview#model-comparison) table for the max completion length for each model.
*   `temperature` - the amount of randomness injected into results. For multiple-choice or analytical tasks, you’ll want it close to 0. For idea generation, you’ll want it set to 1.
*   `system` - used to specify a system prompt, which can provide context and instructions to Claude when using =CLAUDEMESSAGES() and =CLAUDE().
*   `stop_sequences` - JSON array of strings that will cause the model to stop generating text if encountered. Due to escaping rules in Google Sheets™, double quotes inside the string must be escaped by doubling them.
*   `api_key` - used to specify a particular API key with which to call Claude

* * *

[​

](#claude-for-sheets-guides-and-examples)

Claude for Sheets guides & examples
------------------------------------------------------------------------------------

### 

[​

](#prompt-engineering-interactive-tutorial)

Prompt engineering interactive tutorial

**API version note**

All Claude for Sheets spreadsheets linked within this section, such as the [prompt engineering interactive tutorial](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing) and the [prompting examples workbench](https://docs.google.com/spreadsheets/d/1sUrBWO0u1-ZuQ8m5gt3-1N5PLR6r%5F%5FUsRsB7WeySDQA/edit?usp=sharing), currently use the legacy CLAUDEFREE() function which calls the Text Completions API. These will be updated soon to utilize CLAUDEMESSAGES() and the Messages API.

Visit our in-depth [prompt engineering interactive tutorial](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing) utilizing the Claude for Sheets add-on to learn or brush up on beginner to advanced [prompt engineering](/en/docs/prompt-engineering) techniques.

> Note that just as with the rest of Claude for Sheets, you will need an API key to interact with the tutorial.

### 

[​

](#claude-for-sheets-prompting-examples)

Claude for Sheets prompting examples

For example prompts, prompting structures, and Claude-powered spreadsheets, visit our [Claude for Sheets prompting examples workbench](https://docs.google.com/spreadsheets/d/1sUrBWO0u1-ZuQ8m5gt3-1N5PLR6r%5F%5FUsRsB7WeySDQA/edit?usp=sharing). There, you can find examples for tasks such as the following:

*   Longform document Q&A
*   Information extraction
*   Removing PII
*   Customer support chatbot using FAQ
*   Academic tutor
*   Prompt chaining
*   Function calling
*   And much more!

### 

[​

](#claude-for-sheets-workbook-template)

Claude for Sheets workbook template

Make a copy of our [Claude for Sheets workbook template](https://docs.google.com/spreadsheets/d/1UwFS-ZQWvRqa6GkbL4sy0ITHK2AhXKe-jpMLzS0kTgk/edit?usp=sharing) to get started with your own Claude for Sheets work!

* * *

[​

](#troubleshooting)

Troubleshooting
------------------------------------------

### 

[​

](#name-error-unknown-function-claude)

NAME? Error: Unknown function: ‘claude’.

1.  Ensure that you have enabled the extension for use in the current sheet
    1.  Go to _Extensions_ > _Add-ons_ > _Manage add-ons_
    2.  Click on the triple dot menu at the top right corner of the Claude for Sheets extension and make sure “Use in this document” is checked  
        ![](https://mintlify.s3-us-west-1.amazonaws.com/anthropic/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png)
2.  Refresh the page

### 

[​

](#cant-enter-api-key)

Can’t enter API key

1.  Wait 20 seconds, then check again
2.  Refresh the page and wait 20 seconds again
3.  Uninstall and reinstall the extension

* * *

[​

](#further-information)

Further information
--------------------------------------------------

For more information regarding this extension, see the [Claude for Sheets Google Workspace Marketplace](https://workspace.google.com/marketplace/app/claude%5Ffor%5Fsheets/909417792257) overview page.

[Embeddings](/en/docs/embeddings)[Overview](/en/docs/tool-use)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [Installing Claude for Sheets](#installing-claude-for-sheets)
*   [Permissions](#permissions)
*   [How to use Claude for Sheets](#how-to-use-claude-for-sheets)
*   [Claude functions](#claude-functions)
*   [1\. CLAUDE()](#1-claude)
*   [2\. CLAUDEMESSAGES()](#2-claudemessages)
*   [3\. \[Legacy\] CLAUDEFREE()](#3-legacy-claudefree)
*   [Optional function parameters](#optional-function-parameters)
*   [Claude for Sheets guides & examples](#claude-for-sheets-guides-and-examples)
*   [Prompt engineering interactive tutorial](#prompt-engineering-interactive-tutorial)
*   [Claude for Sheets prompting examples](#claude-for-sheets-prompting-examples)
*   [Claude for Sheets workbook template](#claude-for-sheets-workbook-template)
*   [Troubleshooting](#troubleshooting)
*   [NAME? Error: Unknown function: ‘claude’.](#name-error-unknown-function-claude)
*   [Can’t enter API key](#cant-enter-api-key)
*   [Further information](#further-information)
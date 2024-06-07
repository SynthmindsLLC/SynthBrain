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

Tool use (function calling)

Legacy tool use

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
    
    *   [
        
        Overview
        
        
        
        ](/en/docs/tool-use)
    *   [
        
        Tool use examples
        
        
        
        ](/en/docs/tool-use-examples)
    *   [
        
        Tool use pricing and tokens
        
        
        
        ](/en/docs/tool-use-pricing-and-tokens)
    *   [
        
        Legacy tool use
        
        
        
        ](/en/docs/legacy-tool-use)

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

Tool use (function calling)

Legacy tool use
===============

**This tool use format is out of date**

We **highly recommend that you switch as soon as possible to our [improved tool use structure](/en/docs/tool-use)**, which is more reliable and enables higher quality performance, especially for more complex tool use tasks.

This tool use format is **not optimized for Claude 3 and may result in poorer performance** than our updated tool use format.

* * *

[​

](#how-legacy-tool-use-works)

How legacy tool use works
--------------------------------------------------------------

With legacy tool use, functions are defined within the prompt itself. When you provide Claude with descriptions of tools and functions it can use, Claude is able to intelligently decide when and how to use those tools to help answer questions and complete tasks.

For example, let’s say you provide Claude (in the prompt) a function called `get_weather(location)` that retrieves the current weather for a given location. If a user then asks “What’s the weather like in London right now?”, Claude will recognize that it can use the `get_weather` function you provided to look up the answer.

Behind the scenes, this is a multi-step process:

1.  The [function definitions](/en/docs/legacy-tool-use#defining-functions) and user question are both passed to Claude in a single prompt
    *   Claude not only needs the tools & their descriptions in order to successfully decide whether to use the tools, but likely also accompanying examples of situations in which such tools ought to be used, depending on the complexity of the use case and tools.
2.  Claude assesses the user’s question and decides which function(s) to call and with what arguments
3.  Claude constructs a [properly formatted](/en/docs/legacy-tool-use#function-calling-format) function call
4.  The function call is intercepted via client code with a clear `stop_sequence`, and the actual function is executed on the client side
5.  The function result is passed back to Claude
6.  Claude uses the function result to formulate its final response to the user

This technique allows Claude to leverage external knowledge and capabilities while still maintaining a conversational interface.

* * *

[​

](#defining-functions)

Defining functions
------------------------------------------------

Functions are defined by providing Claude with a description of the function wrapped in XML tags. The description should include:

*   The function name
*   A plaintext explanation of what the function does
*   The expected parameters, their types, and descriptions
*   The return values and types
*   Any exceptions that can be raised

Here is an example function definition:

XML

Copy

    <tool_description>
    <tool_name>get_weather</tool_name>
    <description>
    Retrieves the current weather for a specified location.
    Returns a dictionary with two fields:
    - temperature: float, the current temperature in Fahrenheit
    - conditions: string, a brief description of the current weather conditions
    Raises ValueError if the provided location cannot be found.
    </description>
    <parameters>
    <parameter>
    <name>location</name>
    <type>string</type>
    <description>The city and state, e.g. San Francisco, CA</description>
    </parameter>
    </parameters>
    </tool_description>
    

Some tips for writing good function descriptions:

*   Be clear and concise, but provide enough detail for Claude to understand when the function should be used
*   Specify the types of the parameters and return values
*   Mention any relevant exceptions that can be raised
*   Use plaintext descriptions, not code syntax

* * *

[​

](#legacy-tool-use-format)

Legacy tool use format
--------------------------------------------------------

In order for Claude to call a function, it has to output a very specifically formatted XML block. The format looks like this:

XML

Copy

    <function_calls>
    <invoke>
    <tool_name>function_name</tool_name>
    <parameters>
    <param1>value1</param1>
    <param2>value2</param2>
    </parameters>
    </invoke>
    </function_calls>
    

The `<function_calls>` block can contain multiple `<invoke>` blocks if Claude is calling more than one function at the same time. Each `<invoke>` contains the name of the function being called and the parameters being passed in.

> You should pass `</function_calls>` into your API call as a `stop_sequence` to ensure that Claude stops generating text once it has called a function.

After a `<function_calls>` block, and assuming you have the proper stop sequence in place, Claude will stop generating and wait for the function result to be passed back in a `<function_results>` block that looks like this:

XML

Copy

    <function_results>
    <result>
    <tool_name>function_name</tool_name>
    <stdout>
    function result goes here
    </stdout>
    </result>
    </function_results>
    

The function result should be placed inside `<stdout>` tags. If the function raised an exception, that should be returned like:

XML

Copy

    <function_results>
    <error>
    error message goes here
    </error>
    </function_results>
    

The full function result should be passed back to Claude as a message that continues the conversation from before. After receiving the function results, Claude will continue generating to incorporate the results into its response.

* * *

[​

](#example-legacy-tool-use-prompt)

Example legacy tool use prompt
------------------------------------------------------------------------

Here is a full example of a prompt that provides Claude with two functions and a question that requires using them:

| Content |  |
| --- | --- |
| System | In this environment you have access to a set of tools you can use to answer the user’s question.  
  
You may call them like this:  
<function\_calls>  
<invoke>  
<tool\_name>$TOOL\_NAME</tool\_name>  
<parameters>  
<$PARAMETER\_NAME>$PARAMETER\_VALUE</$PARAMETER\_NAME>  
…  
</parameters>  
</invoke>  
</function\_calls>  
  
Here are the tools available:  
<tools>  
<tool\_description>  
<tool\_name>get\_current\_stock\_price  
</tool\_name><description>Gets the current stock price for a company. Returns float: The current stock price.  
Raises ValueError: if the input symbol is invalid/unknown.</description>  
<parameters>  
<parameter>  
<name>symbol</name>  
<type>string</type>  
<description>The stock symbol of the company to get the price for.</description>  
</parameter>  
</parameters>  
</tool\_description>  
  
<tool\_description>  
<tool\_name>get\_ticker\_symbol</tool\_name>  
<description>Gets the stock ticker symbol for a company searched by name. Returns str: The ticker symbol for the company stock. Raises TickerNotFound: if no matching ticker symbol is found.  
</description>  
<parameters>  
<parameter>  
<name>company\_name</name>  
<type>string</type>  
<description>The name of the company.</description>  
</parameter>  
</parameters>  
</tool\_description></tools> |
| User | What is the current stock price of General Motors? |

Here is how Claude would respond:

| Content |  |
| --- | --- |
| Assistant | <scratchpad>  
To answer this question, I will need to:  
  
1\. Get the ticker symbol for General Motors using the get\_ticker\_symbol() function.  
2\. Use the returned ticker symbol to get the current stock price using the get\_current\_stock\_price() function.</scratchpad>  
  
<function\_calls>  
<invoke>  
<tool\_name>get\_ticker\_symbol</tool\_name>  
<parameters>  
<company\_name>General Motors</company\_name>  
</parameters>  
</invoke>  
</function\_calls> |

Claude first calls `get_ticker_symbol` to retrieve the ticker symbol for General Motors. We can recognize that Claude wants to call a function via the `</function calls>` stop sequence. We extract the relevant data from between the relevant XML tags and run the function on Claude’s behalf. Then we pass the results back to Claude in `<function_results>` tags.

| Content |  |
| --- | --- |
| User | <function\_results>  
<result>  
<tool\_name>get\_ticker\_symbol</tool\_name>  
<stdout>  
GM  
</stdout>  
</result>  
</function\_results> |

Now that it knows the ticker symbol, Claude will subsequently decide that it has to call `get_current_stock_price` and get the current price.

| Content |  |
| --- | --- |
| Assistant | <function\_calls>  
<invoke>  
<tool\_name>get\_current\_stock\_price</tool\_name>  
<parameters>  
<symbol>GM</symbol>  
</parameters>  
</invoke>  
</function\_calls> |

We pass back these results as well.

| Content |  |
| --- | --- |
| User | <function\_results>  
<result>  
<tool\_name>get\_current\_stock\_price</tool\_name>  
<stdout>  
38.50  
</stdout>  
</result>  
</function\_results> |

With this whole conversation chain providing Claude all the details it needs, Claude will be able to provide the user an answer as its final output.

| Content |
| --- |
| <answer>  
The current stock price of General Motors is $38.50.  
</answer> |

* * *

[​

](#legacy-tool-use-faq)

Legacy tool use FAQ
--------------------------------------------------

### 

[​

](#how-many-tools-can-i-pass-to-claude-in-a-given-interaction)

How many tools can I pass to Claude in a given interaction?

You can define any number of tools and functions for Claude to use, although we currently recommend that you don’t exceed 3-5 for this legacy tool use structure, depending on the complexity of your use case and the functions in question.

### 

[​

](#does-claude-have-any-built-in-tools-that-it-knows)

Does Claude have any built-in tools that it knows?

No. Any tools that you want Claude to use, you’ll have to define yourself within a tool use prompt. Claude does not have a predetermined list of functions & definitions that work best.

### 

[​

](#when-will-the-new-tool-use-format-come-to-vertex-ai-or-amazon-bedrock)

When will the new tool use format come to Vertex AI or Amazon Bedrock?

In the near future!

[Tool use pricing and tokens](/en/docs/tool-use-pricing-and-tokens)[Overview](/en/docs/prompt-engineering)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [How legacy tool use works](#how-legacy-tool-use-works)
*   [Defining functions](#defining-functions)
*   [Legacy tool use format](#legacy-tool-use-format)
*   [Example legacy tool use prompt](#example-legacy-tool-use-prompt)
*   [Legacy tool use FAQ](#legacy-tool-use-faq)
*   [How many tools can I pass to Claude in a given interaction?](#how-many-tools-can-i-pass-to-claude-in-a-given-interaction)
*   [Does Claude have any built-in tools that it knows?](#does-claude-have-any-built-in-tools-that-it-knows)
*   [When will the new tool use format come to Vertex AI or Amazon Bedrock?](#when-will-the-new-tool-use-format-come-to-vertex-ai-or-amazon-bedrock)
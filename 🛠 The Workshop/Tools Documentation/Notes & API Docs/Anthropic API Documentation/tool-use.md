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

Tool use (function calling)

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

Tool use (function calling)
===========================

Claude is capable of interacting with external client-side tools and functions, allowing you to equip Claude with your own custom tools to perform a wider variety of tasks.

**Tool use is now generally available across the entire Claude 3 model family through the Anthropic Messages API, Amazon Bedrock, and Google Vertex AI.** Learn everything you need to master tool use with Claude via our new comprehensive [tool use course](https://github.com/anthropics/courses/tree/master/ToolUse)! Please continue to share your ideas and suggestions using this [form](https://forms.gle/BFnYc6iCkWoRzFgk7).

Here’s an example of how to provide tools to Claude using the Messages API:

Shell

Python

Copy

    curl https://api.anthropic.com/v1/messages \
      -H "content-type: application/json" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-3-opus-20240229",
        "max_tokens": 1024,
        "tools": [
          {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                }
              },
              "required": ["location"]
            }
          }
        ],
        "messages": [
          {
            "role": "user",
            "content": "What is the weather like in San Francisco?"
          }
        ]
      }'
    

* * *

[​

](#how-tool-use-works)

How tool use works
------------------------------------------------

Using tools with Claude involves the following steps:

1.  **Provide Claude with tools and a user prompt:** (API request)
    *   Define the set of tools you want Claude to have access to, including their names, descriptions, and input schemas.
    *   Provide a user prompt that may require the use of one or more of these tools to answer, such as “What is the weather in San Francisco?“.
2.  **Claude uses a tool:** (API response)
    *   Claude assesses the user prompt and decides whether any of the available tools would help with the user’s query or task. If so, it also decides which tool(s) to use and with what inputs.
    *   Claude constructs a properly formatted tool use request.
    *   The API response will have a `stop_reason` of `tool_use`, indicating that Claude wants to use an external tool.
3.  **Extract tool input, run code, and return results:** (API request)
    *   On the client side, you should extract the tool name and input from Claude’s tool use request.
    *   Run the actual tool code on the client side.
    *   Return the results to Claude by continuing the conversation with a new `user` message containing a `tool_result` content block.
4.  **Claude uses tool result to formulate a response:** (API response)
    *   After receiving the tool results, Claude will use that information to formulate its final response to the original user prompt.

Steps (3) and (4) are optional — for some workflows, Claude using the tool is all the information you need, and you might not need to return tool results back to Claude.

**All tools are user-provided**

It’s important to note that Claude does not have access to any built-in server-side tools. All tools must be explicitly provided by you, the user, in each API request. This gives you full control and flexibility over the tools Claude can use.

* * *

[​

](#specifying-tools)

Specifying tools
--------------------------------------------

Tools are specified in the `tools` top-level parameter of the API request. Each tool definition includes:

*   `name`: The name of the tool. Must match the regex `^[a-zA-Z0-9_-]{1,64}$`.
*   `description`: A detailed plaintext description of what the tool does, when it should be used, and how it behaves.
*   `input_schema`: A [JSON Schema](https://json-schema.org/) object defining the expected parameters for the tool.

Here’s an example simple tool definition:

JSON

Copy

    {
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"],
            "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
          }
        },
        "required": ["location"]
      }
    }
    

This tool, named `get_weather`, expects an input object with a required `location` string and an optional `unit` string that must be either “celsius” or “fahrenheit”.

### 

[​

](#best-practices-for-tool-definitions)

Best practices for tool definitions

To get the best performance out of Claude when using tools, follow these guidelines:

*   **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain every detail about the tool, including:
    *   What the tool does
    *   When it should be used (and when it shouldn’t)
    *   What each parameter means and how it affects the tool’s behavior
    *   Any important caveats or limitations, such as what information the tool does not return if the tool name is unclear  
        The more context you can give Claude about your tools, the better it will be at deciding when and how to use them. Aim for at least 3-4 sentences per tool description, more if the tool is complex.
*   **Prioritize descriptions over examples.** While you can include examples of how to use a tool in its description or in the accompanying prompt, this is less important than having a clear and comprehensive explanation of the tool’s purpose and parameters. Only add examples after you’ve fully fleshed out the description.

Here’s an example of a good tool description:

JSON

Copy

    {
      "name": "get_stock_price",
      "description": "Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
          }
        },
        "required": ["ticker"]
      }
    }
    

In contrast, here’s an example of a poor tool description:

JSON

Copy

    {
      "name": "get_stock_price",
      "description": "Gets the stock price for a ticker.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string"
          }
        },
        "required": ["ticker"]
      }
    }
    

The good description clearly explains what the tool does, when to use it, what data it returns, and what the `ticker` parameter means. The poor description is too brief and leaves Claude with many open questions about the tool’s behavior and usage.

* * *

[​

](#tool-use-and-tool-result-content-blocks)

Tool use and tool result content blocks
------------------------------------------------------------------------------------------

When Claude decides to use one of the tools you’ve provided, it will return a response with a `stop_reason` of `tool_use` and one or more `tool_use` content blocks in the API response that include:

*   `id`: A unique identifier for this particular tool use block. This will be used to match up the tool results later.
*   `name`: The name of the tool being used.
*   `input`: An object containing the input being passed to the tool, conforming to the tool’s `input_schema`.

Here’s an example API response with a `tool_use` content block:

JSON

Copy

    {
      "id": "msg_01Aq9w938a90dw8q",
      "model": "claude-3-opus-20240229",
      "stop_reason": "tool_use",
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "<thinking>I need to use the get_weather, and the user wants SF, which is likely San Francisco, CA.</thinking>"
        },
        {
          "type": "tool_use",
          "id": "toolu_01A09q90qw90lq917835lq9",
          "name": "get_weather",
          "input": {"location": "San Francisco, CA", "unit": "celsius"}
        }
      ]
    }
    

When you receive a tool use response, you should:

1.  Extract the `name`, `id`, and `input` from the `tool_use` block.
2.  Run the actual tool in your codebase corresponding to that tool name, passing in the tool `input`.
3.  \[optional\] Continue the conversation by sending a new message with the `role` of `user`, and a `content` block containing the `tool_result` type and the following information:
    *   `tool_use_id`: The `id` of the tool use request this is a result for.
    *   `content`: The result of the tool, as a string (e.g. `"content": "15 degrees"`) or list of nested content blocks (e.g. `"content": [{"type": "text", "text": "15 degrees"}]`). These content blocks can use the `text` or `image` types.
    *   `is_error` (optional): Set to `true` if the tool execution resulted in an error.

Here’s an example of returning a successful tool result:

JSON

Copy

    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "15 degrees"
        }
      ]
    }
    

Images are supported in `content` as well:

JSON

Copy

    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": [
            {"type": "text", "text": "15 degrees"},
            {
              "type": "image",
              "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": "/9j/4AAQSkZJRg...",
              }
            }
          ]
        }
      ]
    }
    

And here’s an example of returning an error result:

JSON

Copy

    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "ConnectionError: the weather service API is not available (HTTP 500)",
          "is_error": true
        }
      ]
    }
    

After receiving the tool result, Claude will use that information to continue generating a response to the original user prompt.

You can also return a non-erroneous tool result with empty `content`, indicating that the tool ran successfully without any output:

JSON

Copy

    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
        }
      ]
    }
    

**Differences from other APIs**

You may be familiar with other APIs that return tool use as separate from the model’s primary output, or which use a special-purpose `tool` or `function` message `role`.

In contrast, Anthropic’s models and API are built around alternating `user` and `assistant` messages, where each message is an array of rich content blocks: `text`, `image`, `tool_use`, and `tool_result`.

In this format, `user` messages represents client-side and user / human-managed content, and `assistant` messages represent server-side and AI-managed content. As such, there is no special `tool` or `function` message `role`, and you should include `tool_result` blocks in the `content` of your `user` messages.

* * *

[​

](#forcing-tool-use)

Forcing tool use
--------------------------------------------

In some cases, you may want Claude to use a specific tool to answer the user’s question, even if Claude thinks it can provide an answer without using a tool. You can do this by specifying the tool in the `tool_choice` field like so:

Copy

    tool_choice = {"type": "tool", "name": "get_weather"}
    

By explicitly telling Claude to use the `get_weather` tool, you can encourage it to make use the tool you want. This technique can be useful for testing and debugging your tool integrations, or when you know that the tool should always be used, regardless of input.

You can also tell Claude to use any of the tools provided through `{"type": "any"}`. The default `tool_choice` is `{"type": "auto"}`, which allows Claude to decide whether or not to use a tool.

Note that when you have `tool_choice` as `any` or `tool`, we will prefill the assistant message to force a tool to be used. This means that the models will not emit a chain-of-thought `text` content block before `tool_use` content blocks, even if explicitly asked to do so. Our testing has shown that this should not reduce performance. If you would like to keep chain-of-thought (particularly with Opus) while still requesting that the model use a specific tool, you can use `{"type": "auto"}` for `tool_choice` (the default) and add explicit instructions in a `user` message. For example: `What's the weather like in London? Use the get_weather tool in your response.`

* * *

[​

](#json-output)

JSON output
----------------------------------

Tools do not necessarily need to be client-side functions — you can use tools anytime you want the model to return JSON output that follows a provided schema. For example, you might use a `record_summary` tool with a particular schema. See [tool use examples](/en/docs/tool-use-examples) for a full working example.

* * *

[​

](#error-handling)

Error handling
----------------------------------------

There are a few different types of errors that can occur when using tools with Claude:

#### 

[​

](#tool-execution-error)

Tool execution error

If the tool itself throws an error during execution (e.g. a network error when fetching weather data), you can return the error message in the `content` along with `"is_error": true`:

JSON

Copy

    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "ConnectionError: the weather service API is not available (HTTP 500)",
          "is_error": true
        }
      ]
    }
    

Claude will then incorporate this error into its response to the user, e.g. “I’m sorry, I was unable to retrieve the current weather because the weather service API is not available. Please try again later.”

#### 

[​

](#max-tokens-exceeded)

Max tokens exceeded

If Claude’s response is cut off due to hitting the `max_tokens` limit, and the truncated response contains an incomplete tool use block, you’ll need to retry the request with a higher `max_tokens` value to get the full tool use.

#### 

[​

](#invalid-tool-use)

Invalid tool use

If Claude’s attempted use of a tool is invalid (e.g. missing required parameters), it usually means that the there wasn’t enough information for Claude to use the tool correctly. Your best bet during development is to try the request again with more-detailed `description` values in your tool definitions.

However, you can also continue the conversation forward with a `tool_result` that indicates the error, and Claude will try to use the tool again with the missing information filled in:

JSON

Copy

    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Missing required 'location' parameter",
          "is_error": true
        }
      ]
    }
    

* * *

[​

](#chain-of-thought-tool-use)

Chain of thought tool use
--------------------------------------------------------------

When using tools, Claude will often show its “chain of thought”, i.e. the step-by-step reasoning it uses to break down the problem and decide which tools to use. The Claude 3 Opus model will do this if `tool_choice` is set to `auto` (this is the default value, see [Forcing tool use](/en/docs/tool-use#forcing-tool-use)), and Sonnet and Haiku can be prompted into doing it.

For example, given the prompt “What’s the weather like in San Francisco right now, and what time is it there?”, Claude might respond with:

JSON

Copy

    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "<thinking>To answer this question, I will: 1. Use the get_weather tool to get the current weather in San Francisco. 2. Use the get_time tool to get the current time in the America/Los_Angeles timezone, which covers San Francisco, CA.</thinking>"
        },
        {
          "type": "tool_use",
          "id": "toolu_01A09q90qw90lq917835lq9",
          "name": "get_weather",
          "input": {"location": "San Francisco, CA"}
        }
      ]
    }
    

This chain of thought gives insight into Claude’s reasoning process and can help you debug unexpected behavior.

With the Claude 3 Sonnet model, chain of thought is less common by default, but you can prompt Claude to show its reasoning by adding something like “Before answering, explain your reasoning step-by-step in tags.” to the user message or system prompt. For a more in depth example, see [chain of thought tool use example](/en/docs/tool-use-examples#chain-of-thought-tool-use-example).

It’s important to note that while the `<thinking>` tags are a common convention Claude uses to denote its chain of thought, the exact format (such as what this XML tag is named) may change over time. Your code should treat the chain of thought like any other assistant-generated text, and not rely on the presence or specific formatting of the `<thinking>` tags.

* * *

[​

](#tool-use-best-practices-and-limitations)

Tool use best practices and limitations
------------------------------------------------------------------------------------------

When using tools with Claude, keep the following limitations and best practices in mind:

*   **Use Claude 3 Opus for navigating complex tool use, Haiku if dealing with straightforward tools**: Opus is able to handle the most simultaneous tools and is better at catching missing arguments compared to other models. It is more likely to ask for clarification in ambiguous cases where an argument is not explicitly given or when a tool may not be necessary to complete the user request. Haiku defaults to trying to use tools more frequently (even if not relevant to the query) and will infer missing parameters if they are not explicitly given.
*   **Number of tools**: All Claude 3 models can maintain >90% accuracy even when working with hundreds of simple tools, and a smaller number of complex tools. A “complex” tool would be one with a large number of parameters or parameters with complex schemas (e.g. nested objects).
*   **Complex and deeply nested tools**: Just like a human, Claude can work better with simpler interfaces and simpler tools. If Claude is struggling to correctly use your tool, try to flatten the input schema away from deeply nested json objects, and reduce the number of inputs.
*   **Sequential tool use**: Claude generally prefers to use one tool at a time, then use the output of that tool to inform its next action. While you can prompt Claude to use multiple tools in parallel by carefully designing your prompt and tools, this may lead to Claude filling in dummy values for parameters that depend on the results of earlier tool use. For best results, design your workflow and tools to elicit and work with a series of sequential tool use from Claude.
*   **Retries**: If Claude’s tool use request is invalid or missing required parameters, you can return an error response and Claude will usually retry the request with the missing information filled in. However, after 2-3 failed attempts, Claude may give up and return an apology to the user instead of retrying further.
*   **Debugging**: When debugging unexpected tool use behavior, pay attention to Claude’s chain of thought output (if any) to understand why it’s making the choices it’s making. You can also try prompting Claude to use a specific tool to see if that leads to the expected behavior. If Claude is misusing a tool, double check that your tool descriptions and schemas are clear and unambiguous.
*   **<search\_quality\_reflection> tags**: At times when using search tools, the model may return <search\_quality\_reflection> XML tags and a search quality score in its response. To stop the model from doing this, add the sentence “Do not reflect on the quality of the returned search results in your response.” to the end of your prompt.

By keeping these limitations and guidelines in mind, you can design effective tools and agentic orchestrations that significantly extend Claude’s capabilities to tackle a wide variety of tasks.

* * *

[​

](#beta-version-history-legacy)

Beta version history (legacy)
--------------------------------------------------------------------

Tool use is no longer in beta and is generally available as of May 30, 2024.

*   `tools-2024-05-16`
    *   System prompt change for Opus to better handle scenarios where multiple tool uses may be needed in a single turn
*   `tools-2024-04-04`: Initial beta release for tool use

* * *

[​

](#next-steps)

Next steps
--------------------------------

Tool use is a powerful technique for extending Claude’s capabilities by connecting it to external data sources and functionality. With a well-designed set of tools, you can enable Claude to tackle a huge variety of tasks that would be impossible with its base knowledge alone.

Some potential next steps to explore:

*   **Browse our tool use cookbooks**: explore our repository of ready-to-implement tool use code examples, such as:
    *   [Using a calculator tool with Claude](https://github.com/anthropics/anthropic-cookbook/blob/main/tool%5Fuse/calculator%5Ftool.ipynb)
    *   [Creating a customer service agent with client-side tools](https://github.com/anthropics/anthropic-cookbook/blob/main/tool%5Fuse/customer%5Fservice%5Fagent.ipynb)
    *   [Extracting structured JSON using Claude and tool use](https://github.com/anthropics/anthropic-cookbook/blob/main/tool%5Fuse/extracting%5Fstructured%5Fjson.ipynb)
*   **Improve tool use quality and reliability**: Iterate and improve on your tool descriptions and prompts to elicit more reliable and accurate tool use from Claude
*   **Expand Claude’s capabilities**:
    *   Experiment with different tools and schemas to see how Claude handles different types of input and output formats.
    *   Chain multiple tools together to break down complex tasks into a series of simpler steps.
    *   Build agentic orchestrations where Claude can complete a variety of tasks end to end as if it were an assistant.
    *   Explore complex tool use architectures such as giving Claude tools to do RAG search, or to call on smaller model subagents, such as Haiku, to carry out tasks on its behalf

As you build with tool use, we’d love to hear your feedback and see what you create! Join our developer [Discord](https://anthropic.com/discord) to share your projects and discuss tips and techniques with other developers.

We’re excited to see how you use tool use to push the boundaries of what’s possible with Claude. Happy building!

[Google Sheets add-on](/en/docs/google-sheets-add-on)[Tool use examples](/en/docs/tool-use-examples)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [How tool use works](#how-tool-use-works)
*   [Specifying tools](#specifying-tools)
*   [Best practices for tool definitions](#best-practices-for-tool-definitions)
*   [Tool use and tool result content blocks](#tool-use-and-tool-result-content-blocks)
*   [Forcing tool use](#forcing-tool-use)
*   [JSON output](#json-output)
*   [Error handling](#error-handling)
*   [Tool execution error](#tool-execution-error)
*   [Max tokens exceeded](#max-tokens-exceeded)
*   [Invalid tool use](#invalid-tool-use)
*   [Chain of thought tool use](#chain-of-thought-tool-use)
*   [Tool use best practices and limitations](#tool-use-best-practices-and-limitations)
*   [Beta version history (legacy)](#beta-version-history-legacy)
*   [Next steps](#next-steps)
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

Models overview

Models overview

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
        
        Overview
        
        
        
        ](/en/docs/models-overview)
    *   [
        
        Legacy model guide
        
        
        
        ](/en/docs/legacy-model-guide)
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

Models overview

Models overview
===============

Claude is a family of state-of-the-art large language models developed by Anthropic. Our models are designed to provide you with the best possible experience when interacting with AI, offering a range of capabilities and performance levels to suit your needs and make it easy to deploy high performing, safe, and steerable models. In this guide, we’ll introduce you to our latest and greatest models, the Claude 3 family, as well as our legacy models, which are still available for those who need them.

> Eager to chat with Claude immediately? Visit our web [Console](https://console.anthropic.com/) to get an API key and start experimenting with Claude right away!
> 
> See our [quickstart guide](/en/docs/quickstart-guide) for step-by-step guidance on how to send your first API request using Claude.

* * *

[​

](#claude-3-a-new-generation-of-ai)

Claude 3: A new generation of AI
---------------------------------------------------------------------------

| Model | Latest 1P API model name | Latest AWS Bedrock model name | GCP Vertex AI model name |
| --- | --- | --- | --- |
| Claude 3 Opus | claude-3-opus-20240229 | anthropic.claude-3-opus-20240229-v1:0 | claude-3-opus@20240229 |
| Claude 3 Sonnet | claude-3-sonnet-20240229 | anthropic.claude-3-sonnet-20240229-v1:0 | claude-3-sonnet@20240229 |
| Claude 3 Haiku | claude-3-haiku-20240307 | anthropic.claude-3-haiku-20240307-v1:0 | claude-3-haiku@20240307 |

The Claude 3 family of models represents the cutting edge of AI technology, offering unparalleled performance, versatility, and ease of use. These models excel at open-ended conversation, collaboration on ideas, coding tasks, and working with text – whether searching, writing, editing, translating, outlining, or summarizing. They also offer advanced vision capabilities, allowing you to process and analyze visual input such as charts, graphs, and photos.

*   **Claude 3 Opus**: Our most powerful model, delivering state-of-the-art performance on highly complex tasks and demonstrating fluency and human-like understanding
*   **Claude 3 Sonnet**: Our most balanced model between intelligence and speed, a great choice for enterprise workloads and scaled AI deployments
*   **Claude 3 Haiku**: Our fastest and most compact model, designed for near-instant responsiveness and seamless AI experiences that mimic human interactions

### 

[​

](#key-features)

Key features

*   **Multilingual capabilities**: Claude 3 models offer improved fluency in non-English languages such as Spanish and Japanese, enabling use cases like translation services and global content creation.
*   **Vision and image processing**: All Claude 3 models can process and analyze visual input, extracting insights from documents, processing web UI, generating image catalog metadata, and more. See our [vision](/en/docs/vision) page to learn more.
*   **Steerability and ease of use**: Claude 3 models are easier to steer and better at following directions. This gives you more control over model behavior and and more predictable, higher-quality outputs.
*   **Model upgrades**: The Claude 3 family will periodically receive updates to enhance performance, expand capabilities, and address any identified issues. However, each update will be pinned to a new model version, guaranteeing that your workflows on one model version will not break with the release of a new version. When a new model version is released, we will provide a transition period to allow developers to update their applications.

* * *

[​

](#legacy-models)

Legacy models
--------------------------------------

While the Claude 3 family represents the future of our AI technology, we understand that some users may need time to transition from our legacy models:

*   **Claude 2.0**: The predecessor to Claude 3, offering strong performance across a variety of tasks
*   **Claude 2.1**: An updated version of Claude 2 with improved accuracy and consistency
*   **Claude Instant 1.2**: A fast and efficient model that’s the predecessor of Claude Haiku

For more information on our legacy models and how to use them, please refer to our [legacy model guide](/en/docs/legacy-model-guide).

* * *

[​

](#model-recommendations)

Model recommendations
------------------------------------------------------

We recommend that you use the Claude 3 family of models for any and all use cases. Claude 3 models are more capable and intelligent across the board than previous generation Claude models. There is a Claude 3 model for every tradeoff point between cost, speed, and performance. For every legacy model, there is a Claude 3 model that bests it on speed and performance. For details on model comparison metrics, see [model comparison](/en/docs/models-overview#model-comparison). Which Claude 3 model in particular to use depends on the complexity of your use case and your requirements around latency, cost, and performance.

Haiku is the fastest and most cost-effective model for its intelligence category. It can read an information and data dense research paper on arXiv (~10k tokens) with charts and graphs in less than three seconds. Following launch, we expect to reduce latency even further.

For the vast majority of workloads, Sonnet is 2x faster than Claude 2 and Claude 2.1 with higher levels of intelligence. Opus delivers similar speeds to Claude 2 and 2.1, with much higher levels of intelligence.

See the [model comparison](/en/docs/models-overview#model-comparison) section below for a comprehensive overview of our models, including comparative benchmarks and metrics to guide your decision-making.

* * *

[​

](#model-comparison)

Model comparison
--------------------------------------------

To help you choose the right model for your needs, we’ve compiled a table comparing the key features and capabilities of each model in the Claude family:

|  | Claude 3 Opus | Claude 3 Sonnet | Claude 3 Haiku | Claude 2.1 | Claude 2 | Claude Instant 1.2 |
| --- | --- | --- | --- | --- | --- | --- |
| Description | Most powerful model for highly complex tasks | Ideal balance of intelligence and speed for enterprise workloads | Fastest and most compact model fornear-instant responsiveness | Updated version of Claude 2 with improved accuracy | Predecessor to Claude 3, offering strong all-round performance | Our cheapest small and fast model, a predecessor of Claude Haiku. |
| Strengths | Top-level performance, intelligence, fluency, and understanding | Maximum utility at a lower price, dependable, balanced for scaled deployments | Quick and accurate targeted performance | Legacy model - performs less well than Claude 3 models | Legacy model - performs less well than Claude 3 models | Legacy model - performs less well than Claude 3 models |
| Multilingual | Yes | Yes | Yes | Yes, with less coverage, understanding, and skill than Claude 3 | Yes, with less coverage, understanding, and skill than Claude 3 | Yes, with less coverage, understanding, and skill than Claude 3 |
| Vision | Yes | Yes | Yes | No | No | No |
| Latest API model name | claude-3-opus-20240229 | claude-3-sonnet-20240229 | claude-3-haiku-20240307 | claude-2.1 | claude-2.0 | claude-instant-1.2 |
| API format | MessagesAPI | Messages API | MessagesAPI | Messages & Text Completions API | Messages & Text Completions API | Messages & Text Completions API |
| Comparative latency | Moderately fast | Fast | Fastest | Slower than Claude 3 model of similar intelligence | Slower than Claude 3 model of similar intelligence | Slower than Claude 3 model of similar intelligence |
| Context window | 200K\* | 200K\* | 200K\* | 200K\* | 100K\*\* | 100K\*\* |
| Max output | 4096 tokens | 4096 tokens | 4096 tokens | 4096 tokens | 4096 tokens | 4096 tokens |
| Cost (Input / Output per MTok^) | $15.00 / $75.00 | $3.00 / $15.00 | $0.25 / $1.25 | $8.00 / $24.00 | $8.00 / $24.00 | $0.80 / $2.40 |
| Training data cut-off | Aug 2023 | Aug 2023 | Aug 2023 | Early 2023 | Early 2023 | Early 2023 |

*   _\*~150K words, ~680K unicode characters_
*   _\*\*~75K words, ~350K unicode characters_
*   _^Millions of tokens_

Here is a visualization comparing cost vs. speed across Claude 3 models, showcasing the range in tradeoffs between cost and intelligence:

![](https://mintlify.s3-us-west-1.amazonaws.com/anthropic/images/4b0f1c4-Claude_3_Intelligence_vs._Cost.png)

* * *

[​

](#benchmark-performance)

Benchmark performance
------------------------------------------------------

We have evaluated our models on a wide range of industry-standard benchmarks to assess performance across various tasks and capabilities. These benchmarks cover areas such as reasoning, coding, multilingual understanding, long-context handling, honesty, and image processing. You can read in greater detail about our benchmark evals in the [Claude 3 model card](https://anthropic.com/claude-3-model-card/).

* * *

[​

](#prompt-and-output-differences)

Prompt & output differences
--------------------------------------------------------------------

The Claude 3 family of models introduces several key differences in prompting and output generation compared to our legacy models:

*   **More expressive and engaging responses**: Claude 3 tends to generate more expressive and engaging responses, resulting in longer responses on average than previous older models, given the same prompt. This feature allows for more natural and dynamic conversations, making Claude 3 models ideal for applications that require rich, human-like interactions.
    *   If you prefer more concise responses, you can mitigate this by adjusting your prompts to guide the model toward the desired output length (like simply telling Claude to be more concise). Please refer to our [prompt engineering](/en/docs/prompt-engineering) and [reducing latency](/en/docs/reducing-latency) guides for more details.
*   **Improvements in output quality and style between generations**: When migrating from previous model generations to the Claude 3 family, you may notice larger improvements in performance compared to migrations within the same generation of models (such as between Claude 2.0 and Claude 2.1). Depending on the requirements of your use case, this may necessitate more extensive evaluation and testing of post-migration results to ensure they align with your expectations and requirements.

**Model steerability**

Claude 3 models are generally easier to prompt and steer compared to our legacy models. Users should find that they can achieve the desired results with shorter and more concise prompts, potentially reducing costs and improving latency.

As you upgrade to the Claude 3 family, we recommend re-evaluating your existing prompts and making adjustments as needed to take full advantage of the improved steerability, power, and intelligence offered by these frontier models. We recommend starting with Opus, our most powerful model, to establish maximum output quality before looking at using the smaller models in the Claude 3 family.

* * *

[​

](#get-started-with-claude)

Get started with Claude
----------------------------------------------------------

If you’re ready to start exploring what Claude can do for you, let’s dive in! Whether you’re a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, we’ve got you covered.

Check out our [quickstart guide](/en/docs/quickstart-guide) for step-by-step instructions on how to get up and running with Claude. You’ll learn how to create an account, obtain API keys, and start interacting with our models in no time. You can also head over to [claude.ai](https://claude.ai/) or our web [Console](https://console.anthropic.com/) to start experimenting with Claude right away!

If you have any questions or need assistance, don’t hesitate to reach out to our [support team](https://support.anthropic.com/) or consult the [Discord community](https://www.anthropic.com/discord). We’re always here to help you get the most out of Claude.

[Upgrading to the Messages API](/en/docs/upgrading-to-the-messages-api)[Legacy model guide](/en/docs/legacy-model-guide)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [Claude 3: A new generation of AI](#claude-3-a-new-generation-of-ai)
*   [Key features](#key-features)
*   [Legacy models](#legacy-models)
*   [Model recommendations](#model-recommendations)
*   [Model comparison](#model-comparison)
*   [Benchmark performance](#benchmark-performance)
*   [Prompt & output differences](#prompt-and-output-differences)
*   [Get started with Claude](#get-started-with-claude)
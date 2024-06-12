Documentation
-------------

*   [Getting Started with pplx-api](/docs/getting-started)
*   [Rate Limits](/docs/rate-limits)
*   [Supported Models](/docs/model-cards)
*   [Feature Roadmap](/docs/feature-roadmap)
*   [PerplexityBot](/docs/perplexitybot)
*   [Pricing](/docs/pricing)

Powered by [](https://readme.com?ref_src=hub&project=pplx)

Supported Models
================

[Suggest Edits](/edit/model-cards)

Perplexity Models

[](#perplexity-models)
-------------------------------------------

| Model | Parameter Count | Context Length | Model Type |
| --- | --- | --- | --- |
| `llama-3-sonar-small-32k-chat` | 8B | 32768 | Chat Completion |
| `llama-3-sonar-small-32k-online` | 8B | 28000 | Chat Completion |
| `llama-3-sonar-large-32k-chat` | 70B | 32768 | Chat Completion |
| `llama-3-sonar-large-32k-online` | 70B | 28000 | Chat Completion |

Open-Source Models

[](#open-source-models)
---------------------------------------------

Where possible, we try to match the Hugging Face implementation.

| Model | Parameter Count | Context Length | Model Type |
| --- | --- | --- | --- |
| `llama-3-8b-instruct` | 8B | 8192 | Chat Completion |
| `llama-3-70b-instruct` | 70B | 8192 | Chat Completion |
| `mixtral-8x7b-instruct` | 8x7B | 16384 | Chat Completion |

Special Tokens

[](#special-tokens)
=====================================

We do not raise any exceptions if your chat inputs contain messages with special tokens. If avoiding prompt injections is a concern for your use case, it is recommended that you check for special tokens prior to calling the API. For more details, read [Meta's recommendations for Llama](https://github.com/facebookresearch/llama/blob/008385a/UPDATES.md#token-sanitization-update).

Online LLMs

[](#online-llms)
===============================

Note that the search subsystem of the Online LLMs _do not_ attend to the system prompt. You can use the system prompt to provide instructions related to style, tone, and language of the response.

Access to citations and images via API is in closed beta. To request access to citations, fill out [this form](https://perplexity.typeform.com/to/j50rnNiB) and send an email describing your use case to [api@perplexity.ai](mailto:api@perplexity.ai).

Updated 15 days ago

* * *

[

Rate Limits

](/docs/rate-limits)[

Feature Roadmap

](/docs/feature-roadmap)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   *   [Perplexity Models](#perplexity-models)
        *   [Open-Source Models](#open-source-models)
    *   [Special Tokens](#special-tokens)
    *   [Online LLMs](#online-llms)
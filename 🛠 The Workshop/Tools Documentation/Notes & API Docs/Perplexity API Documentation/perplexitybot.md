Documentation
-------------

*   [Getting Started with pplx-api](/docs/getting-started)
*   [Rate Limits](/docs/rate-limits)
*   [Supported Models](/docs/model-cards)
*   [Feature Roadmap](/docs/feature-roadmap)
*   [PerplexityBot](/docs/perplexitybot)
*   [Pricing](/docs/pricing)

Powered by [](https://readme.com?ref_src=hub&project=pplx)

PerplexityBot
=============

[Suggest Edits](/edit/perplexitybot)

We strive to improve our service every day. To provide the best search experience, we need to collect data. We use web crawlers to gather information from the internet and index it for our search engine.

You can identify our web crawler by its user agent

JSX

`User agent token: PerplexityBot Full user agent: User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`

Customizing access

[](#customizing-access)
=============================================

Disallow PerplexityBot

[](#disallow-perplexitybot)
-----------------------------------------------------

To prevent PerplexityBot from accessing your site data, add a record to your site's robots.txt

JSX

`User-Agent: PerplexityBot Disallow: /`

Custom access rules

[](#custom-access-rules)
-----------------------------------------------

You can also customize access, disallowing data retrieval only from specific paths.

JSX

`User-Agent: PerplexityBot Allow: /public/ Disallow: /private/`

IP address ranges

[](#ip-address-ranges)
===========================================

Our IP pool may change over time. You can find the latest information on the [Perplexity Inc. website](https://www.perplexity.ai/perplexitybot.json).

Updated 8 months ago

* * *

[

Feature Roadmap

](/docs/feature-roadmap)[

Pricing

](/docs/pricing)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Customizing access](#customizing-access)
        *   [Disallow PerplexityBot](#disallow-perplexitybot)
        *   [Custom access rules](#custom-access-rules)
    *   [IP address ranges](#ip-address-ranges)
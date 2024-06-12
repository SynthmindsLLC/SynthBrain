Documentation
-------------

*   [Getting Started with pplx-api](/docs/getting-started)
*   [Rate Limits](/docs/rate-limits)
*   [Supported Models](/docs/model-cards)
*   [Feature Roadmap](/docs/feature-roadmap)
*   [PerplexityBot](/docs/perplexitybot)
*   [Pricing](/docs/pricing)

Powered by [](https://readme.com?ref_src=hub&project=pplx)

Getting Started with pplx-api
=============================

[Suggest Edits](/edit/getting-started)

You can access pplx-api using HTTPS requests. Authenticating involves the following steps:

Start by visiting the [Perplexity API Settings page](https://www.perplexity.ai/pplx-api).

![](https://files.readme.io/24cc167-Screenshot_2023-11-28_at_6.19.34_PM.png)

Register your credit card to get started. This step will not charge your credit card. Rather, it stores payment information for later API usage.

![](https://files.readme.io/50d9caa-Screenshot_2023-11-28_at_6.23.21_PM.png)

After providing your payment information, you are ready to purchase credits. API keys can only be generated when your balance is nonzero. Note that pro users receive $5 of free credits on the first day of every month. If you recently purchased Pro, please wait up to 10 minutes for your free $5 credit to be visible in your available balance.

![](https://files.readme.io/b01c13c-Screenshot_2023-11-28_at_9.14.23_AM.png)

Generate an API key. The API key is a long-lived access token that can be used until it is manually refreshed or deleted.

![](https://files.readme.io/c83bb1f-Screenshot_2023-11-28_at_6.41.40_PM.png)

Send the API key as a bearer token in the Authorization header with each pplx-api request.

When you run out of credits, your API keys will be blocked until you add to your credit balance. You can avoid this by configuring "Automatic Top Up", which refreshes your balance whenever you drop below $2.

Our supported models are listed on the ["Supported Models"](/docs/model-cards) page. The API is conveniently OpenAI client-compatible for easy integration with existing applications.

Python

`from openai import OpenAI  YOUR_API_KEY = "INSERT API KEY HERE"  messages = [     {         "role": "system",         "content": (             "You are an artificial intelligence assistant and you need to "             "engage in a helpful, detailed, polite conversation with a user."         ),     },     {         "role": "user",         "content": (             "How many stars are in the universe?"         ),     }, ]  client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")  # chat completion without streaming response = client.chat.completions.create(     model="llama-3-sonar-large-32k-online",     messages=messages, ) print(response)  # chat completion with streaming response_stream = client.chat.completions.create(     model="llama-3-sonar-large-32k-online",     messages=messages,     stream=True, ) for response in response_stream:     print(response)`

Updated about 1 month ago

* * *

What’s Next

*   [Rate Limits](/docs/rate-limits)

Did this page help you?

Yes

No
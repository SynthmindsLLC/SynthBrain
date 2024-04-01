# Microsoft’s new safety system can catch hallucinations in its customers’ AI apps - The Verge

![rw-book-cover](https://cdn.vox-cdn.com/thumbor/RTKHHTGYFSSreNvw0NRAR0cEx50=/0x0:2040x1360/1310x873/cdn.vox-cdn.com/uploads/chorus_image/image/73239918/STK095_Microsoft_04.0.jpg)

## Metadata
- Author: [[Emilia David]]
- Date: 2024-03-28
- Full Title: Microsoft’s new safety system can catch hallucinations in its customers’ AI apps - The Verge
- Category: #articles
- Summary: Microsoft has introduced new safety features for its Azure AI platform to detect and prevent malicious attacks and hallucinations in AI models. These tools, such as Prompt Shields and Groundedness Detection, help users monitor and block potential vulnerabilities in real time. The goal is to enhance the security and reliability of AI applications on Azure.
- URL: https://www.theverge.com/2024/3/28/24114664/microsoft-safety-ai-prompt-injections-hallucinations-azure

## Highlights
- Sarah Bird, Microsoft’s chief product officer of responsible AI, tells *The Verge* in an interview that her team has designed several new safety features that will be easy to use for Azure customers who aren’t hiring groups of red teamers to test the AI services they built. ([View Highlight](https://read.readwise.io/read/01htck6z3f5nbqh7x2fddg9vcc))
- Microsoft [says these LLM-powered tools can detect potential vulnerabilities](https://azure.microsoft.com/en-us/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/), monitor for hallucinations “that are plausible yet unsupported,” and block malicious prompts in real time for Azure AI customers working with any model hosted on the platform. ([View Highlight](https://read.readwise.io/read/01htck78y5zx2pr95a2rec5fd1))
- Three features: [Prompt Shields](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-announces-prompt-shields-for-jailbreak-and-indirect/ba-p/4099140), which blocks prompt injections or malicious prompts from external documents that instruct models to go against their training; [Groundedness Detection](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/detect-and-mitigate-ungrounded-model-outputs/ba-p/4099261), which finds and blocks hallucinations; and [safety evaluations](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/introducing-ai-assisted-safety-evaluations-in-azure-ai-studio/ba-p/4098595), which assess model vulnerabilities, are now available in preview on Azure AI. ([View Highlight](https://read.readwise.io/read/01htck8cv6m6mrvspzjnxenybt))
- Whether the user is typing in a prompt or if the model is processing third-party data, the monitoring system will evaluate it to see if it triggers any banned words or has hidden prompts before deciding to send it to the model to answer. ([View Highlight](https://read.readwise.io/read/01htck8x21aqbfbjwfvc0zzm8y))
- After, the system then looks at the response by the model and checks if the model hallucinated information not in the document or the prompt. ([View Highlight](https://read.readwise.io/read/01htck96yve9h2vdkf3n7zdx84))
- Microsoft and other companies could be deciding what is or isn’t appropriate for AI models, so her team added a way for Azure customers to toggle the filtering of hate speech or violence that the model sees and blocks. ([View Highlight](https://read.readwise.io/read/01htck9x75pynj2arypyxd94yh))
- Azure users [can also get a report of users](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/introducing-risks-amp-safety-monitoring-feature-in-azure-openai/ba-p/4099218) who attempt to trigger unsafe outputs. Bird says this allows system administrators to figure out which users are its own team of red teamers and which could be people with more malicious intent. ([View Highlight](https://read.readwise.io/read/01htcka5nhnmbqj3dastm04gws))

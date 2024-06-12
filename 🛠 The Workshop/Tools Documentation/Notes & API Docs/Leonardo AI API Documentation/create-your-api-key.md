🏁 Quick start
--------------

*   [Getting Started](/docs/getting-started)
*   [Create your API key](/docs/create-your-api-key)
*   [Generate your First Images](/docs/generate-your-first-images)

📝 GUIDes
---------

*   [Image Generation](/docs/generate-images-using-photoreal)
    *   [Generate Images Using PhotoReal](/docs/generate-images-using-photoreal)
    *   [Generate Images Using Alchemy](/docs/generate-images-using-alchemy)
    *   [Generate Images Using Image to Image Guidance](/docs/generate-images-using-image-to-image-guidance)
    *   [Generate Images Using Image Prompts](/docs/generate-images-using-image-prompts)
    *   [Generate Images with Realtime Canvas](/docs/generate-images-with-realtime-canvas)
    *   [Generate Images Using Fantasy Avatar \[Beta\]](/docs/generate-images-using-fantasy-avatar)
    *   [Generate Images Using Transparency](/docs/generate-images-using-transparency)
*   [Video Generation (Motion)](/docs/generate-motion-using-generated-images)
    *   [Generate Motion Using Generated Images](/docs/generate-motion-using-generated-images)
    *   [Generate Motion Using Uploaded Images](/docs/generate-motion-using-uploaded-images)
    *   [Generate Motion Using Variation Images](/docs/generate-motion-using-variation-images)
*   [Variation Generation](/docs/image-variations-with-universal-upscaler)
    *   [Upscale with Universal Upscaler](/docs/image-variations-with-universal-upscaler)
*   [Texture Generation](/docs/generate-textures-on-3d-model)
    *   [Generate Textures on 3D model](/docs/generate-textures-on-3d-model)
*   [Prompt Generation](/docs/generate-enhanced-prompts)
    *   [Generate Enhanced Prompts](/docs/generate-enhanced-prompts)
*   [Best Practices](/docs/guide-to-the-webhook-callback-feature)
    *   [Guide to the Webhook Callback Feature](/docs/guide-to-the-webhook-callback-feature)
    *   [Guide to Handling Not Safe for Work Image Generation (NSFW)](/docs/guide-to-handling-not-safe-for-work-image-generation-nsfw)
*   [Usage and Cost](/docs/plan-with-the-pricing-calculator)
    *   [Plan with the Pricing Calculator](/docs/plan-with-the-pricing-calculator)
    *   [Manage Usage with Auto Top-up](/docs/manage-usage-with-auto-top-up)

❓Technical Support & questions
------------------------------

*   [API FAQ](/docs/api-faq)
*   [API Error Messages](/docs/api-error-messages)
*   [Special Topics](/docs/elements-and-model-compatibility)
    *   [Elements and Model Compatibility](/docs/elements-and-model-compatibility)
    *   [How to upload an image using a presigned URL](/docs/how-to-upload-an-image-using-a-presigned-url)
*   [Need More Support?](/docs/need-more-support)

Powered by [](https://readme.com?ref_src=hub&project=leonardoai)

Create your API key
===================

You can provision an API key from the Leonardo.Ai web application.

Subscribe to an API Plan

[](#subscribe-to-an-api-plan)
=========================================================

Navigate to the API Access menu in the Leonardo web app. Click **Subscribe to API Plan** to launch subscription options.

![Navigate to the API Access Menu](https://files.readme.io/2cd4f43-Screenshot_2023-10-09_at_16.12.47.png)

Navigate to the API Access Menu

Choose from the available plans: API Basic, API Standard, API Pro or contact us directly to discuss setting up a Custom Plan. Purchasing an API plan gives you programmatic access to Leonardo.Ai’s platform.

> 🚧
> 
> Note
> 
> 
> ----------
> 
> An API plan is different from a web-app plan (eg. Free, Apprentice, Artisan, and Maestro).
> 
> An API plan gives you access to Leonardo’s Production API, whereas the web app plan only gives you access to functionalities in the Leonardo.Ai web app, mobile app, and the User API.

Provision an API key

[](#provision-an-api-key)
=================================================

After subscribing to an API plan, you’ll see the API Access Page. Here, you can create your first API key by clicking the **Create New Key** button.

![Click on Create New Key](https://files.readme.io/4d7a378-Screenshot_2023-10-09_at_16.17.19.png)

Click on Create New Key

To create your API key, input your API key name and optional webhook callback details. If you set up a webhook callback, Leonardo will send you a message containing your generations. For more information on setting up a webhook callback, see [Guide to the Webhook Callback Feature](/docs/guide-to-the-webhook-callback-feature).

![Type in your key name and webhook callback details](https://files.readme.io/ef3976a-Screenshot_2023-11-15_at_07.37.24.png)

Type in your key name and webhook callback details

> 📘
> 
> API Best Practice
> 
> 
> -----------------------
> 
> *   Limit the number of API keys you generate for easy management.
> *   Have a system for naming API keys based on factors like application names, environment or teams. For example, mywebapp-dev, mywebapp-prod, myiosapp-dev etc.
> *   Leverage the webhook callback feature to receive a message containing the links to your image instead of polling for generations.

Test the API key

[](#test-the-api-key)
=========================================

Test your API key on the Get User Information page in the [API documentation](/reference/getuserself). Here, you can input your key under _Bearer_ and click **Try It** to test your key.

![Test your API key in the Get User Information API](https://files.readme.io/b2c9a06-Screenshot_2023-10-09_at_16.50.26.png)

Test your API key in the Get User Information API

Updated 6 months ago

* * *

[

Getting Started

](/docs/getting-started)[

Generate your First Images

](/docs/generate-your-first-images)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Subscribe to an API Plan](#subscribe-to-an-api-plan)
    *   [Provision an API key](#provision-an-api-key)
    *   [Test the API key](#test-the-api-key)
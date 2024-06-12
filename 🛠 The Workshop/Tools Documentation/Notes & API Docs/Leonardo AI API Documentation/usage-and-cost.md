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

Plan with the Pricing Calculator
================================

Pricing Calculator on the Web App

[](#pricing-calculator-on-the-web-app)
===========================================================================

The [Pricing Calculator](https://app.leonardo.ai/api-access) helps you plan out how many API credits different generations use. You can use it to test out various configurations and see how many API credits might be consumed.

In the example below, we use the following settings:

*   Number of images = 4
*   Image Dimensions = 512 x 512
*   Step Count = 10

This results in a cost of 7 API credits.

![Pricing Calculator for Production API](https://files.readme.io/97ab6c6-Screenshot_2024-04-02_at_08.44.45.png)

Pricing Calculator for Production API

> 📘
> 
> Tip
> 
> 
> ---------
> 
> The cost of generating 1 image versus multiple images may be the same. You can leverage this in your design. For example, if you notice that your end users are regenerating multiple times, you may consider increasing the **Number of Images** parameter and offer them a selection of images upfront.

Pricing Calculator on the API

[](#pricing-calculator-on-the-api)
===================================================================

The Pricing Calculator is also available on the API: [Calculating API Cost](/reference/pricingcalculator).

The use cases include:

*   Programmatically getting API credit cost for a list of settings
*   Checking the API credit cost for settings that don't appear yet on the web app

Although the Pricing Calculator API can be used interactively within your web app, this endpoint will contribute to your total number of requests. For more information on default rate limits, see [API Rate Limits](/reference/limits). To avoid rate limiting, the best practice is to keep a copy of the API credit cost in your own database if you'd like use this information within your app.

Estimated Pricing Table

[](#estimated-pricing-table)
=======================================================

> 🚧
> 
> Caution
> 
> 
> -------------
> 
> Refer to the table below for an estimate of credit costs. To confirm the cost, do a test request and check the Pricing Calculator and apiCreditCost parameter in the response.

SDXL Finetuned Model, PhotoReal v1, and SD Finetuned Model

[](#sdxl-finetuned-model-photoreal-v1-and-sd-finetuned-model)
---------------------------------------------------------------------------------------------------------------------------

| Request | 4 images, 512 x 512 | 4 images, 1024 x 1024 |
| --- | --- | --- |
| Lighting SDXL Finetune Model + Alchemy v2 (Leonardo Lightning XL) | 15 credits | 40 credits |
| SDXL Finetune Model + Alchemy v2 (Leonardo Diffusion XL) | 24 credits | 66 credits |
| PhotoReal v1 + Alchemy v1 | 23 credits | 63 credits |
| SD Finetune Model + Alchemy v1 (DreamShaper v7) | 16 credits | 44 credits |

SD 1.5 and SD 2.1

[](#sd-15-and-sd-21)
-----------------------------------------

| Request | 4 images, 512 x 512 | 4 images, 1024 x 1024 |
| --- | --- | --- |
| Stable Diffusion 1.5 | 7 credits | 12 credits |
| Stable Diffusion 2.1 | 7 credits | 12 credits |
| Stable Diffusion 1.5 + PM v2 | 7 credits | 12 credits |
| Stable Diffusion 2.1 + PM v2 | 7 credits | 12 credits |
| Stable Diffusion 1.5 + PM v3 + Alchemy | 24 credits | 63 credits |
| Stable Diffusion 2.1 + PM v3 + Alchemy | 24 credits | 63 credits |

Fixed Costs

[](#fixed-costs)
-------------------------------

| Request | API Credit Cost |
| --- | --- |
| Upscales | 15 credits |
| Unzooms | 15 credits |
| Remove Background | 5 credits |
| Motion | 45 credits |
| 3D Model Texturing | 150 credits |
| 3D Texturing Preview | 30 credits |
| Model Training (512px) | 750 credits |
| Model Training (768px) | 1500 credits |

Realtime Canvas (LCM Generations)

[](#realtime-canvas-lcm-generations)
-------------------------------------------------------------------------

Credits will increase based on image dimensions

| Request | 512x512 | 1024x1024 |
| --- | --- | --- |
| LCM generation | 1 credit | 4 credits |
| Instant Refine | 1 credit | 4 credits |
| Inpainting | 1 credit | 4 credits |
| Alchemy Upscale | 8 credits | 8 credits |

Monitoring and Tracking API Credits

[](#monitoring-and-tracking-api-credits)
===============================================================================

The [Create a Generation of Images API endpoint](/reference/creategeneration) returns `apiCreditCost` in the response. You can use this to monitor and track your API credits usage.

Sample Response:

`{   "sdGenerationJob": {     "generationId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",     "apiCreditCost": 11   } }`

On the Leonardo web app, you can also observe the changes in your API credits on the API Access Page.

![](https://files.readme.io/10420f2-Screenshot_2024-01-29_at_14.26.15.png)

If you need help with budgeting or would like to learn more about our Custom API plans, please [contact us](https://leonardo.ai/contact-us/).

Check remaining API Credits and Web Tokens

[](#check-remaining-api-credits-and-web-tokens)
=============================================================================================

Use the [Get User API](/reference/getuserself) endpoint to view your remaining API credits. This can be used to check how many credits you still have and/or set up alerting.

Sample Response:

`{   "user_details": [     {       "user": {         "id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",         "username": <YOUR_USERNAME>       },       "tokenRenewalDate": null,       "paidTokens": 38500,       "subscriptionTokens": 1005,       "subscriptionGptTokens": 1000,       "subscriptionModelTokens": 5,       "apiConcurrencySlots": 5,       "apiPaidTokens": 45677,       "apiSubscriptionTokens": 13,       "apiPlanTokenRenewalDate": null     }   ] }`

> 📘
> 
> Tip
> 
> 
> ---------
> 
> *   The Remaining Web Tokens seen in your top left hand corner will be a combination of `paidTokens` and `subscriptionTokens`
> *   The Remaining Credits seen in your [API tab](https://app.leonardo.ai/api-access) under Usage will be a combination of `apiPaidTokens` and `apiSubscriptionTokens`.

### 

Web Tokens

[](#web-tokens)

From the example above:

`"paidTokens": 38500, "subscriptionTokens": 1005,`

38,500 + 1005 = 39,505 Remaining Web Tokens as shown in the top left hand of your account.

![](https://files.readme.io/b05b361-Screenshot_2024-03-21_at_11.51.22_am.png)

### 

API Credits

[](#api-credits)

From the example above:

 `"apiPaidTokens": 45677,    "apiSubscriptionTokens": 13,`

45,677+13 = 45,690 Remaining Credits as shown in the [API Usage tab](https://app.leonardo.ai/api-access) below.

![](https://files.readme.io/249f8cd-Screenshot_2024-03-14_at_4.02.00_pm.png)

If you would like to increase your concurrency or increase your monthly credit limit, or learn more about our Custom API plans, please [contact us](https://leonardo.ai/contact-us/).

Updated 14 days ago

* * *

[

Guide to Handling Not Safe for Work Image Generation (NSFW)

](/docs/guide-to-handling-not-safe-for-work-image-generation-nsfw)[

Manage Usage with Auto Top-up

](/docs/manage-usage-with-auto-top-up)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Pricing Calculator on the Web App](#pricing-calculator-on-the-web-app)
    *   [Pricing Calculator on the API](#pricing-calculator-on-the-api)
    *   [Estimated Pricing Table](#estimated-pricing-table)
        *   [SDXL Finetuned Model, PhotoReal v1, and SD Finetuned Model](#sdxl-finetuned-model-photoreal-v1-and-sd-finetuned-model)
        *   [SD 1.5 and SD 2.1](#sd-15-and-sd-21)
        *   [Fixed Costs](#fixed-costs)
        *   [Realtime Canvas (LCM Generations)](#realtime-canvas-lcm-generations)
    *   [Monitoring and Tracking API Credits](#monitoring-and-tracking-api-credits)
    *   [Check remaining API Credits and Web Tokens](#check-remaining-api-credits-and-web-tokens)
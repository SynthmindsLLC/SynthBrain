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

Generate Images Using Alchemy
=============================

The guide will recreate the following functionality in the Web UI via API.

![V2 Alchemy ](https://files.readme.io/ee5d9c3-Screenshot_2024-04-09_at_3.34.36_pm.png)

V2 Alchemy

![V1 Alchemy ](https://files.readme.io/cde927d-Screenshot_2024-04-09_at_3.35.30_pm.png)

V1 Alchemy

> 📘
> 
> Tip
> 
> 
> ---------
> 
> There is no need to specify which version of Alchemy is required, the **models will automatically apply the appropriate Alchemy version.**

Generating with Alchemy will produce a higher Output Resolution than the Input dimensions specified in the API body. Find out your Image dimension via the Web App like this.

![](https://files.readme.io/7f11e5e-Screenshot_2024-04-12_at_1.53.13_pm.png)

### 

Sample Request

[](#sample-request)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 512,   "prompt": "A beautiful sleeping white cat",   "modelId": "aa77f04e-3eec-4034-9c07-d0f619684628",//Leonardo Kino XL model   "width": 512,   "alchemy": true,   "presetStyle": "CINEMATIC", } '`

Models and Alchemy Version

[](#models-and-alchemy-version)
-------------------------------------------------------------

This is not a full comprehensive list of all Models. To view all platform models, use the List Platform Models [endpoint](/reference/listplatformmodels).

| Alchemy Applied | Example Models |
| --- | --- |
| V2 | Leonardo Lightning XL  
Leonardo Anime XL  
Leonardo Kino XL  
Leonardo Vision XL  
Leonardo Diffusion XL  
AlbedoBase XL  
SDXL 1.0  
SDXL 0.9 |
| V1 | Absolute Reality v1.6  
Anime Pastel Dream  
Dreamshaper v7  
Stable Diffusion 1.5  
Stable Diffusion 2.1 |

An easy way to view which Alchemy pipeline will be used for your model is to view it on the Web. Any XL model will be using Alchemy v2. A list of all models on the Web can also be found [here](https://app.leonardo.ai/finetuned-models).

![](https://files.readme.io/3dcac27-Screenshot_2024-04-09_at_4.43.35_pm.png)

Updated 2 months ago

* * *

[

Generate Images Using PhotoReal

](/docs/generate-images-using-photoreal)[

Generate Images Using Image to Image Guidance

](/docs/generate-images-using-image-to-image-guidance)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   *   [Sample Request](#sample-request)
    *   [Models and Alchemy Version](#models-and-alchemy-version)
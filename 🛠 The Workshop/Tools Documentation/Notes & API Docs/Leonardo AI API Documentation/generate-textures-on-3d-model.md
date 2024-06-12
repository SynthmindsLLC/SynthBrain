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

Generate Textures on 3D model
=============================

Follow this recipe to upload 3D model and generate a 3D texture on the model:

⚔️

Upload and Generate Texture on 3D Model

Open Recipe

* * *

The guide will recreate the following functionality in the Web UI via API.

![Select Upload New object to create Texture Generation](https://files.readme.io/701d8fa-Screenshot_2024-03-08_at_3.05.40_pm.png)

Select Upload New object to create Texture Generation

Learn more about uploading via a presigned URL [here](/docs/how-to-upload-an-image-using-a-presigned-url)

> 🚧
> 
> Notice
> 
> 
> ------------
> 
> *   Only 3D models in .OBJ format can be accepted as the file extension.
> *   Models need to have a UV mapping to generate Textures.

![Inserting prompt to Generate preview of Texture](https://files.readme.io/5eab8b4-Screenshot_2024-03-08_at_3.51.00_pm.png)

Inserting prompt to Generate preview of Texture

> 📘
> 
> Tip
> 
> 
> ---------
> 
> *   Already have a model uploaded? Find your model ID using the [Get 3D models by user ID API endpoint](/reference/get_models-3d-user-userid)
> *   Use [Webhooks](/docs/guide-to-the-webhook-callback-feature) to get notified in real time when your Textures have completed generating.
> *   View your textures using the [Get Texture Generation by ID](/reference/get_generations-texture-id) API call after creating the Texture Generation.
> *   Model icon preview won't appear on the Texture Generation Web UI but can still be viewed when clicked into.

Generate multiple textures for the same model example.

![Example textures generated on 3D model](https://files.readme.io/e23a271-Screenshot_2024-03-20_at_12.34.43_pm.png)

Example textures generated on 3D model

### 

Sample Request

[](#sample-request)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations-texture \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "prompt": "sword, silver high metallic, low roughness, leather wrapped handle, black guard",   "preview": True,   "modelAssetId": <YOUR_MODEL_ID> }`

### 

Cost

[](#cost)

| Request | Cost |
| --- | --- |
| Preview Generation | 30 credits |
| Full Texture Generation | 150 credits |

Updated 3 months ago

* * *

[

Upscale with Universal Upscaler

](/docs/image-variations-with-universal-upscaler)[

Prompt Generation

](/docs/prompt-generation)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Sample Request](#sample-request)
    *   [Cost](#cost)

🦉

Recipe Title
============

Recipe Description

1.

cURL

​x

1{"success":true}
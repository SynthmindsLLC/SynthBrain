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

Generate Motion Using Uploaded Images
=====================================

Example for generating a video (motion) from your own image

Follow this recipe to generate motion using uploaded images:

🎞️

Generate Motion Using Uploaded Images

Open Recipe

* * *

The guide will recreate the following functionality in the Web UI via API.

![Selecting Images from Recent Generations for Motion](https://files.readme.io/49a4fae-Screenshot_2024-02-27_at_5.17.06_pm.png)

Use Images from Uploaded Images for Motion

![Creating Motion with Uploaded Image](https://files.readme.io/d175b11-Screenshot_2024-02-27_at_5.17.27_pm.png)

Creating Motion with Uploaded Image

> 📘
> 
> Tip
> 
> 
> ---------
> 
> The API endpoints to upload init images or dataset images return a presigned URL. Use this URL to upload the image file to S3. View more details on how to create a presigned URL [here](/docs/how-to-upload-an-image-using-a-presigned-url)

### 

Sample Request

[](#sample-request)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations-motion-svd \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "imageId": "<YOUR_INIT_IMAGE_ID>",   "motionStrength": 3,   "isInitImage": True } '`

Updated 3 months ago

* * *

[

Generate Motion Using Generated Images

](/docs/generate-motion-using-generated-images)[

Generate Motion Using Variation Images

](/docs/generate-motion-using-variation-images)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Sample Request](#sample-request)

🦉

Recipe Title
============

Recipe Description

1.

cURL

​x

1{"success":true}
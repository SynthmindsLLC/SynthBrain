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

Generate Images Using Fantasy Avatar \[Beta\]
=============================================

> ❗️
> 
> Deprecating Feature
> 
> 
> -------------------------
> 
> The Fantasy Avatar Feature will be deprecating in the near future. We recommend using [Character Reference](/docs/generate-images-using-image-to-image-guidance#character-reference) for a more accurate character control feature, this will be compatible with other multiple Control Nets.

![Left: Input image of a face (face_image.jpg). Right: Output image with the prompt “a witch”](https://files.readme.io/c2eb017-Screenshot_2024-03-14_at_17.27.28.png)

Left: Input image of a face (face\_image.jpg). Right: Output image with the prompt “a witch”

Fantasy Avatar is a feature for generating images with a face input image and a prompt. The face is used to influence the output, great for generating creative selfies and portraits.

> 📘
> 
> Fantasy Avatar is currently on public beta.
> 
> 
> -------------------------------------------------
> 
> Please let us know your feedback by [reaching out to support](/docs/need-more-support).

Follow this recipe to generate images using Fantasy Avatar:

🖼️

Generate Images Using Fantasy Avatar

Open Recipe

### 

Sample Request

[](#sample-request)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 512,   "fantasyAvatar": true,   "prompt": "A witch",   "width": 512,   "num_images": 1,   "init_image_id": <YOUR_INIT_IMAGE_ID> } '`

### 

Required Parameters

[](#required-parameters)

*   **fantasyAvatar** - Enable the Fantasy Avatar feature.
*   **prompt** - The prompt used to generate images.
*   **init\_image\_id** - Image ID of uploaded photo. Must be a single human face facing forward.

### 

Recommended Parameters

[](#recommended-parameters)

*   **width** - The input width of the images. Default is 512. Max is 1024 and must be a multiple of 8. Best set to 640.
*   **height** - The input height of the images. Default is 512. Max is 1024 and must be a multiple of 8. Best set to 832.
*   **negative\_prompt** - The negative prompt used to generate images. Best to have negative prompts.
*   **num\_images** - The number of output images. Default is 4.

### 

Other Parameters

[](#other-parameters)

*   **seed** - Default is no seed.
*   **guidance\_scale** - The strength of the influence of the input image. Recommended and default is 7. Must be between 1 and 20.

### 

Ignored Parameters

[](#ignored-parameters)

All other parameters listed in the [Create a Generation of Images API endpoint](/reference/creategeneration) that are not listed above are ignored. Enabling fantasyAvatar will disable other additional settings.

### 

Cost

[](#cost)

| Image Dimension | API Credit Cost |
| --- | --- |
| 512 x 512 | 20 per image |
| 640 x 832 | 24 per image |
| 1024 x 1024 | 25 per image |

Updated 16 days ago

* * *

[

Generate Images with Realtime Canvas

](/docs/generate-images-with-realtime-canvas)[

Generate Images Using Transparency

](/docs/generate-images-using-transparency)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Sample Request](#sample-request)
    *   [Required Parameters](#required-parameters)
    *   [Recommended Parameters](#recommended-parameters)
    *   [Other Parameters](#other-parameters)
    *   [Ignored Parameters](#ignored-parameters)
    *   [Cost](#cost)

🦉

Recipe Title
============

Recipe Description

1.

cURL

​x

1{"success":true}
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

Generate Images Using PhotoReal
===============================

Follow this recipe to generate images using PhotoReal v2

📸

Generate Images Using PhotoReal v2

Open Recipe

* * *

> 👍
> 
> Update
> 
> 
> ------------
> 
> Negative Prompts can be used with PhotoReal v2 via API.

PhotoReal v2

[](#photoreal-v2)
---------------------------------

The guide will recreate the following functionality in the Web UI via API.

![](https://files.readme.io/3a7f34c-Screenshot_2024-03-27_at_11.20.45_am.png)

Specify PhotoReal v2 using `"photoRealVersion":"v2"`, if not specified, the default PhotoReal version will be v1.

> 📘
> 
> Tip
> 
> 
> ---------
> 
> *   Alchemy needs to be set to true (e.g`"alchemy": true`)
> *   `modelId` for PhotoReal v2 needs to be specified as Leonardo Kino XL, Leonardo Diffusion XL or Leonardo Vision XL
> *   `photoRealStrength` is not required for PhotoReal v2

**Preset Styles available**

| Style | Value |
| --- | --- |
| Bokeh | BOKEH |
| Cinematic | CINEMATIC |
| Cinematic (Closeup) | CINEMATIC\_CLOSEUP |
| Creative | CREATIVE |
| Fashion | FASHION |
| Film | FILM |
| Food | FOOD |
| HDR | HDR |
| Long Exposure | LONG\_EXPOSURE |
| Macro | MACRO |
| Minimalistic | MINIMALISTIC |
| Monochrome | MONOCHROME |
| Moody | MOODY |
| Neutral | NEUTRAL |
| Portrait | PORTRAIT |
| Retro | RETRO |
| Stock Photo | STOCK\_PHOTO |
| Vibrant | VIBRANT |
| Unprocessed | UNPROCESSED |

### 

Sample Request

[](#sample-request)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 512,   "prompt": "A majestic cat in the snow",   "negative_prompt": "trees",   "modelId": "aa77f04e-3eec-4034-9c07-d0f619684628",//Leonardo Kino XL model   "width": 512,   "alchemy": true,   "presetStyle": "DYNAMIC",   "photoReal": true,   "photoRealVersion":"v2" } '`

PhotoReal v1

[](#photoreal-v1)
---------------------------------

Follow this recipe to generate images using PhotoReal v1

🖼️

Generate Images Using PhotoReal

Open Recipe

* * *

The guide will recreate the following functionality in the Web UI via API.

![](https://files.readme.io/2f30d3b-Screenshot_2024-02-26_at_4.48.14_pm.png)

> 📘
> 
> Tip
> 
> 
> ---------
> 
> *   Alchemy needs to be set to true (e.g`"alchemy": true`)
> *   `modelId` does not need to be specified in the API body when using PhotoReal v1.

**Preset Styles available**

| Style | Value |
| --- | --- |
| Cinematic | CINEMATIC |
| Creative | CREATIVE |
| Vibrant | VIBRANT |

### 

Sample Request

[](#sample-request-1)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 512,   "prompt": "A cat staring at a window",   "width": 512,   "alchemy": true,   "photoReal": true,   "photoRealStrength": 0.5,   "presetStyle": "CINEMATIC" } '`

Updated about 1 month ago

* * *

[

Generate your First Images

](/docs/generate-your-first-images)[

Generate Images Using Alchemy

](/docs/generate-images-using-alchemy)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [PhotoReal v2](#photoreal-v2)
        *   [Sample Request](#sample-request)
    *   [PhotoReal v1](#photoreal-v1)
        *   [Sample Request](#sample-request-1)

🦉

Recipe Title
============

Recipe Description

1.

cURL

​x

1{"success":true}

🦉

Recipe Title
============

Recipe Description

1.

cURL

​x

1{"success":true}
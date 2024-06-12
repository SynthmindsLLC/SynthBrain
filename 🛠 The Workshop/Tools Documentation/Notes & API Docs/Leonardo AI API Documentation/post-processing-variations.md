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

Upscale with Universal Upscaler
===============================

Follow this recipe to create high resolution upscale images using Universal Upscaler.

🌌

Use Universal Upscaler with Generated Images

Open Recipe

🌌

Use Universal Upscaler with Uploaded Images

Open Recipe

* * *

Upscaling using Universal Upscaler

[](#upscaling-using-universal-upscaler)
-----------------------------------------------------------------------------

The guide will recreate the following functionality in the Web UI via API.

![Universal Upscaler on Leonardo.AI Web ](https://files.readme.io/2f44003-Screenshot_2024-04-19_at_3.32.35_pm.png)

Universal Upscaler on Leonardo.AI Web

![Upscale settings in Universal Upscaler](https://files.readme.io/152d81c-Screenshot_2024-04-19_at_3.30.52_pm.png)

Upscale settings in Universal Upscaler

**Upscaler Styles available**

| Style | Value |
| --- | --- |
| General | GENERAL |
| 2D Art & Illustration | 2D ART & ILLUSTRATION |
| Cinematic | CINEMATIC |
| CG Art & Game Assets | CG ART & GAME ASSETS |

> 📘
> 
> Tip
> 
> 
> ---------
> 
> *   The parameter`creativityStrength` refers to how 'creative' the AI will be on the original image. The higher it is, the more details will be applied.
> *   The `upscaleMultiplier` must be between 1 and 2. The bigger the value, the higher the resolution.
> *   The maximum upscaled image size is 20MP.

### 

Sample Request

[](#sample-request)

`curl --request GET \      --url https://cloud.leonardo.ai/api/rest/v1/generations/<YOUR_GENERATION_ID> \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>'  {   "upscalerStyle": "CINEMATIC",   "creativityStrength": 8,   "upscaleMultiplier": 2,   "generatedImageId": "<YOUR_GENERATED_IMAGE_ID>", }`

Ensure that you run the [Get Variation ID endpoint](/reference/getvariationbyid) to retrieve the image URL after this step

### 

Cost

[](#cost)

The cost is based on the output megapixel size.

| Megapixels | Credits |
| --- | --- |
| 1-5 | 60 |
| 6 | 80 |
| 7 | 100 |
| 8 | 120 |
| 9 | 140 |
| 10 | 160 |
| 11 | 180 |
| 12 | 200 |
| 13 | 220 |
| 14 | 240 |
| 15 | 260 |
| 16 | 280 |
| 17 | 300 |
| 18 | 320 |
| 19 | 340 |
| 20 | 360 |

Updated about 2 months ago

* * *

[

Generate Motion Using Variation Images

](/docs/generate-motion-using-variation-images)[

Texture Generation

](/docs/3d-texture-generation)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Upscaling using Universal Upscaler](#upscaling-using-universal-upscaler)
        *   [Sample Request](#sample-request)
        *   [Cost](#cost)

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
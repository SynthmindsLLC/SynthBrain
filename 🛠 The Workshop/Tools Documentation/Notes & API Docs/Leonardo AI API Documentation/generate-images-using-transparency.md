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

Generate Images Using Transparency
==================================

The [Transparency](https://intercom.help/leonardo-ai/en/articles/9075772-transparency) feature enables you to generate images with a transparent background.

This guide recreates the following Transparency setting in the Leonardo Web App via API.

![Generating with the Transparency feature on the web app](https://files.readme.io/0501294-Screenshot_2024-03-20_at_16.49.47.png)

Generating with the Transparency feature on the web app

### 

Sample Request

[](#sample-request)

This request will generated an image without a background.

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "alchemy": false,   "prompt": "an orange cat",   "width": 512,   "height": 512,   "modelId": "aa77f04e-3eec-4034-9c07-d0f619684628",   "transparency": "foreground_only",   "elements": [     {       "akUUID": "5f3e58d8-7af3-4d5b-92e3-a3d04b9a3414",       "weight": 0.5     }   ] } '`

*   `"transparency": "foreground_only"` - Enables the transparency foreground only feature. The foreground image will be generated and the background will be removed.
*   `"modelId": "aa77f04e-3eec-4034-9c07-d0f619684628"` - Sets the model to Leonardo Kino XL, one of the compatible models to transparency feature.
*   `"elements.[0].akUUID": "5f3e58d8-7af3-4d5b-92e3-a3d04b9a3414"` - Sets the element to Simple Flat Illustration, one of the compatible elements to transparency feature.

> 📘
> 
> Tip
> 
> 
> ---------
> 
> To learn more about the recommended models and elements, please refer to the [compatibility list](https://intercom.help/leonardo-ai/en/articles/9075772-transparency#h_b528f6b0ed).

### 

Sample Output

[](#sample-output)

Below is a sample output corresponding the the sample request above where transparency is set to foreground\_only. The output generated is a PNG file with no background.

![Sample output using Leonardo Kino XL model, Simple Flat Illustration element, and the prompt "an orange cat"](https://files.readme.io/7c410f3-Default_an_orange_cat_1.png)

Sample output using Leonardo Kino XL model, Simple Flat Illustration element, and the prompt "an orange cat"

Updated 3 months ago

* * *

[

Generate Images Using Fantasy Avatar \[Beta\]

](/docs/generate-images-using-fantasy-avatar)[

Video Generation (Motion)

](/docs/video-generation-motion)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Sample Request](#sample-request)
    *   [Sample Output](#sample-output)
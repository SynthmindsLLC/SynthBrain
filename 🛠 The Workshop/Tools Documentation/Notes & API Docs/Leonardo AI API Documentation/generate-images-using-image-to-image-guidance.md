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

Generate Images Using Image to Image Guidance
=============================================

This feature allows for uploaded or generated Images as reference, apply ControlNet and add finer adjustments to your image appearance.

> 👍
> 
> Update
> 
> 
> ------------
> 
> Image guidance via API now supports multiple ControlNets

Follow these recipes with code snippets to generate images using image guidance

🖼️

Generate with Image to Image Guidance using Generated Images

Open Recipe

🖼️

Generate with Image Guidance using multiple ControlNets

Open Recipe

Style Reference

[](#style-reference)
=======================================

This guide will recreate the following [Style Reference](https://intercom.help/leonardo-ai/en/articles/8497988-image-guidance#:~:text=How%20to%20use%20Style%20Reference) functionality in the Web UI via API.

![Using multiple Style Reference on the Web App](https://files.readme.io/ea164ce-Screenshot_2024-05-10_at_11.15.05_am.png)

Using multiple Style Reference on the Web App

![Generation using multiple Style Reference](https://files.readme.io/ba437fc-Screenshot_2024-05-10_at_11.17.50_am.png)

Generation using multiple Style Reference

Parameter breakdown:

*   Specify your image type in `initImageType` as either `GENERATED` for Leonardo.Ai generated images or `UPLOADED` if you upload your own image.
*   The parameter `weight` is a numeric value between 0-2, and '`strengthType`' is a string comprised of the values between Low-Max. This will be bucketed under these settings:

| `strengthType` | `weight` |
| --- | --- |
| Low | 0-0.4 |
| Mid | 0.4-0.8 |
| High | 0.8-1.2 |
| Ultra | 1.2-1.6 |
| Max | 1.6-2 |

Either parameters can be used for the guidance strength, but not both at the same time.

*   `influence` will only appear if multiple Style References are used, and only used for Style Reference. This is a **ratio** of the influence of the two images. i.e. The right image from the example will have a higher influence on the output.

E.g. If Image A has an influence of 1 and Image B also has an influence of 1, their ratio will be 1:1. Similarly, if Image A has an influence of 0.5 and Image B has an influence of 0.5, the ratio remains 1:1. It's important to note that the total of both image influences does not necessarily need to add up to 1.

*   If only using one style reference image, you don’t need to include influence in the body parameter.

### 

Sample Request

[](#sample-request)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 512,   "modelId": "aa77f04e-3eec-4034-9c07-d0f619684628",//Leonardo Kino XL   "prompt": "A wistful young woman stands in the beaming doorway of a sunlit room",   "presetStyle":"CINEMATIC",   "width": 1024,   "photoReal": true,   "photoRealVersion":"v2",   "alchemy":true,   "controlnets": [         {             "initImageId": <YOUR_GENERATED_IMAGE_ID>,             "initImageType": "GENERATED",             "preprocessorId": 67, //Style Reference ID             "strengthType": "High",             "influence": 0.39         },         {             "initImageId": <YOUR_INIT_IMAGE_ID>,             "initImageType": "UPLOADED",             "preprocessorId": 67,             "strengthType": "High",             "influence": 0.64         }     ] }`

Character Reference

[](#character-reference)
===============================================

This guide will recreate the following functionality in the Web UI via API.

![Using Character Reference with Style Reference](https://files.readme.io/b881ec7-Screenshot_2024-05-10_at_2.27.53_pm.png)

Using Character Reference with Style Reference

![Generation using Character and Style Reference](https://files.readme.io/27dc8ed-Screenshot_2024-05-10_at_2.30.06_pm.png)

Generation using Character and Style Reference

Parameter breakdown:

*   Specify your image type in `initImageType` as either `GENERATED` for Leonardo.Ai generated images or `UPLOADED` if you upload your own image.
*   The parameter `weight` is a numeric value between 0-2, and '`strengthType`' is a string comprised of the values between Low-Max. This will be bucketed under these settings:

| `strengthType` | `weight` | Description |
| --- | --- | --- |
| Low | 0-0.66 | Provide greatest flexibility at the cost of resemblance |
| Mid | 0.66-1.32 | Display reasonable flexibility and more resemblance. |
| High | 0.32-2 | Less flexible but have the best resemblance. |

> 📘
> 
> Note
> 
> 
> ----------
> 
> Character Reference is not intended as a face swap feature and does not guarantee a perfect replica of a person in the output.

### 

Sample Request

[](#sample-request-1)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 576,   "modelId": "aa77f04e-3eec-4034-9c07-d0f619684628",//Leonardo Kino XL   "prompt": "A mesmerizing lady with cascading strands of blonde hair gazes through a misty train window",   "presetStyle":"CINEMATIC",   "width": 1024,   "photoReal": true,   "photoRealVersion":"v2",   "alchemy":true,   "controlnets": [         {             "initImageId": <YOUR_INIT_IMAGE_ID>,             "initImageType": "UPLOADED",             "preprocessorId": 133,//Character Reference Id             "strengthType": "Mid",         },         {             "initImageId": <YOUR_GENERATED_IMAGE_ID>,             "initImageType": "GENERATED",             "preprocessorId": 67,//Style Reference Id             "strengthType": "High",         }     ] }`

Image to Image Guidance

[](#image-to-image-guidance)
=======================================================

![Using Image to Image with Style Reference](https://files.readme.io/a0c613d-Screenshot_2024-05-13_at_3.00.23_pm.png)

Using Image to Image with Style Reference

![](https://files.readme.io/402468f-Screenshot_2024-05-13_at_2.59.47_pm.png)

### 

Sample Request

[](#sample-request-2)

Image to Image does not require ControlNet preprocessor IDs, below is an example request.

> 📘
> 
> Note
> 
> 
> ----------
> 
> *   Image to Image with multiple ControlNets is incompatible with most SDXL models, except for Style Reference (67) and Character Reference (133) Preprocessor IDs.

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 644,   "modelId": "b24e16ff-06e3-43eb-8d33-4416c2d75876" //Leonardo Lightning XL,   "prompt": "Vibrant makeup bottle in a showroom",   "presetStyle":"DYNAMIC",   "width": 1040,   "alchemy":true,   "controlnets": [         {             "initImageId":<YOUR_GENERATED_IMAGE_ID>,             "initImageType": "GENERATED",             "preprocessorId": 67, //Style Reference ID             "strengthType": "High",         }          ],   "init_image_id": <YOUR_INIT_IMAGE_ID> ,   "init_strength": 0.5, }`

Other ControlNets

[](#other-controlnets)
===========================================

Image Guidance uses different preprocessor IDs depending on the [base model](/docs/elements-and-model-compatibility#finetuned-models-and-elements-compatibility-table) for different ControlNets. Refer to the table below to combine multiple ControlNets.

| ControlNet | SD1.5 | SD2.1 | SDXL |
| --- | --- | --- | --- |
| Style Reference | x | x | 67 |
| Character Reference | x | x | 133 |
| Content Reference | x | x | 100 |
| Edge to Image | 1 | 12 | 19 |
| Depth to Image | 3 | 13 | 20 |
| Pose to Image | 7 | 16 | 21 |
| Text Image Input | 11 | 18 | 22 |
| Sketch to Image | 10 | 17 | x |
| Normal Map | 6 | 15 | x |
| Line Art | 5 | x | x |
| Pattern to Image | 8 | x | x |
| QR Code to Image | 9 | x | x |

### 

Sample Request

[](#sample-request-3)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 512,   "modelId": "aa77f04e-3eec-4034-9c07-d0f619684628",//Leonardo Kino XL   "prompt": "Intricately swirling nebulas dance across a vividly colored galactic map",   "width": 1024,   "alchemy":true,   "controlnets": [         {             "initImageId": <YOUR_GENERATED_IMAGE_ID>,             "initImageType": "GENERATED",             "preprocessorId": 19, //Edge to Image ID             "weight": "0.5"         }        ] }`

Image Guidance using Uploaded or Generated Images (Legacy format)

[](#image-guidance-using-uploaded-or-generated-images-legacy-format)
=========================================================================================================================================

The guide will recreate the following functionality in the Web UI via API.

![Applying previously generated image as Image to Image Guidance](https://files.readme.io/5659a26-Screenshot_2024-01-30_at_2.41.21_pm.png)

Applying previously generated image as Image to Image Guidance

> 🚧
> 
> Limitations
> 
> 
> -----------------
> 
> *   Legacy Image Guidance features on API does not have full parity with the Web UI.
> 
> `controlNetType`,`controlNet` and `weighting` are now legacy ControlNet parameters.

| ControlNet | `controlNetType` |
| --- | --- |
| Edge to Image | CANNY |
| Pose to Image | POSE |
| Depth to Image | DEPTH |

### 

Sample Request For Uploaded Images

[](#sample-request-for-uploaded-images)

This request has **no ControlNets added**, it is only using Image to Image Guidance.

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 512,   "modelId": "1e60896f-3c26-4296-8ecc-53e2afecc132",   "prompt": "An oil painting of an orange cat",   "width": 512,   "init_image_id": <YOUR_INIT_IMAGE_ID> ,   "init_strength": 0.5, }`

### 

Sample Request for Generated Images

[](#sample-request-for-generated-images)

> 🚧
> 
> Legacy Feature
> 
> 
> --------------------
> 
> The following request is a legacy ControlNet parameter and will be soon be deprecating. We recommend to use the new ControlNet parameters which also allows for multiple ControlNets.

This request adds **Edge to Image ControlNet** using your previously generated image.

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 512,   "modelId": "1e60896f-3c26-4296-8ecc-53e2afecc132",   "prompt": "An oil painting of an orange cat",   "width": 512   "init_generation_image_id": "<YOUR_GENERATED_IMAGE_ID>",   "init_strength": 0.5,   "controlNet": True,   "controlNetType": "CANNY"   }`

Updated 16 days ago

* * *

What’s Next

View our other API References below

*   [Create a Generation of Images](/reference/creategeneration)
*   [Upload init image](/reference/uploadinitimage)
*   [Create SVD Motion Generation](/reference/post_generations-motion-svd)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Style Reference](#style-reference)
    *   [Character Reference](#character-reference)
    *   [Image to Image Guidance](#image-to-image-guidance)
    *   [Other ControlNets](#other-controlnets)
    *   [Image Guidance using Uploaded or Generated Images (Legacy format)](#image-guidance-using-uploaded-or-generated-images-legacy-format)

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
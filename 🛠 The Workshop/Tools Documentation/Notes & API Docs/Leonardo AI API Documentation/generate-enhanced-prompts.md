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

Generate Enhanced Prompts
=========================

Improve your prompts or create random prompts via API

[Improve Prompt](/reference/post_prompt-improve)

[](#improve-prompt)
=======================================================================

The guide will recreate the following functionality in the Web UI via API.

![Improve prompt functionality on web](https://files.readme.io/570be02-Screenshot_2024-03-28_at_11.45.23_am.png)

Improve prompt functionality on web

> 📘
> 
> Tip
> 
> 
> ---------
> 
> The `prompt` parameter has a limit of 200 characters

Sample Request

[](#sample-request)
-------------------------------------

`curl --request POST \      --url 'https://cloud.leonardo.ai/api/rest/v1/prompt/improve' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "prompt": "Meridian sea", }`

An example response

`{     "promptGeneration": {         "prompt": "A luminously shimmering Meridian sea, its surface a kaleidoscope of captivating hues that shift with the touch of the sun. Beneath the crystalline waters, vibrant aquatic life dances amid coral reefs in a mesmerizing display of colors and shapes. This breathtaking scene is captured in a stunningly detailed painting, where every brushstroke seems to breathe life into the underwater world. The image emanates a sense of peacefulness and wonder, drawing viewers into a tranquil realm of beauty and serenity.",         "apiCreditCost": 4     } }`

[New Random Prompt](/reference/post_prompt-random)

[](#new-random-prompt)
============================================================================

The guide will recreate the following functionality in the Web UI via API.

![New Random Prompt functionality on web](https://files.readme.io/dbe84b5-Screenshot_2024-03-28_at_11.56.54_am.png)

New Random Prompt functionality on web

Sample Request

[](#sample-request-1)
---------------------------------------

`curl --request POST \      --url 'https://cloud.leonardo.ai/api/rest/v1/prompt/random' \      --header 'authorization: Bearer <YOUR_API_KEY>' \`

An example response

`{   "promptGeneration": {     "prompt": "A luridly glowing nightmare dragon, its jagged scales shimmering with an eerie light that seems to emanate from within. The dragon is depicted in a vivid gouache painting, the fantastical creature appearing almost tangible against the dark, fantastical background. The artist's attention to detail is impeccable - each scale and claw is rendered with exquisite precision, drawing the viewer into the mesmerizing world of the creature. The overall effect is haunting yet strangely beautiful, a testament to the artist's skill and imagination.",     "apiCreditCost": 4   } }`

  

Cost

[](#cost)
=================

| Request | Cost |
| --- | --- |
| Improve Prompt | 4 credits |
| New Random Prompt | 4 credits |

Updated 2 months ago

* * *

[

Generate Textures on 3D model

](/docs/generate-textures-on-3d-model)[

Best Practices

](/docs/best-practices)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Improve Prompt](#improve-prompt)
        *   [Sample Request](#sample-request)
    *   [New Random Prompt](#new-random-prompt)
        *   [Sample Request](#sample-request-1)
    *   [Cost](#cost)
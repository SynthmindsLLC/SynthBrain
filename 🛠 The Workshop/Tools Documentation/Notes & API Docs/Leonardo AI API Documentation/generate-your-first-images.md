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

Generate your First Images
==========================

Now that you have your API key, you’re ready to generate your first images on Leonardo!

Follow this recipe to generate your first images:

🖼️

Generate your First Images

Open Recipe

* * *

The guide will recreate the following functionality in the Web UI via API.

![Creating Prompt to generate a series of images with model and style specified](https://files.readme.io/a1225c6-Screenshot_2024-02-29_at_2.23.48_pm.png)

Creating Prompt to generate a series of images with model and style specified

Generating Images via API tester

[](#generating-images-via-api-tester)
-------------------------------------------------------------------------

Use the inbuilt tester from our API documentation to generate some images using the default example. Simply add in your [API key](/docs/create-your-api-key#provision-an-api-key) and select **Try It!**.

![Running on API tester in documentation](https://files.readme.io/8894164-Screenshot_2024-02-29_at_3.30.18_pm.png)

Running on API tester in documentation

Below is an example response.

![](https://files.readme.io/e601c6b-Screenshot_2024-02-29_at_3.38.54_pm.png)

Use the `generationId` for the [Get a Single Generation](/reference/getgenerationbyid) in the next call for you to view the images. Below is an expected example response

![](https://files.readme.io/0fbb8bf-Screenshot_2024-02-29_at_3.37.06_pm.png)

> 📘
> 
> Tip
> 
> 
> ---------
> 
> *   Use [Webhooks](/docs/guide-to-the-webhook-callback-feature) to get notified in real time when your Images have completed generating.
> *   View all the generations ever created from your account using the [Get generations by user ID](/reference/getgenerationsbyuserid) API call.

> 🚧
> 
> Heads up
> 
> 
> --------------
> 
> API credit costs will vary depending on the image size, model and features such as Alchemy.
> 
> To help you plan ahead, check out our handy guide [here](/docs/plan-with-the-pricing-calculator). Want to avoid running low on credits? Consider setting up Auto-top up for peace of mind.

### 

Sample Request

[](#sample-request)

`curl --request POST \      --url https://cloud.leonardo.ai/api/rest/v1/generations \      --header 'accept: application/json' \      --header 'authorization: Bearer <YOUR_API_KEY>' \      --header 'content-type: application/json' \      --data ' {   "height": 512,   "modelId": "6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",   "prompt": "An oil painting of a cat",   "width": 512 } '`

Be sure to check out the Image Generation guides for more customisation options and how to use the right combination of parameters to get the result you're looking for.

Updated 3 months ago

* * *

What’s Next

*   [Generate Images Using PhotoReal](/docs/generate-images-using-photoreal)
*   [Generate Images Using Image to Image Guidance](/docs/generate-images-using-image-to-image-guidance)
*   [Generate Motion Using Generated Images](/docs/generate-motion-using-generated-images)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Generating Images via API tester](#generating-images-via-api-tester)
        *   [Sample Request](#sample-request)

🦉

Recipe Title
============

Recipe Description

1.

cURL

​x

1{"success":true}
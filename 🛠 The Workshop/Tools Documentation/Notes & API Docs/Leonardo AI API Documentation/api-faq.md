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

API FAQ
=======

Answers to frequently asked questions when integrating to Leonardo.Ai via API

Models

[](#models)
=====================

### 

Where do I find the model ID of a specific platform model?

[](#where-do-i-find-the-model-id-of-a-specific-platform-model)

To find Leonardo.Ai's platform model IDs, use this [List Platform Models](/reference/listplatformmodels) endpoint to list out all Platform models. You'll find all the public models available with the id, name and description.

Another way is to navigate to the Leonard App, and select [Finetune Models](https://app.leonardo.ai/finetuned-models). Click on the Platform Models tab. Click on the model, then click on View More. This should reveal the Model ID of that particular model.

![](https://files.readme.io/0732c61-Screenshot_2024-02-14_at_4.13.45_pm.png)

### 

What is the model ID of PhotoReal?

[](#what-is-the-model-id-of-photoreal)

**PhotoReal v1** does not have a model ID.

To use PhotoReal on the Production API, you need to remove the modelId parameter and enable the photoReal flag.

For an example, check out the [Generate Images Using PhotoReal](/docs/generate-images-using-photoreal) sample recipe.

**PhotoReal v2** requires Leonardo Kino XL, Leonardo Diffusion XL or Leonardo Vision XL models. See [here](/docs/generate-images-using-photoreal#sample-request) for a sample request.

### 

Can I use my custom model with the Leonardo API?

[](#can-i-use-my-custom-model-with-the-leonardo-api)

Yes, you can use your own custom model with the Leonardo API.

### 

How do I find my custom model ID?

[](#how-do-i-find-my-custom-model-id)

On the Leonard App, navigate to the [Finetune Models](https://app.leonardo.ai/finetuned-models). Click on the Your Models tab. Click on the model, then click on View More. This should reveal the Model ID of that particular custom model.

![](https://files.readme.io/c05c8aa-Screenshot_2024-02-14_at_4.16.54_pm.png)

Generating Images

[](#generating-images)
===========================================

### 

How do I specify the number of Images in my generation?

[](#how-do-i-specify-the-number-of-images-in-my-generation)

Use the parameter `"num_images"`in your API body. For example, to generate 1 image only, your API body could look like this

`{   "height": 512,   "modelId": "6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",   "prompt": "An oil painting of a cat",   "width": 512,   "num_images": 1 }`

### 

How often should I be polling for image generations?

[](#how-often-should-i-be-polling-for-image-generations)

Instead of polling, the best practice is to set your [webhook callback](/docs/guide-to-the-webhook-callback-feature) so that Leonardo.Ai can notify you when to fetch your generation.

You can set your webhook callback URL and authentication details when creating a new Leonardo.Ai Production API key.

![](https://files.readme.io/a389772-Screenshot_2024-02-14_at_4.37.03_pm.png)

### 

How do I use Alchemy v2 on the API?

[](#how-do-i-use-alchemy-v2-on-the-api)

Alchemy V2 works with SDXL models like Leonardo Vision XL, Leonardo Diffusion XL, AlbedoBase XL and KinoXL. To use Alchemy v2, choose an SDXL model and simply set the alchemy parameter to true. This setup will use Alchemy v2.

### 

Do my images expire after generating via the API?

[](#do-my-images-expire-after-generating-via-the-api)

No, images generated via the Leonardo.Ai API will not expire and can also be accessed from the Web App at any time.

### 

Why is my guidance scale setting not reflected?

[](#why-is-my-guidance-scale-setting-not-reflected)

The guidance scale is an advanced parameter and Leonardo advises to use a guidance scale of 7 in most cases.

There are some default behaviours and conditions applied when trying to control the guidance scale. The conditions and logic are as follows:

*   If not set, guidance scale default is 7.
*   If not using Alchemy, guidance scale is limited to 1-20.
*   If using Alchemy but not using an SDXL model, guidance scale is limited to 2-30.
*   If not using Alchemy and scheduler is set to LEONARDO, guidance scale is capped at 7.

### 

How do you set Prompt Magic V3 to RAW mode using the API?

[](#how-do-you-set-prompt-magic-v3-to-raw-mode-using-the-api)

To set Prompt Magic V3 to RAW mode, set`"highContrast": false`. This is similar to enabling RAW mode on the Leonardo app.

### 

How do you set Alchemy's Resonance using the API?

[](#how-do-you-set-alchemys-resonance-using-the-api)

To set Alchemy's resonance, use the `guidance_scale` parameter. This controls the resonance setting on the UI.

### 

Why is the output image bigger than the height and width I specified?

[](#why-is-the-output-image-bigger-than-the-height-and-width-i-specified)

The input resolution is not always equal to the output resolution. When you use Alchemy and high resolution, the output resolution could be bigger by 1.5x, 1.75x, 2x, etc. compared to the input resolution due to upscaling built in to this features. For example, when using Alchemy v2, the output dimension is 1.75 times bigger. When using Alchemy v1, the output is 1.5 times bigger. When using Alchemy v1 and high resolution, the output is twice the input.

To check, you can observe this in the Leonardo web app as the following image.

![](https://files.readme.io/d3d7e43-Screenshot_2024-02-14_at_4.53.34_pm.png)  

Generating Motion

[](#generating-motion)
===========================================

### 

Why am I seeing Service Error when generating SVD motion?

[](#why-am-i-seeing-service-error-when-generating-svd-motion)

Although `Service Error`is a generic error message, in this scenario, the error is commonly due to incorrect IDs being used. Ensure that the ID is not the `generationId`from the [Create a Generation of Images API.](/reference/creategeneration), but rather the Image Id from [Get a Single Generation.](/reference/getgenerationbyid). The `generationId` needs to be passed to [Get a Single Generation.](/reference/getgenerationbyid) , and the returned image `Id` can then be used in the [Create SVD Motion Generation API](/reference/createsvdmotiongeneration).

Uploading Images

[](#uploading-images)
=========================================

### 

How do I upload an image for image to image?

[](#how-do-i-upload-an-image-for-image-to-image)

Use the [Upload Init Image API](/reference/uploadinitimage). This endpoint will return an image ID that you input to `init_image_id` in the [Create a Generation of Images API.](/reference/creategeneration). Ensure that if you are using `init_image_id`, that you also include `isInitImage:true`.

Follow this [recipe](/recipes/generate-with-image-to-image-guidance-using-uploaded-images) for a step by step guide on uploading images to use with image to image guidance.

### 

How to upload an image for image prompt?

[](#how-to-upload-an-image-for-image-prompt)

Use the [Upload Init Image API](/reference/uploadinitimage). This endpoint will return an image ID that you input to `imagePrompts` in the [Create a Generation of Images API.](/reference/creategeneration)

Follow this [recipe](/recipes/generate-images-using-image-prompts) for a step by step guide on using image prompts.

_Note: that the parameter imagePrompts accepts an array of image IDs as a string._

Example 1: One image prompt:

`imagePrompts: [“XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXX1”]`

Example 2: Two image prompts:

`imagePrompts: [XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX111, XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX222]`

### 

What is the extension parameter in the Upload Init Image API?

[](#what-is-the-extension-parameter-in-the-upload-init-image-api)

The extension parameter in the [Upload Init Image API](/reference/uploadinitimage) is the file extension of the image you want to upload. Examples of file extensions are png, jpg, jpeg, or webp only. The extension parameter will not accept the full filename or some binarized image data.

### 

What’s the difference between init\_generation\_image\_id versus init\_image\_id?

[](#whats-the-difference-between-init_generation_image_id-versus-init_image_id)

`init_generation_image_id` accepts the image ID of images generated on Leonardo.Ai. These image IDs are returned by API endpoints like the [Get Generations by User ID](/reference/getgenerationsbyuserid) and [Get a Single Generation.](/reference/getgenerationbyid)

`init_image_id` accepts the image ID returned by the [Upload Init Image API endpoint.](/reference/uploadinitimage)

Variations

[](#variations)
=============================

### 

How do I upscale an image via API?

[](#how-do-i-upscale-an-image-via-api)

To upscale an image via API, use the Variation: [Create Upscale API.](/reference/createvariationupscale) This Upscale will apply 'Creative Upscale' to your image.

### 

How do I get the image ID for transforming like upscale and unzoom?

[](#how-do-i-get-the-image-id-for-transforming-like-upscale-and-unzoom)

You can get the image IDs via the [Get a Single Generation](/reference/getgenerationbyid) or [Get generations by user ID](/reference/getgenerationsbyuserid) API endpoints. These return an array of URL links to images together with an `id` attribute. That`id`attribute is the image ID.

API Credits

[](#api-credits)
===============================

### 

Why is the cost of generating images different using API credits vs Web Tokens?

[](#why-is-the-cost-of-generating-images-different-using-api-credits-vs-web-tokens)

Charges are calculated differently for API calls compared to generating using Web Tokens from the Web App, resulting in variations in costs. Additionally, API credits do not expire, whereas Subscription Tokens have a limited validity period.

### 

How do I top up my API plan with more API credits?

[](#how-do-i-top-up-my-api-plan-with-more-api-credits)

You can buy instant top up API credits via the Leonardo.Ai app. Navigate to [API Access](https://app.leonardo.ai/api-access) on the left side menu, click on Production API tab, and click on the Top-up Credits button.

![](https://files.readme.io/ad8c3a5-Screenshot_2024-02-14_at_4.42.18_pm.png)

### 

Do API Credits expire?

[](#do-api-credits-expire)

No, API Credits do not expire. However, note that you can only use your API credits when you have an active API Plan Subscription.

### 

I still have credits why can't I make anymore API calls?

[](#i-still-have-credits-why-cant-i-make-anymore-api-calls)

Please ensure your API plan is active as you won't be able to access your credits without being on an API Plan.

### 

My API credit balance is negative, is that normal?

[](#my-api-credit-balance-is-negative-is-that-normal)

Yes, it's normal for API credits to go negative.  
​  
Blocking your usage once you run out of API credits is not a precise process. There are expected ways you could get to negative but our system won't let you get too far with a negative API credit balance.  
​  
Note that the negative API credits will be deducted from the next API credit top-up. To avoid running out of credits, [plan your usage](/docs/plan-with-the-pricing-calculator) or [set up auto top-ups](/docs/manage-usage-with-auto-top-up).

### 

Where is the API credits pricing calculator?

[](#where-is-the-api-credits-pricing-calculator)

The API pricing calculator is temporarily unavailable at the moment due to enhancements in progress and will be up and running soon. You can view here for [estimated API credit](/docs/plan-with-the-pricing-calculator) costs and plan your usage.

### 

Do I still get charged credits if my generation failed?

[](#do-i-still-get-charged-credits-if-my-generation-failed)

If you got charged credits but your generations failed via API, the credits will get refunded back into your account.

### 

How do I find the invoice for my API subscription plan?

[](#how-do-i-find-the-invoice-for-my-api-subscription-plan)

We use Paddle.com for our payment system, please head over to [https://paddle.net/](https://paddle.net/) and enter your email to locate your receipt. A copy of your invoice would also have been sent to your email automatically after payment.

Other Questions

[](#other-questions)
=======================================

### 

Does Leonardo have official SDKs?

[](#does-leonardo-have-official-sdks)

The following are Leonardo.Ai's official SDKs.

1.  [Python SDK](https://github.com/Leonardo-Interactive/leonardo-python-sdk)
2.  [TypeScript SDK](https://github.com/Leonardo-Interactive/leonardo-ts-sdk)

### 

Where did the User API key go?

[](#where-did-the-user-api-key-go)

The User API key is now a deprecated feature and has been replaced by the Production API key. This key can be used for all API endpoints and can be generated here. Existing User API keys still work, but new ones need to be generated as Production API keys.

Updated about 1 month ago

* * *

[

Manage Usage with Auto Top-up

](/docs/manage-usage-with-auto-top-up)[

API Error Messages

](/docs/api-error-messages)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Models](#models)
    *   [Generating Images](#generating-images)
    *   [Generating Motion](#generating-motion)
    *   [Uploading Images](#uploading-images)
    *   [Variations](#variations)
    *   [API Credits](#api-credits)
    *   [Other Questions](#other-questions)
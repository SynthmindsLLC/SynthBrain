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

Guide to Handling Not Safe for Work Image Generation (NSFW)
===========================================================

Choosing a Finetuned Model

[](#choosing-a-finetuned-model)
=============================================================

Leonardo.Ai continuously improves safeguards against NSFW generations. Newer Platform Models will tend to be less susceptive to NSFW generation.

Stable Diffusion v1.5 (SD1.5) and Platform Models based on SD1.5 are known to be prone to generate NSFW. As such, we use a more conservative detection and flagging mechanism for these family of models. The best practice is to use newer models such as those based on Stable Diffusion SDXL.0\_9, Stable Diffusion SDXL.1\_0, and SDXL.LIGHTNING (SDXL).

To check the base model of a Platform Model, navigate to [Finetuned Models](https://app.leonardo.ai/finetuned-models) and switch to platform Platform Models tab. Click on the model and then click on View More.

![Checking the base model of a Platform Model](https://files.readme.io/a8c70d2-Screenshot_2024-04-04_at_15.08.59.png)

Checking the base model of a Platform Model

You can also refer to the table [here](/docs/elements-and-model-compatibility#finetuned-models-and-elements-compatibility-table) to check the base model of a particular finetuned model.

> 📘
> 
> Note on PhotoReal
> 
> 
> -----------------------
> 
> PhotoReal v1 is a workflow based on SD1.5 thus prone to generate NSFW. The best practice is to use the latest version, PhotoReal v2, which uses SDXL.

Blocking at the Prompt Level

[](#blocking-at-the-prompt-level)
=================================================================

Like the Leonardo web app, the Leonardo API will block NSFW image generation by default. Any prompts flagged as NSFW will return a 400 Bad Request error.

For example, generating with a prompt “nude” will be blocked with the following error:

`{     "error": "content moderation filter: nude",     "path": "$",     "code": "unexpected"   }`

Flagging at the Response Level

[](#flagging-at-the-response-level)
=====================================================================

The Production API returns a NSFW attribute that flags if the image generated contains NSFW material. Depending on your use case, you can opt to filter out the flagged images and not return them to your end users.

`... "generated_images": \[         {           "url": "<https://cdn.leonardo.ai/users/ef8b8386-94f7-48d1-b10e-e87fd4dee6e6/generations/88b381ea-7baf-457d-a5b4-8068cb6bac21/Leonardo_Creative_An_oil_painting_of_a_cat_0.jpg">,           "nsfw": true,           "id": "5b710f5f-22de-4d27-8b5c-4eadc98bfc85",           "likeCount": 0,           "generated_image_variation_generics": \[]         },       ... ] ...`

If you’d like more rigid NSFW controls, please [contact us](https://leonardo.ai/contact-us/) for assistance, letting us know about your use case and requirements.

> 📘
> 
> Note
> 
> 
> ----------
> 
> Stable Diffusion v1.5 (SD1.5) and Platform Models based on SD1.5 are more prone to generate NSFW images. We recommend using SDXL based models for lower risk of NSFW images. Find out more about which Finetuned models use SDXL as base [here](/docs/elements-and-model-compatibility#finetuned-models-and-elements-compatibility-table).

Adding your own Image Moderation Layer

[](#adding-your-own-image-moderation-layer)
=====================================================================================

For use cases that require more control over the images generated, we recommend adding your own image moderation layer. You can implement your own system, leverage a more specialised third-party detection system, and/or keep a human in the loop to check against your guidelines.

Updated 27 days ago

* * *

[

Guide to the Webhook Callback Feature

](/docs/guide-to-the-webhook-callback-feature)[

Usage and Cost

](/docs/usage-and-cost)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Choosing a Finetuned Model](#choosing-a-finetuned-model)
    *   [Blocking at the Prompt Level](#blocking-at-the-prompt-level)
    *   [Flagging at the Response Level](#flagging-at-the-response-level)
    *   [Adding your own Image Moderation Layer](#adding-your-own-image-moderation-layer)
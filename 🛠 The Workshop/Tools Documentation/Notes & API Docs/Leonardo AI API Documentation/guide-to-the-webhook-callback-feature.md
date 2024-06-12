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

Guide to the Webhook Callback Feature
=====================================

Generating images will take a few seconds to complete. Instead of polling the [Get a Single Generation API endpoint](/reference/getgenerationbyid), it's more efficient to receive a message containing the links to your images and other metadata. To receive a message, you need to leverage the webhook callback feature.

Setting the Webhook Callback

[](#setting-the-webhook-callback)
=================================================================

When creating a production API key, you have the option to fill in your webhook callback URL and webhook callback API key.

![Webhook URL and webhook API key is set during production API key creation.](https://files.readme.io/32407f8-Screenshot_2023-11-09_at_11.30.27.png)

Webhook URL and webhook API key is set during production API key creation.

> 📘
> 
> Note
> 
> 
> ----------
> 
> *   The webhook callback URL and webhook callback API key are not required for creating an API key.
> *   The webhook callback URL field requires HTTPS.
> *   The webhook callback API key will be used for authenticating to your webhook callback. It will be added to the header of the request as`authorization: Bearer $yourWebhookCallbackApiKey`.
> *   To update your webhook callback URL and webhook callback API key, you need to create a new production API key with the new webhook details, then delete the old one after switching to the new API key.

Examining Leonardo's Request to your Webhook

[](#examining-leonardos-request-to-your-webhook)
================================================================================================

Many users find it useful to first study Leonardo's requests to their webhook using online tools like [Webhook.site](https://webhook.site/). Using such tools, you can analyse:

*   Which host and where in the world will the request come from so you can allow those requests?
*   What headers is Leonardo sending so you can make sure that your web servers, firewall, security tool, etc. do not block the requests?
*   Is your webhook callback API key being passed correctly?

![Sample screenshot for an online tool (Webhook.site) for examining HTTP requests.](https://files.readme.io/ef29782-Screenshot_2023-11-09_at_11.53.49.png)

Sample screenshot for an online tool (Webhook.site) for examining HTTP requests.

> 🚧
> 
> Not receiving messages in your webhook from Leonardo?
> 
> 
> -----------------------------------------------------------
> 
> *   Note that the webhook callback API key will be added to the header of the request as `authorization: Bearer $yourWebhookCallbackApiKey`. Please make sure that your system expects that header.
> *   Please check your system for anything that disallow traffic by IP address, location, headers, etc.
> *   Please check if your SSL Certificate is configured correctly. For example, run `openssl s_client -showcerts -connect YOUR_DOMAIN:443 -servername YOUR_DOMAIN` to check if your server's certificate and intermediate certificates are properly set.

Sample Request to your Webhook

[](#sample-request-to-your-webhook)
=====================================================================

Below is a sample request made by Leonardo to a webhook callback.

`curl -X 'POST' \  'https://webhook.site/cc21af5f-4caa-498e-8f26-20c664680b73' \  -H 'connection: close' \  -H 'host: webhook.site' \  -H 'accept-encoding: gzip, compress, deflate, br' \  -H 'content-length: 3166' \  -H 'user-agent: axios/1.4.0' \  -H 'authorization: Bearer abcd' \  -H 'content-type: application/json' \  -H 'accept: application/json, text/plain, */*' \  -d '{     "type": "image_generation.complete",     "object": "generation",     "timestamp": 1699490546932,     "api_version": "v1",     "data": {         "object": {             "id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",             "createdAt": "2023-11-09T00:42:22.707Z",             "updatedAt": "2023-11-09T00:42:26.740Z",             "userId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",             "public": false,             "flagged": false,             "nsfw": false,             "status": "COMPLETE",             "coreModel": "SD",             "guidanceScale": 7,             "imageHeight": 512,             "imageWidth": 512,             "inferenceSteps": 30,             "initGeneratedImageId": null,             "initImageId": null,             "initStrength": null,             "initType": null,             "initUpscaledImageId": null,             "modelId": "6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",             "negativePrompt": "",             "prompt": "An oil painting of a cat",             "quantity": 1,             "sdVersion": "v2",             "tiling": false,             "imageAspectRatio": null,             "tokenCost": 0,             "negativeStylePrompt": "",             "seed": "905778432",             "scheduler": "EULER_DISCRETE",             "presetStyle": null,             "promptMagic": false,             "canvasInitImageId": null,             "canvasMaskImageId": null,             "canvasRequest": false,             "api": true,             "poseImage2Image": false,             "imagePromptStrength": null,             "category": null,             "poseImage2ImageType": null,             "highContrast": false,             "apiDollarCost": "9",             "poseImage2ImageWeight": null,             "alchemy": null,             "contrastRatio": null,             "highResolution": null,             "expandedDomain": null,             "promptMagicVersion": null,             "unzoom": null,             "unzoomAmount": null,             "apiKeyId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",             "photoReal": false,             "promptMagicStrength": null,             "photoRealStrength": null,             "imageToImage": false,             "controlnetsUsed": false,             "model": {                 "id": "6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",                 "createdAt": "2023-01-06T01:02:38.315Z",                 "updatedAt": "2023-03-01T11:45:06.428Z",                 "name": "Leonardo Creative",                 "description": "An alternative finetune of SD 2.1 that brings a little more creative interpretation to the mix.",                 "public": true,                 "userId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",                 "flagged": false,                 "nsfw": false,                 "official": true,                 "status": "COMPLETE",                 "classPrompt": null,                 "coreModel": "SD",                 "initDatasetId": null,                 "instancePrompt": null,                 "sdVersion": "v2",                 "trainingEpoch": null,                 "trainingSteps": null,                 "tokenCost": null,                 "batchSize": 4,                 "learningRate": null,                 "type": "GENERAL",                 "modelHeight": 768,                 "modelWidth": 768,                 "leonardoInstancePrompt": null,                 "trainingStrength": "MEDIUM",                 "featured": false,                 "featuredImageId": null,                 "featuredPosition": 4,                 "api": false,                 "favouriteCount": 0,                 "imageCount": 2416039,                 "enhancedModeration": false,                 "apiDollarCost": null,                 "apiKeyId": null,                 "modelLRN": null             },             "images": [                 {                     "id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",                     "createdAt": "2023-11-09T00:42:26.733Z",                     "updatedAt": "2023-11-09T00:42:26.733Z",                     "userId": "ef8b8386-94f7-48d1-b10e-e87fd4dee6e6",                     "url": "https://cdn.leonardo.ai/users/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/generations/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/Leonardo_Creative_An_oil_painting_of_a_cat_0.jpg",                     "generationId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",                     "nobgId": null,                     "nsfw": false,                     "likeCount": 0,                     "trendingScore": 0,                     "public": false                 }             ],             "apiKey": {                 "id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",                 "createdAt": "2023-11-07T00:11:07.274Z",                 "userId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",                 "key": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",                 "lastUsed": "2023-11-07T00:11:07.274Z",                 "name": "webhook with key",                 "type": "PRODUCTION",                 "webhookCallbackUrl": "https://webhook.site/cc21af5f-4caa-498e-8f26-20c664680b73",                 "webhookCallbackApiKey": "abcd"             }         }     } } '`

Updated 7 months ago

* * *

[

Generate Enhanced Prompts

](/docs/generate-enhanced-prompts)[

Guide to Handling Not Safe for Work Image Generation (NSFW)

](/docs/guide-to-handling-not-safe-for-work-image-generation-nsfw)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Setting the Webhook Callback](#setting-the-webhook-callback)
    *   [Examining Leonardo's Request to your Webhook](#examining-leonardos-request-to-your-webhook)
    *   [Sample Request to your Webhook](#sample-request-to-your-webhook)
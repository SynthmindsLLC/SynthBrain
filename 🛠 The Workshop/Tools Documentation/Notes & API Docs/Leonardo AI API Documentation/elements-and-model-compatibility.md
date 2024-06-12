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

Elements and Model Compatibility
================================

Follow this recipe to generate Images with Elements via API

🖼️

Generate Images with Elements

Open Recipe

Which elements work with which models?

[](#which-elements-work-with-which-models)
====================================================================================

The elements that can be used with a finetuned model depend on its **base model**. You can find the base model of a finetuned model by checking the details of that model. To check the base model of a Platform Model, navigate to Finetuned Models and switch to platform Platform Models tab. Click on the model and then click on View More.

For example, if you click View More on DreamShaper v7 on the Leonardo web app, it will say that DreamShaper v7 is a Finetuned Model from the Base Model: Stable Diffusion v1.5.

![Finetuned Model details will indicate a Base Model ](https://files.readme.io/fa7a17c-Screenshot_2024-04-04_at_15.34.19.png)

Finetuned Model details will indicate a Base Model

You can then refer to the table below to see the compatible elements to Stable Diffusion v1.5 models.

Finetuned Models and Elements Compatibility Table

[](#finetuned-models-and-elements-compatibility-table)
===========================================================================================================

> 📘
> 
> Note
> 
> 
> ----------
> 
> Leonardo.Ai continuously releases new models and elements. The table below may not be the exhaustive list of base models, finetuned models, and elements available on the Leonardo platform. Please refer to the Leonardo web app, the [List Platform Models endpoint](/reference/get_platformmodels), and the [List Elements endpoint](/reference/get_elements) for a comprehensive list of what's available.

The following table is a list of base models, finetuned models, and compatible elements.

| Base Model | Finetuned Model | Element |
| --- | --- | --- |
| SDXL.LIGHTNING | Leonardo Anime XL  
Leonardo Lightning XL | Same as SDXL 0.9 |
| SDXL 1.0 | SDXL 1.0 | Same as SDXL 0.9 |
| SDXL 0.9 | Leonardo Kino XL  
Leonardo Vision XL  
Leonardo Diffusion XL  
AlbedoBase XL  
SDXL 0.9 | 3D Sculpt  
CGI Noir  
Colorful Scribbles  
Coloring Book  
Colorpop  
Cute Emotes  
Cybertech  
Dark Arts  
Digital Painting  
Dragon Scales  
Fantasy Icons  
Fiery Flames  
Folk Art Illustration  
Glasscore  
Glowwave  
Kids Illustration  
Modern Analog Photography  
Oldschool Comic  
Psychedelic Art  
Simple Flat Illustration  
Simple Icons  
Soft Pastel Anime  
Solarpunk  
Sparklecore  
Toon & Anime  
Vintage Christmas Illustration  
Vintage Photography |
| Stable Diffusion 1.5 | Absolute Reality v1.6  
Amulets  
Anime Pastel Dream  
Battle Axes  
Character Portraits  
Chest Armor  
Crystal Deposits  
Crystal Deposits Alternate  
Cute Animal Characters  
Cute Characters  
Christmas Stickers  
Deliberate 1.1  
Dreamshaper v7  
Dreamshaper v6  
Dreamshaper v5  
Dreamshaper 3.2  
Isometric Asteroid Tiles  
Isometric Fantasy  
Isometric Scifi Buildings  
Leonardo PhotoReal  
Leonardo Signature  
Magic Items, Magic Potions  
RPG 4.0  
RPG v5.0  
Shields  
Spirit Creatures  
Stable Diffusion 1.5 | Baroque  
Biopunk  
Celtic Punk  
Crystalline  
Ebony & Gold  
Gingerbread  
Glass & Steel  
Inferno  
Ivory & Gold  
Lunar Punk  
Pirate Punk  
Tiki  
Toxic Punk |
| Stable Diffusion 2.1 | Leonardo Diffusion  
Leonardo Select  
Leonardo Creative  
Stable Diffusion 2.1  
Vintage Style Photography | Surreal Collage |

Updated 28 days ago

* * *

[

API Error Messages

](/docs/api-error-messages)[

How to upload an image using a presigned URL

](/docs/how-to-upload-an-image-using-a-presigned-url)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Which elements work with which models?](#which-elements-work-with-which-models)
    *   [Finetuned Models and Elements Compatibility Table](#finetuned-models-and-elements-compatibility-table)

🦉

Recipe Title
============

Recipe Description

1.

cURL

​x

1{"success":true}
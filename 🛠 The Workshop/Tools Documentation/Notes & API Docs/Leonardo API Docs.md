# Create a Generation of Images

POSThttps://cloud.leonardo.ai/api/rest/v1/generations

This endpoint will generate images

RECIPES

🖼️

Generate your First Images

Open Recipe

🖼️

Generate Images Using PhotoReal

Open Recipe

🖼️

Generate Images Using Image Prompts

Open Recipe

🖼️

Generate with Image to Image Guidance using Uploaded Images

Open Recipe

🖼️

Generate with Image to Image Guidance using Generated Images

Open Recipe

🖼️

Generate Images Using Fantasy Avatar

Open Recipe

📸

Generate Images Using PhotoReal v2

Open Recipe

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

BODY PARAMS

Query parameters to be provided in the request body as a JSON object

alchemy

boolean | null

Enable to use Alchemy.

truefalse

contrastRatio

number | null

Contrast Ratio to use with Alchemy. Must be a float between 0 and 1 inclusive.

controlNet

boolean | null

Enable to use ControlNet. Requires an init image to be provided. Requires a model based on SD v1.5

truefalse

controlNetType

string | null

The type of ControlNet to use.

POSECANNYDEPTH

elements

array of objects or null | null

ADD OBJECT | NULL

expandedDomain

boolean | null

Enable to use the Expanded Domain feature of Alchemy.

truefalse

fantasyAvatar

boolean | null

Enable to use the Fantasy Avatar feature.

truefalse

guidance_scale

integer | null

How strongly the generation should reflect the prompt. 7 is recommended. Must be between 1 and 20.

height

integer | null

The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features.

highContrast

boolean | null

Enable to use the High Contrast feature of Prompt Magic. Note: Controls RAW mode. Set to false to enable RAW mode.

truefalse

highResolution

boolean | null

Enable to use the High Resolution feature of Prompt Magic.

truefalse

imagePrompts

array of strings or null | null

ADD STRING | NULL

imagePromptWeight

number | null

init_generation_image_id

string | null

The ID of an existing image to use in image2image.

init_image_id

string | null

The ID of an Init Image to use in image2image.

init_strength

number | null

How strongly the generated images should reflect the original image in image2image. Must be a float between 0.1 and 0.9.

modelId

string | null

The model ID used for image generation. If not provided, uses sd_version to determine the version of Stable Diffusion to use. In-app, model IDs are under the Finetune Models menu. Click on the platform model or your custom model, then click View More. For platform models, you can also use the List Platform Models API.

negative_prompt

string | null

The negative prompt used for the image generation

nsfw

boolean | null

Not Safe For Work Flag.

truefalse

num_images

integer | null

The number of images to generate. Must be between 1 and 8. If either width or height is over 768, must be between 1 and 4.

num_inference_steps

integer | null

The number of inference steps to use for the generation. Must be between 30 and 60.

photoReal

boolean | null

Enable the photoReal feature. Requires enabling alchemy and unspecifying modelId (for photoRealVersion V1).

truefalse

photoRealVersion

string | null

The version of photoReal to use. Must be v1 or v2.

photoRealStrength

number | null

Depth of field of photoReal. Must be 0.55 for low, 0.5 for medium, or 0.45 for high. Defaults to 0.55 if not specified.

presetStyle

string | null

The style to generate images with. When photoReal is enabled, use CINEMATIC, CREATIVE, VIBRANT, or NONE. When alchemy is disabled, use LEONARDO or NONE. When alchemy is enabled, use ANIME, CREATIVE, DYNAMIC, ENVIRONMENT, GENERAL, ILLUSTRATION, PHOTOGRAPHY, RAYTRACED, RENDER_3D, SKETCH_BW, SKETCH_COLOR, or NONE.

ANIMECINEMATICCREATIVEDYNAMICENVIRONMENTGENERALILLUSTRATIONLEONARDONONEPHOTOGRAPHYRAYTRACEDRENDER_3DSKETCH_BWSKETCH_COLORVIBRANT

prompt

string | null

required

The prompt used to generate images

promptMagic

boolean | null

Enable to use Prompt Magic.

truefalse

promptMagicStrength

number | null

Strength of prompt magic. Must be a float between 0.1 and 1.0

promptMagicVersion

string | null

Prompt magic version v2 or v3, for use when promptMagic: true

public

boolean | null

Whether the generated images should show in the community feed.

truefalse

scheduler

string | null

The scheduler to generate images with. Defaults to EULER_DISCRETE if not specified.

KLMSEULER_ANCESTRAL_DISCRETEEULER_DISCRETEDDIMDPM_SOLVERPNDMLEONARDO

sd_version

string | null

The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models

v1_5v2v3SDXL_0_8SDXL_0_9SDXL_1_0SDXL_LIGHTNING

seed

integer | null

tiling

boolean | null

Whether the generated images should tile on all axis.

truefalse

transparency

string | null

Which type of transparency this image should use

Default: `disabled`

disabledforeground_only

unzoom

boolean | null

Whether the generated images should be unzoomed (requires unzoomAmount and init_image_id to be set).

truefalse

unzoomAmount

number | null

How much the image should be unzoomed (requires an init_image_id and unzoom to be set to true).

upscaleRatio

number | null

How much the image should be upscaled. (Enterprise Only)

weighting

number | null

How much weighting to use for generation.

width

integer | null

The input width of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features.

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.createGeneration({
  height: 512,
  modelId: '6bef9f1b-29cb-40c7-b9df-32b51c1f67d3',
  prompt: 'An oil painting of a cat',
  transparency: 'disabled',
  width: 512
})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));


# Get a Single Generation

GEThttps://cloud.leonardo.ai/api/rest/v1/generations/{id}

This endpoint will provide information about a specific generation

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

METADATA

id

string

required

The ID of the generation to return.

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.getGenerationById({id: 'id'})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

# Create Texture Generation

POSThttps://cloud.leonardo.ai/api/rest/v1/generations-texture

This endpoint will generate a texture generation.

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

BODY PARAMS

Query parameters can also be provided in the request body as a JSON object

front_rotation_offset

integer | null

modelAssetId

string | null

negative_prompt

string | null

preview

boolean | null

truefalse

preview_direction

string | null

prompt

string | null

sd_version

string | null

seed

integer | null

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.createTextureGeneration()
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

# Create SVD Motion Generation

POSThttps://cloud.leonardo.ai/api/rest/v1/generations-motion-svd

This endpoint will generate a SVD motion generation.

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

BODY PARAMS

Query parameters can also be provided in the request body as a JSON object

imageId

string | null

required

The ID of the image, supports generated images, variation images, and init images.

isPublic

boolean | null

Whether the generation is public or not

truefalse

isInitImage

boolean | null

If it is an init image uploaded by the user. This image is uploaded from endpoint: Upload init image.

truefalse

isVariation

boolean | null

If it is a variation image.

truefalse

motionStrength

integer | null

The motion strength.

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.createSVDMotionGeneration()
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

# Create LCM Generation

POSThttps://cloud.leonardo.ai/api/rest/v1/generations-lcm

This endpoint will generate a LCM image generation.

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

BODY PARAMS

Query parameters can also be provided in the request body as a JSON object

imageDataUrl

string | null

required

Image data used to generate image. In base64 format. Prefix: `data:image/jpeg;base64,`

prompt

string | null

required

The prompt used to generate images

guidance

number | null

How strongly the generation should reflect the prompt. Must be a float between 0.5 and 20.

strength

number | null

How strongly the generated images should reflect the original image supplied in imageDataUrl. Must be a float between 0.1 and 1.

requestTimestamp

string | null

style

string | null

The style to generate LCM images with.

ANIMECINEMATICDIGITAL_ARTDYNAMICENVIRONMENTFANTASY_ARTILLUSTRATIONPHOTOGRAPHYRENDER_3DRAYTRACEDSKETCH_BWSKETCH_COLORVIBRANTNONE

steps

integer | null

The number of steps to use for the generation. Must be between 4 and 16.

width

integer | null

The output width of the image. Must be 512, 640 or 1024.

height

integer | null

The output width of the image. Must be 512, 640 or 1024.

seed

integer | null

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.createLCMGeneration({width: 512, height: 512})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

Perform instant refine on a LCM image
POST
https://cloud.leonardo.ai/api/rest/v1/lcm-instant-refine
This endpoint will perform instant refine on a LCM image

LOG IN TO SEE FULL REQUEST HISTORY
TIME	STATUS	USER AGENT	
Make a request to see history.
0 Requests This Month

BODY PARAMS
Query parameters can also be provided in the request body as a JSON object

imageDataUrl
string | null
required
Image data used to generate image. In base64 format. Prefix: data:image/jpeg;base64,

prompt
string | null
required
The prompt used to generate images

guidance
number | null
How strongly the generation should reflect the prompt. Must be a float between 0.5 and 20.

strength
number | null
How strongly the generated images should reflect the original image supplied in imageDataUrl. Must be a float between 0.1 and 1.

requestTimestamp
string | null
style
string | null
The style to generate LCM images with.


steps
integer | null
The number of steps to use for the generation. Must be between 4 and 16.

width
integer | null
The output width of the image. Must be 512, 640 or 1024.

512
height
integer | null
The output width of the image. Must be 512, 640 or 1024.

512
seed
integer | null

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.performInstantRefine({width: 512, height: 512})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

# Perform Alchemy Upscale on a LCM image

POSThttps://cloud.leonardo.ai/api/rest/v1/lcm-upscale

This endpoint will perform Alchemy Upscale on a LCM image

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

BODY PARAMS

Query parameters can also be provided in the request body as a JSON object

imageDataUrl

string | null

required

Image data used to generate image. In base64 format. Prefix: `data:image/jpeg;base64,`

prompt

string | null

required

The prompt used to generate images

guidance

number | null

How strongly the generation should reflect the prompt. Must be a float between 0.5 and 20.

strength

number | null

How strongly the generated images should reflect the original image supplied in imageDataUrl. Must be a float between 0.1 and 1.

requestTimestamp

string | null

style

string | null

The style to generate LCM images with.

ANIMECINEMATICDIGITAL_ARTDYNAMICENVIRONMENTFANTASY_ARTILLUSTRATIONPHOTOGRAPHYRENDER_3DRAYTRACEDSKETCH_BWSKETCH_COLORVIBRANTNONE

steps

integer | null

The number of steps to use for the generation. Must be between 4 and 16.

width

integer | null

The output width of the image. Must be 512, 640 or 1024.

height

integer | null

The output width of the image. Must be 512, 640 or 1024.

seed

integer | null

refineCreative

boolean | null

Refine creative

truefalse

refineStrength

number | null

Must be a float between 0.5 and 0.9.

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.performAlchemyUpscaleLCM({width: 512, height: 512})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

# Get texture generations by 3D Model ID

GEThttps://cloud.leonardo.ai/api/rest/v1/generations-texture/model/{modelId}

This endpoint gets the specific texture generations by the 3d model id.

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

BODY PARAMS

Query parameters can also be provided in the request body as a JSON object

limit

integer | null

modelId

string | null

offset

integer | null

METADATA

modelId

string

required

_"modelId" is required (enter it either in parameters or request body)_

offset

integer

limit

integer

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.getTextureGenerationsByModelId({offset: '0', limit: '10', modelId: 'modelId'})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

# Upload init image

POSThttps://cloud.leonardo.ai/api/rest/v1/init-image

This endpoint returns presigned details to upload an init image to S3

RECIPES

🖼️

Generate Images Using Image Prompts

Open Recipe

🎞️

Generate Motion Using Uploaded Images

Open Recipe

🖼️

Generate with Image to Image Guidance using Uploaded Images

Open Recipe

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

Detailed instructions for using this endpoint are available in the guide: [How to upload an image using a presigned URL](https://docs.leonardo.ai/docs/how-to-upload-an-image-using-a-presigned-url).

BODY PARAMS

Query parameters provided in the request body as a JSON object

extension

string | null

required

Has to be png, jpg, jpeg, or webp.

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.uploadInitImage()
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

# Get single init image

GEThttps://cloud.leonardo.ai/api/rest/v1/init-image/{id}

This endpoint will return a single init image

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

METADATA

id

string

required

_"id" is required_

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.getInitImageById({id: 'id'})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

# Delete init image

DELETEhttps://cloud.leonardo.ai/api/rest/v1/init-image/{id}

This endpoint deletes an init image

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

METADATA

id

string

required

_"id" is required_

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.deleteInitImageById({id: 'id'})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));

# Create upscale

POSThttps://cloud.leonardo.ai/api/rest/v1/variations/upscale

This endpoint will create an upscale for the provided image ID

LOG IN TO SEE FULL REQUEST HISTORY

|TIME|STATUS|USER AGENT||
|:--|:--|:--|:--|
|Make a request to see history.|   |   |   |

0 Requests This Month

BODY PARAMS

Query parameters are provided in the request body as a JSON object

id

string | null

required

const sdk = require('api')('@leonardoai/v1.0#1d9166glulxqhcv');

sdk.createVariationUpscale()
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));
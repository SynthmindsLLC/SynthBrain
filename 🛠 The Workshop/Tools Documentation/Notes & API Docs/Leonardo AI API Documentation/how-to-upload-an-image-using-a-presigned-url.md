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

How to upload an image using a presigned URL
============================================

Introduction

[](#introduction)
---------------------------------

The API endpoints to upload init images or dataset images return a presigned URL. Use this URL to upload the image file to S3.

The overall flow is:

*   Use the API endpoint to create a new init or dataset image. The response returned will contain a presigned URL which you can use to upload the image file.
*   Use the presigned URL returned to make a post call that contains all the fields from the previous response. This call must be done with multipart file instead of `application/json`. The presigned URL expires in 2 minutes, so the method must be run within the first 2 minutes.
*   Add a new param to the form that would be the binary file. This needs to be a data stream or a buffer or bytes. It cannot accept a different encoding, nor base64.
*   Note that the image must be in the format of the `extension` provided to the init image method. It also needs to be scaled to respect the maximum boundaries and aspect ratio that is going to be sent in the generation method. Otherwise it will look deformed.
*   Finally, invoke the generation method with the init image `id` returned by the init image method

Here is an example response when using an image upload API endpoint:

JSON

`{   "uploadDatasetImage": {     "id": "1234-1234-1234-1234", //this is the init image ID to use in the final step     "fields": "{\"example\": \"fields\"}",     "key": "users/1234-1234-1234-1234/datasets/1234-1234-1234-1234/images/1234-1234-1234-1234/example.png",     "url": "https://example.com/"   } }`

Here is an example implementation where the image is uploaded based on the `response` above:

TypeScriptPython

`const uploadDatasetImage = async (file: File, response: any) => { 	const rawFields = response.uploadDatasetImage.fields; 	const fields = JSON.parse(rawFields); 	const url = response.uploadDatasetImage.url;  	const formData = new FormData();  	Object.entries({ ...fields, file }).forEach(([key, value]) => { 		formData.append(key, value as string); 	})  	const request = new XMLHttpRequest(); 	request.open('POST', url);  	const result = await request.send(formData); }`

`import json import requests  def upload_dataset_image(image_file_path: str, response: requests.models.Response) -> requests.models.Response:     """      Upload an image file to a Leonardo.ai dataset via a presigned URL.             :image_file_path: Path to an image file to upload     :response: Response to a request to the datasets/{datasetId}/upload endpoint     """             fields = json.loads(response.json()['uploadDatasetImage']['fields'])     url = response.json()['uploadDatasetImage']['url']     files = {'file': open(image_file_path, 'rb')}             return requests.post(url, data=fields, files=files)`

Updated about 1 year ago

* * *

[

Elements and Model Compatibility

](/docs/elements-and-model-compatibility)[

Need More Support?

](/docs/need-more-support)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Introduction](#introduction)
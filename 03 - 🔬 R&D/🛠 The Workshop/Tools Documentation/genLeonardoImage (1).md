~~~json
{
  "name": "genLeonardoImage",
  "description": "Generate and optionally upscale an image using the Leonardo AI API.",
  "parameters": {
    "type": "object",
    "properties": {
      "prompt": {
        "type": "string",
        "description": "The prompt used to generate the image."
      },
      "width": {
        "type": "integer",
        "description": "The width of the generated image. Must be between 32 and 1024 and be a multiple of 8.",
        "default": 512
      },
      "height": {
        "type": "integer",
        "description": "The height of the generated image. Must be between 32 and 1024 and be a multiple of 8.",
        "default": 512
      },
      "upscale": {
        "type": "boolean",
        "description": "Whether to upscale the generated image.",
        "default": false
      },
      "modelId": {
        "type": "string",
        "description": "The model ID used for image generation.",
        "default": null
      },
      "numInferenceSteps": {
        "type": "integer",
        "description": "The number of inference steps to use for the generation. Must be between 10 and 50.",
        "default": 50
      },
      "guidanceScale": {
        "type": "number",
        "description": "How strongly the generation should reflect the prompt. Must be between 1 and 20.",
        "default": 7
      }
    },
    "required": ["prompt"]
  }
}
~~~

~~~js
async function genLeonardoImage({ prompt, width = 512, height = 512, modelId = null, numInferenceSteps = 50, guidanceScale = 7 }) {
  try {
    const apiKey = "a03535d5-50d7-42ea-a5d3-53209c450131";
    const baseUrl = "https://cloud.leonardo.ai/api/rest/v1";

    // Ensure guidanceScale is an integer within the allowed range
    const parsedGuidanceScale = parseInt(guidanceScale);
    if (isNaN(parsedGuidanceScale) || parsedGuidanceScale < 1 || parsedGuidanceScale > 20) {
      throw new Error("guidanceScale must be an integer between 1 and 20");
    }

    // Generate the image
    const generateResponse = await fetch(`${baseUrl}/generations`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        prompt,
        width,
        height,
        modelId,
        num_inference_steps: numInferenceSteps,
        guidance_scale: parsedGuidanceScale,
        num_images: 1,
      }),
    });

    const generateData = await generateResponse.json();
    if (!generateResponse.ok) {
      console.error("Error generating Leonardo image:", generateData);
      throw new Error("Error generating Leonardo image");
    }

    const imageId = generateData.sdGenerationJob?.generationId;
    if (!imageId) {
      console.error("Missing generationId in the API response:", generateData);
      throw new Error("Missing generationId in the API response");
    }

    // Get the image URL
    async function getImageUrl(baseUrl, apiKey, imageId) {
      const maxAttempts = 30;
      const delay = 2000; // 2 seconds

      for (let attempt = 1; attempt <= maxAttempts; attempt++) {
        const imageResponse = await fetch(`${baseUrl}/generations/${imageId}`, {
          headers: { Authorization: `Bearer ${apiKey}` },
        });

        const imageData = await imageResponse.json();
        if (!imageResponse.ok) {
          console.error("Error fetching Leonardo image URL:", imageData);
          throw new Error("Error fetching Leonardo image URL");
        }

        console.log(`Attempt ${attempt}: Image data:`, JSON.stringify(imageData, null, 2));

        const generatedImages = imageData.generations_by_pk?.generated_images;
        if (generatedImages && generatedImages.length > 0) {
          const imageUrl = generatedImages[0].url;
          if (imageUrl) {
            return imageUrl;
          }
        }

        console.log(`Image URL not available yet. Waiting for ${delay}ms before trying again.`);
        await new Promise(resolve => setTimeout(resolve, delay));
      }

      throw new Error("Max attempts reached. Image URL not found.");
    }

    const imageUrl = await getImageUrl(baseUrl, apiKey, imageId);

    // Save the image to the vault
    const response = await fetch(imageUrl);
    const blob = await response.blob();
    const buffer = await blob.arrayBuffer();
    const data = new Uint8Array(buffer);

    const timestamp = Date.now();
    const fileName = `leonardo_${timestamp}.png`;
    await app.vault.createBinary(fileName, data);

    // Return the markdown image link
    const imageLink = `![${prompt}](${fileName})`;

    // Return the generated image link along with the prompt to upscale
    return `${imageLink}\n\nDo you want to upscale the generated image? (Type 'yes' to upscale or anything else to skip)`;
  } catch (error) {
    console.error("Error in genLeonardoImage:", error);
    throw error;
  }
}
~~~
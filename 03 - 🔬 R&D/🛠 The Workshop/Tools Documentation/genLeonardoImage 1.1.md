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
      "numInferenceSteps": {
        "type": "integer",
        "description": "The number of inference steps to use for the generation. Must be between 10 and 50.",
        "default": 50
      },
      "guidanceScale": {
        "type": "number",
        "description": "How strongly the generation should reflect the prompt. Must be between 1 and 20.",
        "default": 7
      },
      "scheduler": {
        "type": "string",
        "description": "The scheduler to generate images with.",
        "default": "EULER_DISCRETE"
      },
      "presetStyle": {
        "type": "string",
        "description": "The style to generate images with.",
        "default": null
      },
      "sdVersion": {
        "type": "string",
        "description": "The version of Stable Diffusion to use.",
        "default": "v1_5"
      },
      "modelId": {
        "type": "string",
        "description": "The ID of the model to use for image generation."
      },
      "alchemy": {
        "type": "boolean",
        "description": "Whether to use alchemy for image generation.",
        "default": false
      },
      "photoRealV2": {
        "type": "boolean",
        "description": "Whether to use PhotoReal v2 for image generation.",
        "default": false
      }
    },
    "required": ["prompt"]
  }
}
~~~

~~~js
async function genLeonardoImage({ prompt, numInferenceSteps = 50, guidanceScale = 7, scheduler = "EULER_DISCRETE", presetStyle = null, sdVersion = "v1_5" }) {
  try {
    const apiKey = "a03535d5-50d7-42ea-a5d3-53209c450131";
    const baseUrl = "https://cloud.leonardo.ai/api/rest/v1";

    // Ensure guidanceScale is a number within the allowed range
    const parsedGuidanceScale = parseFloat(guidanceScale);
    if (isNaN(parsedGuidanceScale) || parsedGuidanceScale < 1 || parsedGuidanceScale > 20) {
      throw new Error("guidanceScale must be a number between 1 and 20");
    }

    // Hardcoded list of available models
    const availableModels = [
	    {
        id: "e71a1c2f-4f80-4800-934f-2c68979d8cc8",
        name: "Leonardo Anime XL",
        description: "A new high-speed Anime-focused model that excels at a range of anime, illustrative, and CG styles.",
        nsfw: false,
        featured: false,
        generated_image: {
          id: "4fc2c951-5a86-4fc1-9ff2-d72a2213bb14",
          url: "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/16cbffcc-8672-47d6-8738-d22167dcea3f/Default_A_lush_vibrant_anime_hero_figure_emerges_from_the_shad_0.jpg"
        }
      },
      {
        id: "b24e16ff-06e3-43eb-8d33-4416c2d75876",
        name: "Leonardo Lightning XL",
        description: "Our new high-speed generalist image gen model. Great at everything from photorealism to painterly styles.",
        nsfw: false,
        featured: false,
        generated_image: {
          id: "e1d0556b-7ccd-4568-8b1e-7d33e9db9e82",
          url: "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/334022a8-7cea-43f9-a8a0-b9c2d232f32f/Default_an_ageing_astronaut_piloting_an_old_spaceship_0.jpg"
        }
      },
      {
        id: "aa77f04e-3eec-4034-9c07-d0f619684628",
        name: "Leonardo Kino XL",
        description: "A model with a strong focus on cinematic outputs. Excels at wider aspect ratios, and does not need a negative prompt.",
        nsfw: false,
        featured: false,
        generated_image: {
          id: "af8d108e-82c9-4330-8301-b3ef3165b637",
          url: "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/38c684e6-702f-446a-b99b-649462d6a3d6/Leonardo_Kino_XL_cinematic_photo_of_a_surreal_adventurer_on_a_2.jpg"
        }
      },
      {
        id: "5c232a9e-9061-4777-980a-ddc8e65647c6",
        name: "Leonardo Vision XL",
        description: "A versatile model that excels at realism and photography. Better results with longer prompts.",
        nsfw: false,
        featured: true,
        generated_image: {
          id: "b65405dd-9096-42ba-aa59-704e4b0859c0",
          url: "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/bc0a7117-ad5e-4754-8648-6412cc554478/Leonardo_Vision_XL_A_gritty_unedited_photograph_perfectly_capt_2.jpg"
        }
      },
      {
        id: "1e60896f-3c26-4296-8ecc-53e2afecc132",
        name: "Leonardo Diffusion XL",
        description: "The next phase of the core Leonardo model. Stunning outputs, even with short prompts.",
        nsfw: false,
        featured: true,
        generated_image: {
          id: "f85f70f5-ceb2-4665-8089-241ce6f19ea8",
          url: "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/9ea08719-5fd1-4df7-9adc-5218637cba17/Leonardo_Diffusion_XL_a_brain_suspended_in_midair_bathed_in_a_1.jpg"
        }
      },
      {
        id: "2067ae52-33fd-4a82-bb92-c2c55e7d2786",
        name: "AlbedoBase XL",
        description: "A great generalist model that tends towards more CG artistic outputs. By alebdobond.",
        nsfw: false,
        featured: true,
        generated_image: {
          id: "2590401b-a844-4b79-b0fa-8c44bb54eda0",
          url: "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/6a441e3f-594d-442f-b70b-0d867a09e589/AlbedoBase_XL_A_sleek_and_menacing_dwarf_his_metallic_body_gle_3.jpg"
        }
      }
    ];

    // Extract width, height, and model from the prompt
    const widthMatch = prompt.match(/width:\s*(\d+)/i);
    const heightMatch = prompt.match(/height:\s*(\d+)/i);
    const modelMatch = prompt.match(/model:\s*(\w+)/i);

    const width = widthMatch ? parseInt(widthMatch[1]) : 512;
    const height = heightMatch ? parseInt(heightMatch[1]) : 512;
    const modelName = modelMatch ? modelMatch[1].toLowerCase() : null;

    // Validate width and height
    if (width < 32 || width > 1024 || width % 8 !== 0) {
      throw new Error("width must be between 32 and 1024 and be a multiple of 8");
    }
    if (height < 32 || height > 1024 || height % 8 !== 0) {
      throw new Error("height must be between 32 and 1024 and be a multiple of 8");
    }

    // Find the specified model or choose an appropriate model based on the user's prompt
    let modelId;
    if (modelName) {
      const specifiedModel = availableModels.find(model => model.name.toLowerCase().includes(modelName));
      if (specifiedModel) {
        modelId = specifiedModel.id;
      }
    }
    if (!modelId) {
      modelId = await chooseModel(availableModels, prompt);
    }

    // Check if photoreal is requested in the prompt
    const photorealMatch = prompt.match(/photoreal:\s*(true|false)/i);
    const photoreal = photorealMatch ? photorealMatch[1].toLowerCase() === "true" : false;

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
        scheduler,
        presetStyle,
        sd_version: sdVersion,
        photoReal: photoreal,
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

async function chooseModel(availableModels, prompt) {
  // Convert the prompt to lowercase for case-insensitive matching
  const lowercasePrompt = prompt.toLowerCase();

  // Define keywords or patterns for each model
  const modelKeywords = {
    "e71a1c2f-4f80-4800-934f-2c68979d8cc8": ["anime", "xl", "extra large"],
    "b24e16ff-06e3-43eb-8d33-4416c2d75876": ["lightning", "xl", "extra large", "generalist"],
    "aa77f04e-3eec-4034-9c07-d0f619684628": ["kino", "xl", "extra large", "cinematic"],
    "5c232a9e-9061-4777-980a-ddc8e65647c6": ["vision", "xl", "extra large", "realism", "photography"],
    "1e60896f-3c26-4296-8ecc-53e2afecc132": ["diffusion", "xl", "extra large", "core"],
    "2067ae52-33fd-4a82-bb92-c2c55e7d2786": ["albedo", "xl", "extra large", "cg", "artistic"]
  };

  // Find the model that best matches the prompt based on keywords
  const matchedModel = availableModels.find(model => {
    const keywords = modelKeywords[model.id];
    return keywords.some(keyword => lowercasePrompt.includes(keyword));
  });

  // If a matching model is found, return its ID
  if (matchedModel) {
    return matchedModel.id;
  }

  // If no specific model matches the prompt, select a default model
  const defaultModel = availableModels.find(model => model.name === "Leonardo Diffusion XL");
  return defaultModel ? defaultModel.id : availableModels[0].id;
}
~~~
# Overview

Obsistants is an innovative plug-in for Obsidian, a popular note-taking application. It enhances Obsidian by enabling integration with various large language models like ChatGPT. This is achieved through a unique setup where users can add 'tools' to Obsidian through notes, defined by a JSON schema and accompanied by JavaScript code. These tools can then interact with APIs or perform actions directly within the Obsidian vault.

Here's how it works:
- **Tool Selection**: Users toggle tools via filenames. However, only versions included in the filename are recognized by Obsistants for selection. If the tool's other names don't match, it might lead to errors.
- **JSON Schema**: Acts as the identifier for the Assistant when making API requests to OpenAI, defining how the tool should interact with the large language models.
- **JavaScript Execution**: The part of the tool that executes code within the Obsistants plugin, enabling dynamic interactions within the Obsidian environment.

A key aspect to note is the parallel execution of these tools. Because of this, the order of operations is crucial. For example, attempting to execute a `readTools` function and a `writeFile` function simultaneously will not work as intended because the output of `readTools` won't be ready in time to be written by `writeFile`.

To circumvent this, you could:
1. Sequence operations across messages—first, execute `readTools` to read data, and in a subsequent message, use `writeFile` to write about the tools.
2. Combine operations in a single function, ensuring synchronous execution. For instance, a custom function could read tool data and then write a note, bypassing the parallel execution issue.

Tool interaction primarily involves parameter setting—specifying what information is required for a tool to run properly. For instance, a weather tool would need latitude and longitude to fetch the correct forecast.

Lastly, this plugin allows for the usage of unstructured data to prompt further actions, enabling a flexible interaction model where the user's input can directly influence tool execution. This makes Obsistants a powerful addition to Obsidian for automating tasks and integrating with external data sources.

# Obsistant Feedback and Roadmap

For an update on the roadmap you can access it in the [github here](https://github.com/Forgetabyteit/obsistants/blob/master/ROADMAP.md).

There is no need to include enhancements that are already in the roadmap.

For any issues or enhancements, leave a comment in the [Issues tab](https://github.com/Forgetabyteit/obsistants/issues).

Be sure to mark it properly as either an **enhancement** or an **issue**.
# Creating Obsistant Tools

Obsistant tools are powerful extensions that enhance the functionality of the Obsidian note-taking app. They allow users to perform various tasks and interact with external APIs directly within Obsidian. In this guide, we'll explore the process of creating Obsistant tools, including best practices and tips to ensure a smooth development experience.

## Prerequisites
Before diving into creating Obsistant tools, make sure you have the following:
- A basic understanding of JavaScript programming language
- Familiarity with Obsidian and its plugin ecosystem
- Access to the Obsistant plugin and its documentation

## Step 1: Define the Tool's Purpose
Start by clearly defining the purpose and functionality of your Obsistant tool. Consider the following questions:
- What problem does the tool solve?
- What are the key features and capabilities of the tool?
- How will users interact with the tool within Obsidian?

Having a clear understanding of the tool's purpose will guide your development process and help you make informed decisions along the way.

## Step 2: Design the JSON Schema
Create a JSON schema that defines the structure and parameters of your Obsistant tool. The JSON schema serves as a blueprint for the tool and specifies the input parameters required from the user.

Consider the following when designing the JSON schema:
- Use descriptive names for the tool and its parameters
- Specify the data types of the parameters (e.g., string, integer, boolean)
- Provide clear descriptions for each parameter to guide the user
- Indicate which parameters are required and which are optional
- Define default values for optional parameters when applicable

Example JSON Schema:
```json
{
  "name": "myTool",
  "description": "A tool to perform a specific task",
  "parameters": {
    "type": "object",
    "properties": {
      "param1": {
        "type": "string",
        "description": "The first parameter"
      },
      "param2": {
        "type": "integer",
        "description": "The second parameter",
        "default": 10
      }
    },
    "required": ["param1"]
  }
}
```

## Step 3: Implement the JavaScript Code
Write the JavaScript code that implements the functionality of your Obsistant tool. The JavaScript code will be executed when the tool is invoked within Obsidian.

Consider the following best practices when implementing the JavaScript code:
- Use asynchronous programming techniques (e.g., async/await) for handling asynchronous operations
- Handle errors gracefully and provide informative error messages
- Use modular and reusable code practices
- Follow JavaScript coding conventions and style guides
- Perform necessary data validation and sanitization
- Implement robust error handling and logging mechanisms
- Consider edge cases and handle them appropriately

Example JavaScript Code:
```js
async function myTool({ param1, param2 }) {
  try {
    // Perform the tool's functionality
    const result = await someAsyncOperation(param1, param2);
    
    // Return the result or perform further processing
    return `The result is: ${result}`;
  } catch (error) {
    console.error("Error in myTool:", error);
    throw error;
  }
}
```

## Step 4: Handle User Interactions
Design the user interaction flow for your Obsistant tool. Consider how users will provide input, trigger actions, and receive output.

Some common interaction patterns include:
- Prompting the user for input using natural language or specific commands
- Providing buttons or clickable elements for users to trigger actions
- Displaying output or results within Obsidian's user interface
- Allowing users to configure settings or preferences

Example User Interaction:
```js
async function handleUserInput(input) {
  if (input.toLowerCase() === "/run-tool") {
    const param1 = await promptUserForParam1();
    const param2 = 10; // Default value
    
    const result = await myTool({ param1, param2 });
    displayResult(result);
  }
}

function promptUserForParam1() {
  // Prompt the user for param1 using Obsidian's UI
  // Return the user's input
}

function displayResult(result) {
  // Display the result to the user using Obsidian's UI
}
```

## Step 5: Test and Debug
Thoroughly test your Obsistant tool to ensure it functions as expected. Consider the following testing strategies:
- Test various input scenarios, including valid and invalid inputs
- Verify that the tool handles errors and edge cases properly
- Test the tool's integration with Obsidian and ensure smooth user interactions
- Perform end-to-end testing to validate the complete flow of the tool

Use debugging techniques to identify and fix any issues that arise during testing. Obsidian's developer console and JavaScript debugging tools can be helpful for troubleshooting.

## Step 6: Document and Share
Create documentation for your Obsistant tool to help users understand its purpose, usage, and any necessary setup or configuration steps. Include examples and explanations of the tool's parameters and expected outputs.

Consider sharing your Obsistant tool with the community if it provides value to others. You can contribute to the Obsistant plugin's ecosystem or share your tool through Obsidian's community forums or repositories.

## Best Practices
Here are some additional best practices to keep in mind when creating Obsistant tools:
- Keep the tool focused on a specific task or functionality
- Optimize for performance and efficiency
- Handle rate limits and API constraints when interacting with external services
- Implement caching mechanisms to avoid unnecessary API calls
- Respect user privacy and handle sensitive data securely
- Provide clear and concise error messages to assist users in troubleshooting
- Regularly update and maintain your tool to ensure compatibility with Obsidian and its ecosystem

## Conclusion
Creating Obsistant tools allows you to extend the capabilities of Obsidian and provide powerful functionality to users. By following the steps outlined in this guide and adhering to best practices, you can develop robust and user-friendly tools that enhance the Obsidian experience.

Remember to iterate and refine your tools based on user feedback and evolving requirements. Continuously improve and expand your tools to provide greater value to the Obsidian community.

Happy tool building!

# Code Snippets for Interacting with the vault or Obsistants

![[Pasted image 20240417190251.png]]

## Get the Active ID Thread

```
app.plugins.getPlugin("obsistants").settings.activeThreadId
```  
Returns the active threadID.

e.g. 

```js
let chatID = app.plugins.getPlugin("obsistants").settings.activeThreadId;
``` 

Then that is also the note name, so you can then get into the obsistants folder and get the chat and just parse the JSON from it. Simple for the AI to write that code.  
  
Once you have it parsed as JSON you can do whatever you need to with the whole chat programmatically. If you write back to the chat note you will update the chatUI's messages, too.

## Opening Files
```js
async function openFile(filepath, newLeaf = false) {
  const leaf = app.workspace.getLeaf(newLeaf);
  await leaf.openFile(app.vault.getAbstractFileByPath(filepath));
}
```

## Creating Files
```js
async function createFile(filepath, content = '') {
  const parts = filepath.split('/');
  const dir = parts.slice(0, parts.length - 1).join('/');
  if (parts.length > 1 && !(app.vault.getAbstractFileByPath(dir) instanceof TFolder)) {
    await app.vault.createFolder(dir);
  }
  await app.vault.create(filepath, content);
}
```

## Modifying Files
```js
async function modifyFile(filepath, content) {
  const file = app.vault.getAbstractFileByPath(filepath);
  if (file instanceof TFile) {
    await app.vault.modify(file, content);
  }
}
```

## Appending Content to Files
```js
async function appendToFile(filepath, content) {
  const file = app.vault.getAbstractFileByPath(filepath);
  if (file instanceof TFile) {
    const fileContent = await app.vault.read(file);
    const newContent = fileContent + '\n' + content;
    await app.vault.modify(file, newContent);
  }
}
```

## Prepending Content to Files

```js
async function prependToFile(filepath, content) {
  const file = app.vault.getAbstractFileByPath(filepath);
  if (file instanceof TFile) {
    const fileContent = await app.vault.read(file);
    const newContent = content + '\n' + fileContent;
    await app.vault.modify(file, newContent);
  }
}
```

## Setting Cursor Position
```js
function setCursorPosition(mode) {
  const view = app.workspace.getActiveViewOfType(MarkdownView);
  if (view) {
    const editor = view.editor;
    if (mode === 'append') {
      const lastLine = editor.lastLine();
      const lastLineLength = editor.getLine(lastLine).length;
      editor.setCursor({ ch: lastLineLength, line: lastLine });
    } else if (mode === 'prepend') {
      editor.setCursor({ ch: 0, line: 0 });
    }
  }
}
```

## Executing Commands
```js
function executeCommand(commandId) {
  app.commands.executeCommandById(commandId);
}

function executeCommandByName(commandName) {
  const command = app.commands.findCommand(commandName);
  if (command) {
    app.commands.executeCommand(command);
  }
}
```

## Handling Daily Notes

```js
async function getDailyNote(date) {
  const dailyNotesPlugin = app.internalPlugins.getPluginById('daily-notes');
  if (dailyNotesPlugin) {
    const dailyNote = await dailyNotesPlugin.instance.getDailyNoteForDate(date);
    return dailyNote;
  }
  return null;
}

async function createDailyNote(date) {
  const dailyNotesPlugin = app.internalPlugins.getPluginById('daily-notes');
  if (dailyNotesPlugin) {
    const dailyNote = await dailyNotesPlugin.instance.createDailyNote(date);
    return dailyNote;
  }
  return null;
}
```

# Example Tools

## DALLE
~~~json
{
  "name": "generateAndSaveDalle3Image",
  "description": "Generate an image using the DALLE3 API.",
  "parameters": {
    "type": "object",
    "properties": {
      "prompt": {
        "type": "string",
        "description": "A text description of the desired image(s). The maximum length is 4000 characters."
      },
      "size": {
        "type": "string",
        "description": "The size of the generated image. Must be one of '1024x1024', '1792x1024', or '1024x1792'.",
        "default": "1024x1024"
      },
      "style": {
        "type": "string",
        "description": "The style of the generated image. Must be one of 'vivid' or 'natural'.",
        "default": "vivid"
      }
    },
    "required": ["prompt"]
  }
}
~~~

~~~js
async function generateAndSaveDalle3Image({ prompt, size = "1024x1024", style = "vivid" }) {
  try {
    const apiKey = await app.plugins.getPlugin("obsistants").settings.apiKey;

    const response = await fetch("https://api.openai.com/v1/images/generations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model: "dall-e-3",
        prompt,
        n: 1,
        size,
        style,
        response_format: "b64_json",
      }),
    });

    const data = await response.json();

    if (response.ok) {
      const base64Image = data.data[0].b64_json;

      // Truncate the prompt to a maximum of 30 characters and remove invalid characters from the filename
      const timestamp = Date.now();
      const truncatedPrompt = prompt.slice(0, 30).replace(/[\\/:*?"<>|]/g, "_").replace(/\s/g, "_");
      const fileName = `${truncatedPrompt}_${timestamp}.png`;
      const filePath = `dalle3/${fileName}`;

      // Ensure the directory exists
      const dirs = filePath.split('/');
      let currentPath = '';

      for (const dir of dirs.slice(0, -1)) {
        currentPath += `${dir}/`;
        try {
          const dirExists = await app.vault.adapter.exists(currentPath);
          if (!dirExists) {
            await app.vault.createFolder(currentPath);
          }
        } catch (error) {
          console.error("Error checking or creating directory:", error);
          throw error;
        }
      }

      // Convert the base64 image to a Uint8Array
      const imageData = Uint8Array.from(atob(base64Image), c => c.charCodeAt(0));

      // Save the image file using the Uint8Array
      await app.vault.create(filePath, imageData);
      console.log("Image file saved successfully.");

      // Get the full system path of the saved image
      const fullPath = await app.vault.adapter.getFullPath(filePath);

      // Replace spaces with underscores in the full path
      const fullPathWithUnderscores = fullPath.replace(/\s/g, "_");

      // Return the markdown image using the full path with underscores and the truncated prompt
      return `![${truncatedPrompt}](${fullPathWithUnderscores})`;
    } else {
      console.error("Error generating DALLE3 image:", data.error);
      throw new Error("Error generating DALLE3 image");
    }
  } catch (error) {
    console.error("Error generating DALLE3 image:", error);
    throw error;
  }
}
~~~

The [[generateDalle3]] tool for Obsistants shows how to interact with an API (in this case, DALLE3) and manage files within Obsidian. Breaking down the code provides insights into creating tools for Obsistants:

1. **Function Definition**: The JavaScript function takes parameters (`prompt`, `size`, `style`) that define the image generation request. These parameters correspond to the user's input and predefined defaults.

2. **API Key Retrieval**: The tool retrieves the API key from the Obsistants plugin settings. This key is necessary for authentication when communicating with the DALLE3 API.

3. **API Request**: It sends a POST request to the DALLE3 API with the necessary data, including the image prompt, size, style, and format. This is where the actual communication with the external service occurs, using the provided parameters to request image generation.

4. **Response Handling**: After receiving the response, the tool checks if the operation was successful. If so, it proceeds to process and save the generated image.

5. **File Management**: The tool prepares the filename and path, ensuring the directory structure exists in Obsidian's vault. It then converts the received image data (in base64 format) into a binary format suitable for saving as a file.

6. **Saving the Image**: The image is saved in the specified directory within the Obsidian vault. The tool logs the successful operation or errors if something goes wrong.

7. **Output Generation**: Finally, it constructs a Markdown link to the saved image, making it easy to reference within Obsidian notes.

From this tool's code, we learn the following about creating tools for Obsistants:

- **Parameter Design**: Tools must define their parameters carefully to match user input and functionality requirements.
- **API Integration**: They should handle external API interactions securely and efficiently, using authentication keys and managing data formats.
- **File Operations**: Tools must navigate Obsidian's file system correctly, creating directories and saving files as needed.
- **Error Handling**: Robust error checking and handling are crucial to ensure the tool operates reliably within the Obsidian environment.

By understanding these aspects, you can write tools that extend Obsidian's capabilities through Obsistants, integrating with external APIs and performing complex operations seamlessly within the app.

# Get Today in History

The [[getTodayInHistory]] tool for Obsistants offers valuable insights into tool design and functionality for Obsidian extensions. Here's what we can infer:

1. **Simplicity and Focus**: Tools should be focused on a specific function. `getTodayInHistory` concentrates on generating a directive based on the current date, showcasing that effective tools perform one task well.

2. **Use of Native JavaScript Functions**: The tool leverages JavaScript's native capabilities, like date handling and locale-specific formatting, to perform its core logic. This indicates tools should efficiently use built-in functions to reduce complexity.

3. **Custom Logic Handling**: The inclusion of a custom function `getOrdinalIndicator` within the main function illustrates that tools can contain specialized logic to handle particular needs, ensuring outputs are tailored and user-friendly.

4. **Directive Generation**: The tool's primary output is a directive—a clear instruction set for further action, in this case, to retrieve historical events. This highlights that tools can be designed to produce actionable outputs that facilitate subsequent tasks, even outside the tool itself.

5. **User Experience Consideration**: The detailed and specific request to make the information "visually appealing and not boring" implies that tools should consider the end-user experience, producing outputs that are engaging and useful.

From this example, we learn that tools for Obsistants are not just about performing a task but are designed with end-use and integration in mind, ensuring they provide clear, specific, and actionable output while maintaining focus on user interaction and experience.


# Useful Functions

## Saving to a folder

1. **Saving Files to a Specific Folder**:
    - You can save generated files, such as images, to a specific folder within the Obsidian vault.
    - Before saving a file, check if the target folder exists using `app.vault.adapter.exists(folderName)`.
    - If the folder doesn't exist, create it using `app.vault.createFolder(folderName)`.
2. **Generating File Names**:
    - It's important to generate meaningful and concise file names for the files you save to the vault.
    - You can use the Obsistant's `processMessage` function to generate file names based on the prompt or context.
    - Construct a `namePrompt` by appending the original prompt to an instruction asking for a concise file name.
    - Call `app.plugins.getPlugin("obsistants").processMessage(namePrompt, true)` to generate the file name using the Obsistant.
3. **Truncating File Names**:
    - To ensure file names are concise and compatible with the file system, you can truncate the generated file names to a maximum length (e.g., 30 characters).
    - Use the `slice` method to truncate the file name, like `generatedName.slice(0, 30)`.
    - Replace any characters that are not alphanumeric or underscores with underscores to ensure a valid file name.
4. **Ensuring File Name Uniqueness**:
    - To prevent overwriting existing files, you can append a timestamp to the file name.
    - Generate a timestamp using `new Date().toISOString().replace(/[-:.]/g, "")`.
    - Concatenate the truncated file name and the timestamp to create a unique file name.
5. **Saving Files to the Vault**:
    - Use `app.vault.createBinary(filePath, fileContent)` to save a file to the specified `filePath` in the vault.
    - If you have a URL or data URL of the file, you can fetch the file content using `fetch(fileUrl)` and convert it to a `Uint8Array` before saving it to the vault.
6. **Getting the File Path**:
    - After saving a file to the vault, you can retrieve the correct file path using `app.vault.getResourcePath(filePath)`.
    - This function returns the proper path that can be used in markdown links or embeds.
7. **Embedding Files in Markdown**:
    - To embed a saved file in a markdown document, use the markdown syntax `![Alt Text](filePath)`.
    - Replace `Alt Text` with a meaningful description of the file and `filePath` with the path returned by `app.vault.getResourcePath(filePath)`.

# Troubleshooting

## ~~~
You need to enclose the JSON and Javascript in ~~~ separately, and make sure that they ~~~ are each on their own line, so it doesn't interfere with the code

The below is WRONG
~~~JSON
{code
}~~~

## Type Error
`TypeError: Cannot read properties of undefined (reading 'execute')`

This exact error means that Obsistants doesn't see the code, the code portion isn't being written to the execute method.  
  
You can open up the console log and put this line in `console.log(app.plugins.getPlugin("obsistants").tools);` and you'll see all of the tools. You can open them up, and where execute is you should see that `_ƒ`_ symbol. If you do not, then the code has not been created for the tool.

## API Key
Use the below code to directly retrieve your API key from the obsistants plugin.

`const apiKey = await app.plugins.getPlugin("obsistants").settings.apiKey`

## Logging outputs
Anytime the input matters for another function/thing _always_ log out the output to make sure it's what I expect in the first place.

Based on our conversation and the lessons learned from creating and refining the tools, here are some key insights and best practices for making Obsistants tools that are not already covered in the attached Obsistants KB file:

## Handling Special Characters
When generating filenames or content, it's important to handle special characters that may cause issues. For example, when creating filenames, replace characters like `\/:*?"<>|` with underscores or remove them entirely to ensure valid filenames.

## Customizing File Naming 
Allow users to control the naming of generated files by providing relevant parameters like `title`. Use these parameters to create meaningful and descriptive filenames, such as using the first few words of the title or truncating long titles to a specified length.

## Generating YAML Front Matter
When creating files with YAML front matter, pay attention to the formatting and structure. Ensure that the field names are followed by colons and that the values don't contain any colons. Use appropriate indentation and line breaks to maintain readability.

## Handling Tags
If the tool involves generating tags, provide clear instructions to users on how to format the tags. For example, specify whether tags should include the '#' character or not. When adding tags to the YAML front matter, format them as a list with each tag on a separate line, prefixed with a hyphen and a space.

## Folder Management
If the tool generates files, consider allowing users to specify the target folder or use a default folder like `_📭 Inbox`. Ensure that the specified folder exists before attempting to create files within it, and create the folder if it doesn't exist.

## Error Handling
Implement robust error handling in the tool's code. Catch and handle errors gracefully, providing informative error messages to users. Log errors to the console for easier debugging and troubleshooting.

## Truncating Content 
If the tool generates content that may exceed a certain length, consider adding a `max_tokens` parameter to allow users to control the maximum number of tokens in the generated content. Truncate the content if it exceeds the specified limit to prevent excessive memory usage or performance issues.

## Providing Usage Instructions
When defining the tool's parameters in the JSON schema, include clear and concise descriptions for each parameter. Explain the purpose of each parameter, its expected format, and any default values. This helps users understand how to use the tool effectively.

## Tool Functionality
There are two types of returns to consider with tools. 
1. If a function is within another function, that function returns info to a function. The top level function, or the one that the AI calls, is the return that matters for the LLM, it's the only one it will see. 
2. Any other return used from function to function is only "seen" by code.

![[Pasted image 20240417124435.png]]
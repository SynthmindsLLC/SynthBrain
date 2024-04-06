---
Title: Instructing an LLM to Create and Input a Diagram into Obsidian Canvas Using JavaScript
Description: A guide on how to instruct an LLM to generate a new canvas in Obsidian and input a predefined diagram in JSON format into the canvas, utilizing JavaScript for automation.
Date: 2024-04-04
Tags: 
 - "#Obsidian"
 - "#LLM"
 - "#JavaScript"
 - "#JSON"
 - "#Automation"
---

To instruct an LLM (Language Learning Model) to create a new canvas in Obsidian and then input a predefined diagram in JSON into the canvas using JavaScript, follow these steps:

1. **Create a New Canvas in Obsidian**: First, you need to generate a new canvas. This can be done manually through the Obsidian interface or programmatically if Obsidian's API supports canvas creation. As of the information available, direct creation of a canvas via an external script might not be directly supported, but you can create a `.canvas` file with the necessary JSON structure and save it to your Obsidian vault directory.

2. **Define the Diagram in JSON Format**: Ensure your diagram is defined according to the JSON Canvas schema. This involves structuring your nodes and edges in a JSON object that Obsidian Canvas can understand and render.

3. **Input the Diagram into the Canvas**: If you're working within the constraints of a plugin or script that operates inside Obsidian, you would use Obsidian's API to manipulate the canvas. However, since direct manipulation via external scripts might be limited, the primary method involves modifying or creating `.canvas` files directly in the Obsidian vault.

Here's a conceptual JavaScript function that outlines how you might prepare the JSON for a diagram and save it as a `.canvas` file. Note that this is a conceptual example, as direct file system operations would depend on the environment (Node.js, browser extension, etc.) and permissions:

```javascript
// This function assumes the existence of an API or method to save files to Obsidian's vault.
// It's a conceptual example illustrating the steps rather than a directly executable script.

function createAndInputDiagramToCanvas(diagramJSON, canvasName, obsidianVaultPath) {
  // Convert the diagram object to a JSON string
  const diagramJSONString = JSON.stringify(diagramJSON, null, 2);

  // Define the full path for the new canvas file
  const canvasFilePath = `${obsidianVaultPath}/${canvasName}.canvas`;

  // Save the JSON string to a new .canvas file in the Obsidian vault
  // The method to save the file will vary based on your environment (Node.js, browser extension, etc.)
  saveFileToObsidianVault(canvasFilePath, diagramJSONString);
}

// Example usage
const diagramJSON = {
  // Define your nodes and edges here according to the JSON Canvas schema
};

createAndInputDiagramToCanvas(diagramJSON, "MyNewCanvas", "/path/to/obsidian/vault");
```

This function outlines the process of converting a diagram defined in JSON into a string, then saving it as a `.canvas` file within the Obsidian vault. The actual implementation of `saveFileToObsidianVault` would depend on the specific environment and capabilities of the script or plugin you're developing.

Remember, direct manipulation of Obsidian data through external scripts should be done with caution to avoid data loss or corruption. Always back up your data before attempting such operations.

## List of Relevant Backlinks
- [[Obsidian Canvas Integration]]
- [[JSON Canvas Schema and Usage]]
- [[Developing Obsidian Plugins and Scripts]]

Sources
[1] Obsidian Canvas - Visualize your ideas https://obsidian.md/canvas
[2] Announcing JSON Canvas: an open file format for infinite canvas data https://www.reddit.com/r/ObsidianMD/comments/1bc879m/announcing_json_canvas_an_open_file_format_for/
[3] Supercharge your Obsidian.md canvas experience! Create ... - GitHub https://github.com/Developer-Mike/obsidian-advanced-canvas
[4] JSON Canvas – An open file format for infinite canvas data - Hacker News https://news.ycombinator.com/item?id=39670922
[5] Create a new canvas directly from quick switcher - Obsidian Forum https://forum.obsidian.md/t/create-a-new-canvas-directly-from-quick-switcher/72798
[6] Convert a canvas into an excalidraw drawing? - Help - Obsidian Forum https://forum.obsidian.md/t/convert-a-canvas-into-an-excalidraw-drawing/69354
[7] The new Canvas plugin will enhance MOC and revolutionize Obsidian https://www.reddit.com/r/ObsidianMD/comments/zrftar/the_new_canvas_plugin_will_enhance_moc_and/
[8] zapthedingbat/drawio-obsidian: Draw.io plugin for obsidian.md https://github.com/zapthedingbat/drawio-obsidian
[9] Create new note from within Canvas - Feature archive - Obsidian Forum https://forum.obsidian.md/t/create-new-note-from-within-canvas/49123
[10] Obsidian Plugin Stats https://obsidian-plugin-stats.vercel.app/plugins
[11] Add properties to canvas files - Feature archive - Obsidian Forum https://forum.obsidian.md/t/add-properties-to-canvas-files/74469
[12] dwolfe884/obsidian-x86-flow-graph - GitHub https://github.com/dwolfe884/obsidian-x86-flow-graph
[13] Canvas - Fork My Brain https://notes.nicolevanderhoeven.com/obsidian-playbook/Obsidian%2BPlugins/Core%2BPlugins/Canvas
[14] JSON Canvas – An open file format for infinite canvas data - Brian Lovin https://brianlovin.com/hn/39670922
[15] Obsidian Canvas Walkthrough: Build with Me and Explore 3 I've Made https://www.youtube.com/watch?v=8DTYGSKHxCM

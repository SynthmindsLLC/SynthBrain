---

---

The JSON schema for Obsidian Canvas, now referred to as JSON Canvas, is designed to facilitate the creation, import, export, and storage of infinite canvas data in a structured and easily parsable format. This schema is part of an open-source initiative under the MIT license, aimed at providing longevity, readability, interoperability, and extensibility to data created with infinite canvas apps. The schema is currently at version 1.0 and is described as relatively conservative, focusing on essential features to serve as a useful starting point for further development[1][2][3].

### JSON Canvas Schema Overview

The JSON Canvas schema is structured to represent the elements within a canvas, such as nodes (ideas, notes, or objects) and edges (connections or relationships between nodes). While specific details of the schema were not explicitly outlined in the provided sources, the general approach to such a schema typically includes:

- **Nodes**: Represented by objects containing properties such as `id`, `x` (x-coordinate), `y` (y-coordinate), `width`, `height`, `type` (e.g., text, image), and `text` (for text nodes). Nodes serve as the primary elements within the canvas, around which users can organize their ideas and content.
- **Edges**: Represented by objects linking two nodes, containing properties such as `id`, `fromNode` (ID of the source node), `toNode` (ID of the target node), and additional properties to describe the visual representation of the connection (e.g., `color`, `label`).

### Example JSON Canvas Structure

```json
{
  "nodes": [
    {
      "id": "node1",
      "x": 100,
      "y": 150,
      "width": 250,
      "height": 60,
      "type": "text",
      "text": "This is a note"
    }
  ],
  "edges": [
    {
      "id": "edge1",
      "fromNode": "node1",
      "toNode": "node2"
    }
  ]
}
```

This example illustrates a basic structure where a canvas consists of nodes and edges. Each node and edge has an `id` for identification, with nodes also detailing their position (`x`, `y`), dimensions (`width`, `height`), type, and content (`text`). Edges specify their source (`fromNode`) and target (`toNode`) nodes, creating a visual and conceptual link between them.

### Conclusion

The JSON Canvas schema is a foundational step towards creating a standardized, open format for representing infinite canvas data. It emphasizes ease of parsing and user ownership over data, with the potential for wide adoption across various applications and tools. As the schema evolves, it is expected to incorporate more features and capabilities to support the diverse needs of canvas app users and developers[1][2][3].

## List of Relevant Backlinks
- [[Obsidian JSON Canvas Introduction]]
- [[JSON Canvas Open Source Initiative]]
- [[Developing with JSON Canvas]]

Sources
[1] Announcing JSON Canvas: an open file format for infinite canvas data https://www.reddit.com/r/ObsidianMD/comments/1bc879m/announcing_json_canvas_an_open_file_format_for/
[2] Announcing JSON Canvas: an open file format for infinite canvas data https://obsidian.md/blog/json-canvas/
[3] JSON Canvas – An open file format for infinite canvas data - Hacker News https://news.ycombinator.com/item?id=39670922
[4] Obsidian Canvas - Visualize your ideas https://obsidian.md/canvas
[5] Supercharge your Obsidian.md canvas experience! Create ... - GitHub https://github.com/Developer-Mike/obsidian-advanced-canvas
[6] Obsidian Canvas uses a new JSON-based file format that we ... https://news.ycombinator.com/item?id=34067709
[7] JSON schema - mnml's vault - Obsidian Publish https://publish.obsidian.md/manuel/Wiki/Programming/JSON%2Bschema
[8] vjeux on X: "I've been wanting something like this to popup for ... https://twitter.com/Vjeux/status/1767315527784141269
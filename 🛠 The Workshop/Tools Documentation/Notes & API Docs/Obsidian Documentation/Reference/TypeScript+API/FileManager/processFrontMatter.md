[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

processFrontMatter

    aliases: "FileManager.processFrontMatter"
    cssclasses: hide-title

[`FileManager`](https://docs.obsidian.md/Reference/TypeScript+API/FileManager) › [`processFrontMatter`](https://docs.obsidian.md/Reference/TypeScript+API/FileManager/processFrontMatter)

FileManager.processFrontMatter() method
-----------------------------------------

Atomically read, modify, and save the frontmatter of a note. The frontmatter is passed in as a JS object, and should be mutated directly to achieve the desired result.

Remember to handle errors thrown by this method.

**Signature:**

    processFrontMatter(file: TFile, fn: (frontmatter: any) => void, options?: DataWriteOptions): Promise<void>;
    

Parameters
------------

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | [`TFile`](https://docs.obsidian.md/Reference/TypeScript+API/TFile) | the file to be modified. Must be a markdown file. |
| `fn` | `(frontmatter: any) => void` | a callback function which mutates the frontmatter object synchronously. |
| `options` | [`DataWriteOptions`](https://docs.obsidian.md/Reference/TypeScript+API/DataWriteOptions) | _(Optional)_ write options. |

**Returns:**

`Promise``<void>`

Exceptions
------------

YAMLParseError if the YAML parsing fails

any errors that your callback function throws

Links to this page

[FileManager](https://docs.obsidian.md/Reference/TypeScript+API/FileManager)

[Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines)

processFrontMatter

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

registerEditorExtension

    aliases: "Plugin.registerEditorExtension"
    cssclasses: hide-title

[`Plugin`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin) › [`registerEditorExtension`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerEditorExtension)

Plugin.registerEditorExtension() method
-----------------------------------------

Registers a CodeMirror 6 extension. To reconfigure cm6 extensions for a plugin on the fly, an array should be passed in, and modified dynamically. Once this array is modified, calling [Workspace.updateOptions()](https://docs.obsidian.md/Reference/TypeScript+API/Workspace/updateOptions) will apply the changes.

**Signature:**

    registerEditorExtension(extension: Extension): void;
    

Parameters
------------

| Parameter | Type | Description |
| --- | --- | --- |
| `extension` | `Extension` | must be a CodeMirror 6 `Extension`, or an array of Extensions. |

**Returns:**

`void`

Links to this page

[Editor extensions](https://docs.obsidian.md/Plugins/Editor/Editor+extensions)

[Plugin](https://docs.obsidian.md/Reference/TypeScript+API/Plugin)

[Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines)

registerEditorExtension

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
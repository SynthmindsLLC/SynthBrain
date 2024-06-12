[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Editor

The [Editor](https://docs.obsidian.md/Reference/TypeScript+API/Editor) class exposes operations for reading and manipulating an active Markdown document in edit mode.

If you want to access the editor in a command, use the [editorCallback](https://docs.obsidian.md/Plugins/User+interface/Commands#Editor commands).

If you want to use the editor elsewhere, you can access it from the active view:

    const view = this.app.workspace.getActiveViewOfType(MarkdownView);
    
    // Make sure the user is editing a Markdown file.
    if (view) {
    	const cursor = view.editor.getCursor();
    
    	// ...
    }
    

Note

Obsidian uses [CodeMirror](https://codemirror.net/) (CM) as the underlying text editor, and exposes the CodeMirror editor as part of the API. `Editor` serves as an abstraction to bridge features between CM6 and CM5 (legacy editor, only available on desktop). By using `Editor` instead of directly accessing the CodeMirror instance, you ensure that your plugin works on both platforms.

Insert text at cursor position
--------------------------------

The [replaceRange()](https://docs.obsidian.md/Reference/TypeScript+API/Editor/replaceRange) method replaces the text between two cursor positions. If you only give it one position, it inserts the new text between that position and the next.

The following command inserts today's date at the cursor position:

    import { Editor, moment, Plugin } from "obsidian";
    
    export default class ExamplePlugin extends Plugin {
      async onload() {
        this.addCommand({
          id: "insert-todays-date",
          name: "Insert today's date",
          editorCallback: (editor: Editor) => {
            editor.replaceRange(
              moment().format("YYYY-MM-DD"),
              editor.getCursor()
            );
          },
        });
      }
    }
    

![editor-todays-date.gif](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/editor-todays-date.gif)

Replace current selection
---------------------------

If you want to modify the selected text, use [replaceSelection()](https://docs.obsidian.md/Reference/TypeScript+API/Editor/replaceRange) to replace the current selection with a new text.

The following command reads the current selection and converts it to uppercase:

    import { Editor, Plugin } from "obsidian";
    
    export default class ExamplePlugin extends Plugin {
      async onload() {
        this.addCommand({
          id: "convert-to-uppercase",
          name: "Convert to uppercase",
          editorCallback: (editor: Editor) => {
            const selection = editor.getSelection();
            editor.replaceSelection(selection.toUpperCase());
          },
        });
      }
    }
    

![editor-uppercase.gif](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/editor-uppercase.gif)

Links to this page

[About user interface](https://docs.obsidian.md/Plugins/User+interface/About+user+interface)

[on('editor-change')](https://docs.obsidian.md/Reference/TypeScript+API/Workspace/on\('editor-change'\))

[on('editor-drop')](https://docs.obsidian.md/Reference/TypeScript+API/Workspace/on\('editor-drop'\))

[on('editor-menu')](https://docs.obsidian.md/Reference/TypeScript+API/Workspace/on\('editor-menu'\))

[on('editor-paste')](https://docs.obsidian.md/Reference/TypeScript+API/Workspace/on\('editor-paste'\))

[Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines)

Editor

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
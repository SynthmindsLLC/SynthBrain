[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Editor extensions

    alias: editor extension

Editor extensions let you customize the experience of editing notes in Obsidian. This page explains what editor extensions are, and when to use them.

Obsidian uses CodeMirror 6 (CM6) to power the Markdown editor. Just like Obsidian, CM6 has plugins of its own, called _extensions_. In other words, an Obsidian _editor extension_ is the same thing as a _CodeMirror 6 extension_.

The API for building editor extensions is a bit unconventional and requires that you have a basic understanding of its architecture before you get started. This section aims to give you enough context and examples for you to get started. If you want to learn more about building editor extensions, refer to the [CodeMirror 6 documentation](https://codemirror.net/docs/).

Do I need an editor extension?
--------------------------------

Building editor extensions can be challenging, so before you start building one, consider whether you really need it.

*   If you want to change how to convert Markdown to HTML in the Reading view, consider building a [Markdown post processor](https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing).
*   If you want to change how the document looks and feels in Live Preview, you need to build an editor extension.

Registering editor extensions
-------------------------------

CodeMirror 6 (CM6) is a powerful engine for editing code using web technologies. At its core, the editor itself has a minimal set of features. Any features you'd expect from a modern editor are available as _extensions_ that you can pick and choose. While Obsidian comes with many of these extensions out-of-the-box, you can also register your own.

To register an editor extension, use [registerEditorExtension()](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerEditorExtension) in the `onload` method of your Obsidian plugin:

    onload() {
      this.registerEditorExtension([examplePlugin, exampleField]);
    }
    

While CM6 supports several types of extensions, two of the most common ones are [View plugins](https://docs.obsidian.md/Plugins/Editor/View+plugins) and [State fields](https://docs.obsidian.md/Plugins/Editor/State+fields).  

Links to this page

[About user interface](https://docs.obsidian.md/Plugins/User+interface/About+user+interface)

[Decorations](https://docs.obsidian.md/Plugins/Editor/Decorations)

[Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines)

[State fields](https://docs.obsidian.md/Plugins/Editor/State+fields)

[State management](https://docs.obsidian.md/Plugins/Editor/State+management)

[View plugins](https://docs.obsidian.md/Plugins/Editor/View+plugins)

Editor extensions

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
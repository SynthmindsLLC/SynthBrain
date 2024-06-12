[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Plugin

    aliases: "Plugin"
    cssclasses: hide-title

[`Plugin`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin)

Plugin class
--------------

**Signature:**

    export abstract class Plugin extends Component 
    

**Extends:** [`Component`](https://docs.obsidian.md/Reference/TypeScript+API/Component)

Constructors
--------------

| Constructor | Modifiers | Description |
| --- | --- | --- |
| [`(constructor)(app, manifest)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/\(constructor\)) |  | Constructs a new instance of the `Plugin` class |

Properties
------------

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| [`app`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/app) |  | [`App`](https://docs.obsidian.md/Reference/TypeScript+API/App) |  |
| [`manifest`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/manifest) |  | [`PluginManifest`](https://docs.obsidian.md/Reference/TypeScript+API/PluginManifest) |  |

Methods
---------

| Method | Modifiers | Description |
| --- | --- | --- |
| [`addChild(component)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/addChild) |  | 
Adds a child component, loading it if this component is loaded

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`addCommand(command)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/addCommand) |  | Register a command globally. Registered commands will be available from the @{link [https://help.md/Plugins/Command+palette](https://help.md/Plugins/Command+palette) Command pallete}. The command id and name will be automatically prefixed with this plugin's id and name. |
| [`addRibbonIcon(icon, title, callback)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/addRibbonIcon) |  | Adds a ribbon icon to the left bar. |
| [`addSettingTab(settingTab)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/addSettingTab) |  | Register a settings tab, which allows users to change settings. |
| [`addStatusBarItem()`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/addStatusBarItem) |  | Adds a status bar item to the bottom of the app. Not available on mobile. |
| [`load()`](https://docs.obsidian.md/Reference/TypeScript+API/Component/load) |  | 

Load this component and its children

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`loadData()`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/loadData) |  | Load settings data from disk. Data is stored in `data.json` in the plugin folder. |
| [`onExternalSettingsChange()?`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/onExternalSettingsChange) |  | 

_(Optional)_ Called when the `data.json` file is modified on disk externally from Obsidian. This usually means that a Sync service or external program has modified the plugin settings.

Implement this method to reload plugin settings when they have changed externally.

 |
| [`onload()`](https://docs.obsidian.md/Reference/TypeScript+API/Component/onload) |  | 

Override this to load your component

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`onunload()`](https://docs.obsidian.md/Reference/TypeScript+API/Component/onunload) |  | 

Override this to unload your component

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`register(cb)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/register) |  | 

Registers a callback to be called when unloading

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`registerDomEvent(el, type, callback, options)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/registerDomEvent) |  | 

Registers an DOM event to be detached when unloading

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`registerDomEvent(el, type, callback, options)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/registerDomEvent_1) |  | 

Registers an DOM event to be detached when unloading

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`registerDomEvent(el, type, callback, options)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/registerDomEvent_2) |  | 

Registers an DOM event to be detached when unloading

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`registerEditorExtension(extension)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerEditorExtension) |  | Registers a CodeMirror 6 extension. To reconfigure cm6 extensions for a plugin on the fly, an array should be passed in, and modified dynamically. Once this array is modified, calling [Workspace.updateOptions()](https://docs.obsidian.md/Reference/TypeScript+API/Workspace/updateOptions) will apply the changes. |
| [`registerEditorSuggest(editorSuggest)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerEditorSuggest) |  | Register an EditorSuggest which can provide live suggestions while the user is typing. |
| [`registerEvent(eventRef)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/registerEvent) |  | 

Registers an event to be detached when unloading

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`registerExtensions(extensions, viewType)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerExtensions) |  |  |
| [`registerHoverLinkSource(id, info)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerHoverLinkSource) |  | Registers a view with the 'Page preview' core plugin as an emitter of the 'hover-link' on the event. |
| [`registerInterval(id)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/registerInterval) |  | 

Registers an interval (from setInterval) to be cancelled when unloading Use instead of to avoid TypeScript confusing between NodeJS vs Browser API

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`registerMarkdownCodeBlockProcessor(language, handler, sortOrder)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerMarkdownCodeBlockProcessor) |  | Register a special post processor that handles fenced code given a language and a handler. This special post processor takes care of removing the `<pre><code>` and create a `<div>` that will be passed to the handler, and is expected to be filled with custom elements. |
| [`registerMarkdownPostProcessor(postProcessor, sortOrder)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerMarkdownPostProcessor) |  | Registers a post processor, to change how the document looks in reading mode. |
| [`registerObsidianProtocolHandler(action, handler)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerObsidianProtocolHandler) |  | Register a handler for obsidian:// URLs. |
| [`registerView(type, viewCreator)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerView) |  |  |
| [`removeChild(component)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/removeChild) |  | 

Removes a child component, unloading it

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`saveData(data)`](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/saveData) |  | Write settings data to disk. Data is stored in `data.json` in the plugin folder. |
| [`unload()`](https://docs.obsidian.md/Reference/TypeScript+API/Component/unload) |  | 

Unload this component and its children

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |

Links to this page

[(constructor)](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/\(constructor\))

[(constructor)](https://docs.obsidian.md/Reference/TypeScript+API/PluginSettingTab/\(constructor\))

[addCommand](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/addCommand)

[addRibbonIcon](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/addRibbonIcon)

[addSettingTab](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/addSettingTab)

[addStatusBarItem](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/addStatusBarItem)

[Anatomy of a plugin](https://docs.obsidian.md/Plugins/Getting+started/Anatomy+of+a+plugin)

[app](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/app)

[loadData](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/loadData)

[manifest](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/manifest)

[onExternalSettingsChange](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/onExternalSettingsChange)

[registerEditorExtension](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerEditorExtension)

[registerEditorSuggest](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerEditorSuggest)

[registerExtensions](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerExtensions)

[registerHoverLinkSource](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerHoverLinkSource)

[registerMarkdownCodeBlockProcessor](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerMarkdownCodeBlockProcessor)

[registerMarkdownPostProcessor](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerMarkdownPostProcessor)

[registerObsidianProtocolHandler](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerObsidianProtocolHandler)

[registerView](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerView)

[saveData](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/saveData)

Plugin

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
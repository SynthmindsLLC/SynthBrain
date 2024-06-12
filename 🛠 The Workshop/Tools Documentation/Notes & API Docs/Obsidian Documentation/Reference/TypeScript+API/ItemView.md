[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

ItemView

    aliases: "ItemView"
    cssclasses: hide-title

[`ItemView`](https://docs.obsidian.md/Reference/TypeScript+API/ItemView)

ItemView class
----------------

**Signature:**

    export abstract class ItemView extends View 
    

**Extends:** [`View`](https://docs.obsidian.md/Reference/TypeScript+API/View)

Constructors
--------------

| Constructor | Modifiers | Description |
| --- | --- | --- |
| [`(constructor)(leaf)`](https://docs.obsidian.md/Reference/TypeScript+API/ItemView/\(constructor\)) |  | Constructs a new instance of the `ItemView` class |

Properties
------------

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| [`app`](https://docs.obsidian.md/Reference/TypeScript+API/View/app) |  | [`App`](https://docs.obsidian.md/Reference/TypeScript+API/App) | 
(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`containerEl`](https://docs.obsidian.md/Reference/TypeScript+API/View/containerEl) |  | `HTMLElement` | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`contentEl`](https://docs.obsidian.md/Reference/TypeScript+API/ItemView/contentEl) |  | `HTMLElement` |  |
| [`icon`](https://docs.obsidian.md/Reference/TypeScript+API/View/icon) |  | [`IconName`](https://docs.obsidian.md/Reference/TypeScript+API/IconName) | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`leaf`](https://docs.obsidian.md/Reference/TypeScript+API/View/leaf) |  | [`WorkspaceLeaf`](https://docs.obsidian.md/Reference/TypeScript+API/WorkspaceLeaf) | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`navigation`](https://docs.obsidian.md/Reference/TypeScript+API/View/navigation) |  | `boolean` | 

Whether or not the view is intended for navigation. If your view is a static view that is not intended to be navigated away, set this to false. (For example: File explorer, calendar, etc.) If your view opens a file or can be otherwise navigated, set this to true. (For example: Markdown editor view, Kanban view, PDF view, etc.)

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`scope`](https://docs.obsidian.md/Reference/TypeScript+API/View/scope) |  | [`Scope`](https://docs.obsidian.md/Reference/TypeScript+API/Scope) `| null` | 

Assign an optional scope to your view to register hotkeys for when the view is in focus.

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |

Methods
---------

| Method | Modifiers | Description |
| --- | --- | --- |
| [`addAction(icon, title, callback)`](https://docs.obsidian.md/Reference/TypeScript+API/ItemView/addAction) |  |  |
| [`addChild(component)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/addChild) |  | 
Adds a child component, loading it if this component is loaded

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`getDisplayText()`](https://docs.obsidian.md/Reference/TypeScript+API/View/getDisplayText) | `abstract` | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`getEphemeralState()`](https://docs.obsidian.md/Reference/TypeScript+API/View/getEphemeralState) |  | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`getIcon()`](https://docs.obsidian.md/Reference/TypeScript+API/View/getIcon) |  | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`getState()`](https://docs.obsidian.md/Reference/TypeScript+API/View/getState) |  | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`getViewType()`](https://docs.obsidian.md/Reference/TypeScript+API/View/getViewType) | `abstract` | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`load()`](https://docs.obsidian.md/Reference/TypeScript+API/Component/load) |  | 

Load this component and its children

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`onClose()`](https://docs.obsidian.md/Reference/TypeScript+API/View/onClose) | `protected` | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`onload()`](https://docs.obsidian.md/Reference/TypeScript+API/Component/onload) |  | 

Override this to load your component

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`onOpen()`](https://docs.obsidian.md/Reference/TypeScript+API/View/onOpen) | `protected` | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`onPaneMenu(menu, source)`](https://docs.obsidian.md/Reference/TypeScript+API/View/onPaneMenu) |  | 

Populates the pane menu.

(Replaces the previously removed `onHeaderMenu` and `onMoreOptionsMenu`)

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`onResize()`](https://docs.obsidian.md/Reference/TypeScript+API/View/onResize) |  | 

Called when the size of this view is changed.

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

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
| [`registerEvent(eventRef)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/registerEvent) |  | 

Registers an event to be detached when unloading

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`registerInterval(id)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/registerInterval) |  | 

Registers an interval (from setInterval) to be cancelled when unloading Use instead of to avoid TypeScript confusing between NodeJS vs Browser API

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`removeChild(component)`](https://docs.obsidian.md/Reference/TypeScript+API/Component/removeChild) |  | 

Removes a child component, unloading it

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |
| [`setEphemeralState(state)`](https://docs.obsidian.md/Reference/TypeScript+API/View/setEphemeralState) |  | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`setState(state, result)`](https://docs.obsidian.md/Reference/TypeScript+API/View/setState) |  | 

(Inherited from [View](https://docs.obsidian.md/Reference/TypeScript+API/View))

 |
| [`unload()`](https://docs.obsidian.md/Reference/TypeScript+API/Component/unload) |  | 

Unload this component and its children

(Inherited from [Component](https://docs.obsidian.md/Reference/TypeScript+API/Component))

 |

Links to this page

[(constructor)](https://docs.obsidian.md/Reference/TypeScript+API/ItemView/\(constructor\))

[addAction](https://docs.obsidian.md/Reference/TypeScript+API/ItemView/addAction)

[contentEl](https://docs.obsidian.md/Reference/TypeScript+API/ItemView/contentEl)

[EditableFileView](https://docs.obsidian.md/Reference/TypeScript+API/EditableFileView)

[FileView](https://docs.obsidian.md/Reference/TypeScript+API/FileView)

[MarkdownView](https://docs.obsidian.md/Reference/TypeScript+API/MarkdownView)

[TextFileView](https://docs.obsidian.md/Reference/TypeScript+API/TextFileView)

[Use Svelte in your plugin](https://docs.obsidian.md/Plugins/Getting+started/Use+Svelte+in+your+plugin)

[Views](https://docs.obsidian.md/Plugins/User+interface/Views)

ItemView

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
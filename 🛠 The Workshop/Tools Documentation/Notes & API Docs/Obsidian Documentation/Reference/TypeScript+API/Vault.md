[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Vault

    aliases: "Vault"
    cssclasses: hide-title

[`Vault`](https://docs.obsidian.md/Reference/TypeScript+API/Vault)

Vault class
-------------

Work with files and folders stored inside a vault.

**Signature:**

    export class Vault extends Events 
    

**Extends:** [`Events`](https://docs.obsidian.md/Reference/TypeScript+API/Events)

Properties
------------

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| [`adapter`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/adapter) |  | [`DataAdapter`](https://docs.obsidian.md/Reference/TypeScript+API/DataAdapter) |  |
| [`configDir`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/configDir) |  | `string` | Gets the path to the config folder. This value is typically `.obsidian` but it could be different. |

Methods
---------

| Method | Modifiers | Description |
| --- | --- | --- |
| [`append(file, data, options)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/append) |  | Add text to the end of a plaintext file inside the vault. |
| [`cachedRead(file)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/cachedRead) |  | Read the content of a plaintext file stored inside the vault Use this if you only want to display the content to the user. If you want to modify the file content afterward use [Vault.read()](https://docs.obsidian.md/Reference/TypeScript+API/Vault/read) |
| [`copy(file, newPath)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/copy) |  | Create a copy of the selected file. |
| [`create(path, data, options)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/create) |  | Create a new plaintext file inside the vault. |
| [`createBinary(path, data, options)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/createBinary) |  | Create a new binary file inside the vault. |
| [`createFolder(path)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/createFolder) |  | Create a new folder inside the vault. |
| [`delete(file, force)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/delete) |  | Deletes the file completely. |
| [`getAbstractFileByPath(path)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getAbstractFileByPath) |  | Get a file or folder inside the vault at the given path. To check if the return type is a file, use `instanceof TFile`. To check if it is a folder, use `instanceof TFolder`. |
| [`getAllLoadedFiles()`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getAllLoadedFiles) |  | Get all files and folders in the vault. |
| [`getFileByPath(path)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getFileByPath) |  | Get a file inside the vault at the given path. Returns `null` if the file does not exist. |
| [`getFiles()`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getFiles) |  | Get all files in the vault. |
| [`getFolderByPath(path)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getFolderByPath) |  | Get a folder inside the vault at the given path. Returns `null` if the folder does not exist. |
| [`getMarkdownFiles()`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getMarkdownFiles) |  | Get all markdown files in the vault. |
| [`getName()`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getName) |  | Gets the name of the vault. |
| [`getResourcePath(file)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getResourcePath) |  | Returns an URI for the browser engine to use, for example to embed an image. |
| [`getRoot()`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getRoot) |  | Get the root folder of the current vault. |
| [`modify(file, data, options)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/modify) |  | Modify the contents of a plaintext file. |
| [`modifyBinary(file, data, options)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/modifyBinary) |  | Modify the contents of a binary file. |
| [`off(name, callback)`](https://docs.obsidian.md/Reference/TypeScript+API/Events/off) |  | 
(Inherited from [Events](https://docs.obsidian.md/Reference/TypeScript+API/Events))

 |
| [`offref(ref)`](https://docs.obsidian.md/Reference/TypeScript+API/Events/offref) |  | 

(Inherited from [Events](https://docs.obsidian.md/Reference/TypeScript+API/Events))

 |
| [`on(name: 'create', callback, ctx)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/on\('create'\)) |  | Called when a file is created. This is also called when the vault is first loaded for each existing file If you do not wish to receive create events on vault load, register your event handler inside [Workspace.onLayoutReady()](https://docs.obsidian.md/Reference/TypeScript+API/Workspace/onLayoutReady). |
| [`on(name: 'modify', callback, ctx)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/on\('modify'\)) |  | Called when a file is modified. |
| [`on(name: 'delete', callback, ctx)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/on\('delete'\)) |  | Called when a file is deleted. |
| [`on(name: 'rename', callback, ctx)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/on\('rename'\)) |  | Called when a file is renamed. |
| [`process(file, fn, options)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/process) |  | Atomically read, modify, and save the contents of a note. |
| [`read(file)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/read) |  | Read a plaintext file that is stored inside the vault, directly from disk. Use this if you intend to modify the file content afterwards. Use [Vault.cachedRead()](https://docs.obsidian.md/Reference/TypeScript+API/Vault/cachedRead) otherwise for better performance. |
| [`readBinary(file)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/readBinary) |  | Read the content of a binary file stored inside the vault. |
| [`recurseChildren(root, cb)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/recurseChildren) | `static` |  |
| [`rename(file, newPath)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/rename) |  | Rename or move a file. |
| [`trash(file, system)`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/trash) |  | Tries to move to system trash. If that isn't successful/allowed, use local trash |
| [`trigger(name, data)`](https://docs.obsidian.md/Reference/TypeScript+API/Events/trigger) |  | 

(Inherited from [Events](https://docs.obsidian.md/Reference/TypeScript+API/Events))

 |
| [`tryTrigger(evt, args)`](https://docs.obsidian.md/Reference/TypeScript+API/Events/tryTrigger) |  | 

(Inherited from [Events](https://docs.obsidian.md/Reference/TypeScript+API/Events))

 |

Links to this page

[adapter](https://docs.obsidian.md/Reference/TypeScript+API/Vault/adapter)

[App](https://docs.obsidian.md/Reference/TypeScript+API/App)

[append](https://docs.obsidian.md/Reference/TypeScript+API/Vault/append)

[cachedRead](https://docs.obsidian.md/Reference/TypeScript+API/Vault/cachedRead)

[configDir](https://docs.obsidian.md/Reference/TypeScript+API/Vault/configDir)

[copy](https://docs.obsidian.md/Reference/TypeScript+API/Vault/copy)

[create](https://docs.obsidian.md/Reference/TypeScript+API/Vault/create)

[createBinary](https://docs.obsidian.md/Reference/TypeScript+API/Vault/createBinary)

[createFolder](https://docs.obsidian.md/Reference/TypeScript+API/Vault/createFolder)

[DataAdapter](https://docs.obsidian.md/Reference/TypeScript+API/DataAdapter)

[delete](https://docs.obsidian.md/Reference/TypeScript+API/Vault/delete)

[getAbstractFileByPath](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getAbstractFileByPath)

[getAllLoadedFiles](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getAllLoadedFiles)

[getFileByPath](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getFileByPath)

[getFiles](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getFiles)

[getFolderByPath](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getFolderByPath)

[getMarkdownFiles](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getMarkdownFiles)

[getName](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getName)

[getResourcePath](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getResourcePath)

[getRoot](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getRoot)

[modify](https://docs.obsidian.md/Reference/TypeScript+API/Vault/modify)

[modifyBinary](https://docs.obsidian.md/Reference/TypeScript+API/Vault/modifyBinary)

[on('create')](https://docs.obsidian.md/Reference/TypeScript+API/Vault/on\('create'\))

[on('delete')](https://docs.obsidian.md/Reference/TypeScript+API/Vault/on\('delete'\))

[on('modify')](https://docs.obsidian.md/Reference/TypeScript+API/Vault/on\('modify'\))

[on('rename')](https://docs.obsidian.md/Reference/TypeScript+API/Vault/on\('rename'\))

[process](https://docs.obsidian.md/Reference/TypeScript+API/Vault/process)

[read](https://docs.obsidian.md/Reference/TypeScript+API/Vault/read)

[readBinary](https://docs.obsidian.md/Reference/TypeScript+API/Vault/readBinary)

[recurseChildren](https://docs.obsidian.md/Reference/TypeScript+API/Vault/recurseChildren)

[rename](https://docs.obsidian.md/Reference/TypeScript+API/Vault/rename)

[TAbstractFile](https://docs.obsidian.md/Reference/TypeScript+API/TAbstractFile)

[TFile](https://docs.obsidian.md/Reference/TypeScript+API/TFile)

[TFolder](https://docs.obsidian.md/Reference/TypeScript+API/TFolder)

[trash](https://docs.obsidian.md/Reference/TypeScript+API/Vault/trash)

[Vault](https://docs.obsidian.md/Plugins/Vault)

Vault

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
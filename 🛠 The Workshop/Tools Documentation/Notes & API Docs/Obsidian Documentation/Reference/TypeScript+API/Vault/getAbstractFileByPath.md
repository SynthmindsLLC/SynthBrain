[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

getAbstractFileByPath

    aliases: "Vault.getAbstractFileByPath"
    cssclasses: hide-title

[`Vault`](https://docs.obsidian.md/Reference/TypeScript+API/Vault) › [`getAbstractFileByPath`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/getAbstractFileByPath)

Vault.getAbstractFileByPath() method
--------------------------------------

Get a file or folder inside the vault at the given path. To check if the return type is a file, use `instanceof TFile`. To check if it is a folder, use `instanceof TFolder`.

**Signature:**

    getAbstractFileByPath(path: string): TAbstractFile | null;
    

Parameters
------------

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `string` | vault absolute path to the folder or file, with extension, case sensitive. |

**Returns:**

[`TAbstractFile`](https://docs.obsidian.md/Reference/TypeScript+API/TAbstractFile) `| null`

the abstract file, if it's found.

Links to this page

[Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines)

[Vault](https://docs.obsidian.md/Reference/TypeScript+API/Vault)

getAbstractFileByPath

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
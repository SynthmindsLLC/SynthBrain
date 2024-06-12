[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

trash

    aliases: "Vault.trash"
    cssclasses: hide-title

[`Vault`](https://docs.obsidian.md/Reference/TypeScript+API/Vault) › [`trash`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/trash)

Vault.trash() method
----------------------

Tries to move to system trash. If that isn't successful/allowed, use local trash

**Signature:**

    trash(file: TAbstractFile, system: boolean): Promise<void>;
    

Parameters
------------

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | [`TAbstractFile`](https://docs.obsidian.md/Reference/TypeScript+API/TAbstractFile) | The file or folder to be deleted |
| `system` | `boolean` | Set to `false` to use local trash by default. |

**Returns:**

`Promise``<void>`

Links to this page

[Vault](https://docs.obsidian.md/Plugins/Vault)

[Vault](https://docs.obsidian.md/Reference/TypeScript+API/Vault)

trash

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
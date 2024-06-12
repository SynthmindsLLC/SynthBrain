[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

read

    aliases: "Vault.read"
    cssclasses: hide-title

[`Vault`](https://docs.obsidian.md/Reference/TypeScript+API/Vault) › [`read`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/read)

Vault.read() method
---------------------

Read a plaintext file that is stored inside the vault, directly from disk. Use this if you intend to modify the file content afterwards. Use [Vault.cachedRead()](https://docs.obsidian.md/Reference/TypeScript+API/Vault/cachedRead) otherwise for better performance.

**Signature:**

    read(file: TFile): Promise<string>;
    

Parameters
------------

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | [`TFile`](https://docs.obsidian.md/Reference/TypeScript+API/TFile) |  |

**Returns:**

`Promise``<string>`

Links to this page

[cachedRead](https://docs.obsidian.md/Reference/TypeScript+API/Vault/cachedRead)

[Vault](https://docs.obsidian.md/Plugins/Vault)

[Vault](https://docs.obsidian.md/Reference/TypeScript+API/Vault)

read

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
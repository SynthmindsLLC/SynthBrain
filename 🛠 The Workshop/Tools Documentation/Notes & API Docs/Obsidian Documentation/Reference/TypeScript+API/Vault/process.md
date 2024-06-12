[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

process

    aliases: "Vault.process"
    cssclasses: hide-title

[`Vault`](https://docs.obsidian.md/Reference/TypeScript+API/Vault) › [`process`](https://docs.obsidian.md/Reference/TypeScript+API/Vault/process)

Vault.process() method
------------------------

Atomically read, modify, and save the contents of a note.

**Signature:**

    process(file: TFile, fn: (data: string) => string, options?: DataWriteOptions): Promise<string>;
    

Parameters
------------

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | [`TFile`](https://docs.obsidian.md/Reference/TypeScript+API/TFile) | the file to be read and modified. |
| `fn` | `(data: string) => string` | a callback function which returns the new content of the note synchronously. |
| `options` | [`DataWriteOptions`](https://docs.obsidian.md/Reference/TypeScript+API/DataWriteOptions) | _(Optional)_ write options. |

**Returns:**

`Promise``<string>`

string - the text value of the note that was written.

Links to this page

[Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines)

[Vault](https://docs.obsidian.md/Plugins/Vault)

[Vault](https://docs.obsidian.md/Reference/TypeScript+API/Vault)

process

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
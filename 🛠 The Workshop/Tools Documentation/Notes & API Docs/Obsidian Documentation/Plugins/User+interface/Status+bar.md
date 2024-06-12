[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Status bar

To create a new block in the status bar, call the [addStatusBarItem()](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/addStatusBarItem) in the `onload()` method. The `addStatusBarItem()` method returns an [HTML elements](https://docs.obsidian.md/Plugins/User+interface/HTML+elements) that you can add your own elements to.

Obsidian mobile

Custom status bar items [are **not** supported](https://discord.com/channels/686053708261228577/707816848615407697/832321402106544179) on Obsidian mobile apps.

    import { Plugin } from "obsidian";
    
    export default class ExamplePlugin extends Plugin {
      async onload() {
        const item = this.addStatusBarItem();
        item.createEl("span", { text: "Hello from the status bar 👋" });
      }
    }
    

Note

For more information on how to use the `createEl()` method, refer to [HTML elements](https://docs.obsidian.md/Plugins/User+interface/HTML+elements).

You can add multiple status bar items by calling `addStatusBarItem()` multiple times. Since Obsidian adds a gap between them, you need to create multiple HTML element on the same status bar item if you need more control of spacing.

    import { Plugin } from "obsidian";
    
    export default class ExamplePlugin extends Plugin {
      async onload() {
        const fruits = this.addStatusBarItem();
        fruits.createEl("span", { text: "🍎" });
        fruits.createEl("span", { text: "🍌" });
    
        const veggies = this.addStatusBarItem();
        veggies.createEl("span", { text: "🥦" });
        veggies.createEl("span", { text: "🥬" });
      }
    }
    

The example above results in the following status bar:

![status-bar.png](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/status-bar.png)

Links to this page

[About user interface](https://docs.obsidian.md/Plugins/User+interface/About+user+interface)

[Use React in your plugin](https://docs.obsidian.md/Plugins/Getting+started/Use+React+in+your+plugin)

Status bar

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
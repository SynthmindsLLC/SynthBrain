[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

HTML elements

Several components in the Obsidian API, such as the [Settings](https://docs.obsidian.md/Plugins/User+interface/Settings), expose _container elements_:

    import { App, PluginSettingTab } from "obsidian";
    
    class ExampleSettingTab extends PluginSettingTab {
      plugin: ExamplePlugin;
    
      constructor(app: App, plugin: ExamplePlugin) {
        super(app, plugin);
        this.plugin = plugin;
      }
    
      display(): void {
        // highlight-next-line
        let { containerEl } = this;
    
        // ...
      }
    }
    

Container elements are `HTMLElement` objects that make it possible to create custom interfaces within Obsidian.

Create HTML elements using `createEl()`
-----------------------------------------

Every `HTMLElement`, including the container element, exposes a `createEl()` method that creates an `HTMLElement` under the original element.

For example, here's how you can add an `<h1>` heading element inside the container element:

    containerEl.createEl("h1", { text: "Heading 1" });
    

`createEl()` returns a reference to the new element:

    const book = containerEl.createEl("div");
    book.createEl("div", { text: "How to Take Smart Notes" });
    book.createEl("small", { text: "Sönke Ahrens" });
    

Style your elements
---------------------

You can add custom CSS styles to your plugin by adding a `styles.css` file in the plugin root directory. To add some styles for the previous book example:

    .book {
      border: 1px solid var(--background-modifier-border);
      padding: 10px;
    }
    
    .book__title {
      font-weight: 600;
    }
    
    .book__author {
      color: var(--text-muted);
    }
    

Tip

`--background-modifier-border` and `--text-muted` are [CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) that are defined and used by Obsidian itself. If you use these variables for your styles, your plugin will look great even if the user has a different theme! 🌈

To make the HTML elements use the styles, set the `cls` property for the HTML element:

    const book = containerEl.createEl("div", { cls: "book" });
    book.createEl("div", { text: "How to Take Smart Notes", cls: "book__title" });
    book.createEl("small", { text: "Sönke Ahrens", cls: "book__author" });
    

Now it looks much better! 🎉

![styles.png](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/styles.png)

### 

Conditional styles

Use the `toggleClass` method if you want to change the style of an element based on the user's settings or other values:

    element.toggleClass("danger", status === "error");
    

Links to this page

[Icons](https://docs.obsidian.md/Plugins/User+interface/Icons)

[Markdown post processing](https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing)

[Modals](https://docs.obsidian.md/Plugins/User+interface/Modals)

[Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines)

[Settings](https://docs.obsidian.md/Plugins/User+interface/Settings)

[Status bar](https://docs.obsidian.md/Plugins/User+interface/Status+bar)

[Use React in your plugin](https://docs.obsidian.md/Plugins/Getting+started/Use+React+in+your+plugin)

[Use Svelte in your plugin](https://docs.obsidian.md/Plugins/Getting+started/Use+Svelte+in+your+plugin)

[Views](https://docs.obsidian.md/Plugins/User+interface/Views)

HTML elements

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
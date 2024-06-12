[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Events

Many of the interfaces in the Obsidian lets you subscribe to events throughout the application, for example when the user makes changes to a file.

Any registered event handlers need to be detached whenever the plugin unloads. The safest way to make sure this happens is to use the [registerEvent()](https://docs.obsidian.md/Reference/TypeScript+API/Component/registerEvent) method.

    import { Plugin } from "obsidian";
    
    export default class ExamplePlugin extends Plugin {
      async onload() {
        this.registerEvent(this.app.vault.on('create', () => {
          console.log('a new file has entered the arena')
        }));
      }
    }
    

Timing events
---------------

If you want to repeatedly call a function with a fixed delay, use the [`window.setInterval()`](https://developer.mozilla.org/en-US/docs/Web/API/setInterval) function with the [registerInterval()](https://docs.obsidian.md/Reference/TypeScript+API/Component/registerInterval) method.

The following example displays the current time in the status bar, updated every second:

    import { moment, Plugin } from "obsidian";
    
    export default class ExamplePlugin extends Plugin {
      statusBar: HTMLElement;
    
      async onload() {
        this.statusBar = this.addStatusBarItem();
    
        this.updateStatusBar();
    
        this.registerInterval(
          window.setInterval(() => this.updateStatusBar(), 1000)
        );
      }
    
      updateStatusBar() {
        this.statusBar.setText(moment().format("H:mm:ss"));
      }
    }
    

Date and time

[Moment](https://momentjs.com/) is a popular JavaScript library for working with dates and time. Obsidian uses Moment internally, so you don't need to install it yourself. You can import it from the Obsidian API instead:

    import { moment } from "obsidian";
    

Links to this page

[Context menus](https://docs.obsidian.md/Plugins/User+interface/Context+menus)

Events

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
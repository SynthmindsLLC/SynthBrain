[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Icons

Several of the UI components in the Obsidian API lets you configure an accompanying icon. You can choose from one of the built-in icons, or you can add your own.

Browse available icons
------------------------

Browse to [lucide.dev](https://lucide.dev/) to see all available icons and their corresponding names.

**Please note:** Only icons up to v0.292.0 are supported at this time.

Use icons
-----------

If you'd like to use icons in your custom interfaces, use the [setIcon()](https://docs.obsidian.md/Reference/TypeScript+API/setIcon) utility function to add an icon to an [HTML element](https://docs.obsidian.md/Plugins/User+interface/HTML+elements). The following example adds icon to the status bar:

    import { Plugin, setIcon } from "obsidian";
    
    export default class ExamplePlugin extends Plugin {
      async onload() {
        const item = this.addStatusBarItem();
        setIcon(item, "info");
      }
    }
    

To change the size of the icon, set the `--icon-size` [CSS variable](https://docs.obsidian.md/Reference/CSS+variables/Foundations/Icons) on the element containing the icon using preset sizes:

    div {
      --icon-size: var(--icon-size-m);
    }
    

Add your own icon
-------------------

To add a custom icon for your plugin, use the [addIcon()](https://docs.obsidian.md/Reference/TypeScript+API/addIcon) utility:

    import { addIcon, Plugin } from "obsidian";
    
    export default class ExamplePlugin extends Plugin {
      async onload() {
        addIcon("circle", `<circle cx="50" cy="50" r="50" fill="currentColor" />`);
    
        this.addRibbonIcon("circle", "Click me", () => {
          console.log("Hello, you!");
        });
      }
    }
    

`addIcon` takes two arguments:

1.  A name to uniquely identify your icon.
2.  The SVG content for the icon, without the surrounding `<svg>` tag.

Note that your icon needs to fit within a `0 0 100 100` view box to be drawn properly.

After the call to `addIcon`, you can use the icon just like any of the built-in icons.

### 

Icon design guidelines

For compatibility and cohesiveness with the Obsidian interface, your icons should [follow Lucide’s guidelines](https://lucide.dev/guide/design/icon-design-guide):

*   Icons must be designed on a 24 by 24 pixels canvas
*   Icons must have at least 1 pixel padding within the canvas
*   Icons must have a stroke width of 2 pixels
*   Icons must use round joins
*   Icons must use round caps
*   Icons must use centered strokes
*   Shapes (such as rectangles) in icons must have border radius of 2 pixels
*   Distinct elements must have 2 pixels of spacing between each other

Lucide also [provides templates and guides](https://github.com/lucide-icons/lucide/blob/main/CONTRIBUTING.md) for vector editors such as Illustrator, Figma, and Inkscape.

Links to this page

[Context menus](https://docs.obsidian.md/Plugins/User+interface/Context+menus)

[Ribbon actions](https://docs.obsidian.md/Plugins/User+interface/Ribbon+actions)

Icons

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
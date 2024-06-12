[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

About styling

The Obsidian app uses [Cascading Style Sheets](https://en.wikipedia.org/wiki/CSS) (CSS) to control the design of the user interface. CSS is the same markup language used for websites and web-based apps, which means you can find many resources online to help you learn how to use and edit CSS.

Obsidian includes hundreds of [CSS variables](https://docs.obsidian.md/Reference/CSS+variables/CSS+variables) that enable consistently beautiful user interfaces.

For plugins
-------------

By using the built-in CSS variables for you own custom elements, you can create native-looking user interfaces in your plugin that look beautiful and are compatible with community themes.

**styles.css**:

    .todo-list {
      background-color: var(--background-secondary);
    }
    

For themes and snippets
-------------------------

By overriding the default values for the Obsidian CSS variables, you can create beautiful themes without the need for complex CSS selectors.

**theme.css**:

    .theme-dark {
      --background-primary: #18004F;
      --background-secondary: #220070;
    }
    
    .theme-light {
      --background-primary: #ECE4FF;
      --background-secondary: #D9C9FF;
    }
    

To learn more about how to build a theme using CSS variables, refer to [Build a theme](https://docs.obsidian.md/Themes/App+themes/Build+a+theme).

About styling

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
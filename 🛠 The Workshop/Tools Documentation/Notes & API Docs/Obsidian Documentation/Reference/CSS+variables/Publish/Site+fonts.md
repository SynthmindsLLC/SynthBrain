[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Site fonts

    cssClass: reference

To load remote fonts we recommend using CSS with `@import` or defining your fonts with `@font-face` and an absolute URL. [Learn more.](https://css-tricks.com/snippets/css/using-font-face-in-css/)

For example you can use [Google Fonts](https://fonts.google.com/) in your `publish.css` file. Here's how you would use the font Poppins:

    /* @import must always be at the top of your publish.css file */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    
    body {
      --font-text-theme: 'Poppins';
    }
    

CSS variables
---------------

Obsidian Publish shares many [CSS variables](https://docs.obsidian.md/Reference/CSS+variables/CSS+variables) with the Obsidian app. You can change these variables on the `body` element.

| Variable | Description |
| --- | --- |
| `--font-text-theme` | Font family for page text |
| `--font-monospace-theme` | Font family for code |
| `--font-interface-theme` | Font family for interface elements such as navigation |

Publish-specific CSS variables should be defined on the `.published-container`. See [Build a Publish theme](https://docs.obsidian.md/Themes/Obsidian+Publish+themes/Build+a+Publish+theme).

| Variable | Description |
| --- | --- |
| `--page-title-font` | Font family for [page titles](https://docs.obsidian.md/Reference/CSS+variables/Publish/Site+pages) |
| `--font-text-size` | Font size for page text |

Links to this page

[CSS variables](https://docs.obsidian.md/Reference/CSS+variables/CSS+variables)

[Publish](https://docs.obsidian.md/Reference/CSS+variables/Publish/Publish)

[Site pages](https://docs.obsidian.md/Reference/CSS+variables/Publish/Site+pages)

Site fonts

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Build a Publish theme

You can build themes for your [Obsidian Publish](https://help.obsidian.md/Obsidian+Publish/Introduction+to+Obsidian+Publish) site. Themes for Obsidian Publish use the same [CSS variables](https://docs.obsidian.md/Reference/CSS+variables/CSS+variables) as the Obsidian app along with [Publish-specific CSS variables](https://docs.obsidian.md/Reference/CSS+variables/CSS+variables#Obsidian Publish).

See [Build a theme](https://docs.obsidian.md/Themes/App+themes/Build+a+theme) for more in-depth information on the `body`, `:root`, `.theme-dark`, and `.theme-light` selectors.

To build a theme for your site:

1.  Add a file called `publish.css` to the root folder of your vault.
    *   You need to use a external editor to create this file, as Obsidian does not support editing CSS files.
2.  Publish `publish.css` to enable the theme on your live Publish site.

**Example:**

    .published-container {
      --page-width: 800px;
      --page-side-padding: 48px;
      
      /* ... CSS variables for Publish that do not change when light or dark mode is enabled. They sometimes link to color variables in .theme-light or .theme-dark */
    }
    
    .theme-light {
      --background-primary: #ebf2ff;
      --h1-color: #000000;
     
      /* ... CSS color variables for when light mode is enabled */
    }
    .theme-dark {
      --background-primary: #1f2a3f;
      --h1-color: #ffffff;
      
      /* ... CSS color variables for when dark mode is enabled */
    }
    

For more information on how to customize your site, refer to [Customize your site](https://help.obsidian.md/Obsidian+Publish/Customize+your+site).

Links to this page

[Publish](https://docs.obsidian.md/Reference/CSS+variables/Publish/Publish)

[Site fonts](https://docs.obsidian.md/Reference/CSS+variables/Publish/Site+fonts)

Build a Publish theme

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
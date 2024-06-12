[![](https://publish-01.obsidian.md/access/caa27d6312fe5c26ebc657cc609543be/Assets/obsidian-lockup-docs.svg)](https://docs.obsidian.md/Home)[Developer Documentation](https://docs.obsidian.md/Home)

Manifest

    cssClass: reference

This page describes the schema for the manifest, `manifest.json`.

Properties
------------

The following properties are available for both plugins and themes.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `author` | `string` | **Yes** | The author's name. |
| `minAppVersion` | `string` | **Yes** | The minimum required Obsidian version. |
| `name` | `string` | **Yes** | The display name. |
| `version` | `string` | **Yes** | The version, using [Semantic Versioning](https://semver.org/). |
| `authorUrl` | `string` | No | A URL to the author's website. |
| `fundingUrl` | `string` or [`object`](https://docs.obsidian.md/Reference/Manifest#fundingurl) | No | A URL or multiple URLs to where the users can support your project financially. |

Plugin-specific properties
----------------------------

The following properties are only available to plugins.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
| `description` | `string` | **Yes** | A description of your plugin. |
| `id` | `string` | **Yes** | The ID of your plugin. |
| `isDesktopOnly` | `boolean` | **Yes** | Whether your plugin uses NodeJS or Electron APIs. |

fundingUrl
------------

`fundingUrl` can either be a string with a single URL, or an object with multiple URLs.

**Single URL**:

    {
      "fundingUrl": "https://buymeacoffee.com"
    }
    

**Multiple URLs**:

    {
      "fundingUrl": {
        "Buy Me a Coffee": "https://buymeacoffee.com",
        "GitHub Sponsor": "https://github.com/sponsors",
        "Patreon": "https://www.patreon.com/"
      }
    }
    

Links to this page

[Mobile development](https://docs.obsidian.md/Plugins/Getting+started/Mobile+development)

[Submission requirements for plugins](https://docs.obsidian.md/Plugins/Releasing/Submission+requirements+for+plugins)

[Submit your plugin](https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin)

[Submit your theme](https://docs.obsidian.md/Themes/App+themes/Submit+your+theme)

[Versions](https://docs.obsidian.md/Reference/Versions)

Manifest

Not found

This page does not exist

Interactive graph

On this page

[Powered by Obsidian Publish](https://publish.obsidian.md)
Install and use the HubSpot Visual Studio Code extension


============================================================

Last updated: January 12, 2024

The HubSpot Visual Studio Code extension provides a set of tools to streamline local HubSpot development. Using the extension, you can install and manage the HubSpot CLI, authenticate and manage connected accounts, as well as quickly develop using HubL with syntax highlighting, autocomplete, boilerplate content, and more. 

Below, learn how to install and use the extension.

Install the extension[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#install-the-extension)
------------------------------------------------------------------------------------------------------------------------------------

To install the HubSpot VS Code extension:

*   In VS Code, navigate to **Preferences** \> **Extensions**.
*   In the search bar, search for **HubSpot**, then click **Install**.

A HubSpot panel will then be added to the left sidebar, which you can click to access HubSpot-specific actions, resources, and more.  
![vs-code-hubspot-extension-installed](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/vs-code-hubspot-extension-installed.png?width=1286&height=650&name=vs-code-hubspot-extension-installed.png)

Manage authenticated HubSpot accounts[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#manage-authenticated-hubspot-accounts)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Using the extension, you can manage the accounts that you want connected to the CLI, similar to using the [authentication CLI commands](/docs/cms/developer-reference/local-development-cli#authentication).

### Authenticate a new account

To authenticate a HubSpot account using the extension:

*   In the extension panel, under _Authentication_, click **Authenticate HubSpot Account**.![authenticate-hubspot-account](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/authenticate-hubspot-account.png?width=209&height=287&name=authenticate-hubspot-account.png)
*   In the dialog box, click **Open** to open HubSpot in a browser window.
*   In your browser, select the HubSpot account you want to authenticate, then click **Continue with this account**.
*   If you haven't generated an access key for your account yet, select the **permissions** you need, then click **Generate personal access key**.
*   In the dialog box, click **Open Visual Studio Code** to navigate back to VS Code.
*   You'll then be prompted to select whether this account should be set as the default account. Click **Yes** if you'd like CLI commands to interact with this account by default. You can change this at any time in the extension panel after authentication.
*   To authenticate more accounts, click **Authenticate additional HubSpot account**, then repeat the above process.  
    ![vs-code-extension-authenticate-additional-accounts](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/vs-code-extension-authenticate-additional-accounts.png?width=300&height=330&name=vs-code-extension-authenticate-additional-accounts.png)

### Manage connected accounts

Under _Accounts_, the extension panel will display all currently authenticated HubSpot accounts, with the current default account marked by a **star** icon.

![vs-code-extension-accounts](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/vs-code-extension-accounts.png?width=300&height=303&name=vs-code-extension-accounts.png)  
You can right-click the **account** to view account management options:

*   **Open design manager:** navigate to the account's [design manager](/docs/cms/developer-reference/design-manager).
*   **Show personal access key info:** navigate to the account's personal access key page. This can be useful if you need to copy the key, see its scopes, or deactivate it.
*   **Set as default account:** instruct the CLI to interact with the account by default when running commands.
*   **Rename account:** change the account's name in the CLI. This will only change the label that the CLI uses.
*   **Delete account:** remove the account from your list of authenticated accounts. This will not [delete the account](https://knowledge.hubspot.com/account/how-do-i-cancel-my-hubspot-account#crm-free-only).

![vs-code-extension-right-click-account](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/vs-code-extension-right-click-account.png?width=450&height=289&name=vs-code-extension-right-click-account.png)

File management[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#file-management)
------------------------------------------------------------------------------------------------------------------------

In the Remote file system (default account) section of the extension, you can view, upload, and manage files stored in the default account's [developer file system](/docs/cms/key-concepts#developer-file-system), which will reflect the files in the account's design manager. The files displayed in this section are read-only. Below, learn how to view, fetch, upload, watch, delete, and create new files.

### View files[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#view-files)

To view the default account's files, click to expand the Remote File System section in the left sidebar. You can refresh this view by clicking the ... options icon and selecting Refresh.

![remote-file-system-refresh](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/remote-file-system-refresh.png?width=951&height=350&name=remote-file-system-refresh.png)

### Upload files[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#upload-files)

To upload a new file or folder to the account:

*   Click the ... options icon, then select Upload.

![remote-file-system-upload](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/remote-file-system-upload.png?width=948&height=354&name=remote-file-system-upload.png)

*   Select the **file** or **folder** that you want to upload to the account.
*   Enter the **destination path** where the file or folder will live in HubSpot, including any file extensions (e.g. `/my-theme/images/examplefile.jpg`). You can nest files within another folder by including those folders in the path.

![remote-file-system-path-enter](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/remote-file-system-path-enter.png?width=1350&height=132&name=remote-file-system-path-enter.png)

You can find the path of an existing folder in the account's design manager. To open the design manager, right-click the account in the VS Code extension, then select **Open design manager**. Then, locate the folder in the left sidebar of the design manager, then right-click it and select **Copy path**.

![design-manager-copy-path (1)](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-manager-copy-path%20(1).png?width=400&height=365&name=design-manager-copy-path%20(1).png)

*   Press **Enter** to upload the file. The file system viewer will then update after upload. If an error occurs during upload, it will display in the bottom right of VS Code.

### Watch folders[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#watch-folders)

You can set a [watch](/docs/cms/developer-reference/local-development-cli#watch) on a folder to automatically upload changes within the folder on save. To watch a folder:

*   Click the **... options icon**, then select **Watch**.

![remote-file-system-watch](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/remote-file-system-watch.png?width=953&height=224&name=remote-file-system-watch.png)

*   Select the **folder** that you want to watch.
*   Enter the destination path where the folder will live in HubSpot, then press **Enter**.

![remote-file-system-path-enter](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/remote-file-system-path-enter.png?width=1350&height=132&name=remote-file-system-path-enter.png)

*   The extension will display a **sync icon** next to the folder in the left sidebar to indicate that it's being watched.  
    ![remote-file-system-sync-icon](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/remote-file-system-sync-icon.png?width=662&height=142&name=remote-file-system-sync-icon.png)
*   To end a watch, right-click the folder being watched, then select **End Watch**

**Please note:** only one file or folder can be watched at a time. To watch multiple files or folders simultaneously, you can instead watch the root directory or other parent directory.

### Delete and fetch files[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#delete-and-fetch-files)

To delete a file or folder from the account:

*   Right-click the **file** or **folder** that you want to delete, then select **Delete**.
*   You'll then be prompted to confirm whether you want to delete it. Click **Okay** to confirm the deletion.![delete-confirmation](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/delete-confirmation.png?width=874&height=188&name=delete-confirmation.png)

To download a file or folder from the account to your local environment:

*   Right-click the file or folder that you want to fetch, then select Fetch. 
*   You'll then be prompted to select the folder that you want to download it to. 

![vs-code-extension-right-click-file](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/vs-code-extension-right-click-file.png?width=400&height=194&name=vs-code-extension-right-click-file.png) 

### Create new files[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#create-new-files)

To generate scaffolded files for new CMS assets in VS Code:

*   In the left sidebar, click the Explorer icon to view your working directory.  
    ![vs-code-explorer-icon](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/vs-code-explorer-icon.png?width=694&height=588&name=vs-code-explorer-icon.png)
*   Right-click the File explorer panel and select one of the New options:
    *   **New template:** generates a new global partial, page, partial, or section template with boilerplate content.
    *   **New module:** generates a new module with boilerplate content.
    *   **New Serverless Function folder:** generates a `.functions` folder that contains boilerplate `serverless.js` and `serverless.json` files. You can add another serverless function to the folder by right-clicking the **folder**, then selecting **New serverless function**.

![create-new-files-extension](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/create-new-files-extension.png?width=405&height=455&name=create-new-files-extension.png)

HubL Language support[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#hubl-language-support)
------------------------------------------------------------------------------------------------------------------------------------

To enable HubL language support in your files, configure your VS Code file association settings:

*   In VS Code, open the command prompt by pressing `cmd` + `shift` + `p`.
*   Search for and select **Preferences: Open User Settings**. 
*   Choose the scope of your settings by clicking either the **User** or **Workspace** tab.
*   In the settings search bar, search for **files.associations**.
*   Click **Add item**, then add the following item-value pairs: 
    *   `*html`: `html-hubl`
    *   `*css`: `css-hubl`

![files-associations](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/files-associations.png?width=739&height=304&name=files-associations.png)

### Supported HubL syntax[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#supported-hubl-syntax)

When developing with HubL, the extension offers the following [HubL syntax](/docs/cms/hubl) support:

*   **Inline HubL linting:** checks your HTML, CSS, HTML + HubL, and CSS + HubL files for HubL-related errors and displays them inline.
*   **HubL syntax highlighting:** supports HubL syntax highlighting in the files associated through your VS Code language mode settings. Learn how to [set your file associations](#add-hubl-file-associations) below.
*   **Statement wrapping:** supports `{% %}`, `{# #}`, and `{{ undefined.undefined }}` [delimiters](/docs/cms/hubl#types-of-delimiters).
*   **Block comment toggling:** create HubL comments by pressing `cmd` + `/`. 
*   **Autocomplete:** offers autocomplete suggestions for supported HubL tags, filters, expression tests, and functions. [Learn more about autocomplete](#autocomplete-reference) below.
*   **Emmet** **for HTML + HubL files:** allows [Emmet](https://code.visualstudio.com/docs/editor/emmet) abbreviation and snippet expansions for HTML + HubL files. Learn how to [enable Emmet support](#enable-emmet-for-html-hubl-files) below.
*   **IntelliSense suggestions:** enables [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense#:~:text=You%20can%20trigger%20IntelliSense%20in,name%20to%20limit%20the%20suggestions.) suggestions when in snippet placeholders. Learn how to [enable IntelliSense Suggestions](#enable-intellisense-suggestions) below.

### Enable Emmet for HTML + HubL files[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#enable-emmet-for-html-hubl-files)

To enable [Emmet](https://code.visualstudio.com/docs/editor/emmet) support for abbreviations and snippet expansion in `html-hubl` files, map `html-hubl` to `html` in your Emmet settings:

*   In VS Code, open the command prompt by pressing `cmd` + `shift` + `p`.
*   Search for and select **Preferences: Open User Settings**. 
*   Choose the scope of your settings by clicking either the **User** or **Workspace** tab.
*   In the settings search bar, search for **Emmet: Include Languages**.
*   Click **Add item**, then add the following item-value pair: `html-hubl`: `html`.

![files-associations](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/files-associations.png?width=739&height=304&name=files-associations.png)

### Enable IntelliSense suggestions[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#enable-intellisense-suggestions)

To enable [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense#:~:text=You%20can%20trigger%20IntelliSense%20in,name%20to%20limit%20the%20suggestions.) suggestions when in snippet placeholders:

*   In VS Code, open the command prompt by pressing `cmd` + `shift` + `p`.
*   Search for and select **Preferences: Open User Settings**. 
*   Choose the scope of your settings by clicking either the **User** or **Workspace** tab.
*   In the settings search bar, search for **Editor** **Suggest: Snippets Prevent Quick Suggestions** and ensure that the checkbox is **cleared**.  
    ![intellisense-quick-suggestion](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/intellisense-quick-suggestion.png?width=735&height=163&name=intellisense-quick-suggestion.png)
*   Then, in the settings search bar, search for **Editor Parameter Hints Enabled** and ensure that the checkbox is **selected**.  
    ![intellisense-hints-enabled](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/intellisense-hints-enabled.png?width=585&height=137&name=intellisense-hints-enabled.png)

### Autocomplete reference[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#autocomplete-reference)

The HubSpot extension enables quick access to snippets that map to support HubL tags, filters, expression tests, and functions. To access autocomplete suggestions, you'll need to use the following prefixes:

*   [Expression tests](/docs/cms/hubl/operators-and-expression-tests): type the test name alone, then pres Enter. For example, typing `div` produces `divisibleby`.
*   **[Filters](/docs/cms/hubl/filters):** type `|` followed by the filter, then press Enter. For example, typing `|se` produces `|selectattr('attr', exp_test)`.
*   [Functions](/docs/cms/hubl/functions) and [tags](/docs/cms/hubl/tags): type `~` followed by the function or tag, then press Enter. For example, typing `~hub` produces `hubdb_table_rows(${table_id}`.
*   **[HubL supported variables](/docs/cms/hubl/variables):** type the **variable name** alone, then press **Enter**. For example, `content.ab` produces `{{ content.absolute_url` `}}`.
*   **[Module fields](/docs/cms/building-blocks/module-theme-fields-overview):** in JSON files, type the field type, then press Enter. For example: `ri` produces:

// typing ri > Enter produces: { "name": "richtext\_field", "label": "Rich text field", "required": false, "locked": false, "type": "richtext", "inline\_help\_text": "", "help\_text": "", "default": null }

### Other snippets[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#other-snippets)

Other snippets you can generate with the VS Code extension include:

 
| Snippet prefix | Description | Example |
| --- | --- | --- |
| `otrue` | Generates `overrideable=True` for HubL tags. | `overrideable=True` |
| `ofalse` | Generates `overrideable=False` for [HubL tags](/docs/cms/hubl/tags). | `overrideable=False` |
| `for` | Returns a basic [for loop](/docs/cms/hubl/for-loops). | 
`{% for iterable in dict %}`

`{{ iterable }}`

`{% endfor %}`



 |
| `if` | Returns a basic [if statement](/docs/cms/hubl/if-statements). | `{% if {condition} %} do_something {% endif %}` |
| `elif` | Returns an [else if](/docs/cms/hubl/if-statements#using-elif-and-else) statement to be used within an if statement. | 

`{% elif {condition} %}`



 |
| `else` | Returns an [else](/docs/cms/hubl/if-statements#using-elif-and-else) statement to be used within an if statement. | `{% else %}` |
| `hubldoc` | Returns a boilerplate HTML + HubL document. |   |
| `hublblog` | Returns boilerplate blog markup. |   |

The extension also offers autocomplete for file paths when used with the HubL tags and parameters below. To access file path autocompletions, start typing the HubL tag or parameter followed by a quotation mark.

*   `{% include "... %}`
*   `{% import "... %}`
*   `{% tag_name path="... %}`
*   `{% extend "... %}`

![autocomplete-path](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/autocomplete-path.png?width=602&height=69&name=autocomplete-path.png)

**Please note:** autocomplete will not pull in [HubSpot default module](/docs/cms/building-blocks/modules/default-modules) file paths.

Enable extension beta features[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#enable-extension-beta-features)
------------------------------------------------------------------------------------------------------------------------------------------------------

To enable HubSpot VS Code extension beta features:

*   In VS Code, open the command prompt by pressing `cmd` + `shift` + `p`.
*   Search for and select **Preferences: Open User Settings**. 
*   Choose the scope of your settings by clicking either the **User** or **Workspace** tab.
*   In the settings search bar, search for **HubSpot: Beta** and select the **checkbox**.

![enable-beta-features](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/enable-beta-features.png?width=979&height=199&name=enable-beta-features.png)

Telemetry[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#telemetry)
------------------------------------------------------------------------------------------------------------

HubSpot for VS Code collects user data in order to improve the extension’s experience. You can [review HubSpot’s privacy policy here](https://legal.hubspot.com/privacy-policy). Additionally, you may opt out of data collection by changing the setting for global telemetry in VS Code. To read more about VS Code and telemetry, including disabling telemetry reporting, [please read the official VS Code documentation](https://code.visualstudio.com/docs/getstarted/telemetry).

Contribute[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#contribute)
--------------------------------------------------------------------------------------------------------------

This extension is open source and HubSpot welcomes contributions as well as issues for feature requests and bug reports. For more information about contributing, see the [contributing docs](https://github.com/HubSpot/hubspot-cms-vscode/blob/master/CONTRIBUTING.md) to get started.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension#page-feedback)
--------------------------------------------------------------------------------------------------------------------------

Was this article helpful? Yes No

Thanks for letting us know. How would you describe this article?

 Inaccurate: it doesn’t reflect what I see in the product

 Unclear: it’s difficult to understand

 Missing information: it’s not comprehensive enough

 Irrelevant: it doesn’t match what I searched for

Great! Is there anything we could change to make it even more helpful? Is there anything we could change to make this article helpful?

 Allow HubSpot to contact me about my documentation feedback.

Email address

Only used if we need clarification on your feedback.

 

Thank you for your feedback, it means a lot to us.

Sorry this feedback form requires JavaScript to function.

This form is used for documentation feedback only. Learn how to [get help with HubSpot](https://knowledge.hubspot.com/account/get-help-with-hubspot).
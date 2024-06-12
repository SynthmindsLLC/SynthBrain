---
Please provide me with more context! I need to know what the mission is about in order to help you complete it. 

For example, tell me: "* **What is the purpose of the mission?**  What are you trying to achieve?"
* **Who is involved in the mission?**  Is it a personal mission, a team mission, or something else?
* **What are the goals of the mission?**  What specific outcomes are you hoping to see?
* **What is the time frame for the mission?**  Is it a short-term or long-term mission?

Once I have this information, I can help you develop a compelling and informative mission statement.
---

HubSpot CLI commands


========================

Last updated: May 9, 2024

The HubSpot CLI connects your local development tools to HubSpot, allowing you to develop on the HubSpot CMS with version control, your favorite text editor, and various web development technologies.

If you're new to developing on HubSpot, check out our quick start guide where you'll walk through installing the CLI all the way to publishing a live page.

[Quick start to CMS Hub development](https://developers.hubspot.com/cs/c/?cta_guid=c66b91fb-14b1-4c35-ab0d-7e4af8000592&signature=AAH58kGBc5oeNw3Wj6fW7Xi8Wrz_xfenUQ&portal_id=53&pageId=29844611102&placement_guid=28bfd0e9-ec05-48a5-b069-ce20015f54ac&click=f2e7ea8f-0ff0-4a63-83ad-650c2b6868ba&redirect_url=APefjpHLhRLGZiXIzWYJ_VrwdAKnSi3RxBfDRwjEsHzNKkPuiEm5mMFK0YDnrQUHHuXsu6gcpZNfiYt0S3K7qcYmfVvvTlD8pRzzaFmotV5IiWPVJjZoi_J6WbHHVrPnhgwiP5swIX5b6__8tCQW3_Pv0ARyQEGQGQ&hsutk=7b5c42bd7e6cffe21f6b4921f98ff2f0&canon=https%3A%2F%2Fdevelopers.hubspot.com%2Fdocs%2Fcms%2Fdeveloper-reference%2Flocal-development-cli&__hstc=20629287.7b5c42bd7e6cffe21f6b4921f98ff2f0.1715711134006.1715711134006.1715711134006.1&__hssc=20629287.1.1715711134006&__hsfp=1511885054&contentType=standard-page "Quick start to CMS Hub development") hbspt.cta.\_relativeUrls=true;hbspt.cta.load(53, '28bfd0e9-ec05-48a5-b069-ce20015f54ac', {"useNewLoader":"true","region":"na1"});

  
  
  
[View on GitHub](https://github.com/HubSpot/hubspot-cms-tools/)

Use this guide as a reference for the available commands and file formatting options for HubSpot's local development tooling. For a walkthrough of how to use these tools, see the [getting started with local development tutorial](/docs/cms/guides/getting-started-with-local-development). 

If you prefer, you can use [Yarn](https://classic.yarnpkg.com/en/docs/install) by running commands with the `yarn` prefix.

Show all commands[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#show-all-commands)
------------------------------------------------------------------------------------------------------------------------

Shows all commands and their definitions. To learn more about a specific command, add `--help` to the end of the command.

hs help

Install the CLI[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#install-the-cli)
--------------------------------------------------------------------------------------------------------------------

You can install HubSpot local development tools either globally (recommended) or locally. To install the HubSpot tools globally, in your command line run the command below.  To install locally, omit `-g` from the command.

npm install -g @hubspot/cli

### Install to just the current directory[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#install-to-just-the-current-directory)

To install the tools only in your current directory instead, run the command below. You do not need to install locally if you already have the CLI installed globally.

npm install @hubspot/cli

**Getting an EACCES error when installing?**  
See [NPM Resolving EACCESS permissions errors when installing packages globally](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally).

Update the CLI[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#update-the-cli)
------------------------------------------------------------------------------------------------------------------

The CLI is updated regularly. To upgrade to the latest version of the local tools, run:

npm install -g @hubspot/cli@latest

The CLI changed from `@hubspot/cms-cli` to `@hubspot/cli`. If you are still using the old cms-cli you will need to uninstall it prior to installing the new version.

To see which version you're on, run `hs --version`

If your version number is less than 3.0.0, you're on the old version.

To uninstall the old version run `npm uninstall -g @hubspot/cms-cli`

Authentication[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#authentication)
------------------------------------------------------------------------------------------------------------------

The following commands enable you to authenticate HubSpot accounts with the CLI so that you can interact with the account. If you haven't yet authenticated an account with the CLI, you'll first run `hs init` to create a `hubspot.config.yml` file, which will contain the authentication details for any connected HubSpot accounts. The rest of the commands will update that file.

Learn more in the [Getting started with local development guide](/docs/cms/guides/getting-started-with-local-development).

### init[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#init)

Creates your `hubspot.config.yml` file in the current directory and sets up authentication for an account. If you're adding authentication for a new account to an existing config file, run the [auth](#auth) command. When prompted for a name to use for the account, the name can't contain spaces.

hs init

### Authenticate an account[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#authenticate-an-account)

Generate authentication for a HubSpot account using a [personal access key](/docs/cms/personal-cms-access-key). You can [generate your access key here](https://app.hubspot.com/l/personal-access-key/). If you already have a `hubspot.config.yml` file you can use this command to add credentials for additional accounts. For example you might [use your sandbox account as a development environment.](/docs/cms/guides/creating-an-efficient-development-workflow#setting-up-your-development-environment) When prompted for a name to use for the account, the name can't contain spaces.

hs auth

### List authenticated accounts[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#list-authenticated-accounts)

Lists the name, ID, and auth type for the each account in your config file. If you're not seeing the accounts you expect, you may need to run the [auth](#auth) command to add accounts to your config file.

hs accounts list

### Set default account[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#set-default-account)

Set the default account in your config file.

hs accounts use accountNameOrID

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`accountNameOrID`

 | 

Identify the new default account by its name (as set in the config file) or ID.

 |

### Remove an account[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#remove-an-account)

Removes an account from your config file.

hs accounts remove accountNameOrID

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`accountNameOrID`

 | 

Identify the account to remove by its name (as set in the config file) or ID.

 |

### Remove invalid accounts[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#remove-invalid-accounts)

Removes any deactivated HubSpot accounts from your config file.

hs accounts clean

Interacting with the developer file system[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#interacting-with-the-developer-file-system)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Using the CLI, you can interact with the [developer file system](/docs/cms/key-concepts#developer-file-system), which is the file system in the [Design Manager](/docs/cms/developer-reference/design-manager). These commands enable you to create new assets locally, such as modules and themes, upload them to the account, list files in the HubSpot account, or download existing files to your local environment.

### List files[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#list-files)

List files stored in the developer file system by path or from the root. Works similar to using standard `ls` to view your current directory on your computer.

hs ls \[path\] hs list \[path\]

| Argument | Description |
| --- | --- |
| 
`dest`

Optional



 | 

Path to the remote developer file system directory you would like to list files for. If omitted, defaults to the account root.

 |

### Fetch files[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#fetch-files)

Fetch a file, or directory and its child folders and files, by path. Copies the files from your HubSpot account into your local environment.

By default, fetching will not overwrite existing local files. To overwrite local files, include the `--overwrite` flag.

hs fetch --account=<name> <src> \[dest\] hs filemanager fetch --account=<name> <src> \[dest\]

| Argument | Description |
| --- | --- |
| 
`src`

Required



 | 

Path in HubSpot Design Tools

 |
| 

`dest`

Optional



 | 

Path to the local directory you would like the files to be placed, relative to your current working directory. If omitted, this argument will default to your current working directory.

 |

| Options | Description |
| --- | --- |
| 
`--account`

 | 

Specify an `accountId` or name to fetch from

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |
| 

`--overwrite`

 | 

Overwrite existing files with fetched files.

 |
| 

`--mode`

 | 

Specify if fetching a draft or published version of a file from HubSpot. [Click here](#modes) for more info

 |

### Upload files[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#upload-files)

Upload a new local asset to your HubSpot account. Changes uploaded through this command will be live immediately. 

hs upload --account=<name> <src> <dest> hs filemanager upload --account=<name> <src> <dest>

| Argument | Description |
| --- | --- |
| 
`src`

Required



 | 

Path to the local file, relative to your current working directory.

 |
| 

`dest`

Required



 | 

Path in HubSpot Design Tools, can be a net new path.

 |

| Options | Description |
| --- | --- |
| 
`--account`

 | 

Specify a `accountId` or name to fetch from.

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |
| 

`--mode`

 | 

Specify if uploaded files are published in HubSpot. [See "modes"](#modes) for more info.

 |
| 

`--clean`

 | 

An optional flag that will delete the destination directory and its contents before uploading.

 |

| Subcommands | Description |
| --- | --- |
| 
`filemanager`

 | 

Uploads the specified src directory to the [File Manager](/docs/cms/features/file-manager), rather than to the [developer file system](/docs/cms/key-concepts#developer-file-system) in the Design Manager.

**Note**: Uploaded files will be set to _public_, making them viewable by anyone with the URL. See our [help documentation](https://knowledge.hubspot.com/cos-general/organize-edit-and-delete-files#edit-the-file-visibility-setting) for more details on file visibility settings.

 |

### Set a watch for automatic upload[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#set-a-watch-for-automatic-upload)

Watch your local directory and automatically upload changes to your HubSpot account on save. Any changes made when saving will be live immediately.

Keep the following in mind when using `watch`:

*   Deleting watched files locally will not automatically delete them from HubSpot. To delete files, use `--remove`.
*   Renaming a folder locally will upload a new folder to HubSpot with the new name. The existing folder in HubSpot will not be deleted automatically. To delete the folder, use `--remove`.

hs watch --account=<name> <src> <dest>

| Argument | Description |
| --- | --- |
| 
`src`

Required



 | 

Path to the local directory your files are in, relative to your current working directory

 |
| 

`dest`

Required



 | 

Path in HubSpot Design Tools, can be a net new path.

 |

| Options | Description |
| --- | --- |
| 
`--account`

 | 

Specify a `accountId` or name to fetch from

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |
| 

`--mode`

 | 

Specify if uploaded files are published or saved as drafts in HubSpot. [Learn more about using modes](#modes).

 |
| 

`--initial-upload`

 | 

Causes an initial upload to occur before file saves have occured. Supports an alias of `-i`

 |
| 

`--remove`

 | 

Will cause watch to delete files in your HubSpot account that are not found locally.

 |
| 

`--notify=<path/to/file>`

 | 

log to specified file when a watch task is triggered and after workers have gone idle.

 |

### Move files[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#move-files)

Moves files within the [developer file system](/docs/cms/key-concepts#developer-file-system) from one directory to another. Does not affect files stored locally.

hs mv --account=<name> <src> <dest>

| Argument | Description |
| --- | --- |
| 
`src`

Required



 | 

Path to the remote developer file system directory your files are in.

 |
| 

`dest`

Required



 | 

Path to move assets to within the developer file system.

 |

| Options | Description |
| --- | --- |
| 
`--account`

 | 

Specify a `accountId` or name to move files within.

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |

### Create new files[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#create-new-files)

Creates the folder/file structure of a new asset.

hs create <type> <name> \[dest\]

| Argument | Description |
| --- | --- |
| 
`type`

Required



 | 

Type of asset. Supported types include:

*   [`module`](/docs/cms/building-blocks/modules)
*   [`template`](/docs/cms/building-blocks/templates)
*   [`website-theme`](/docs/cms/building-blocks/themes/hubspot-cms-boilerplate)
*   [`function`](/docs/cms/features/serverless-functions/reference)
*   [`webpack-serverless`](https://github.com/HubSpot/cms-webpack-serverless-boilerplate)
*   [`react-app`](https://github.com/HubSpot/cms-react-boilerplate)
*   [`vue-app`](https://github.com/HubSpot/cms-vue-boilerplate)

 |
| 

`name`

Required



 | 

The name of the new asset

 |
| 

`dest`

Optional



 | 

The destination folder for the new asset, relative to your current working directory. If omitted, this will default to your current working directory.

 |

### Remove files[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#remove-files)

Deletes files, or folders and their files, from your HubSpot account. This does not delete the files and folders stored locally. This command has an alias of rm.

hs remove --account=<name> <path>

| Argument | Description |
| --- | --- |
| 
`path`

Required



 | 

Path in HubSpot Design Tools

 |

| Options | Description |
| --- | --- |
| 
`--account`

 | 

Specify a `accountId` or name to remove a file from.

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |

### Ignore files[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#ignore-files)

You can include a .hsignore file to specify files that should not be tracked when using the CLI. This file functions similar to how `.gitignore` files work. Files matching the patterns specified in the .hsignore file will not be uploaded to HubSpot when using the [upload](/docs/cms/developer-reference/local-development-cms-cli#upload) or [watch](/docs/cms/developer-reference/local-development-cms-cli#watch) commands.

By default there are some rules HubSpot automatically enforces. There is no way to override these defaults.

The following are always ignored:

*   `hubspot.config.yml`/`hubspot.config.yaml`
*   `node_modules` - dependencies
*   `.*` - hidden files/folders
*   `*.log` - NPM error log
*   `*.swp` - Swap file for Vim state
*   `Icon\\r` - Mac OS custom Finder icon
*   `__MACOSX` - Mac resource fork
*   `~` Linux Backup file
*   `Thumbs.db` - Windows image file cache
*   `ehthumbs.db` - Windows folder config file
*   `Desktop.ini` - Windows custom folder attribute information
*   `@eaDir` - Windows Synology diskstation "hidden" folder where the server stores thumbnails.

Shell script

Copy all

    # ignore all files within a specific directory
    /ignore/ignored
    # ignore a specific file
    /ignore/ignore.md
    # ignore all .txt files
    *.txt
    # ignore all log files - useful if you commonly output serverless function logs as files.
    *.log

Locally preview theme[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#locally-preview-theme)
--------------------------------------------------------------------------------------------------------------------------------

When developing a theme, you can run `hs theme preview` in the theme's root directory to render a live preview of your changes without uploading files to the account. The preview will run on a local proxy server at [https://hslocal.net:3000/](https://hslocal.net:3000/).

Once run, this command will run a watch process so that any saved changes are rendered in the preview. 

**Please note:** to allow the local server to run on https, HubSpot must generate a self-signed SSL certificate and register it with your operating system. This will require entering your sudo password.

hs theme preview <src> <dest>

| Argument | Description |
| --- | --- |
| 
`src`

Required



 | 

Path to the local file, relative to your current working directory. This command should be run in the theme's root directory..

 |
| 

`dest`

Required



 | 

The path for the preview. This can be any value, and is only used internally and for display purposes on the preview page.

 |

The main page at [https://hslocal.net:3000/](https://hslocal.net:3000/) will display a list of your theme's templates and modules, all of which can be individually previewed by clicking the provided links. You'll also see a list of the account's connected domains, which you can use to preview content on specific domains. The domain will be prepended to the `hslocal.net` domain.

![local-theme-preview-homepage](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/local-theme-preview-homepage.png?width=863&height=664&name=local-theme-preview-homepage.png)

HubDB Commands[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#hubdb-commands)
------------------------------------------------------------------------------------------------------------------

The HubDB commands are currently in Developer Preview. They are available to use now but understand they are subject to change.  Developer previews are subject to our [developer beta terms](https://legal.hubspot.com/developerbetaterms).

Use these commands to create, delete, fetch, and clear all rows of a HubDB table. The HubSpot account must have access to HubDB to use these commands.

### Create HubDB table[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#create-hubdb-table)

Create a new HubDB table in the HubSpot account. 

hs hubdb create <src>

| Argument | Description |
| --- | --- |
| 
`src`

Required



 | 

The local [JSON file](#hubdb-table-json) to use to generate the HubDB table.

 |

| Options | Description |
| --- | --- |
| 
`--account`

 | 

Specify a `accountId` or name to create HubDB in.

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |

### Fetch HubDB Table[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#fetch-hubdb-table)

Download a HubDB table's data to your computer.

hs hubdb fetch <tableId> <dest>

| Argument | Description |
| --- | --- |
| 
`tableId`

Required



 | 

HubDB table id found in the HubDB dashboard.

 |
| 

`dest`

 | 

The local path destination to store the `[hubdb.json](#hubdb-table-json)` file.

 |

When you fetch a HubDB the data is stored as `tablename.hubdb.json`. When you create a new table you must specify a source JSON file. Below is an example of a table in JSON format.

// store\_locations.hubdb.json { "name": "store\_locations", "useForPages": true, "label": "Store locations", "allowChildTables": false, "allowPublicApiAccess": true, "dynamicMetaTags": { "DESCRIPTION": 3, "FEATURED\_IMAGE\_URL": 7 }, "enableChildTablePages": false, "columns": \[ { "name": "name", "label": "Name", "type": "TEXT" }, { "name": "physical\_location", "label": "Physical Location", "type": "LOCATION" }, { "name": "street\_address", "label": "Street address", "type": "TEXT" }, { "name": "city", "label": "City", "type": "TEXT" }, { "name": "state", "label": "State", "options": \[ { "id": 1, "name": "Wisconsin", "type": "option", "order": null }, { "id": 2, "name": "Minnesota", "type": "option", "order": null }, { "id": 3, "name": "Maine", "type": "option", "order": null }, { "id": 4, "name": "New York", "type": "option", "order": null }, { "id": 5, "name": "Massachusetts ", "type": "option", "order": null }, { "id": 6, "name": "Mississippi", "type": "option", "order": null }, { "id": 7, "name": "Arkansas", "type": "option", "order": null }, { "id": 8, "name": "Texas", "type": "option", "order": null }, { "id": 9, "name": "Florida", "type": "option", "order": null }, { "id": 10, "name": "South Dakota", "type": "option", "order": null }, { "id": 11, "name": "North Dakota", "type": "option", "order": null }, { "id": 12, "name": "n/a", "type": "option", "order": null } \], "type": "SELECT", "optionCount": 12 }, { "name": "phone\_number", "label": "Phone Number", "type": "TEXT" }, { "name": "photo", "label": "Store Photo", "type": "IMAGE" } \], "rows": \[ { "path": "super\_store", "name": "Super Store", "isSoftEditable": false, "values": { "name": "Super Store", "physical\_location": { "lat": 43.01667, "long": -88.00608, "type": "location" }, "street\_address": "1400 75th Greenfield Ave", "city": "West Allis", "state": { "id": 1, "name": "Wisconsin", "type": "option", "order": 0 }, "phone\_number": "(123) 456-7890" } }, { "path": "store\_123", "name": "Store #123", "isSoftEditable": false, "values": { "name": "Store #123", "physical\_location": { "lat": 32.094803, "long": -166.85889, "type": "location" }, "street\_address": "Pacific Ocean", "city": "at sea", "state": { "id": 12, "name": "n/a", "type": "option", "order": 11 }, "phone\_number": "(123) 456-7891" } } \] }

### Clear rows in a HubDB table[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#clear-rows-in-a-hubdb-table)

Clear all of the rows in a HubDB table.

hs hubdb clear <tableId>

| Argument | Description |
| --- | --- |
| 
`tableId`

Required



 | 

HubDB table id found in the HubDB dashboard.

 |

| Options | Description |
| --- | --- |
| 
`--account`

 | 

Specify a `accountId` or name to clear HubDB rows from.

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |

### Delete HubDB table[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#delete-hubdb-table)

Deletes the specified HubDB table from the account.

hs hubdb delete <tableId>

| Argument | Description |
| --- | --- |
| 
`tableId`

Required



 | 

HubDB table id found in the HubDB dashboard.

 |

| Options | Description |
| --- | --- |
| 
`--account`

 | 

Specify a `accountId` or name to delete HubDB from.

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |

Serverless function commands[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#serverless-function-commands)
----------------------------------------------------------------------------------------------------------------------------------------------

Use these commands to create and debug [serverless functions](/docs/cms/features/serverless-functions) (**_CMS Hub_** _Enterprise_ only).

### Create a function[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#create-a-function)

Creates a serverless function using the [create](#create) command. Running this command will guide you through the steps of creating the function, such as naming its parent and function file and defining its methods and endpoint path.

hs create function

### List functions[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#list-functions)

Prints a list of all of the account's deployed functions, their endpoints, methods, the names of the secrets they use and last updated date.

hs functions ls --account=<name> hs functions list --account=<name>

| Argument | Description |
| --- | --- |
| 
`--account`

 | 

The HubSpot account nickname from your hubspot.config. This parameter is required if you do not have a [defaultAccount](/docs/cms/developer-reference/local-development-cms-cli#top-level-parameters) in your `hubspot.config`.

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |
| 

`--json`

 | 

Output JSON into the command line with data on all of the functions. The JSON data includes, portal id, function id, route, raw asset path, method, secrets, created and last modified dates.

 |

### Get logs[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#get-logs)

Prints a log from your serverless function. Displays any `console.logs` contained within your function after execution. Logs also include execution time. Logs are retained for 90 days. 

hs logs <endpoint-name> --account=<name> --follow

| Argument | Description |
| --- | --- |
| 
`endpoint-name`

Required



 | 

The endpoint name as defined in your serverless.json file (not the path to the function file).

 |
| 

`--file`

 | 

Output the logs to function.log

 |
| 

`--follow`

 | 

Tail the logs to get a live update as you are executing your serverless functions.

 |
| 

`--latest`

 | 

Output only the most recent log

 |
| 

`--account`

 | 

The HubSpot account nickname from your hubspot.config. This parameter is required if you do not have a [defaultPortal](/docs/cms/developer-reference/local-development-cms-cli#top-level-parameters) in your hubspot.config.

Supports an alias of `--portal` for backward compatibility with older versions of the CLI.

 |
| 

`--compact`

 | 

hides log output/info. Returns success/error and execution time.

 |
| 

`--limit=<number>`

 | 

 limit the amount of logs displayed in output

 |

If you receive this error: `A server error occurred: WARNING: The logs for this function have exceeded the 4KB limit`, your log is too large. This can be caused by trying to console log a very large object, or by a lot of separate console logs. To resolve this, reduce how much you're trying to log, hit your endpoint, then run the command again.

### Add a secret[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#add-a-secret)

Add a [secret](/docs/cms/features/serverless-functions#secrets) to your account which can be used within serverless functions. After running the command you will be prompted to enter the secret's value.

To expose the secret to your function, update your [`serverless.json`](/docs/cms/features/serverless-functions/reference#serverless-json) file with the secret's name, either to the specific endpoints you want to use it in or globally to make it available to all.

hs secrets add <secret-name>

| Argument | Description |
| --- | --- |
| 
`secret-name`

Required



 | 

Name of secret.

 |
| 

`secret-value`

Required



 | 

The secret's value (auth detail, or otherwise).

 |

### Update a secret[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#update-a-secret)

Update the value of a [secret](/docs/cms/features/serverless-functions#secrets) in your account which can be used within serverless functions. You will then be prompted to enter the secret's value.

**Please note:** due to caching, it can take about one minute to see updated secret values. If you've just updated a secret but are still seeing the old value, check again after about a minute.

hs secrets update <secret-name>

| Argument | Description |
| --- | --- |
| 
`secret-name`

Required



 | 

The name of the secret, which you'll later use to reference the secret. This can be any unique value, though it's recommended to keep it simple for ease of use.

 |

### Remove a secret[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#remove-a-secret)

Remove a [secret](/docs/cms/features/serverless-functions#secrets) from your account, making it no longer usable within serverless functions. After running this command, edit your [`serverless.json`](/docs/cms/features/serverless-functions/reference#serverless-json) file to remove the secret's name.

hs secrets delete <secret-name>

| Argument | Description |
| --- | --- |
| 
`secret-name`

Required



 | 

Name of secret you want to remove.

 |

### List secrets[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#list-secrets)

List [secrets](/docs/cms/features/serverless-functions#secrets) within your account to know what you have stored already using the add secrets command.

hs secrets list

Open browser shortcuts[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#open-browser-shortcuts)
----------------------------------------------------------------------------------------------------------------------------------

There are so many parts of the HubSpot app that developers need to access frequently. To make it easier to get to these tools you can open them directly from the command line. Your `defaultAccount` or `--account` argument will be used to open the associated tool for that account.

### open[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#open)

hs open <shortcut-name or alias>

| Argument | Description |
| --- | --- |
| 
`shortcut`

Required



 | 

Provide the full shortcut name or alias of the short cut you wish to open in your browser.

 |

hs open --list

| Argument | Description |
| --- | --- |
| 
`--list`

Required



 | 

Lists all of the shortcuts, their aliases and  destinations.

 |

Command completion[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#command-completion)
--------------------------------------------------------------------------------------------------------------------------

If you use the CLI frequently, it can be useful to be-able-to tab to auto-complete commands.

hs completion >> ~/.bashrc

For Mac OS X

hs completion >> ~/.bash\_profile

Evaluate themes and templates for SEO and accessibility[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#evaluate-themes-and-templates-for-seo-and-accessibility)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Uses [Google's Lighthouse tools](https://developer.chrome.com/docs/lighthouse/overview) to score the quality of your themes and templates for their adherence to the following categories:

*   Accessibility
*   Web best practices
*   Performance
*   PWA
*   SEO

The following types of templates are scored:

*   landing pages
*   website pages
*   Blog posts
*   Blog listing page

If any templates fail to generate a score because of Lighthouse errors, a list of these templates will be provided.  

hs cms lighthouse-score --theme=path

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`--theme-path`

Required



 | 

Path to a theme in the Design Manager.

 |
| 

`--verbose`

 | 

*   When this parameter is excluded, the returned score is an average of all the theme's templates (default).
*   When this parameter is included, the individual template scores are shown. You'll also receive [Lighthouse report](https://developer.chrome.com/docs/lighthouse/overview/#report-viewer) links for each template.

 |
| 

`--target`

 | 

This can either be desktop or mobile to see respective scores. By default, the target is desktop. 

 |

Generate theme field selectors for in-app highlighting[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#generate-theme-field-selectors-for-in-app-highlighting)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When creating a theme, use the following command to generate an `editor-preview.json` file which maps CSS selectors to theme fields. This enables content creators to see which theme elements will be impacted by updates to a field's styling options.

After running the command, you'll need to review and refine the `editor-preview.json` file to ensure that fields and selectors are mapped properly. While this command will make a rudimentary guess as to which fields affect which selectors, you'll need to make corrections based on how your theme is built. For example, this command cannot detect when modules are overriding styling or when you're using macros. Learn more about [theme editor field highlighting](/docs/cms/building-blocks/module-theme-fields-overview#theme-editor-field-highlighting).

hs theme generate-selectors <theme-directory-path>

Modes[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#modes)
------------------------------------------------------------------------------------------------

The \--mode option allows you to determine if local changes are published when uploaded to HubSpot. This option can be used in each command or set as a default in your hubspot.config.yml file.

The two options for \--mode are \--mode=draft and \--mode=publish.

The following is the order of precedence for setting \--mode:

1.  Using \--mode in a command will override all other settings.
2.  Setting a defaultMode for each account in your hubspot.config.yml file, removes the need to use \--mode in each command. It will override the top-level setting.
3.  Setting a defaultMode at the top-level in your hubspot.config.yml file, sets a default\--mode for all accounts. It will override the default behavior.
4.  The default behavior for \--mode is publish

Environment variables[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#environment-variables)
--------------------------------------------------------------------------------------------------------------------------------

The HubSpot CLI supports the use of environment variables, this can be especially useful when creating automations like a GitHub Action.

Run any command using the `--use-env` flag to use the environment variables instead of the `hubspot.config.yml`.

hs upload example-project example-project-remote --use-env

| Name | Description |
| --- | --- |
| 
`HUBSPOT_PORTAL_ID`

Required



 | 

The HubSpot account ID.

 |
| 

`HUBSPOT_PERSONAL_ACCESS_KEY`

Recommended



 | 

The [personal access key](/docs/cms/personal-access-key) of a user on the HubSpot account. All updates made will be associated to this user.

 |
| 

`HUBSPOT_CLIENT_ID`

 | 

The OAuth client ID.

 |
| 

`HUBSPOT_CLIENT_SECRET`

 | 

The OAuth secret.

 |

**Please note:** as of November 30, 2022, HubSpot API Keys are no longer supported. Continued use of HubSpot API Keys is a security risk to your account and data. During this deprecation phase, HubSpot may deactivate your key at any time.

You should instead authenticate using a private app access token or OAuth. Learn more about [this change](https://developers.hubspot.com/changelog/upcoming-api-key-sunset) and how to [migrate an API key integration](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app) to use a private app instead.

Marketplace asset validation[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#marketplace-asset-validation)
----------------------------------------------------------------------------------------------------------------------------------------------

 The CLI provides a suite of automated tests you can perform on your assets to get them in-line with the marketplace requirements prior to submitting. Passing all automated tests does not mean you will for sure pass the review process, further review is conducted to ensure quality beyond what can be easily automated.

### Validate theme[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#validate-theme)

The theme validation command allows you to quickly run automated tests on your theme to identify problems that need to be fixed prior to submission to the asset marketplace. These will be returned in your CLI as a list of \[error\] and \[success\] messages separated into groups that represent types of assets within a theme.

Before you can validate a theme, you'll first need to upload it to your account with `hs upload`. Then, run the following command to validate the uploaded theme.

hs theme marketplace-validate <src>

| Argument | Description |
| --- | --- |
| 
`src`

Required



 | 

Root relative path to the theme folder in the design manager. 

 |

### Validate module[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#validate-module)

Similar to validating a theme, this command allows you to quickly run automated tests on a module to identify problems that need to be fixed prior to submission to the asset marketplace. 

Before you can validate a module, you'll first need to upload it to your account with `hs upload`. Then, run the following command to validate the uploaded module.

hs module marketplace-validate <src>

| Argument | Description |
| --- | --- |
| 
`src`

Required



 | 

Root relative path to the module folder in the design manager. 

 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#page-feedback)
----------------------------------------------------------------------------------------------------------------------

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
---
Please provide me with more information! I need to know what your mission is about in order to help you. 

For example, tell me: "* **What is the purpose of the mission?**  What are you trying to achieve?"
* **Who is involved?**  Who is this mission for?
* **What are the key goals?**  What are the specific things you want to accomplish?
* **What is the timeline?**  When does this mission take place?

Once I have a better understanding of your mission, I can help you write a compelling and informative mission statement.
---

Getting started with local development


==========================================

Last updated: May 13, 2024

The [HubSpot CLI](/docs/cms/developer-reference/local-development-cms-cli) (Command Line Interface) connects your local environment to HubSpot, meaning you'll have local copies of your HubSpot web assets. This allows you to use version control, your favorite text editor and various web development technologies when developing on the HubSpot CMS. 

This guide is best for those who are already familiar with the CMS but want to learn about working with the CLI. If you are completely new to HubSpot CMS Hub development, we encourage you to follow the quickstart guide.

[Quick start to CMS Hub development](https://developers.hubspot.com/cs/c/?cta_guid=c66b91fb-14b1-4c35-ab0d-7e4af8000592&signature=AAH58kHify-r5w0eLoD2Gq9STiBIGF7dnQ&portal_id=53&pageId=29837710048&placement_guid=28bfd0e9-ec05-48a5-b069-ce20015f54ac&click=5a3f030b-154a-40a9-9bce-b943b1e81f08&redirect_url=APefjpGanAUA_5dbJxlAVJwbU0xIF9BF7Y05ChUNZz1KC_L9IRNh101U-0mExFAHndaYyMkeHaXwolN_05MfEJKd_HHwfSCM7WwalBD01F0qaB0I0saIw8_N_cCkq3xEgFqsxXzPUi0w-6eQ5MFgQMsMjL6S-53gUQ&hsutk=e0f621748f2081b00b19015fb8021f93&canon=https%3A%2F%2Fdevelopers.hubspot.com%2Fdocs%2Fcms%2Fguides%2Fgetting-started-with-local-development&__hstc=20629287.e0f621748f2081b00b19015fb8021f93.1715711065397.1715711065397.1715711065397.1&__hssc=20629287.1.1715711065397&__hsfp=1511885054&contentType=standard-page "Quick start to CMS Hub development") hbspt.cta.\_relativeUrls=true;hbspt.cta.load(53, '28bfd0e9-ec05-48a5-b069-ce20015f54ac', {"useNewLoader":"true","region":"na1"});

In this tutorial, you'll learn:

*   How to install the CLI and connect it to your HubSpot account.
*   How to fetch a module from your HubSpot account.
*   How to update the module locally, then upload your changes.
*   How to use the `watch` command to continue uploading saved changes.

For more commands and local file formats, see the [Local Development Tooling Reference](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli).

Install dependencies[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development#install-dependencies)
----------------------------------------------------------------------------------------------------------------------------------

To develop on HubSpot locally, you'll need to:

1.  Install [Node.js](https://nodejs.org/en/), a Javascript runtime environment that enables the local tools. Versions 16 or higher of Node are supported, but we recommend the long-term support (LTS) version.
2.  Run npm install -g @hubspot/cli in your command line to install the HubSpot CLI globally. To install the tools in only your current directory instead, run npm install @hubspot/cli.

If you prefer, you can also use [Yarn](https://classic.yarnpkg.com/en/docs/install). If you are using Yarn, commands are run with the yarn prefix.

**Getting an EACCES error when installing?**   
See [NPM Resolving EACCESS permissions errors when installing packages globally](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally).

1\. Create a working directory[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development#create-a-working-directory)
--------------------------------------------------------------------------------------------------------------------------------------------------

Create a folder for the work you'll be doing below. For the purposes of this tutorial, name the folder `local-dev-tutorial`.

You can do this locally by running mkdir local-dev-tutorial in the command line, which will create the directory. Then, run cd local-dev-tutorial to navigate to that directory.

2\. Configure the local development tools[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development#configure-the-local-development-tools)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, run `hs init` to connect the tools to your HubSpot account. This command will walk you through the steps below.

*   To connect the CLI to a HubSpot account, you'll need to copy the account's personal access key. When prompted, press Enter to open hubspot.com to the [personal access key page of the account](https://app.hubspot.com/l/personal-access-key). If you have multiple accounts, you'll be prompted in the browser to select an account first.
*   On the personal access key page, you can generate a new personal access key or copy the existing key value if one already exists.
    *   If you're creating a key for the first time, select which scopes the key has access to. You'll need to select at least the Design Manager permission to interact with the account's design tools. 
    *   After selecting the key's permissions, click **Generate personal access key**.
*   Once a key has been generated, copy its value by first clicking **Show** under the key, then clicking **Copy**.
*   Paste the key into the command line, then press **Enter**.

*   Next, enter a name for the account. This name is only seen and used by you when running commands. For example, you might use "sandbox" if you're using a developer sandbox or "company.com" if you’re using a standard account. This name can't contain spaces. 
*   Press **Enter**. 

With the init flow complete, you'll see a success message confirming that a configuration file, [hubspot.config.yml](//developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli#authentication), has been created in your current directory.

Your hubspot.config.yml will look something like this:

defaultPortal: mainProd portals: - name: mainProd portalId: 123456 defaultMode: publish authType: personalaccesskey auth: tokenInfo: accessToken: >- {accessTokenValue} expiresAt: '2023-06-27T19:45:58.557Z' personalAccessKey: >- {personalAccessKeyValue} sandboxAccountType: null parentAccountId: null

Use this table to describe parameters / fields
| Name | Description |
| --- | --- |
| 
`defaultPortal`

Optional



 | 

The account that is interacted with by default when running CLI commands.

To interact with an authenticated account that is not set as the default, you can add a `--account=` flag to the command, followed by the account name or ID. For example, `--account=12345` or `--account=mainProd`.

 |
| 

`name`

Optional



 | 

Under `portals` you'll find an entry for each connected account. `name` specifies the given name for the account. You can use this name when [setting a new default account](/docs/cms/developer-reference/local-development-cli#set-default-account) or specifying an account with the `--account` flag.

 |
| 

`portalId`

Required



 | 

The account ID.

 |
| 

`defaultMode`

Optional



 | 

When uploading to the account, sets the default state to upload content as. Can be either `draft` or `publish`.

 |
| 

`authType`

Required



 | 

The form of authentication used to auth the account. 

 |
| 

`sandboxAccountType`

Optional



 | 

If the account is a sandbox account, indicates the ID of the parent production account.

 |
| 

`parentAccountId`

Optional



 | 

parentAccountId

 |

The `hubspot.config.yml` file supports multiple accounts. To authenticate more accounts, run [`hs auth`](/docs/cms/developer-reference/local-development-cms-cli#auth) and follow the prompts.

3\. Create an asset to fetch in HubSpot[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development#create-an-asset-to-fetch-in-hubspot)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

For the purpose of this tutorial, you'll first create a new asset in HubSpot so that you can fetch it to your local environment using the CLI. 

*   In your HubSpot account, navigate to **Marketing** > **Files and Templates** > **Design tools**. This will open the design manager, which is where you can access the files you upload using the CLI. This tree of files and folders is also referred to as the [developer file system](/docs/cms/key-concepts#developer-file-system).
*   In the left sidebar of the design manager, select the **@hubspot** folder to view HubSpot's default assets, such as themes and modules.  
    ![design-manager-hubspot-folder](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-manager-hubspot-folder.png?width=1798&height=832&name=design-manager-hubspot-folder.png)
*   In the left sidebar, scroll down to and right-click the **icon** module, then select **Clone module**. The module will be cloned to the root of the developer file system, and your new module copy will be opened on the right.  
    ![default-icon-module-cloned](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/default-icon-module-cloned.png?width=400&height=316&name=default-icon-module-cloned.png)
*   At the top of the left sidebar, click **Actions**, then select **Copy path**. This will copy the relative path to the module in the developer file system, which you'll use in the next step to fetch the module locally.   
    ![module-actions-copy-path](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/module-actions-copy-path.png?width=600&height=400&name=module-actions-copy-path.png) 

4\. Fetch the module to your local environment[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development#fetch-the-module-to-your-local-environment)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

With the module cloned, you'll now use the [fetch](/docs/cms/developer-reference/local-development-cms-cli#fetch) command to bring it into your local environment.

In the terminal, run `hs fetch '/icon copy.module'`.

hs fetch '/icon copy.module'

The module will be downloaded as a directory containing five files:  

*   `fields.json`: contains the code for the module's various fields. In this case, this includes the icon field, two accessibility option fields, and a set of style fields. You can see these fields in the right sidebar of the module editor in HubSpot.
*   `meta.json`: contains the module's basic information, such as its label, ID, and the types of templates it can be used in. This information will be displayed in the right sidebar of the module editor.
*   `module.css`: contains the module's CSS, which you can also see in the CSS pane of the module editor in HubSpot. 
*   `module.html`: contains the module's HTML, which you can also see in the HubL + HTML pane of the module editor in HubSpot.
*   `module.js`: contains the module's JavaScript, which you can also see in the JS pane of the module editor in HubSpot.  
    ![module-directory-local](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/module-directory-local.png?width=1306&height=562&name=module-directory-local.png)

Next, you'll make an update to the module's `meta.json` file, then upload it to your account and view the change in HubSpot.

5\. Make changes and upload[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development#make-changes-and-upload)
--------------------------------------------------------------------------------------------------------------------------------------------

First, make a change to the module:

*   In your preferred code editor, open the module's `meta.json` file.  
    ![module-meta-json-file-open](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/module-meta-json-file-open.png?width=600&height=331&name=module-meta-json-file-open.png)
*   Update the `label` field from `"Icon"` to `"CMS tutorial module"`. Then, save the file.  
    ![module-meta-json-file-label-updated](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/module-meta-json-file-label-updated.png?width=752&height=436&name=module-meta-json-file-label-updated.png)

Before running the next command, `hs upload`, let's break down the command and the arguments it takes. This command takes two arguments: `hs upload <src> <dest>`  

*   `src`: the relative path of the source folder that you're uploading from your local environment.
*   `dest`: the path of the destination directory in HubSpot, local to the root of the developer file system. You can create a new directory in the account by specifying the directory name, such as `hs upload <src> /new-directory`.
*   With that in mind, because you're uploading to the root of the developer file system, run the following command:

hs upload 'icon copy.module' 'icon copy.module'

*   After the CLI confirms that the module has been successfully uploaded, refresh the design manager to view your change in HubSpot. You should now see that the _Label_ field shows your new value.

![module-label-updated](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/module-label-updated.png?width=1062&height=598&name=module-label-updated.png)

6\. Run a watch to automatically upload changes[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development#run-a-watch-to-automatically-upload-changes)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now that you've used the `upload` command to run a one-time upload of your local files, you'll now use the `watch` command to continuously upload saved changes. This command takes the same arguments as `upload`, so you can specify the same `<src>` and `<dest>` as above.

*   Run `hs watch 'icon copy.module' 'icon copy.module'`

hs watch 'icon copy.module' 'icon copy.module'

With the watch now running, saved changes will automatically upload to the HubSpot account. As a demonstration, make the following local change to the module:

*   In the `meta.json` file, update the `host_template_types` field to remove `"BLOG_LISTING"` and `"BLOG_POST"` so that the module is only available for pages:  
      
    `"host_template_types"``:["PAGE"]`
*   Ten, save the file. This should prompt the CLI to automatically upload the file to HubSpot.
*   With the file uploaded, refresh the design manager in HubSpot to view your change. The _Template types_ section of the right sidebar should now only include _Page_.

![module-editor-template-type](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/module-editor-template-type.png?width=400&height=228&name=module-editor-template-type.png)

*   To end the watch, press `Control + C`. It's important to note that you won't be able to run other commands in the same terminal window that the watch command is running in. To run other commands while running a watch, you should instead open another terminal window and execute your commands there.

Next steps[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development#next-steps)
--------------------------------------------------------------------------------------------------------------

Now that you've walked through how to use the `fetch`, `upload`, and `watch` commands, you may want to check out the full [CLI command reference guide](/docs/cms/developer-reference/local-development-cli) to learn what else you can do with the CLI.

It's also recommended to check out the following tutorials:

*   [Creating an efficient development workflow](/docs/cms/guides/creating-an-efficient-development-workflow)
*   [How to set up continuous integration with GitHub](/docs/cms/guides/github-integration)
*   [Getting started with custom modules](/docs/cms/guides/getting-started-with-modules)
*   [Getting started with themes](/docs/cms/guides/getting-started-with-themes)
*   [Getting started with drag and drop areas](/docs/cms/guides/creating-a-drag-and-drop-area)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development#page-feedback)
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
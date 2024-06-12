---
Please provide me with the rest of the mission statement so I can help you complete it. 

For example, you could tell me: "* **The organization or project the mission statement is for.** This will help me understand the context and tailor the mission statement to the specific goals and values."
* **What the organization or project aims to achieve.** This will give me a clearer idea of the overall purpose and direction.
* **The key values or beliefs that guide the organization or project.** This will help me craft a mission statement that reflects the organization's core principles.

Once I have this information, I can help you craft a compelling and effective mission statement.
---

Developer projects setup guide (BETA)
=====================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

To develop HubSpot projects, you’ll first need to set up your local environment, including installing the HubSpot CLI and connecting it to your HubSpot account. While getting set up, you may also want to create a development sandbox in your production account so that you can develop your project in a siloed environment before deploying to the production account.

Below, learn how to connect your production account to the CLI then create a development sandbox within it. After setting up your local environment, you can proceed to [creating a project](/docs/platform/create-a-project). To learn more about the CLI commands you'll be using, check out the [project-specific CLI commands reference](/docs/platform/project-cli-commands).

**Please note:** for a complete guide to creating a UI extension, including these setup steps, check out the [UI extensions quickstart guide](/docs/platform/ui-extensions-quickstart).

Set up your local environment[](https://developers.hubspot.com/docs/platform/developer-projects-setup#set-up-your-local-environment)
------------------------------------------------------------------------------------------------------------------------------------

 To set up your local environment, you'll first need to: 

*   Install [Node.js](https://nodejs.org/en/download/) which enables HubSpot’s local development tools. Versions 16 and higher are supported.
*   Install the HubSpot CLI globally by running `npm install -g @hubspot/cli@next` in the terminal. This command will also update the CLI to the latest version if you’ve already installed it.

With the CLI installed, you can now connect it to the account you'll be uploading to. Note that you do not need to complete these steps now if you'll be following the [quickstart guide](/docs/platform/ui-extensions-quickstart).

*   In the terminal, navigate to the directory where you’ll be working.
*   Run `hs init`.
*   Press **Enter** to open the personal access key page in your browser.
*   Select the **production** **account** that you want to deploy to, then click **Continue with this account**. You’ll then be redirected to the personal access key page of the account.
*   To retrieve your personal access key:
    *   If you haven't generated a key yet:
        *   Ensure that the **Developer projects**, **Sandboxes**, and **Serverless functions** checkboxes are selected, then click **Generate personal access key**.
        *   Click **Show** to reveal the key, then click **Copy** to copy it to your clipboard.
    *   If you've already generated a key, next to _Personal CMS Access Key_, click **Show** to reveal your key, then click **Copy** to copy it to your clipboard. Your key must include the following scopes to create projects, apps, and sandboxes. If your key is missing these scopes, you'll need to deactivate it and create a new one.
        *   `developer.projects.write`
        *   `developer.app_functions.read`
        *   `developer.app_functions.write`
        *   `developer.sandboxes.read`
        *   `developer.sandboxes.write`
        *   `sandboxes.read`
        *   `sandboxes.write`

**Please note:** when connecting the CLI to an existing sandbox account, you can ignore the sandbox-related scopes above. Personal access keys in sandbox accounts don't have access to those scopes because you cannot create a sandbox within a sandbox.

*   Paste the copied key into the terminal, then press **Enter**.
*   Enter a unique name for the account, which is only used when running CLI commands. Then, press **Enter**.

The CLI will display a success message confirming that the `hubspot.config.yml` file was created, which stores your connected accounts. After creating this file, you can add more accounts by running the `hs auth` command. At any time, you can view all the currently connected accounts by running `hs accounts list`. 

When you later run commands to upload, fetch, or watch a project, HubSpot will use the account that’s set as the default in the file. When developing on multiple accounts, you can change the default account by running `hs accounts use accountName`. You can also interact with a specific account by adding the following flag to the end of a command: `--account=accountName`.

Below, learn more about developing in sandbox accounts.

Create and use development sandboxes[](https://developers.hubspot.com/docs/platform/developer-projects-setup#create-and-use-development-sandboxes)
--------------------------------------------------------------------------------------------------------------------------------------------------

After following the steps above to connect a production account to the CLI, you can create a development sandbox within it to setup a lightweight testing environment. This enables you to develop your apps and extensions in a siloed environment before deploying to a production account. 

Before proceeding, review the following development sandbox limits:

*   A production account can have only two development sandboxes at a time.
*   CRM object definitions are synced from the production account to the development sandbox at the time of sandbox creation. If you create properties in the production account after creating the sandbox, they will not automatically sync over. Learn how to [resync a development sandbox](#resync-a-development-sandbox).
*   You cannot create a sandbox within another sandbox.

### Create a development sandbox[](https://developers.hubspot.com/docs/platform/developer-projects-setup#create-a-development-sandbox)

To set up a development sandbox account:

*   Because development sandboxes are created within the `defaultPortal` in your `hubspot.config.yml` file, first confirm that your production account is connected and set as the default:
    *   In the terminal, run `hs accounts list`.
    *   In your list of connected accounts, confirm that your production account is listed as the default account.  
        ![hs-acounts-list-default](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hs-acounts-list-default.png?width=457&height=130&name=hs-acounts-list-default.png)
    *   If your production account is not the default, run `hs accounts use` and select your production account.
*   After confirming your production account is the default, run `hs sandbox create`. 
*   You'll then be prompted to select a type of sandbox to create. Select **Development sandbox**, then press **Enter**.
*   Enter a `name` for the sandbox account, then press **Enter**.
*   Following the prompts, enter `y` (yes) or `n` (no) to select what you'll be syncing:
    *   **Sync CRM object definitions:** sync the current CRM object definitions from the production account to the sandbox. This includes all custom CRM properties and custom objects. If you don't sync CRM object definitions, the sandbox will be created with only the standard set of CRM properties along with two example contacts.
    *   **Include up to 100 most recent contact records and associations:** while syncing CRM object definitions, this option will create CRM records for the 100 most recently created production account contacts, along with up to 100 associated companies, 100 associated deals, and 100 associated ticket records. You can only perform this sync once per development sandbox, and only if you've chosen to sync CRM object definitions.
    *   To skip the sync, enter `n`, then press **Enter**. You can later sync the sandbox either [in HubSpot or using the CLI](#resync-a-development-sandbox).

*   The CLI will then begin the sandbox setup process. Once the sandbox is fully set up and synced, you'll see a _Sandbox sync complete_ confirmation. 

With your development sandbox created, it will appear under the associated production account when running `hs accounts list`.

If you want to set the development sandbox as your default account, run `hs accounts use`, then select the **sandbox**. To deploy to your sandbox or production account, you can either run `hs accounts use` to set the default account, or manually select the account when uploading by running `hs project upload --account=<name-of-account>`.

![cli-connected-accounts-sandbox](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/cli-connected-accounts-sandbox.png?width=377&name=cli-connected-accounts-sandbox.png)

After setting up your development sandbox, learn how to quickly create a UI extension by jumping to [section three of the UI extensions quickstart guide](/docs/platform/ui-extensions-quickstart#start-local-development). Or, learn more about [projects](/docs/platform/create-a-project), [private apps](/docs/platform/create-private-apps-with-projects), and [UI extensions](/docs/platform/create-ui-extensions).

Learn more about the [CLI commands](/docs/platform/project-cli-commands#sandbox-commands) you can use to interact with both standard and development sandboxes.

### View a development sandbox in HubSpot[](https://developers.hubspot.com/docs/platform/developer-projects-setup#view-a-development-sandbox-in-hubspot)

By default, only the user who created the development sandbox can access it in HubSpot. However, you can enable other users to access it by [adding them as users to the development sandbox](https://knowledge.hubspot.com/settings/add-and-remove-users). Super admins who haven't been added as users will still be able to view the development sandbox details in HubSpot, and can delete the sandbox if needed.

![sandbox-request-access](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/sandbox-request-access.png?width=479&name=sandbox-request-access.png)

To access the development sandbox account in HubSpot:

*   In your HubSpot account, navigate to **CRM Development** in the main navigation bar.
*   In the left sidebar menu, select **Sandboxes**.
*   Click the **Development** tab, where your new sandbox will be listed along with its name, create date, and the user who created it. 
*   To navigate to the sandbox account, click the **development sandbox name**.

Once a non-super admin user has been granted access to a development sandbox, they can access it by clicking the **Profile picture** in the top right of HubSpot, then clicking the **Account selection menu** and selecting the account.

![portal-picker-hobbes](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/portal-picker-hobbes.png?width=299&name=portal-picker-hobbes.png)

### Delete a development sandbox[](https://developers.hubspot.com/docs/platform/developer-projects-setup#delete-a-development-sandbox)

*   To delete a development sandbox using the CLI, run `hs sandbox delete`, then follow the prompts.
*   To delete a development sandbox in HubSpot:
    *   In your HubSpot account, navigate to **CRM Development** in the main navigation bar.
    *   In the left sidebar menu, select **Sandboxes**.
    *   Click the **Development** tab.
    *   Hover over the development sandbox, then click **Delete**.

![delete-development-sandbox](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/delete-development-sandbox.png?width=984&height=134&name=delete-development-sandbox.png)

### Resync a development sandbox[](https://developers.hubspot.com/docs/platform/developer-projects-setup#resync-a-development-sandbox)

After creating a development sandbox, new properties and property groups created in the production account will not automatically sync over to the sandbox. You can resync the development sandbox as needed either from the CLI or within HubSpot:

*   To resync a development sandbox in the CLI:
    *   First ensure that the development sandbox is set as the default account by running `hs accounts use`, then selecting the **sandbox**.
    *   With the sandbox set as the default, run `hs sandbox sync`.
    *   Following the prompts, enter `y` (yes) or `n` (no) to select what you'll be syncing:
        *   **Sync CRM object definitions:** sync the current CRM object definitions from the production account to the sandbox. This includes all custom CRM properties and custom objects.
        *   **Include up to 100 most recent contact records and associations:** if you didn't perform this one-time sync during sandbox creation, this option will also create CRM records for the 100 most recently created contacts in the production account, along with up to 100 of their associated company, deal, and ticket records. You can only perform this sync once per development sandbox, and only if you've chosen to sync CRM object definitions.
*   To resync a development sandbox in HubSpot:
    *   In your HubSpot account, navigate to **CRM Development** in the main navigation bar.
    *   In the left sidebar menu, select **Sandboxes**.
    *   Click the **Development** tab.
    *   To the right of the sandbox, click **Set up sync to sandbox**.  
        ![set-up-sync-development-sandbox](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/set-up-sync-development-sandbox.png?width=1002&height=135&name=set-up-sync-development-sandbox.png)
    *   In the right panel, review what you'll be syncing. If you haven't performed a one-time sync of the production account's contacts and associated records, you can select the **checkbox** to include that data in the sync. This will sync the 100 most recently created contacts from the production account, along with up to 100 associated deals, 100 associated companies, and 100 associated tickets.  
          
        ![set-up-sync-development-sandbox-include-contacts](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/set-up-sync-development-sandbox-include-contacts.png?width=552&height=653&name=set-up-sync-development-sandbox-include-contacts.png)
    *   Click **Sync to development sandbox**.
    *   When the sync is complete, the _Last sync status_ will display any changes synced to the sandbox.

Properties and property groups from the following CRM objects will then be synced:

*   Contacts
*   Companies
*   Deals
*   Tickets
*   Custom objects

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/developer-projects-setup#page-feedback)
----------------------------------------------------------------------------------------------------------

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
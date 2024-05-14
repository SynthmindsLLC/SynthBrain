HubSpot Account Types
=====================

 There are several types of HubSpot accounts, each with a distinct purpose. Below, learn about each account type and what they're intended for.  

Standard HubSpot accounts[](https://developers.hubspot.com/docs/api/account-types#standard-hubspot-accounts)
------------------------------------------------------------------------------------------------------------

A standard HubSpot account is the most common type of account. It’s where you’ll find all the tools, features, and settings included with your HubSpot plan. It can be free or paid, and is used as your production environment.

A standard HubSpot account will have access to all the tools and features included with your plan.

App developer accounts[](https://developers.hubspot.com/docs/api/account-types#app-developer-accounts)
------------------------------------------------------------------------------------------------------

App developer accounts are free accounts intended for creating and managing apps, integrations, and developer test accounts. They're also where you can create and manage App Marketplace listings. However, app developer accounts and their associated test accounts aren’t connected to a standard HubSpot account. They can’t sync data or assets to or from another HubSpot account. 

App developer accounts can be identified by a banner at the top of any page that says _This_ _is an app_ _developer account_. ![](https://paper-attachments.dropbox.com/s_FE997E185BD47B083EA9B7C65FEC2822D18406AA9C2CBDB7FA3CA77217D16F19_1626814303990_App+dev+account+info+alert+option+3.png)

Get started by creating an [app developer account](/get-started).

Developer test accounts[](https://developers.hubspot.com/docs/api/account-types#developer-test-accounts)
--------------------------------------------------------------------------------------------------------

Within [app developer accounts](#app-developer-accounts), you can create developer test accounts to test apps and integrations without affecting any real HubSpot data. Developer test accounts do not mirror production accounts, but are instead free HubSpot accounts with access to a 90-day trial of many enterprise features, with the following limitations:

*   **Marketing** **Hub:** you can only send marketing emails to addresses of users who you've added to your developer test account.
*   **CMS Hub:** the number of pages you can create are subject to the following limits:  
    *   **Website pages:** 25
    *   **Blogging tools:** 1 blog with up to 100 posts
    *   **Landing pages:** 25
*   **Workflows:** a maximum of 100,000 records can be enrolled per day in workflows created in a developer test account. If this daily limit is reached:  
    *   Any additional attempted enrollment beyond this limit will be dropped.
    *   Users will be informed in app that they reached the daily record enrollment limit, as well as what time the limit will be refreshed.

You can create up to 10 test accounts per developer account. This type of account cannot sync data with other accounts, and they can't be connected to a standard HubSpot account. Test accounts can be identified by a banner at the top of the page, which includes how many days are left before it expires. 

![trial-banner](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/trial-banner.png?width=631&name=trial-banner.png)

Below, learn more about creating and managing test accounts.

### Create a developer test account[](https://developers.hubspot.com/docs/api/account-types#create-a-developer-test-account)

To create a developer test account:

*   In the top navigation bar of your app developer account, click **Testing**.
*   In the upper right, click **Create an app test account**.
*   Enter an **account name**, then click **Create**.

To access and manage your developer test accounts:

*   In the top navigation bar of your app developer account, click **Testing**.
*   Hover over the **account** you want to manage, then select an action:
    *   To delete the account, click **Delete**.
    *   To copy the account ID, renew the account, or rename it, click the **More** dropdown menu.

![developer-account-test-accounts](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/developer-account-test-accounts.png?width=985&name=developer-account-test-accounts.png)

### Renew a developer test account

Developer test accounts will expire after 90 days if no API calls are made to the account. You can either manually renew the account from the _Testing_ page in HubSpot, or by making an API call to the account. Keep the following in mind when attempting to renew the account via API call:

*   This only applies to API requests made using [OAuth tokens](/docs/api/oauth/tokens) generated from an application in the same developer account as the test account you want to renew.
*   Renewals must be made no more than 30 days before the test account’s expiration date. 

Sandbox accounts[](https://developers.hubspot.com/docs/api/account-types#sandbox-accounts)
------------------------------------------------------------------------------------------

Sandbox accounts allow you to test out changes without impacting your standard account. Learn more about the different types of sandbox accounts in the sections below.

### Standard sandbox accounts[](https://developers.hubspot.com/docs/api/account-types#standard-sandbox-accounts)

If you have an _Enterprise_ subscription, you can create a standard sandbox account that provides a safe and secure environment where you can test new workflows, integrations, website pages, and other important changes without impacting anything in your standard account. These sandboxes copy the structure of your standard account.

These accounts can be identified by a yellow banner at the top of the page that includes the label: _You're in \[name of sandbox\], which is a standard sandbox account_. The banner will also include a link back to your production account for easy switching.

![standard-sandbox-banner](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/standard-sandbox-banner.png?width=725&height=136&name=standard-sandbox-banner.png)

Learn more about standard sandbox accounts on [HubSpot's Knowledge Base](https://knowledge.hubspot.com/account/set-up-a-hubspot-standard-sandbox-account).

### CMS sandbox accounts[](https://developers.hubspot.com/docs/api/account-types#cms-sandbox-accounts)

CMS sandboxes are free accounts intended for building and testing website changes without impacting your standard account or live website. Similar to app developer accounts, CMS sandbox accounts are not connected to your standard HubSpot account. 

You can [create a CMS sandbox account for free](https://offers.hubspot.com/free-cms-developer-sandbox).

CMS sandboxes don’t have a banner, but they only have access to HubSpot’s free tools and _CMS Hub_ _Enterprise_, minus the ability to connect a domain.

### Development sandbox accounts (BETA)[](https://developers.hubspot.com/docs/api/account-types#development-sandbox-accounts-beta-)

If you have a Sales Hub or Service Hub Enterprise subscription, you can create a development sandbox account through the CLI for local development. You can gain access to development sandbox accounts by [opting into the CRM developer tools beta in your standard HubSpot account.](https://knowledge.hubspot.com/account/opt-your-hubspot-account-into-a-beta-feature) 

Development sandboxes can be identified by a yellow banner at the top of the page that reads: _You're in \[name of sandbox\], which is a development sandbox account._

![development-sandboxes-banner](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/development-sandboxes-banner.png?width=1190&height=123&name=development-sandboxes-banner.png)

Marketplace provider accounts[](https://developers.hubspot.com/docs/api/account-types#marketplace-provider-accounts)
--------------------------------------------------------------------------------------------------------------------

Marketplace Provider accounts are intended for creating and managing [Template Marketplace listings](/docs/cms/marketplace-guidelines) and transactions. To get started selling on the Template Marketplace, [create a Template Marketplace provider account](https://app.hubspot.com/signup-hubspot/asset-provider?_gl=1*1xpzfk0*_ga*MjE0MDM5NjAwMS4xNjg3MjUxNjQz*_ga_LXTM6CQ0XK*MTY4NzMxMTYzMi4yLjAuMTY4NzMxMTYzMi42MC4wLjA.). If you're a [HubSpot Partner](https://www.hubspot.com/partners), you already have Marketplace Provider functionality in your Partner account.

A Marketplace Provider account can be identified by a Template Marketplace item in the top navigation menu. 

![template-marketplace-acct](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/template-marketplace-acct.png?width=678&height=238&name=template-marketplace-acct.png) 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/account-types#page-feedback)
------------------------------------------------------------------------------------------

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
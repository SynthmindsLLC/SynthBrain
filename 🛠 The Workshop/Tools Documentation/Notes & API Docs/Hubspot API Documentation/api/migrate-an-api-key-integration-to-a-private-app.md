Migrate an API key integration to a private app
===============================================

If you're seeing a banner in your account about deactivating your API key:

*   Ensure that you've migrated all impacted integrations, then [deactivate the API key](https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key#deactivate-your-api-key).
*   To check if the account's API key has been used in the past seven days, you can [view your API key call log history](https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key#view-your-api-key-call-log). The call log will not show any requests made with the key more than seven days ago.
*   Apps listed on the [_Connected apps_ page of your account settings](https://knowledge.hubspot.com/integrations/connect-apps-to-hubspot#:~:text=You%20can%20view%20all%20your,Connected%20Apps%20page.) do not need to be migrated, as they authenticate with OAuth.

*   Developer API keys are separate from standard HubSpot API keys, and are not being deprecated. Developer API keys are used for managing settings related to your HubSpot apps, including [webhooks API](/docs/api/webhooks) subscriptions and [timeline events API](/docs/api/crm/timeline) event types.

If you've built an internal integration that uses a [HubSpot API key](https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key), your API key provides both read and write access to all of your HubSpot CRM data, which can be a security risk if your API key is compromised. By migrating to a private app, you can authorize the specific scopes that your integration requires, which generates an access token that limits the data that your integration can request or change in your account.

Follow the steps below to migrate an existing API key integration to a private app. It's recommended you first use a test environment, such as a [developer test account](/docs/api/creating-test-accounts) or [sandbox account](https://knowledge.hubspot.com/account/set-up-a-hubspot-sandbox-account), before making changes in production. If you have questions while migrating your app, visit the [Developer Community](https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers). 

For a video walkthrough of migrating an API key integration to a private app, check out the HubSpot Developers video below:  
  

In this guide
-------------

*   [Create a new private app](#create-a-new-private-app)
*   [Update the authorization method of your integration's API request](#update-the-authorization-method-of-your-integration-s-api-requests)
*   [Verify requests and monitor logs](#verify-requests-and-monitor-logs)
*   [Implementation examples](#implementation-examples)

**Please note:** private apps do not support webhooks and [certain types of extensions](/docs/api/crm/extensions/overview). If your existing integration uses any of these features, you should create a public app using [OAuth](/docs/api/working-with-oauth) instead.

Create a new private app[](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#create-a-new-private-app)
--------------------------------------------------------------------------------------------------------------------------------------------

*   In your HubSpot account, click the **settings icon** in the main navigation bar.
*   In the left sidebar menu, navigate to **Integrations** > **Private Apps**.
*   Click **Create private app**.
*   On the _Basic Info_ tab, configure the details of your app:
    *   Enter your app's **name**.
    *   Hover over the placeholder logo and click the **upload icon** to upload a square image that will serve as the logo for your app.
    *   Enter a **description** for your app.
*   Click the **Scopes** tab.
*   Next, select the scopes to authorize based on the APIs that your integration uses. To find out which scopes your app will need:
    *   Compile a list of HubSpot APIs that your existing integration uses.
    *   For each API request, navigate to the associated developer documentation (e.g., the [contacts API](/docs/api/crm/contacts)).
    *   Click the **Endpoints** tab, then scroll to the endpoint your integration is using.
    *   Under the _Requirements_ section, locate the scopes required to use the endpoint. Whenever possible, you should opt for scopes listed under _Granular scopes_ instead of the ones under _Standard scopes_. If no granular scopes are listed, use the standard scopes.![locate-scope-in-endpoints-tab-for-private-app-migration](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/locate-scope-in-endpoints-tab-for-private-app-migration.png?width=1880&name=locate-scope-in-endpoints-tab-for-private-app-migration.png)
    *   Back in the settings for your private app, select the **Read** or **Write** checkboxes next to the matching scopes. You can also search for a scope using the _Find a scope_ search bar.![select-matching-scope-for-private-app](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/select-matching-scope-for-private-app.png?width=1912&name=select-matching-scope-for-private-app.png)
*   After you're done selecting your scopes, click **Create app** in the top right. You can always make changes to your app after you create it.
*   In the dialog box, review the info about your app's access token, then click **Continue creating**.

With your private app created, you can start making API requests using its access token. On the _Details_ tab of the settings page of your private app, click Show token under your access token to reveal it.

![show-private-app-access-token-migration-guide](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/show-private-app-access-token-migration-guide.png?width=938&name=show-private-app-access-token-migration-guide.png)

Update the authorization method of your integration's API requests[](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#update-the-authorization-method-of-your-integration-s-api-requests)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instead of using a `hapiKey` query parameter to make API requests, private app access tokens are included in the `Authorization` header of your request. When making a request, set the value of the `Authorization` header to `Bearer YOUR_ACCESS_TOKEN`. Unless otherwise noted, this method of authorization is compatible with all public API endpoints, including the legacy APIs listed on HubSpot's [legacy developer documentation](https://legacydocs.hubspot.com/docs/overview).

Your request may resemble the following:

axios.get('https://api.hubapi.com/crm/v3/objects/contacts', { headers: { 'Authorization': \`Bearer ${YOUR\_ACCESS\_TOKEN}\`, 'Content-Type': 'application/json' } }, (err, data) => { // Handle the API response } );$headers = \[ 'Content-Type: application/json', 'Authorization: Bearer ' . YOUR\_ACCESS\_TOKEN, \]; $curl = curl\_init(); curl\_setopt($curl, CURLOPT\_HTTPHEADER, $headers); curl\_setopt($curl, CURLOPT\_URL, 'https://api.hubapi.com/crm/v3/objects/contacts'); curl\_setopt($curl, CURLOPT\_RETURNTRANSFER, true); $contacts = curl\_exec($curl); curl\_close($curl); var\_dump($contacts);require 'uri' require 'net/http' require 'openssl' url = URI("https://api.hubapi.com/crm/v3/objects/contacts") http = Net::HTTP.new(url.host, url.port) http.use\_ssl = true http.verify\_mode = OpenSSL::SSL::VERIFY\_NONE request = Net::HTTP::Get.new(url) request\['content-type'\] = 'application/json' token = 'YOUR\_ACCESS\_TOKEN' request\['authorization'\] = "Bearer #{token}" response = http.request(request) puts response.read\_bodyimport requests url = "https://api.hubapi.com/crm/v3/objects/contacts" headers = { 'content-type': 'application/json', 'authorization': 'Bearer %s' % YOUR\_ACCESS\_TOKEN } response = requests.request("GET", url, headers=headers) print(response.text)

Private app access tokens are implemented on top of OAuth, so you can also make authenticated calls with your access token using one of HubSpot's client libraries. For example, if you're using the [Node.js client library](https://github.com/HubSpot/hubspot-api-nodejs), you can instantiate an OAuth client by passing in your app's access token. 

const hubspotClient = new hubspot.Client({ accessToken: YOUR\_ACCESS\_TOKEN }); $hubSpot = \\HubSpot\\Factory::createWithAccessToken('access-token'); $response = $hubSpot->crm()->contacts()->basicApi()->getPage();\# Load the gem require 'hubspot-api-client' # Setup client client = Hubspot::Client.new(access\_token: 'YOUR\_ACCESS\_TOKEN') # Get contacts contacts = client.crm.contacts.basic\_api.get\_pagefrom hubspot import HubSpot api\_client = HubSpot(access\_token='YOUR\_ACCESS\_TOKEN') api\_client.crm.contacts.get\_page()

To complete the migration over to your private app, remove all references to the HubSpot API key from your code, and instead use the approach above to use your private app's access token. Depending on the request you're making, you may want to create a secret to store your token, rather than hard coding it in your requests. Using a secret will prevent your token from being exposed, such as when using a token in a [serverless function](#serverless-functions). To store the access token as a secret:

*   In the terminal, run `hs secrets add secretName`. It's recommended to name the secret something simple so that you can easily reference it in the future.
*   Paste the access token into the terminal, then press **Enter**.

You can then access your secret as an environment variable. Learn more in the [serverless functions example below](#serverless-functions).

To confirm that all references to your API key have been removed, you can check the call log in your HubSpot account:

*   In your HubSpot account, click the **settings icon** in the main navigation bar.
*   In the left sidebar, navigate to **Integrations > API key**.
*   Review the most recent requests in the _Call log_ tab to confirm that no recent requests have been made since removing all previous references over to use your private app's access token.

![check-api-key-call-log-after-migration](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/check-api-key-call-log-after-migration.png?width=881&name=check-api-key-call-log-after-migration.png)

If you have a paid _Marketing Hub_ account with [marketing contacts](https://knowledge.hubspot.com/contacts/marketing-contacts), and you previously [set contacts created by integrations using your API key as marketing contacts](https://knowledge.hubspot.com/integrations/manage-marketing-contacts-settings-for-your-integrations#set-contacts-created-by-api-key-apps-as-marketing-contacts), you must also do the same for your private app:

*   In your HubSpot account, click the **settings icon** in the main navigation bar.
*   In the left sidebar, navigate to **Integrations > Marketing contacts**.
*   Under _Your connected apps_, use the search bar to locate your private app, then click the **Turn on to sync contacts as marketing contacts** switch on.

![set-private-app-contacts-as-marketing-contacts](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/set-private-app-contacts-as-marketing-contacts.png?width=1112&name=set-private-app-contacts-as-marketing-contacts.png)

Once you've finished setting up your private app and you've confirmed all references to your API key have been removed in your code, you can [deactivate the key](https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key#deactivate-your-api-key).

Verify requests and monitor logs[](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#verify-requests-and-monitor-logs)
------------------------------------------------------------------------------------------------------------------------------------------------------------

Once you've removed all references to the HubSpot API key in your code and replaced them with references to your private app's access token instead, no further code changes are required.

If you followed the steps above in a developer test or sandbox account, repeat the same process in your production account. Then, monitor your private app's API call logs and confirm that none of your app's requests return `400` errors:

*   In your HubSpot account, click the **settings icon** in the main navigation bar.
*   In the left sidebar menu, navigate to **Integrations** > **Private Apps**.
*   Click the **name** of your private app.
*   Click the **Logs** tab.
*   Any unsuccessful API request that failed due to a missing scope will appear as a `403` error. If you access the runtime logs of your integration, the response from the corresponding API request should include an error message with details about any missing scopes.

![403-error-after-private-app-migration](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/403-error-after-private-app-migration.png?width=925&name=403-error-after-private-app-migration.png)

*   If you need to include a new scope for your private app:
    *   Click the **Details** tab.
    *   Click **Edit details**.
    *   At the top of the page, click **Scopes**.
    *   Select the **checkbox** next to any missing scopes, then click **Commit changes** in the top right when you're done.

![select-missing-scopes-private-app-migration](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/select-missing-scopes-private-app-migration.png?width=993&name=select-missing-scopes-private-app-migration.png)

Learn more about creating and managing private apps, along with their limits, in the [private apps guide](/docs/api/private-apps).

Implementation examples[](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#implementation-examples)
------------------------------------------------------------------------------------------------------------------------------------------

Below, learn more about common API key usages and how to migrate to private app access tokens instead.

### Serverless functions[](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#serverless-functions)

If you’re using an API key within a [serverless function](/docs/cms/data/serverless-functions), you can similarly use the private app’s access token for authentication. You'll need to ensure that the private app has the [scopes](/docs/api/working-with-oauth#scopes) that the function needs to execute. 

To authenticate a serverless function with a private app access token:

*   On the _Access_ _token_ card, click **Show token** to reveal your access token. Then click **Copy** to copy the token to your clipboard.  
    ![show-private-app-access-token-1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/show-private-app-access-token-1.png?width=957&name=show-private-app-access-token-1.png)
*   With your access token copied, create a new secret to store the token:
    *   In the terminal, run `hs secrets add secretName`. It's recommended to name the secret something simple so that you can easily reference it in the future.
    *   Paste the access token into the terminal, then press **Enter**.
*   In your serverless function's `serverless.json` file, add the secret name to the `secrets` array:

// example serverless.json file { "runtime": "nodejs18.x", "version": "1.0", "secrets": \["secretName"\], "endpoints": { "getPrompts": { "method": "GET", "file": "serverlessFunction.js" } } }

*   In your serverless function's JavaScript file, set the value of the `Authorization` header to `Bearer secretName`. For example, if you're making a call to the [Contacts API](https://developers.hubspot.com/docs/api/crm/contacts) using Node.js and [axios](https://www.npmjs.com/package/axios), the request would look like the following:

// example serverless function const axios = require('axios'); exports.main = (context, sendResponse) => { axios.get(\`https://api.hubapi.com/crm/v3/objects/contacts\`, { headers: { 'Authorization': \`Bearer ${process.env.secretName}\`, 'Content-Type': 'application/json' } } ) sendResponse({statusCode: 200}); };

Learn more about [making API calls with your app's token](/docs/api/private-apps#make-api-calls-with-your-app-s-access-token).

### One-time jobs[](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#one-time-jobs)

If you’re using an API key for running one-time jobs, such as [creating a property](/docs/api/crm/properties), you can instead create a private app and use its access token to authenticate the call. Once a private app is created, you can reuse its access token for any one-time jobs, as long as the private app has the proper [scopes](https://developers.hubspot.com/docs/api/working-with-oauth#scopes). You can update a private app’s scopes at any time from the private app’s settings in HubSpot. Or, you can delete the private app and create a new one specific to the job you need to run.

![private-app-edit-scopes](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/private-app-edit-scopes.png?width=461&name=private-app-edit-scopes.png)

### Create custom objects[](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#create-custom-objects)

Instead of using an API key to [create a custom object](/docs/api/crm/crm-custom-objects), you can instead create a private app and use its access token to authenticate the call, as long as the app has the necessary [scopes](/docs/api/working-with-oauth#scopes). For example, when using Postman to create a custom object, set the authorization type to Bearer token, then enter the token into the _Token_ field.

![postman-private-app-access-token-field](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/postman-private-app-access-token-field.png?width=849&name=postman-private-app-access-token-field.png)

Learn more about creating a custom object using a private app on [HubSpot's developer blog](/blog/how-to-build-a-custom-object-using-private-apps).

### Custom code workflow actions[](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#custom-code-workflow-actions)

If you’re using an API key in a [_Custom code_ workflow action](/docs/api/workflows/custom-code-actions#create-a-custom-code-action), you can instead use the private app’s access token, as long as the app has the necessary [scopes](/docs/api/working-with-oauth#scopes). To make the update, open the custom action in the workflow editor, then make the following updates:

*   First, [add a new secret](/docs/api/conversations/code-snippets-in-bots) that contains the private app access token.  
    ![workflow-action-add-secret](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/workflow-action-add-secret.png?width=447&name=workflow-action-add-secret.png)
*   Then [update the action code](/docs/api/workflows/custom-code-actions#secret) with the new secret. 

const hubspotClient = new hubspot.Client({ accessToken: process.env.secretName });

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#page-feedback)
----------------------------------------------------------------------------------------------------------------------------

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
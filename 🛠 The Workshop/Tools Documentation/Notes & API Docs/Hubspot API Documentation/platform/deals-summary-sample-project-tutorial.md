---
Please provide me with more context! I need to know what the mission is about in order to help you. 

For example, tell me: "* **What is the mission for?** (Is it a company, a project, a personal goal, etc.?)"
* **What is the overall purpose or objective?** (What are you trying to achieve?)
* **What are the key values or principles?** (What will guide your actions?)
* **What is the desired outcome?** (What do you want to see happen as a result of this mission?)

Once I have this information, I can help you write a compelling and impactful mission statement.
---

Deals summary sample project tutorial (BETA)
============================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

To better understand how to build UI extensions and get the most out of CRM data, extension components, and project development, HubSpot provides a set of [sample projects](/docs/platform/sample-projects) featuring a variety of functionalities. These sample projects can server as inspiration, reference, or a starting point for your own UI extensions. 

By the end of this tutorial, you will have:

*   Uploaded the deal summary sample project to your account.
*   Created two deal records to supply the custom card with example data.
*   Customized the card with a component to display calculated deal data. 

For the purposes of this tutorial, it's recommended to complete these steps in a [development sandbox](/docs/platform/developer-projects-setup#create-and-use-development-sandboxes) account to keep this example data separate from the production account. 

If you haven't created a UI extension yet, it's recommended to [follow the quickstart guide](/docs/platform/ui-extensions-quickstart) first.

Update your CLI and authenticate your account[](https://developers.hubspot.com/docs/platform/deals-summary-sample-project-tutorial#update-your-cli-and-authenticate-your-account)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To get started, you'll first need to ensure that your CLI is on the latest version that your account is authenticated. If this is your first time setting up your local environment, check out the [projects setup guide](/docs/platform/developer-projects-setup).

*   Update to the latest CLI version by running `npm install -g @hubspot/cli@next`.
*   If you haven't yet connected your production account to the CLI, run `hs init` to create the necessary `hubspot.config.yml` file. You can either create this file in your working directory or in one of its parent directories. When working locally, the CLI will use whichever config file is closest, meaning you can also have multiple config files depending on your preferred workflow.

Clone the sample project and upload to your account[](https://developers.hubspot.com/docs/platform/deals-summary-sample-project-tutorial#clone-the-sample-project-and-upload-to-your-account)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

With your local environment set up, you'll now download the sample project and upload it to your account. You'll then be able to view the extension's custom card on any contact record in your account.

*   Clone the [sample app](https://github.com/HubSpot/ui-extensions-examples/tree/main/deals-summary) to your working directory.
*   Upload the sample app to your account by running `hs project upload`, then follow the CLI prompts to complete the upload.
*   With the project uploaded, log in to your HubSpot account.
*   In your HubSpot account, navigate to **Contacts** > **Contacts**.
*   Click the **name** of any contact record. If you're in a new account, you can click the **Brian Halligan** sample contact, or click **Create contact** in the upper right to create a new test contact.
*   On the contact record, click the **Custom** tab at the top of the record. On this tab, you'll see the uploaded sample project card titled _Deals summary_. Because you haven't yet created any deals associated with the contact, the card will show no data.  
    ![deals-summary-tutorial-empty-state](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/deals-summary-tutorial-empty-state.png?width=561&height=292&name=deals-summary-tutorial-empty-state.png)

**Please note:** if the project uploaded successfully but you're not seeing the custom card on the contact record, you may need to click **Customize tabs** to add the card to the _Custom_ tab first.

Next, you'll create two deals associated with the contact to populate the card with data.

Create two deals[](https://developers.hubspot.com/docs/platform/deals-summary-sample-project-tutorial#create-two-deals)
-----------------------------------------------------------------------------------------------------------------------

If your test contact has no deals associated with it, you'll need to create two deals to fill the custom card with data.

*   In the _Deals_ card in the right sidebar of the contact record, click **\+ Add**.  
    ![contact-record-create-deal](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/contact-record-create-deal.png?width=336&height=155&name=contact-record-create-deal.png)
*   In the right panel, give the deal a **Deal name** and **amount**. Then, click **Create and add another** at the bottom of the panel.
*   Repeat the same step as above to give the second deal a **Deal name** and **amount**. Then, click **Create** at the bottom of the panel.

Because you created these deals from the contact record, they'll automatically be associated with the contact. If you now refresh the page, the card will populate with the aggregated deal data.  
![sample-app-contact-with-deals](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/sample-app-contact-with-deals.png?width=588&height=401&name=sample-app-contact-with-deals.png)Next, you'll start the local development server and update your project with authentication so that you can fetch more deal data using HubSpot's API.

Start local development[](https://developers.hubspot.com/docs/platform/deals-summary-sample-project-tutorial#start-local-development)
-------------------------------------------------------------------------------------------------------------------------------------

By starting a local development server, you'll be able to update the card's frontend and see your saved changes without needing to upload first. And by adding the private app access token to the project, you'll enable the serverless function to make authenticated requests to the [HubSpot deals API](/docs/api/crm/deals). Learn more about [running the local development server](/docs/platform/ui-extensions-quickstart#start-local-development) and [managing secrets](/docs/platform/serverless-functions#managing-secrets).

*   Run `npm install` to install dependencies needed for running the local development server.
*   Inside the `src/app/app.functions` folder, create a new file named `.env` to store your private app access token.
*   Retrieve the private app's access token:
    *   In your HubSpot account, navigate to **CRM Development**.
    *   In the left sidebar menu, navigate to **Private apps**.
    *   Click **Deals summary app** to navigate to the app's overview page.
    *   Click the **Auth** tab.
    *   In the _Access token_ section, click **Show token**. Then, click **Copy**.  
        ![private-app-show-token](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-show-token.png?width=988&height=418&name=private-app-show-token.png)
    *   Paste the token into your `.env` file using the following format:

PRIVATE\_APP\_ACCESS\_TOKEN=your-access-token

*   Save the file.
*   Start the local development server by running `hs project dev`, then following the prompts to select the account to develop in.
*   Return the contact record in HubSpot and refresh the browser. You should now see an icon on the card that says _DEVELOPING LOCALLY_.  
    ![deals-summary-card-developing-locally](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/deals-summary-card-developing-locally.png?width=578&height=290&name=deals-summary-card-developing-locally.png)

Next, you'll update your local extension files to fetch deal data with the API, calculate average deal margin, and add a new component to the card.

Add the average margin component[](https://developers.hubspot.com/docs/platform/deals-summary-sample-project-tutorial#add-the-average-margin-component)
-------------------------------------------------------------------------------------------------------------------------------------------------------

You'll now update the card with a new component to display the calculated average deal margin. You'll first update the card's backend (serverless function), then the frontend React files.

### Update the serverless function[](https://developers.hubspot.com/docs/platform/deals-summary-sample-project-tutorial#update-the-serverless-function)

*   In your project files, open the `get-data.js` file. This serverless function is using the HubSpot API client to fetch associated deal data through the `getAssociatedDeals` function.
*   Add the following function to the bottom of the file, below the `calculateTotalAmounts` function.

function calculateAverageAmount(deals) { const totalCount = deals.length; const amounts = deals.map((deal) => parseFloat(deal.properties.amount)); const totalDeals = amounts.reduce((sum, amount) => sum + amount, 0); const average = Math.ceil(totalDeals / totalCount); return -Math.round(-average); }

*   To store the result of this function, update `exports.main` with a new variable, then add that variable to the existing `sendResponse`.

const avgAmount = calculateAverageAmount(deals); sendResponse({ dealsCount: deals.length, totalAmount, avgAmount });

### Update the React frontend[](https://developers.hubspot.com/docs/platform/deals-summary-sample-project-tutorial#update-the-react-frontend)

*   Open the `DealsSummary.jsx` file, then add the following state variable to define the initial state of the average amount.

const \[avgAmount, setAvgAmount\] = useState(0);

*   Update the state within the `useEffect` function.

setAvgAmount(serverlessResponse.response.avgAmount);

*   Lastly, add a new [`StatisticsItem` component](/docs/platform/ui-extension-components#statistics) to display the averaged amount in the card.

<StatisticsItem label="AVG MARGIN" number={avgAmount}> <Text>Low End</Text> </StatisticsItem>

After making the above changes, the `DealsSummary.jsx` file should contain the following code:

// for HubSpot API calls const hubspot = require('@hubspot/api-client'); exports.main = async (context = {}, sendResponse) => { const { hs\_object\_id } = context.propertiesToSend; const deals = await getAssociatedDeals(hs\_object\_id); const totalAmount = calculateTotalAmount(deals); const avgAmount = calculateAverageAmount(deals); sendResponse({ dealsCount: deals.length, totalAmount, avgAmount }); }; async function getAssociatedDeals(hs\_object\_id) { const hubSpotClient = new hubspot.Client({ accessToken: process.env\['PRIVATE\_APP\_ACCESS\_TOKEN'\], }); const objectData = await hubSpotClient.crm.contacts.basicApi.getById( hs\_object\_id, null, null, \['deals'\] ); const dealIds = objectData.associations.deals.results.map((deal) => deal.id); const deals = await hubSpotClient.crm.deals.batchApi.read({ inputs: dealIds.map((id) => ({ id })), }); return deals.results; } function calculateTotalAmount(deals) { const amounts = deals.map((deal) => parseFloat(deal.properties.amount)); return amounts.reduce((sum, amount) => sum + amount, 0); } function calculateAverageAmount(deals) { const totalCount = deals.length; const amounts = deals.map((deal) => parseFloat(deal.properties.amount)); const totalDeals = amounts.reduce((sum, amount) => sum + amount, 0); const average = Math.ceil(totalDeals / totalCount); return -Math.round(-average); }

With your changes saved, you should now see the new component in the card displaying the calculation.

![deals-summary-card-changes](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/deals-summary-card-changes.png?width=870&height=305&name=deals-summary-card-changes.png)

*   To quit the local development server and upload your finished work, press `q` in the terminal, then run `hs project upload`.

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/deals-summary-sample-project-tutorial#page-feedback)
-----------------------------------------------------------------------------------------------------------------------

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
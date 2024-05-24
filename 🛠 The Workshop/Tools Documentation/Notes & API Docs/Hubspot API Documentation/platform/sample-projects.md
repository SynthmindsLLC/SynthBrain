Sample projects (BETA)
======================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

Create UI extensions using HubSpot's sample projects to get familiar with what's possible when building CRM UI extensions. These sample projects can be used as inspiration, reference, or starting points for your own projects.

Below, learn more about the currently available sample projects.

*   [Build a multi-step flow](#build-a-multi-step-flow)
*   [Create a deals summary](#create-a-deals-summary)
*   [Custom logger example](#custom-logger-example)
*   [Display an iframe modal](#display-an-iframe-modal)Beginner
*   [Duplicate contact](#duplicate-contact)Beginner[](#use-crm-data-components)
*   [Generate multiple quotes](#generate-multiple-quotes)
*   [Manage layouts: Flex and Box](#manage-layouts-flex-and-box)Beginner
*   [Use CRM data components](#use-crm-data-components)Beginner
*   [View nearby companies: Mapbox API](#view-nearby-companies-mapbox-api)
*   [Bidirectional property refresh](#bidirectional-property-refresh)

Build a multi-step flow[](https://developers.hubspot.com/docs/platform/sample-projects#build-a-multi-step-flow)
---------------------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/multi-step-flow)

Send a meal from a local restaurant to one of your contacts.

Example use case: with one of their agency partners working overtime to close an upgrade deal, an account manager wants a way to order them dinner from the CRM as a thank you. 

What's included: an example card for contact records featuring search, data validation, custom components, and more.

![ui-extension-sample-multi-step-flow-with-panel](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extension-sample-multi-step-flow-with-panel.gif?width=700&height=399&name=ui-extension-sample-multi-step-flow-with-panel.gif)

What you'll learn: 

*   Searching a table, including pagination.
*   Implementing realtime form validation.
*   Fetching data asynchronously with HubSpot serverless functions.
*   Including empty, error, and loading states.
*   Using the [Panel component](/docs/platform/ui-extension-components#panel) to display a form.
*   Getting current contact properties.
*   Getting current user properties.
*   Triggering alerts in the CRM outside of the card 's boundaries.

Create a deals summary[](https://developers.hubspot.com/docs/platform/sample-projects#create-a-deals-summary)
-------------------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/deals-summary)

View a high-level summary of data from associated deals. [Follow through the tutorial](/docs/platform/deals-summary-sample-project-tutorial) to add the project to your account, create two example deal records to display data from, then customize the extension with additional components.

**Example use case:** a salesperson needs a way to quickly view important deal information from their contact records so that they can plan, prioritize, and report on their efforts.

**What's included:** an example card for contact records that aggregates and displays associated CRM record data.

![ui-extensions-deals-summary-sample-extension](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-deals-summary-sample-extension.png?width=600&height=460&name=ui-extensions-deals-summary-sample-extension.png)

What you'll learn: how to surface data from associated CRM records and how to customize extensions with additional components.

Custom logger example[](https://developers.hubspot.com/docs/platform/sample-projects#custom-logger-example)
-----------------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/custom-logger-example)

Explore the various `logger` API methods by sending custom logs from deployed extensions. When used in local development mode, logs will be sent to the browser console. In cases where the extensions fail to load, a trace ID will be generated which you can then use to trace the log within the  [app's logs in HubSpot](/docs/platform/create-private-apps-with-projects#logs). Learn more about the [custom logger API](/docs/platform/ui-extensions-sdk#send-custom-log-messages-for-debugging).

**What's included:**

*   **Middle column card:** an example card for the middle column of contact records, which includes custom logging for serverless function success/failure, logging different types of information, and logging for extension failure.  
    ![custom-logger-example-middle-panel-card](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/custom-logger-example-middle-panel-card.png?width=562&height=582&name=custom-logger-example-middle-panel-card.png)
*   **Sidebar card:** an example card for the right sidebar of contact records, which includes custom logging for serverless function success/failure, logging different types of information, and logging for extension failure.

![sidebar-card-logging-example](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/sidebar-card-logging-example.png?width=314&height=795&name=sidebar-card-logging-example.png)

What you'll learn: how to use the [custom logger API](/docs/platform/ui-extensions-sdk#send-custom-log-messages-for-debugging) to enable more in-depth troubleshooting of UI extensions.

Display an iframe modal[](https://developers.hubspot.com/docs/platform/sample-projects#display-an-iframe-modal)
---------------------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/display-iframe-modal)

Open a popup iframe modal on button click to embed external content on CRM records. Learn more about [opening iframe modals in UI extensions](/docs/platform/create-ui-extensions#open-an-iframe-in-a-modal).

**Example use case:** you want to embed a section of your company's ERP so that sales reps can check inventory levels when putting together potential deals.

**What's included:** an example card for contact records that includes descriptive text and a button that loads Wikipedia in an iframe modal.

![ui-extensions-iframe-modal-example](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-iframe-modal-example.gif?width=700&height=538&name=ui-extensions-iframe-modal-example.gif)

What you'll learn: how to launch a modal that contains an iframe for displaying external content.

Duplicate contact[](https://developers.hubspot.com/docs/platform/sample-projects#duplicate-contact)
---------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/duplicate-contact)

Duplicate a contact along with some of its properties and associated deals and companies.

Example use case: after an in-person consultation, a marketer needs a way to quickly create several contact records for a new group of clients who share similar data. 

What's included: an example card for contact records featuring data display and form submission.

![sample-project-contact-duplication](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/sample-project-contact-duplication.gif?width=700&height=413&name=sample-project-contact-duplication.gif)

What you'll learn: 

*   Fetching data asynchronously using HubSpot serverless functions.
*   Using loading and error states.
*   Making GraphQL calls inside serverless functions.

Generate multiple quotes[](https://developers.hubspot.com/docs/platform/sample-projects#generate-multiple-quotes)
-----------------------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/generate-quotes)

Match a customer with a service based on specified criteria, then generate a sales quote. The extension is built on top of the HubSpot quotes tool and uses the [quotes API](/docs/api/crm/quotes).

Example use case: a fictional shuttle bus rental company with several service options needs a way to match customers with the most appropriate service, then generate a quote for them.

What's included: a _Shuttle bus quotes sample_ card for deal records featuring a multi-part form and quote generator.

![ui-extensions-multiple-quotes-example](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-multiple-quotes-example.png?width=700&height=416&name=ui-extensions-multiple-quotes-example.png)

What you'll learn:

*   Building multi-page forms.
*   Fetching data asynchronously using HubSpot serverless functions.
*   Customized sales quote generation.

Manage layouts: Flex and Box[](https://developers.hubspot.com/docs/platform/sample-projects#manage-layouts-flex-and-box)
------------------------------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/flex-and-box)

Learn how the `Flex` and `Box` components can be used to [manage extension layout](/docs/platform/manage-ui-extension-layout).

Example use case: you want to customize the structure of your card and its various components to better organize information and improve UX.

What's included:

*   **Flex playground card:** a card for deal records where you can experiment with various `Flex` props to better understand how they work together.

![flex-playground-card-demo](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-playground-card-demo.gif?width=600&height=564&name=flex-playground-card-demo.gif)

*   **Flex and box example card:** a real estate listing card for deal records that uses `Flex` and `Box` to arrange information on each listing. This card does not include any real data handling functionality. The example data is hardcoded for component demonstration purposes only. 

![flex-and-box-example-card-demo](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-and-box-example-card-demo.gif?width=600&height=566&name=flex-and-box-example-card-demo.gif)

What you'll learn: 

*   Using the `Flex` and `Box` [layout components](/docs/platform/manage-ui-extension-layout).
*   Improving `Form` component arrangement.
*   Optimizing the space of your cards through a variety of components.
*   Using `Tile` components to group information.
*   Including multiple extensions in one project.

Use CRM data components[](https://developers.hubspot.com/docs/platform/sample-projects#use-crm-data-components)
---------------------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/crm-data-components)

View a contact's associated deal information in a table, then navigate to the deal record to view and modify its progress in the sales pipeline.

Example use case: a salesperson needs a way to quickly view a contact's associated deal information, then navigate to the deal record to confirm the deal's progress and close it.

What's included:

*   **Association Table Card:** a card for contact records to display high-level associated deal information in a table.

![ui-extensions-association-table-sample](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-association-table-sample.png?width=600&height=372&name=ui-extensions-association-table-sample.png)

*   **Stage Tracker Card:** a card for deal records to view and update pipeline stage progress.

![ui-extensions-deal-stage-tracker-sample](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-deal-stage-tracker-sample.png?width=600&height=510&name=ui-extensions-deal-stage-tracker-sample.png)

What you'll learn: 

*   Using [CRM data components](/docs/platform/ui-extension-components#crm-data-components), which are pre-configured to display CRM data.
*   Using the `Flex` [layout component](/docs/platform/manage-ui-extension-layout).
*   Making API calls to the HubSpot API using serverless functions.
*   Fetching properties for the currently displaying record.

View nearby companies: Mapbox API[](https://developers.hubspot.com/docs/platform/sample-projects#view-nearby-companies-mapbox-api)
----------------------------------------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/mapbox-api)

Find and display companies that are located near the currently displaying company record.

Example use case: a salesperson will be traveling to visit client and wants to know if there are other companies they can visit along the way.

What's included:

*   **Top value companies within radius:** a card for company records to show the companies nearest to the currently displaying record.  
      
    ![ui-extensions-search-by-radius](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-search-by-radius.png?width=700&height=278&name=ui-extensions-search-by-radius.png)
*   **Nearest companies to currency company record:** a card for company records to search for nearby companies by mile radius.  
    ![ui-extensions-promixity-current-company](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-promixity-current-company.png?width=600&height=315&name=ui-extensions-promixity-current-company.png)

What you'll learn:

*   Including multiple UI extensions in one project using one private app.
*   Working with third-party data.

Bidirectional Property Refresh[](https://developers.hubspot.com/docs/platform/sample-projects#bidirectional-property-refresh)
-----------------------------------------------------------------------------------------------------------------------------

[View the source code in GitHub](https://github.com/HubSpot/ui-extensions-examples/tree/main/bi-directional-property-refresh)

Provides bidirectional refresh of contact property changes between a custom card and the CRM record page.

Example use case: a salesperson in your account makes frequent changes to a contact's properties and associated fields on a custom card and requires a seamless editing experience to avoid manual page refreshes.

**What's included:** a _Refresh properties between custom card and CRM page_ card that displays the latest `firstname` and `lastname` property values when changed on the CRM record page, as well as a lifecycle stage dropdown menu that you can update on the card and immediately see the change reflected on the CRM record page.

![bi-directional-crm-record-card-sync](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/bi-directional-crm-record-card-sync.gif?width=700&height=467&name=bi-directional-crm-record-card-sync.gif)

What you'll learn:

*   How you can use the `fetchCrmObjectProperties` and `onCrmPropertiesUpdate` actions to listen to changes on the CRM record page and fetch the latest values.
*   How you can ensure data in the custom card stays up to date with the `refreshObjectProperties` action.

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/sample-projects#page-feedback)
-------------------------------------------------------------------------------------------------

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
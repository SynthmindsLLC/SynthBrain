---
title: "Migrate an existing Accounting Extension API integration"
description: "Guide on migrating the Accounting Extension API integration before sunsetting of API keys, including contact and product sync migration using HubSpot's APIs."
type: "work"
tags:
- "API"
- "Migration"
- "Hubspot"
- "Accounting_Extension"
relationships:
- "#related_to [[API Key Sunset]]"
- "#requires [[Contacts API]]"
- "#requires [[Products API]]"
- "#uses [[CRM Cards API]]"
- "#implements [[Data Fetch Request]]"
- "#implements [[Action Hook Action]]"
- "#related_to [[Webhooks]]"
- "#enables [[Invoice Data Display on CRM Card]]"
- "#requires [[IFRAME action for View invoice PDF]]"
published_date: "2022-11-30"
---

Migrate an existing Accounting Extension API integration
========================================================

[API keys will be sunsetted](https://developers.hubspot.com/changelog/upcoming-api-key-sunset) on November 30th, 2022. If your Accounting Extension integration uses API keys, you will need to update it to a [private app](/docs/api/migrate-an-api-key-integration-to-a-private-app), then implement the following API changes below. 

Migrate contact and product sync[](https://developers.hubspot.com/docs/api/migrate-an-existing-account-extension-integration#migrate-contact-and-product-sync)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Learn about the different APIs you can use for the contact and product sync. The respective API documentation includes details on relevant scope requirements.

*   For contact sync, you can instead use the [Contacts API](https://developers.hubspot.com/docs/api/crm/contacts). Specifically, you can make a `POST` request to the `/crm/v3/objects/contacts`. 
*   For product sync, you can instead use the [Products API](https://developers.hubspot.com/docs/api/crm/products). Specifically, you can make a `POST` request to `/crm/v3/objects/products`.

The above APIs do not automatically retry if they return errors. If your integration experiences errors interacting with the above APIs, your system will need to retry API calls.

**Please note:** when using the Products API, deduplication will not happen automatically. When you create products using this API, you should record the ID so you know when to update existing products instead of creating new ones. 

Migrate the deal record invoice card[](https://developers.hubspot.com/docs/api/migrate-an-existing-account-extension-integration#migrate-the-deal-record-invoice-card)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

To display invoice data on a deal record, use the [CRM Cards API](/docs/api/crm/extensions/custom-cards) to create an invoice card.

### Display invoice data on a CRM card[](https://developers.hubspot.com/docs/api/migrate-an-existing-account-extension-integration#display-invoice-data-on-a-crm-card)

To display invoice data on a CRM card:

*   Implement a **data fetch request** detailed in the _Webhooks_ section of the documentation.
*   Use an **action hook action** for HubSpot to retrieve invoice data from your system depending on which deal record a customer is viewing.
*   With the CRM Cards API endpoints, you can customize which invoice data is displayed on each card, as well as actions customers can perform.
*   Your system will need to keep a record of what invoices to display depending on `associatedObjectId`, which is the `ObjectId` of the current deal a customer is viewing. 

### Other CRM card actions[](https://developers.hubspot.com/docs/api/migrate-an-existing-account-extension-integration#other-crm-card-actions)

You can also implement actions, which allow customers to perform operations on the data displayed on the CRM card:

*   For example, you can choose where a customer can modify or delete a specific invoice in the CRM card by returning an `action` array from your implemented action hook API.
*   If you want customers to be able to create net new invoices via your CRM card, you can achieve this by configuring and returning a `primaryAction` attribute in the response from your built action hook API.
*   You can also implement a "View invoice PDF" action using an `IFRAME` action type as the `secondaryAction`. 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/migrate-an-existing-account-extension-integration#page-feedback)
------------------------------------------------------------------------------------------------------------------------------

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
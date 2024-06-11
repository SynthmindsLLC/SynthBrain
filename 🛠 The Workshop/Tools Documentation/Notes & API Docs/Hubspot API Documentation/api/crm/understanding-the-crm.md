---
title: "Understanding the CRM"
description: "The foundation of your HubSpot account is a database of your business relationships and processes, called the Customer Relationship Management (CRM) system. To manage this data, HubSpot accounts include objects, which represent types of relationships or processes. All HubSpot accounts include four standard objects: contacts, companies, deals, and tickets. Depending on your subscription, there are additional objects such as products and custom objects."
type: "concept"
tags:
- "CRM"
- "HubSpot"
relationships:
- "#part_of [[Customer Relationship Management]]"
---

Understanding the CRM
=====================

The foundation of your HubSpot account is a database of your business relationships and processes, called the CRM (Customer Relationship Management). To manage this data, HubSpot accounts include objects, which represent types of relationships or processes. All HubSpot accounts include four standard objects: contacts, companies, deals, and tickets. Depending on your [HubSpot subscription](https://legal.hubspot.com/hubspot-product-and-services-catalog), there are additional objects, such as products and custom objects.  

Records are individual instances of an object (e.g., John Smith is a contact). For each record, you can store information in properties, track interactions, and create reports. You can also make associations between records to understand the relationships between them. Below, learn about CRM objects, records, properties, and additional functionalities.

To learn more about managing your CRM database from within HubSpot, check out [HubSpot's Knowledge Base](https://knowledge.hubspot.com/get-started/manage-your-crm-database).

Objects
-------

The CRM API provides access to objects, records, and activities. The list below explains the objects available in HubSpot.

The following objects each have an [index page](https://knowledge.hubspot.com/crm-setup/create-customize-and-manage-your-saved-views) within HubSpot, and can all be associated with each other:

*   [Contacts](https://knowledge.hubspot.com/contacts/a-guide-to-using-records?_ga=2.248927623.1430331704.1585575540-500942594.1573763828): store information about an individual person. [View contacts endpoints](/docs-beta/crm/contacts) 
*   [Companies](https://knowledge.hubspot.com/contacts/a-guide-to-using-records?_ga=2.248927623.1430331704.1585575540-500942594.1573763828): store information about an individual business or organization. [View companies endpoints](/docs-beta/crm/companies) 
*   [Deals](https://knowledge.hubspot.com/contacts/a-guide-to-using-records?_ga=2.248927623.1430331704.1585575540-500942594.1573763828): represent revenue opportunities with a contact or company. They’re tracked through pipeline stages, resulting in the deal being won or lost. [View deals endpoints](/docs-beta/crm/deals)
*   [Tickets](https://knowledge.hubspot.com/contacts/a-guide-to-using-records?_ga=2.248927623.1430331704.1585575540-500942594.1573763828): represent customer requests for help or support. They're tracked through pipeline statuses, resulting in the ticket being closed. [View tickets endpoints](/docs-beta/crm/tickets) 
*   [Calls](https://knowledge.hubspot.com/calling/use-the-calling-tool): store information about calls with contacts, but can also be associated with other objects as an engagement. [View calls endpoints.](/docs/api/crm/calls)
*   [**Quotes**](https://knowledge.hubspot.com/quotes/use-quotes): represent pricing information shared with potential buyers. Quotes can be associated with contacts, companies, deals, and line items. View [quotes endpoints](/docs/api/crm/quotes).
*   [Custom Objects](https://knowledge.hubspot.com/crm-setup/use-custom-objects?_ga=2.256946827.1637125445.1604003319-315276892.1604003319) (Enterprise only): create a custom object to store any type of data in HubSpot—particularly data that doesn't fit the standard objects listed above. [View custom object endpoints](/docs/api/crm/crm-custom-objects)

The following objects do not have index pages within HubSpot, but can be associated with certain other objects: 

*   [Activities/Engagements](https://knowledge.hubspot.com/contacts/manually-log-a-call-email-or-meeting-on-a-record) (Calls, Emails, Meetings, Notes, Tasks, SMS, LinkedIn, WhatsApp, Postal Mail): represent interactions associated with your records. You can associate activities with contacts, companies, deals, tickets, and custom objects. View [engagements endpoints.](/docs/api/crm/engagements)
*   [Products](https://knowledge.hubspot.com/deals/how-do-i-use-products?_ga=2.248927623.1430331704.1585575540-500942594.1573763828): represent goods or services for sale. Products can't be associated with other CRM objects, but you can create line items based on products and associate those with deals and quotes. [View products endpoints](/docs-beta/crm/products)
*   [Line items](https://knowledge.hubspot.com/products/how-do-i-use-products): represent individual products and services sold in a deal. Line items can be created from existing products in your product library, or can be created as standalone line items. Standalone line items will not be added to the product library. [View line items endpoints](/docs-beta/crm/line-items)
*   [**Feedback submissions**](https://knowledge.hubspot.com/customer-feedback/feedback-submission-properties): stores information submitted to a feedback survey. Feedback submissions are associated with contact records. View [feedback submission endpoints](/docs/api/crm/feedback-submissions)
*   [Marketing events](https://knowledge.hubspot.com/integrations/use-marketing-events): represent events related to your marketing efforts, specifically including events from connected integrations. You can specify whether or not a contact attended, registered for, or cancelled attending a marketing event. View [marketing events endpoints](/docs/api/marketing/marketing-events)
*   [Invoices](/docs/api/commerce/invoices): represent the invoices that you send for sales made. Invoices can be associated with **[contacts](https://developers.hubspot.com/docs/api/crm/contacts)**, **[companies](https://developers.hubspot.com/docs/api/crm/companies)**, **[deals](https://developers.hubspot.com/docs/api/crm/deals)**, **[line items](https://developers.hubspot.com/docs/api/crm/line-items)**, **[discounts](https://developers.hubspot.com/docs/api/crm/discounts)**, **[fees](https://developers.hubspot.com/docs/api/crm/fees)**, and **[taxes](https://developers.hubspot.com/docs/api/crm/taxes)**. 
*   [Payments](/docs/api/commerce/payments): the payments made by buyers through invoices, payment links, and quotes. Payments can be associated with  **[contacts](https://developers.hubspot.com/docs/api/crm/contacts)**, **[companies](https://developers.hubspot.com/docs/api/crm/companies)**, **[deals](https://developers.hubspot.com/docs/api/crm/deals)**, [invoices](https://developers.hubspot.com/docs/api/commerce/invoices), [quotes](https://developers.hubspot.com/docs/api/crm/quotes), **[line items](https://developers.hubspot.com/docs/api/crm/line-items)**, [subscriptions](https://developers.hubspot.com/docs/api/commerce/subscriptions), **[discounts](https://developers.hubspot.com/docs/api/crm/discounts)**, **[fees](https://developers.hubspot.com/docs/api/crm/fees)**, and **[taxes](https://developers.hubspot.com/docs/api/crm/taxes).**
*   [Subscriptions](/docs/api/commerce/subscriptions): recurring payments scheduled through payment links and quotes. Invoices can be associated with **[contacts](https://developers.hubspot.com/docs/api/crm/contacts)**, **[companies](https://developers.hubspot.com/docs/api/crm/companies)**, **[deals](https://developers.hubspot.com/docs/api/crm/deals)**, [quotes](https://developers.hubspot.com/docs/api/crm/quotes), **[line items](https://developers.hubspot.com/docs/api/crm/line-items)**, [payments](https://developers.hubspot.com/docs/api/commerce/payments), **[discounts](https://developers.hubspot.com/docs/api/crm/discounts)**, **[fees](https://developers.hubspot.com/docs/api/crm/fees)**, and **[taxes](https://developers.hubspot.com/docs/api/crm/taxes)**.
*   [Users](/docs/api/crm/users): represent the users in your HubSpot account. Users cannot be associated with other CRM objects, but can be retrieved and updated through the users API. You can also add users to an account with the [user provisioning API](/docs/api/settings/user-provisioning).

### Object relationships

Within HubSpot, to show how objects are related to one another, you can associate records. For example, you can associate multiple contacts with a company, and then associate the company and relevant contacts with a deal. All HubSpot accounts have contacts, companies, deals, tickets, and activities, which can be associated with one another, shown in the model below. If you have access to a HubSpot account, you can review your account's unique object relationships by navigating to [the data model tool.](https://knowledge.hubspot.com/crm-setup/view-a-model-of-your-crm-object-and-activity-relationships)![data-model-overview-updated](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/data-model-overview-updated.gif?width=800&height=286&name=data-model-overview-updated.gif)

Depending on your subscription, you can describe the specific relationship between records using [association labels](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels), and your account may have additional custom objects, which can be associated with the other standard objects. Other objects, such as products and line items, can only be associated with certain objects. Learn more about these [additional objects and their associations](#other-objects).

**L**earn more about object relationships and managing associations using the [associations endpoints](/docs-beta/crm/associations).

### Activities and attachments

[Engagements](/docs/api/crm/engagements), also called activities, store data from interactions with records. For example, if you call a prospect, you can log a call to the contact record, and also associate the call with their associated company. Possible activities include notes, tasks, meetings, emails, calls, postal mail, SMS, LinkedIn messages, and WhatsApp messaged.

You can also store attachments on records to keep track of relevant files. These are often related to engagements.

Learn more about the [engagements APIs.](/docs/api/crm/engagements)[](/docs/api/crm/engagements)

### Data syncing

Syncing engagement data is not required to sync object data. Because an object can be associated with numerous engagements, it’s also important to keep [API limits](/docs/api/usage-details) in mind before syncing.

However, you may want to sync engagements rather than properties when an integration is a precursor to a full migration. In this case, syncing engagements across both systems will ensure all users have the data they need during the transition. For example, when a business development team working in HubSpot is handing deals to an inside sales rep working in another CRM, you should sync engagements so both teams have the context they need to close a sale.

### Object type IDs

When using certain APIs, you'll need to use the `objectTypeId` field. Below are the ID values for each object or activity:

*   **Contacts**: `0-1`
*   **Companies**:  `0-2`
*   **Deals**: `0-3`
*   **Tickets:** `0-5`
*   **Custom objects**: to find the ID value for your custom object, make a `GET` request to `/crm/v3/schemas`. The value will look similar to `2-3453932`. 
*   **Calls**: `0-48`
*   **Emails**: `0-49`
*   **Meetings**: `0-47`
*   **Notes**: `0-4`
*   **Tasks**: `0-27`
*   **Products**: `0-7`
*   **Invoices:** `0-52`
*   **Line items**: `0-8`
*   **Payments:** `0-101`
*   **Quotes:** `0-14`
*   **Subscriptions:** `0-69`
*   **Communications** (SMS, LinkedIn, WhatsApp messages): `0-18`
*   **Postal mail**: `0-116`
*   **Marketing events**: `0-54`
*   **Feedback submissions**: `0-19`

While you can always use the numerical ID value, in some cases, you can also use the object's name for contacts, companies, deals, tickets, or notes. For example:

*   When starting an import with the [imports API](/docs/api/crm/imports), the `**columnObjectTypeId**` specifies which object the data in your file belongs to. To import data for contacts, your value for `**columnObjectTypeId**` could be `contact` or `0-1`.
*   When using the [associations API](/docs/api/crm/associations), the `fromObjectType` and `toObjectType` values specify the objects and the direction of the association. To view association types for contacts to companies, your `GET` request URL could be `crm/v4/associations/contact/company/labels` or `crm/v4/associations/0-1/0-2/labels`.

Batch actions
-------------

Each object provides batch endpoints that let you create, read, update, and archive multiple object records in a single request. Batch endpoints have a limit of 100 records per call.

Properties
----------

Information about records are stored in fields called properties, which are then organized into [groups](https://knowledge.hubspot.com/contacts/manage-your-properties?_ga=2.149271734.1430331704.1585575540-500942594.1573763828#create-and-edit-property-groups). In addition to each object’s default properties, you can store custom data by [creating custom properties](https://knowledge.hubspot.com/contacts/manage-your-properties?_ga=2.248927623.1430331704.1585575540-500942594.1573763828#create-custom-properties). 

### Default properties

CRM objects are defined by a primary _type_ and a set of _properties_. Each type has a unique set of standard properties, represented by a map of name-value pairs. Learn more about default properties for different objects:

*   [Contacts](https://knowledge.hubspot.com/contacts/hubspots-default-contact-properties?_ga=2.149271734.1430331704.1585575540-500942594.1573763828)
*   [Companies](https://knowledge.hubspot.com/companies/hubspot-crm-default-company-properties?_ga=2.149271734.1430331704.1585575540-500942594.1573763828)
*   [Deals](https://knowledge.hubspot.com/deals/hubspots-default-deal-properties?_ga=2.149271734.1430331704.1585575540-500942594.1573763828)
*   [Tickets](https://knowledge.hubspot.com/tickets/hubspots-default-ticket-properties?_ga=2.149271734.1430331704.1585575540-500942594.1573763828)
*   [Feedback submissions](https://knowledge.hubspot.com/customer-feedback/feedback-submission-properties)
*   [Invoices](https://knowledge.hubspot.com/invoices/hubspots-default-invoice-properties)
*   [Payments](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties)
*   [Subscriptions](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties)

### Custom properties

Create [custom properties](https://knowledge.hubspot.com/contacts/manage-your-properties?_ga=2.149271734.1430331704.1585575540-500942594.1573763828#create-custom-properties) to store specialized information for an object. Custom properties can be managed through the CRM object properties endpoints.

### Record owners

You can assign HubSpot users as [owners](https://knowledge.hubspot.com/contacts/how-to-set-an-owner?_ga=2.149271734.1430331704.1585575540-500942594.1573763828) of records. Any HubSpot user with access to an object can be assigned as an owner, and multiple owners can be assigned to an object by creating a [custom property](https://knowledge.hubspot.com/articles/kcs_article/contacts/how-can-i-create-a-custom-owner-property?_ga=2.149271734.1430331704.1585575540-500942594.1573763828) for this purpose. Owners can only be created in HubSpot, but you can use the [owners endpoint](/docs-beta/crm/owners) to get their identifying details, including IDs and email addresses. This data can then be assigned to CRM records in HubSpot or via property change API calls. 

Unique identifiers and record IDs
---------------------------------

A unique identifier is a value that differentiates one record in a database from another, even if they have otherwise identical information. For example, a database for a bank might have records for two people named John Smith.  To avoid accidentally sending money to the wrong John Smith, each record is given a number as their unique ID.

You'll use these unique identifiers to send your data to the correct records, and manage deduplication. Learn more about the ways that HubSpot handles deduplication in the [Knowledge Base](https://knowledge.hubspot.com/contacts/deduplication-of-contacts-companies-deals-tickets).

### HubSpot’s default unique identifiers

When a record is created in HubSpot, a unique ID is automatically generated and should be treated as a string. These IDs are unique only within the object type, so there can be both a contact and company with the same ID. 

For contacts and companies, there are additional unique identifiers, including a contact's `email` and a company's `domain` name.

### Creating your own unique identifiers

In many cases, you can use the record ID (`hs_object_id`) generated by HubSpot to drive the logic of your integration. However, your data may require other properties with unique values, or there may be times when record ID either cannot be used or complicates the integration logic of your app. In these cases, you can [create a custom unique identifier property via the Properties API.](/docs/api/crm/properties#create-unique-identifier-properties)

Once you've created a custom unique ID property, you can use it in API calls to to identify and update specific records in the same way you can use `hs_object_id`, `email` for contacts, or `domain` for companies. For example, to retrieve a deal based on its value for a custom unique ID property, your request URL could look like: `GET` [https://api.hubapi.com/crm/v3/objects/deals/abc?idProperty=system\_a\_unique](https://api.hubapi.com/crm/v3/objects/deals/unique_string?idProperty=system_a_unique). 

FAQs
----

For more information about objects in HubSpot, learn how to [manage your CRM database.](https://knowledge.hubspot.com/get-started/manage-your-crm-database)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#page-feedback)
------------------------------------------------------------------------------------------------------

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
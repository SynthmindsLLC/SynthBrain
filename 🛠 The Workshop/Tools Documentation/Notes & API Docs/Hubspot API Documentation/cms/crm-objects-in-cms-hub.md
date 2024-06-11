---
title: "CRM Object Data in CMS Hub"
description: "Use CRM object data on your website, allowing sales, marketing, and website data to live in the same place and reflect the same information. Associate CRM records with one another to pull in associated data onto your website pages. Learn more about building data-based CMS pages in HubSpot Academy's [CMS Data-Driven Content course](https://app.hubspot.com/academy/tracks/1148948/intro)."
type: "group"
tags:
- "CRM"
- "HubSpot CMS"
- "Data Integration"
relationships:
- "#part_of [[CMS Hub]]"
- "#enables [[Dynamic Pages]]"
founded: "2014-03-05"
---

Use CRM object data in CMS Hub


==================================

Last updated: December 20, 2023

You can query CRM objects to use data from the object's records on HubSpot hosted content, allowing data to be shared between your business operations, website, and emails. Using the [`crm_object`](https://developers.hubspot.com/docs/cms/hubl/functions#crm-object), [`crm_objects`](https://developers.hubspot.com/docs/cms/hubl/functions#crm-objects) and [`crm_associations`](https://developers.hubspot.com/docs/cms/hubl/functions#crm-associations) HubL functions, you can display and control logic based on your CRM object data. 

Using CRM data on your website means that your sales, marketing, and website data all live in the same place and will always reflect the same information. In addition, because you can associate CRM records with one another, you can also pull in associated data onto your website pages.

Similarly, you can [create sets of dynamic pages that automatically generate using CRM object or HubDB data](/docs/cms/data/dynamic-pages).

You can learn more about building data-based CMS pages in HubSpot Academy's [CMS Data-Driven Content course](https://app.hubspot.com/academy/tracks/1148948/intro).

### Example use case[](https://developers.hubspot.com/docs/cms/data/crm-objects#example-use-case)

One example of using CRM object data in pages is a real estate listing page. With a custom object called _property_, individual object records can be created for each house that needs to be listed. Real estate agents can then add information to object properties to store details, such as location, number of bedrooms, and asking prices. 

Website pages can then pull in that record data for each property to create a listing page and details pages for each property. 

[Check out the GitHub repo](https://github.com/HubSpot/cms-custom-objects-example) to view the full example.

For an overview of this example, check out the [recording of HubSpot Developer Day 2020](/developer-day-2020). 

Supported CRM object types[](https://developers.hubspot.com/docs/cms/data/crm-objects#supported-crm-object-types)
-----------------------------------------------------------------------------------------------------------------

Below are the types of CRM objects that you can pull data from for your CMS Hub pages. Whether you can use the data across all pages or only on private pages depends on the object type.

In the tables below, learn about which object types are available for CMS content along with their object type names and fully qualified names. 

**Please note:** standard object names, such as "contact," are not case sensitive, but must be singular.

### CRM object data available for all pages

Data from the following CRM objects can be used on any CMS page.  
  

| **Object type** | **object\_type name** | **Fully qualified name** |
| --- | --- | --- |
| [Products](/docs/api/crm/products) | `product` | `PRODUCT` |
| [Marketing events](/docs/api/marketing/marketing-events) | `marketing_event` | `MARKETING_EVENT` |
| [Custom objects](/docs/api/crm/crm-custom-objects) | 
_CMS Hub Enterprise_ only.

You can either use the object's [fully qualified name](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details), or the name that was entered at the time of creation. For example, if you create an object named "Cars," you cannot reference it with "cars" or Car."

You must use the [fully qualified name](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details) if the custom object shares a name with a standard object.

 | 

 | 

### CRM object data available for private pages

Data from the following CRM objects can be used only on pages that require either a [password](https://knowledge.hubspot.com/website-pages/password-protect-a-page) or a [membership login.](https://knowledge.hubspot.com/website-pages/require-member-registration-to-access-private-content)  
  

| **Object type** | **object\_type name** |  **FULLY QUALIFIED NAME** |
| --- | --- | --- |
| [Contacts](/docs/api/crm/contacts) | `contact` | `CONTACT` |
| [Companies](/docs/api/crm/companies) | `company` | `COMPANY` |
| [Deals](/docs/api/crm/deals) | `deal` | `DEAL` |
| [Tickets](/docs/api/crm/tickets) | `ticket` | `TICKET` |
| [Quotes](/docs/api/crm/quotes) | `quote` | `QUOTE` |
| Integrator objects | 
To get an integrator object's name, use the [CRM objects schema API](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details).

For integrator objects with the same name as the standard objects, use the integrator object's [fully qualified name](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details).

 | 

 | 

Display data from a single CRM record with the crm\_object function[](https://developers.hubspot.com/docs/cms/data/crm-objects#display-data-from-a-single-crm-record-with-the-crm-object-function)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the [`crm_object`](/docs/cms/hubl/functions#crm-object) function to get a single record from the HubSpot CRM by query or by CRM record ID. 

Object records are returned as a dict of properties and values.

{# Render custom object by query #} {% set event = crm\_object("event", "name=Defensive Health") %} {{ event.name }} {# Render custom objects specifying the id of the object #} {% set event = crm\_object("event", 289236) %} {{ event.name }}<p>Defensive Heatlh</p> <p>Defensive Heatlh</p>

If a query returns a collection of records, the function will return the first record in the collection.

Display data from multiple CRM records with the crm\_objects function[](https://developers.hubspot.com/docs/cms/data/crm-objects#display-data-from-multiple-crm-records-with-the-crm-objects-function)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the [`crm_objects()`](/docs/cms/hubl/functions#crm-objects) function to get CRM records by object type from the HubSpot CRM by query or by record ID. Records are returned as a dict of properties and values.

The record returned contains a `results` property that can be looped through to display the information in the record's items.

{# Render custom objects by query #} {% set events = crm\_objects("event", "limit=3&type=virtual") %} <h3>{{events.total}} New Events:<h3> <ul> {% for event in events.results %} <li>Name: {{ event.name }}</li> {% endfor %} <ul> {# Render custom objects by ids #} {% set events = crm\_objects("event", \[289236,289237,289238\]) %} <h3>{{events.total}} New Events:<h3> <ul> {% for event in events.results %} <li>Name: {{ event.name }}</li> {% endfor %} <ul> <h3>3 New Events:<h3> <ul> <li>Name: Defensive Health</li> <li>Name: Body Balance</li> <li>Name: Happy Heart</li> <ul> <h3>3 New Events:<h3> <ul> <li>Name: Defensive Health</li> <li>Name: Body Balance</li> <li>Name: Happy Heart</li> <ul>

Display associated records[](https://developers.hubspot.com/docs/cms/data/crm-objects#display-associated-records)
-----------------------------------------------------------------------------------------------------------------

Use the [`crm_associations`](/docs/cms/hubl/functions#crm-associations) HubL function to get a list of associated records from the HubSpot CRM based on the given record ID, association category, and association definition ID.[](#getting-a-custom-object-s-details)

Records are returned as a dict of properties and values.

{% set associated\_objects = crm\_associations(289236, "USER\_DEFINED", 3) %} <h3>Contacts Associated With Event</h3> <ul> {% for contact in associated\_objects.results %} <li>Name: {{ contact.firstname }} {{ contact.lastname }}</li> {% endfor %} </ul> <h3>Contacts Associated With Event<h3> <ul> <li>Name: Brian Halligan</li> <li>Name: Dharmesh Shah</li> <li>Name: Yamini Rangan</li>

Getting a custom object type's details[](https://developers.hubspot.com/docs/cms/data/crm-objects#getting-a-custom-object-type-s-details)
-----------------------------------------------------------------------------------------------------------------------------------------

To get a custom object type's `name`, `id`, `fullyQualifiedName`, association IDs, and other details, you can make a `GET` request to the [CRM Objects schema API](https://developers.hubspot.com/crm-custom-objects).

**Please note:** `fullyQualifiedName` for account-specific object types includes the HubSpot account ID, so it's recommended to avoid using it when developing your code for multiple HubSpot accounts.

CRM Object Module field[](https://developers.hubspot.com/docs/cms/data/crm-objects#crm-object-module-field)
-----------------------------------------------------------------------------------------------------------

To provide a way for content creators to select CRM records to display or execute logic, you can build modules that include the [CRM object field](/en/docs/cms/building-blocks/module-theme-fields#crm-object).

For example, you may want to display information from a specific product, contact, company, deal, quote, ticket, or custom object.

![CRM Object Field](https://developers.hubspot.com/hubfs/CRM%20Object%20Field.png "CRM Object Field")

CRM Object tutorials and resources[](https://developers.hubspot.com/docs/cms/data/crm-objects#crm-object-tutorials-and-resources)
---------------------------------------------------------------------------------------------------------------------------------

*   [Essentials of getting started with Custom Objects](/blog/essentials-for-getting-started-with-custom-objects)
*   [Think like an architect: Build scalable Custom Objects](/blog/how-to-think-like-an-architect-by-building-scalable-custom-objects)
*   [Build Dynamic Pages with CRM Objects](/docs/cms/guides/dynamic-pages/crm-objects)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/data/crm-objects#page-feedback)
---------------------------------------------------------------------------------------------

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
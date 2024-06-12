---
title: "Dynamic Pages Overview"
description: "An explanation on how dynamic pages function in HubSpot in relation to HubDB and CRM objects."
type: "concept"
tags:
- "Marketing"
- "Website"
- "Content Management"
relationships:
- "#related_to [[HubDB]]"
- "#related_to [[CRM Objects]]"
- "#related_to [[Query String Parameters]]"
- "#discusses [[Dynamic Pages]]"
- "#discusses [[CMS Data-Driven Content]]"
- "#discusses [[Custom Objects]]"
- "#discusses [[Private Pages]]"
- "#discusses [[Automation]]"
- "#discusses [[API]]"
- "#discusses [[Content Management]]"
- "#discusses [[Search Engine Optimization]]"
- "#discusses [[Referral URLs]]"
- "#discusses [[HubL]]"
- "#discusses [[HubDB Technical Limits]]"
- "#discusses [[Queries]]"
- "#discusses [[Data Sources]]"
- "#discusses [[User Experience]]"
- "#discusses [[Web Analytics]]"
- "#discusses [[Data Management]]"
- "#discusses [[Content Creation]]"
- "#discusses [[CRM Database Management]]"
- "#discusses [[Website Pages]]"
- "#discusses [[Marketing Events]]"
- "#discusses [[Products]]"
- "#discusses [[Contacts]]"
- "#discusses [[Companies]]"
- "#discusses [[Deals]]"
- "#discusses [[Quotes]]"
- "#discusses [[Tickets]]"
- "#discusses [[Tables]]"
- "#discusses [[Rows]]"
- "#discusses [[Columns]]"
- "#discusses [[Meta Description]]"
- "#discusses [[Featured Image]]"
- "#discusses [[Canonical URL]]"
- "#discusses [[HubDB API]]"
- "#discusses [[Sitemaps]]"
- "#discusses [[Website Search]]"
- "#discusses [[Duplicate Content]]"
- "#discusses [[HubDB Table Rows]]"
- "#discusses [[HubDB Table Row]]"
- "#discusses [[Object Identifiers]]"
- "#discusses [[URL Parameters]]"
- "#discusses [[HubDB Records]]"
- "#discusses [[Logo]]"
- "#discusses [[Query String Parsing]]"
- "#discusses [[Image Rendering]]"
- "#discusses [[Feedback]]"
- "#discusses [[Documentation]]"
---

Dynamic pages overview


==========================

Last updated: December 20, 2023

Dynamic pages are CMS pages that get their content from a structured data source, such as HubDB or CRM objects. Based on how you configure your dynamic page template or modules, HubSpot will use that data to automatically create and populate a set of pages. This includes a listing page that displays summaries of the data, and individual pages for each data source entry (HubDB row or CRM object record).

Depending on the data source you choose, there are different prerequisites, advantages, and content creation experiences. Below, read about each data source and how to choose which one is best for you.

You can learn more about building data-based CMS pages in HubSpot Academy's [CMS Data-Driven Content course](https://app.hubspot.com/academy/tracks/1148948/intro).

CRM object dynamic pages[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#crm-object-dynamic-pages)
---------------------------------------------------------------------------------------------------------------

In HubSpot, CRM objects represent the different types of records and relationships your business has. Standard CRM objects include contacts, companies, deals, and tickets. With an _Enterprise_ subscription, you can also [create custom objects](https://developers.hubspot.com/docs/api/crm/crm-custom-objects). Using any of these CRM objects, you can create a listing page and individual details pages for each record of the object type you choose.

For example, a car dealership could store their inventory as records with a custom _Car_ object. Then, using CRM object dynamic pages, they could list their inventory online with a unique page automatically created for each car. When a new record is created under the _Car_ object, a new page will be created automatically, keeping the inventory and website in sync.

You may want to use CRM objects as your data source if:

*   You want to associate records to other CRM objects, such as contacts.
*   You want to create automation or personalization based on the object.
*   It simplifies your businesses processes and record keeping.

### Requirements[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#requirements)

To build CRM object dynamic pages, you’ll need:

*   _**CMS Hub Professional**_ or _**Enterprise**_.
*   To build using Custom Objects you'll need either **_CMS_ _Hub_ _Enterprise_**, or **_Marketing Hub_ _Enterprise_** with **_CMS Hub_ _Professional_**.
*   An understanding of how to [create custom modules](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules). 
*   A standard or custom object as a data source.

### Content creation[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#content-creation)

After you create your dynamic content modules, they can be inserted into any page that includes a [drag and drop area](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area). To edit how the data is displayed, you'll need to update the modules or template you've created. If the template includes any other drag and drop areas, you can edit the page's non-dynamic content within the page editor. Any updates made to the dynamic or non-dynamic content will apply to both the listing page and the details pages, similar to editing a template.

Because the dynamic page content is coming from [CRM object records](https://knowledge.hubspot.com/crm-setup/use-custom-objects), you manage dynamic page content the same way you would manage other CRM records. For example, you can edit dynamic page content by [editing](https://knowledge.hubspot.com/crm/update-a-property-value-for-a-record) or [deleting](https://knowledge.hubspot.com/contacts/delete-crm-records) individual records in HubSpot. Similarly, you can manage content in bulk by [importing](https://knowledge.hubspot.com/crm-setup/import-objects) or [bulk editing records](https://knowledge.hubspot.com/crm-setup/how-can-i-bulk-edit-contacts-companies-deals-or-tasks).

The type of pages you can create depends on the object you choose:

*   Public pages can be built using the following objects:
    *    Products
    *   Marketing events
    *   Custom objects

*   Private pages ([password protected](https://knowledge.hubspot.com/website-pages/password-protect-a-page) or [member registration](https://knowledge.hubspot.com/website-pages/require-member-registration-to-access-private-content)) can be built using the following objects:
    *    Contacts
    *    Companies
    *    Deals
    *    Quotes
    *   Tickets

It’s important to be aware of automation that’s set up for the CRM object you choose. For example, if you have a workflow that automatically updates a custom object record’s name based on associated deal stage, your dynamic page content will also be updated any time the record’s name changes.

### Start building[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#start-building)

To start building CRM object dynamic pages, check out the [developer guide for building CRM object dynamic pages](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/crm-objects).

If you plan to use custom objects as your data source, learn how to [create and manage custom objects through HubSpot’s API](https://developers.hubspot.com/docs/api/crm/crm-custom-objects).

### More resources[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#more-resources)

*   [How to build dynamic pages using CRM objects](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/crm-objects) 
*   [CRM objects in CMS](https://developers.hubspot.com/docs/cms/features/custom-objects)
*   [Manage your CRM database](https://knowledge.hubspot.com/get-started/manage-your-crm-database)

HubDB dynamic pages[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#hubdb-dynamic-pages)
-----------------------------------------------------------------------------------------------------

Using [HubDB](https://developers.hubspot.com/docs/cms/features/hubdb), you can generate dynamic pages from the rows of a HubDB table. You can also use child tables to create nested pages that map to separate blogs or listing pages of your website. When you enable a HubDB table as a data source, you can select which columns to use for the meta description, featured image, and canonical URL.

You may want to use HubDB as the data source for your dynamic pages if:

*   You don’t need to associate data from your tables with your CRM data.
*   The [HubDB technical limits](https://developers.hubspot.com/docs/cms/features/hubdb#hubdb-technical-limits) are not an issue for your use-case.

### Prerequisites[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#prerequisites)

To build HubDB dynamic pages, you’ll need:

*   CMS Hub Professional, or Enterprise.
*   An existing HubDB table, or learn how to get started and [create your first HubDB table](https://developers.hubspot.com/docs/cms/features/hubdb#creating-your-first-table).
*   An understanding of how to [create custom modules](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules).

### Content creation[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#content-creation)

After you create and enable your HubDB table for dynamic page content, you manage the content of your pages by creating, editing, and deleting HubDB rows. You can edit HubDB tables directly in your HubSpot account, or you can edit your schema externally then upload the data via a CSV or through the [HubDB API](/docs/api/cms/hubdb).

To edit how the data is displayed, you'll need to update the modules or template you've created. If the template includes any other drag and drop areas, you can edit the page's non-dynamic content within the page editor. Any updates made to the dynamic or non-dynamic content will apply to both the listing page and the details pages, similar to editing a template.

### Start building[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#start-building)

To start building dynamic pages using HubDB,check out the [developer guide for building HubDB dynamic pages](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb).

### More resources[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#more-resources)

*   [How to build multi-level dynamic pages with HubDB](/docs/cms/guides/dynamic-pages/hubdb/multilevel)
*   [How to add videos to HubDB dynamic pages](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/video)
*   [How to join multiple HubDB tables](https://developers.hubspot.com/docs/cms/guides/hubdb/join-multiple-tables)

Creating dynamic referral URLs with query string parameters[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#creating-dynamic-referral-urls-with-query-string-parameters)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you have a setup where you'll need unique versions of each page URL while the content of the page remains the same across all versions, you should use query string parameters instead of dynamic pages.

When using dynamic pages, instances of your content are generated for every instance of a HubDB table or CRM object, but if the content is identical across all your pages, you will be flagged for duplicate content by search engines. This will lead to a scattered sitemap, a confusing website search experience, and extra entries in your website's page analytics.

By using query string parameters, you can accomplish the same goal of having a unique URL per referrer. You can even dynamically show unique content on a page if needed, but there won't be a dynamically generated page per instance of a HubDB table or CRM object; instead, there will only be one page with dynamic content that's shown based on the query string parameter.

Depending on whether you're using a HubDB table or CRM object as your data source, you'll need to use a different HubL function to query for the associated data in your account.

Consult the code snippets below, which both parse the logo ID from a URL such as `https://example.com/my-page?logo_identifier=123`.

### CRM objects[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#crm-objects)

The HubL code below checks whether a `logo_identifier` parameter is present in the query string, then uses the `crm_object` HubL function to fetch the data that corresponds to the associated logo record, which was created as a custom object.

{% if request.query\_dict.logo\_identifier %} <h3> The logo query string is present</h3> {% set logo\_identifier = request.query\_dict.logo\_identifier|string %} {% set query = "logo\_id=" + logo\_identifier %} {% set logo = crm\_object("logos", query, "logo\_name, logo\_id, logo\_url") %} Logo data: {{ logo }} <br> Logo id: {{ logo.logo }} <br> Logo name: {{ logo.name }} {% else %} <h3>The logo query string is NOT present</h3> {% endif %}

Learn more about the `crm_object` HubL function in [this article](/docs/cms/hubl/functions#crm-object).

### HubDB table[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#hubdb-table)

The HubL code below parses the `logo_identifier` parameter in the query string, then uses the `hubdb_table_rows` HubL function to fetch the logo's URL from the associated HubDB table (e.g., a table with an ID of `10181541`) using the logo ID from the query string.

{# get logo ID from query string#} {% set logo\_identifier = request.query\_dict.logo\_identifier|string %} {% set query = "identifier=" + logo\_identifier %} {% set logo\_row = hubdb\_table\_rows(10181541, query)\[0\] %} <img src="{{ logo\_row.logo.url }}" style="max-width: 500px;">

Or you can also invoke the `hubdb_table_row` function, though you'll need to pass the row ID in the query parameter.

{% set row\_id = request.query\_dict.logo\_identifier|string %} {% set logo\_row = hubdb\_table\_row(10181541, row\_id) %} <img src="{{ logo\_row.logo.url }}" style="max-width: 500px;">

Learn more about the `hubdb_table_row` HubL function in [this article](/docs/cms/hubl/functions#hubdb-table-row).

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/data/dynamic-pages#page-feedback)
-----------------------------------------------------------------------------------------------

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
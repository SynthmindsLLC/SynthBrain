---
title: "Breaking changes on the HubSpot platform"
description: "When developing an integration on the HubSpot platform, you'll need to be aware of the types of changes that HubSpot might make to its platform or data within. Below, learn about what HubSpot considers a breaking or non-breaking change, and use these lists to inform decisions you'll make when working with HubSpot's APIs."
type: "concept"
tags:
- "HubSpot"
- "API Changes"
- "Breaking Change Definition"
relationships:
- "#related_to [[REST APIs]]"
- "#related_to [[HubL]]"
- "#related_to [[Embedded Content]]"
- "#related_to [[JavaScript SDK]]"
- "#related_to [[Snowflake Data Share]]"
start_date: "2023-01-01"
end_date: "null"
---

Breaking changes on the HubSpot platform
========================================

When developing an integration on the HubSpot platform, you'll need to be aware of the types of changes that HubSpot might make to its platform or data within. Below, learn about what HubSpot considers a breaking or non-breaking change, and use these lists to inform decisions you'll make when working with HubSpot's APIs.

If a change is listed as a breaking change, we aim to provide you with 90 days notice if we do decide to make that change.

**Please note:** this notice period applies to developer products released to general availability. For beta and developer preview products, we’ll continue to update those regularly as we learn more about them. In certain situations, such as those related to security or privacy, we may shorten that 90 day timeframe.

As an example of correctly handling non-breaking changes, you can safely write (in pseudo code here) `if err.code === 500 then retry` but you should not write `if err.message === "Uh oh, something went wrong" then retry`. By asking yourself the question "if HubSpot makes a change listed as non-breaking, will this negatively impact the user experience?", you can write code that will be easier to maintain and create a more reliable app. 

REST APIs[](https://developers.hubspot.com/docs/breaking-change-definition#rest-apis)
-------------------------------------------------------------------------------------

Below, learn about what changes are breaking for incoming and outgoing RESTful APIs (e.g., contacts API and webhooks).

Breaking changes 

*   Removing an endpoint
*   Removing a field from the response (a “field” in this case is a JSON key/value pair)
*   Removing an option from a field in the request - If a request field could previously accept two String values, and we remove the ability to accept one of those, that would be a breaking change
*   Adding a new required field, header, or parameter in the request
*   Renaming a field
*   Changing the data type of a field
*   Changing field lengths past industry standard data limits (int, long, etc.)
*   Changing error response code or category
*   Changing auth types
*   Restricting scope
*   Reduce API limits
*   Making validation more stringent
*   Changing the default sort order
*   Significantly increase the size of a response (10x)

Non-breaking changes

*   Changing the error message
*   Adding a new option to a response (e.g., adding a new possible return value to a string field)
*   Adding a new optional input parameter
*   Property labels changing - Labels can be changed by HubSpot, application providers, and even customers. Integrations should not rely on property labels for their functionality.

HubL[](https://developers.hubspot.com/docs/breaking-change-definition#hubl)
---------------------------------------------------------------------------

Below, learn about what changes are considered breaking for HubL (e.g., the `hubdb_table_rows` function or `escape` filter).

Breaking changes

*   Removing a filter, function, variable or tag
*   Adding a new required argument
*   Changing the order of an argument
*   Change the data type of a field in a module/theme field JSON
*   Reduce the number of times a function can be invoked on a page

Non-breaking changes

*   Adding a new optional argument
*   Adding a new function, filter, variable or tag

Embedded content[](https://developers.hubspot.com/docs/breaking-change-definition#embedded-content)
---------------------------------------------------------------------------------------------------

Below, learn about what changes are considered breaking for embedded content (e.g., forms and CTAs).

Breaking changes

*   Adding or removing class names
*   Changing the timing or execution of custom form events (e.g. `onFormSubmit`)
*   Changing the timing or structure of global form events

Non-breaking changes

*   Add an optional setting for customizing the behavior of the embed

JavaScript SDK[](https://developers.hubspot.com/docs/breaking-change-definition#javascript-sdk)
-----------------------------------------------------------------------------------------------

Below, learn about what changes are considered breaking for JavaScript SDK (e.g., the calling SDK).

Breaking changes 

*   Removing an operation
*   Requiring a new argument to a function or field in an object that is passed to the function
*   Changing order of required parameters
*   Changing data type returned

Non-breaking changes

*   Adding a new function

Snowflake Data Share[](https://developers.hubspot.com/docs/breaking-change-definition#snowflake-data-share)
-----------------------------------------------------------------------------------------------------------

Occasionally, there will be changes to the schema that describes the data share. Any change that makes querying a share fail due to changing an existing schema object is considered a breaking change.

For example, renaming a table is a breaking change for the [Snowflake Data Share integration](https://knowledge.hubspot.com/reports/query-hubspot-data-in-snowflake) because queries referencing the former name of the table will fail after the rename. In this case, HubSpot will add a new table with the same data to the share so that you can begin using the new name. The old table will continue to exist until the end of the 90 day notice period.

Below, learn about what changes are considered breaking for the Snowflake Data Share.

Breaking changes 

*   Removing or renaming the database schema
*   Removing or renaming a table or view
*   Removing or renaming a column
*   Changing a column's datatype
*   Column nullability

Non-breaking changes

If a change is listed as a non-breaking change, it will be added to the schema with no notice given. For example, adding a new column to the schema.

This means that queries accessing shares should be as specific as possible when referencing schema objects. For example, you should always qualify tables by specifying the database schema they belong to. It also means that you shouldn’t use the `SELECT *`  clause in your queries, because that might break when a new column is added.

The following are examples of non-breaking changes:

*   Adding to the database schema
*   Adding a table or view
*   Adding a column
*   Changes to objects and their properties (e.g., the data within the `objects` and `object_properties` tables and views)

* * *

Share your feedback[](https://developers.hubspot.com/docs/breaking-change-definition#page-feedback)
---------------------------------------------------------------------------------------------------

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
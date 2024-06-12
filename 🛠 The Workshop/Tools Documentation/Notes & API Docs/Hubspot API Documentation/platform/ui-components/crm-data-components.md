---
Please provide me with more context! I need to know what the mission is about in order to help you complete it. 

For example, tell me: "* **What is the overall goal?** What are you trying to achieve?"
* **Who is the target audience?** Who are you trying to reach with this mission?
* **What are the specific objectives?** What are the key steps or tasks that need to be completed?
* **What are the resources available?** What tools, people, or information can you use to accomplish the mission?

Once you give me more information, I can help you develop a compelling and effective mission statement.
---

CRM data components (BETA)
==========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

CRM data components can pull data directly from the currently displaying CRM record, including information about associated records and single object reports. These components can only be placed in the middle column of CRM records.

These components are imported from `@hubspot/ui-extensions/crm`.

import { CrmAssociationPivot, CrmReport } from '@hubspot/ui-extensions/crm';

Available components[](https://developers.hubspot.com/docs/platform/ui-components/crm-data-components#available-components)
---------------------------------------------------------------------------------------------------------------------------

*   [CrmAssociationPivot](/docs/platform/ui-components/crmassociationpivot)
*   [CrmAssociationPropertyList](/docs/platform/ui-components/crmassociationpropertylist)
*   [CrmAssociationTable](/docs/platform/ui-components/crmassociationtable)
*   [CrmDataHighlight](/docs/platform/ui-components/crmdatahighlight)
*   [CrmPropertyList](/docs/platform/ui-components/crmpropertylist)
*   [CrmReport](/docs/platform/ui-components/crmreport)
*   [CrmStageTracker](/docs/platform/ui-components/crmstagetracker)
*   [CrmStatistics](/docs/platform/ui-components/crmstatistics)

Filtering data[](https://developers.hubspot.com/docs/platform/ui-components/crm-data-components#filtering-data)
---------------------------------------------------------------------------------------------------------------

In the `CrmAssociationPivot` and `CrmAssociationTable` components, you can filter the data to fetch only what's most relevant. Review the table below for available filtering options.

import { CrmAssociationPivot, CrmReport } from '@hubspot/ui-extensions/crm'; const Extension = () => { return ( <CrmAssociationPivot objectTypeId="0-1" associationLabels={\["CEO", "Co-founder"\]} maxAssociations={10} preFilters={\[ { "operator": "NOT\_IN", "property": "dealstage", "values": \["closedwon"\] } \]} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `operator` | `EQ` | `NEQ` | `LT` | `LTE` | `GT` | `GTE` | `BETWEEN` | `IN` | `NOT_IN` | `HAS_PROPTERTY` | `NOT_HAS_PROPERTY` | The filter's operator (e.g. `IN`). Can be one of:
*   `EQ`: is equal to `value`.
*   `NEQ`: is not equal to `value`.
*   `LT`: is less than `value`.
*   `LTE`:  is less than or equal to `value`.
*   `GT`:  is greater than `value`.
*   `GTE`: is greater than or equal to `value`.
*   `BETWEEN`: is within the specified range between `value` and `highValue`.
*   `IN`: is included in the specified `values` array. This operator is case-sensitive, so inputted values must be in lowercase. 
*   `NOT_IN`: is not included in the specified `values` array.
*   `HAS_PROPERTY`: has a value for the specified property.
*   `NOT_HAS_PROPERTY`: does not have a value for the specified property.

Learn more about [filtering CRM searches](/docs/api/crm/search#filter-operators). |
| `property` | String | The property to filter by. |
| `value` | String | number | The property value to filter by. |
| `values` | String | number | The property values to filter by when using an operator that requires an array, such as `IN`. |
| `highValue` | String | number | The upper value to filter by when using an operator that requires a range, such as `BETWEEN`. |

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crm-data-components#page-feedback)
-------------------------------------------------------------------------------------------------------------------

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
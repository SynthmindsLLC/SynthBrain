---
Please provide me with more context!  To help me write a compelling mission statement, tell me: "* **What is the purpose of this mission?** Is it for a company, a project, a personal goal, or something else entirely?"
* **What are the key values or goals?** What are you trying to achieve or accomplish?
* **Who is your target audience?** Who are you trying to reach with this mission? 

Once you provide me with this information, I can help you craft a powerful and inspiring mission statement!
---

CrmAssociationPivot | UI components (BETA)
==========================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmAssociationPivot` component is a CRM data component that renders a list of associated records organized by their assigned [association label](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels). You'll specify the type of records that you want to appear along with table attributes such as pagination, sorting, and more. You can either return all labels or specify the labels to return.

![ui-ext-components-associationspivot](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/ui-ext-components-associationspivot.png)

import { CrmAssociationPivot } from '@hubspot/ui-extensions/crm'; const Extension = () => { return ( <CrmAssociationPivot objectTypeId="0-1" associationLabels={\["CEO", "CEO of subsidiary", "Co-founder"\]} maxAssociations={10} preFilters={\[ { "operator": "NOT\_IN", "property": "dealstage", "values": \["closedwon"\] } \]} sort={\[ { "columnName": "createdate", "direction": -1 } \]} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `objectTypeId` Required | String | The numeric ID of the type of associated object to display (e.g., `0-1` for contacts). See [complete list](/docs/api/crm/understanding-the-crm#object-type-id) of object IDs. |
| `associationLabels` | Array | Filters results by specific association labels. By default, all association labels will appear. |
| `maxAssociations` | Number | The number of items to return in each association label group before displaying a "Show more" button. |
| `preFilters` | Array | Filters the data by specific values of the associated records. Review the [CRM data filter options](/docs/platform/ui-components/crm-data-components#filtering-data) for more information. |
| `sort` | Array | The default sorting behavior for the table. In the array, you'll include an object for the column you want to sort by, which specifies:
*   `columnName`: the column to sort by.
*   `direction`: the direction to sort by. Can be either `1` (ascending) or `-1` (descending). By default, order is ascending.

 |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpivot#related-components)
-----------------------------------------------------------------------------------------------------------------------

*   [CrmAssociationPropertyList](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpropertylist)
*   [CrmAssociationTable](https://developers.hubspot.com/docs/platform/ui-components/crmassociationtable)
*   [CrmReport](https://developers.hubspot.com/docs/platform/ui-components/crmreport)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpivot#page-feedback)
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
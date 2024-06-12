---
Please provide me with more context! I need to know what your mission is about in order to help you write it. 

For example, tell me: "* **What is the purpose of your mission?**  Is it for a company, a project, a personal goal?"
* **What are the key objectives you want to achieve?**
* **Who is your target audience?** 
* **What values or principles guide your mission?** 

Once I understand your goals, I can help you craft a clear, compelling, and impactful mission statement.
---

CrmAssociationPropertyList | UI components (BETA)
=================================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmAssociationPropertyList` component renders a list of properties belonging to a record associated with the currently displaying record. For example, you can use this component to display properties of a company record from its associated contact record. You can edit these property values inline, and changes will automatically save when leaving the field or pressing Enter.

![](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/ui-extensions-component-associationpropertylist.png)

import { CrmAssociationPropertyList } from '@hubspot/ui-extensions/crm'; const Extension = () => { return ( <CrmAssociationPropertyList objectTypeId="0-2" properties={\[ 'name', 'domain', 'city', 'state' \]} filters={\[ { operator: 'EQ', property: 'domain', value: 'meowmix.com' } \]} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `properties` Required | Array | The list of properties to display from the associated record, up to 12. |
| `objectTypeId` Required | String | The numeric ID of the type of associated object to display (e.g., `0-1` for contacts). See [complete list](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id) of object IDs. |
| `associationLabels` | Array | When provided, returns associated records that have all the specified labels. |
| `filters` | Array | Filters the data by specific values of the associated records. Review the [CRM data filter options](/docs/platform/ui-components/crm-data-components#filtering-data) for more information. |
| `sort` | Array | The default sorting behavior for the table. In each sort object in the array, you'll specify the following:
*   `columnName`: the column to sort by.
*   `direction`: the direction to sort by. Can be either `1` (ascending) or `-1` (descending). By default, order is ascending.

 |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpropertylist#related-components)
------------------------------------------------------------------------------------------------------------------------------

*   [CrmAssociationTable](https://developers.hubspot.com/docs/platform/ui-components/crmassociationtable)
*   [CrmReport](https://developers.hubspot.com/docs/platform/ui-components/crmreport)
*   [CrmAssociationPivot](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpivot)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpropertylist#page-feedback)
--------------------------------------------------------------------------------------------------------------------------

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
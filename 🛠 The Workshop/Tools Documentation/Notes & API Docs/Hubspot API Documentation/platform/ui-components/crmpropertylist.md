---
Please provide me with more context! To help me craft a compelling mission statement, I need to know: "* **What is the purpose of this mission?** Is it for a company, a project, a personal goal, a club, or something else?"
* **What are the core values and beliefs?**  What principles guide the mission?
* **What are the desired outcomes?** What impact do you want to achieve?
* **Who is the target audience?** Who will be impacted by this mission?

Once you provide me with this information, I can generate a strong and impactful mission statement for you!
---

CrmPropertyList | UI components (BETA)
======================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmPropertyList` component renders a list of properties along with their values. You can use this component to surface important property data from either the currently displaying record or another specified record. You can edit these property values inline and will automatically save when leaving the field or pressing Enter.

![ui-ext-components-propertylist](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/ui-ext-components-propertylist.png)

import { CrmPropertyList } from '@hubspot/ui-extensions/crm'; const Extension = () => { return ( <CrmPropertyList properties={\[ 'lastname', 'email', 'createdate', 'address', 'city', 'state', 'zip', \]} direction="row" /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `properties` Required | Array | The properties to display, up to four. By default, will display property data from the currently displaying record. To pull data from a specific record, include the `objectTypeId` and `objectId` props. |
| `direction` | `'column'` (default) | `'row'` | The layout direction of the table. |
| `objectTypeId` | String | The numeric ID of the type of associated object to display (e.g., `0-1` for contacts). See [complete list](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id) of object IDs. |
| `objectId` | String | The ID of the CRM record to display property data from. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmpropertylist#related-components)
-------------------------------------------------------------------------------------------------------------------

*   [CrmDataHighlight](https://developers.hubspot.com/docs/platform/ui-components/crmdatahighlight)
*   [CrmStageTracker](https://developers.hubspot.com/docs/platform/ui-components/crmstagetracker)
*   [CrmAssociationPivot](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpivot)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmpropertylist#page-feedback)
---------------------------------------------------------------------------------------------------------------

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
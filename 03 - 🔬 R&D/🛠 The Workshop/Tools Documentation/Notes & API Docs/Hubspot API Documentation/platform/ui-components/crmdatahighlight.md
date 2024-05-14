CrmDataHighlight | UI components (BETA)
=======================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmDataHighlight` component renders a list of properties along with their values. You can use this component to surface important property data from either the currently displaying record or another specified record.

![data-highlight](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/data-highlight.png?width=800&height=115&name=data-highlight.png)

import { CrmDataHighlight } from '@hubspot/ui-extensions/crm'; const Extension = () => { return ( <CrmDataHighlight properties={\["createdate", "lifecyclestage", "hs\_num\_open\_deals", "hs\_num\_child\_companies"\]} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `properties` Required | Array | The properties to display, up to four. By default, will display property data from the currently displaying record. To pull data from a specific record, include the `objectTypeId` and `objectId` props. |
| `objectTypeId` | String | The numeric ID of the type of associated object to display (e.g., `0-1` for contacts). See [complete list](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id) of object IDs. |
| `objectId` | String | The ID of the CRM record to display property data from. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmdatahighlight#related-components)
--------------------------------------------------------------------------------------------------------------------

*   [CrmPropertyList](https://developers.hubspot.com/docs/platform/ui-components/crmpropertylist)
*   [CrmStageTracker](https://developers.hubspot.com/docs/platform/ui-components/crmstagetracker)
*   [CrmAssociationPivot](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpivot)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmdatahighlight#page-feedback)
----------------------------------------------------------------------------------------------------------------

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
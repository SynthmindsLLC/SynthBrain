CrmStageTracker | UI components (BETA)
======================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmStageTracker` component renders a lifecycle or pipeline stage progress bar and a list of properties. Available for contacts, companies, deals, tickets, and custom objects.

Use this component to show stage progress for the currently displaying record, or you can specify a record. You can also edit the property values inline and your changes will automatically save when leaving the field or pressing Enter.

![ui-extensions-component-dealstagetracker](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/ui-extensions-component-dealstagetracker.png)

import { CrmStageTracker } from '@hubspot/ui-extensions/crm'; const Extension = () => { return ( <CrmStageTracker objectId="13833764681" objectTypeId="0-3" properties={\[ 'dealname', 'amount', \]} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `objectTypeId` Required | String | The numeric ID of the type of associated object to display (e.g., `0-1` for contacts. See [complete list](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id) of object IDs. |
| `objectId` Required | String | The ID of the CRM record to display property data from. |
| `properties` Required | Array | The properties to display, up to four. By default, will display property data from the currently displaying record. To pull data from a specific record, include the `objectTypeId` and `objectId` props. |
| `showProperties` | Boolean | Whether to display the properties below the progress indicator. When set to `false`, properties will not display. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmstagetracker#related-components)
-------------------------------------------------------------------------------------------------------------------

*   [CrmPropertyList](https://developers.hubspot.com/docs/platform/ui-components/crmpropertylist)
*   [CrmDataHighlight](https://developers.hubspot.com/docs/platform/ui-components/crmdatahighlight)
*   [CrmReport](https://developers.hubspot.com/docs/platform/ui-components/crmreport)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmstagetracker#page-feedback)
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
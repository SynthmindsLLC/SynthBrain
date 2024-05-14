CrmActionLink | UI components (BETA)
====================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmActionLink` component renders a clickable link that can execute a built-in set of [CRM actions](/docs/platform/ui-components/crm-action-components#available-actions).

This type of component is useful for enabling your extension to interact with other CRM entities, such as records and engagements. To learn more about how CRM action components work together, check out the [CRM action components overview](/docs/platform/ui-components/crm-action-components).

![ui-extensions-crm-action-link](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-crm-action-link.png?width=299&height=39&name=ui-extensions-crm-action-link.png)

import { CrmActionLink } from '@hubspot/ui-extensions/crm'; const dealContext = { objectTypeId: "0-3", objectId: 14795354663, }; hubspot.extend(({ context, runServerlessFunction, actions }) => { return ( <> <CrmActionLink actionType="ADD\_NOTE" actionContext={dealContext} > Add a note about this deal to the record </CrmActionLink> </> ); });

| Prop | Type | Description |
| --- | --- | --- |
| `actionType` Required | String | The type of action to perform. See [list of available actions](/docs/platform/ui-components/crm-action-components#available-actions) for more information. |
| `actionContext` Required | Object | An object containing the CRM object and record context for performing the action. See [list of available actions](/docs/platform/ui-components/crm-action-components#available-actions) for required context values. |
| `variant` | `'primary'`  (default)| `'light'` | `'dark'` | `'destructive'` | The color variation of the link. See the [variants section](#variants) for more information. |
| `onError` | (errors: string\[\]) => void | An optional callback that will pass any error messages that were generated. Common errors include missing required context values or the user not having sufficient permissions to perform an action. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/crmactionlink#variants)
---------------------------------------------------------------------------------------------

Using the `variant` prop, you can control the color of the link.

*   `primary`: the default blue (`#0091ae`).  
    ![design-guidelines-links_4](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_4.png?width=206&height=37&name=design-guidelines-links_4.png) 
*   `light`: a white link that turns to a lighter shade of blue on hover (`#7fd1de`).  
    ![design-guidelines-links_3](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_3.png?width=206&height=34&name=design-guidelines-links_3.png)
*   `dark`: a darker shade of blue (`#33475b`).  
    ![design-guidelines-links_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_2.png?width=206&height=38&name=design-guidelines-links_2.png)  
    
*   `destructive`: a red link (`#f2545b`).  
    ![design-guidelines-links_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_1.png?width=206&height=37&name=design-guidelines-links_1.png) 

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmactionlink#related-components)
-----------------------------------------------------------------------------------------------------------------

*   [CrmActionButtons](https://developers.hubspot.com/docs/platform/ui-components/crmactionbutton)
*   [Button](https://developers.hubspot.com/docs/platform/ui-components/button)
*   [CrmCardActions](https://developers.hubspot.com/docs/platform/ui-components/crmcardactions)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmactionlink#page-feedback)
-------------------------------------------------------------------------------------------------------------

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
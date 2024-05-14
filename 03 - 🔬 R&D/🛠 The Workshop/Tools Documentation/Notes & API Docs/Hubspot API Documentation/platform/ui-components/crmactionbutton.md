CrmActionButton | UI components (BETA)
======================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmActionButton` component renders a button that can execute a built-in set of [CRM actions](/docs/platform/ui-components/crm-action-components#available-actions).

This type of component is useful for enabling your extension to interact with other CRM entities, such as records and engagements. To learn more about how CRM action components work together, check out the [CRM action components overview](/docs/platform/ui-components/crm-action-components).

![ui-extensions-crm-action-button](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-crm-action-button.png?width=397&height=64&name=ui-extensions-crm-action-button.png)

import { CrmActionButton } from '@hubspot/ui-extensions/crm'; <CrmActionButton actionType="PREVIEW\_OBJECT" actionContext={{ objectTypeId: "0-3", objectId: 123456 }} variant="secondary" > Preview deal </CrmActionButton>

| Prop | Type | Description |
| --- | --- | --- |
| `actionType` Required | String | The type of action to perform. See [list of available actions](/docs/platform/ui-components/crm-action-components#available-actions) for more information. |
| `actionContext` Required | Object | An object containing the CRM object and record context for performing the action. See [list of available actions](/docs/platform/ui-components/crm-action-components#available-actions) for required context values. |
| `variant` | `'primary'` | `'secondary'` (default) | `'destructive'` | The color variation of the button. |
| `type` | `'button'` (default) | `'reset'` | `'submit'` | The button's HTML `role` attribute. |
| `size` | `'xs'`, `'extra-small'` | `'sm'`, `'small'` | `'md'`, `'medium'` (default) | The size of the button. |
| `disabled` | Boolean | When set to to `true`, button renders in a disabled, greyed-out state and cannot be clicked. |
| `onError` | (errors: string\[\]) => void | An optional callback that will pass any error messages that were generated. Common errors include missing required context values or the user not having sufficient permissions to perform an action. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/crmactionbutton#variants)
-----------------------------------------------------------------------------------------------

Using the `variant` prop, you can set the color of the button.

*   **Primary:** a dark blue button for the most frequently used or most important action on an extension. Each extension should only have one primary button.  
    ![design-guide-button-type-primary](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guide-button-type-primary.png?width=196&height=65&name=design-guide-button-type-primary.png)
    *   **Secondary:** a grey button to provide alternative or non-primary actions. Each extension should include no more than two secondary buttons.  
        ![design-guide-button-type-secondary](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guide-button-type-secondary.png?width=205&height=65&name=design-guide-button-type-secondary.png)

*   **Destructive:** a red button for actions that delete, disconnect, or perform any action that the user can't undo. Button text should clearly communicate what is being deleted or disconnected. After a destructive button is clicked, the user should have to verify or confirm the action.  
    ![design-guide-button-type-destructive](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guide-button-type-destructive.png?width=211&height=65&name=design-guide-button-type-destructive.png)

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmactionbutton#related-components)
-------------------------------------------------------------------------------------------------------------------

*   [CrmActionLink](https://developers.hubspot.com/docs/platform/ui-components/crmactionlink)
*   [CrmCardActions](https://developers.hubspot.com/docs/platform/ui-components/crmcardactions)
*   [Dropdown](https://developers.hubspot.com/docs/platform/ui-components/dropdown)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmactionbutton#page-feedback)
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
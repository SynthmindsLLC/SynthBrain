---
Please provide me with more information about the mission you're writing about. I need context to help you craft a compelling mission statement. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a non-profit, or something else?"
* **What are the goals and objectives?** What are you trying to achieve?
* **Who is the target audience?** Who will benefit from this mission?
* **What are the values and principles that guide this mission?**

Once you give me more details, I can help you write a strong and impactful mission statement.
---

CrmCardActions | UI components (BETA)
=====================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmCardActions` component renders a smaller standalone or dropdown menu button that can contain multiple [CRM actions](/docs/platform/ui-components/crm-action-components#available-actions).

This type of component is useful for enabling your extension to interact with other CRM entities, such as records and engagements. To learn more about how CRM action components work together, check out the [CRM action components overview](/docs/platform/ui-components/crm-action-components).

![2023-08-29_15-08-37 (1)](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/2023-08-29_15-08-37%20(1).gif?width=323&height=280&name=2023-08-29_15-08-37%20(1).gif)

import { CrmCardAction } from '@hubspot/ui-extensions/crm'; <CrmCardActions actionConfigs={\[ { type: "action-library-button", label: "Preview", actionType: "PREVIEW\_OBJECT", actionContext: { objectTypeId:"0-3", objectId: 14795354663 }, tooltipText: "Preview this deal record." }, { type: "dropdown", label: "Activities", options: \[ { type: "action-library-button", label: "Send email", actionType: "SEND\_EMAIL", actionContext: { objectTypeId: "0-1", objectId: 769851 } }, { type: "action-library-button", label: "Add note", actionType: "ADD\_NOTE", actionContext: { objectTypeId: "0-1", objectId: 769851 }, } \] } \]} />

Unlike [CrmActionButton](/docs/platform/ui-components/crmactionbutton) and [CrmActionLink](/docs/platform/ui-components/crmactionlink) where props such as `actionType` are accepted at the top level, `CrmCardActions` includes an `actionConfigs` prop which accepts fields for action configuration. 

| Prop | Type | Description |
| --- | --- | --- |
| `actionConfigs` Required | Array | An array that stores fields for configuration button actions. See below for list of supported fields. |
| `label` | String | The button's label text. |
| `onError` | (errors: string\[\]) => void | An optional callback that will pass any error messages that were generated. Common errors include missing required context values or the user not having sufficient permissions to perform an action. |

In the `actionConfigs` array, you can include the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `type` Required | `'action-library-button'` |  
`'dropdown'` | The type of button to render:
*   `action-library-button`: a standalone button that can perform one action.
*   `dropdown`: a dropdown menu button containing multiple `'action-library-button'` actions. When using this type, you'll need to include an `options` array containing each action.

 |
| `options` | Array | For `dropdown` type buttons, this array stores objects for each action in the dropdown menu. Each action should be set to the `'action-library-button'` type. |
| `actionType` Required | String | The type of action to perform. See [list of available actions](/docs/platform/ui-components/crm-action-components#available-actions) for more information. |
| `actionContext` Required | Object | An object containing the CRM object and record context for performing the action. See [list of available actions](/docs/platform/ui-components/crm-action-components#available-actions) for required context values. |
| `disabled` | Boolean | When set to `true`, the button or dropdown menu option will render in a disabled, greyed-out state and can't be clicked. |
| `tooltipText` | String | Tooltip text that appears when hovering over the button or dropdown menu option. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmcardactions#related-components)
------------------------------------------------------------------------------------------------------------------

*   [CrmActionLink](https://developers.hubspot.com/docs/platform/ui-components/crmactionlink)
*   [Button](https://developers.hubspot.com/docs/platform/ui-components/button)
*   [ButtonRow](https://developers.hubspot.com/docs/platform/ui-components/buttonrow)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmcardactions#page-feedback)
--------------------------------------------------------------------------------------------------------------

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
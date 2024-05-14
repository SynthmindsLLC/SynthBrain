ButtonRow | UI components (BETA)
================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `ButtonRow` component renders a row of [Button](/docs/platform/ui-components/button)[](https://developers.hubspot.com/docs/platform/ui-extension-components?hs_preview=YSMJqMjb-115642861738#button) components. In `ButtonRow`, you'll specify individual `Button` components.  Use this component When you want to include multiple buttons in a row.

![design-guide-button-row-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guide-button-row-component.png?width=900&height=178&name=design-guide-button-row-component.png)

1.  **Primary button:** only use one per extension.
2.  **Secondary button:** only use with a primary and/or destructive button.
3.  **Destructive button:** only use for actions that are destructive, paired with a secondary button.

import { Button, ButtonRow } from '@hubspot/ui-extensions'; const Extension = () => { return ( <ButtonRow disableDropdown={false}> <Button onClick={() => { console.log('Regular button clicked'); }} > Regular Button </Button> <Button onClick={() => { console.log('Reset button clicked'); }} variant="destructive" type="reset" > Reset </Button> <Button onClick={() => { console.log('Submit button clicked'); }} variant="primary" type="submit" > Submit </Button> </ButtonRow> ); };

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `disableDropdown` | Boolean | Disables the dropdown list of buttons that appears when child button expand beyond horizontal space. By default, set to `false`. |

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/buttonrow#usage-examples)
-----------------------------------------------------------------------------------------------------

*   A primary and secondary button in a row to progress through a multi-step form.  
    ![design-guide-button-row-example](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-row-example.png?width=217&height=69&name=design-guide-button-row-example.png)
*   A destructive and secondary button in a row to confirm and cancel a contact deletion.  
    ![buttonrow-example-cancel-delete-contact](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/buttonrow-example-cancel-delete-contact.png?width=285&height=73&name=buttonrow-example-cancel-delete-contact.png)

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/buttonrow#guidelines)
---------------------------------------------------------------------------------------------

*   **DO:** include a secondary button with a destructive button to allow users to cancel the action.
*   **DON'T:** use multiples of the same button type in a row. For example, don't include more than one primary button in one row.
*   **DON'T:** use more than two secondary buttons in a single extension.
*   **DON'T:** use more than three buttons in a row.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/buttonrow#related-components)
-------------------------------------------------------------------------------------------------------------

*   [Button](https://developers.hubspot.com/docs/platform/ui-components/button)
*   [CRM action components](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components)
*   [CrmActionButton](https://developers.hubspot.com/docs/platform/ui-components/crmactionbutton)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/buttonrow#page-feedback)
---------------------------------------------------------------------------------------------------------

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
Button | UI components (BETA)
=============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Button` component renders a single button. Use this component to enable users to perform actions, such as submitting a form, sending data to an external system, or deleting data.

Button text is passed into the component like a standard HTML element, rather than through a prop. 

![design-guide-button-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-component.png?width=920&name=design-guide-button-component.png)

1.  **Button text:** the visible button text that describes the button's action.
2.  **Variant:** the color of the button. Learn more about [available button variants below](#variants).

import { Button } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Button onClick={() => { console.log('Someone clicked the button!'); }} href="https://hubspot.com" variant="destructive" size="md" type="button" > Click me! </Button> ); };

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `href` | String  | Navigates to a URL on button click. When a button includes both `href` and an `onClick` action, both will be executed on button click. Links to external pages will open in a new tab, while links to pages in the HubSpot account will open in the same tab. |
| `onClick` | () => void | A function that will be invoked when the button is clicked. It receives no arguments and it's return value is ignored |
| `disabled` | Boolean | When set to `true`, the button will render in a greyed-out state and cannot be clicked. |
| `variant` | `'primary'` | `'secondary'` (default) | `'destructive'` | Sets the color of the button. See [variants section](#variants) for more information. |
| `type` | `'button'` (default) | `'reset'` | `'submit'` | Sets the `role` HTML attribute of the button. |
| `size` | `'xs'`, `'extra-small'` | `'sm'`, `'small'` | `'med'`, `'medium'` (default) | The size of the button. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/button#variants)
--------------------------------------------------------------------------------------

Using the `variant` prop, you can set the color of the button.  

*   **Primary:** a dark blue button for the most frequently used or most important action on an extension. Each extension should only have one primary button.  
    ![design-guide-button-type-primary](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guide-button-type-primary.png?width=196&height=65&name=design-guide-button-type-primary.png)

*   **Secondary:** a grey button to provide alternative or non-primary actions. Each extension should include no more than two secondary buttons.  
    ![design-guide-button-type-secondary](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guide-button-type-secondary.png?width=205&height=65&name=design-guide-button-type-secondary.png)

*   **Destructive:** a red button for actions that delete, disconnect, or perform any action that the user can't undo. Button text should clearly communicate what is being deleted or disconnected. After a destructive button is clicked, the user should have to verify or confirm the action.  
    ![design-guide-button-type-destructive](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guide-button-type-destructive.png?width=211&height=65&name=design-guide-button-type-destructive.png)

**Please note:** HubSpot does not provide variant options for the orange buttons you’ll find across the app (both solid and outlined). Those color variants are reserved for the HubSpot product, which helps to maintain the hierarchy of available actions on a given page.

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/button#usage-examples)
--------------------------------------------------------------------------------------------------

*   Use a `primary` button at the end of a form to submit data to another system.
*   Use a `secondary` button next to a primary form submit button to reset form fields.
*   Use a `destructive` button to enable users to delete a contact's data from an external system.
*   Set a button to `disabled` when a contact doesn't qualify for a form submission due to missing criteria or other ineligibility.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/button#guidelines)
------------------------------------------------------------------------------------------

*   **DO:** set button text that clearly communicates what action will occur when a user clicks it. Text should be unambiguous and concise (~2-4 words).
*   **DO:** use sentence-casing for button text (only the first word capitalized)
*   **DO:** minimize the number of buttons that appear on a page record across all extensions.
*   **DON'T:** include multiple primary buttons in a single extension.
*   **DON'T:** use a destructive button unless the consequences are significant or irreversible.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/button#related-components)
----------------------------------------------------------------------------------------------------------

*   [ButtonRow](https://developers.hubspot.com/docs/platform/ui-components/buttonrow)
    
*   [](https://developers.hubspot.com/docs/platform/ui-components/buttonrow)[CRM action components](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components)
    
*   [](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components)[CrmActionButton](https://developers.hubspot.com/docs/platform/ui-components/crmactionbutton)
    
*   [Panel](/docs/platform/ui-components/panel)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/button#page-feedback)
------------------------------------------------------------------------------------------------------

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
---
Please provide me with more information!  To write a mission statement, I need to know: "* **What is the purpose of this mission?** Is it for a company, a project, a personal goal?"
* **What are the key values and goals?** What are you trying to achieve?
* **Who is your target audience?** Who are you trying to reach with this mission?

Once you provide me with these details, I can help you craft a compelling mission statement!
---

Dropdown | UI components (BETA)
===============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Dropdown` component renders a dropdown menu that can appear as a button or hyperlink.  Use this component to enable users to select from multiple options in a compact list. This component includes sizing options.

![ui-extensions-dropdown-variants](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-dropdown-variants.gif?width=466&height=230&name=ui-extensions-dropdown-variants.gif)

import { Dropdown } from '@hubspot/ui-extensions'; const Extension = () => { const ddOptions = \[ { label: 'Clone', onClick: () => console.log({ message: 'Clone group' }) }, { label: 'Delete', onClick: () => console.log({ message: 'Delete group' }) } \] return ( <Dropdown options={ddOptions} variant="primary" buttonSize="md" buttonText="More" /> ); };

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `options`   Required |  Object | The options included in the dropdown menu. For each option, include:  
*   `label`: the text label for the option.
*   `onClick`: the function that gets invoked when the option is selected.

 |
| `variant` |  `'primary'` (default) | `'secondary'` | `'transparent'` | The type of dropdown button to display. `'primary'` and `'secondary'` will display a blue and grey button, respectively, while `'transparent'` will display a blue hyperlink. |
| `buttonText` |  String | The button text. |
| `buttonSize` |  `'xs'`, `'extra-small'` | `'sm'`, `'small'` | `'md'`, `'medium'` (default) | The size of the button. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/dropdown#variants)
----------------------------------------------------------------------------------------

Using the `variant` and `buttonSize` props, you can set the type of button along with its size.

*   `'primary'` buttons with size set to `'xs'`, `'sm'`, and `'md'` respectively:  
    ![dropdown-buttons-primary](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/dropdown-buttons-primary.png?width=117&height=170&name=dropdown-buttons-primary.png)
*   `'secondary'` buttons with size set to `'xs'`, `'sm'`, and `'md'` respectively:  
    ![dropdown-buttons-secondary](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/dropdown-buttons-secondary.png?width=117&height=178&name=dropdown-buttons-secondary.png)
*   `'transparent'` buttons with size set to `'sm'` and `'md'` respectively:  
    ![dropdown-buttons-transparent](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/dropdown-buttons-transparent.png?width=97&height=120&name=dropdown-buttons-transparent.png)

Related components[](https://developers.hubspot.com/docs/platform/ui-components/dropdown#related-components)
------------------------------------------------------------------------------------------------------------

*   [CrmActionLink](https://developers.hubspot.com/docs/platform/ui-components/crmactionlink)
*   [CrmCardActions](https://developers.hubspot.com/docs/platform/ui-components/crmcardactions)
*   [Button](https://developers.hubspot.com/docs/platform/ui-components/button)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/dropdown#page-feedback)
--------------------------------------------------------------------------------------------------------

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
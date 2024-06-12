---
Please provide me with more context!  To help you write a mission statement, I need to know: "* **What is the mission for?**  Is it for a company, a project, a personal goal, a non-profit organization, etc.? "
* **What is the purpose or objective?** What do you want to achieve? 
* **Who are you serving?**  Who are you trying to help or benefit?
* **What are your core values?** What principles guide your actions?

Once you provide me with this information, I can help you craft a compelling and impactful mission statement.
---

RadioButton | UI components (BETA)
==================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `RadioButton` component renders a radio select button. If you want to include more than two radio buttons, or are building a form, it's recommended to use the [ToggleGroup](/docs/platform/ui-components/togglegroup) component instead.

![ui-extensions-component-radio-buttons](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-component-radio-buttons.png?width=300&height=142&name=ui-extensions-component-radio-buttons.png)

import { RadioButton } from '@hubspot/ui-extensions'; function Extension() { const \[roleType, setRoleType\] = useState( 'support' ); return ( <> <RadioButton checked={roleType === 'superAdmin'} name="roleType" description="Select to grant superpowers." onChange={() => { setRoleType('superAdmin'); }} > Super Admin </RadioButton> <RadioButton checked={roleType === 'support'} name="roleType" description="Select to assign a Support role." onChange={() => { setRoleType('support'); }} > Customer Support </RadioButton> </> ); }

| Prop | Type | Description |
| --- | --- | --- |
| `name` | String | The input's unique identifier. |
| `value` | String | number | The radio button value. This value is not displayed, but is passed on the server side when submitted, along with `name`. |
| `checked` | Boolean | Whether the radio button is currently selected. Default is `false`. |
| `initialIsChecked` | Boolean | When set to `true`, the option will be selected by default. Default is `false`. |
| `description` | String | Text that describes the field's purpose. |
| `readonly` | Boolean | When set to `true`, users will not be able to enter a value into the field. Set to `false` by default. |
| `variant` | `'sm'`, `'small'` | `'default'` (default) | The size of the checkbox. |
| `inline` | Boolean | When set to `true`, arranges radio buttons side by side. Default is `false`. |
| `onChange` | (checked: boolean, value: string) \=> void | A callback function that is invoked when the radio button is selected. Passes the new value. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/radiobutton#related-components)
---------------------------------------------------------------------------------------------------------------

*   [Checkbox](https://developers.hubspot.com/docs/platform/ui-components/checkbox)
*   [ToggleGroup](https://developers.hubspot.com/docs/platform/ui-components/togglegroup)
*   [TextArea](https://developers.hubspot.com/docs/platform/ui-components/textarea)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/radiobutton#page-feedback)
-----------------------------------------------------------------------------------------------------------

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
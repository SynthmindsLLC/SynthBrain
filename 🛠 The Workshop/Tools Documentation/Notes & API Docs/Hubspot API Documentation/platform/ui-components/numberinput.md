---
Please provide me with the context or the rest of the mission statement.  I need more information to help you complete it. For example: "* **What is the mission for?** Is it for a company, a project, a team, a personal goal? "
* **What are the key values or goals?** What do you want to achieve? 
* **Who is the target audience?** Who is this mission statement for? 

Once I have more information, I can help you write a compelling and impactful mission statement.
---

NumberInput | UI components (BETA)
==================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `NumberInput` component renders a number input field. Commonly used within the [Form](/docs/platform/ui-components/form) component. 

![design-guidelines-number-input](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guidelines-number-input.png?width=700&height=183&name=design-guidelines-number-input.png)

1.  **Label:** the input's label.
2.  **Description:** the text that describes the field's purpose.
3.  **Value:** an entered value.

import { NumberInput } from '@hubspot/ui-extensions'; const Extension = () => { const \[portalCount, setPortalCount\] = useState(0); return ( <NumberInput label={'HubSpot Portal Count'} name="portalsNumber" description={'Number of active portals'} placeholder={'number of portals'} value={portalCount} onChange={value => setPortalCount(value)} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `name` Required | String | The input's unique identifier. |
| `label` Required | String | The text that displays above the dropdown menu. |
| `value` | String | number | The value of the input. |
| `defaultValue` | Number | The value of the input on initial render. |
| `description` | String | Text that describes the field's purpose. |
| `required` | Boolean | When set to `true`, displays a required field indicator. |
| `readOnly` | Boolean | When set to `true`, users will not be able to enter a value into the field. Set to `false` by default. |
| `placeholder` | String | The text that appears in the input before a value is set. |
| `tooltip` | String | The text that displays in a tooltip next to the label. |
| `error` | Boolean | When set to `true`, `validationMessage` is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. When `false` (default), `validationMessage` is displayed as a success message.  
  
 |
| `validationMessage` | String | The text to display if the input has an error. |
| `min` | Number | Sets the lower bound of the input. |
| `max` | Number | Sets the upper bound of the input. |
| `precision` | Number | Sets the number of digits to the right of the decimal point. |
| `formatStyle` | `'decimal'` | `'percentage'` | Formats the input as a decimal or percentage. |
| `onBlur` | (value: number) => void | A function that is called every time the field loses focus, passing the value. |
| `onChange` | (value: number) => void | A callback function that is invoked when the value is committed. Currently these times are `onBlur` of the input and when the user submits the form. |
| `onFocus` | (value: number) => void | A function that is called every time the field gets focused on, passing the value. |

Usage example[](https://developers.hubspot.com/docs/platform/ui-components/numberinput#usage-example)
-----------------------------------------------------------------------------------------------------

A field in a form where salespeople can enter the total deal amount.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/numberinput#guidelines)
-----------------------------------------------------------------------------------------------

*   **DO:** make label and description text concise and clear.
*   **DO:** include placeholder text to help users understand what's expected in the field.
*   **DO:** indicate if there is a minimum or maximum number requirement.
*   **DO:** indicate if a field is required.
*   **DO:** include clear validation error messages so that users know how to fix errors.
*   **DON'T:** use this component for long responses, such as open-ended comments or feedback. Instead, use the [TextArea component](/docs/platform/ui-components/textarea).
*   **DON'T:** use placeholder text for critical information, as it will disappear once users begin to type. Critical information should be placed in the label and descriptive text, with additional context in the tooltip if needed.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/numberinput#related-components)
---------------------------------------------------------------------------------------------------------------

*   [Form](https://developers.hubspot.com/docs/platform/ui-components/form)
*   [DateInput](https://developers.hubspot.com/docs/platform/ui-components/dateinput)
*   [MultiSelect](https://developers.hubspot.com/docs/platform/ui-components/multiselect)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/numberinput#page-feedback)
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
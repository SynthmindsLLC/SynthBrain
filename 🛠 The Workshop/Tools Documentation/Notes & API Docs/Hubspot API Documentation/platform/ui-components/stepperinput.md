StepperInput | UI components (BETA)
===================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `StepperInput` component renders a number input field that can be increased or decreased by a set number.

This component inherits many of its props from the `NumberInput` component, with an additional set of props to control the increase/decrease interval.

![ui-extension-component-stepper-input](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extension-component-stepper-input.gif?width=672&height=209&name=ui-extension-component-stepper-input.gif)

import { StepperInput } from '@hubspot/ui-extensions'; return ( <StepperInput min={5} max={20} minValueReachedTooltip="You need to eat at least 5 cookies." maxValueReachedTooltip="More than 20 cookies is a bit much." label="Number of cookies to eat" name="cookiesField" description={'I want cookies'} value={cookies} stepSize={5} onChange={(value) => { setCookieCount(value); }} /> );

| Prop | Type | Description |
| --- | --- | --- |
| `name` Required | String | The input's unique identifier. |
| `label` Required | String | The text that displays above the input. |
| `stepSize`  | Number | The amount that the current value will increase or decrease by. Default is `1`. |
| `min` | Number | The lowest number allowed in the input. |
| `max` | Number | The highest number allowed in the input. |
| `minValueReachedTooltip` | String | Text that will appear in a tooltip when the user has reached the minimum value. |
| `maxValueReachedTooltip` | String | Text that will appear in a tooltip when the user has reached the maximum value. |
| `precision` | Number | The number of digits to the right of the decimal point. |
| `formatStyle` | `'decimal'` (default) | `'percentage'` | Formats the number as a decimal or percentage. |
| `value` | String | The value of the input. |
| `defaultValue` | String | The default input value.  |
| `placeholder` | String | Text that appears in the input when no value is set. |
| `required` | Boolean | When set to `true`, displays a required field indicator. Default is `false`. |
| `tooltip` | String | The text that displays in a tooltip next to the label. |
| `readOnly` | Boolean | When set to `true`, the checkbox cannot be selected. Default is `false`. |
| `description` | String | Text that describes the field's purpose. |
| `error` | Boolean | When set to `true`, `validationMessage` is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left `false` (default), `validationMessage` is displayed as a success message. |
| `validationMessage` | String | The text to display if the input has an error. |
| `onChange` | (value: number) => void | A callback function that is called with the new value or values when the list is updated. |
| `onFocus` | (value: number) => void | A function that is called and passed the value when the field gets focused. |
| `onBlur` | (value: number) => void | A function that is called and passes the value when the field loses focus. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/stepperinput#related-components)
----------------------------------------------------------------------------------------------------------------

*   [Form](https://developers.hubspot.com/docs/platform/ui-components/form)
*   [DateInput](https://developers.hubspot.com/docs/platform/ui-components/dateinput)
*   [NumberInput](https://developers.hubspot.com/docs/platform/ui-components/numberinput)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/stepperinput#page-feedback)
------------------------------------------------------------------------------------------------------------

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
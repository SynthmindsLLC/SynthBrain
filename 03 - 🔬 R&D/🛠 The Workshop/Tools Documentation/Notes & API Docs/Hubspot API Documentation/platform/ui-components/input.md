Input | UI components (BETA)
============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Input` component renders a text input field where a user can enter a custom text value. Like other inputs, this component should only be used within a [Form](/docs/platform/ui-components/form) that has a submit button.

![design-guidelines-input](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guidelines-input.png?width=665&height=203&name=design-guidelines-input.png)

1.  **Label:** the input's label.
2.  **Description:** the text that describes the field's purpose.
3.  **Placeholder:** the placeholder value that displays when no value has been entered.
4.  **Required field indicator:** communicates to the user that the field is required for form submission.
5.  **Tooltip:** on hover, displays additional information about the field.

import {useState } from 'react'; import { Form, Input } from '@hubspot/ui-extensions'; const Extension = () => { const \[name, setName\] = useState(''); const \[validationMessage, setValidationMessage\] = useState(''); const \[isValid, setIsValid\] = useState(true); return ( <Form> <Input label="First Name" name="first-name" tooltip="Please enter your first name" description="Please enter your first name" placeholder="First name" required={true} error={!isValid} validationMessage={validationMessage} onChange={value => { setName(value); }} onInput={value => { if (value !== 'Bill') { setValidationMessage('This form only works for people named Bill'); setIsValid(false); } else if (value === '') { setValidationMessage('First name is required'); setIsValid(false); } else { setValidationMessage('Valid first name!'); setIsValid(true); } }} /> <Input label="Password" name="password" description="Enter your password" placeholder="Password" onInput={() => {}} type="password" /> </Form> ); };

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `name`   Required |  String | The input's unique identifier, similar to the [HTML input element name attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name). |
| `label` Required |  String | The text that displays above the input. Required if `inputType` is not set to `hidden`. |
| `required` |  Boolean | When set to `true`, displays a required field indicator. |
| `value` |  Function | The value of the input. |
| `type` | `'text'` (default) | `'password'` | The type of input. An input with the `'password'` type will hide the characters that the user types. |
| `readOnly` | Boolean | When set to `true`, users will not be able to enter a value into the field. |
| `description` | String | Displayed text that describes the field's purpose. |
| `tooltip` | String | The text that displays in a tooltip next to the input label. |
| `placeholder` | String | The text that appears in the input before a value is set. |
| `error` | Boolean | When set to `true`, `validationMessage` is displayed as an error message if provided. The input will also render in an error state so that users are aware. If left `false`, `validationMessage` is displayed as a success message. |
| `validationMessage` | String | The text to show if the input has an error. |
| `onChange` | (value: string) => void | A callback function that is invoked when the value is committed. Currently, these are `onBlur` of the input and when the user submits the form. |
| `onInput` | (value: string) => void | A function that is called and passes the value when the field is edited by the user. Should be used for validation. It's recommended that you don't use this value to update state (use `onChange` instead). |
| `onBlur` | (value: string) => void | A function that is called and passes the value when the field loses focus. |
| `onFocus` | (value: string) => void | A function that is called and passed the value when the field gets focused. |

Usage example[](https://developers.hubspot.com/docs/platform/ui-components/input#usage-example)
-----------------------------------------------------------------------------------------------

Use for form fields where a user can enter any text value, such as email address or name.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/input#guidelines)
-----------------------------------------------------------------------------------------

*   **DO:** make label and description text concise and clear.
*   **DO:** include placeholder text to help users understand what's expected in the field.
*   **DO:** indicate if a field is required.
*   **DO:** include clear validation error messages so that users know how to fix errors.
*   **DON'T:** use this component for long responses, such as open-ended comments or feedback. Instead, use the [TextArea component](/docs/platform/ui-components/textarea).
*   **DON'T:** use placeholder text for critical information, as it will disappear once users begin to type. Critical information should be placed in the label and descriptive text, with additional context in the tooltip if needed.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/input#related-components)
---------------------------------------------------------------------------------------------------------

*   [Select](https://developers.hubspot.com/docs/platform/ui-components/select)
*   [TextArea](https://developers.hubspot.com/docs/platform/ui-components/textarea)
*   [Form](https://developers.hubspot.com/docs/platform/ui-components/form)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/input#page-feedback)
-----------------------------------------------------------------------------------------------------

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
---
Please provide me with the rest of your mission statement! I need more context to understand what you're trying to achieve. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a personal goal, or something else?"
* **What are the main objectives?** What are you trying to accomplish?
* **What are the values?** What principles guide your actions?

Once you provide more information, I can help you complete your mission statement.
---

TextArea | UI components (BETA)
===============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `TextArea` component renders a fillable text field. Includes props to customize the size of the field along with maximum number of characters and resizability.

![design-guidelines-text-area](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-text-area.png)

1.  **Label:** the field's label.
2.  **Description:** the text that describes the field's purpose.
3.  **Value:** an entered value.
4.  **Required field indicator:** communicates to the user that the field is required for form submission.
5.  **Tooltip:** on hover, displays additional information about the field.

import { TextArea } from '@hubspot/ui-extensions'; import { useState } from 'react'; const Extension = () => { const \[description, setDescription\] = useState(''); const \[validationMessage, setValidationMessage\] = useState(''); const \[isValid, setIsValid\] = useState(true); return ( <Form> <TextArea label="Description" name="description" tooltip="Provide as much detail as possible" description="Please include a link" placeholder="My description" required={true} error={!isValid} validationMessage={validationMessage} onChange={value => { setDescription(value); }} onInput={value => { if (!value.includes('http')) { setValidationMessage('A link must be included.'); setIsValid(false); } else { setValidationMessage('Valid description!'); setIsValid(true); } }} /> </Form> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `name` Required | String | The input's unique identifier. |
| `label` Required | String | The text that displays above the input. |
| `value` | String | The value of the input. |
| `description` | String | Text that describes the field's purpose. |
| `tooltip` | String | The text that displays in a tooltip next to the label. |
| `placeholder` | String | Text that appears in the input when no value is set. |
| `required` | Boolean | When set to `true`, displays a required field indicator. Default is `false`. |
| `cols` | Number | The visible width of the text field in average character widths. |
| `rows` | Number | The number of visible text lines for the text field. |
| `maxLength` | Number | The maximum number of characters (UTF-16 code units) that the user can enter. If not specified, maximum length is unlimited. |
| `resize` | `'vertical'` | `'horizontal'` | `'both'` (default) | `'none'` | The maximum number of characters (UTF-16 code units) that the user can enter. If not specified, maximum length is unlimited. |
| `readOnly` | Boolean | When set to `true`, the checkbox cannot be selected. Default is `false`. |
| `error` | Boolean | When set to `true`, `validationMessage` is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left `false` (default), `validationMessage` is displayed as a success message. |
| `validationMessage` | String | The text to display if the input has an error. |
| `onChange` | (value: number) => void | A callback function that is called with the new value or values when the list is updated. |
| `onFocus` | (value: number) => void | A function that is called and passed the value when the field gets focused. |
| `onBlur` | (value: number) => void | A function that is called and passes the value when the field loses focus. |
| `onInput` | (value: number) => void | A function that is called and passes the value when the field is edited by the user. Should be used for validation. It's recommended that you don't use this value to update state (use `onChange`instead). |

Usage example[](https://developers.hubspot.com/docs/platform/ui-components/textarea#usage-example)
--------------------------------------------------------------------------------------------------

A field where salespeople can leave comments after meeting a new client.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/textarea#guidelines)
--------------------------------------------------------------------------------------------

*   **DO:** make label and description text concise and clear.
*   **DO:** indicate if a field is required.
*   **DO:** include clear validation error messages so that users know how to fix errors.
*   **DO:** include placeholder text to help users understand what's expected in the field.
*   **DO:** indicate if there is a character limit.
*   **DON'T:** use this field for short values, such as names, numbers, and dates.
*   **DON'T:** use placeholder text for critical information, as it will disappear once users begin to type. Critical information should be placed in the label and descriptive text, with additional context in the tooltip if needed.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/textarea#related-components)
------------------------------------------------------------------------------------------------------------

*   [Text](https://developers.hubspot.com/docs/platform/ui-components/text)
*   [Select](https://developers.hubspot.com/docs/platform/ui-components/select)
*   [Form](https://developers.hubspot.com/docs/platform/ui-components/form)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/textarea#page-feedback)
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
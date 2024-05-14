Select | UI components (BETA)
=============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Select` component renders a dropdown menu select field where a user can select a single value. A search bar will be automatically included when there are more than seven options.

![design-guidelines-select-input](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-select-input.png)

1.  **Label:** the label that describes the field's purpose.
2.  **Value:** the field's selected value.

import { Select } from '@hubspot/ui-extensions'; const Extension = () => { const \[name, setName\] = useState(null); const \[validationMessage, setValidationMessage\] = useState(''); const \[isValid, setIsValid\] = useState(true); const options = \[ { label: 'Bill', value: 42 }, { label: 'Ted', value: 43 }, \]; return ( <Form> <Select label="Best Bill & Ted Character?" name="best-char" tooltip="Please choose" description="Please choose" placeholder="Bill or Ted?" required={true} error={!isValid} validationMessage={validationMessage} onChange={value => { setName(value); if (!value) { setValidationMessage('This is required'); setIsValid(false); } else { setValidationMessage('Excellent!'); setIsValid(true); } }} options={options} /> </Form> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `name` | String | The input's unique identifier. |
| `label` | String | The text that displays above the input. |
| `options` Required | Array | The options to display in the dropdown menu. `label` will be used as the display text, and `value` should be the option's unique identifier, which is submitted with the form. |
| `value` | String | number | boolean | The value of the input. |
| `variant` | `input` (default) | `transparent` | The visual style of the button |
| `required` | Boolean | When set to `true`, displays a required field indicator. Default is `false`. |
| `readOnly` | Boolean | When set to `true`, users will not be able to fill the input field. Default is `false`. |
| `tooltip` | String | The text that displays in a tooltip next to the label. |
| `description` | String | Text that describes the field's purpose. |
| `error` | Boolean | When set to `true`, `validationMessage` is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left `false` (default), `validationMessage` is displayed as a success message. |
| `validationMessage` | String | The text to display if the input has an error. |
| `onChange` | (value: string) => void | A callback function that is invoked when the value is committed. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/select#variants)
--------------------------------------------------------------------------------------

Using the variant prop, you can set the input to be one of two styles:

*   `input` (default): a standard dropdown menu.  
    ![ui-extension-components-input-selelect-input-variant](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-input-selelect-input-variant.png?width=537&height=273&name=ui-extension-components-input-selelect-input-variant.png)
*   `transparent`: a hyperlink dropdown menu.  
    ![ui-extension-components-input-selelect-transparent-variant](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-input-selelect-transparent-variant.png?width=286&height=271&name=ui-extension-components-input-selelect-transparent-variant.png) 

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/select#usage-examples)
--------------------------------------------------------------------------------------------------

Use this type of field when there are a range of set options to choose from, such as:

*   A list of products that can be purchased.
*   A list of office locations to ship to.
*   A list of delivery options for a vendor.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/select#guidelines)
------------------------------------------------------------------------------------------

*   **DO:** make label and description text concise and clear.
*   **DO:** indicate if a field is required.
*   **DO:** include clear validation error messages so that users know how to fix errors.
*   **DO:** include placeholder text to help users understand what's expected in the field.
*   **DON'T:** use this component when you want users to be able to select multiple options. For multiple options, use the [MultiSelect component](/docs/platform/ui-components/multiselect).
*   **DON'T:** use placeholder text for critical information, as it will disappear once users begin to type. Critical information should be placed in the label and descriptive text, with additional context in the tooltip if needed.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/select#related-components)
----------------------------------------------------------------------------------------------------------

*   [Form](https://developers.hubspot.com/docs/platform/ui-components/form)
*   [Text](https://developers.hubspot.com/docs/platform/ui-components/text)
*   [TextArea](https://developers.hubspot.com/docs/platform/ui-components/textarea)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/select#page-feedback)
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
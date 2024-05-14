MultiSelect | UI components (BETA)
==================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `MultiSelect` component renders a dropdown menu select field where a user can select multiple values. Commonly used within the [Form](/docs/platform/ui-components/form) component. 

![ui-extensions-component-multiselect](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-component-multiselect.png?width=525&height=339&name=ui-extensions-component-multiselect.png)

import { Form, MultiSelect, Button } from '@hubspot/ui-extensions'; function MultiSelectControlledExample() { const \[formValue, setFormValue\] = useState(\[\]); return ( <Form preventDefault={true} onSubmit={() => console.log(formValue, 'hola')}> <MultiSelect value={formValue} placeholder="Pick your Products" label="Select Mutiple Products" name="selectProduct" required={true} onChange={(value) => setFormValue(value)} options={\[ { label: 'Amazing Product 1', value: 'p1' }, { label: 'Amazing Product 2', value: 'p2' }, { label: 'Amazing Product 3', value: 'p3' }, { label: 'Amazing Product 4', value: 'p4' }, { label: 'Amazing Product 5', value: 'p5' }, { label: 'Amazing Product 6', value: 'p6' }, \]} /> <Button type="submit">Submit</Button> </Form> ); }

| Prop | Type | Description |
| --- | --- | --- |
| `name` Required | String | The input's unique identifier. |
| `label` Required | String | The text that displays above the dropdown menu. |
| `options` Required | Array | The options to display in the dropdown menu. `label` will be used as the display text, and `value` should be the option's unique identifier, which is submitted with the form. |
| `value` | String | number | The value of the input. |
| `required` | Boolean | When set to `true`, displays a required field indicator. |
| `tooltip` | String | The text that displays in a tooltip next to the label. |
| `description` | String | Text that describes the field's purpose. |
| `error` | Boolean | When set to `true`, `validationMessage` is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left `false` (default), `validationMessage` is displayed as a success message.  
  
 |
| `validationMessage` | String | The text to display if the input has an error. |
| `onChange` | (value: (string | number)\[\]) => void | A callback function that is invoked when the value is committed. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/multiselect#related-components)
---------------------------------------------------------------------------------------------------------------

*   [Form](https://developers.hubspot.com/docs/platform/ui-components/form)
*   [DateInput](https://developers.hubspot.com/docs/platform/ui-components/dateinput)
*   [NumberInput](https://developers.hubspot.com/docs/platform/ui-components/numberinput)
*   [Select](/docs/platform/ui-components/select)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/multiselect#page-feedback)
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
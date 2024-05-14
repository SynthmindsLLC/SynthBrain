ToggleGroup | UI extension components (BETA)
============================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `ToggleGroup` component renders a list of selectable options, either in radio button or checkbox form.

![design-guide-toggle-group](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-toggle-group.png?width=400&height=293&name=design-guide-toggle-group.png)

1.  **Group label:** the text that displays above the group of checkboxes.
2.  **Tooltip:** on hover, displays additional information about the field.
3.  **Unchecked checkbox:** an unselected checkbox.
4.  **Option label:** the text that displays next to the checkbox.
5.  **Option description:** the text that displays below the option label to describe the option.

import { ToggleGroup } from '@hubspot/ui-extensions'; const options = \[1, 2, 3, 4\].map(n => ({ label: \`Option ${n}\`, value: \`${n}\`, initialIsChecked: n === 2, readonly: false, description: \`This is option ${n}\`, })); const Extension = () => { return ( <ToggleGroup name="toggle-checkboxes" label="Toggle these things" error={false} options={options} tooltip="Here's a secret tip." validationMessage="Make sure you do the thing correctly." required={false} inline={false} toggleType="checkboxList" variant="default" /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `name` Required | String | The input's unique identifier. |
| `label` Required | String | The text that displays above the toggles. |
| `options` Required | Array | An array of options to display in the group. Each object in the array contains:
*   `label` (string)
*   `value` (string)
*   `initialIsChecked` (boolean)
*   `readonly` (boolean)
*   `description` (string)

 |
| `toggleType` Required | `'radioButtonList'`| `'checkboxList'` | The type of toggle, whether checkboxes or radio buttons. Radio buttons only allow one option to be selected. |
| `variant` | `'default'` (default) | `'small'` | The size of the toggle. |
| `error` | Boolean | When set to true, `validationMessage` is displayed as an error message if provided. The input will also render its error state to let the user know there is an error. If left `false`, `validationMessage` is displayed as a success message. |
| `value` | String | The value of the toggle group.

*   Accepts a string when `toggleType` is `radioButtonList`.
*   Accepts an array when `toggleType` is `checkboxList`.

 |
| `required` | Boolean | When set to `true`, displays a required indicator next to the toggle group. Default is `false`. |
| `tooltip` | String | Text that will appear in a tooltip next to the toggle group label. |
| `validationMessage` | String | The text to display if the input has an error. |
| `inline` | Boolean | When set to `true`, stacks the options horizontally. Default is `false`. |
| `readonly` | Boolean | When set to `true`, users will not be able to select the toggle. Default is `false`. |
| `onChange` | (checked: boolean) => void | A function that is invoked when the toggle is clicked. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/togglegroup#variants)
-------------------------------------------------------------------------------------------

By default, the toggle group will render as a vertical list of checkboxes. Using the `toggleType` prop, you can set the options to display as checkboxes or radio buttons. You can also use the `inline` prop to stack options horizontally.

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; border: 0px; height: 714.016px;"><tbody><tr style="height: 220.672px;"><td style="border: 0px; width: 99.8927%; height: 220.672px;"><p><img src="https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_3.png" loading="lazy" alt="toggle-group-checklist-variant"></p></td></tr><tr style="height: 52px;"><td style="border: 0px; width: 99.8927%; text-align: center; height: 52px;"><code>toggleType='checkboxList'</code> (default)</td></tr><tr style="height: 206.672px;"><td style="border: 0px; width: 99.8927%; height: 206.672px;"><p><br><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_4.png?width=273&amp;height=164&amp;name=design-guidelines-togglegroup-styles_4.png" width="273" height="164" loading="lazy" alt="toggle-group-radio-buttons" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_4.png?width=137&amp;height=82&amp;name=design-guidelines-togglegroup-styles_4.png 137w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_4.png?width=273&amp;height=164&amp;name=design-guidelines-togglegroup-styles_4.png 273w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_4.png?width=410&amp;height=246&amp;name=design-guidelines-togglegroup-styles_4.png 410w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_4.png?width=546&amp;height=328&amp;name=design-guidelines-togglegroup-styles_4.png 546w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_4.png?width=683&amp;height=410&amp;name=design-guidelines-togglegroup-styles_4.png 683w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_4.png?width=819&amp;height=492&amp;name=design-guidelines-togglegroup-styles_4.png 819w" sizes="(max-width: 273px) 100vw, 273px"></p></td></tr><tr style="height: 52px;"><td style="border: 0px; width: 99.8927%; text-align: center; height: 52px;"><code>toggleType='radioButtonList'</code></td></tr><tr style="height: 147.672px;"><td style="border: 0px; width: 99.8927%; height: 147.672px;"><p><br><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_1.png?width=443&amp;height=105&amp;name=design-guidelines-togglegroup-styles_1.png" width="443" height="105" loading="lazy" alt="toggle-group-inline" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_1.png?width=222&amp;height=53&amp;name=design-guidelines-togglegroup-styles_1.png 222w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_1.png?width=443&amp;height=105&amp;name=design-guidelines-togglegroup-styles_1.png 443w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_1.png?width=665&amp;height=158&amp;name=design-guidelines-togglegroup-styles_1.png 665w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_1.png?width=886&amp;height=210&amp;name=design-guidelines-togglegroup-styles_1.png 886w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_1.png?width=1108&amp;height=263&amp;name=design-guidelines-togglegroup-styles_1.png 1108w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_1.png?width=1329&amp;height=315&amp;name=design-guidelines-togglegroup-styles_1.png 1329w" sizes="(max-width: 443px) 100vw, 443px"></p></td></tr><tr style="height: 35px;"><td style="border: 0px; width: 99.8927%; text-align: center; height: 35px;"><code>inline={true}</code></td></tr></tbody></table>

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/togglegroup#usage-examples)
-------------------------------------------------------------------------------------------------------

*   A radio button list to enable salespeople to select one of four sales packages for a new customer.
*   A checkbox list to enable customer support reps to select several options of swag to send to a delightful customer.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/togglegroup#guidelines)
-----------------------------------------------------------------------------------------------

*   **DO:** use this component when the user has a small selection of items to choose from. For longer lists of options, consider using the [Select component](/docs/platform/ui-components/select) instead.
*   **DO:** keep label options concise when possible.
*   **DON'T:** use toggle groups to display long lists of options.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/togglegroup#related-components)
---------------------------------------------------------------------------------------------------------------

*   [Checkbox](https://developers.hubspot.com/docs/platform/ui-components/checkbox)
*   [RadioButton](https://developers.hubspot.com/docs/platform/ui-components/radiobutton)
*   [Toggle](https://developers.hubspot.com/docs/platform/ui-components/toggle)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/togglegroup#page-feedback)
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
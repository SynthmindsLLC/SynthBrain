---
Please provide me with the context or specifics of the mission you'd like me to write about.  For example, tell me: "* **What kind of mission is it?** Is it a personal mission statement, a mission for a company, a mission for a team, a mission for a project, or something else? "
* **What is the overall goal or purpose of the mission?**  What are you trying to achieve?
* **Who are the stakeholders involved?**  Who will benefit from the mission's success?
* **What are some key values or principles that should guide the mission?**  What are the ethical considerations?

Once I have this information, I can help you craft a compelling and impactful mission statement.
---

Checkbox | UI components (BETA)
===============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Checkbox` component renders single checkbox input. If you want to display multiple checkboxes, you should use [ToggleGroup](/docs/platform/ui-components/togglegroup) instead, as it comes with extra logic for handling multiple checkboxes and radio buttons.

![ui-extensions-component-checkbox](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-component-checkbox.png?width=300&height=93&name=ui-extensions-component-checkbox.png)

import { Checkbox } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Checkbox checked={isSuperAdmin} name="adminCheck" description="Select to grant superpowers" > Super Admin </Checkbox> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `value` |  String | The checkbox value. This value is not displayed on the card, but is passed on the server side when submitted, along with the checkbox name. |
| `name` |  String | The checkbox's unique identifier. |
| `checked` |  Boolean | When set to `true`, the checkbox is selected. Default is `false`. |
| `initialIsChecked` |  Boolean | When set to `true`, the checkbox is selected by default. Default is `false`. |
| `readOnly` | Boolean | When set to `true`, the checkbox cannot be selected. |
| `description` | String | Text that describes the field's purpose. |
| `aria-label` | String | The checkbox's accessibility label. |
| `variant` | `'sm'`, `'small'` | `'default'` | The size of the checkbox |
| `inline` | Boolean | When set to `true`, arranges checkboxes side by side. Default is `false`.  
  
 |
| `onChange` | (checked: boolean, value: string) => void; | A callback function that is called when the checkbox is selected or cleared. Passes the new value. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/checkbox#related-components)
------------------------------------------------------------------------------------------------------------

*   [RadioButton](https://developers.hubspot.com/docs/platform/ui-components/radiobutton)
*   [ToggleGroup](https://developers.hubspot.com/docs/platform/ui-components/togglegroup)
*   [TextArea](https://developers.hubspot.com/docs/platform/ui-components/textarea)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/checkbox#page-feedback)
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
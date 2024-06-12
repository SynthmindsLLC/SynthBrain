---
Please provide me with more information! I need to know what the mission is about.  

For example, tell me: "* **What is the context of the mission?**  Is it a personal mission, a business mission, a mission for a school project, etc.? "
* **What is the goal of the mission?**  What are you trying to achieve?
* **What are the specific objectives of the mission?**  What steps need to be taken to reach the goal?

Once you give me more information, I can help you craft a compelling and impactful mission statement.
---

Toggle | UI components (BETA)
=============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Toggle` component renders a boolean toggle switch that can be configured with sizing, label position, read-only, and more.

![toggle-example](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/toggle-example.png?width=160&height=99&name=toggle-example.png)

import { Toggle } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Toggle size="md" label="My toggle" labelDisplay="top" initialIsChecked={true} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `name` Required | String | The input's unique identifier. |
| `label` Required | String | The text that displays above the input. |
| `size` | `'xs'`, `'extra-small'` | `'sm'`, `'small'` | `'md'`, `'medium'` (default) | The size of the toggle. Only `'md'` / `'medium'` sized toggles can display text on the toggle (ON, OFF). All other sizes will hide checked/unchecked text. |
| `labelDisplay` | `'inline'` (default) | `'top'` | `'hidden'` | The display option for the toggle label. |
| `checked` | Boolean | Whether the toggle is selected. Default is `false`. |
| `initialIsChecked` | Boolean | When set to `true`, the toggle will be selected by default. Sets the default `checked` state when the component is uncontrolled. |
| `textChecked` | String | The text that displays on the toggle when checked. Default is ON. Extra small and small toggles will not display any text. |
| `textUnchecked` | String | The text that displays on the toggle when not checked. Default is _OFF_. Extra small and small toggles will not display any text.  
  
 |
| `readonly` | Boolean | When set to `true`, users will not be able to select the toggle. Default is `false`. |
| `onChange` | (checked: boolean) => void | A function that is invoked when the toggle is clicked. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/toggle#variants)
--------------------------------------------------------------------------------------

Using the `labelDisplay` and `size` props, you can customize toggle appearance.

*   `labelDisplay`:  set to `'inline'` or `'top'` to configure the label position, or set to `'hidden'` to hide the label.  
    ![toggledisplay-examples](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/toggledisplay-examples.png?width=413&height=114&name=toggledisplay-examples.png)
*   `size`: by default, toggles are set to `'medium'`. Shrink the toggle size by setting this prop to `'xs'`/`'extra-small'` or `'sm'`/`'small'`. Note that only medium toggles will display ON/OFF status text.  
    ![toggle-size-exaples](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/toggle-size-exaples.png?width=497&height=99&name=toggle-size-exaples.png)

Related components[](https://developers.hubspot.com/docs/platform/ui-components/toggle#related-components)
----------------------------------------------------------------------------------------------------------

*   [Tag](https://developers.hubspot.com/docs/platform/ui-components/tag)
*   [ToggleGroup](https://developers.hubspot.com/docs/platform/ui-components/togglegroup)
*   [ProgressBar](https://developers.hubspot.com/docs/platform/ui-components/progressbar)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/toggle#page-feedback)
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
---
Please provide me with the rest of the mission statement! I need more information to help you complete it. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a team, an organization, a personal goal?"
* **What are the key values or goals?** What do you want to achieve? What are the main principles that guide your actions? 
* **Who is the target audience?** Who will benefit from this mission? 

Once I have this information, I can help you craft a compelling and effective mission statement.
---

Tag | UI components (BETA)
==========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Tag` component renders a tag to label or categorize information or other components. Tags can be static or clickable for invoking functions.

![design-guidelines-tag](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-tag.png?width=290&height=128&name=design-guidelines-tag.png)

1.  **Variant:** the color of the tag.
2.  **Tag text:** the text that communicates the tag's purpose.

import { Tag } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Tag variant='success' onClick={() => { console.log('Tag clicked!'); }} > Success </Tag> ); }

| Prop | Type | Description |
| --- | --- | --- |
| `variant` | `'default'` (default) | `'warning'` | `'success'` | `'error'` | The color of the alert. See the [variants section](#variants) for more information. |
| `onClick` | `() => void` | A function that will be invoked when the tag is clicked. The function receives no arguments and its return value is ignored. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/tag#variants)
-----------------------------------------------------------------------------------

Using the `variant` prop, you can choose from one of four tag colors:

*   `default` (default): for general tagging and labeling.  
    ![design-guidelines-tags_1](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-tags_1.png?width=125&height=51&name=design-guidelines-tags_1.png)
*   `success`: for indicating or confirming the success of an action.  
    ![design-guidelines-tags_2](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-tags_2.png?width=111&height=50&name=design-guidelines-tags_2.png)
*   `warning`: for indicating something that might be time-sensitive or of importance.  
    ![design-guidelines-tags_3](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-tags_3.png?width=111&height=44&name=design-guidelines-tags_3.png)
*   `error`: for indicating error or failure.  
    ![design-guidelines-tags_4](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-tags_4.png?width=101&height=52&name=design-guidelines-tags_4.png)

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/tag#usage-examples)
-----------------------------------------------------------------------------------------------

*   Use a default tag to indicate that a customer is active
*   Use a success tag to indicate that an item in a to-do list has been completed.
*   Use a warning tag to indicate that a deal is expiring soon.
*   Use an error tag to indicate that an error happened when trying to sync a specific property in a table.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/tag#guidelines)
---------------------------------------------------------------------------------------

*   **DO:** make tag text concise and clear.
*   **DO:** ensure that tag variants are used consistently across the extension.
*   **DON'T:** use tags in place of buttons or links.
*   **DON'T:** rely on color alone to communicate the tag's meaning. Ensure that tag text is clear and helpful.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/tag#related-components)
-------------------------------------------------------------------------------------------------------

*   [Toggle](https://developers.hubspot.com/docs/platform/ui-components/toggle)
*   [Alert](https://developers.hubspot.com/docs/platform/ui-components/alert)
*   [ProgressBar](https://developers.hubspot.com/docs/platform/ui-components/progressbar)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/tag#page-feedback)
---------------------------------------------------------------------------------------------------

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
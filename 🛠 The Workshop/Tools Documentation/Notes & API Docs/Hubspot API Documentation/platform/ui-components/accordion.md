---
Please provide me with more information so I can help you write a compelling mission statement. 

Tell me: "* **What is the purpose of this mission statement?** Is it for a company, a project, a personal goal, or something else?"
* **What are the key values, goals, and aspirations of the entity or project?** 
* **Who is the target audience for this mission statement?** 
* **What kind of tone and style are you looking for?** (formal, informal, inspiring, etc.)

Once I have this information, I can help you craft a powerful and effective mission statement.
---

Accordion | UI components (BETA)
================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Accordion` component renders an expandable and collapsable section that can contain other components. This component can be helpful for saving space and breaking up extension content.

![ui-extensions-accordion-section](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extensions-accordion-section.png?width=546&height=212&name=ui-extensions-accordion-section.png)

import { Accordion, Text } from '@hubspot/ui-extensions'; const Extension = () => { return ( <> <Accordion title="Item One" defaultOpen={true}> <Text>Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.</Text> </Accordion> <Accordion title="Item Two"> <Text>Second inner text</Text> </Accordion> </> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `title` Required | String | The accordion's title text. |
| `defaultOpen` | Boolean | When set to `true`, the accordion will be open on initial page load. The `open` prop takes precedence over this prop. |
| `disabled` | Boolean | When set to `true`, the accordion's state cannot be changed. Set to `false` by default. |
| `open` | Boolean | Controls the accordion's open state programmatically. When set to `true`, the accordion will open. Takes precedence over `defaultOpen`. |
| `onClick` | `() => void` | A function that will be invoked with the accordion title is clicked. This function receives no arguments and its returned value is ignored. |
| `size` | `'xs'`, `'extra-small'` | `'sm'`, `'small'` | `'med'`, `'medium'` (default) | The size of the accordion title. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/accordion#related-components)
-------------------------------------------------------------------------------------------------------------

*   [Box](https://developers.hubspot.com/docs/platform/ui-components/box)
*   [Divider](https://developers.hubspot.com/docs/platform/ui-components/divider)
*   [Heading](https://developers.hubspot.com/docs/platform/ui-components/heading)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/accordion#page-feedback)
---------------------------------------------------------------------------------------------------------

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
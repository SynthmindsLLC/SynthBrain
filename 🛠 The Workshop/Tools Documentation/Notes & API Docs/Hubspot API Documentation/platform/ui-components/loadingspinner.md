---
Please provide me with the context or details of the mission you want to describe. I need more information to help you write a compelling mission statement. 

For example, tell me: "* **What is the purpose of the mission?** (e.g., a business, a project, a personal goal)"
* **What are the key objectives?** (e.g., increase profits, solve a problem, achieve a certain outcome)
* **Who is the target audience?** (e.g., customers, employees, stakeholders)
* **What are the values or guiding principles?** (e.g., innovation, sustainability, customer focus)

Once you provide me with more context, I can help you craft a clear, concise, and impactful mission statement.
---

LoadingSpinner | UI components (BETA)
=====================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `LoadingSpinner` component renders a visual indicator for when an extension is loading or processing data.

![design-guidelines-loading-spinners](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-loading-spinners.png?width=800&name=design-guidelines-loading-spinners.png)

1.  **Label:** the text that describes the loading state.
2.  **Size:** the size of the component. From left to right: extra small (`'xs'`), small (`'sm'`, default), medium (`'md'`).
3.  **Layout:** the positioning of the spinner. From left to right: `inline`, `centered`.

import { LoadingSpinner } from '@hubspot/ui-extensions'; const Extension = () => { return ( <LoadingSpinner label="Loading..." /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `label` Required | String | The text that displays next to the spinner. |
| `showLabel` | Boolean | When set to `true`, the `label` will appear next to the spinner. Default is `false`. |
| `size` | `'xs'`, `'extra-small'` | `'sm'`, `'small'` (default) | `'md'`, `'medium'` | The size of the spinner. |
| `layout` | `'inline'` (default) | `'centered'` | The position of the spinner |

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/loadingspinner#usage-examples)
----------------------------------------------------------------------------------------------------------

*   A loading state after the user submits form data to an external system (e.g., "Submitting contact details").
*   A loading state as the card retrieves customer purchase history from an external system (e.g., "Loading purchase history").

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/loadingspinner#guidelines)
--------------------------------------------------------------------------------------------------

*   **DO:** keep label text as concise as possible.
*   **DO:** use label text to describe what's happening during the loading process.
*   **DO:** use complete sentences in label text.
*   **DON'T:** include multiple loading spinners at once in a single card to avoid confusion.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/loadingspinner#related-components)
------------------------------------------------------------------------------------------------------------------

*   [Alert](https://developers.hubspot.com/docs/platform/ui-components/alert)
*   [EmptyState](https://developers.hubspot.com/docs/platform/ui-components/emptystate)
*   [ErrorState](https://developers.hubspot.com/docs/platform/ui-components/errorstate)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/loadingspinner#page-feedback)
--------------------------------------------------------------------------------------------------------------

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
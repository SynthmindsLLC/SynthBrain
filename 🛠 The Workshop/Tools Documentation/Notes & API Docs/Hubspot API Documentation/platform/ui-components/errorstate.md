---
Please provide me with more information about the mission you want to describe! I need more context to help you write a compelling mission statement. 

For example, tell me: "* **What is the mission about?** What are you trying to accomplish? "
* **Who is this mission for?** What is the target audience?
* **What are the main goals of the mission?** What are you hoping to achieve? 
* **What are the values that underpin this mission?** What principles guide your actions?

The more information you give me, the better I can help you craft a clear, concise, and impactful mission statement.
---

ErrorState | UI components (BETA)
=================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `ErrorState` component sets the content of an erroring extension. Use this component to guide users through resolving errors that your extension might encounter.

![design-guidelines-error-state-primary-button](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guidelines-error-state-primary-button.png?width=503&height=381&name=design-guidelines-error-state-primary-button.png)

1.  **Illustration:** one of three error-themed illustrations.
2.  **Title:** the main error message to explain the root cause if known.
3.  **Additional text:** an additional [`Text` component](/docs/platform/ui-components/text) to provide further guidance. This does not come with the component by default. Error text should use the following formats:
    *   **Known cause:** \[what failed\] + \[why it failed\] + \[next steps\]. For example, _Failed to load extension due to outage, please wait a few minutes and try again._
    *   **Unknown cause:** \[what failed\] + \[next steps\]. For example, _Couldn't load data, try refreshing the page or contacting IT._
4.  **Additional button:** an additional [`Button` component](/docs/platform/ui-components/button) to can help users take action. This does not come with the component by default.

import { ErrorState, Text, Button } from '@hubspot/ui-extensions'; const Extension = ({ data, error, fetchData }) => { if (error) { return ( <ErrorState title="Trouble fetching properties."> <Text> Please try again in a few moments. </Text> <Button onClick={fetchData}> Try again </Button> </ErrorState> ) } return ( {data.map(...)} ); }

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `title` |  String | The text of the component header. |
| `type` |  `'support'` | `'lock'` | `'error'` (default) | The type of image that will be displayed. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/errorstate#variants)
------------------------------------------------------------------------------------------

Using the `type` prop, you can set one of three illustrations.

![design-guidelines-error-states_3](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-error-states_3.png?width=512&name=design-guidelines-error-states_3.png)

const Extension = ({ data, error, fetchData }) => { if (error) { return ( <ErrorState title="Trouble fetching properties." type="error" > </ErrorState> ) } return ( {data.map(...)} ); }

![design-guidelines-error-states_1](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-error-states_1.png?width=512&name=design-guidelines-error-states_1.png)

const Extension = ({ data, error, fetchData }) => { if (error) { return ( <ErrorState title="Something went wrong." type="support" > </ErrorState> ) } return ( {data.map(...)} ); }

![design-guidelines-lock](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-lock.png?width=449&name=design-guidelines-lock.png)

const Extension = ({ data, error, fetchData }) => { if (error) { return ( <ErrorState title="You must log in to view this data." type="lock" > </ErrorState> ) } return ( {data.map(...)} ); }

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/errorstate#usage-examples)
------------------------------------------------------------------------------------------------------

*   Use the `default` error type when a card encounters an error when fetching data.
*   Use the `support` error type when the user should contact internal or external support to resolve an error.
*   Use the `lock` error type when the user needs to log in or doesn't have permission to access the card's data.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/errorstate#guidelines)
----------------------------------------------------------------------------------------------

*   **DO:** use text that's clear, direct, brief, and helpful.
*   **DON'T:** use technical jargon.
*   **DON'T:** say "sorry" or use frivolous language such as "oops," "uh-oh," and "it's us, not you."
*   **DON'T:** use exclamation points.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/errorstate#related-components)
--------------------------------------------------------------------------------------------------------------

*   [Alert](https://developers.hubspot.com/docs/platform/ui-components/alert)
*   [EmptyState](https://developers.hubspot.com/docs/platform/ui-components/emptystate)
*   [LoadingSpinner](https://developers.hubspot.com/docs/platform/ui-components/loadingspinner)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/errorstate#page-feedback)
----------------------------------------------------------------------------------------------------------

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
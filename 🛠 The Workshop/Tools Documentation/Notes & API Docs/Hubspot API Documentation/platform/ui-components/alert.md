---
Please provide me with more information! To help you write a compelling mission statement, I need to know: "**1. What is the purpose of your mission?**"
-Are you writing a mission statement for a company, organization, project, or something else?

**2. What are your goals and objectives?**
-What do you want to achieve? What problem are you trying to solve?

**3. What are your values?**
-What principles will guide your actions?

**4. What is your target audience?**
-Who are you trying to reach with your mission?

Once you provide me with these details, I can help you write a concise, impactful mission statement.
---

Alert | UI components (BETA)
============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

Use the `Alert` component to render an alert within a card. Use this component to give usage guidance, notify users of action results, or warn them about potential issues or failures. Alerts can be placed in components statically or triggered dynamically as the result of an action.  
  
If you want to render an alert banner at the top of the page, check out the guidance covering the `addAlert` method [here](/docs/platform/ui-extensions-sdk#display-alert-banners). 

![updated-alert-component-design-guidelines-diagram](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/updated-alert-component-design-guidelines-diagram.png?width=698&height=200&name=updated-alert-component-design-guidelines-diagram.png)

1.  **Title:** the alert's bolded title text which should summarize its intent or an action outcome.
2.  **Body:** the descriptive text that follows the title, which should provide the user with the necessary information to proceed.
3.  **Variant:** the color of the alert. Learn more about when to use each variant below.

import { Alert } from '@hubspot/ui-extensions'; const Extension = () => { return ( <> <Alert title="Important Info" variant="info"> This is an informative message. </Alert> <Alert title="Success"variant="success"> Operation completed successfully. </Alert> <Alert title="Warning" variant="warning" > Proceed with caution. </Alert> <Alert title="Danger" variant="danger" > This action cannot be undone. Be careful. </Alert> </> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `title`  Required | String | The bolded text of the alert. |
| `variant` | `'info'` (default) | `'success'` | `'warning'` | `'danger'` | The color of the alert. See below for more information about variants. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/alert#variants)
-------------------------------------------------------------------------------------

There are four alert types, which can be set using the `variant` prop: 

*   `info`**:** a blue alert for general tips and messages that guide the user through a specific task.  
    ![ui-extension-component-alert-info](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extension-component-alert-info.png?width=540&height=53&name=ui-extension-component-alert-info.png)

*   `success`**:** a green alert to indicate the successful completion of a task or to convey a positive CRM record status.  
    ![ui-extension-component-alert-success](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extension-component-alert-success.png?width=540&height=48&name=ui-extension-component-alert-success.png)

`warning`**:** a yellow alert for general warnings related to the performance of the system or the status of the CRM record.  
![ui-extension-component-alert-warning](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extension-component-alert-warning.png?width=540&height=58&name=ui-extension-component-alert-warning.png)

*   `error` and `danger`**:** a red alert indicating an error, the degradation of a system, or a negative CRM record status. You should not use this alert type for anything other than errors and negative statuses.  
    ![danger-alert-component-updated](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/danger-alert-component-updated.png?width=535&height=46&name=danger-alert-component-updated.png) 

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/alert#usage-examples)
-------------------------------------------------------------------------------------------------

*   Use an `info` alert to add instructions to a custom card, such as "Fill out this form using the contact's company information."
*   Use a `success` alert when a user successfully submits a form in the UI extension, or to convey that a contact qualifies for enrollment in a promotional offering.
*   Use a `warning` alert to call attention to a contact's upcoming renewal date.
*   Use a `danger` alert to notify the user of a form submission error or to signify that a high-urgency ticket has lapsed.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/alert#guidelines)
-----------------------------------------------------------------------------------------

*   **DO:** use alert text that clearly communicates to the user what they need to know.
*   **DO:** make alert text actionable, especially for error alerts which should provide a clear path to resolution.
*   **DO:** use proper punctuation, such as periods and question marks at the end of the descriptive text.
*   **DO:** set the alert as the first component in the extension when possible for visibility. Extensions with alerts should also be placed at the top of the CRM record by a HubSpot admin. Learn more about [customizing CRM record tabs](https://knowledge.hubspot.com/crm-setup/view-and-customize-record-overviews).
*   **DON'T:** use exclamation points in warning or error alerts. Exclamation points should only be used for short, positive messages (e.g. "Great!" or "Well done!").

Related components[](https://developers.hubspot.com/docs/platform/ui-components/alert#related-components)
---------------------------------------------------------------------------------------------------------

*   [Display alert banners outside of a card](/docs/platform/ui-extensions-sdk#display-alert-banners)
*   [EmptyState](https://developers.hubspot.com/docs/platform/ui-components/emptystate)
    
*   [ErrorState](https://developers.hubspot.com/docs/platform/ui-components/errorstate)
    
*   [LoadingSpinner](https://developers.hubspot.com/docs/platform/ui-components/loadingspinner)
    

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/alert#page-feedback)
-----------------------------------------------------------------------------------------------------

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
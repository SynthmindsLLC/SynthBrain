Form | UI components (BETA)
===========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Form` component renders a form that can contain other subcomponents, such as [Input](/docs/platform/ui-components/input), [Select](/docs/platform/ui-components/select), and [Button](/docs/platform/ui-components/button). Use this component to enable users to submit data to HubSpot or an external system.

![design-guide-form-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guide-form-component.png?width=600&height=383&name=design-guide-form-component.png)

1.  **Label:** the input label.
2.  **Text input:** an [Input](https://developers.hubspot.com/docs/platform/ui-components/input) component with a placeholder value of First name.
3.  **Label:** the select input label.
4.  **Select input:** a [Select](https://developers.hubspot.com/docs/platform/ui-components/select) component with value of Customer.
5.  **Button:** a [Button](https://developers.hubspot.com/docs/platform/ui-components/button) component to submit the form's information. 

import { Form, Input, Button } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Form onSubmit={() => { console.log('Form submitted!')}} preventDefault={true}> <Input label="First Name" name="first-name" tooltip="Please enter your first name" description="Please enter your first name" placeholder="First name" /> <Input label="Last Name" name="last-name" tooltip="Please enter your last name" description="Please enter your last name" placeholder="Last name" /> <Button onClick={() => { console.log('Submit button clicked'); }} variant="primary" type="submit" > Submit </Button> </Form> ); }

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `onSubmit` | Function | The function that is called when the form is submitted. It will receive a `RemoteEvent` as an argument and its return value will be ignored. |
| `preventDefault` | Boolean | When set to `true`, `event.preventDefault()` will be invoked before the `onSubmit` function is called, preventing the default HTML form behavior. |

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/form#usage-examples)
------------------------------------------------------------------------------------------------

*   A form to submit customer information to an external database.
*   A form to place a product order on behalf of a customer.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/form#guidelines)
----------------------------------------------------------------------------------------

*   **DO:** include text inputs when a user should be able to submit any value.
*   **DO:** include select inputs when a user should only be able to select from a set of values.
*   **DO:** include descriptions and placeholder text to provide context to users.
*   **DO:** always position the submit button at the bottom of the form. 
*   **DON'T:** include a form without a submit button.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/form#related-components)
--------------------------------------------------------------------------------------------------------

*   [Button](/docs/platform/ui-components/button)
*   [DateInput](https://developers.hubspot.com/docs/platform/ui-components/dateinput)
*   [Input](/docs/platform/ui-components/input)
*   [MultiSelect](https://developers.hubspot.com/docs/platform/ui-components/multiselect)
*   [NumberInput](https://developers.hubspot.com/docs/platform/ui-components/numberinput)
*   [Select](/docs/platform/ui-components/select)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/form#page-feedback)
----------------------------------------------------------------------------------------------------

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
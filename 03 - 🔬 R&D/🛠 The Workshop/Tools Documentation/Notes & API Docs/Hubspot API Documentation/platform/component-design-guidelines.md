Component design guidelines (BETA)
==================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

When creating a UI extension, you'll include HubSpot-provided components to render various UI elements for interaction and displaying data. When using these components, you should follow the guidelines below to create a more expected, seamless user experience. These guidelines follow the same principles that HubSpot uses when designing UI elements, which will help your extension feel more like a native functionality.

To view the code and prop definitions for each component, check out the [UI extension components reference guide](/docs/platform/ui-extension-components). Each component below will also contain a link out to its respective code reference.

Below you'll find guidance for the following components:

Standard components

*   [Alerts](#alerts)
*   [Buttons](#buttons)
*   [Button rows](#button-rows)
*   [Description lists](#description-lists)
*   [Dividers](#dividers)
*   [Empty states](#empty-states)
*   [Error states](#error-states)
*   [Forms](#forms)
*   [Headings](#headings)
*   [Images](#images)
*   Inputs:  
    *   [Inputs](#inputs)
    *   [Number inputs](#number-inputs)
    *   [Select inputs](#select-inputs)
    *   [Text area inputs](#text-area-inputs)

*   [Links](#linkd)
*   [Loading spinners](#loading-spinners)
*   [Progress bars](#progress-bars)
*   [Statistics](#statistics)
*   [Tables](#tables)
*   [Tags](#tags)
*   [Text](#text)
*   [Tiles](#tiles)
*   [Toggle groups](#toggle-groups)

Alerts[](https://developers.hubspot.com/docs/platform/component-design-guidelines#alerts)
-----------------------------------------------------------------------------------------

The [`Alert` component](/docs/platform/ui-extension-components#alert) should give usage guidance, notify users of action results, or warn them about potential issues or failures. Alerts can be placed in components statically or triggered dynamically as the result of an action.

![design-guide-alert-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-alert-component.png?width=1031&height=356&name=design-guide-alert-component.png)

1.  Title: the alert's bolded title text which should summarize its intent or an action outcome.
2.  Body: the descriptive text that follows the title, which should provide the user with the necessary information to proceed.
3.  Variant: the color of the alert. Learn more about when to use each variant below.

### Styles

### There are four alert types, which can be set using the `variant` prop: 

*   **Info:** a blue alert for general tips and messages that guide the user through a specific task.  
    ![ui-extension-component-alert-info](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-component-alert-info.png?width=540&height=53&name=ui-extension-component-alert-info.png)
*   **Success:** a green alert to indicate the successful completion of a task or to convey a positive CRM record status.  
    ![ui-extension-component-alert-success](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-component-alert-success.png?width=540&height=48&name=ui-extension-component-alert-success.png)
*   **Warning:** a yellow alert for general warnings related to the performance of the system or the status of the CRM record.  
    ![ui-extension-component-alert-warning](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-component-alert-warning.png?width=540&height=58&name=ui-extension-component-alert-warning.png)
*   **Error/danger:** a red alert indicating an error, the degradation of a system, or a negative CRM record status. You should not use this alert type for anything other than errors and negative statuses.  
    ![ui-extension-component-alert-error-danger](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-component-alert-error-danger.png?width=540&height=117&name=ui-extension-component-alert-error-danger.png)

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Use an info alert to add instructions to a custom card, such as "Fill out this form using the contact's company information."
*   Use a success alert when a user successfully submits a form in the UI extension, or to convey that a contact qualifies for enrollment in a promotional offering.
*   Use a warning alert to call attention to a contact's upcoming renewal date.
*   Use an error or danger alert to notify the user of a form submission error or to signify that a high-urgency ticket has lapsed.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** use alert text that clearly communicates to the user what they need to know.
*   **DO:** make alert text actionable, especially for error alerts which should provide a clear path to resolution.
*   **DO:** use proper punctuation, such as periods and question marks at the end of the descriptive text.
*   **DO:** set the alert as the first component in the extension when possible for visibility. Extensions with alerts should also be placed at the top of the CRM record by a HubSpot admin. Learn more about [customizing CRM record tabs](https://knowledge.hubspot.com/crm-setup/view-and-customize-record-overviews).
*   **DON'T:** use exclamation points in warning or error alerts. Exclamation points should only be used for short, positive messages (e.g. "Great!" or "Well done!").

Buttons[](https://developers.hubspot.com/docs/platform/component-design-guidelines#buttons)
-------------------------------------------------------------------------------------------

The [`Button` component](/docs/platform/ui-extension-components#button) should give users a way to perform actions, such as submitting a form, sending data to an external system, or deleting/disconnecting data related to a CRM record.

![design-guide-button-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-component.png?width=920&height=281&name=design-guide-button-component.png)

1.  Button text: the visible button text that describes the button's action.
2.  Variant: the color of the button. Learn more about when to use each type below.

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

*   **Primary:** a dark blue button for the most frequently used or most important action on an extension. Each extension should only have one primary button.  
    ![design-guide-button-type-primary](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-type-primary.png?width=196&height=65&name=design-guide-button-type-primary.png)
*   **Secondary:** a grey button to provide alternative or non-primary actions. Each extension should include no more than two secondary buttons.  
    ![design-guide-button-type-secondary](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-type-secondary.png?width=205&height=65&name=design-guide-button-type-secondary.png)
*   **Destructive:** a red button for actions that delete, disconnect, or perform any action that the user can't undo. Button text should clearly communicate what is being deleted or disconnected. After a destructive button is clicked, the user should have to verify or confirm the action.  
    ![design-guide-button-type-destructive](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-type-destructive.png?width=211&height=65&name=design-guide-button-type-destructive.png)
*   **Disabled:** a greyed out button that cannot be clicked. This button state is set with the `disabled` prop, not the `variant` prop.  
    ![design-guide-button-type-disabled](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-type-disabled.png?width=194&height=65&name=design-guide-button-type-disabled.png)

**Please note:** HubSpot does not provide variant options for the orange buttons you’ll find across the app (both solid and outlined). Those color variants are reserved for the HubSpot product, which helps to maintain the hierarchy of available actions on a given page.

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Use a primary button at the end of a form to submit data to another system.
*   Use a secondary button next to a primary form submit button to reset form fields.
*   Use a destructive button to enable users to delete a contact's data from an external system.
*   Set a button to disabled when a contact doesn't qualify for a form submission due to missing criteria or other ineligibility.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** set button text that clearly communicates what action will occur when a user clicks it. Text should be unambiguous and concise (~2-4 words).
*   **DO:** use sentence-casing for button text (only the first word capitalized)
*   **DO:** minimize the number of buttons that appear on a page record across all extensions.
*   **DON'T:** include multiple primary buttons in a single extension.
*   **DON'T:** use a destructive button unless the consequences are significant or irreversible.

Button rows[](https://developers.hubspot.com/docs/platform/component-design-guidelines#button-rows)
---------------------------------------------------------------------------------------------------

The [`ButtonRow`](/docs/platform/ui-extension-components#button-row) [component](/docs/platform/ui-extension-components#button-row) renders two or more individual [Button](https://developers.hubspot.com/docs/platform/ui-extension-components?hs_preview=YSMJqMjb-115642861738#button) components in a row. The buttons within the row follow the same guidelines as the [Button component above](#buttons).

![design-guide-button-row-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-row-component.png?width=1327&height=262&name=design-guide-button-row-component.png)

1.  Primary button: only use one per extension.
2.  Secondary button: only use with a primary and/or destructive button.
3.  Destructive button: only use for actions that are destructive, paired with a secondary button.

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   A primary and secondary button in a row to progress through a multi-step form.  
    ![design-guide-button-row-example](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-row-example.png?width=217&height=69&name=design-guide-button-row-example.png)
*   A destructive and secondary button in a row to confirm and cancel a contact deletion.  
    ![design-guide-button-row-example-2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-button-row-example-2.png?width=217&height=50&name=design-guide-button-row-example-2.png)

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** include a secondary button with a destructive button to allow users to cancel the action.
*   **DON'T:** use multiples of the same button type in a row. For example, don't include more than one primary button in one row.
*   **DON'T:** use more than two secondary buttons in a single extension.
*   **DON'T:** use more than three buttons in a row.

Description lists[](https://developers.hubspot.com/docs/platform/component-design-guidelines#description-lists)
---------------------------------------------------------------------------------------------------------------

Use the [`DescriptionList` component](/docs/platform/ui-extension-components#description-list) to display pairs of labels and values in a way that's easy to read at a glance. 

![design-guide-description-list-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-description-list-component.png?width=1238&height=168&name=design-guide-description-list-component.png)

1.  Label: describes the information being displayed.
2.  Value: the information to display.

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

By default, list items will be stacked vertically. You can use the the `direction` prop to stack them horizontally.

*   `row`:  
    ![ui-ext-component-descriptionlist](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-component-descriptionlist.png?width=516&height=68&name=ui-ext-component-descriptionlist.png)
*   `column` (default):  
    ![ui-extension-component-vertical-description-list](https://developers.hubspot.com/hs-fs/hubfs/ui-extension-component-vertical-description-list.png?width=87&height=239&name=ui-extension-component-vertical-description-list.png)

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Display easy to scan information for a sales rep to use on a call.
*   Highlight the most recently updated properties on a company record.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** keep copy succinct, ideally one word each for the label and value.
*   **DO:** use the horizontal orientation for horizontal layouts, and vertical orientation for column layouts.
*   **DON'T:** use this component to display long strings of text.
*   **DON'T:** use this component for lists that you want to be editable in the UI. 

Dividers[](https://developers.hubspot.com/docs/platform/component-design-guidelines#dividers)
---------------------------------------------------------------------------------------------

The [`Divider` component](/docs/platform/ui-extension-components#divider) adds a grey, horizontal line for spacing out components vertically or creating sections in an extension. Use this component to space out other components when the content needs more separation than white space.

![design-guide-divider-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-divider-component.png?width=500&height=156&name=design-guide-divider-component.png)

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

Using the `distance` prop, you can set the amount of padding above and below the divider. Values range from `extra-small` to `extra-large` (`flush` by default).

![design-guide-divider-styles](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-divider-styles.png?width=623&height=177&name=design-guide-divider-styles.png)

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** use dividers to group similar components together.
*   **DO:** consider when a new card or component might be needed, rather than using a divider.
*   **DON'T:** use two dividers in a row without content between them.

Empty states[](https://developers.hubspot.com/docs/platform/component-design-guidelines#empty-states)
-----------------------------------------------------------------------------------------------------

The [`EmptyState` component](/docs/platform/ui-extension-components#empty-state) sets the content that appears when the extension is in an empty state. Use this component when there's no content or data to help guide users.

![design-guidelines-empty-state-primary-button](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-empty-state-primary-button.png?width=455&height=347&name=design-guidelines-empty-state-primary-button.png)

1.  Image: the default image that comes with the component.
2.  **Title:** the title that describes why the component is in an empty state.
3.  **Additional text:** an additional [`Text` component](#text) to provide further guidance. This does not come with the component by default.
4.  **Additional button:** an additional [`Button` component](#buttons) to can help users take action.

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Display when it's the first use of a feature.
*   Show when the user is required to take action in order to populate the card with information.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** make empty states informative so that users understand what will appear when the extension is not empty.
*   **DO:** make empty states actionable. If relevant, explain the benefits of this area and how to add content or data.
*   **DON'T:** make empty states too long.

Error states[](https://developers.hubspot.com/docs/platform/component-design-guidelines#error-states)
-----------------------------------------------------------------------------------------------------

The [`ErrorState` component](/docs/platform/ui-extension-components#error-state) communicates extension errors.

![design-guidelines-error-state-primary-button](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-error-state-primary-button.png?width=503&height=381&name=design-guidelines-error-state-primary-button.png)

1.  Illustration: one of three default error illustrations.
2.  **Title:** the main error message to explain the root cause if known.
3.  **Additional text:** an additional [`Text` component](#text) to provide further guidance. This does not come with the component by default.
4.  **Additional button:** an additional [`Button` component](#buttons) to can help users take action.

### Error message text[](https://developers.hubspot.com/docs/platform/component-design-guidelines#error-message-text)

Include an additional Text component below this component to provide further guidance to users. Error text should use the following formats:  

*   **Known cause:** \[what failed\] + \[why it failed\] + \[next steps\]. For example, _Failed to load extension due to outage, please wait a few minutes and try again._
*   **Unknown cause:** \[what failed\] + \[next steps\]. For example, _Couldn't load data, try refreshing the page or contacting IT._

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

Using the `type` prop, you can set one of three illustrations:

*   `error`:  
    ![design-guidelines-error-states_3](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-error-states_3.png?width=512&height=293&name=design-guidelines-error-states_3.png)
*   `support`:   
    ![design-guidelines-error-states_1](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-error-states_1.png?width=512&height=257&name=design-guidelines-error-states_1.png)
*   `lock`:   
    ![design-guidelines-lock](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-lock.png?width=449&height=289&name=design-guidelines-lock.png) 

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Use the `default` error type when a card encounters an error when fetching data.
*   Use the `support` error type when the user should contact internal or external support to resolve an error.
*   Use the `lock` error type when the user needs to log in or doesn't have permission to access the card's data.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** use text that's clear, direct, brief, and helpful.
*   **DON'T:** use technical jargon.
*   **DON'T:** say "sorry" or use frivolous language such as "oops," "uh-oh," and "it's us, not you."
*   **DON'T:** use exclamation points.

Forms[](https://developers.hubspot.com/docs/platform/component-design-guidelines#forms)
---------------------------------------------------------------------------------------

the [`Form` component](/docs/platform/ui-extension-components#form) renders a submittable form containing other form-related elements, such as inputs and a submit button.

![design-guide-form-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-form-component.png?width=600&height=383&name=design-guide-form-component.png)

1.  Label: the input label.
2.  **Text input:** a [text input](/docs/platform/ui-extension-components#text-input) with a placeholder value of "First name."
3.  **Label:** the select input label.
4.  **Select input:** a [select input](/docs/platform/ui-extension-components#select-input) with value of "Customer."
5.  **Button:** a button to submit the form's information. 

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   A form to submit customer information to an external database.
*   A form to place a product order on behalf of a customer.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** include text inputs when a user should be able to submit any value.
*   **DO:** include select inputs when a user should only be able to select from a set of values.
*   **DO:** include descriptions and placeholder text to provide context to users.
*   **DO:** always position the submit button at the bottom of the form. 
*   **DON'T:** include a form without a submit button.

Headings[](https://developers.hubspot.com/docs/platform/component-design-guidelines#headings)
---------------------------------------------------------------------------------------------

The Heading component renders large text for titles.

![design-guide-heading-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-heading-component.png?width=400&height=140&name=design-guide-heading-component.png)

### Usage example[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-example)

The title at the top of an extension to introduce its content.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** use headers to give users a summary of the information that the extension contains.
*   **DON'T:** use more than one heading for each page or section in the extension.
*   **DON'T:** use headers for paragraphs or long sentences.

Images[](https://developers.hubspot.com/docs/platform/component-design-guidelines#images)
-----------------------------------------------------------------------------------------

The [`Image` component](/docs/platform/ui-extension-components#image) should be used to add a logo or other visual brand identity asset, or to accentuate other content in the extension. Images cannot exceed the width of the extension's container at various screen sizes, and values beyond that maximum width will not be applied to the image.

![ui-extension-image-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-image-component.png?width=527&height=464&name=ui-extension-image-component.png)

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   In a custom card that displays a contact's purchased real estate, include an image of the property.
*   Add a logo or other visual asset to a card that reflects your brand's identity.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** use images with a predominantly horizontal aspect ratio for scalability (e.g. 21:9, 16:9, 4:3) for scalability.
*   **DO:** balance image quality and page performance. Images should be high enough quality to serve their purpose, but should not exceed 2-3MBs.
*   **DO:** include alt-text in every image (set by the `alt` prop) for accessibility.
*   **DON'T:** use images containing text that can only be interpreted by sighted users.
*   **DON'T:** use images that contain hateful, violent, or profane language and/or visuals.

Inputs[](https://developers.hubspot.com/docs/platform/component-design-guidelines#inputs)
-----------------------------------------------------------------------------------------

The [`Input` component](/docs/platform/ui-extension-components#input) renders a text input field where users can enter a custom text value. Like other inputs, this component should only be used within a [form](https://developers.hubspot.com/docs/platform/ui-extension-components#form) that has a submit button.

![design-guidelines-input](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-input.png?width=700&height=214&name=design-guidelines-input.png)

1.  **Label:** the input's label.
2.  **Description:** the text that describes the field's purpose.
3.  **Placeholder:** the placeholder value that displays when no value has been entered.
4.  **Required field indicator:** communicates to the user that the field is required for form submission.
5.  **Tooltip:** on hover, displays additional information about the field.

### Usage example[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-example)

Use for form fields where a user can enter any value, such as email address or name.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** make label and description text concise and clear.
*   **DO:** include placeholder text to help users understand what's expected in the field.
*   **DO:** indicate if a field is required.
*   **DO:** include clear validation error messages so that users know how to fix errors.
*   **DON'T:** use this component for long responses, such as open-ended comments or feedback. Instead, use the [text area input](#text-area-input).
*   **DON'T:** use placeholder text for critical information, as it will disappear once users begin to type. Critical information should be placed in the label and descriptive text, with additional context in the tooltip if needed.

Number inputs[](https://developers.hubspot.com/docs/platform/component-design-guidelines#number-inputs)
-------------------------------------------------------------------------------------------------------

The [`NumberInput` component](/docs/platform/ui-extension-components#number-input) renders an field for entering number values. Like other inputs, this component should only be used within a [form](https://developers.hubspot.com/docs/platform/ui-extension-components#form) that has a submit button.

![design-guidelines-number-input](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-number-input.png?width=700&height=183&name=design-guidelines-number-input.png)

1.  **Label:** the input's label.
2.  **Description:** the text that describes the field's purpose.
3.  **Value:** an entered value.

### Usage example[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-example)

A field where salespeople can enter the total deal amount.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** make label and description text concise and clear.
*   **DO:** include placeholder text to help users understand what's expected in the field.
*   **DO:** indicate if there is a minimum or maximum number requirement.
*   **DO:** indicate if a field is required.
*   **DO:** include clear validation error messages so that users know how to fix errors.
*   **DON'T:** use this component for long responses, such as open-ended comments or feedback. Instead, use the [text area input](#text-area-input).
*   **DON'T:** use placeholder text for critical information, as it will disappear once users begin to type. Critical information should be placed in the label and descriptive text, with additional context in the tooltip if needed.

Select inputs[](https://developers.hubspot.com/docs/platform/component-design-guidelines#select-inputs)
-------------------------------------------------------------------------------------------------------

The [`Select` input component](/docs/platform/ui-extension-components#select-input) renders a dropdown select field where a user can select a single value. A search bar will be automatically included when there are more than seven options. Like other inputs, this component should only be used within a [form](https://developers.hubspot.com/docs/platform/ui-extension-components#form) that has a submit button.

![design-guidelines-select-input](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-select-input.png?width=700&height=162&name=design-guidelines-select-input.png)

1.  **Label:** the label that describes the field's purpose.
2.  **Value:** the field's selected value.

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

Using the `variant` prop, you can render the input with standard styling or transparent styling:

*   `variant="input"` (default):  
    ![ui-extension-components-input-selelect-input-variant](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-input-selelect-input-variant.png?width=537&height=273&name=ui-extension-components-input-selelect-input-variant.png)
*   `variant="transparent"`: 

![ui-extension-components-input-selelect-transparent-variant](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-input-selelect-transparent-variant.png?width=286&height=271&name=ui-extension-components-input-selelect-transparent-variant.png)

*   When `readOnly` is set to `true`, the field will be greyed out and uneditable.  
    ![design-guidelines-select-input-read-only](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-select-input-read-only.png?width=513&height=103&name=design-guidelines-select-input-read-only.png)
*   When you include a `placeholder` value, that value will display by default. Otherwise, the field will display _Select_ by default.

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

Use this type of field when there are a range of set options to choose from, such as:

*   A list of products that can be purchased.
*   A list of office locations to ship to.
*   A list of delivery options for a vendor.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** make label and description text concise and clear.
*   **DO:** indicate if a field is required.
*   **DO:** include clear validation error messages so that users know how to fix errors.
*   **DO:** include placeholder text to help users understand what's expected in the field.
*   **DON'T:** use this component when you want users to be able to select multiple options. Instead, use the [multi-select input component](/docs/platform/ui-extension-components#multi-select-input).
*   **DON'T:** use placeholder text for critical information, as it will disappear once users begin to type. Critical information should be placed in the label and descriptive text, with additional context in the tooltip if needed.

Text area inputs[](https://developers.hubspot.com/docs/platform/component-design-guidelines#text-area-inputs)
-------------------------------------------------------------------------------------------------------------

The [`TextArea` input component](/docs/platform/ui-extension-components#text-area-input) renders a text field where users can enter longer strings of text. Using props, you can customize the size of the field along with the maximum number of characters. Like other inputs, this component should only be used within a [form](https://developers.hubspot.com/docs/platform/ui-extension-components#form) that has a submit button.

![design-guidelines-text-area](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-text-area.png?width=700&height=307&name=design-guidelines-text-area.png)

1.  **Label:** the field's label.
2.  **Description:** the text that describes the field's purpose.
3.  **Value:** an entered value.
4.  **Required field indicator:** communicates to the user that the field is required for form submission.
5.  **Tooltip:** on hover, displays additional information about the field.

### Usage example[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-example)

A field where salespeople can leave comments after meeting a new client.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** make label and description text concise and clear.
*   **DO:** indicate if a field is required.
*   **DO:** include clear validation error messages so that users know how to fix errors.
*   **DO:** include placeholder text to help users understand what's expected in the field.
*   **DO:** indicate if there is a character limit.
*   **DON'T:** use this field for short values, such as names, numbers, and dates.
*   **DON'T:** use placeholder text for critical information, as it will disappear once users begin to type. Critical information should be placed in the label and descriptive text, with additional context in the tooltip if needed.

Links[](https://developers.hubspot.com/docs/platform/component-design-guidelines#links)
---------------------------------------------------------------------------------------

The [`Link` component](/docs/platform/ui-extension-components#link) renders a clickable hyperlink. Links might take users to another page or part of the HubSpot app, or function as buttons.

![design-guidelines-link](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-link.png?width=700&height=232&name=design-guidelines-link.png)

1.  **Link text:** text that describes where the link leads.
2.  **External link** **icon**: indicates that the link will lead to a page outside of the HubSpot app. 

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

Using the `variant` prop, you can set the following styling:

*   `primary`: the default blue (#0091ae).  
    ![design-guidelines-links_4](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_4.png?width=206&height=37&name=design-guidelines-links_4.png) 
*   `light`: a white link that turns to a lighter shade of blue on hover (#7fd1de).  
    ![design-guidelines-links_3](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_3.png?width=206&height=34&name=design-guidelines-links_3.png)
*   `dark`: a darker shade of blue (#33475b).  
    ![design-guidelines-links_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_2.png?width=206&height=38&name=design-guidelines-links_2.png)  
    
*   `destructive`: a red link (#f2545b).  
    ![design-guidelines-links_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_1.png?width=206&height=37&name=design-guidelines-links_1.png)

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Use the default `primary` variant when you want to link to another page or contact record in HubSpot.
*   Use the `light` variant when you want to include a link on a dark background.
*   Use the `dark` variant to include a link in an alert.
*   Use the `destructive` variant when the link results in an action that can't be undone by the user, such as deleting contact property information.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** space out links so that users can tell when they'll be navigation to a different place.
*   **DO:** make link text concise and contextual.
*   **DO:** use the `destructive` variant sparingly and only when the action can't be undone.
*   **DON'T:** crowd multiple links together.
*   **DON'T:** use the `dark` variant outside of alerts.

Loading spinners[](https://developers.hubspot.com/docs/platform/component-design-guidelines#loading-spinners)
-------------------------------------------------------------------------------------------------------------

The [`LoadingSpinner` component](/docs/platform/ui-extension-components#loading-spinner) renders a visual indicator that the card is loading or processing information. 

![design-guidelines-loading-spinners](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-loading-spinners.png?width=1600&height=615&name=design-guidelines-loading-spinners.png)

1.  **Label:** the text that describes the loading state.
2.  **Size:** the size of the component. From left to right: extra small (`xs`), small (`sm`, default), medium (`md`).
3.  **Layout:** the positioning of the spinner. From left to right: `inline`, `centered`.

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   A loading state after the user submits form data to an external system (e.g., "Submitting contact details").
*   A loading state as the card retrieves customer purchase history from an external system (e.g., "Loading purchase history").

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** keep label text as concise as possible.
*   **DO:** use label text to describe what's happening during the loading process.
*   **DO:** use complete sentences in label text.
*   **DON'T:** include multiple loading spinners at once in a single card to avoid confusion.

Progress bars[](https://developers.hubspot.com/docs/platform/component-design-guidelines#progress-bars)
-------------------------------------------------------------------------------------------------------

The [`ProgressBar` component](/docs/platform/ui-extension-components#progress-bar) renders a visual representation of data in motion towards a positive or negative target.

![design-guidelines-progress-bar](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-progress-bar.png?width=1600&height=793&name=design-guidelines-progress-bar.png)

1.  **Title:** the text that displays above the bar to describe the data it represents.
2.  **Completion percentage:** the percent value of how much progress has been made.
3.  **Value description:** the text that describes the current state of the bar's value.
4.  **Variant:** the color of the progress bar.

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

Using the variant prop, you can set the following progress bar colors:

*   `success`: a green colored bar to indicate movement towards a positive goal or outcome.  
    ![design-guidelines-progress-bars_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-progress-bars_1.png?width=544&height=67&name=design-guidelines-progress-bars_1.png)
*   `warning`: a yellow colored bar to indicate movement towards a negative outcome or limitation.  
    ![design-guidelines-progress-bars_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-progress-bars_2.png?width=544&height=84&name=design-guidelines-progress-bars_2.png)
*   `danger`: a red colored bar to indicate movement towards an extremely negative outcome or when a limitation has been reached.  
    ![design-guidelines-progress-bars_3](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-progress-bars_3.png?width=544&height=81&name=design-guidelines-progress-bars_3.png)

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Evaluating the sale of products against a quota or goal.
*   Communicating the stage progress of a deal or ticket.
*   Monitoring the number of support calls or tickets per customer.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** use the `showPercentage` prop to give the user more information about the status of the progress.
*   **DON'T:** use more than 3-4 progress bars in a single card.

Statistics[](https://developers.hubspot.com/docs/platform/component-design-guidelines#statistics)
-------------------------------------------------------------------------------------------------

The [`Statistics` component](/docs/platform/ui-extension-components#statistics) renders a visual spotlight of one or more data points. Includes the `StatisticItem` and `StatisticTrend` components. 

![design-guidelines-statistics](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-statistics.png?width=1600&height=432&name=design-guidelines-statistics.png)

1.  **StatisticItem label:** the `statisticItem`'s label text.
2.  **StatisticItem number:** the `statisticItem`'s primary number.
3.  **StatisticTrend value:** the percentage trend value.
4.  **StatisticTrend direction:** the direction if the trend arrow (up or down).

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

In `StatisticsTrend` components, use the `direction` prop to describe whether the data is trending up or down.

*   `increase`: for additions or positive progression for a given time period.  
    ![design-guidelines-increase-trend](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-increase-trend.png?width=151&height=121&name=design-guidelines-increase-trend.png)
*   `decrease`: for subtractions or negative progression for a given time period.  
    ![design-guidelines-decrease-trend](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-decrease-trend.png?width=137&height=113&name=design-guidelines-decrease-trend.png)

Note that the positive or negative movement of a given statistic is intended solely to represent the increase or decrease in numerical value. Be mindful of how these movements can communicate sentiment. For example, a decrease in support volume can be a net positive, which can be confusing when represented by a red, downward arrow.

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Calling out the progress of quarterly sales for a company.
*   Monitoring the amount of traffic and social media engagement that a contact has for the month.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** keep statistics labels short and concise.
*   **DO:** place statistics components towards the top of a card when possible to enable users to more easily scan information without scrolling.
*   **DON'T:** include more than three statistics components per card if possible.
*   **DON'T:** use more than four statistics components side by side.
*   **DON'T:** include sensitive data that you don't want all users to see.

Tables[](https://developers.hubspot.com/docs/platform/component-design-guidelines#tables)
-----------------------------------------------------------------------------------------

The [`Table` component](/docs/platform/ui-extension-components#table) renders a table that displays information in columns and rows. To build a table, you'll need to include the following other components:

*   `TableHead`: the header section of the table containing column labels.
*   `TableRow`: individual table rows.
*   `TableHeader`: cells containing bolded column labels.
*   `TableBody`: container for the main table contents (rows and cells).
*   `TableCell`: individual cells within the main body.

![design-principes-table-with-pagination](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-principes-table-with-pagination.png?width=748&height=571&name=design-principes-table-with-pagination.png)

1.  **Table head:** the header row of the table containing table headers that label each column.
2.  **Table row:** an individual table row containing table cells. 
3.  **Table column:** an individual column, consisting of a table header and table cells in each row.
4.  **Table cell:** an individual cell containing data. 
5.  **Pagination:** table pagination to navigate through contents.

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   A client list containing names, phone numbers, job positions, and email addresses that salespeople can use to prioritize outreach.
*   A summary table of the deals closed last quarter.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** keep text within data cells clear and concise for easier scanning.
*   **DO:** always include a table header row to label columns.
*   **DO:** limit the use of links in table cells.
*   **DON'T:** use multiple tables on one screen when possible.
*   DON'T: render a blank table if there's no potential for no data to display, such as with search or filters. Instead, use the [empty state component](#empty-states) when there are no results to display.

Tags[](https://developers.hubspot.com/docs/platform/component-design-guidelines#tags)
-------------------------------------------------------------------------------------

The [`Tag` component](/docs/platform/ui-extension-components#tag-nbsp-) renders a tag to label or categorize information or other components. Tags can be static or clickable for invoking functions.

![design-guidelines-tag](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-tag.png?width=400&height=177&name=design-guidelines-tag.png)

1.  **Variant:** the color of the tag.
2.  **Tag text:** the text that communicates the tag's purpose.

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

Using the `variant` prop, you can choose from one of four tag colors:

*   `default` (default): for general tagging and labeling.  
    ![design-guidelines-tags_1](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-tags_1.png?width=125&height=51&name=design-guidelines-tags_1.png)
*   `success`: for indicating or confirming the success of an action.  
    ![design-guidelines-tags_2](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-tags_2.png?width=111&height=50&name=design-guidelines-tags_2.png)
*   `warning`: for indicating something that might be time-sensitive or of importance.  
    ![design-guidelines-tags_3](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-tags_3.png?width=111&height=44&name=design-guidelines-tags_3.png)
*   `error`: for indicating error or failure.  
    ![design-guidelines-tags_4](https://developers.hubspot.com/hs-fs/hubfs/design-guidelines-tags_4.png?width=101&height=52&name=design-guidelines-tags_4.png)

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Use a default tag to indicate that a customer is active
*   Use a success tag to indicate that an item in a to-do list has been completed.
*   Use a warning tag to indicate that a deal is expiring soon.
*   Use an error tag to indicate that an error happened when trying to sync a specific property in a table.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** make tag text concise and clear.
*   **DO:** ensure that tag variants are used consistently across the extension.
*   **DON'T:** use tags in place of buttons or links.
*   **DON'T:** rely on color alone to communicate the tag's meaning. Ensure that tag text is clear and helpful.

Text[](https://developers.hubspot.com/docs/platform/component-design-guidelines#text)
-------------------------------------------------------------------------------------

The [`Text` component](/docs/platform/ui-extension-components#text) renders text with formatting options.

![design-guidelines-text](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-text.jpg?width=207&height=231&name=design-guidelines-text.jpg)

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

Using the `format` prop, you can style text with a number of options:

*   `{ fontWeight: 'bold' }`: sets the text to bold.
*   `{ fontWeight: 'demibold' }`: sets the text to a lighter bold.
*   `{ italic: true }`: sets the text to italics.
*   `{ lineDecoration: 'strikethrough' }`: adds a strikethrough to the text.
*   `{ lineDecoration: 'underline' }`: underlines the text.
*   `<Text inline={true}>`: enables you to set text styling within the same line by adding more text without breaking the line. For example: `<Text>Text <Text inline={true} format=> with inner bold.</Text>`.

You can also control text size with the `variant` prop.

*   `variant="bodytext"` (default)  
    ![design-guidelines-text-size_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-text-size_1.png?width=250&height=64&name=design-guidelines-text-size_1.png)
*   `variant="microcopy"`  
    ![design-guidelines-text-size_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-text-size_2.png?width=213&height=50&name=design-guidelines-text-size_2.png)

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Use body text when you want to display a summary of the last call with a contact.
*   Use microcopy to include an explanation of a displayed status on a contact record.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** use text with clear messaging.
*   **DO:** use text formatting thoughtfully. For example, don't bold all of the text that can be seen. Instead, only bold key words and phrases for easier scanning.
*   **DON'T:** use the text component for the primary textual information on a card. Instead, consider using the [header component](#headers).
*   **DON'T:** use underline formatting for text that's next to a hyperlink, as it will also look clickable.
*   **DON'T:** use microcopy for important or critical information. Instead, consider whether an [alert component](#alerts) would fit better.
*   **DON'T:** use text components in place of headers, alerts, and errors.

Tiles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#tiles)
---------------------------------------------------------------------------------------

The [`Tile` component](/docs/platform/ui-extension-components#tile) renders a square tile that can contain other components. Use this component to create groups of related components.

![design-guidelines-tiles](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-tiles.png?width=519&height=91&name=design-guidelines-tiles.png)

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

Using the `flush` prop, you can remove left and right padding from the tile contents.

*   `flush={false}` (default)  
    ![design-guidelines-tile-styles_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-tile-styles_1.png?width=546&height=109&name=design-guidelines-tile-styles_1.png)
*   `flush={true}`  
    ![design-guidelines-tile-styles_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-tile-styles_2.png?width=546&height=108&name=design-guidelines-tile-styles_2.png)

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   Group a form and its inputs together.
*   Group a bulleted text summary and statistics components together.

Toggle groups[](https://developers.hubspot.com/docs/platform/component-design-guidelines#toggle-groups)
-------------------------------------------------------------------------------------------------------

The [`ToggleGroup` component](/docs/platform/ui-extension-components#toggle-group) renders a list of selectable options, either in radio button or checkbox form.

![design-guide-toggle-group](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guide-toggle-group.png?width=400&height=293&name=design-guide-toggle-group.png)

1.  **Group label:** the text that displays above the group of checkboxes.
2.  **Tooltip:** on hover, displays additional information about the field.
3.  **Unchecked checkbox:** an unselected checkbox.
4.  **Option label:** the text that displays next to the checkbox.
5.  **Option description:** the text that displays below the option label to describe the option.

### Styles[](https://developers.hubspot.com/docs/platform/component-design-guidelines#styles)

By default, the toggle group will render as a vertical list of checkboxes. Using the `toggleType` prop, you can set the options to display as checkboxes or radio buttons. You can also use the `inline` prop to stack options horizontally.  
  

*   `toggleType="checkboxList"` (default)  
    ![design-guidelines-togglegroup-styles_3](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_3.png?width=273&height=178&name=design-guidelines-togglegroup-styles_3.png)
*   `toggleType="radioButtonList"`

![design-guidelines-togglegroup-styles_4](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_4.png?width=273&height=164&name=design-guidelines-togglegroup-styles_4.png)

*   `inline={true}`

![design-guidelines-togglegroup-styles_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_1.png?width=443&height=105&name=design-guidelines-togglegroup-styles_1.png)

![design-guidelines-togglegroup-styles_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-togglegroup-styles_2.png?width=443&height=111&name=design-guidelines-togglegroup-styles_2.png)

### Usage examples[](https://developers.hubspot.com/docs/platform/component-design-guidelines#usage-examples)

*   A radio button list to enable salespeople to select one of four sales packages for a new customer.
*   A checkbox list to enable customer support reps to select several options of swag to send to a delightful customer.

### Guidelines[](https://developers.hubspot.com/docs/platform/component-design-guidelines#guidelines)

*   **DO:** use this component when the user has a small selection of items to choose from. For longer lists of options, consider using the [select input](#select-input) instead.
*   **DO:** keep label options concise when possible.
*   **DON'T:** use toggle groups to display long lists of options.

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/component-design-guidelines#page-feedback)
-------------------------------------------------------------------------------------------------------------

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
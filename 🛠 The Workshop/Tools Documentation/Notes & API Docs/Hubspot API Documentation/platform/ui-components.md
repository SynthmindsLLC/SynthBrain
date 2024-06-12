---
Please provide me with the context or the topic of the mission you want to define. 

For example, tell me: "* **What is the mission for?** (e.g., a company, a project, a team, a personal goal)"
* **What is the overall objective?** (e.g., to solve a problem, to create something new, to improve something)
* **What are the key values or principles?** (e.g., innovation, sustainability, customer focus)

Once I have this information, I can help you create a compelling and impactful mission statement.
---

UI components overview (BETA)
=============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

To create the UI for a [UI extension](/docs/platform/create-ui-extensions), you can include any number of HubSpot-provided reusable components. These components range from simple text fields to out-of-the-box CRM object reports, and each component offers customization options through properties.

Components are imported at the top of your `tsx` or `jsx` extension file. Depending on the type of component, you'll need to import them from one of two SDK directories.

*   [Standard components](#standard-components) are imported from `'@hubspot/ui-extensions'`
*   [CRM data](#crm-data-components) and [CRM action components](#crm-action-components) are imported from `'@hubspot/ui-extensions/crm'`

import { Alert, Text } from '@hubspot/ui-extensions'; import { CrmAssociationPivot, CrmActionLink } from '@hubspot/ui-extensions/crm';

**Please note:** to access the latest components, ensure that you've installed the latest npm package by running `npm i @hubspot/ui-extensions` in the `extensions` directory.

Standard components[](https://developers.hubspot.com/docs/platform/ui-components#standard-components)
-----------------------------------------------------------------------------------------------------

Standard components are components that can be used for both internal and external data. These components do not fetch data on their own, but are more flexible in their implementation.

These components are imported from `'@hubspot/ui-extensions'`.

| Component | Description |
| --- | --- |
| [Accordion](/docs/platform/ui-components/accordion) | A collapsable accordion section that can contain other components. |
| [Alert](/docs/platform/ui-components/alert) | Alerts for indicating statuses and action outcomes, such as success and error messages. |
| [Box](/docs/platform/ui-components/box) | Component used for layout management. Can be used with [Flex](/docs/platform/ui-components/flex). Learn more about [managing extension layout](/docs/platform/manage-ui-extension-layout). |
| [Button](/docs/platform/ui-components/button) | Buttons that enable users to perform actions, such as sending or retrieving data. |
| [Button row](/docs/platform/ui-components/buttonrow) | For rendering multiple buttons. |
| [Checkbox](/docs/platform/ui-components/checkbox) | A single checkbox input. To display multiple checkboxes, use [ToggleGroup](/docs/platform/ui-components/togglegroup) instead. |
| [DateInput](/docs/platform/ui-components/dateinput) | A field that enables users to select a date. |
| [DescriptionList](/docs/platform/ui-components/descriptionlist) | Displays pairs of custom labels and values, similar to how HubSpot properties appear in the left sidebar of CRM records. |
| [Divider](/docs/platform/ui-components/divider) | A horizontal line for separating components within an extension. |
| [Dropdown](/docs/platform/ui-components/dropdown) | A dropdown menu for selecting values, styled as either buttons or hyperlinks. |
| [EmptyState](/docs/platform/ui-components/emptystate) | A labeled illustration to indicate a component without content. |
| [ErrorState](/docs/platform/ui-components/errorstate) | Labeled illustrations to indicate errors. |
| [Flex](/docs/platform/ui-components/flex) | Wraps other components in an empty `div` set to `display=flex`. Use this component and [Box](/docs/platform/ui-components/box) to [manage extension layout](/docs/platform/manage-ui-extension-layout). |
| [Form](/docs/platform/ui-components/form) | A form for submitting data, which can contain other related components such as [Input](/docs/platform/ui-components/input), [Select](/docs/platform/ui-components/select), and [Button](/docs/platform/ui-components/button). |
| [Heading](/docs/platform/ui-components/heading) | Renders large text for titles. |
| [Image](/docs/platform/ui-components/image) | An image, primarily used for adding logos or other visual brand identity assets, or to accentuate other extension content. |
| [Input](/docs/platform/ui-components/input) | A text input field where users can enter custom text values. Primarily used within [Form](/docs/platform/ui-components/form) components. |
| [Link](/docs/platform/ui-components/link) | A clickable hyperlink for navigating to external and HubSpot app pages, or for triggering functions. |
| [List](/docs/platform/ui-components/list) | An ordered or unordered list of items. |
| [LoadingSpinner](/docs/platform/ui-components/loadingspinner) | A visual indicator that the card is loading or processing. |
| [MultiSelect](/docs/platform/ui-components/multiselect) | A dropdown select field where users can select multiple values. To allow only one value to be selected, use [Select](/docs/platform/ui-components/select) instead. Primarily used within [Form](/docs/platform/ui-components/form) components. |
| [NumberInput](/docs/platform/ui-components/numberinput) | A number input field. Primarily used within [Form](/docs/platform/ui-components/form) components. |
| [Panel](/docs/platform/ui-components/panel) | A panel that opens on the right side of the page, containing other components. Can be opened and closed by using `onClick` handles in [Button](/docs/platform/ui-components/button), [Link](/docs/platform/ui-components/link), [Tag](/docs/platform/ui-components/tag), and [Image](/docs/platform/ui-components/image) components. |
| [ProgressBar](/docs/platform/ui-components/progressbar) | A visual representation of data in motion toward a positive or negative target. Can display both numbers and percentages. |
| [RadioButton](/docs/platform/ui-components/radiobutton) | A radio select button. If you want to include more than two radio buttons, or are building a [Form](/docs/platform/ui-components/form), it's recommended to use [ToggleGroup](/docs/platform/ui-components/togglegroup) instead. |
| [Select](/docs/platform/ui-components/select) | A dropdown select field where a user can select a single value. To allow selecting multiple values, use [MultiSelect](/docs/platform/ui-components/multiselect) instead. |
| [Statistics](/docs/platform/ui-components/statistics) | A visual spotlight of one or more data points. Includes numeric values and trend indicators (increasing/decreasing percentage). |
| [StepIndicator](/docs/platform/ui-components/stepindicator) | A visual indicator to describe the progress within a multi-step process. |
| [StepperInput](/docs/platform/ui-components/stepperinput) | Similar to the [NumberInput](/docs/platform/ui-components/numberinput) component, but this field enables users to increase or decrease the value by a set amount. |
| [Table](/docs/platform/ui-components/table) | Displays data in columns and rows. Tables can be paginated and sortable. |
| [Tag](/docs/platform/ui-components/tag) | Colored labels for categorizing information or other components. Can be static or clickable for triggering functions. |
| [Text](/docs/platform/ui-components/text) | Renders text with formatting options. |
| [Tile](/docs/platform/ui-components/tile) | A rectangular, bordered container for creating groups of related components. |
| [TextArea](/docs/platform/ui-components/textarea) | Similar to [Text](/docs/platform/ui-components/text), but for longer sets of text. Includes props for configuring field size, maximum characters, and resizeability. |
| [Toggle](/docs/platform/ui-components/toggle) | A boolean toggle switch that can be configured with sizing and label options. |
| [ToggleGroup](/docs/platform/ui-components/togglegroup) | A list of selectable checkboxes or radio buttons. |

CRM data components[](https://developers.hubspot.com/docs/platform/ui-components#crm-data-components)
-----------------------------------------------------------------------------------------------------

CRM data components can pull data directly from the currently displaying CRM record, including information about associated records and single object reports. These components can only be placed in the middle column of CRM records. Learn more about [CRM data components](/docs/platform/ui-components/crm-data-components).

These components are imported from `@hubspot/ui-extensions/crm`.

| Component | Description |
| --- | --- |
| [CrmAssociationPivot](/docs/platform/ui-components/crmassociationpivot) | A list of records associated with the currently dislplaying record, organized by their association label. |
| [CrmAssociationPropertyList](/docs/platform/ui-components/crmassociationpropertylist) | An editable list of CRM properties belonging to a record associated with the currently displaying record.  |
| [CrmAssociationTable](/docs/platform/ui-components/crmassociationtable) | A table of records associated with the currently displaying record. |
| [CrmDataHighlight](/docs/platform/ui-components/crmdatahighlight) | A list of CRM properties belonging to the currently displaying record or another specified record. |
| [CrmPropertyList](/docs/platform/ui-components/crmpropertylist) | An editable list of CRM properties belonging to the currently displaying record or another specified record. |
| [CrmReport](/docs/platform/ui-components/crmreport) | Display an existing single object report. Includes filtering options, or can display all report data unfiltered. |
| [CrmStageTracker](/docs/platform/ui-components/crmstagetracker) | A lifecycle or pipeline stage progress bar with a list of properties. |
| [CrmStatistics](/docs/platform/ui-components/crmstatistics) | Display summaries of data calculated from the currently displaying record's associations. For example, the average revenue across a contact's associated companies. |

CRM action components[](https://developers.hubspot.com/docs/platform/ui-components#crm-action-components)
---------------------------------------------------------------------------------------------------------

CRM action components provide a built-in set of CRM-related actions, including adding notes to records, opening a one-to-one email composition window, creating new records, and more. Each component can perform the same set of actions, so which component to choose will depend on your needs and preferences. Learn more about [CRM action components](/docs/platform/ui-components/crm-action-components).

CRM action components are imported from `@hubspot/ui-extensions/crm`.

| Component | Description |
| --- | --- |
| [CrmActionButton](/docs/platform/ui-components/crmactionbutton) | A button that can execute a built-in set of CRM actions.  |
| [CrmActionLink](/docs/platform/ui-components/crmactionlink) | A clickable link that can execute a built-in set of CRM actions. |
| [CrmCardActions](/docs/platform/ui-components/crmcardactions) | Smaller standalone or dropdown menu buttons that can contain multiple CRM actions. |

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components#page-feedback)
-----------------------------------------------------------------------------------------------

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
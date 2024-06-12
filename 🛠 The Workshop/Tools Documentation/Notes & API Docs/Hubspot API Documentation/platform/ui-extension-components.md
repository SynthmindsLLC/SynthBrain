---
Please provide me with more context! To help you write your mission statement, I need to know: "* **What is the purpose of this mission?**  Is it for a company, a project, a personal goal, or something else?"
* **What are the goals and objectives?** What do you want to achieve?
* **What are the values and principles?** What are the guiding beliefs that will inform your actions?
* **Who is your target audience?**  Who are you trying to reach with your mission?

Once I have this information, I can help you craft a compelling and effective mission statement.
---

UI extension components (BETA)
==============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

When [building a UI extension](/docs/platform/create-ui-extensions), you'll include any number of HubSpot-provided components to render the extension's UI. There are three types of components to select from:

*   **Standard components:** raw components that can be used for both internal and external data. These components do not fetch data on their own, but are more flexible in their implementation.

*   **CRM data components:** out of the box components that can fetch/display only HubSpot data. These components enable easy visualization of account data, including properties, associations, and reports. They also automatically handle permissions, input validation, conditional properties, and more. These components can only be placed in the middle column of CRM records.
*   **CRM action components:** out of the box actions related to CRM records, engagements, and more. Includes three components and a set of actions that each can perform. For example, use these actions to create new records, schedule meetings, and navigate to other HubSpot pages.

Components are included in the UI Extensions SDK, and should be imported at the top of your `jsx` or `tsx` file. Standard components are imported from `'@hubspot/ui-extensions'` while CRM data and CRM action components are imported from `'@hubspot/ui-extensions/crm'`.  
  

import { Alert, Text } from '@hubspot/ui-extensions'; import { CrmAssociationPivot, CrmActionLink } from '@hubspot/ui-extensions/crm';

**Please note:** to access the latest components, ensure that you've installed the latest npm package by running `npm i` `@hubspot/ui-extensions` in the `extensions` directory.

Below are the currently available UI extension components:

Standard components

*   [Accordion](#accordion)
*   [Alert](#alert)
*   [Button](#button)
*   [Button row](#button-row)
*   [Description list](#description-list)
*   [Divider](#divider)
*   [Dropdown](#dropdown-component)
*   [Empty state](#empty-state)
*   [Error state](#error-state)
*   [Form](#form)
*   [Heading](#heading)
*   [Image](#image)
*   Inputs:
    *   [Checkbox](#checkbox)
    *   [Date input](#date-input)
    *   [Input](#input)
    *   [Multi-select input](#multi-select-input)
    *   [Number input](#number-input)
    *   [Radio button](#radio-button)
    *   [Select input](#select-input)
    *   [Stepper input](#stepper-input)
    *   [Text area input](#text-area-input)
    *   [Toggle](#toggle)
    *   [Toggle group](#toggle-group)

*   Layout components:
    *   [Flex](#layout-flex)
    *   [Box](#layout-box)
*   [Link](#link)
*   [List](#list)
*   [Loading spinner](#loading-spinner)
*   [Panel](#panel)
*   [Progress bar](#progress-bar)
*   [Statistics](#statistics)
*   [Step indicator](#step-indicator)
*   [Table](#table)
*   [Tag](#tag-nbsp-)
*   [Text](#text)
*   [Tile](#tile)

CRM data components

*   [Overview and filtering](#crm-data-components)
*   [Association pivot](#association-pivot)
*   [Association property list](#association-property-list)
*   [Association table](#association-table)
*   [Data highlight](#data-highlight)
*   [Property list](#property-list)
*   [Report](#report)
*   [Stage tracker](#stage-tracker)
*   [CRM statistics](#crm-statistics)

CRM action components

*   [**Overview**](#crm-action-components)
*   [Action buttons](#action-buttons)
*   [Action links](#action-links)
*   [**Action menus**](#action-menus)
*   [**Available actions**](#available-actions)
    *   [Preview a CRM record](#preview-a-crm-record)
    *   [Create a note](#create-a-note)
    *   [Send a one-to-one email](#send-a-one-to-one-email)
    *   [Schedule a meeting](#schedule-a-meeting)
    *   [Create an associated CRM record](#create-an-associated-record)
    *   [Navigate to an engagement](#navigate-to-an-engagement)
    *   [Navigate to a record](#navigate-to-a-record)
    *   [Navigate to a HubSpot page](#navigate-to-a-hubspot-page)
    *   [Navigate to an external page](#navigate-to-an-external-page)

Below, learn about each type of component and how to include it in an extension.

Standard components[](https://developers.hubspot.com/docs/platform/ui-extension-components#standard-components)
---------------------------------------------------------------------------------------------------------------

Standard components are imported from `@hubspot/ui-extensions`.

import { Alert, Text } from '@hubspot/ui-extensions';

### Accordion[](https://developers.hubspot.com/docs/platform/ui-extension-components#accordion)

The `Accordion` component renders a collapsable accordion section that can contain other components.

![ui-extensions-accordion-section](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-accordion-section.png?width=546&height=212&name=ui-extensions-accordion-section.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>title</code>&nbsp; <strong>string </strong>(required)<p>The accordion's title text.</p></td></tr><tr><td style="padding: 10px 4px;"><code>defaultOpen</code>&nbsp; <strong>boolean</strong><p>Defines default open behavior on page load. When set to <code>true</code>, the accordion will be open by default on initial load.</p><p>The <code>open</code> prop takes precedence over this prop.</p></td></tr><tr><td style="padding: 10px 4px;"><code>disabled</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, the accordion's state cannot be changed.</p></td></tr><tr><td style="padding: 10px 4px;"><code>open</code>&nbsp; <strong>boolean</strong><p>For controlling the accordion's open state programmatically. When set to <code>true</code>, the accordion will open. Takes precedence over <code>defaultOpen</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onClick</code>&nbsp; <strong>function</strong><p>A function that will be invoked with the accordion title is clicked. This function receives no arguments and its returned value is ignored.</p></td></tr><tr><td style="padding: 10px 4px;"><code>size</code>&nbsp; <strong>string</strong><p>The size of the accordion title. Can be one of:</p><ul><li><code>xs</code> or <code>extra-small</code></li><li><code>sm</code> or <code>small</code>&nbsp;</li><li><code>md</code> or <code>medium</code> (default)</li></ul></td></tr></tbody></table>

const Extension = () => { return ( <> <Accordion title="Item One" defaultOpen={true}> <Text>Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.</Text> </Accordion> <Accordion title="Item Two"> <Text>Second inner text</Text> </Accordion> <Divider /> </> ); };

### Alert[](https://developers.hubspot.com/docs/platform/ui-extension-components#alert)

The `Alert` component renders a single alert.

![ui-ext-components-alert](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-alert.png?width=475&height=254&name=ui-ext-components-alert.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>title</code>&nbsp; <strong>string </strong>(required)<p>The bolded title text of the alert.</p></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code>&nbsp; <strong>string</strong><p>The color of the alert. The following variants are available:</p><ul><li><code>info</code><span>&nbsp;</span>(default)</li><li><code>success</code></li><li><code>warning</code></li><li><code>error</code></li><li><code>danger</code></li></ul></td></tr></tbody></table>

const Extension = () => { return ( <> <Alert title="Important Info" variant="info"> This is an informative message. </Alert> <Alert title="Success"variant="success"> Operation completed successfully. </Alert> <Alert title="Warning" variant="warning" > Proceed with caution. </Alert> <Alert title="Error" variant="error" > Something went wrong. Please try again. </Alert> <Alert title="Danger" variant="danger" > This action cannot be undone. Be careful. </Alert> </> ); };

### Button[](https://developers.hubspot.com/docs/platform/ui-extension-components#button)

The `Button` component renders a single button. The button text is passed into the component like a standard HTML element, rather than through a prop. 

![ui-ext-component-buttons-all](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-component-buttons-all.png?width=818&height=65&name=ui-ext-component-buttons-all.png)

![ui-extension-button-size-examples](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-button-size-examples.png?width=400&height=53&name=ui-extension-button-size-examples.png) 

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 99.9915%; height: 893.422px;"><tbody><tr style="height: 219.922px;"><td style="padding: 10px 4px; width: 99.7367%; height: 220px;"><code>href</code>&nbsp; <strong>string&nbsp;</strong><p>Navigates to a URL on button click. When a button includes both <code>href</code> and an <code>onClick</code> action, both will be executed on button click. Links to external pages will open in a new tab, while links to pages in the HubSpot account will open in the same tab.</p></td></tr><tr style="height: 79.6719px;"><td style="padding: 10px 4px; width: 99.7367%; height: 80px;"><code>onClick</code>&nbsp; <strong>function&nbsp;</strong><p><span>A function that will be invoked when the button is clicked. It receives no arguments and it's return value is ignored</span></p></td></tr><tr style="height: 107.922px;"><td style="padding: 10px 4px; width: 99.7367%; height: 108px;"><code>disabled</code>&nbsp; <strong>boolean</strong><p>Set to <code>true</code> to render the button in a disabled state.</p></td></tr><tr style="height: 244.422px;"><td style="padding: 10px 4px; width: 99.7367%; height: 244px;"><code>variant</code>&nbsp; <strong>string&nbsp;</strong><p>Sets the color variation of the button. Values include:</p><ul><li><code>primary</code></li><li><code>secondary</code><span>&nbsp;</span>(default)</li><li><code>destructive</code></li></ul></td></tr><tr style="height: 244.422px;"><td style="padding: 10px 4px; width: 99.7367%; height: 244px;"><code>size</code>&nbsp; <strong>string&nbsp;</strong><p>Sets the size of the button. Values include:</p><ul><li><code>xs</code>, <code>extra-small</code></li><li><code>sm</code>, <code>small</code></li><li><code>md</code>, <code>medium</code> (default)</li></ul></td></tr><tr style="height: 79.9219px;"><td style="padding: 10px 4px; width: 99.7367%; height: 80px;"><code>type</code>&nbsp; <strong>string</strong><p>Sets the HTML attribute <code>role</code> of the button. Can be one of:</p><ul><li><code>button</code> (default)</li><li><code>reset</code></li><li><code>submit</code></li></ul></td></tr></tbody></table>

const Extension = () => { return ( <Button onClick={() => { console.log('Someone clicked the button!'); }} href="https://hubspot.com" variant="destructive" size="md" type="button" > Click me! </Button> ); };

### Button row[](https://developers.hubspot.com/docs/platform/ui-extension-components#button-row)

The `ButtonRow` component renders a row of [button](#button) components. In `ButtonRow`, you'll specify individual `Button` components.

![ui-ext-component-buttonrow](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-component-buttonrow.png?width=396&height=68&name=ui-ext-component-buttonrow.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>disableDropdown</code>&nbsp; <strong>boolean</strong>&nbsp;<p>Disables the dropdown list of buttons that appears when child button expand beyond horizontal space (<code>false</code> by default).</p></td></tr></tbody></table>

const Extension = () => { return ( <ButtonRow disableDropdown={false}> <Button onClick={() => { console.log('Regular button clicked'); }} > Regular Button </Button> <Button onClick={() => { console.log('Reset button clicked'); }} variant="destructive" type="reset" > Reset </Button> <Button onClick={() => { console.log('Submit button clicked'); }} variant="primary" type="submit" > Submit </Button> </ButtonRow> ); };

### Description list[](https://developers.hubspot.com/docs/platform/ui-extension-components#description-list)

The `DescriptionList` component renders pairs of labels and values. It also contains a `DescriptionListItem` subcomponent.

![ui-ext-component-descriptionlist](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-component-descriptionlist.png?width=516&height=68&name=ui-ext-component-descriptionlist.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>direction</code>&nbsp; <strong>string</strong><br><br>The direction that the <code>label</code> and <code>value</code> pairs are displayed. By default, the value is set to <code>column</code>. You can also set the direction to <code>row</code>.</td></tr></tbody></table>

#### DescriptionListItem[](https://developers.hubspot.com/docs/platform/ui-extension-components#descriptionlistitem)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>label</code>&nbsp; <strong>string&nbsp;</strong>(required)<br><br>The text to display as the label.</td></tr></tbody></table>

const Extension = () => { return ( <DescriptionList direction="row"> <DescriptionListItem label={'First Name'}> <Text>Alan</Text> </DescriptionListItem> <DescriptionListItem label={'Last Name'}> <Text>Turing</Text> </DescriptionListItem> </DescriptionList> ); };

### Divider[](https://developers.hubspot.com/docs/platform/ui-extension-components#divider)

The `Divider` component renders a divider for spacing out components.

![ui-ext-component-divider](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-component-divider.png?width=539&height=110&name=ui-ext-component-divider.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>distance</code>&nbsp; <strong>string</strong><p>The space between the divider and the content above and below it. Can be one of:</p><ul><li><code>extra-small</code></li><li><code>small</code> (default)</li><li><code>medium</code></li><li><code>large</code></li><li><code>extra-large</code></li><li><code>flush</code></li></ul></td></tr></tbody></table>

const Extension = () => { return <Divider distance="extra-large" />; };

### Dropdown[](https://developers.hubspot.com/docs/platform/ui-extension-components#dropdown)

The `Dropdown` component renders a dropdown menu that can appear as a button or hyperlink. Includes sizing options.

![ui-extensions-dropdown-variants](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-dropdown-variants.gif?width=466&height=230&name=ui-extensions-dropdown-variants.gif)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>options</code>&nbsp; <strong>object </strong><span style="font-weight: normal;">(required)</span><p>The options included in the dropdown menu. For each option, include:</p><ul><li><code>label</code>: the text label for the option.</li><li><code>onClick</code>: the function that gets invoked when the option is selected.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code>&nbsp; <strong>string</strong><p>The type of dropdown button to display. Values include:</p><ul><li><code>primary</code> (default): a blue button.</li><li><code>secondary</code>: a grey button.</li><li><code>transparent</code>: a hyperlink.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>buttonText</code>&nbsp; <strong>string&nbsp;</strong><p>The text on the button.</p></td></tr><tr><td style="padding: 10px 4px;"><code>buttonSize</code>&nbsp; <strong>string</strong><p>The size of the button. Values include:</p><ul><li><code>xs</code>, <code>extra-small</code></li><li><code>sm</code>, <code>small</code></li><li><code>md</code>, <code>medium</code></li></ul></td></tr></tbody></table>

const Extension = () => { const ddOptions = \[ { label: 'Clone', onClick: () => console.log({ message: 'Clone group' }) }, { label: 'Delete', onClick: () => console.log({ message: 'Delete group' }) } \] return ( <Dropdown options={ddOptions} variant="primary" buttonSize="md" buttonText="More" /> ); };

### Empty state[](https://developers.hubspot.com/docs/platform/ui-extension-components#empty-state)

The `EmptyState` component sets the content that appears when the extension is in an empty state.

![ui-ext-components-emptystate](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-emptystate.png?width=305&height=264&name=ui-ext-components-emptystate.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>flush</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, removes the default vertical margins in the component.</p></td></tr><tr><td style="padding: 10px 4px;"><code>imageWidth</code>&nbsp; <strong>number</strong><p>The max-width for the image container</p></td></tr><tr><td style="padding: 10px 4px;"><code>layout</code>&nbsp; <strong>string</strong><p>Sets the layout direction for the content. Can be either <code>horizontal</code> or <code>vertical</code> (default).</p></td></tr><tr><td style="padding: 10px 4px;"><code>reverseOrder</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, swaps the visual order of the text (primary) and image (secondary) content. This ensures the primary content is still presented first to assistive technology.</p></td></tr><tr><td style="padding: 10px 4px;"><code>title</code>&nbsp; <strong>string</strong><p>The text for the title header.</p></td></tr></tbody></table>

const Extension = ({ data }) => { if (!data || !data.length) { return ( <EmptyState title="Nothing here yet" layout="vertical" reverseOrder={true}> <Text>Go out there and get some leads!</Text> </EmptyState> ) } return ( {data.map(...)} ); }

### Error state[](https://developers.hubspot.com/docs/platform/ui-extension-components#error-state)

The `ErrorState` component sets the content of an erroring extension.

![ui-ext-components-errorstate](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-errorstate.png?width=381&height=382&name=ui-ext-components-errorstate.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>title</code>&nbsp; <strong>string</strong>&nbsp;<p>The text of the title header.</p></td></tr><tr><td style="padding: 10px 4px;"><code>type</code>&nbsp; <strong>string</strong><p>The type of error image that will be shown. Can be one of:</p><ul><li><code>error</code> (default)</li><li><code>support</code></li><li><code>lock</code></li></ul></td></tr></tbody></table>

const Extension = ({ data, error, fetchData }) => { if (error) { return ( <ErrorState title="Trouble fetching properties." layout="vertical" reverseOrder={true}> <Text> Please try again in a few moments. </Text> <Button onClick={fetchData}> Try again </Button> </ErrorState> ) } return ( {data.map(...)} ); }

### Form[](https://developers.hubspot.com/docs/platform/ui-extension-components#form)

The `Form` component renders a form that can contain other subcomponents, such as [Input](#text-input), [Select](#select-input), and [Button](#button). 

![ui-ext-components-form](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-form.png?width=510&height=338&name=ui-ext-components-form.png) 

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>onSubmit</code>&nbsp; <strong>function</strong><p>The function that is called when the form is submitted. It will receive a <code>RemoteEvent</code> as an argument and its return value will be ignored.</p></td></tr><tr><td style="padding: 10px 4px;"><code>preventDefault</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, <code>event.preventDefault()</code> will be invoked before the <code>onSubmit</code> function is called, preventing the default HTML form behavior.</p></td></tr></tbody></table>

const Extension = () => { return ( <Form onSubmit={() => { console.log('Form submitted!')}} preventDefault={true}> <Input label="First Name" name="first-name" tooltip="Please enter your first name" description="Please enter your first name" placeholder="First name" /> <Input label="Last Name" name="last-name" tooltip="Please enter your last name" description="Please enter your last name" placeholder="Last name" /> <Button onClick={() => { console.log('Submit button clicked'); }} variant="primary" type="submit" > Submit </Button> </Form> ); }

### Heading[](https://developers.hubspot.com/docs/platform/ui-extension-components#heading)

The `Heading` component renders large heading text.

![ui-ext-components-heading](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-heading.png?width=215&height=50&name=ui-ext-components-heading.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>inline</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, text will not line break.</p></td></tr></tbody></table>

const Extension = () => { return <Heading>Plain text, nothing special here</Heading>; };

### Image[](https://developers.hubspot.com/docs/platform/ui-extension-components#image)

The `Image` component renders an image.

![ui-ext-component-img](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-component-img.png?width=215&height=314&name=ui-ext-component-img.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>src</code>&nbsp; <strong>string</strong> (required)<p>The URL of the image to display.</p></td></tr><tr><td style="padding: 10px 4px;"><code>alt</code>&nbsp; <strong>string&nbsp;</strong><p>The alt text for the image.</p></td></tr><tr><td style="padding: 10px 4px;"><code>href</code>&nbsp; <strong>string&nbsp;</strong><p>If provided, will be used as the href that will be opened in a new browser tab on click.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onClick</code>&nbsp; <strong>function&nbsp;</strong><p>A function that will be called when the image is clicked. This function will receive no arguments and any returned values will be ignored.</p></td></tr><tr><td style="padding: 10px 4px;"><code>width</code>&nbsp; <strong>number&nbsp;</strong><p>The pixel width of the image.</p></td></tr><tr><td style="padding: 10px 4px;"><code>height</code>&nbsp; <strong>number&nbsp;</strong><p>The pixel height of the image.</p></td></tr></tbody></table>

const Extension = () => { return ( <Image alt="A picture of an adorable black lab puppy, click on me to see in a new tab" src="https://picsum.photos/id/237/200/300" href="https://picsum.photos/id/237" onClick={() => { console.log('Someone clicked on the image!'); }} width={200} /> ); };

### Checkbox[](https://developers.hubspot.com/docs/platform/ui-extension-components#checkbox)

The `Checkbox` component renders single checkbox input. If you want to display multiple checkboxes, you may want to use [ToggleGroup](#toggle-group) instead, as it comes with extra logic for handling multiple checkboxes and radio buttons.

![ui-extensions-component-checkbox](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-component-checkbox.png?width=300&height=93&name=ui-extensions-component-checkbox.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 4px;"><code>value</code>&nbsp; <strong>string</strong><p>The checkbox value. This value is not displayed on the card, but is passed on the server side when submitted, along with the checkbox name.</p></td></tr><tr><td style="padding: 4px;"><code>name</code>&nbsp; <strong>string</strong><p>The checkbox's unique identifier.</p></td></tr><tr><td style="padding: 4px;"><code>checked</code>&nbsp;&nbsp;<strong>boolean&nbsp;</strong><p>When set to <code>true</code>, the checkbox is selected by default. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 4px;"><code>initialIsChecked</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, the checkbox is selected by default. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 4px;"><code>readonly</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, users cannot toggle the checkbox. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 4px;"><code>description</code>&nbsp; <strong>string&nbsp;</strong><p>The string that displays below the checkbox.</p></td></tr><tr><td style="padding: 4px;"><code>aria-label</code>&nbsp; <strong>string</strong><p>The checkbox's accessibility label.</p></td></tr><tr><td style="padding: 4px;"><code>variant</code>&nbsp; <strong>string&nbsp;</strong><p>The size of the checkbox. Values include:</p><ul><li><code>sm</code>, <code>small</code></li><li><code>default</code></li></ul></td></tr><tr><td style="padding: 4px;"><code>inline</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, arranges checkboxes side by side. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 4px;"><code>onChange</code>&nbsp; <strong>function</strong><p>A callback function that is called when the checkbox is selected or cleared. Passes the new value.</p><p><code>(checked: boolean, value: string) =&gt; void;</code></p></td></tr></tbody></table>

const Extension = () => { return ( <Checkbox checked={isSuperAdmin} name="adminCheck" description="Select to grant superpowers" > Super Admin </Checkbox> ); };

### Date input[](https://developers.hubspot.com/docs/platform/ui-extension-components#date-input)

The `DateInput` component renders an input field where a user can select a date.

![ui-extension-components-date-input](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-date-input.png?width=580&height=362&name=ui-extension-components-date-input.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100.018%; height: 2701px;"><tbody><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>name</code>&nbsp; <strong>string </strong>(required)<p>The input's unique identifier, similar to the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name" rel="noopener">HTML input element <code>name</code> attribute</a>.</p></td></tr><tr style="height: 72px;"><td style="padding: 4px; width: 99.7%; height: 72px;"><code>label</code>&nbsp; <strong>string </strong>(required)<p>The text that displays above the input.</p></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>required</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, displays a required indicator.</p></td></tr><tr><td style="padding: 4px; width: 99.7%;"><code>value</code>&nbsp; <strong>object&nbsp;</strong><p>The value of the input. Must include the year, month, and day:</p><p><code>{ year: number;</code><code>month: number;</code><code>date: number }</code></p><ul><li><code>year</code>: the four-digit year (e.g., <code>2023</code>).</li><li><code>month</code>: starting at <code>0</code>, the number of the month (e.g., <code>0</code> = January, <code>11</code> = December).</li><li><code>date</code>: the number of the day (e.g., <code>1</code> = the first day of the month).</li></ul></td></tr><tr style="height: 124px;"><td style="padding: 4px; width: 99.7%; height: 124px;"><code>readOnly</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, sets the field as read-only on the CRM record, and users will not be able to fill the field.</p></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>description</code>&nbsp; <strong>string&nbsp;</strong><p>Displayed text that describes the field's purpose.</p></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>tooltip</code>&nbsp; <strong>string&nbsp;</strong><p>The text that displays in a tooltip next to the label.</p></td></tr><tr style="height: 208px;"><td style="padding: 4px; width: 99.7%; height: 208px;"><code>error</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, <code>validationMessage</code> is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left <code>false</code> (default), <code>validationMessage</code> is displayed as a success message.</p></td></tr><tr style="height: 72px;"><td style="padding: 4px; width: 99.7%; height: 72px;"><code>validationMessage</code>&nbsp; <strong>string&nbsp;</strong><p>The text to show if the input has an error.</p></td></tr><tr style="height: 124px;"><td style="padding: 4px; width: 99.7%; height: 124px;"><code>onChange</code>&nbsp; <strong>function</strong><p>A callback function that is invoked when the value is committed. Currently, this occurs on <code>onBlur</code> of the input and when the user submits the form.</p></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>onBlur</code>&nbsp; <strong>function&nbsp;</strong><p>A function that is called and passes the value when the field loses focus.</p></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>onFocus</code>&nbsp; <strong>function&nbsp;</strong><p>A function that is called and passed the value when the field gets focused.</p></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>min</code>&nbsp; <strong>object&nbsp;</strong><p>Sets the earliest valid date available using the following format:</p><p><code>{ year: number;</code><code>month: number;</code><code>date: number }</code></p><ul><li><code>year</code>: the four-digit year (e.g., <code>2023</code>).</li><li><code>month</code>: starting at <code>0</code>, the number of the month (e.g., <code>0</code> = January, <code>11</code> = December).</li><li><code>date</code>: the number of the day (e.g., <code>1</code> = the first day of the month).</li></ul></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>max</code>&nbsp; <strong>object&nbsp;</strong><p>A Sets the latest valid date available using the following format:</p><p><code>{ year: number;</code><code>month: number;</code><code>date: number }</code></p><ul><li><code>year</code>: the four-digit year (e.g., <code>2023</code>).</li><li><code>month</code>: starting at <code>0</code>, the number of the month (e.g., <code>0</code> = January, <code>11</code> = December).</li><li><code>date</code>: the number of the day (e.g., <code>1</code> = the first day of the month).</li></ul></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>minValidationMessage</code>&nbsp; <strong>string&nbsp;</strong><p>A function that is called and passed the value when the field gets focused.</p></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>maxValidationMessage</code>&nbsp; <strong>string&nbsp;</strong><p>A function that is called and passed the value when the field gets focused.</p></td></tr><tr style="height: 431.672px;"><td style="padding: 4px; width: 99.7%; height: 432px;"><code>format</code>&nbsp; <strong>string&nbsp;</strong><p>Sets the date format the input will display. Can be one of:</p><ul><li><code>short</code> (default): <span>09/04/1986</span></li><li><code>long</code>: <span>September 4, 1986</span></li><li><code>medium</code>: <span>Sep 4, 1986</span></li><li><code>standard</code>: <span>1986-09-04</span></li><li><code>YYYY-MM-DD</code>: <span>1986-09-04</span></li><li><code>L</code>: <span>09/04/1986</span></li><li><code>LL</code>: <span>September 4, 1986</span></li><li><code>ll</code>: <span>Sep 4, 1986</span></li></ul></td></tr><tr style="height: 191.672px;"><td style="padding: 4px; width: 99.7%; height: 192px;"><code>timezone</code>&nbsp; <strong>string&nbsp;</strong><p>Sets the timezone that the component will use to calculate valid dates. Can be one of:</p><ul><li><code>userTz</code> (default): the user's time zone.</li><li><code>portalTz</code>: the portal's default time zone.</li></ul></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>clearButtonLabel</code>&nbsp; <strong>string&nbsp;</strong><p>Sets the label of the button to clear the selected date. <code>Clear</code> by default.</p></td></tr><tr style="height: 96px;"><td style="padding: 4px; width: 99.7%; height: 96px;"><code>todayButtonLabel</code>&nbsp; <strong>string&nbsp;</strong><p>Sets the label of the button to select today's date. <code>Today</code> by default.</p></td></tr></tbody></table>

function RemoteApp() { const \[dateValue, setDateValue\] = useState(null); return ( <Flex direction="column"> <DateInput label="Appointment Date Partially Controlled" name="date" onChange={(value) => { setDateValue(value); }} value={dateValue} format="YYYY-MM-DD" /> <DateInput label="Appointment Date Uncontrolled" name="appointment-date" format="standard" /> </Flex> ); }

### Input[](https://developers.hubspot.com/docs/platform/ui-extension-components#input)

The `Input` component renders a text input field where a user can enter a custom text value.

![ui-extension-component-input-with-typed-password](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-component-input-with-typed-password.png?width=500&height=237&name=ui-extension-component-input-with-typed-password.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>name</code>&nbsp; <strong>string </strong>(required)<p>The input's unique identifier, similar to the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name" rel="noopener">HTML input element <code>name</code> attribute</a>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>label</code>&nbsp; <strong>string </strong>(required)<p>The text that displays above the input. Required if <code>inputType</code> is not set to <code>hidden</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>required</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, displays a required indicator.</p></td></tr><tr><td style="padding: 10px 4px;"><code>value</code>&nbsp; <strong>string&nbsp;</strong><p>The value of the input.</p></td></tr><tr><td style="padding: 10px 4px;"><code>type</code>&nbsp; <strong>string&nbsp;</strong><p>The type of input. Can be either <code>text</code> (default) or <code>password</code>. An input with the <code>password</code> type will hide the characters that the user types.</p></td></tr><tr><td style="padding: 10px 4px;"><code>readOnly</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, sets the field as read-only on the CRM record, and users will not be able to fill the input field.</p></td></tr><tr><td style="padding: 10px 4px;"><code>description</code>&nbsp; <strong>string&nbsp;</strong><p>Displayed text that describes the field's purpose.</p></td></tr><tr><td style="padding: 10px 4px;"><code>tooltip</code>&nbsp; <strong>string&nbsp;</strong><p>The text that displays in a tooltip next to the label.</p></td></tr><tr><td style="padding: 10px 4px;"><code>placeholder</code>&nbsp; <strong>string&nbsp;</strong><p>Text that appears in the input when no value is set.</p></td></tr><tr><td style="padding: 10px 4px;"><code>error</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, <code>validationMessage</code> is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left <code>false</code> (default), <code>validationMessage</code> is displayed as a success message.</p></td></tr><tr><td style="padding: 10px 4px;"><code>validationMessage</code>&nbsp; <strong>string&nbsp;</strong><p>The text to show if the input has an error.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onChange</code>&nbsp; <strong>function</strong><p>A callback function that is invoked when the value is committed. Currently, these are <code>onBlur</code> of the input and when the user submits the form.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onInput</code>&nbsp; <strong>function </strong>(required)<p>A function that is called and passes the value when the field is edited by the user. Should be used for validation. It's recommended that you don't use this value to update state (use <code>onChange</code> instead).</p></td></tr><tr><td style="padding: 10px 4px;"><code>onBlur</code>&nbsp; <strong>function&nbsp;</strong><p>A function that is called and passes the value when the field loses focus.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onFocus</code>&nbsp; <strong>function&nbsp;</strong><p>A function that is called and passed the value when the field gets focused.</p></td></tr></tbody></table>

import { useState } from 'react'; const Extension = () => { const \[name, setName\] = useState(''); const \[validationMessage, setValidationMessage\] = useState(''); const \[isValid, setIsValid\] = useState(true); return ( <Form> <Input label="First Name" name="first-name" tooltip="Please enter your first name" description="Please enter your first name" placeholder="First name" required={true} error={!isValid} validationMessage={validationMessage} onChange={value => { setName(value); }} onInput={value => { if (value !== 'Bill') { setValidationMessage('This form only works for people named Bill'); setIsValid(false); } else if (value === '') { setValidationMessage('First name is required'); setIsValid(false); } else { setValidationMessage('Valid first name!'); setIsValid(true); } }} /> <Input label="Password" name="password" description="Enter your password" placeholder="Password" onInput={() => {}} type="password" /> </Form> ); };

### Multi-select input[](https://developers.hubspot.com/docs/platform/ui-extension-components#multi-select-input)

The `MultiSelect` component renders a dropdown menu select field where a user can select multiple values. Commonly used within the [Form](#form) component. 

![ui-extensions-component-multiselect](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-component-multiselect.png?width=525&height=339&name=ui-extensions-component-multiselect.png) 

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>label</code>&nbsp; <strong>string <span style="font-weight: normal;">(required)</span></strong><p>The text that displays above to the dropdown menu.</p></td></tr><tr><td style="padding: 10px 4px;"><code>name</code>&nbsp; <strong>string <span style="font-weight: normal;">(required)</span></strong><p>The unique identifier for the select element.</p></td></tr><tr><td style="padding: 10px 4px;"><code>value</code>&nbsp; <strong>array</strong><p>The value of the select input.</p></td></tr><tr><td style="padding: 10px 4px;"><code>options</code>&nbsp; <strong>array </strong><span style="font-weight: normal;">(required)</span><p>The options to display in the dropdown menu. <code>label</code> will be used as the display text, and <code>value</code> should be the option's unique identifier, which is submitted with the form.</p></td></tr><tr><td style="padding: 4px;"><code>required</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, displays a required field indicator.</p></td></tr><tr><td style="padding: 4px;"><code>readOnly</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, sets the field as read-only on the CRM record, and users will not be able to fill the input field.</p></td></tr><tr><td style="padding: 4px;"><code>description</code>&nbsp; <strong>string&nbsp;</strong><p>Displayed text that describes the field's purpose.</p></td></tr><tr><td style="padding: 4px;"><code>tooltip</code>&nbsp; <strong>string&nbsp;</strong><p>The text that displays in a tooltip next to the label.</p></td></tr><tr><td style="padding: 4px;"><code>placeholder</code>&nbsp; <strong>string&nbsp;</strong><p>Text that appears in the input when no value is set.</p></td></tr><tr><td style="padding: 4px;"><code>error</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, <code>validationMessage</code> is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left <code>false</code> (default), <code>validationMessage</code> is displayed as a success message.</p></td></tr><tr><td style="padding: 4px;"><code>validationMessage</code>&nbsp; <strong>string&nbsp;</strong><p>The text to show if the input has an error.</p></td></tr><tr><td style="padding: 4px;"><code>onChange</code>&nbsp; <strong>function</strong><p>A callback function that is invoked when the value is committed.&nbsp;</p></td></tr></tbody></table> 

function MultiSelectControlledExample() { const \[formValue, setFormValue\] = useState(\[\]); return ( <Form preventDefault={true} onSubmit={() => console.log(formValue, 'hola')}> <MultiSelect value={formValue} placeholder="Pick your Products" label="Select Mutiple Products" name="selectProduct" required={true} onChange={(value) => setFormValue(value)} options={\[ { label: 'Amazing Product 1', value: 'p1' }, { label: 'Amazing Product 2', value: 'p2' }, { label: 'Amazing Product 3', value: 'p3' }, { label: 'Amazing Product 4', value: 'p4' }, { label: 'Amazing Product 5', value: 'p5' }, { label: 'Amazing Product 6', value: 'p6' }, \]} /> <Button type="submit">Submit</Button> </Form> ); }

### Number input[](https://developers.hubspot.com/docs/platform/ui-extension-components#number-input)

The `NumberInput` component renders a number input field.

![ui-ext-numberinput](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-numberinput.png?width=400&height=123&name=ui-ext-numberinput.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>name</code>&nbsp; <strong>string </strong>(required)<p>The input's unique identifier, similar to the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name" rel="noopener">HTML input element <code>name</code> attribute</a>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>label</code>&nbsp; <strong>string </strong>(required)<p>The text that displays above the input. Required if <code>inputType</code> is not set to <code>hidden</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>required</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, displays a required indicator.</p></td></tr><tr><td style="padding: 10px 4px;"><code>value</code>&nbsp; <strong>string&nbsp;</strong><p>The value of the input.</p></td></tr><tr><td style="padding: 10px 4px;"><code>readOnly</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, sets the field as read-only on the CRM record, and users will not be able to fill the input field.</p></td></tr><tr><td style="padding: 10px 4px;"><code>description</code>&nbsp; <strong>string&nbsp;</strong><p>Displayed text that describes the field's purpose.</p></td></tr><tr><td style="padding: 10px 4px;"><code>tooltip</code>&nbsp; <strong>string&nbsp;</strong><p>The text that displays in a tooltip next to the label.</p></td></tr><tr><td style="padding: 10px 4px;"><code>placeholder</code>&nbsp; <strong>string&nbsp;</strong><p>Text that appears in the input when no value is set.</p></td></tr><tr><td style="padding: 10px 4px;"><code>error</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, <code>validationMessage</code> is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left <code>false</code> (default), <code>validationMessage</code> is displayed as a success message.</p></td></tr><tr><td style="padding: 10px 4px;"><code>validationMessage</code>&nbsp; <strong>string&nbsp;</strong><p>The text to show if the input has an error.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onChange</code>&nbsp; <strong>function</strong><p>A callback function that is invoked whenever a valid number is entered. The function is invoked with the current numerical value of the input.<br><br>Entering a non-numerical character will not invoke the function. But following that character with a valid number will call the function with the field's current numerical value without the invalid character. For example, entering <code>1d4</code> as separate characters will result in the following:</p><ul><li>After entering <code>1</code>: the function is invoked with <code>1</code>.</li><li>After entering <code>d</code>: the function is not invoked.</li><li>After entering <code>4</code>: the function is invoked with <code>14</code>.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>onBlur</code>&nbsp; <strong>function&nbsp;</strong><p>A function that is called and passes the value when the field loses focus.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onFocus</code>&nbsp; <strong>function&nbsp;</strong><p>A function that is called and passed the value when the field gets focused.</p></td></tr><tr><td style="padding: 10px 4px;"><code>min</code>&nbsp; <strong>number&nbsp;</strong><p>Sets the lower bound of the input.</p></td></tr><tr><td style="padding: 10px 4px;"><code>max</code>&nbsp; <strong>number&nbsp;</strong><p>Sets the upper bound of the input.</p></td></tr><tr><td style="padding: 10px 4px;"><code>precision</code>&nbsp;&nbsp;<strong>number&nbsp;</strong><p>Sets the number of digits to the right of the decimal point.</p></td></tr><tr><td style="padding: 10px 4px;"><code>formatStyle</code>&nbsp; <strong>string&nbsp;</strong><p>Formats the input as a decimal point (<code>decimal</code>) or percentage (<code>percentage</code>).</p></td></tr></tbody></table>

const Extension = () => { const \[portalCount, setPortalCount\] = useState(0); return ( <NumberInput label={'HubSpot Portal Count'} name="portalsNumber" description={'Number of active portals'} placeholder={'number of portals'} value={portalCount} onChange={value => setPortalCount(value)} /> ); };

### Radio button[](https://developers.hubspot.com/docs/platform/ui-extension-components#radio-button)

The `RadioButton` component renders a radio select button. If you want to include more than two radio buttons, or are building a form, it's recommended to use the [ToggleGroup](#toggle-group) component instead.

![ui-extensions-component-radio-buttons](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-component-radio-buttons.png?width=350&height=166&name=ui-extensions-component-radio-buttons.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 4px;"><code>value</code>&nbsp; <strong>string</strong><p>The radio button value. This value is not displayed, but is passed on the server side when submitted, along with the checkbox name.</p></td></tr><tr><td style="padding: 4px;"><code>name</code>&nbsp; <strong>string</strong><p>The radio button's unique identifier.</p></td></tr><tr><td style="padding: 4px;"><code>checked</code>&nbsp;&nbsp;<strong>boolean&nbsp;</strong><p>When set to <code>true</code>, the radio button is selected by default. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 4px;"><code>initialIsChecked</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, the radio button is selected by default. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 4px;"><code>readonly</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, users cannot select the radio button. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 4px;"><code>description</code>&nbsp; <strong>string&nbsp;</strong><p>The string that displays below the radio button.</p></td></tr><tr><td style="padding: 4px;"><code>variant</code>&nbsp; <strong>string&nbsp;</strong><p>The size of the checkbox. Values include:</p><ul><li><code>sm</code>, <code>small</code></li><li><code>default</code></li></ul></td></tr><tr><td style="padding: 4px;"><code>inline</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, arranges radio buttons side by side. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 4px;"><code>onChange</code>&nbsp; <strong>function</strong><p>A callback function that is called when the radio button is selected. Passes the new value.</p><p><code>(checked: boolean, value: string) =&gt; void;</code></p></td></tr></tbody></table>

function Extension() { const \[roleType, setRoleType\] = useState( 'support' ); return ( <> <RadioButton checked={roleType === 'superAdmin'} name="roleType" description="Select to grant superpowers." onChange={() => { setRoleType('superAdmin'); }} > Super Admin </RadioButton> <RadioButton checked={roleType === 'support'} name="roleType" description="Select to assign a Support role." onChange={() => { setRoleType('support'); }} > Customer Support </RadioButton> </> ); }

### Select input[](https://developers.hubspot.com/docs/platform/ui-extension-components#select-input)

The `Select` component renders a dropdown select input field where a user can select a single value. When there are more than seven selectable options in the input, the component will automatically include a search field. Commonly used within the [Form](#form) component. 

Using the `variant` prop, you can render the input with standard styling or transparent styling:

*   `variant="input"` (default):  
    ![ui-extension-components-input-selelect-input-variant](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-input-selelect-input-variant.png?width=537&height=273&name=ui-extension-components-input-selelect-input-variant.png)
*   `variant="transparent"`: 

![ui-extension-components-input-selelect-transparent-variant](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-input-selelect-transparent-variant.png?width=286&height=271&name=ui-extension-components-input-selelect-transparent-variant.png) 

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 4px;"><code>name</code>&nbsp; <strong>string </strong>(required)<p>The input's unique identifier, similar to the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name" rel="noopener">HTML input element <code>name</code> attribute</a>.</p></td></tr><tr><td style="padding: 4px;"><code>label</code>&nbsp; <strong>string </strong>(required)<p>The text that displays above the input. Required if <code>inputType</code> is not set to <code>hidden</code>.</p></td></tr><tr><td style="padding: 4px;"><code>required</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, displays a required indicator.</p></td></tr><tr><td style="padding: 4px;"><code>value</code>&nbsp; <strong>string&nbsp;</strong><p>The value of the input.</p></td></tr><tr><td style="padding: 4px;"><code>readOnly</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, sets the field as read-only on the CRM record, and users will not be able to fill the input field.</p></td></tr><tr><td style="padding: 4px;"><code>description</code>&nbsp; <strong>string&nbsp;</strong><p>Displayed text that describes the field's purpose.</p></td></tr><tr><td style="padding: 4px;"><code>tooltip</code>&nbsp; <strong>string&nbsp;</strong><p>The text that displays in a tooltip next to the label.</p></td></tr><tr><td style="padding: 4px;"><code>placeholder</code>&nbsp; <strong>string&nbsp;</strong><p>Text that appears in the input when no value is set.</p></td></tr><tr><td style="padding: 4px;"><code>error</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, <code>validationMessage</code> is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left <code>false</code> (default), <code>validationMessage</code> is displayed as a success message.</p></td></tr><tr><td style="padding: 4px;"><code>validationMessage</code>&nbsp; <strong>string&nbsp;</strong><p>The text to show if the input has an error.</p></td></tr><tr><td style="padding: 4px;"><code>onChange</code>&nbsp; <strong>function</strong><p>A callback function that is invoked when the value is committed. Currently, these are <code>onBlur</code> of the input and when the user submits the form.</p></td></tr><tr><td style="padding: 4px;"><code>options</code>&nbsp; <strong>array</strong><p>An array of options to display in the dropdown menu. Each object in the array contains:</p><ul><li><code>label</code>: the text that displays in the dropdown menu.</li><li><code>value</code>: the unique value that is submitted with the form.</li></ul></td></tr><tr><td style="padding: 4px;"><code>variant</code>&nbsp; <strong>string</strong><p>The type of input, which controls its appearance. Values include:</p><ul><li><code>input</code> (default): the standard select input, including a grey background and border.</li><li><code>transparent</code>: removes the background and border from the input. The input will render as a blue hyperlink with an arrow.</li></ul></td></tr></tbody></table>

const Extension = () => { const \[name, setName\] = useState(null); const \[validationMessage, setValidationMessage\] = useState(''); const \[isValid, setIsValid\] = useState(true); const options = \[ { label: 'Bill', value: 42 }, { label: 'Ted', value: 43 }, \]; return ( <Form> <Select label="Best Bill & Ted Character?" name="best-char" tooltip="Please choose" description="Please choose" placeholder="Bill or Ted?" required={true} error={!isValid} validationMessage={validationMessage} onChange={value => { setName(value); if (!value) { setValidationMessage('This is required'); setIsValid(false); } else { setValidationMessage('Excellent!'); setIsValid(true); } }} options={options} /> </Form> ); };

### Stepper input[](https://developers.hubspot.com/docs/platform/ui-extension-components#stepper-input)

The `StepperInput` component renders a number input field that can be increased or decreased by a set number. This component inherits many of its props from the `NumberInput` component, with an additional set of props to control the increase/decrease interval.

![ui-extension-component-stepper-input](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extension-component-stepper-input.gif?width=672&height=209&name=ui-extension-component-stepper-input.gif)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>name</code>&nbsp; <strong>string </strong>(required)<p>The input's unique identifier, similar to the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name" rel="noopener">HTML input element <code>name</code> attribute</a>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>label</code>&nbsp; <strong>string </strong>(required)<p>The text that displays above the input. Required if <code>inputType</code> is not set to <code>hidden</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>stepSize</code>&nbsp; <strong>number</strong><p>The amount that the current value will increase or decrease by. By default, set to <code>1</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>maxValueReachedTooltip</code>&nbsp; <strong>string&nbsp;</strong><p>When the maximum value (<code>max</code>) has been reached, this text will display in a tooltip when hovering over the increase button.&nbsp;</p></td></tr><tr><td style="padding: 10px 4px;"><code>minValueReachedTooltip</code>&nbsp; <strong>string</strong><p>When the minimum value (<code>min</code>) has been reached, this text will display in a tooltip when hovering over the increase button.</p></td></tr><tr><td style="padding: 10px 4px;"><code>min</code>&nbsp; <strong>number&nbsp;</strong><p>Sets the lower bound of the input.</p></td></tr><tr><td style="padding: 10px 4px;"><code>max</code>&nbsp; <strong>number&nbsp;</strong><p>Sets the upper bound of the input.</p></td></tr><tr><td style="padding: 10px 4px;"><code>required</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, displays a required indicator.</p></td></tr><tr><td style="padding: 10px 4px;"><code>value</code>&nbsp; <strong>string&nbsp;</strong><p>The value of the input.</p></td></tr><tr><td style="padding: 10px 4px;"><code>readOnly</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, sets the field as read-only on the CRM record, and users will not be able to fill the input field.</p></td></tr><tr><td style="padding: 10px 4px;"><code>description</code>&nbsp; <strong>string&nbsp;</strong><p>Displayed text that describes the field's purpose.</p></td></tr><tr><td style="padding: 10px 4px;"><code>tooltip</code>&nbsp; <strong>string&nbsp;</strong><p>The text that displays in a tooltip next to the label.</p></td></tr><tr><td style="padding: 10px 4px;"><code>placeholder</code>&nbsp; <strong>string&nbsp;</strong><p>Text that appears in the input when no value is set.</p></td></tr><tr><td style="padding: 10px 4px;"><code>error</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, <code>validationMessage</code> is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left <code>false</code> (default), <code>validationMessage</code> is displayed as a success message.</p></td></tr><tr><td style="padding: 10px 4px;"><code>validationMessage</code>&nbsp; <strong>string&nbsp;</strong><p>The text to show if the input has an error.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onChange</code> &nbsp;<strong>(value: number) =&gt; void;</strong><p>A callback function that is invoked whenever a valid number is entered. The function is invoked with the current numerical value of the input.<br><br>Entering a non-numerical character will not invoke the function. But following that character with a valid number will call the function with the field's current numerical value without the invalid character. For example, entering <code>1d4</code> as separate characters will result in the following:</p><ul><li>After entering <code>1</code>: the function is invoked with <code>1</code>.</li><li>After entering <code>d</code>: the function is not invoked.</li><li>After entering <code>4</code>: the function is invoked with <code>14</code>.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>onBlur</code> &nbsp;<strong>(value: number) =&gt; void;</strong><p>A function that is called and passes the value when the field loses focus.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onFocus</code> &nbsp;<strong>(value: number) =&gt; void;</strong><strong>&nbsp;</strong><p>A function that is called and passed the value when the field gets focused.</p></td></tr><tr><td style="padding: 10px 4px;"><code>precision</code>&nbsp;&nbsp;<strong>number&nbsp;</strong><p>Sets the number of digits to the right of the decimal point.</p></td></tr><tr><td style="padding: 10px 4px;"><code>formatStyle</code>&nbsp; <strong>string&nbsp;</strong><p>Formats the input as a decimal point (<code>decimal</code>) or percentage (<code>percentage</code>).</p></td></tr></tbody></table>

return ( <StepperInput min={5} max={20} minValueReachedTooltip="You need to eat at least 5 cookies." maxValueReachedTooltip="More than 20 cookies is a bit much." label="Number of cookies to eat" name="cookiesField" description={'I want cookies'} value={cookies} stepSize={5} onChange={(value) => { setCookieCount(value); }} /> );

### Text area input[](https://developers.hubspot.com/docs/platform/ui-extension-components#text-area-input)

The `TextArea` component renders a fillable text field. You can customize the size of the field along with maximum number of characters and resizability.

![ui-ext-components-textarea](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-textarea.png?width=486&height=120&name=ui-ext-components-textarea.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 4px; width: 100.018%;"><code>name</code>&nbsp; <strong>string </strong>(required)<p>The input's unique identifier, similar to the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name" rel="noopener">HTML input element <code>name</code> attribute</a>.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>label</code>&nbsp; <strong>string </strong>(required)<p>The text that displays above the input. Required if <code>inputType</code> is not set to <code>hidden</code>.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>required</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, displays a required indicator.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>value</code>&nbsp; <strong>string&nbsp;</strong><p>The value of the input.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>readOnly</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, sets the field as read-only on the CRM record, and users will not be able to fill the input field.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>description</code>&nbsp; <strong>string&nbsp;</strong><p>Displayed text that describes the field's purpose.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>tooltip</code>&nbsp; <strong>string&nbsp;</strong><p>The text that displays in a tooltip next to the label.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>placeholder</code>&nbsp; <strong>string&nbsp;</strong><p>Text that appears in the input when no value is set.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>error</code>&nbsp; <strong>boolean</strong><p>When set to <code>true</code>, <code>validationMessage</code> is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left <code>false</code> (default), <code>validationMessage</code> is displayed as a success message.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>validationMessage</code>&nbsp; <strong>string&nbsp;</strong><p>The text to show if the input has an error.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>onChange</code>&nbsp; <strong>function</strong><p>A callback function that is invoked when the value is committed. Currently, these are <code>onBlur</code> of the input and when the user submits the form.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>onInput</code>&nbsp; <strong>function </strong>(required)<p>A function that is called and passes the value when the field is edited by the user. Should be used for validation. It's recommended that you don't use this value to update state (use <code>onChange</code> instead).</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>onBlur</code>&nbsp; <strong>function&nbsp;</strong><p>A function that is called and passes the value when the field loses focus.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>onFocus</code>&nbsp; <strong>function&nbsp;</strong><p>A function that is called and passed the value when the field gets focused.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>cols</code>&nbsp; <strong>number&nbsp;</strong><p>The visible width of the text field in average character widths.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>rows</code>&nbsp; <strong>number&nbsp;</strong><p>The number of visible text lines for the text field.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>maxLength</code>&nbsp; <strong>number&nbsp;</strong><p>The maximum number of characters (UTF-16 code units) that the user can enter. If not specified, the max length is unlimited.</p></td></tr><tr><td style="padding: 4px; width: 100.018%;"><code>resize</code>&nbsp; <strong>string&nbsp;</strong><p>Sets whether the element is resizable, and if so in which directions. Can be one of:</p><ul><li><code>vertical</code></li><li><code>horizontal</code></li><li><code>both</code></li><li><code>none</code></li></ul></td></tr></tbody></table>

import { useState } from 'react'; const Extension = () => { const \[description, setDescription\] = useState(''); const \[validationMessage, setValidationMessage\] = useState(''); const \[isValid, setIsValid\] = useState(true); return ( <Form> <TextArea label="Description" name="description" tooltip="Provide as much detail as possible" description="Please include a link" placeholder="My description" required={true} error={!isValid} validationMessage={validationMessage} onChange={value => { setDescription(value); }} onInput={value => { if (!value.includes('http')) { setValidationMessage('A link must be included.'); setIsValid(false); } else { setValidationMessage('Valid description!'); setIsValid(true); } }} /> </Form> ); };

### Toggle[](https://developers.hubspot.com/docs/platform/ui-extension-components#toggle)

The `Toggle` component renders a boolean toggle switch that can be configured with sizing, label position, read-only, and more.

![ui-extension-toggle](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-toggle.png?width=250&height=439&name=ui-extension-toggle.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 99.9156%;"><tbody><tr><td style="padding: 10px 4px; width: 100%;"><code>label</code> &nbsp;<strong>string</strong> (required)<p>The toggle's label. By default, the label will display inline to the left of the switch. You can use the <code>labelDisplay</code> prop to further configure the label.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>labelDisplay</code> &nbsp;<strong>string</strong>&nbsp;<p>The display option for the toggle label. Values include:</p><ul><li><code>inline</code> (default): the label appears inline to the left of the switch.</li><li><code>top</code>: the label appears above the switch.</li><li><code>hidden</code>: the label is hidden.</li></ul></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>checked</code> &nbsp;<strong>boolean</strong>&nbsp;<p>When set to <code>true</code>, the toggle is checked and displays a blue enabled state. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>readonly</code> &nbsp;<strong>boolean</strong>&nbsp;<p>When set to <code>true</code>, the toggle is set to read-only, appearing greyed out and unable to be interacted with by users.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>name</code> &nbsp;<strong>string</strong>&nbsp;<p>The internal name of the toggle.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>size</code> &nbsp;<strong>string</strong>&nbsp;<p>The size of the toggle. Values include:</p><ul><li><code>xs</code>, <code>extra-small</code></li><li><code>sm</code>, <code>small</code></li><li><code>md</code>, <code>medium</code> (default)</li></ul><p>Note that only <code>md</code>/ <code>medium</code> sized toggles can display text on the toggle (<em>ON</em>,&nbsp;<em>OFF</em>). All other sizes will hide checked/unchecked text.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>onChange</code>&nbsp; <span style="font-weight: bold;">(checked: boolean) =&gt; void;</span><br>&nbsp;<br>A function that is invoked when the toggle is clicked.</td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>initialIsChecked</code> &nbsp;<strong>boolean</strong>&nbsp;<p>When set to <code>true</code>, the toggle is checked by default. Default is <code>false</code>.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>textChecked</code> &nbsp;<strong>string</strong>&nbsp;<p>The text that displays on the toggle when checked. Default is <em>ON</em>. Extra small and small toggles will not display any text.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>textUnchecked</code> &nbsp;<strong>string</strong>&nbsp;<p>The text that displays on the toggle when not checked. Default is&nbsp;<em>OFF</em>. Extra small and small toggles will not display any text.</p></td></tr></tbody></table>

const Extension = () => { return ( <Toggle size="sm" label="My toggle" labelDisplay="top" initialIsChecked={true} /> ); };

### Toggle group[](https://developers.hubspot.com/docs/platform/ui-extension-components#toggle-group)

The `ToggleGroup` component renders a list of selectable options.

![ui-ext-components-togglegroup](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-togglegroup.png?width=262&height=294&name=ui-ext-components-togglegroup.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>name</code> &nbsp;<strong>string</strong> (required)<p>The unique identifier for the toggle group element.</p></td></tr><tr><td style="padding: 10px 4px;"><code>label</code> &nbsp;<strong>string</strong> (required)<p>The label that displays above the toggle group.</p></td></tr><tr><td style="padding: 10px 4px;"><code>toggleType</code> &nbsp;<strong>string</strong> (required)<p>The type of toggle group. Can be one of:</p><ul><li><code>radioButtonList</code>: options will render as radio buttons. Only allows for one option to be selected.</li><li><code>checkboxList</code>: options will render as checkboxes. Allows for multiple options to be selected.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>error</code> &nbsp;<strong>boolean</strong><p>When set to <code>true</code>, <code>validationMessage</code> is displayed as an error message if provided. The input will also render its error state to let the user know there is an error. If left <code>false</code>, <code>validationMessage</code> is displayed as a success message.</p></td></tr><tr><td style="padding: 10px 4px;"><code>options</code> &nbsp;<strong>array</strong> (required)<p>An array of options to display in the dropdown menu. Each object in the array contains:</p><ul><li><code>label</code> (string): the text that displays next to the checkbox.</li><li><code>value</code> (string): the unique value that is submitted with the form.</li><li><code>initialIsChecked</code> (boolean): when set to <code>true</code>, the option will be selected by default.</li><li><code>readonly</code> (boolean): when set to <code>true</code>, the option cannot be selected.</li><li><code>description</code>: the string that displays below the toggle.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>value</code> &nbsp;<strong>string</strong>&nbsp;<p>The value of the toggle group.</p><ul><li>If <code>toggleType</code> is <code>radioButtonList</code>, this should be a string.</li><li>If <code>toggleType</code> is <code>checkboxList</code>, this should be an array of strings.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>onChange</code> &nbsp;<strong>function</strong> (required)<p>A function that is called with the new value or values when it's updated.</p><ul><li>If <code>toggleType</code> is <code>radioButtonList</code>, the function will be called with the value that is a string.</li><li>If <code>toggleType</code> is <code>checkboxList</code>, the function will be called with the value that is an array of strings.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>required</code> &nbsp;<strong>boolean</strong>&nbsp;<p>When set to <code>true</code>, displays a required indicator next to the toggle group.</p></td></tr><tr><td style="padding: 10px 4px;"><code>tooltip</code> &nbsp;<strong>string</strong>&nbsp;<p>Text that will appear in a tooltip next to the toggle group label.</p></td></tr><tr><td style="padding: 10px 4px;"><code>validationMessage</code> &nbsp;<strong>string</strong><p>The text to display if the input has an error.</p></td></tr><tr><td style="padding: 10px 4px;"><code>inline</code> &nbsp;<strong>boolean</strong><p>When set to <code>true</code>, stacks the options horizontally.</p></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code> &nbsp;<strong>string</strong>&nbsp;<p>The size variation of the individual options. Can be one of <code>default</code> (default) or <code>small</code>.</p></td></tr></tbody></table>

const options = \[1, 2, 3, 4\].map(n => ({ label: \`Option ${n}\`, value: \`${n}\`, initialIsChecked: n === 2, readonly: false, description: \`This is option ${n}\`, })); const Extension = () => { return ( <ToggleGroup name="toggle-checkboxes" label="Toggle these things" error={false} options={options} tooltip="Here's a secret tip." validationMessage="Make sure you do the thing correctly." required={false} inline={false} toggleType="checkboxList" variant="default" /> ); };

### Link[](https://developers.hubspot.com/docs/platform/ui-extension-components#link)

The `Link` component renders a clickable hyperlink.

![ui-ext-components-link](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-link.png?width=167&height=37&name=ui-ext-components-link.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>href</code>&nbsp; <strong>string</strong><p>The URL that will be opened on click. Links to pages in the HubSpot account will open in the same tab, while non-HubSpot links will open in a new tab.</p></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code>&nbsp; <strong>string&nbsp;</strong><p>The color variation of the link. Can be one of:</p><ul><li><code>primary</code> (default)</li><li><code>light</code></li><li><code>dark</code></li><li><code>destructive</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>onClick</code>&nbsp; <strong>function</strong><p>A function that will be invoked with the link is clicked. The function receives no arguments and its return value is ignored.</p></td></tr><tr><td style="padding: 10px 4px;"><code>preventDefault</code> &nbsp;<strong>boolean</strong><p>When set to <code>true</code>, <code>event.preventDefault()</code> will be invoked before the <code>onClick</code> function is called, preventing automatic navigation to the <code>href</code> URL.</p></td></tr></tbody></table>

const Extension = () => { return <Link href="https://app.hubspot.com/">HubSpot</Link>; };

### List[](https://developers.hubspot.com/docs/platform/ui-extension-components#list)

The `List` component renders a list of items. Each item in `List` will be wrapped in `<li>` tags. A list can be styled as inline, ordered, or unordered with the `variant` prop.

![ui-extension-component-list](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-component-list.png?width=300&height=543&name=ui-extension-component-list.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>variant</code>&nbsp; <strong>string</strong><p>The type of list to render.</p><ul><li><code>unordered</code> (default): an unordered list without bullet points.</li><li><code>unordered-styled</code>: an unordered list with bullet points.</li><li><code>ordered</code>: an ordered list without numbers.</li><li><code>ordered-styled</code>: an unordered list without numbers.</li><li><code>inline</code>: an inline list (items are on one line).</li><li><code>inline-divided</code>: an inline list with vertical dividers between each item.</li></ul></td></tr></tbody></table>

const Extension() { return ( <List variant="unordered-styled"> <Link href="www.hubspot.com">List item 1</Link> <Link href="www.developers.hubspot.com">List item 2</Link> <Link href="www.knowledge.hubspot.com">List item 3</Link> </List> ); }

### Layout: Flex[](https://developers.hubspot.com/docs/platform/ui-extension-components#layout-flex)

The `Flex` component renders an empty `div` container set to `display=flex`. When wrapped around other components, this enables those child components to be arranged using props. `Flex` can contain other `Flex` or `Box` components. Learn more about [configuring UI extension layout](/docs/platform/manage-ui-extension-layout).

![ui-extension-components-flex-child](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-flex-child.png?width=521&height=207&name=ui-extension-components-flex-child.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>direction</code>&nbsp; <strong>string</strong><p>Arranges components horizontally or vertically by setting the main axis. Can be one of:</p><ul><li><code>row</code> (default)</li><li><code>column</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>justify</code>&nbsp; <strong>string&nbsp;</strong><p>Distributes components along the main axis using the available free space. Can be one of:</p><ul><li><code>center</code></li><li><code>start</code><span>&nbsp;</span>(default)</li><li><code>end</code></li><li><code>around</code></li><li><code>between</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>align</code>&nbsp; <strong>string&nbsp;</strong><p>Distributes components along the cross-axis using the available free space. Can be one of:</p><ul><li><code>start</code></li><li><code>center</code></li><li><code>baseline</code></li><li><code>end</code></li><li><code>stretch</code><span>&nbsp;</span>(default)</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>alignSelf</code>&nbsp; <strong>string&nbsp;</strong><p>Distributes a child component along the cross-axis using the available free space. Use this prop for nested child <code>Flex</code> and <code>Box</code> components to align them differently from other child components in the <code>Flex</code> group. Can be one of:</p><ul><li><code>start</code></li><li><code>center</code></li><li><code>baseline</code></li><li><code>end</code></li><li><code>stretch</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>wrap</code>&nbsp; <strong>string&nbsp;</strong><p>Whether components will wrap instead of trying to fit on one line. Can be one of:</p><ul><li><code>wrap</code></li><li><code>nowrap</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>gap</code>&nbsp; <strong>string&nbsp;</strong><p>Sets the spacing between components. Can be one of:&nbsp;</p><ul><li><code>flush</code><span>&nbsp;</span>(default)</li><li><code>extra-small</code></li><li><code>small</code></li><li><code>medium</code></li><li><code>large</code></li><li><code>extra-large</code></li></ul></td></tr></tbody></table>

const Extension = () => { return ( <Flex direction={'row'} justify={'end'} wrap={'wrap'} gap={'small'} > <Tile>Left</Tile> <Tile>Right</Tile> <Flex direction={'column'}> <Tile>Bottom</Tile> </Flex> </Flex> ); };

### Layout: Box[](https://developers.hubspot.com/docs/platform/ui-extension-components#layout-box)

The `Box` component renders an empty `div` container, and can be wrapped around `Flex` child components. Use this component to fine tune spacing of individual components. Learn more about [configuring UI extension layout](/docs/platform/manage-ui-extension-layout).

![ui-extrensions-layout-box](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-box.png?width=521&height=226&name=ui-extrensions-layout-box.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>alignSelf</code>&nbsp; <strong>string&nbsp;</strong><p>Distributes a child component along the cross-axis using the available free space. Use this prop for nested child&nbsp;<code>Box</code> components to align them differently from other child components in the <code>Flex</code> group. Can be one of:</p><ul><li><code>start</code></li><li><code>center</code></li><li><code>baseline</code></li><li><code>end</code></li><li><code>stretch</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>flex</code>&nbsp; <strong>string&nbsp;</strong><p>Distributes components based on the available empty space around them. Can be one of:</p><ul><li>number value</li><li><code>initial</code> (default)</li><li><code>auto</code></li><li><code>none</code></li></ul></td></tr></tbody></table>

const Extension = () => { return ( <Flex direction={'row'} justify={'start'} gap={'small'} > <Box flex={1}> <Tile>flex = 1</Tile> </Box> <Box flex={2}> <Tile>flex = 2</Tile> </Box> <Box flex={3}> <Tile>flex = 3</Tile> </Box> <Box flex={4}> <Tile>flex = 4</Tile> </Box> </Flex> ); };

### Loading spinner[](https://developers.hubspot.com/docs/platform/ui-extension-components#loading-spinner)

The `LoadingSpinner` component renders a spinner that indicates a loading state.

![2023-05-26_13-38-56 (1)](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/2023-05-26_13-38-56%20(1).gif?width=148&height=55&name=2023-05-26_13-38-56%20(1).gif) 

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>label</code>&nbsp; <strong>string</strong><p>The text that displays next to the spinner.</p></td></tr><tr><td style="padding: 10px 4px;"><code>showLabel</code>&nbsp; <strong>boolean&nbsp;</strong><p>When set to <code>true</code>, the <code>label</code> will appear next to the spinner. Value is <code>false</code> by default.</p></td></tr><tr><td style="padding: 10px 4px;"><code>size</code>&nbsp; <strong>string&nbsp;</strong><p>The size of the spinner. Can be one of:</p><ul><li><code>xs</code></li><li><code>sm</code> (default)</li><li><code>md</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>layout</code>&nbsp; <strong>string&nbsp;</strong><p>The position of the spinner. Can be one of <code>inline</code> or <code>centered</code>.</p></td></tr></tbody></table>

const Extension = () => { return ( <LoadingSpinner label="Loading..." /> ); };

### Panel[](https://developers.hubspot.com/docs/platform/ui-extension-components#panel)

The `Panel` component renders a panel on the right side of the page and contains other components. The panel can be opened and closed by using `onClick` handles for [Button](#button), [Link](#link), Tag, and [Image](#image) components. Learn more about [how to open a panel in your UI extension](/docs/platform/ui-extensions-sdk#open-a-panel). To see an example of incorporating a panel into an extension, check out HubSpot's [Build a multi-step flow sample project](/docs/platform/sample-projects#build-a-multi-step-flow).

![panel-example-gif](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/panel-example-gif.gif?width=700&height=595&name=panel-example-gif.gif)

The `Panel` component uses three subcomponents to control its design and content, which follows the general structure below:

*   `<Panel>`: the outermost container.  
    *   `<PanelBody>`: the container that wraps the panel's content and makes it scrollable. Include only one `PanelBody` per `Panel`.
        *   `<PanelSection>`: a container that adds padding and bottom margin to provide spacing between content. You can use [Flex](#layout-flex) and [Box](#layout-box) to further customize content layout.
    *   `<PanelFooter>`: a sticky footer component at the bottom of the panel. Include only one `PanelFooter` per `Panel`.

**Please note:**

*   Panels must be a top-level component. They cannot be contained within other components, such as `Flex`.
*   Only one panel can be open at a time. Opening a panel while another is already open will cause the first panel to close.
*   If your `onClick` function to open the panel is asynchronous, ensure that it returns a promise.

#### <Panel> props[](https://developers.hubspot.com/docs/platform/ui-extension-components#lt-panel-gt-props)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>id</code>&nbsp;<span>&nbsp;</span><strong>string&nbsp;</strong><span>(required)</span><p>A unique ID for the panel.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onOpen</code><span>&nbsp;</span>&nbsp;<span>() =&gt; void;&nbsp;</span><p>A function that will be invoked when the panel has finished opening.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onClose</code><span>&nbsp;</span>&nbsp;<span>() =&gt; void;</span><p>A function that will be invoked with the panel has finished closing.</p></td></tr><tr><td style="padding: 10px 4px;"><code>width</code>&nbsp;<span>&nbsp;</span><strong>string&nbsp;</strong><p>The width of the panel. Can be one of:</p><ul><li><code>sm</code>,<span>&nbsp;</span><code>small</code><span>&nbsp;</span>(default)</li><li><code>md</code>,<span>&nbsp;</span><code>medium</code></li><li><code>lg</code>,<span>&nbsp;</span><code>large</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>title</code>&nbsp;<span>&nbsp;</span><strong>string&nbsp;</strong><p>The title that displays at the top of the panel.</p></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code>&nbsp; '<strong>modal'&nbsp;</strong><span>&nbsp;</span>|<span>&nbsp;</span><strong>'default'</strong><p>The variant of the panel. The<span>&nbsp;</span><code>modal</code><span>&nbsp;</span>variant includes better screen reader focus on the panel and is recommended for visual and motor accessibility and tab navigation.</p></td></tr><tr><td style="padding: 10px 4px;"><code>aria-label</code>&nbsp;<span>&nbsp;</span><strong>string</strong><p>The panel's accessibility label.</p></td></tr></tbody></table>

#### <PanelSection> props[](https://developers.hubspot.com/docs/platform/ui-extension-components#lt-panelsection-gt-props)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>flush</code>&nbsp;<span>&nbsp;</span><strong>boolean&nbsp;</strong><p>When set to<span>&nbsp;</span><code>true</code>,<span>&nbsp;</span>the section will have no bottom margin. Default is<span>&nbsp;</span><code>false</code>.</p></td></tr></tbody></table>

<> <Panel title="Welcome to my Panel" id="my-panel"> <Form> <PanelBody> <PanelSection> <Select name="test" label="Test" options={\[ {label: 'foo', value: 'foo'}, {label:"bar", value: "bar"}\]} /> </PanelSection> <PanelSection> lorem ipsum... </PanelSection> </PanelBody> <PanelFooter><Button type="submit">Click me</Button></PanelFooter> </Form> </Panel> <Button onClick={(event, reactions) => { reactions.openPanel('my-panel')}}> Open Panel </Button> </>

### Progress bar[](https://developers.hubspot.com/docs/platform/ui-extension-components#progress-bar)

The `ProgressBar` component renders a progress bar that shows a numeric and/or percentage-based representation of progress. The percentage is calculated based on the maximum possible value specified in the component.![ui-ext-components-progressbar-description](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-progressbar-description.png?width=546&height=311&name=ui-ext-components-progressbar-description.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>title</code>&nbsp; <strong>string</strong><p>The text that displays above the progress bar.</p></td></tr><tr><td style="padding: 10px 4px;"><code>showPercentage</code>&nbsp; <strong>boolean&nbsp;</strong><p>Whether the progress bar displays the completion percentage.</p></td></tr><tr><td style="padding: 10px 4px;"><code>value</code>&nbsp; <strong>number&nbsp;</strong><p>The number representing the progress so far. Defaults to <code>0</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>maxValue</code>&nbsp; <strong>number&nbsp;</strong><p>The maximum value of the progress bar. Defaults to <code>100</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>valueDescription</code>&nbsp; <strong>string&nbsp;</strong><p>The text that explains the current state of the <code>value</code> property. For example, <code>"150 out of 250"</code>. Displays above the progress bar on the right side.</p></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code>&nbsp; <strong>string</strong><p>The color that indicates the type of progress bar. Can be one:</p><ul><li><code>success</code></li><li><code>danger</code></li><li><code>warning</code></li></ul></td></tr></tbody></table>

const Extension = () => { return ( <ProgressBar variant="warning" value={50} maxValue={200} showPercentage={true} /> ); };

### Statistics[](https://developers.hubspot.com/docs/platform/ui-extension-components#statistics)

The `Statistics` component renders data summaries via the `StatisticsItem` and `StatisticsTrend` child components.

![ui-ext-components-statistics](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-statistics.png?width=402&height=113&name=ui-ext-components-statistics.png)

#### StatisticsItem[](https://developers.hubspot.com/docs/platform/ui-extension-components#statisticsitem)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>id</code>&nbsp; <strong>string</strong><p>The unique identifier</p></td></tr><tr><td style="padding: 10px 4px;"><code>label</code>&nbsp; <strong>string</strong><p>The item's label text.</p></td></tr><tr><td style="padding: 10px 4px;"><code>number</code>&nbsp; <strong>string</strong><p>The string to be displayed as the item's primary number.</p></td></tr></tbody></table>

#### StatisticsTrend[](https://developers.hubspot.com/docs/platform/ui-extension-components#statisticstrend)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>value</code>&nbsp; <strong>string</strong><p>The text to be displayed as the trend value.</p></td></tr><tr><td style="padding: 10px 4px;"><code>direction</code>&nbsp; <strong>string</strong><p>The direction of the trend arrow. Can be one of <code>increase </code>or <code>decrease</code>.</p></td></tr></tbody></table>

const Extension = () => { return ( <Statistics> <StatisticsItem label="Item A Sales" number="10000"> <StatisticsTrend direction="decrease" value="200%" /> </StatisticsItem> <StatisticsItem label="Item B Sales" number="100000"> <StatisticsTrend direction="increase" value="100%" /> </StatisticsItem> </Statistics> ); };

### Step indicator[](https://developers.hubspot.com/docs/platform/ui-extension-components#step-indicator)

The `StepIndicator` component renders a horizontal indicator to show the current step of a multi-step process.

![ui-extension-component-stepindicator](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-component-stepindicator.png?width=1385&height=372&name=ui-extension-component-stepindicator.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>stepNames</code>&nbsp; <strong>array </strong><span style="font-weight: normal;">(required)</span><p>An array containing the name of each step.</p></td></tr><tr><td style="padding: 10px 4px;"><code>currentStep</code>&nbsp; <strong>number</strong><p>The currently active step.</p></td></tr><tr><td style="padding: 10px 4px;"><code>direction</code>&nbsp; <strong>string</strong><p>The orientation of the indicator. Can be one of <code>horizontal</code> or <code>vertical</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>onClick</code>&nbsp; <strong>function</strong><p>A function that will be invoked when a step in the indicator is clicked. The function receives the current step index as an argument (zero-based). Use this to update the currently active step.</p></td></tr><tr><td style="padding: 10px 4px;"><code>circleSize</code>&nbsp; <strong>string</strong><p>The size of the indicator circles. Can be one of:</p><ul><li><code>extra-small</code></li><li><code>small</code> (default)</li><li><code>medium</code></li><li><code>large</code></li><li><code>extra-large</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code>&nbsp; <strong>string</strong><p>The visual style of the component. Can be one of:</p><ul><li><code>default</code>: default spacing.</li><li><code>compact</code>: only shows the title of the currently active step.</li><li><code>flush</code>: only shows the title of the currently active step and removes left and right margins.</li></ul></td></tr></tbody></table>

function Extension() { const \[currentStep, setCurrentStep\] = useState(0); return ( <StepIndicator currentStep={currentStep} stepNames={\["First", "Second", "Third"\]} /> <Button onClick={() => setCurrentStep(currentStep - 1)}> Previous </Button> <Button onClick={() => setCurrentStep(currentStep + 1)}>Next</Button> ); }

### Table[](https://developers.hubspot.com/docs/platform/ui-extension-components#table)

The `Table` component renders a table. To format the table, you can use the following subcomponents:

*   `TableHead`: the header section of the table containing column labels.
*   `TableRow`: individual table rows.
*   `TableHeader`: cells containing bolded column labels. Use the `sortDirection` and `onSortChange` props to [make the table sortable](#sortable-tables).
*   `TableBody`: container for the main table contents (rows and cells).
*   `TableCell`: individual cells within the main body.

You can also configure pagination with the `pagination` prop.

![design-guidelines-table-paginated](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-table-paginated.png?width=533&height=445&name=design-guidelines-table-paginated.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100.018%;"><tbody><tr><td style="padding: 10px 4px; width: 100%;"><code>flush</code>&nbsp; <strong>boolean</strong>&nbsp;<p>When set to <code>true</code>, the table will not have bottom margin.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>bordered</code> &nbsp;<strong>boolean</strong>&nbsp;<p>When set to <code>false</code>, the table will not have borders.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>paginated</code> &nbsp;<strong>boolean</strong>&nbsp;<p>When set to <code>true</code>, the table will include pagination navigation. To configure pagination options, you'll need to configure the following pagination props:</p></td></tr><tr><td style="padding: 10px 4px 10px 22px; width: 100%;"><span>⮑</span> <code>pageCount</code> &nbsp;<strong>string</strong><p>The total number of pages available.</p></td></tr><tr><td style="padding: 10px 4px 10px 22px; width: 100%;"><span>⮑</span> <code>onPageChange</code> &nbsp;<strong>function</strong><p><span>A function that will be invoked when the pagination button is clicked. It receives the new page number as argument.</span></p><p><code><span>onPageChange: (pageNumber: number) =&gt; void</span></code></p></td></tr><tr><td style="padding: 10px 4px 10px 22px; width: 100%;"><span>⮑</span> <code>showButtonLabels</code> &nbsp;<strong>boolean</strong><p>When set to <code>false</code>, hides the text labels for the First/Prev/Next buttons. The button labels will still be accessible to screen readers.</p></td></tr><tr><td style="padding: 10px 4px 10px 22px; width: 100%;"><span>⮑</span> <code>showFirstLastButtons</code> &nbsp;<strong>boolean</strong><p>When set to <code>true</code>, displays the First/Last page buttons</p></td></tr><tr><td style="padding: 10px 4px 10px 22px; width: 100%;"><span>⮑</span> <code>maxVisiblePageButtons</code> &nbsp;<strong>number</strong><p>Sets how many page buttons are displayed.</p></td></tr><tr><td style="padding: 10px 4px 10px 22px; width: 100%;"><span>⮑</span> <code>page</code> &nbsp;<strong>number</strong><p>Denotes the current page.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>align</code> &nbsp;<strong>string</strong><p>Align <code>TableCell</code> and <code>TableHeader</code> subcomponents using <code>left</code>, <code>center</code>, or <code>right</code>.</p></td></tr><tr><td style="padding: 10px 4px; width: 100%;"><code>width</code> &nbsp;<strong>string</strong><p>Set the width of <code>TableCell</code> and <code>TableHeader</code> subcomponents with a specific pixel value or one of the following values:</p><ul><li><code>min</code>: the content will only be as wide as required, overflowing if the content is wider than the table. A horizontal scrollbar will appear when there is overflow.</li><li><code>max</code>: the content will expand to occupy the maximum available width without overflowing.</li><li><code>auto</code>: the content will adjust its width based on the available space without overflowing.</li></ul></td></tr></tbody></table> 

const Extension = () => { return ( <Table bordered={true} paginated={true} pageCount="5" > <TableHead> <TableRow> <TableHeader>Name</TableHeader> <TableHeader>Role</TableHeader> </TableRow> </TableHead> <TableBody> <TableRow> <TableCell>Tim Robinson</TableCell> <TableCell>Driver's Ed. Instructor</TableCell> </TableRow> <TableRow> <TableCell>Patti Harrison</TableCell> <TableCell>Tables (vendor)</TableCell> </TableRow> <TableRow> <TableCell>Sam Richardson</TableCell> <TableCell>Show host</TableCell> </TableRow> <TableRow> <TableCell>Ruben Rabasa</TableCell> <TableCell>Car imagineer</TableCell> </TableRow> </TableBody> </Table> ); }

#### Sortable tables

To add sorting functionality to a table, you can include the `sortDirection` and `onSortChange` props in the table's `TableHeader` components. To enable table data to dynamically reorder based on user input, you'll need to store your table data in variables rather than hard coding it into table cells. Below is an example of a sortable table with a static table footer.

![ui-extensions-sortable-table-1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-sortable-table-1.gif?width=484&height=362&name=ui-extensions-sortable-table-1.gif)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>sortDirection</code>&nbsp; <strong>string</strong>&nbsp;<p>Visually indicates with an arrow which way the rows are sorted. Values include:</p><ul><li><code>none</code> (default)</li><li><code>ascending</code></li><li><code>descending</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>onSortChange</code> &nbsp;<strong>function</strong>&nbsp;<p>A function that will be invoked when the header is clicked. It receives a <code>sortDirection</code> as an argument&nbsp;(cannot be <code>none</code> or a null value).</p></td></tr></tbody></table>

hubspot.extend(({ context, runServerlessFunction, actions }) => ( <Extension context={context} runServerless={runServerlessFunction} sendAlert={actions.addAlert} /> )); const ORIGINAL\_DATA = \[ { name: 'The Simpsons', yearsOnAir: 28, emmys: 31, }, { name: 'M\*A\*S\*H', yearsOnAir: 11, emmys: 14, }, { name: 'Arrested Development', yearsOnAir: 4, emmys: 5, }, \]; const DEFAULT\_STATE = { name: 'none', yearsOnAir: 'none', emmys: 'none', } function Extension() { const \[data, setData\] = useState(ORIGINAL\_DATA); const \[sortState, setSortState\] = useState({...DEFAULT\_STATE}); function handleOnSort(fieldName, sortDirection) { const dataClone = \[...data\]; dataClone.sort((entry1, entry2) => { if (sortDirection === 'ascending') { return entry1\[fieldName\] < entry2\[fieldName\] ? -1 : 1; } return entry2\[fieldName\] < entry1\[fieldName\] ? -1 : 1; }); setSortState({ ...DEFAULT\_STATE, \[fieldName\]: sortDirection }); setData(dataClone); } return ( <Table> <TableHead> <TableRow> <TableHeader sortDirection={sortState.name} onSortChange={sortDirection => handleOnSort('name', sortDirection)} > Series </TableHeader> <TableHeader sortDirection={sortState.yearsOnAir} onSortChange={sortDirection => handleOnSort('yearsOnAir', sortDirection) } > Years on air </TableHeader> <TableHeader sortDirection={sortState.emmys} onSortChange={sortDirection => handleOnSort('emmys', sortDirection)} > Emmys </TableHeader> </TableRow> </TableHead> <TableBody> {data.map(({ name, yearsOnAir, emmys }) => { return ( <TableRow key={name}> <TableCell>{name}</TableCell> <TableCell>{yearsOnAir}</TableCell> <TableCell>{emmys}</TableCell> </TableRow> ); })} </TableBody> <TableFooter> <TableRow> <TableHeader>Totals</TableHeader> <TableHeader>43</TableHeader> <TableHeader>50</TableHeader> </TableRow> </TableFooter> </Table> ); }

### Tag  [](https://developers.hubspot.com/docs/platform/ui-extension-components#tag-nbsp-)

The `Tag` component renders a tag.

![ui-ext-components-tag](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-tag.png?width=106&height=189&name=ui-ext-components-tag.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>onClick</code>&nbsp; <strong>function</strong><p>A function that will be invoked when the tag is clicked. It receives no argument and its return value is ignored.</p></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code>&nbsp; <strong>string</strong><p>The tag's color. The following variants are available: <code>default</code> (default), <code>warning</code>, <code>success</code><span>, and </span><code>error</code>.</p></td></tr></tbody></table>

const Extension = () => { return ( <Tag variant='success' onClick={() => { console.log('Tag clicked!'); }} > Success </Tag> ); }

### Text[](https://developers.hubspot.com/docs/platform/ui-extension-components#text)

The `Text` component renders text with formatting options.

![ui-extension-text-component-with-truncate](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-text-component-with-truncate.png?width=300&height=331&name=ui-extension-text-component-with-truncate.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>format</code>&nbsp; <strong>object</strong> (required)<p>The type of formatting for the text. Format types include:</p><ul><li><code>{ fontWeight: 'bold' }</code></li><li><code>{ fontWeight: 'demibold' }</code></li><li><code>{ italic: true }</code></li><li><code>{ lineDecoration: 'strikethrough' }</code></li><li><code>{ lineDecoration: 'underline' }</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code> <strong>string</strong><br><p>The style of text to display. Can be either of:</p><ul><li><code>bodytext</code>: the default value which renders the standard text size.</li><li><code>microcopy</code>: smaller text used for adding context.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>inline</code> <strong>boolean</strong><br><p>When set to <code>false</code>, inserts a line break.&nbsp;</p></td></tr><tr><td style="padding: 10px 4px;"><code>truncate</code> <strong>boolean </strong><span style="font-weight: normal;">|</span><strong> object</strong><br><p>This prop takes either a boolean or an options object:</p><ul><li><code>false</code> (default): text is not truncated.</li><li><code>true</code>: truncates text to a single line. Full text will display in a tooltip on hover.</li></ul><p>To specify the maximum width of the text and the text that will appear in a tooltip on hover:</p><p><code>truncate={{ tooltipText: 'string', maxWidth: px }}</code></p><ul><li><code>{tooltipText: 'string'}</code>: sets the text that will display in a tooltip on hover.</li><li><code>{maxWidth: px}</code>: the number of pixels wide to set the text before truncating.</li></ul></td></tr></tbody></table>

const Extension = () => { return ( <> <Text truncate={{ tooltipText:'string', maxWidth: 68 }}>Truncated text</Text> <Text>Plain text</Text> <Text format={{ fontWeight: 'bold' }}>Bold</Text> <Text format={{ italic: true }}>Italics</Text> <Text format={{ fontWeight: 'bold', italic: true }}> Bold and Italic text </Text> <Text format={{ lineDecoration: 'strikethrough' }}> Strikethrough Text </Text> <Text variant="microcopy"> Microcopy text <Text inline={true} format={{ fontWeight: 'bold' }}> with inner bold </Text> </Text> </> ); };

### Tile[](https://developers.hubspot.com/docs/platform/ui-extension-components#tile)

The `Tile` component renders a square tile containing other components.

![ui-components-tile-variants](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-components-tile-variants.png?width=546&height=244&name=ui-components-tile-variants.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>compact</code> &nbsp;<strong>boolean</strong>&nbsp;<p>When set to <code>true</code>, reduces the amount of padding in the tile.</p></td></tr><tr><td style="padding: 10px 4px;"><code>flush</code> &nbsp;<strong>boolean</strong>&nbsp;<p>When set to <code>true</code>, removes left and right padding from tile contents.</p></td></tr></tbody></table>

const Extension = () => { return ( <> <Tile> <Text>This is the default tile. It has a small amount of left padding</Text> </Tile> <Tile compact={true}> <Text>This is a compact tile. It reduces the amount of padding within.</Text> </Tile> <Tile flush={true}> <Text>This is a flush tile. It has no left padding</Text> </Tile> </> ); };

CRM data components[](https://developers.hubspot.com/docs/platform/ui-extension-components#crm-data-components)
---------------------------------------------------------------------------------------------------------------

CRM data components can pull data directly from the currently displaying CRM record, including information about associated records and single object reports. These components can only be placed in the middle column of CRM records.

These components are imported from `@hubspot/ui-extensions/crm`.

import { CrmAssociationPivot, CrmReport } from '@hubspot/ui-extensions/crm';

In the `CrmAssociationPivot` and `CrmAssociationTable` components, you can filter the data to fetch only what's most relevant. Review the table below for available filtering options.

Use this table to describe parameters / fields
| Prop | Type | Description |
| --- | --- | --- |
| 
`operator`

 | String | 

The filter's operator (e.g. `IN`). Can be one of:

*   `EQ`: is equal to `value`.
*   `NEQ`: is not equal to `value`.
*   `LT`: is less than `value`.
*   `LTE`:  is less than or equal to `value`.
*   `GT`:  is greater than `value`.
*   `GTE`: is greater than or equal to `value`.
*   `BETWEEN`: is within the specified range between `value` and `highValue`.
*   `IN`: is included in the specified `values` array. This operator is case-sensitive, so inputted values must be in lowercase. 
*   `NOT_IN`: is not included in the specified `values` array.
*   `HAS_PROPERTY`: has a value for the specified property.
*   `NOT_HAS_PROPERTY`: does not have a value for the specified property.

Learn more about [filtering CRM searches](/docs/api/crm/search#filter-operators).

 |
| 

`property`

 | String | 

The property to filter by.

 |
| 

`value`

 | String or number | 

The property value to filter by.

 |
| 

`values`

 | String or number | 

The property values to filter by when using an operator that requires an array, such as `IN`.

 |
| 

`highValue`

 | String or number | 

The upper value to filter by when using an operator that requires a range, such as `BETWEEN`.

 |

### Association pivot[](https://developers.hubspot.com/docs/platform/ui-extension-components#association-pivot)

The `CrmAssociationPivot` component renders a list of associated records organized by their assigned [association label](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels). You'll specify the type of records that you want to appear along with table attributes such as pagination, sorting, and more. You can either return all labels or specify the labels to return.

![ui-ext-components-associationspivot](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-associationspivot.png?width=579&height=249&name=ui-ext-components-associationspivot.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100.018%; height: 858.516px;"><tbody><tr style="height: 136px;"><td style="padding: 10px 4px; height: 136px;"><code>objectTypeId</code>&nbsp; <strong>string</strong>&nbsp; (required)<p>The numeric ID of the type of associated object to display (e.g., <code>0-1</code> for contacts). See <a href="/docs/api/crm/understanding-the-crm#object-type-id" rel="noopener">full list of object IDs</a>.</p></td></tr><tr style="height: 133px;"><td style="padding: 10px 4px; height: 133px;"><code>associationLabels</code>&nbsp; <strong>array</strong><p>Filters results by specific association labels. By default, all association labels will appear.</p></td></tr><tr style="height: 136.344px;"><td style="padding: 10px 4px; height: 136px;"><code>maxAssociations</code>&nbsp; <strong>number</strong><p>The number of items to return in each association label group before displaying a "Show more" button.</p></td></tr><tr style="height: 136px;"><td style="padding: 10px 4px; height: 136px;"><code>preFilters</code>&nbsp; <strong>array</strong><p>Filters the data by specific values of the associated records. <a href="#crm-data-properties" rel="noopener">Review the filtering options above</a> for more information.</p></td></tr><tr style="height: 316.172px;"><td style="padding: 10px 4px;"><code>sort</code>&nbsp; <strong>array</strong><p>The default sorting behavior for the table. In each sort object in the array, you'll specify the following:</p><ul><li><code>columnName</code>: the column to sort by.</li><li><code>direction</code>: the direction to sort by. Can be either <code>1</code> (ascending) or <code>-1</code> (descending). By default, order is ascending.</li></ul></td></tr></tbody></table>

const Extension = () => { return ( <CrmAssociationPivot objectTypeId="0-1" associationLabels={\["CEO", "CEO of subsidiary", "Co-founder"\]} maxAssociations={10} preFilters={\[ { "operator": "NOT\_IN", "property": "dealstage", "values": \["closedwon"\] } \]} sort={\[ { "columnName": "createdate", "direction": -1 } \]} /> ); };

### Association property list[](https://developers.hubspot.com/docs/platform/ui-extension-components#association-property-list)

The `CrmAssociationPropertyList` component renders a list of properties belonging to a record associated with the currently displaying record. For example, you can use this component to display properties of a company record from its associated contact record. You can edit these property values inline and will automatically save when leaving the field or pressing Enter.

![ui-extensions-component-associationpropertylist](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-component-associationpropertylist.png?width=516&height=126&name=ui-extensions-component-associationpropertylist.png)

 <table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%; height: 761.422px;"><tbody><tr style="height: 107.672px;"><td style="padding: 10px 4px; width: 100.112%; height: 108px;"><code>properties</code>&nbsp; <strong>array</strong>&nbsp;(required)<p>The list of properties to display from the associated record, up to 12.</p></td></tr><tr style="height: 135.922px;"><td style="padding: 10px 4px; width: 100.112%; height: 136px;"><code>objectTypeId</code> &nbsp;<strong>string</strong> (required)<p>The numeric ID of the type of associated object to display (e.g., <code>0-1</code> for contacts). See <a href="/docs/api/crm/understanding-the-crm#object-type-id" rel="noopener">full list of object IDs</a>.</p></td></tr><tr style="height: 107.672px;"><td style="padding: 10px 4px; width: 100.112%; height: 108px;"><code>associationLabels</code> &nbsp;<strong>array</strong><p>When provided, returns associated records that have all specified labels.</p></td></tr><tr style="height: 123.672px;"><td style="padding: 4px; width: 100.112%; height: 124px;"><code>filters</code> &nbsp;<strong>array</strong><p>Filters the data by specific values of the associated records. <a href="#crm-data-properties" rel="noopener">Review the filtering options above</a> for more information.</p></td></tr><tr style="height: 284.422px;"><td style="padding: 4px; width: 100.112%; height: 284px;"><code>sort</code> &nbsp;<strong>array</strong><p>The default sorting behavior for the returned results. In each sort object in the array, you'll specify the following:</p><ul><li><code>columnName</code>: the column to sort by.</li><li><code>direction</code>: the direction to sort by. Can be either <code>1</code> (ascending) or <code>-1</code> (descending). By default, order is ascending.</li></ul></td></tr></tbody></table>

const Extension = () => { return ( <CrmAssociationPropertyList objectTypeId="0-2" properties={\[ 'name', 'domain', 'city', 'state' \]} filters={\[ { operator: 'EQ', property: 'domain', value: 'meowmix.com' } \]} /> ); };

### Association table[](https://developers.hubspot.com/docs/platform/ui-extension-components#association-table)

The `CrmAssociationTable` component renders a table of associated records with optional filtering, sorting, and search methods. You'll specify the type of records that you want to appear along with the properties to display as columns.

![ui-ext-components-associationstable](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-associationstable.png?width=790&height=290&name=ui-ext-components-associationstable.png)

 <table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>objectTypeId</code>&nbsp; <strong>string</strong>&nbsp;(required)<p>The numeric ID of the type of associated object to display (e.g., <code>0-1</code> for contacts). See <a href="/docs/api/crm/understanding-the-crm#object-type-id" rel="noopener">full list of object IDs</a>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>propertyColumns</code> &nbsp;<strong>array</strong> (required)<p>The properties to add as table columns.</p></td></tr><tr><td style="padding: 10px 4px;"><code>quickFilterProperties</code> &nbsp;<strong>array</strong><p>The properties that appear as filters above the table. When included, the "Association label" quick filter will always display. See note below for more details on this prop.</p></td></tr><tr><td style="padding: 10px 4px;"><code>associationLabelFilter</code> &nbsp;<strong>boolean</strong><p>When set to <code>false</code>, hides the "Association label" quick filter above the table.</p></td></tr><tr><td style="padding: 10px 4px;"><code>searchable</code> &nbsp;<strong>boolean</strong><p>Set to <code>false</code> to hide the search box above the table.</p></td></tr><tr><td style="padding: 10px 4px;"><code>pagination</code> &nbsp;<strong>boolean</strong><p>Set to <code>false</code> to hide the pagination navigation below the table.</p></td></tr><tr><td style="padding: 10px 4px;"><code>pageSize</code> &nbsp;<strong>number</strong><p><span>The number of rows to include per page of results. Include the&nbsp;</span><code>pagination</code><span>&nbsp;property to enable users to navigate through returned results.</span></p></td></tr><tr><td style="padding: 10px 4px;"><code>preFilters</code> &nbsp;<strong>array</strong><p>Filters the data by specific values of the associated records. <a href="#crm-data-properties" rel="noopener">Review the filtering options above</a> for more information.</p></td></tr><tr><td style="padding: 10px 4px;"><code>sort</code> &nbsp;<strong>array</strong><p>The default sorting behavior for the table. In each sort object in the array, you'll specify the following:</p><ul><li><code>columnName</code>: the column to sort by.</li><li><code>direction</code>: the direction to sort by. Can be either <code>1</code> (ascending) or <code>-1</code> (descending). By default, order is ascending.</li></ul></td></tr></tbody></table>

const Extension = () => { return ( <CrmAssociationTable objectTypeId="0-3" propertyColumns={\['dealname', 'amount', 'description'\]} quickFilterProperties={\['createdate'\]} pageSize={10} preFilters={\[ { operator: 'EQ', property: 'dealstage', value: 'contractsent', }, \]} sort={\[ { direction: 1, columnName: 'amount', }, \]} searchable={true} pagination={true} /> ); };

**Please note:** for `quickFilterProperties`:

*   By default, four quick filters will display automatically depending on the object type.
    *   **Contacts (0-1):** `[ 'hubspot_owner_id', 'createdate', 'hs_lead_status', 'notes_last_updated' ]`
    *   **Companies (0-2):** `[ 'hubspot_owner_id', 'hs_lead_status', 'notes_last_updated', 'createdate' ]`
    *   **Deals (0-3):** `[ 'hubspot_owner_id', 'closedate', 'createdate', 'dealstage' ]`
    *   **Tickets (0-5):** `[ 'hubspot_owner_id', 'createdate', 'hs_pipeline_stage', 'hs_lastactivitydate' ]`
*   Custom objects do not have default quick filters
*   An empty array (`[]`) will remove any default quick filters except for "Association label".

### Data highlight[](https://developers.hubspot.com/docs/platform/ui-extension-components#data-highlight)

The `CrmDataHighlight` component renders a list of properties along with their values. You can use this component to surface important property data from either the currently displaying record or another specified record.

![data-highlight](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/data-highlight.png?width=800&height=115&name=data-highlight.png)

 <table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>properties</code>&nbsp; <strong>array</strong>&nbsp;(required)<p>The list of properties to display, up to four. By default, will show property data from the currently displaying record. Specify <code>objectTypeId</code> and <code>objectId</code> to pull data from another record.</p></td></tr><tr><td style="padding: 10px 4px;"><code>objectTypeId</code> &nbsp;<strong>string</strong><p>The numeric ID of the type of associated object to display (e.g., <code>0-1</code> for contacts). See <a href="/docs/api/crm/understanding-the-crm#object-type-id" rel="noopener">full list of object IDs</a>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>objectId</code> &nbsp;<strong>string</strong><p>The ID of the CRM record to display property data from.</p></td></tr></tbody></table>

const Extension = () => { return ( <CrmDataHighlight properties={\["createdate", "lifecyclestage", "hs\_num\_open\_deals", "hs\_num\_child\_companies"\]} /> ); };

### Property list[](https://developers.hubspot.com/docs/platform/ui-extension-components#property-list)

The `CrmPropertyList` component renders a list of properties along with their values. You can use this component to surface important property data from either the currently displaying record or another specified record. You can edit these property values inline and will automatically save when leaving the field or pressing Enter.

![ui-ext-components-propertylist](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-propertylist.png?width=481&height=252&name=ui-ext-components-propertylist.png)

 <table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>properties</code>&nbsp; <strong>array</strong>&nbsp;(required)<p>The list of properties to display, up to 12. By default, will show property data from the currently displaying record. Specify <code>objectTypeId</code> and <code>objectId</code> to pull data from another record.</p></td></tr><tr><td style="padding: 10px 4px;"><code>direction</code> &nbsp;<strong>string</strong><p>The layout direction of the table. Can be one of:&nbsp;</p><ul><li><code>column</code> (default): displays properties in single column.</li><li><code>row</code>: displays properties in a grid from left to right.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>objectTypeId</code> &nbsp;<strong>string</strong><p>The numeric ID of the type of associated object to display (e.g., <code>0-1</code> for contacts). See <a href="/docs/api/crm/understanding-the-crm#object-type-id" rel="noopener">full list of object IDs</a>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>objectId</code> &nbsp;<strong>string</strong><p>The ID of the CRM record to display property data from.</p></td></tr></tbody></table>

const Extension = () => { return ( <CrmPropertyList properties={\[ 'lastname', 'email', 'createdate', 'address', 'city', 'state', 'zip', \]} direction="row" /> ); };

### Report[](https://developers.hubspot.com/docs/platform/ui-extension-components#report)

The `CrmReport` component renders a [single object report](https://knowledge.hubspot.com/reports/create-custom-single-object-reports), which can be filtered with the `use` prop to surface data based on the currently displaying record, its associations, or unfiltered.

By default, the report data will automatically filter for the currently displaying record, as long as there is an association between the displaying record and records included in the report. For example, using this component you can display a single object report that shows which deals closed this quarter. When viewing the report on a contact record, by default the report will only display data from deals associated with that contact.

This component requires you to specify the ID of the report to render. To get a report's ID:

*   In your HubSpot account, navigate to **Reports** \> **Reports**.
*   Click the **name** of the report you want to display.
*   In the URL, copy the **number** that is not your HubID.

![report-id-in-URL](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/report-id-in-URL.png?width=452&height=36&name=report-id-in-URL.png)

![ui-ext-components-report](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-report.png?width=426&height=344&name=ui-ext-components-report.png)

**Please note:** users must have [permissions to view reports](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#reports) to view the component.

 <table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%; height: 504.094px;"><tbody><tr style="height: 107.672px;"><td style="padding: 10px 4px; height: 107.672px;"><code>reportId</code>&nbsp; <strong>string</strong>&nbsp;<p>The ID of the single object report, which can be found in the URL when viewing the report.</p></td></tr><tr style="height: 396.422px;"><td style="padding: 10px 4px; height: 396.422px;"><code>use</code>&nbsp; <strong>string</strong>&nbsp;<p>Specifies how the report should be filtered based on its relationship to the currently displaying CRM record:</p><ul><li><code>associations</code> (default): report will only include data from records associated with the currently displaying record.</li><li><code>subject</code>: report will only include data from the currently displaying record. Will not include data from associated records.</li><li><code>unfiltered</code>: report will display all data regardless of the currently displaying record and its associations.</li></ul></td></tr></tbody></table>

const Extension = () => { return ( <CrmReport reportId="6339949" />; ); };

### Stage tracker[](https://developers.hubspot.com/docs/platform/ui-extension-components#stage-tracker)

The `CrmStageTracker` component renders a lifecycle or pipeline stage progress bar and a list of properties. Available for contacts, companies, deals, tickets, and custom objects.

Use this component to show stage progress for the currently displaying record, or you can specify a record. You can also edit the property values inline and your changes will automatically save when leaving the field or pressing Enter.

![ui-extensions-component-dealstagetracker](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-component-dealstagetracker.png?width=537&height=136&name=ui-extensions-component-dealstagetracker.png)

 <table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>objectId</code> &nbsp;<strong>string</strong><p>The ID of the record to display. If not specified, will default to displaying information for the currently displaying record.</p></td></tr><tr><td style="padding: 10px 4px;"><code>objectTypeId</code>&nbsp; <strong>string</strong><p>The ID of the type of record to display (e.g., <code>0-3</code> for deals, <code>0-5</code> for tickets). See <a href="/docs/api/crm/understanding-the-crm#object-type-id" rel="noopener">full list of object IDs</a>. If not specified, will default to displaying information for the currently displaying record.</p></td></tr><tr><td style="padding: 10px 4px;"><code>properties</code>&nbsp; <strong>array</strong> (required)<p>The names of the properties to display. You can specify up to four properties, but properties beyond that will be ignored. If omitted, a set of default properties will render, depending on the object type.</p></td></tr><tr><td style="padding: 10px 4px;"><code>showProperties</code>&nbsp; <strong>boolean</strong>&nbsp;<p>Whether the show the list of properties below the stage progress indicator. When set to <code>false</code>, will not show the list of properties, even if provided.</p></td></tr></tbody></table>

const Extension = () => { return ( <CrmStageTracker objectId="13833764681" objectTypeId="0-3" properties={\[ 'dealname', 'amount', \]} /> ); };

### CRM statistics[](https://developers.hubspot.com/docs/platform/ui-extension-components#crm-statistics)

The `CrmStatistics` component renders data summaries calculated from the currently displaying CRM record's associations. For example, you can use this component to display data such as:

*   The average revenue of all of a contact’s associated companies.
*   The total number of times that a company has been contacted based on all of their associated tickets.
*   The maximum number of days to close from all of a company's associated deals.

To render data, you'll specify the properties you want to read from the associated records along with the type of calculation to perform on the property values. For each property, you can also include filters to narrow down the records that are included in the calculation.

![ui-extension-component-crm-statistics](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-component-crm-statistics.png?width=537&height=128&name=ui-extension-component-crm-statistics.png)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>objectTypeId</code>&nbsp; <strong>string </strong><span style="font-weight: normal;">(required)</span><p>The ID of the type of record to fetch data from (e.g., <code>0-3</code> for deals, <code>0-5</code> for tickets). See <a href="/docs/api/crm/understanding-the-crm#object-type-id" rel="noopener">full list of object IDs</a>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>statistics</code>&nbsp; <strong>array</strong> (required)<p>An array containing objects for each set of data to fetch. Each item in the array will contain:</p><ul><li><code>label</code>: the label to display above the statistic.</li><li><code>statisticType</code>: the type of statistic to request:<ul><li><code>SUM</code>: the sum of the values of the specified property.</li><li><code>AVG</code>: the average of the values of the specified property.</li><li><code>MIN</code>: the smallest value of the specified property.</li><li><code>MAX</code>: the largest value of the specified property.</li><li><code>COUNT</code>: the number of associated records with a value for the specified property.</li><li><code>DISTINCT_APPROX</code>: an approximate count of distinct values for the specified property.</li><li><code>PERCENTILES</code>: the property value at which a certain percentage of observed values occur. When using this type, you'll also need to include a <code>percentile</code> field to specify the percentile to display. <code>percentile</code> takes an integer from 0-100.</li></ul></li><li><code>propertyName</code>: the name of the property to fetch data from. The property type must be number, date, or datetime. Specifying any other type of property will result in the statistic showing <code>--</code> for its value.</li><li><code>filterGroups</code>: an optional array containing filters that specify which associated records to fetch property data from. You can include up to three filter group objects with each filter containing up to three filters. Exceeding these limits will result in the statistic showing <code>--</code> for its value. Filters are structured the same way as filters in the <a href="/docs/api/crm/search#filter-search-results" rel="noopener">CRM search API</a>.</li></ul></td></tr></tbody></table>

const Extension = () => { return ( <CrmStatistics objectTypeId="0-3" statistics={\[ { label: 'Average Deal Amount', statisticType: 'AVG', propertyName: 'amount', }, { label: '50th Percentile Deal Amount', statisticType: 'PERCENTILES', propertyName: 'amount', percentile: 50, }, { label: 'Time Left for Most Important Upcoming Deal', statisticType: 'MIN', propertyName: 'days\_to\_close', // The filters below narrow the fetched // deals by the following criteria: // - Amount must be >= 10,000 // - Deal must not be closed filterGroups: \[ { filters: \[ { operator: 'GTE', property: 'amount', value: 10000, }, { operator: 'EQ', property: 'hs\_is\_closed', value: "false", }, \], }, \], }, \]} /> ); };

CRM action components[](https://developers.hubspot.com/docs/platform/ui-extension-components#crm-action-components)
-------------------------------------------------------------------------------------------------------------------

CRM action components provide a built-in set of CRM-related actions, including adding notes to records, opening a one-to-one email composition window, creating new records, and more. Each component can perform the same set of actions, so which component to choose will depend on your needs and preferences. Check out the [component design guidelines](/docs/platform/component-design-guidelines) for additional guidance. 

CRM action components are imported from `@hubspot/ui-extensions/crm`.

import { CrmActionButton, CrmActionLink } from '@hubspot/ui-extensions/crm';

![crm-card-actions](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/crm-card-actions.png?width=726&height=254&name=crm-card-actions.png)

1.  **CRM action buttons:** buttons for [previewing a CRM record](#preview-a-crm-record) or [creating a new associated record](#create-an-associated-record).
2.  **CRM action link:**  a link for [creating a new note](#create-a-note) on the deal record on click.
3.  **CRM card actions:** buttons in the top right of the card that contain lists of actions in dropdown menus.

Users can only take actions through these components when they have the proper permissions. For example, if a user doesn't have permission to create deal records, they won't be able to use a CRM action component to create a deal record. Instead, an error message will be generated and returned through an optional `onError` callback.

Each action requires an `actionType` and `actionContext`.

*   `actionType`: the type of action. See the [available actions](#available-actions) section below.
*   `actionContext`: the CRM object and record context required for the action to be performed. For example, to include an action to open a preview sidebar for a specified record, you'll need to provide the record's `objectTypeId` and `objectId` in `actionContext`. See the [available actions](#available-actions) for more information about what's required for each action.

### Action button[](https://developers.hubspot.com/docs/platform/ui-extension-components#action-button)

The `CrmActionButton` component renders a button that can execute a built-in set of CRM actions. See [list of available actions](#available-actions) for more information. This component can be used in extensions that are in either the sidebar or middle column.

![ui-extensions-crm-action-button](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-crm-action-button.png?width=397&height=64&name=ui-extensions-crm-action-button.png)

 <table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>actionType</code>&nbsp; <strong>string</strong>&nbsp;(required)<p>The type of action for the button to perform. See <a href="#available-actions" rel="noopener">list of available actions below</a>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>actionContext</code> &nbsp;<strong>object</strong> (required)<p>An object containing the CRM object and record context for performing the action. See <a href="#available-actions" rel="noopener">list of available actions below</a> for required context values.</p></td></tr><tr><td style="padding: 10px 4px;"><code>variant</code> &nbsp;<strong>string</strong><p>Sets the color variation of the button. Values include:</p><ul><li><code>primary</code></li><li><code>secondary</code><span>&nbsp;</span>(default)</li><li><code>destructive</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>size</code>&nbsp; <strong>string&nbsp;</strong><p>Sets the size of the button. Values include:</p><ul><li><code>xs</code>, <code>extra-small</code></li><li><code>sm</code>, <code>small</code></li><li><code>md</code>, <code>medium</code> (default)</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>disabled</code> &nbsp;<strong>boolean</strong><p>Set to <code>true</code> to render the button in a disabled, greyed-out state.</p></td></tr><tr><td style="padding: 10px 4px;"><code>type</code> &nbsp;<strong>array</strong><p>Sets the HTML attribute<span>&nbsp;</span><code>role</code><span>&nbsp;</span>of the button. Can be one of:</p><ul><li><code>button</code><span>&nbsp;</span>(default)</li><li><code>reset</code></li><li><code>submit</code></li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>onError</code> &nbsp;<strong>function</strong><p>An optional callback that will be passed any error messages that were generated. Common errors include missing required context values or the user having insufficient permissions to perform an action.</p></td></tr></tbody></table>

const dealContext = { objectTypeId: "0-3", objectId: 14795354663, }; const associateContext = { objectTypeId: "0-3", association: { objectTypeId: "0-1", objectId: 769851, }, }; hubspot.extend(({ context, runServerlessFunction, actions }) => { return ( <> <CrmActionButton actionType="PREVIEW\_OBJECT" actionContext={dealContext} variant="secondary" > Preview existing Deal </CrmActionButton> <CrmActionButton actionType="OPEN\_RECORD\_ASSOCIATION\_FORM" actionContext={associateContext} variant="primary" > Create new Deal </CrmActionButton> </> ); });

### Action link[](https://developers.hubspot.com/docs/platform/ui-extension-components#action-link)

The `CrmActionLink` component renders a clickable link that can execute a built-in set of CRM actions. See [list of available actions](#available-actions) for more information. This component can be used in extensions that are in either the sidebar or middle column.

![ui-extensions-crm-action-link](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-crm-action-link.png?width=299&height=39&name=ui-extensions-crm-action-link.png)

 <table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px; width: 100.112%;"><code>actionType</code>&nbsp; <strong>string</strong>&nbsp;(required)<p>The type of action for the button to perform. See <a href="#available-actions" rel="noopener">list of available actions below</a>.</p></td></tr><tr><td style="padding: 10px 4px; width: 100.112%;"><code>actionContext</code> &nbsp;<strong>object</strong> (required)<p>An object containing the CRM object and record context for performing the action. See <a href="#available-actions" rel="noopener">list of available actions below</a> for required context values.</p></td></tr><tr><td style="padding: 10px 4px; width: 100.112%;"><code>variant</code> &nbsp;<strong>string</strong><p>Sets the color variation of the button. Values include:</p><ul><li><code>primary</code> (default)</li><li><code>light</code><span>&nbsp;</span></li><li><code><span>dark</span></code></li><li><code>destructive</code></li></ul></td></tr><tr><td style="padding: 4px; width: 100.112%;"><code>onError</code> &nbsp;<strong>function</strong><p>An optional callback that will be passed any error messages that were generated. Common errors include missing required context values or the user having insufficient permissions to perform an action.</p></td></tr></tbody></table>

const dealContext = { objectTypeId: "0-3", objectId: 14795354663, }; hubspot.extend(({ context, runServerlessFunction, actions }) => { return ( <> <CrmActionLink actionType="ADD\_NOTE" actionContext={dealContext} > Add a note about this deal to the record </CrmActionLink> </> ); });

### Action menu[](https://developers.hubspot.com/docs/platform/ui-extension-components#action-menu)

The `CrmCardActions` component renders a smaller standalone or dropdown menu button that can contain multiple CRM actions. See [list of available actions](#available-actions) for more information. This component can only be used in extensions that are in the middle column.

![2023-08-29_15-08-37 (1)](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/2023-08-29_15-08-37%20(1).gif?width=323&height=280&name=2023-08-29_15-08-37%20(1).gif)

 <table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>type</code>&nbsp; <strong>string</strong>&nbsp;(required)<p>The type of button to render:</p><ul><li><code>action-library-button</code>: a standalone button that can perform one action.&nbsp;</li><li><code>dropdown</code>: a dropdown menu button containing multiple action options. When using this type, you'll need to include an <code>options</code> array containing each action.</li></ul></td></tr><tr><td style="padding: 10px 4px 10px 22px;"><span>⮑</span> <code>options</code> &nbsp;<strong>array</strong><p>Array containing an object for each available action. See <a href="#available-actions" rel="noopener">list of available actions below</a>.</p></td></tr><tr><td style="padding: 10px 4px; width: 100.112%;"><code>actionContext</code> &nbsp;<strong>object</strong> (required)<p>An object containing the CRM object and record context for performing the action. See <a href="#available-actions" rel="noopener">list of available actions below</a> for required context values.</p></td></tr><tr><td style="padding: 4px; width: 100.112%;"><code>disabled</code> &nbsp;<strong>boolean</strong><p>Set to <code>true</code> to render the button in a disabled, greyed-out state.</p></td></tr><tr><td style="padding: 4px; width: 100.112%;"><code>tooltipText</code> &nbsp;<strong>string</strong><p>Text that displays above the button on hover.</p></td></tr></tbody></table>

<CrmCardActions actionConfigs={\[ { type: "action-library-button", label: "Preview", actionType: "PREVIEW\_OBJECT", actionContext: { objectTypeId:"0-3", objectId: 14795354663 }, tooltipText: "Preview this deal record." }, { type: "dropdown", label: "Activities", options: \[ { type: "action-library-button", label: "Send email", actionType: "SEND\_EMAIL", actionContext: { objectTypeId: "0-1", objectId: 769851 } }, { type: "action-library-button", label: "Add note", actionType: "ADD\_NOTE", actionContext: { objectTypeId: "0-1", objectId: 769851 }, } \] } \]} />

### Available actions[](https://developers.hubspot.com/docs/platform/ui-extension-components#available-actions)

The following actions are available for CRM action components:

*   [Preview a CRM record](#preview-a-crm-record)
*   [Create a note](#create-a-note)
*   [Send a one-to-one email](#send-a-one-to-one-email)
*   [Schedule a meeting](#schedule-a-meeting)
*   [Create an associated CRM record](#create-an-associated-record)
*   [Navigate to an engagement](#navigate-to-an-engagement)
*   [Navigate to a record](#navigate-to-a-record)
*   [Navigate to a HubSpot page](#navigate-to-a-hubspot-page)

#### Preview a CRM record[](https://developers.hubspot.com/docs/platform/ui-extension-components#preview-a-crm-record)

The `PREVIEW_OBJECT` action opens a preview sidebar for the specified CRM record.

Requires the following `actionContext`:

*   `objectTypeId`: the CRM record's object type (e.g., `0-1` for contacts). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to preview.

<CrmActionButton actionType="PREVIEW\_OBJECT" actionContext={{ objectTypeId: "0-3", objectId: 123456 }} variant="secondary" > Preview deal </CrmActionButton>

#### Create a note[](https://developers.hubspot.com/docs/platform/ui-extension-components#create-a-note)

The `ADD_NOTE` action opens a note composition window, enabling users to add a note to the specified CRM record.

Requires the following `actionContext`:

*   `objectTypeId`: the CRM record's object type (e.g., `0-1` for contacts). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record.

<CrmActionButton actionType="ADD\_NOTE" actionContext={{ objectTypeId: "0-3", objectId: 123456 }} variant="secondary" > Create note </CrmActionButton>

#### Send a one-to-one email[](https://developers.hubspot.com/docs/platform/ui-extension-components#send-a-one-to-one-email)

The `SEND_EMAIL` action opens a one-to-one email composition window, enabling users to send an email to the specified contact or the contacts associated with the specified record.

Requires the following `actionContext`:

*   `objectTypeId`: the CRM record's object type (e.g., `0-1` for contacts). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to send the email to.

<CrmActionButton actionType="SEND\_EMAIL" actionContext={{ objectTypeId: "0-3", objectId: 123456 }} variant="secondary" > Send email </CrmActionButton>

#### Schedule a meeting[](https://developers.hubspot.com/docs/platform/ui-extension-components#schedule-a-meeting)

The `SCHEDULE_MEETING` action opens a window for [scheduling a meeting](https://knowledge.hubspot.com/meetings-tool/create-and-edit-scheduling-pages).

Requires the following `actionContext`:

*   `objectTypeId`: the CRM record's object type (e.g., `0-1` for contacts). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to schedule the meeting with.

<CrmActionButton actionType="SCHEDULE\_MEETING" actionContext={{ objectTypeId: '0-1', objectId: 123456 }} > Schedule meeting </CrmActionButton>

#### Create an associated record[](https://developers.hubspot.com/docs/platform/ui-extension-components#create-an-associated-record)

The `OPEN_RECORD_ASSOCIATION_FORM` action opens a side panel for creating a new record to be associated with another.

Requires the following `actionContext`:

*   `objectTypeId`: the type of CRM record to create (e.g., `0-2` for companies). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `association`: an object containing information about the record that the new one will be associated with. This is typically the currently displaying record. Contains:
    *   `objectTypeId`: the type of CRM record to associate the new one with.
    *   `objectId`: the ID of the CRM record to associate the new one with.

<CrmActionButton actionType="OPEN\_RECORD\_ASSOCIATION\_FORM" actionContext={{ objectTypeId: '0-2', association: { objectTypeId: '0-1', objectId: 123456 } }} > Create new record </CrmActionButton>

#### Navigate to an engagement[](https://developers.hubspot.com/docs/platform/ui-extension-components#navigate-to-an-engagement)

The `ENGAGEMENT_APP_LINK` action navigates the user to a specific engagement on a CRM record timeline, such as a call or task.

Requires the following `actionContext`:

*   `objectTypeId`: the type of CRM record to navigate to (e.g., `0-2` for companies). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to navigate to.
*   `engagementId`: the ID of the engagement, such as a task or note.
*   `external`: optionally, set to `true` to navigate to the engagement in a new browser tab.

<CrmActionButton actionType="ENGAGEMENT\_APP\_LINK" actionContext={{ objectTypeId: "0-2", objectId: 2763710643, engagementId: 39361694368 }} variant="secondary" > Open note </CrmActionButton>

#### Navigate to a CRM record[](https://developers.hubspot.com/docs/platform/ui-extension-components#navigate-to-a-crm-record)

The `RECORD_APP_LINK` action navigates the user to a specific CRM record.

Requires the following `actionContext`:

*   `objectTypeId`: the type of CRM record to navigate to (e.g.,  `0-2` for companies). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to navigate to.
*   `external`: optionally, set to `true` to navigate to the record in a new browser tab.
*   `includeEschref`: optionally, set to `true` to include a _Back_ button in the top left corner of the opened CRM record to navigate the user back to the original record.  
    ![ui-extensions-crm-action-back-button](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-crm-action-back-button.png?width=342&height=171&name=ui-extensions-crm-action-back-button.png)

<CrmActionButton actionType="RECORD\_APP\_LINK" actionContext={{ objectTypeId: "0-2", objectId: 2763710643, includeEschref: true }} variant="secondary" > View company </CrmActionButton>

#### Navigate to a HubSpot page[](https://developers.hubspot.com/docs/platform/ui-extension-components#navigate-to-a-hubspot-page)

The `PAGE_APP_LINK` navigates the user to any page within the HubSpot account. Use this action when a user would need to navigate to a non-CRM record account page, such as the email tool.

Requires the following `actionContext`:

*   `path`: the URL path of the HubSpot page. This path is relative to `https://app.hubspot.com` and should begin with `/`.
*   `external`: optionally, set to `true` to navigate to the page in a new browser tab.

<CrmActionButton actionType="PAGE\_APP\_LINK" actionContext={{ path: "/email/123456/analyze?emailType=followup-2", external: true }} variant="secondary" > Open email dashboard </CrmActionButton>

#### Navigate to an external page[](https://developers.hubspot.com/docs/platform/ui-extension-components#navigate-to-an-external-page)

The `EXTERNAL_URL` action navigates the user to a website page in a new tab.

Requires the following `actionContext`:

*   `href`: the URL, which must begin with `http` or `https`. When protocol is not specified, HubSpot will automatically prefix the URL with `https`.

<CrmActionButton actionType="EXTERNAL\_URL" actionContext={{ href: "https://www.google.com", }} variant="secondary" > Open Google </CrmActionButton>

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-extension-components#page-feedback)
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
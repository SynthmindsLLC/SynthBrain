---
Please provide me with more context!  I need to know what kind of mission you're writing about. For example, tell me: "* **What is the mission's purpose?** Is it for a company, a non-profit, a team, a personal goal, or something else?"
* **What is the overall objective?** What are you trying to achieve?
* **Who is the target audience?** Who is this mission for?

Once I have this information, I can help you write a compelling and effective mission statement!
---

CRM action components (BETA)
============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

CRM action components provide a built-in set of CRM-related actions, including adding notes to records, opening a one-to-one email composition window, creating new records, and more. Each component can perform the same set of actions, so which component to choose will depend on your needs and preferences.

Below, learn more about CRM action components and actions available to each.

CRM action components are imported from `@hubspot/ui-extensions/crm`.

import { CrmActionButton, CrmActionLink, CrmCardActions } from '@hubspot/ui-extensions/crm';

Available components[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#available-components)
-----------------------------------------------------------------------------------------------------------------------------

![crm-card-actions](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/crm-card-actions.png?width=726&height=254&name=crm-card-actions.png)

1.  [CrmActionButton](/docs/platform/ui-components/crmactionbutton)**:** renders a button.
2.  [CrmActionLink](/docs/platform/ui-components/crmactionlink): renders a clickable link.
3.  [CrmCardActions](/docs/platform/ui-components/crmcardactions): renders dropdown menu buttons in the top right of the extension.

Users can only take actions through these components when they have the proper permissions. For example, if a user doesn't have permission to create deal records, they won't be able to use a CRM action component to create a deal record. Instead, an error message will be generated and returned through an optional `onError` callback.

Each action requires an `actionType` and `actionContext`.

*   `actionType`: the type of action. See the [available actions section](#available-actions) below.
*   `actionContext`: the CRM object and record context required for the action to be performed. For example, to include an action to open a preview sidebar for a specified record, you'll need to provide the record's `objectTypeId` and `objectId` in `actionContext`. See the [available actions section](#available-actions) for more information about what's required for each action.

Available actions[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#available-actions)
-----------------------------------------------------------------------------------------------------------------------

The following actions are available for CRM action components:

*   [Preview a CRM record](#preview-a-crm-record)
*   [Create a note](#create-a-note)
*   [Send a one-to-one email](#send-a-one-to-one-email)
*   [Schedule a meeting](#schedule-a-meeting)
*   [Create an associated CRM record](#create-an-associated-record)
*   [Navigate to an engagement](#navigate-to-an-engagement)
*   [Navigate to a CRM record](#navigate-to-a-crm-record)
*   [Navigate to a HubSpot page](#navigate-to-a-hubspot-page)
*   [Navigate to an external page](#navigate-to-an-external-page)

### Preview a CRM record[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#preview-a-crm-record)

The `PREVIEW_OBJECT` action opens a preview sidebar for the specified CRM record.

Requires the following `actionContext`:

*   `objectTypeId`: the CRM record's object type (e.g., `0-1` for contacts). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to preview.

<CrmActionButton actionType="PREVIEW\_OBJECT" actionContext={{ objectTypeId: "0-3", objectId: 123456 }} variant="secondary" > Preview deal </CrmActionButton>

### Create a note[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#create-a-note)

The `ADD_NOTE` action opens a note composition window, enabling users to add a note to the specified CRM record.

Requires the following `actionContext`:

*   `objectTypeId`: the CRM record's object type (e.g., `0-1` for contacts). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record.

<CrmActionButton actionType="ADD\_NOTE" actionContext={{ objectTypeId: "0-3", objectId: 123456 }} variant="secondary" > Create note </CrmActionButton>

### Send a one-to-one-email[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#send-a-one-to-one-email)

The `SEND_EMAIL` action opens a one-to-one email composition window, enabling users to send an email to the specified contact or the contacts associated with the specified record.

Requires the following `actionContext`:

*   `objectTypeId`: the CRM record's object type (e.g., `0-1` for contacts). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to send the email to.

<CrmActionButton actionType="SEND\_EMAIL" actionContext={{ objectTypeId: "0-3", objectId: 123456 }} variant="secondary" > Send email </CrmActionButton>

### Schedule a meeting[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#schedule-a-meeting)

The `SCHEDULE_MEETING` action opens a window for [scheduling a meeting](https://knowledge.hubspot.com/meetings-tool/create-and-edit-scheduling-pages).

Requires the following `actionContext`:

*   `objectTypeId`: the CRM record's object type (e.g., `0-1` for contacts). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to schedule the meeting with.

<CrmActionButton actionType="SCHEDULE\_MEETING" actionContext={{ objectTypeId: '0-1', objectId: 123456 }} > Schedule meeting </CrmActionButton>

### Create an associated record[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#create-an-associated-record)

The `OPEN_RECORD_ASSOCIATION_FORM` action opens a side panel for creating a new record to be associated with another.

Requires the following `actionContext`:

*   `objectTypeId`: the type of CRM record to create (e.g., `0-2` for companies). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `association`: an object containing information about the record that the new one will be associated with. This is typically the currently displaying record. Contains:
    *   `objectTypeId`: the type of CRM record to associate the new one with.
    *   `objectId`: the ID of the CRM record to associate the new one with.

<CrmActionButton actionType="OPEN\_RECORD\_ASSOCIATION\_FORM" actionContext={{ objectTypeId: '0-2', association: { objectTypeId: '0-1', objectId: 123456 } }} > Create new record </CrmActionButton>

### Navigate to an engagement[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#navigate-to-an-engagement)

The `ENGAGEMENT_APP_LINK` action navigates the user to a specific engagement on a CRM record timeline, such as a call or task.

Requires the following `actionContext`:

*   `objectTypeId`: the type of CRM record to navigate to (e.g., `0-2` for companies). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to navigate to.
*   `engagementId`: the ID of the engagement, such as a task or note.
*   `external`: optionally, set to `true` to navigate to the engagement in a new browser tab.

<CrmActionButton actionType="ENGAGEMENT\_APP\_LINK" actionContext={{ objectTypeId: "0-2", objectId: 2763710643, engagementId: 39361694368 }} variant="secondary" > Open note </CrmActionButton>

### Navigate to a CRM record[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#navigate-to-a-crm-record)

The `RECORD_APP_LINK` action navigates the user to a specific CRM record.

Requires the following `actionContext`:

*   `objectTypeId`: the type of CRM record to navigate to (e.g., `0-2` for companies). See [full list of object IDs](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id).
*   `objectId`: the ID of the CRM record to navigate to.
*   `external`: optionally, set to `true` to navigate to the record in a new browser tab.
*   `includeEschref`: optionally, set to `true` to include a _Back_ button in the top left corner of the opened CRM record to navigate the user back to the original record.

![ui-extensions-crm-action-back-button](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-crm-action-back-button.png?width=342&height=171&name=ui-extensions-crm-action-back-button.png)

<CrmActionButton actionType="RECORD\_APP\_LINK" actionContext={{ objectTypeId: "0-2", objectId: 2763710643, includeEschref: true }} variant="secondary" > View company </CrmActionButton>

### Navigate to a HubSpot page[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#navigate-to-a-hubspot-page)

The `PAGE_APP_LINK` navigates the user to any page within the HubSpot account. Use this action when a user would need to navigate to a non-CRM record account page, such as the email tool.

Requires the following `actionContext`:

*   `path`: the URL path of the HubSpot page. This path is relative to `https://app.hubspot.com` and should begin with `/`.
*   `external`: optionally, set to `true` to navigate to the page in a new browser tab.

<CrmActionButton actionType="PAGE\_APP\_LINK" actionContext={{ path: "/email/123456/analyze?emailType=followup-2", external: true }} variant="secondary" > Open email dashboard </CrmActionButton>

### Navigate to an external page[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#navigate-to-an-external-page)

The `EXTERNAL_URL` action navigates the user to a website page in a new tab.

Requires the following `actionContext`:

*   `href`: the URL, which must begin with `http` or `https`. When protocol is not specified, HubSpot will automatically prefix the URL with `https`.

<CrmActionButton actionType="EXTERNAL\_URL" actionContext={{ href: "https://www.google.com", }} variant="secondary" > Open Google </CrmActionButton>

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crm-action-components#page-feedback)
---------------------------------------------------------------------------------------------------------------------

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
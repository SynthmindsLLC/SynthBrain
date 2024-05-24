CrmReport | UI components (BETA)
================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmReport` component renders a [single object report](https://knowledge.hubspot.com/reports/create-custom-single-object-reports), which can be filtered with the `use` prop to surface data based on the currently displaying record, its associations, or unfiltered.

By default, the report data will automatically filter for the currently displaying record, as long as there is an association between the displaying record and records included in the report.

For example, using this component you can display a single object report that shows which deals closed this quarter. When viewing the report on a contact record, by default the report will only display data from deals associated with that contact.

![ui-ext-components-report](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-report.png?width=426&height=344&name=ui-ext-components-report.png)

This component requires you to specify the ID of the report to render. To get a report's ID:

*   In your HubSpot account, navigate to **Reports** \> **Reports**.
*   Click the **name** of the report you want to display.
*   In the URL, copy the **number** that is not your HubID.

![report-id-in-URL](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/report-id-in-URL.png?width=452&height=36&name=report-id-in-URL.png)

**Please note:** report data will only display for users with [permissions to view reports](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#reports).

import { CrmReport } from '@hubspot/ui-extensions/crm'; const Extension = () => { return ( <CrmReport reportId="6339949" />; ); };

| Prop | Type | Description |
| --- | --- | --- |
| `reportId` Required | String | The numeric ID of the single object report, which can be found in the URL when viewing the report in HubSpot. |
| `use` | `'associations'` (default) |  
`'subject'` |  
`'unfiltered'` | Specifies how the report should be filtered based on its relationship to the currently displaying CRM record:
*   `associations`: report will only include data from records associated with the currently displaying record.
*   `subject`: report will only include data from the currently displaying record. Will not include data from associated records.
*   `unfiltered`: report will display all data regardless of the currently displaying record and its associations.

 |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmreport#related-components)
-------------------------------------------------------------------------------------------------------------

*   [CrmAssociationPivot](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpivot)
*   [CrmAssociationPropertyList](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpropertylist)
*   [CrmAssociationTable](https://developers.hubspot.com/docs/platform/ui-components/crmassociationtable)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmreport#page-feedback)
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
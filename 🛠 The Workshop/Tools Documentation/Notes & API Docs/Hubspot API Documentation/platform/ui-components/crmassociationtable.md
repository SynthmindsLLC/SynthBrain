---
Please provide me with more context!  I need to know what the mission is about. 

For example, tell me: "* **What is the goal of the mission?**  What are you trying to achieve?"
* **Who is involved in the mission?**  Is it a team, a company, an individual?
* **What is the scope of the mission?**  Is it a small project, or something much larger?

Once I have more information, I can help you write a compelling mission statement.
---

CrmAssociationTable | UI components (BETA)
==========================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmAssociationTable` component renders a table of associated records with optional filtering, sorting, and search methods. You'll specify the type of records that you want to appear along with the properties to display as columns.

![ui-ext-components-associationstable](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-components-associationstable.png?width=790&height=290&name=ui-ext-components-associationstable.png)

import { CrmAssociationTable } from '@hubspot/ui-extensions/crm'; const Extension = () => { return ( <CrmAssociationTable objectTypeId="0-3" propertyColumns={\['dealname', 'amount', 'description'\]} quickFilterProperties={\['createdate'\]} pageSize={10} preFilters={\[ { operator: 'EQ', property: 'dealstage', value: 'contractsent', }, \]} sort={\[ { direction: 1, columnName: 'amount', }, \]} searchable={true} pagination={true} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `propertyColumns` Required | Array | The properties to display as table columns. |
| `objectTypeId` Required | String | The numeric ID of the type of associated object to display (e.g., `0-1` for contacts). See [complete list](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id) of object IDs. |
| `quickFilterProperties` | Array | The properties that appear as filters above the table. When included, the "Association label" quick filter will always display. See note below for more details on this prop. |
| `associationLabelFilter` | Boolean | When set to `false`, hides the "Association label" quick filter above the table. |
| `searchable` | Boolean | When set to `false`, hides the search bar above the table. |
| `pagination` | Boolean | When set to `false`, hides the pagination navigation below the table. |
| `pageSize` | Number | The number of rows to include per page of results. Include the `pagination` property to enable users to navigate through returned results. |
| `preFilters` | Array | Filters the data by specific values of the associated records. Review the [CRM data filter options](/docs/platform/ui-components/crm-data-components#filtering-data) for more information. |
| `sort` | Array | The default sorting behavior for the table. In each sort object in the array, you'll specify the following:
*   `columnName`: the column to sort by.
*   `direction`: the direction to sort by. Can be either `1` (ascending) or `-1` (descending). By default, order is ascending.

 |

**Please note:** for `quickFilterProperties`:

*   By default, four quick filters will display automatically depending on the object type.
    *   **Contacts (`0-1`):** `[ 'hubspot_owner_id', 'createdate', 'hs_lead_status', 'notes_last_updated' ]`
    *   **Companies (`0-2`):** `[ 'hubspot_owner_id', 'hs_lead_status', 'notes_last_updated', 'createdate' ]`
    *   **Deals (`0-3`):** `[ 'hubspot_owner_id', 'closedate', 'createdate', 'dealstage' ]`
    *   **Tickets (`0-5`):** `[ 'hubspot_owner_id', 'createdate', 'hs_pipeline_stage', 'hs_lastactivitydate' ]`
*   Custom objects do not have default quick filters.
*   An empty array (`[]`) will remove any default quick filters except for "Association label."

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmassociationtable#related-components)
-----------------------------------------------------------------------------------------------------------------------

*   [CrmAssociationPivot](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpivot)
*   [CrmAssociationPropertyList](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpropertylist)
*   [CrmReport](https://developers.hubspot.com/docs/platform/ui-components/crmreport)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmassociationtable#page-feedback)
-------------------------------------------------------------------------------------------------------------------

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
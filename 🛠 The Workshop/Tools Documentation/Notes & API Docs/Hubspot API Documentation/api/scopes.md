Scopes
======

Scopes provide access to a specific set of HubSpot API endpoints and the associated data from a HubSpot account. If you created a private app, you can specify which scopes your app has access to in your [private app settings](/docs/api/private-apps#create-a-private-app). If you're developing a public app, you'll [configure both required and optional scopes](/docs/api/creating-an-app#configure-scopes) that users who install your app will be prompted to authorize via the app's install URL.

Find required scopes for an endpoint[](https://developers.hubspot.com/docs/api/scopes#find-required-scopes-for-an-endpoint)
---------------------------------------------------------------------------------------------------------------------------

Any scopes required to make a request to a specific endpoint will be listed under the _Requirements_ section in the endpoint documentation, which can be accessed by clicking the Endpoints tab in an API reference article.

![find-scopes-on-endpoints-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/find-scopes-on-endpoints-tab.png?width=425&height=434&name=find-scopes-on-endpoints-tab.png)

Some scopes may list both _Standard_ and _Granular_ scopes. If both scope types are listed, you should opt for using the granular scopes when possible, as they specify more explicit access for your API requests.

List of available scopes[](https://developers.hubspot.com/docs/api/scopes#list-of-available-scopes)
---------------------------------------------------------------------------------------------------

Access to specific APIs or endpoints depends on HubSpot account tier. You can find a full list of available scopes and accessible endpoints in the table below.

  

| **Scope** | **Description** | **Provides access to** | **Required account tier** |
| --- | --- | --- | --- |
| `cms.domains.read` | Integrators can list CMS domains in a customer's account.  | CMS API | Any account |
| `cms.domains.write` | Integrators can create, update, and delete CMS custom domains.  | CMS API | Any account |
| `cms.functions.read` | Integrators can view all CMS serverless functions, any related secrets, and function execution results.  | CMS API | _**CMS Hub** Enterprise_ |
| `cms.functions.write` | Integrators can write CMS serverless functions and secrets. | CMS API | _**CMS Hub**_ _Enterprise_ |
| `cms.knowledge_base.articles.read` | View details about knowledge articles. | CMS API | _**Service Hub**_ _Professional_ or _Enterprise_  |
| 
`cms.knowledge_base.articles.write`

 | Grants access to update knowledge articles.  | CMS API | _**Service Hub** Professional_ or _Enterprise_  |
| `cms.knowledge_base.articles.publish` | Grants access to update and publish knowledge articles. | CMS API | _**Service Hub** Professional_ or _Enterprise_  |
| `cms.knowledge_base.settings.read` | View general and template knowledge base settings, such as the domain or root URL. | CMS API | _**Service Hub** Professional_ or _Enterprise_  |
| `cms.knowledge_base.settings.write` | Grants access to update general and template knowledge base settings. This includes write access to knowledge articles. | CMS API | _**Service Hub** Professional_ or _Enterprise_  |
| `cms.performance.read` | Integrators can view CMS performance data for all your sites. | CMS API | Any account |
| `crm.lists.read` | View details about contact lists. | List endpoints | Any account |
| `crm.lists.write` | Create, delete, or make changes to contact lists | List endpoints | Any account |
| `crm.objects.companies.read` | View properties and other details about companies. | Companies endpoints | Any account |
| `crm.objects.companies.write` | View properties and create, delete, or make changes to companies. | Companies endpoints | Any account |
| `crm.objects.contacts.read` | View properties and other details about contacts. | Contacts endpoints | Any account |
| `crm.objects.contacts.write` | View properties and create, delete, and make changes to contacts. | Contacts endpoints | Any account |
| `crm.objects.custom.read` | View details about custom objects in the HubSpot CRM. | Custom objects endpoints | Any _Enterprise_ |
| `crm.objects.custom.write` | Create, delete, or make changes to custom objects in the HubSpot CRM.  | Custom objects endpoints | Any _Enterprise_ |
| `crm.objects.deals.read` | View properties and other details about deals. | Deal endpoints | Any account |
| `crm.objects.deals.write` | View properties and create, delete, or make changes to deals. | Deal endpoints | Any account |
| `crm.objects.feedback_submission.read` | View details about submissions to any of your feedback surveys. | Feedback survey endpoints | **_Service Hub_** _Professional_ or _Enterprise_ |
| `crm.objects.goals.read` | View all goal types.  | Goals endpoints | _**Sales Hub**_ _Starter_, _Professional_, or _Enterprise_ |
| `crm.objects.line_items.read` | View properties and other details about line items | Line items endpoints | Any account |
| `crm.objects.line_items.write` | Create, delete, or make changes to line items.  | Line items endpoints | Any account |
| `crm.objects.marketing_events.read` | View details about marketing events.  | Marketing events endpoints | Any account |
| `crm.objects.marketing_events.write` | Create, delete, or make changes to marketing events.  | Marketing events endpoints | Any account |
| `crm.objects.owners.read` | View details about users assigned to a CRM record. | Owners endpoints | Any account |
| `crm.objects.quotes.read` | View properties and other details about quotes and quote templates. | Quote endpoints | Any account |
| `crm.objects.quotes.write` | Create, delete, or make changes to quotes. | Quote endpoints | Any account |
| `crm.schemas.companies.read` | View details about property settings for companies | Properties endpoints | Any account |
| `crm.schemas.companies.write` | Create, delete, or make changes to property settings for companies. | Properties endpoints | Any account |
| `crm.schemas.contacts.read` | View details about property settings for contacts. | Properties endpoints. | Any account |
| `crm.schemas.contacts.write` | Create, delete, or make changes to property settings for contacts. | Properties endpoints | Any account |
| `crm.schemas.custom.read` | View details about custom object definitions in the HubSpot CRM. | Custom objects endpoints | Any _Enterprise_ |
| `crm.schemas.deals.read` | View details about property settings for deals. | Properties endpoints | Any account |
| `crm.schemas.deals.write` | Create, delete, or make changes to property settings for deals. | Properties endpoints | Any account |
| `crm.schemas.line_items.read` | View details about line items. | Line items endpoints | Any account |
| `crm.schemas.quotes.read` | View details about quotes and quotes templates. | Quote endpoints | Any account |
| `settings.billing.write` | Make changes to your account's billing settings. This includes managing and assigning paid seats for users. | Settings endpoints | Any account |
| `settings.currencies.read` | Reads existing exchange rates along with the current company currency associated with your portal.  | Account information endpoints | Any account |
| `settings.currencies.write` | Create, update and delete exchange rates along with updating the company currency associated with your portal.  | Account information endpoints | Any account |
| `settings.users.read` | View details about account users and their permissions. | User Provisioning endpoints | Any account |
| `settings.users.write` | Manage users and user permissions on your HubSpot account. This includes creating new users, assigning permissions and roles, and deleting existing users.  | User Provisioning endpoints | Any account |
| `settings.users.teams.read` | See details about the account's teams.  | User Provisioning endpoints | Any account |
| `settings.users.team.write` | Assign users to teams on your HubSpot account.  | User Provisioning endpoints | Any account |
| `account-info.security.read` | Includes access to account activity logs and other account security information.  | Account activity API | Any account |
| `accounting` | Allows HubSpot and the accounting integration to share invoice, product, and contact details. | Accounting Extension API | Any account |
| `actions` | Add forms to the contact's pages that do custom actions. | CRM Extensions API | Any account |
| `analytics.behavioral_events.send` | Includes access to send custom behavioral events.  | Analytics API | _**Marketing Hub**_ _Enterprise_ |
| `automation` | This includes workflows. | Automation API (Workflows endpoints) | _**Marketing Hub**_ _Professional_ or _Enterprise_ |
| `behavioral_events.event_definitions.read_write` | Create, read, update, or delete behavioral events. This includes behavioral event properties.  | Analytics API | _**Marketing Hub**_ _Enterprise_ |
| `business_units.view.read` | View business unit data, including logo information. | Business Units API | Business Units Add-on |
| `business-intelligence` | This includes endpoints that sit on top of sources and email. | Analytics API | Any account |
| `collector.graphql_query.execute` | Query data from your HubSpot account using the GraphQL API endpoint | GraphQL API endpoint | **_CMS Hub_** _Professional_ or _Enterprise_ |
| `collector.graphql_schema.read` | Perform introspection queries via GraphQL application clients such as GraphiQL | GraphiQL and other 3rd party GraphQL clients | _**CMS Hub** Professional_ or _Enterprise_ |
| `communication_preferences.read` | View details of your contacts' subscription preferences.  | Subscription Preferences API | Any account |
| `communication_preferences.read_write` | Subscribe/unsubscribe contacts to your subscription types. It won't subscribe contacts who have unsubscribed.  | Subscription Preferences API | Any account |
| `communication_preferences.write` | Subscribe/unsubscribe contacts to your subscription types. It won't subscribe contacts who have unsubscribed.  | Subscription Preferences API | Any account |
| `content` | This includes sites, landing pages, email, blog, and campaigns. | CMS API and Calendar, Email and Email Events endpoints | _**CMS Hub**_ _Professional_ or _Enterprise,_ or _**Marketing Hub**_ _Professional_ or _Enterprise_ |
| `conversations.read` | View details about threads in the conversations inbox. | Conversations inbox and messages API | Any account |
| `conversations.visitor_identification.tokens.create` | Fetch identification tokens for authenticated website visitors interacting with the HubSpot chat widget. | Visitor Identification API | Any _Professional_ or _Enterprise_ |
| `conversations.write` | Send messages in conversations. Create and update message threads. | Conversations inbox and messages API | Any account |
| `crm.export` | Export records from your CRM for all CRM data types. | CRM Exports API |  Any account |
| `crm.import` | Allows you to import records into your CRM. This includes creating new records or modifying any of your existing records for all CRM data types (contacts, companies, deals, tickets, etc). It doesn't include archiving or deleting any data. | CRM Imports API | Any account |
| `ctas.read` | Allows read access for CTAs. | No publicAPI available | _**Marketing Hub** or **CMS Hub**_ _Starter, Professional or Enterprise_ |
| `e-commerce` | This includes access to e-commerce features. | Products and line items endpoints | 

Any account

**Note:** Only _Professional_ and _Enterprise_ accounts can use this scope for the Products API.

 |
| `external_integrations.forms.access` | Includes the ability to rename, delete, and clone existing forms. | Forms endpoints | 

Any account

 |
| `files` | This includes access to File Manager. | Files (File Manager) and file mapper (CMS templates, modules, and layout) endpoints | Any account |
| `files.ui_hidden.read` | View details or download user files, attachments, and system files from all HubSpot tools.  | Files (File Manager) and file mapper (CMS templates, modules, and layout) endpoints | Any account |
| `forms` | This includes access to the Forms endpoints. | Forms endpoints | Any account |
| `forms-uploaded-files` | Download files submitted through a form. | Get a file uploaded via form submission endpoint | Any account |
| `hubdb` | This includes access to HubDB. | HubDB endpoints | _**CMS Hub**_ _Professional_ or _Enterprise_, or _**Marketing Hub**_ _Professional_ or _Enterprise_ with [Website Add-on](https://www.hubspot.com/products/website?_ga=2.66722414.1955409981.1585246367-500942594.1573763828&_gac=1.195636702.1585338011.CjwKCAjwsMzzBRACEiwAx4lLGyhm1kRPOqA4ECRGjXC9E1lqLmkjAkm_n327nPunuhr5z2D0LTrIyhoCCX0QAvD_BwE) |
| `integration-sync` | This exposes the sync API, which allows syncing of most CRM objects. | Ecommerce Bridge API | Any account |
| `media_bridge.read` | Grants access to events and objects from the media bridge. | Media Bridge API | Any account |
| `media_bridge.write` | Grants access to create and update events and objects from the media bridge. | Media Bridge API | Any account |
| `oauth` | Basic scope required for OAuth. This scope is added by default to all apps. |   | Any account |
| `sales-email-read` | Grants access to read all details of one-to-one emails sent to contacts. | Engagements endpoints  
  
**Note:** This scope is required to get the content of email engagements. See the [Engagements overview](/docs-beta/crm/engagements#email-content) for more details. | Any account |
| `social` | This includes Social Inbox. | Social Media API | _**Marketing Hub**_ _Professional_ or _Enterprise_ |
| `tickets` | This includes access to tickets. | Tickets endpoints | Any accounbt |
| `timeline` | Grants access to manage custom events on HubSpot CRM records. This includes creating or updating records. | Timeline Events endpoints | Any account |
| `transactional-email` | This includes transactional emails and the transactional emails endpoints. | Transactional email endpoints | Marketing Hub Professional or Enterprise with [Transactional Email Add-on](https://www.hubspot.com/products/email/transactional-email?_ga=2.6502002.1955409981.1585246367-500942594.1573763828&_gac=1.45687254.1585338011.CjwKCAjwsMzzBRACEiwAx4lLGyhm1kRPOqA4ECRGjXC9E1lqLmkjAkm_n327nPunuhr5z2D0LTrIyhoCCX0QAvD_BwE) |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/scopes#page-feedback)
-----------------------------------------------------------------------------------

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
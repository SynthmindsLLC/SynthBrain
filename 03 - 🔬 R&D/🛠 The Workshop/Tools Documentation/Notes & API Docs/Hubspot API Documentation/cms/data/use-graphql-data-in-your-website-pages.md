Use data from a GraphQL query in your website pages


=======================================================

Last updated: April 15, 2024

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Professional or Enterprise

[GraphQL](https://graphql.org/) allows you to create data queries that access your HubSpot CRM and HubDB data to create personalized and data-driven experiences for your website visitors. Learn more about how GraphQL works and how to create a query [here](/docs/cms/data/query-hubspot-data-using-graphql).

You can learn more about building data-based pages in HubSpot Academy's [Data-Driven Content course](https://app.hubspot.com/academy/tracks/1148948/intro).

Once you're familiar with how GraphQL works and you've written a query that specifies the data you'll need, you can use the query in your theme.

*   Save your query in a file with the .graphql extension. It's recommended you keep GraphQL query files in a separate directory at the root of your theme to keep them organized and make them easier to reference with a relative path.
*   Upload a theme that includes the query file [using the HubSpot CLI tools](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cli#upload), or [through the design manager](https://knowledge.hubspot.com/design-manager/a-quick-tour-of-the-design-manager#creating-new-templates-and-files) in your HubSpot account. 

Once you've uploaded your GraphQL files, you can bind them to a module or template, which will make the query's data available to the rendering context of the module or template.

Bind a data query to a template[](https://developers.hubspot.com/docs/cms/data/use-graphql-data-in-your-website-pages#bind-a-data-query-to-a-template)
------------------------------------------------------------------------------------------------------------------------------------------------------

To bind a GraphQL query to a template so you can reference the data in your code, add a `dataQueryPath` template annotation and provide the path to the associated GraphQL query file. You don't need to include the file's _.graphql_ extension in the path.

For example, if you want to bind a query file to a template that renders the query's results on the page, the top of your template's code would include the following:

<!-- templateType: page isAvailableForNewContent: true label: Contact profile page - GraphQL dataQueryPath: ../data-queries/contact\_info -->

You can then reference the response to the data query in your template and module code from the `data_query` variable in HubL. The example below defines a HubL variable to store available roles:

{% set contactData = data\_query.data.CRM.contact %}

Bind a data query to a module[](https://developers.hubspot.com/docs/cms/data/use-graphql-data-in-your-website-pages#bind-a-data-query-to-a-module)
--------------------------------------------------------------------------------------------------------------------------------------------------

You can bind a GraphQL query to a module using the design manager.

*   In your HubSpot account, navigate to **Marketing** > **Files and Templates** > **Design Tools**.
*   At the top of the finder, click the File dropdown menu and select **New file**.
*   In the dialog box, click the **What would you like to build today?** dropdown menu and select **GraphQL**.
*   Click **Next**.
*   Enter a **file name**, then confirm the location for your GraphQL file.
*   Copy and paste your query into the editor, then click **Publish changes**.
*   Navigate to the module you want to use with your query. Under _Linked files_, click the **GraphQL file** dropdown menu, then select your query.

![bind-graphql-query-to-module-in-design-manager](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/bind-graphql-query-to-module-in-design-manager.png?width=342&name=bind-graphql-query-to-module-in-design-manager.png)

You can then reference the response of your query in your module code using the `data_query` variable. The example below defines a HubL variable to store the queried data for a collection of contacts:

{% set contactCollectionData = module.data\_query.data.CRM.contact\_collection %}

If you're developing locally, you may prefer to bind a GraphQL query directly to a module by including a `data_query_path` parameter in your module's meta.json file. It's recommended you define your module within a _modules_ directory at the root of your theme to make it easier to reference your query with a relative path.

*   Using the HubSpot CLI tools, [fetch](/docs/cms/developer-reference/local-development-cli#fetch) the module's directory. 
*   Add the `data_query_path` parameter and specify the path to the associated GraphQL query file, relative to the location of the meta.json file. For example, if the query file is in a _data-queries_ directory at the root of your theme, your meta.json file would include the following:

// meta.json { "data\_query\_path": "../../data-queries/contactsQuery" }

*   Upload the updated meta.json file to your HubSpot account.

Pass dynamic context into a query[](https://developers.hubspot.com/docs/cms/data/use-graphql-data-in-your-website-pages#pass-dynamic-context-into-a-query)
----------------------------------------------------------------------------------------------------------------------------------------------------------

If your query requires context that is dynamic to a given request, such as data from a contact who's visiting one of your pages, you can pass [HubL variables](/docs/cms/hubl/variables) in your GraphQL queries. 

*   First, define the variable in a single line comment at the top of your query using the `#` character. The convention for GraphQL variable names is to prefix them with a `$` character. For example, to define a variable for the ID of a contact:

`# $contact_id = "{{ request.contact.contact_vid || ''}}"`  

*   Include your variable and its type as a parameter in your query definition. If you want your variable to non-nullable, add an `!` after its type. To pass the `$contact_id` variable above into a query to show contact info for a given contact, your query definition would begin with:

`query contact_info($contact_id: String!)`

*   You can then reference your variable and provide it as an argument to any of the filters in your query. Using the `$contact_id` variable from above, the query below would provide the first name, last name, and email of a contact visiting a page:

\# label: "Contact info page" # description: "Show a contact's name and email" # $contact\_id: "{{request.contact.contact\_vid }}" query contact\_info($contact\_id: String!) { CRM { contact(uniqueIdentifier: "id", uniqueIdentifierValue: $contact\_id) { \_metadata { id } firstname lastname email } } }

*   You can also pass URL query string parameters as arguments to your GraphQL query using the `request.query_dict` HubL variable. For example, if you have a page URL that contained _/contacts?location=Boston&department=marketing_, and wanted to use the URL query parameters in your GraphQL query to filter contacts by location and department, you could use the following GraphQL query:

\# label: "Contact listing page with filters" # description: "Filter contacts by location and department" # $location: "{{ request.query\_dict.location || ''}}" # $department: "{{ request.query\_dict.department || ''}" query contact\_listing\_page($location: String!, department: $String) { CRM { contact\_collection(filter: {location\_\_eq: $location, department\_eq: $department) { items { \_metadata { id } firstname lastname email } } } }

Create dynamic pages using query data[](https://developers.hubspot.com/docs/cms/data/use-graphql-data-in-your-website-pages#create-dynamic-pages-using-query-data)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

You use directives in your GraphQL queries to dynamically generate pages based on certain properties from your CRM data. Each dynamic page will pull its metadata from the directives you annotate in your query. The values you define for each directive should uniquely identify the content of the page to stand out in search results.

This metadata includes the following directives:

| Dynamic page directive | Description |
| --- | --- |
| `web_page_canonical_url` | The canonical URL of the page |
| `web_page_featured_image` | The page's featured image, which will appear when the page is shared. |
| `web_page_meta_description` | The page's meta description |
| `web_page_title` | The page's title |

In addition to these directives, you'll also need to choose a custom property to use as a unique identifier in your query if you're querying CRM data. This property must be configured with `"hasUniqueValue": true`. Existing properties cannot be updated to have this parameter, so you'll need to [create a new property through the API](/docs/api/crm/properties) if you don't already have one.

### Create a query and module for your dynamic pages[](https://developers.hubspot.com/docs/cms/data/use-graphql-data-in-your-website-pages#create-a-query-and-module-for-your-dynamic-pages)

To create a query you can use with dynamic pages:

*   Include a `label` and `description` for your query as single line comments at the top of your query. Then add another single line comment for an identifier to associate with the dynamic slug of your page:
    *   Set the name of your identifier to the `dynamic_slug` field provided by the `request.path_param_dict` HubL variable. 
    *   For example, if you're creating a query to dynamically create profile pages for your contacts, and you want to use a custom property named `profile_full_name` as the slug for each contact's profile page, the following comment would be included above the query definition:

`#$profile_full_name: {{ request.path_param_dict.dynamic_slug }}`

*   Include an ID field in your query that matches your data source:
    *   If you're querying `CRM` data, include the `hs_object_id` field.
    *   If you're querying data from a `HUBDB` table, include the `hs_id` field. 
*   Annotate the fields of your query with the corresponding metadata directive from the table above, prefacing each directive with the `@` character. For example, to configure the title, meta description, and featured image for a contact profile page:

\# label: "Contact profile" # description: "Contact profile query for showing details for a single contact" # $profile\_full\_name: {{ request.path\_param\_dict.dynamic\_slug }} query contact\_profile\_page($profile\_full\_name: String!) { CRM { contact(uniqueIdentifier: "profile\_full\_name", uniqueIdentifierValue: $profile\_full\_name) { hs\_object\_id email profile\_full\_name @web\_page\_title profile\_description @web\_page\_meta\_description profile\_picture\_url @web\_page\_featured\_image } } }

*   Save your query in a file with the .graphql extension. As you design your module, you can access the data from your query using the `data_query` HubL variable.

### Create a listing page query and module[](https://developers.hubspot.com/docs/cms/data/use-graphql-data-in-your-website-pages#create-a-listing-page-query-and-module)

Depending on your use case, you may want the dynamic page's root URL to display a listing of your object's records. In the example above, a website visitor who navigated to _https://website.com/profiles_ would be presented with a listing of all contact profiles. To set up a listing page:

*   Create another GraphQL query to retrieve a collection of the associated object records you'll need for the listing page.
    *   Add a label, description, and any other variables you need to pass to your query as single line comments at the top of your query.
    *   Include any [filters](#query-arguments-and-filters) you might need as arguments to your collection field.

\# label: "Profile listing" # description: "Contact profile listing query for showing all profiles with a "hubspot.com" email address" query contact\_listing { CRM { contact\_collection(filter: {email\_\_contains: "hubspot.com"}) { email profile\_full\_name } } }

*   Save your listing page query with the .graphql extension, then follow the instructions above to bind your query to a listing page module.

### Create website pages[](https://developers.hubspot.com/docs/cms/data/use-graphql-data-in-your-website-pages#create-website-pages)

Once you've created your queries and bound them to their associated modules, you can use the modules in a listing page and a details page.

*   To create a listing page:
    *   Create a new page, selecting a page template that has a drag and drop area or flexible column.
    *   In the page editor, click the **Settings** tab.
    *   Enter a **page title**.
    *   Under _Page URL_, enter a **content slug** that corresponds to the collection that you're retrieving for your dynamic pages. Following the example above, the content slug would be `/profiles`.
    *   Enter a **meta description** for the listing page, then click the **Content** tab to return to the editor.
    *   In the left sidebar, in the _Add_ tab, search for your listing page module, then drag it into the page editor.
    *   After you're done designing your page, publish it by clicking **Publish** in the upper right.
*   Next, set up the details page:
    *   [Create a new page](https://knowledge.hubspot.com/website-pages/create-and-customize-pages), selecting a page template that has a drag and drop area or flexible column.
    *   In the page editor, click the **Settings** tab.
    *   Enter a **page** **title**.
    *   Under _Page URL_, click the **pencil icon** to edit the page's URL. Set the URL to where you want your listing page to appear. In the example above, the listing page will be at: `/profiles`, so the full content slug for the page should be `/profiles/[:dynamic-slug]`.
    *   Click **Advanced options**, then scroll to the _Dynamic pages_ section.
    *   Under _Dynamic pages_, click the **Data source** dropdown menu, then select the **label** that matches the one you included at the top of your GraphQL query.
    *   Click the **Content** tab at the top of the page to return to the editor. 
    *   In the left sidebar, in the _Add_ tab, search for your details module and drag it into the page editor.
    *   When you're ready, publish your page by clicking **Publish** in the upper right.

Further reading[](https://developers.hubspot.com/docs/cms/data/use-graphql-data-in-your-website-pages#further-reading)
----------------------------------------------------------------------------------------------------------------------

Learn more about how to construct, test, and refine your GraphQL query [here](/docs/cms/data/query-hubspot-data-using-graphql).

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/data/use-graphql-data-in-your-website-pages#page-feedback)
------------------------------------------------------------------------------------------------------------------------

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
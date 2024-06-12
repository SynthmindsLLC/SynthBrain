---
Please provide me with more context! To help you write a compelling mission statement, I need to know: "* **What is the purpose of this mission?** Is it for a company, a project, a personal goal, or something else? "
* **What are the core values or beliefs that guide this mission?**  What do you want to achieve or contribute?
* **What is the desired outcome of this mission?**  What impact do you want to have?

Once I have this information, I can help you craft a clear, concise, and impactful mission statement.
---

Create emails with programmable content


===========================================

Last updated: December 4, 2023

This feature is currently in beta. By using this functionality you agree to the [developer beta terms](https://legal.hubspot.com/developerbetaterms). This guide refers to functionality available only through that beta. [Opt-into the beta in your templates or modules.](https://knowledge.hubspot.com/email/create-programmable-emails)

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Professional or Enterprise

Using programmable content to personalize emails with data from your HubSpot account using HubL. 

The data sources you can use in a programmable email depend on your HubSpot subscription:

*   If you have a **_Marketing Hub_** _Professional_ subscription, you can use data from standard CRM objects, such as contacts, companies, and products.
*   If you have a **_Marketing Hub_** Enterprise subscription, you can also use structured data sources such as [HubDB](https://developers.hubspot.com/docs/cms/features/hubdb) tables and [custom objects](https://knowledge.hubspot.com/crm-setup/use-custom-objects). This data can be filtered based on the contact properties of the recipient.

For example, a real estate website could have prospects fill out a form with their home needs. The form submission could then trigger a workflow that sends the prospect an email with homes they may be interested in.

Email sending limits[](https://developers.hubspot.com/docs/cms/guides/email/hubdb-crm-objects#email-sending-limits)
-------------------------------------------------------------------------------------------------------------------

You can include the [crm\_object](/docs/cms/hubl/functions#crm-object), [crm\_objects](/docs/cms/hubl/functions#crm-objects), and [crm\_associations](/docs/cms/hubl/functions#crm-associations) CRM HubL functions in a programmable email, but any email that includes these specific functions are subject to the following limits that are based on the number of recipients you're sending to:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; border: 1px solid #99acc2; height: 431.979px;"><tbody><tr style="height: 71.9965px;"><td style="width: 49.9181%; padding: 4px; height: 71.9965px; background: #E5EBF3;"><strong>Total recipients</strong></td><td style="width: 49.9206%; padding: 4px; height: 71.9965px; background: #E5EBF3;"><strong>Maximum number of CRM HubL functions</strong></td></tr><tr style="height: 71.9965px;"><td style="width: 49.9181%; padding: 4px; height: 71.9965px;">500,000</td><td style="width: 49.9206%; padding: 4px; height: 71.9965px;">1</td></tr><tr style="height: 71.9965px;"><td style="width: 49.9181%; padding: 4px; height: 71.9965px;">250,000</td><td style="width: 49.9206%; padding: 4px; height: 71.9965px;">2</td></tr><tr style="height: 71.9965px;"><td style="width: 49.9181%; padding: 4px; height: 71.9965px;">165,000</td><td style="width: 49.9206%; padding: 4px; height: 71.9965px;">3</td></tr><tr style="height: 71.9965px;"><td style="width: 49.9181%; padding: 4px; height: 71.9965px;">125,000</td><td style="width: 49.9206%; padding: 4px; height: 71.9965px;">4</td></tr><tr style="height: 71.9965px;"><td style="width: 49.9181%; padding: 4px; height: 71.9965px;">100,000</td><td style="width: 49.9206%; padding: 4px; height: 71.9965px;">5</td></tr></tbody></table>

Sending an email that meets or exceeds one of the limits above will delay or cancel the sending of your email.

In addition to the limits outlined above, be aware of the additional caveats listed below:

*   If you clone a programmable email, it cannot be sent while the original is still in a processing state. You should wait at least 1 hour between each email send.
*   You cannot conduct an A/B test for a programmable email that includes a `crm_object`, `crm_objects`, or `crm_associations` HubL function.

1\. Create a programmable email module[](https://developers.hubspot.com/docs/cms/guides/email/hubdb-crm-objects#create-a-programmable-email-module)
---------------------------------------------------------------------------------------------------------------------------------------------------

To create the email module to access your HubDB or custom object data:

*   In your HubSpot account, navigate to **Marketing** > **Files and Templates** > **Design Tools**.
*   In the upper left, click **File**, then select **New file**.
*   In the dialog box, select **Module** for the file type, then click **Next**. Then, select the **Emails** checkbox and enter a **name** for the file.
*   Click **Create**. 
*   To enable programmable email for the module:  
    *   In the inspector on the right, toggle the **Enable module for programmable email beta** switch on. ![programmable-email-switch0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/programmable-email-switch0.png?width=358&name=programmable-email-switch0.png)

*   You can also enable programmable email for a coded email template by adding `isEnabledForEmailV3Rendering: true` to the top of the file.   
    
    ![enable-design-manager-template-for-programmable-email](https://developers.hubspot.com/hs-fs/hubfs/Imported%20sitepage%20images/enable-design-manager-template-for-programmable-email.png?width=510&name=enable-design-manager-template-for-programmable-email.png)
    

With the module created, you'll then add code to access data from your CRM. The following examples below demonstrate how to query from different data sources.

### Standard objects[](https://developers.hubspot.com/docs/cms/guides/email/hubdb-crm-objects#standard-objects)

You can use the HubL functions such as [crm\_object](/docs/cms/hubl/functions#crm-object), [crm\_objects](/docs/cms/hubl/functions#crm-objects), and [crm\_associations](/docs/cms/hubl/functions#crm-associations) to query data from standard objects in your account, such as contacts, companies, or products.

The code below uses the [`crm_object`](/docs/cms/hubl/functions#crm-object) HubL function to query the data from a product with an ID of `2444498793` and render the name, description, and price:

{% set product = crm\_object("product", 2444498793, "name,description,price") %} <div> <p> <span>Name: </span> <span>{{ product.name }}</span> </p> <p> <span>Description: </span> <span>{{ product.description }}</span> </p> <p> <span>Price: </span> <span>{{ product.price }}</span> </p> </div>

### Custom objects[](https://developers.hubspot.com/docs/cms/guides/email/hubdb-crm-objects#custom-objects)

If you have a _Marketing Hub Enterprise_ account, you can query data from a custom object you've created in your account.

The code below retrieves data from a custom object named _Property_, returning values (e.g. location, price) stored in the custom object's properties.

Note that the example below uses the custom object's fully qualified name as the first argument when invoking the `crm_objects` [HubL function](/docs/cms/hubl/functions#crm-objects).

*   The fully qualified name begins with the HubSpot account ID (prefixed by `p`), followed by an underscore and the lower-cased plural name of the custom object (e.g., `properties`).
*   You can retrieve an object's `fullyQualifiedName` by making a `GET` request to the [CRM Objects schema API](/crm-custom-objects).

{% set real\_estate\_listings = crm\_objects("p2990812\_properties", "", "listing\_name,location, price, address, type") %} {% for home in real\_estate\_listings.results %} {{ home.address}} <br> {{ home.price }} <br> <img alt="{{ home.name }}" src="{{ home.hero\_image }}" style="outline: none; max-width: 100%;" width="260px" /> <br> <hr> {% endfor %}

**Please note:** if the name of your custom object contains hyphens (e.g., _My-Custom-Object_), its properties can not be rendered in a programmable email. You can recreate the custom object with the hyphens omitted [directly in your HubSpot account](https://knowledge.hubspot.com/crm-setup/create-custom-objects), or you can use the [custom object API](/docs/api/crm/crm-custom-objects).

To filter the data returned for each recipient, you can add a `query` parameter, which will filter the results by the recipient's contact properties. View the [full list of filter options](https://legacydocs.hubspot.com/docs/methods/hubdb/v2/get_table_rows).

{% set query = "price\_\_lte="~contact.budget\_max|int~"&price\_\_gte="~contact.budget\_min|int~"&city="~contact.city~"&order=listing\_name" %} {% set real\_estate\_listings = crm\_objects("p2990812\_Property", query, "listing\_name,location, price, address, type") %} {% for home in real\_estate\_listings.results %} ... {% endfor %}

### HubDB[](https://developers.hubspot.com/docs/cms/guides/email/hubdb-crm-objects#hubdb)

If you have a Marketing Hub Enterprise account, you can use data from a HubDB table in your email.

The code below uses the `[hubdb_table_rows](https://developers.hubspot.com/docs/cms/hubl/functions#hubdb-table-rows)` HubL function to retrieve all data from the table. This will list all the real estate properties in the email, outputting the details of each property along with their image.

{% set real\_estate\_listings = hubdb\_table\_rows(1234567) %} {% for home in real\_estate\_listings%} {{ home.address}} <br> {{ home.price }} <br> <img alt="{{ home.name }}" src="{{ home.hero\_image.url }}" style="outline: none; max-width: 100%;" width="260px" /> <br> <hr> {% endfor %}

To filter the data returned for each recipient, you can add a `query` parameter, which will filter results by the specified contact properties. View the [full list of filter options](/docs/api/cms/hubdb#filter-returned-rows).

{% set query = "price\_\_lte="~contact.budget\_max|int~"&price\_\_gte="~contact.budget\_min|int~"&persona="~contact.hs\_persona.value~"&order=listing\_name" %} {% for home in real\_estate\_listings %} ... {% endfor %}

In the above example, the contact property _Budget max_ is referenced with `contact.budget_max`, while _Persona_ is referenced  with `contact.hs_persona.value`. This is because _Persona_ is an [enumeration property](https://knowledge.hubspot.com/account/property-field-types-in-hubspot), which requires an additional `.value` to parse the property's value, while other property types do not.

2\. Add the module to an email[](https://developers.hubspot.com/docs/cms/guides/email/hubdb-crm-objects#add-the-module-to-an-email)
-----------------------------------------------------------------------------------------------------------------------------------

With the module published, you'll now add it to the body of the drag and drop email.

*   In your HubSpot account, navigate to Marketing > Email.
*   Select the email that you created.
*   In the left sidebar, under _Content_, click **More**. Find your programmable email module, then drag it into the email body.

![drag-and-drop-email-editor-more-modules](https://developers.hubspot.com/hubfs/Knowledge_Base_2021/Developer/drag-and-drop-email-editor-more-modules.png "drag-and-drop-email-editor-more-modules")

If you've set up the module to filter data by specific contact properties, the email preview will appear blank. This is because the email tool hasn't been set to preview the email by a specific contact.

To preview what the email will look like for a specific contact:

*   In the upper right, click **Actions**, then select **Preview**. ![email-actions-menu0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/email-actions-menu0.png?width=302&name=email-actions-menu0.png)
*   On the next screen, click the **Preview as a specific contact** dropdown menu, then select a **contact**. ![preview-email-as-specific-contact0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/preview-email-as-specific-contact0.png?width=450&name=preview-email-as-specific-contact0.png) 

You should now see only the data relevant to the recipient, filtered by their contact properties.

![Screenshot of Email Preview](https://developers.hubspot.com/hubfs/preview%20window.png "Screenshot of Email Preview")

It's important to always have fallback data to send in the case that there are no HubDB rows or custom object records that meet the criteria you've set. Otherwise, the recipient might receive a blank email.

This beta may cause issues with existing templates. It's important to test any changes thoroughly before publishing and sending a live email.

More HubDB focused tutorials[](https://developers.hubspot.com/docs/cms/guides/email/hubdb-crm-objects#more-hubdb-focused-tutorials)
-----------------------------------------------------------------------------------------------------------------------------------

*   [Building dynamic pages with HubDB](https://developers.hubspot.com/docs/cms/guides/building-dynamic-pages-with-hubdb)
*   [How to join multiple HubDB tables](https://designers.hubspot.com/tutorials/how-to-join-hubdb-tables?_ga=2.184951017.170051683.1600090415-183703055.1599146624)
*   [How to build a dynamic team member page with HubDB](https://designers.hubspot.com/docs/tutorials/how-to-build-a-dynamic-team-member-page-with-hubdb)
*   [How to build multilevel dynamic pages using HubDB](https://designers.hubspot.com/how-to-build-multilevel-dynamic-templates)

HubSpot Academy[](https://developers.hubspot.com/docs/cms/guides/email/hubdb-crm-objects#hubspot-academy)
---------------------------------------------------------------------------------------------------------

*   [Using HubDB and Custom Objects in CMS Hub](https://academy.hubspot.com/lessons/other_data_sources_hubdb_and_custom_objects)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/email/hubdb-crm-objects#page-feedback)
-----------------------------------------------------------------------------------------------------------

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
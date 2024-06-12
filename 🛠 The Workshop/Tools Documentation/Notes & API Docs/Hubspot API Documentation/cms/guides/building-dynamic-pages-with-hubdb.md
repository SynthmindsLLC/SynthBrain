---
Please provide me with more context! I need to know what the mission is about to help you write it. 

For example, tell me: "* **What is the mission for?** (A company, a project, a person, a team, etc.)"
* **What are the goals of this mission?** (What do you want to achieve?)
* **What are the values that guide this mission?** (What principles are important?)
* **Who is the target audience for this mission statement?** (Who are you trying to reach?)

Once I have this information, I can help you write a compelling and effective mission statement!
---

Build dynamic pages using HubDB


===================================

Last updated: February 29, 2024

[Dynamic pages](/docs/cms/data/dynamic-pages) are CMS pages that get their content from a structured data source. Based on how you configure your dynamic page, HubSpot will pull data from the selected source and automatically create a set of pages. This includes a listing page that displays summaries of the data, and individual pages for each data source entry.

Using a [HubDB table](/docs/cms/features/hubdb) as a data source, you can create a dynamic page which then generates a page for each row in the table. Each dynamic page includes its own unique, SEO-friendly URL, and offers page-specific analytics. 

This tutorial walks through how to create a set of dynamic pages using HubDB as the data source. To follow this tutorial, you'll need:

*   _**CMS Hub** Professional_ or _Enterprise_
*   Some prior knowledge of HTML and CSS

You can learn more about building data-based CMS pages in HubSpot Academy's [CMS Data-Driven Content course](https://app.hubspot.com/academy/tracks/1148948/intro).

1\. Create a HubDB table[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#create-a-hubdb-table)
-------------------------------------------------------------------------------------------------------------------

To create a new HubDB table:

*   In your HubSpot account, navigate to **Marketing** > **Files and Templates** > **HubDB**.
*   In the upper right, click **Create table**.
*   In the dialog box, enter the table **label** and **name**, then click **Create**.

With the table created, you can set it to be used for dynamic page content:

*   In the upper right, click **Actions**, then select **Manage settings**.
*   In the right panel, click to toggle the **Enable creation of dynamic pages using row data** switch on.
*   You can optionally select the meta description, featured image, and canonical URL of the individual dynamic pages. If you leave these values empty, each page will inherit the respective values from its parent page.

**Please note:** for a page to use the values from the meta description, featured image, and canonical URL columns, the page must include the following `page_meta` HubL variables rather than `content` variables:

*   `{{page_meta.meta_description}}`
*   `{{page_meta.featured_image_URL}}`
*   `{{page_meta.canonical_url}}`

For example, HubSpot templates pull in their meta description from the `{{content.meta_description}}` tag by default. You'll instead need to use `{{page_meta.meta_description}}`.

*   Click **Save** to save your changes.

![hubdb-table-settings-sidebar-save](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hubdb-table-settings-sidebar-save.png?width=400&height=672&name=hubdb-table-settings-sidebar-save.png "hubdb-table-settings-sidebar-save")

After you update the table settings, the _Page title_ and _Page path_ columns will be added to the table.

*   **Page title:** the name of this page as seen in the HTML title tag.
*   **Page path:** the last segment of the URL for the dynamic page created by each row in the table. 

The following table is an example modeled after an "About us" page for members of a company's executive team. This table will be used to create dynamic pages with paths ending in `cfo-harlow`, `ceo-jeff`, `cto-bristow`, and `pd-hugo`. 

| Page title | Page path | Role | Name | Bio |
| --- | --- | --- | --- | --- |
| CFO Harlow | cfo-harlow | CFO | Harlow | This is Harlow, who is generally pennywise. |
| CEO Jeff | ceo-jeff | CEO | Jeff | Jeff is the CEO, which means he usually runs things around here. |
| CTO Bristow | cto-bristow | CTO | Bristow | This is our CTO, Bristow, who likes to tinker. |
| Chief PD | pd-hugo | CPD | Hugo | Hugo, our Chief Product Designer, enjoys designing products. |

![example-hubdb-table](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/example-hubdb-table.png?width=1348&height=537&name=example-hubdb-table.png "example-hubdb-table")

**Please note:** though you have to enter page paths as lowercase, the resulting URLs are case insensitive. In the example above, when someone navigates to `/CEO-Jeff` they will see the same page as `/ceo-jeff` instead of a 404 error.

When you're ready to use the data from your table to build out your pages, click Publish in the top right.

2\. Create a template[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#create-a-template)
-------------------------------------------------------------------------------------------------------------

Next, you'll create one template for both the listing page and the individual detail pages for each row, similar to how blog templates can be used for both listing and post detail pages. To create the page template:

*   In your HubSpot account, navigate to **Marketing** \> **Files and Templates** > **Design Tools**.
*   In the left sidebar menu, navigate to the folder that you want to create the template in. To create a new folder, in the upper left click **File**, then select **New folder**. Then, click **File**, and select **New file**.
*   In the dialog box, use the **dropdown menu** to select **HTML + HubL** as the file type.
*   Click **Next**.

![Creating a new HTML + HubL Template](https://developers.hubspot.com/hs-fs/hubfs/Developer%20Site/assets/images/create-html-hubl-template.jpg?width=800&height=469&name=create-html-hubl-template.jpg "Creating a new HTML + HubL Template")

*   In the **File name** field, enter the name of the template.
*   Under _File location_, you can change where the template is located in your design manager by clicking **Change**_._
*   Click **Create** to create the template.

When a dynamic page is set to use this template and the end of the page URL matches the path column, you can access the `dynamic_page_hubdb_row` and `dynamic_page_hubdb_table_id` variables in the template. For example, for building an executive profile page, the code below demonstrates how you can use fields from `dynamic_page_hubdb_row` to display an executive's info:

*   `hs_name`: the associated _Page title_ for the HubDB row.
*   `name`: the executive's name.
*   `role`: the executive's role.

{% if dynamic\_page\_hubdb\_row %} <h1>{{ dynamic\_page\_hubdb\_row.hs\_name }}</h1> <h2>{{ dynamic\_page\_hubdb\_row.name }}</h2> <h3>{{ dynamic\_page\_hubdb\_row.role }}</h3> <p>{{dynamic\_page\_hubdb\_row.bio}}</p> {% endif %}

Next, you can add handling for the case in which someone loads your dynamic page without any additional paths from your table. Usually, this is used as a listing page, for listing links to the pages for the rows in your HubDB table. Replace your code with:

{% if dynamic\_page\_hubdb\_row %} <h1>{{ dynamic\_page\_hubdb\_row.hs\_name }}</h1> <h2>{{ dynamic\_page\_hubdb\_row.name }}</h2> <h3>{{ dynamic\_page\_hubdb\_row.role }}</h3> <p>{{dynamic\_page\_hubdb\_row.bio}}</p> {% elif dynamic\_page\_hubdb\_table\_id %} <ul> {% for row in hubdb\_table\_rows(dynamic\_page\_hubdb\_table\_id) %} <li><a href="{{ request.path }}/{{ row.hs\_path }}">{{ row.hs\_name }}</a></li> {% endfor %} </ul> {% endif %}

The code inside the `elief` block iterates over all the rows in the executive's table and displays each entry in a list, with a link to their unique path.

*   In the design manager, click **Preview** to preview the template. The preview will be blank, because it relies on the context of the page to set the `dynamic_page_hubdb_row` or `dynamic_page_hubdb_table_id` variables. 
*   To test your code at the template level, add the following temporary code to the top of your template, ensuring that you remove it before publishing:

`{% set dynamic_page_hubdb_table_id = %}`

*   After adding the above code, your template should now render a list of hyperlinks, pulling data from the HubDB table you built.

![hubdb-template-preview](https://developers.hubspot.com/hubfs/Knowledge_Base_2021/Developer/hubdb-template-preview.png "hubdb-template-preview")

*   After previewing the template, remove the temporary code above. Then, click **Publish** in the top right to make it available for creating pages.

3\. Create the dynamic page[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#create-the-dynamic-page)
-------------------------------------------------------------------------------------------------------------------------

To create a dynamic page from your template:

*   With your new template open in the design manager, click the **Actions** dropdown menu at the top of the finder, then select **Create page**.  
    ![create-page-from-design-manager](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/create-page-from-design-manager.png?width=418&height=351&name=create-page-from-design-manager.png)
*   In the dialog box, select **Website page**, then enter a **page name**.
*   Click **Create page**.
*   At the top of the page editor, click the **Settings** tab.
*   In the **Page title** field, enter a page name, which you can use later to look up traffic analytics.
*   In the **URL** field, enter a **URL** of `/executives`. The URL will be the base URL for your dynamic page.
*   Click **Advanced Options** to expand additional settings.
*   Scroll down to the _Dynamic pages_ section, then click the **Data sources** dropdown menu. Select the **HubDB table** you created.

![Advanced options in page settings for linking to HubDB table](https://developers.hubspot.com/hs-fs/hubfs/page%20editor%20hubdb%20dynamic%20.png?width=600&height=788&name=page%20editor%20hubdb%20dynamic%20.png "Advanced options in page settings for linking to HubDB table")

*   When you’re finished, click **Publish** in the upper right. Your pages are now ready to view.

4\. View live pages[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#view-live-pages)
---------------------------------------------------------------------------------------------------------

Now you can visit your new dynamic page and all of its paths, as defined by your HubDB table.

*   Navigate to the dynamic listing page at the URL you set in the page editor. This tutorial uses `/executives` for its dynamic page URL, so in that case you would navigate to: `https://www.yourdomain.com/executives`.
*   From the listing page, click the **names** in the bulleted list to view the details page for that executive.

![2022-11-28_15-55-47 (1)](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/2022-11-28_15-55-47%20(1).gif?width=487&height=376&name=2022-11-28_15-55-47%20(1).gif)

5\. Add a new table row[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#add-a-new-table-row)
-----------------------------------------------------------------------------------------------------------------

With your dynamic page loading HubDB data, navigate back to the table and add a new row. After publishing the table, you'll then see your live page dynamically update with the new HubDB data.

*   In your HubSpot account, navigate to **Marketing** > **Files and Templates** > **HubDB**.
*   Click the **name** of the table that you create.
*   Click **Add row**, then fill out each column. Below is a sample set of data.

| Page title | Page path | Role | Name | Bio |
| --- | --- | --- | --- | --- |
| CMO Hobbes | cmo-hobbes | CMO | Hobbes | Hobbes is our go-to cat enthusiast. |

*   In the upper right, click **Publish**.
*   In another tab, navigate back to the listing page (`/executives` in this example). You should now see the new executive appear on the listing page, and clicking their name will reveal their details page.

6\. View dynamic page data[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#view-dynamic-page-data)
-----------------------------------------------------------------------------------------------------------------------

Once there are visits to your dynamic page, you can [measure individual page performance](https://knowledge.hubspot.com/website-pages/analyze-performance-for-individual-pages-and-blog-posts) or [view all page data in the traffic analytics tool](https://knowledge.hubspot.com/reports/analyze-your-site-traffic-with-the-traffic-analytics-tool). Even though the individual executive pages are built from the same dynamic page, traffic data, such as page views, will be attributed to each page. 

To view your page visit data in HubSpot:

*   In your HubSpot account, navigate to **Reports** > **Analytics Tools**.
*   Click **Traffic Analytics**.
*   In the traffic analytics report, click the **Pages** tab.
*   View the table to see traffic data for the individual parent and child pages. Child pages will be denoted with **\> arrow icons** to show their relation to parent pages.   
    ![example-traffic-data-2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/example-traffic-data-2.png?width=610&height=499&name=example-traffic-data-2.png)

Keep in mind the following if you're not seeing the traffic data you expect:

*   If you've [excluded your IP addresses in the account's report settings](https://knowledge.hubspot.com/reports/exclude-traffic-from-your-site-analytics), ensure that you're accessing your pages from outside your network for your page views to register.
*   It can take [up to 40 minutes](https://knowledge.hubspot.com/reports/how-often-do-analytics-in-hubspot-update) for new page data to appear in HubSpot. 

More HubDB focused tutorials[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#more-hubdb-focused-tutorials)
-------------------------------------------------------------------------------------------------------------------------------

*   [How to join multiple HubDB tables](/docs/cms/guides/hubdb/join-multiple-tables)[](/how-to-add-videos-to-dynamic-pages-in-hubdb)
*   [How to build a dynamic team member page with HubDB](https://designers.hubspot.com/docs/tutorials/how-to-build-a-dynamic-team-member-page-with-hubdb)
*   [How to add videos to dynamic pages](/docs/cms/guides/dynamic-pages/hubdb/video)
*   [How to build multilevel dynamic pages using HubDB](/docs/cms/guides/dynamic-pages/hubdb/multilevel)
*   [Let's build a page with a map using HubDB](https://designers.hubspot.com/docs/tutorials/lets-build-a-page-with-a-map-with-hubdb)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#page-feedback)
-------------------------------------------------------------------------------------------------------

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
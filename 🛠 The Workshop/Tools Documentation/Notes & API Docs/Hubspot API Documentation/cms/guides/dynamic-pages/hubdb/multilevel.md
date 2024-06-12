---
Please provide me with more context!  "Mission" can be used in many different ways. To help me write a mission statement for you, I need to know: "* **What is the mission for?** Is it for a company, a project, a personal goal, a team, a website, etc.? "
* **What are the key goals and values?** What do you want to achieve with this mission? 
* **What is the target audience?** Who are you trying to reach with this mission? 

Once I have this information, I can help you craft a compelling and effective mission statement.
---

How to build multilevel dynamic pages with HubDB


====================================================

Last updated: November 18, 2022

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Professional or Enterprise

A [dynamic website page](/docs/cms/data/dynamic-pages) is a CMS page whose content changes based on the path of the URL requested by an end user. [HubDB](/docs/cms/features/hubdb) already allows you to store, filter, and display data in your HubSpot website pages. Multilevel dynamic pages take this concept further, allowing you to create up to five levels of pages within one dynamic template.

Each dynamic page includes its own unique, SEO-friendly URL, and offers page-specific analytics.

**Please note:** that this tutorial assumes you already have multiple HubDB tables created. Please see the [HubDB documentation](https://developers.hubspot.com/docs/cms/features/hubdb) if you are unfamiliar with HubDB or want to create your first HubDB tables.

1\. Enable child tables in your table's settings.[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/multilevel#enable-child-tables-in-your-table-s-settings-)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   In your HubSpot account, navigate to **Marketing** \> **Files and Templates** > **HubDB**.
*   Click the **name** the table that will act as the parent for any other tables that will be used for your nested child tables.
*   In the top right, click the **Actions** dropdown menu, then select **Manage settings**.
*   If you haven't yet enabled the table for dynamic pages, click to toggle the **Enable creation of dynamic pages using row data** switch on, then select the columns to populate the page data.
*   Click to select the **Allow child tables** and **Automatically create listing pages for child tables** checkboxes.  
    ![hubdb-manage-settings-child-tables](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hubdb-manage-settings-child-tables.png?width=515&height=658&name=hubdb-manage-settings-child-tables.png)
*   Click **Save**.

With your changes saved, you'll then see a **Child table** column added to the table. In this column, use the **dropdown menu** to select another HubDB table to pull data from. 

To streamline this process, keep the child table columns and their internal names the same. If they are not the same, you'll need to use conditional logic later to render unique content for a given table.

2\. Select child tables for each row[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/multilevel#select-child-tables-for-each-row)
------------------------------------------------------------------------------------------------------------------------------------------------------

In the parent table, use the Child table column dropdown menus to select tables to pull data from.

You can only select tables that are enabled for dynamic page content creation. If you've enabled a table for dynamic page creation but aren't seeing it in the **Child table** dropdown menu, ensure that you've clicked **Publish** in the child table.

**Please note:** a parent table cannot reference a child table which also references the parent table. This will create a loop that results in an error when trying to select the child table within the parent table. 

![hubdb-menu-parent-table](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hubdb-menu-parent-table.png?width=822&height=328&name=hubdb-menu-parent-table.png)

In the above example, the first row will be pulling its food data from the _Foods_ child table, which contains data about available foods, as shown below.

![hubdb-food-child-table](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hubdb-food-child-table.png?width=816&height=394&name=hubdb-food-child-table.png)

When setting multilevel dynamic pages, the page paths for each row in the child table will be `parent_path/child_path`. For example, the page path for the `banana` row will be `page_path/foods/banana`.

By turning on the Automatically create listing pages for child tables setting, HubSpot will also automatically create intermediate listing pages for the child table rows (`page_path/foods` and `page_path/beverages`). 

If you would rather have those intermediate routes not resolve and return a 404 page, deselect the Automatically create listing pages child child tables checkbox in the table's settings.

3\. Create the multilevel template[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/multilevel#create-the-multilevel-template)
--------------------------------------------------------------------------------------------------------------------------------------------------

Through child tables, you can create up to five levels of pages with one dynamic template. You can configure each level by using the `dynamic_page_route_level` HubL variable. The top-level template starts at a value of `0` and increments for each table layer.

{% if dynamic\_page\_route\_level == 0 %} Top Level Template {% elif dynamic\_page\_route\_level == 1 %} Parent table template (/food /beverage) {% elif dynamic\_page\_route\_level == 2 %} Child table template (/food/banana etc., /beverage/soda etc.) {% endif %}

4\. Populate the top-level template[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/multilevel#populate-the-top-level-template)
----------------------------------------------------------------------------------------------------------------------------------------------------

For this tutorial, the goal is to list the child rows and group them by parent category. The example code below does the following:

*   First, it retrieves the category rows using `dynamic_page_hubdb_table_id`. 
*   Then, the `hs_child_table_id` property of each category row retrieves the table IDs of the child tables.
*   Last, it uses those table IDs to list the child rows under each parent category. 

{% if dynamic\_page\_route\_level == 0 %} <h1>Categories</h1> {% set rows = hubdb\_table\_rows(dynamic\_page\_hubdb\_table\_id) %} {% for row in rows %} <h2><a href="{{ request.path }}/{{ row.hs\_path }}">{{ row.hs\_name }}</a></h2> {% set childRows = hubdb\_table\_rows(row.hs\_child\_table\_id) %} {% for childRow in childRows %} <li><a href="{{ request.path }}/{{ row.hs\_path }}/{{childRow.hs\_path}}">{{ childRow.hs\_name }}</a></li> {% endfor %} {% endfor %} {% endif %}

5\. Populate the dynamic-level templates[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/multilevel#populate-the-dynamic-level-templates)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

After populating the top-level template, you'll then need to define templates for the subsequent levels in a similar fashion.

While building out your templates, it can be useful to access parent table data within child templates. For example, when our example page resolves to `foods/banana`, the `dynamic_page_hubdb_row` variable will be set to the `banana` row. However, you may want to access data from the `food` row. You can use `hs_parent_row` value on the `dynamic_page_hubdb_row` to retrieve the parent row:

{% if dynamic\_page\_route\_level == 1 %} <h1>Categories</h1> <h2>{{dynamic\_page\_hubdb\_row.hs\_name}}</h2> {% set rows = hubdb\_table\_rows(dynamic\_page\_hubdb\_row.hs\_child\_table\_id) %} {% for row in rows %} <li><a href="{{ request.path }}/{{ row.hs\_path }}">{{ row.hs\_name }}</a></li> {% endfor %} {% elif dynamic\_page\_route\_level == 2 %} <h1>Categories</h1> <h2>{{dynamic\_page\_hubdb\_row.hs\_parent\_row.hs\_name}}</h2> <h3>{{dynamic\_page\_hubdb\_row.hs\_name}}</h3> {% endif %}

Continue building out templates for each needed level. Then, you'll need to l ink the parent table to a page.

6\. Link parent table to page[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/multilevel#link-parent-table-to-page)
----------------------------------------------------------------------------------------------------------------------------------------

The final step is to create a page from the multilevel template and link the top-level parent table to the page. To do so, you'll [create a page](https://knowledge.hubspot.com/website-pages/create-and-customize-pages#create-pages), then access its settings. In the _Advanced Options_ settings of the page editor, click the Data source dropdown menu and select the Parent table.

![dynamic-pages-dropdown-menu](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/dynamic-pages-dropdown-menu.png?width=477&height=166&name=dynamic-pages-dropdown-menu.png)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/multilevel#page-feedback)
------------------------------------------------------------------------------------------------------------------

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
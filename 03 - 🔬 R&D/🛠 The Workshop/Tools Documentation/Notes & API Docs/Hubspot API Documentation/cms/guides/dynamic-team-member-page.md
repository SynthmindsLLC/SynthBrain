How To build a Dynamic Team Member Page with HubDB


======================================================

Last updated: July 30, 2021

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Professional or Enterprise

In this tutorial, I’ll show you how to create a Dynamic Team Member Page on HubSpot’s CMS, using HubDB. You can reference more detailed HubDB documentation [here.](https://designers.hubspot.com/docs/tools/hubdb)

 You’ll need:

*   **A HubSpot account with the CMS Add-on  
    **

*   Portals with _Website Starter_ or _without the Website Add-On_ do not support HubDB
*   You can check if your portal has the CMS Add-on by [signing in here](https://app.hubspot.com/l/account-dashboard/).

*   Approximately 3 hours
*   Some prior knowledge of HubSpot's CMS, HTML and CSS will be needed to customize your page

At the conclusion of this tutorial, we will have a working Dynamic Team Member Page based on the requesting page's URL, like this example here: [Dynamic Team Member Example](https://designers.hubspot.com/team-members)

1\. Build your HubDB Team Member Table[](https://developers.hubspot.com/docs/cms/guides/dynamic-team-member-page#build-your-hubdb-team-member-table)
----------------------------------------------------------------------------------------------------------------------------------------------------

This tutorial will focus on adding logic that allows your Team Member page to be dynamic, based on the requested CMS page's URL. If you are new to HubDB and need help generating an initial HubDB Team Member Table, take a look at this tutorial here: [Static Team Member Page](https://designers.hubspot.com/docs/tutorials/lets-build-a-team-page-with-hubdb)

If you are familiar with building HubDB tables you can import some testing data for walking through this example, here's a file you can use: [team-member.csv](https://cdn2.hubspot.net/hubfs/327485/HubDB/team-member-example.csv). Upload the file to HubDB, to follow along with this example. 

Once done, be sure to publish your table, making note of the ID of the table (the last number in the URL) and you will be ready to start using your data.

![hubdb-table-id](https://developers.hubspot.com/hubfs/hubdb-table-id.jpg "hubdb-table-id")

2\. Create a Custom Module[](https://developers.hubspot.com/docs/cms/guides/dynamic-team-member-page#create-a-custom-module)
----------------------------------------------------------------------------------------------------------------------------

Okay, so we have our HubDB Table generated which will showcase our amazing team members. 

First, we will need to create a new template in Design Manager (if you haven't already) and a new Custom Module. You can name it something like "Dynamic Team Member Module". We want to generate a Custom Module to allow for easier use across multiple templates or allow for potential custom fields to be created, depending on your needs. In this example, we are going to incorporate two custom fields which will allow each page to apply different styling to our rendered Table (more on that later). Be sure to add your new Custom Module to your desired template as well. 

Within your new Custom Module, add the following code. This code is generating the framework for which our logic will be applied to, that allows our Team Member section to be dynamic.

{# Get Team Members from HubDB #} {% set table = hubdb\_table\_rows(\[Insert YOUR Table ID\], queryparam)%} {% if table == \[\] %} <p class='align-center'>Sorry, no one found for that Search. Try changing your filter and search again.</p> {% else %} {% for row in table %} <div class="team-member-card-container {{ widget.cards\_in\_row }}"> <div class="team-member-card"> <div class="image-container"> <img src="{{ row.image.url }}" width="500" {% if row.image.width > row.image.height %}class="landscape"{% endif %} alt="{{ row.name }} Headshot"> </div> <div class="team-member-info"> <h3>{{ row.name }}</h3> <h4>{{ row.title }}</h4> <p>{{ row.description }}</p> </div> </div> </div> {% endfor %} {% endif %}

Click over to the preview of the template and you should see the simple Team Listing. If nothing appears, double-check that your table ID is correct, the table is published and that your variable names match what is set within your HubDB table.

Let's breakdown what we are doing here. Don't worry about the 'queryparam' just yet, this will be needed for later in the tutorial when we filter our Team Member Table based on the requesting page's URL path!

First, we add a little logic to render an error if for some reason our table returns an empty object. Next, we map out the rows for our Team Members. If done correctly, our preview should be rendering our entire Team. Feel free to modify the HTML structure as needed. 

It is worth noting that we are accessing the values of our HubDB rows via dot notation here. It is also perfectly acceptable to adjust this to use 'bracket' notation.

3\. Add Custom Field to the Custom Module[](https://developers.hubspot.com/docs/cms/guides/dynamic-team-member-page#add-custom-field-to-the-custom-module)
----------------------------------------------------------------------------------------------------------------------------------------------------------

This example is using a custom field within the module to further enhance the functionality of the rendered Team Member page. Our Custom Module will ultimately be applied to multiple pages so we want the ability to easily adjust the HTML structure of Table, if one of our Locations only has, say, 2 employees verse another that might have 6 employees. 

We can handle this by including CSS that controls the size of our team member containers based on a custom class that is applied to the HTML! We can accomplish this by adding a Choice field to our module. As seen below. 

![](https://developers.hubspot.com/hs-fs/hubfs/team-member-choice-card-size.jpg?width=602&height=993&name=team-member-choice-card-size.jpg)

In order for this field to have an impact, on the rendered layout of our widget, you will need to generate some CSS that can handle this. For simplicity, here is some CSS to get you going: [team-member-card.css](https://cdn2.hubspot.net/hubfs/327485/HubDB/team-member-card.css)

By default, our Module will set the 'half' class on our containers. Now, each card will render with 50% width. Now, if we generate a page, using this Module, and we know that we will have fewer team members rendered, we can dynamically adjust the CSS to make the Table display better!

Be sure to include this CSS within the custom module too. Our updated module will now look like this.

{# Load Card Stylesheet #} {{ require\_css(\[insert link to CSS\]) }} {# Get Team Members from HubDB #} {% set table = hubdb\_table\_rows(\[Insert YOUR Table ID\], queryparam)%} {% if table == \[\] %} <p class='align-center'>Sorry, no one found for that Search. Try changing your filter and search again.</p> {% else %} {% for row in table %} <div class="team-member-card-container {{ widget.cards\_in\_row }}"> <div class="team-member-card"> <div class="image-container"> <img src="{{ row.image.url }}" width="500" {% if row.image.width > row.image.height %}class="landscape"{% endif %} alt="{{ row.name }} Headshot"> </div> <div class="team-member-info"> <h3>{{ row.name }}</h3> <h4>{{ row.title }}</h4> <p>{{ row.description }}</p> </div> </div> </div> {% endfor %} {% endif %}

4\. Add Logic to Handle Dynamic Filtering by Page URL[](https://developers.hubspot.com/docs/cms/guides/dynamic-team-member-page#add-logic-to-handle-dynamic-filtering-by-page-url)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now that we have our Team Members rendering, we need to write some logic to handle rendering the Table, based on the requesting page's URL path. 

We can do this with a few [If Requests](https://designers.hubspot.com/docs/hubl/if-statements) that will pass a 'queryparameter' variable into our HubDB function to control which rows are returned onto the page. Insert the following code into your Custom Module, after our CSS include, but before the main HubDB table code. 

{# sets the different query parameters using request path for hubdb query #} {% set queryparam = "" %} {% if request.path == "/team-members/location/ma" %} {% set queryparam = queryparam ~ "&location=1" %} {% endif %} {% if request.path == "/team-members/location/nh" %} {% set queryparam = queryparam ~ "&location=2" %} {% endif %} {% if request.path == "/team-members/location/pa" %} {% set queryparam = queryparam ~ "&location=3" %} {% endif %}

Remember the `queryparam` variable from the beginning of this tutorial? This code puts it to use! Using the request object on the CMS page, specifically the **path**, we can control which team members are returned. Depending on the **path** of the page we set `queryparam` equal to a specific **value** from our HubDB table's location field. When this value is appended as our Table's filter option, our Team Member page will be dynamically updated to reflect only those members! 

5\. Generate your Team Member Pages[](https://developers.hubspot.com/docs/cms/guides/dynamic-team-member-page#generate-your-team-member-pages)
----------------------------------------------------------------------------------------------------------------------------------------------

Our Dynamic Team Member module is set and ready to go. All that is left to do is generate our pages. This example uses 4 pages. One that is the main Team Member 'Parent' page and three child pages. Feel free to utilize the example paths (slug) when generating your pages. Otherwise, you will need to remember to update the Custom Module to use the path's you are expecting your visitors to land on. 

This tutorial uses fairly simple logic so please feel free to modify or adapt anything you see here that is specific for your needs. 

Here is an example Dynamic Team Member Directory that we generated based on this tutorial: [Team Members Example](https://designers.hubspot.com/team-members)

More HubDB focused tutorials[](https://developers.hubspot.com/docs/cms/guides/dynamic-team-member-page#more-hubdb-focused-tutorials)
------------------------------------------------------------------------------------------------------------------------------------

*   [How to join multiple HubDB tables](https://designers.hubspot.com/tutorials/how-to-join-hubdb-tables)[](/how-to-add-videos-to-dynamic-pages-in-hubdb)
*   [How to add videos to dynamic pages](/docs/cms/guides/dynamic-pages/hubdb/video)
*   [How to build multilevel dynamic pages using HubDB](//designers.hubspot.com/how-to-build-multilevel-dynamic-templates)
*   [Let's build a page with a map using HubDB](https://designers.hubspot.com/docs/tutorials/lets-build-a-page-with-a-map-with-hubdb)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/dynamic-team-member-page#page-feedback)
------------------------------------------------------------------------------------------------------------

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
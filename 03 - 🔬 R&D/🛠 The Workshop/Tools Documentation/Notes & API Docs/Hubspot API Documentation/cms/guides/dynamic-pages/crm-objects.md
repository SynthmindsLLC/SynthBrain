Build dynamic pages using CRM objects


=========================================

Last updated: December 20, 2023

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Professional or Enterprise

You can build CRM object dynamic pages using [standard HubSpot objects](https://developers.hubspot.com/docs/api/crm/understanding-the-crm), such as _Products_, or [custom objects](https://developers.hubspot.com/docs/api/crm/crm-custom-objects) (_Enterprise_ only). Dynamic pages consist of a listing page view and a unique details page for each record. The listing page displays a list of all records in the object, and the details pages display information about each record based on the record's property values. 

You can also [build dynamic pages using HubDB](/docs/cms/guides/dynamic-pages/hubdb). Learn more about the different types of [dynamic pages](/docs/cms/data/dynamic-pages-overview).

You can learn more about building data-based CMS pages in HubSpot Academy's [CMS Data-Driven Content course](https://app.hubspot.com/academy/tracks/1148948/intro).

Building a CRM object dynamic page requires four steps:

1.  Prepare your CRM object with data you want to display.
2.  Create a custom module to display the data.
3.  Create a listing module to display all records on a listing page.
4.  Add the modules to a drag and drop page and select the object as the data source.

This tutorial will walk through how to build a CRM object dynamic page using the example of a _Car_ custom object, which stores data on individual cars at a dealership. 

Prerequisites[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/crm-objects#prerequisites)
-------------------------------------------------------------------------------------------------------

The following are required for building dynamic pages using CRM objects:

*   For custom object dynamic pages, you'll need a **_CMS_** **_Hub_** _Enterprise_ subscription, or a **_Marketing Hub_** _Enterprise_ account with **_CMS Hub_** _Professional_.
*   For standard CRM object dynamic pages, you'll need a **CMS Hub** _Professional_ or _Enterprise_ account.
*   An understanding of how to [create custom modules](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules). 
*   A standard or [custom object](https://developers.hubspot.com/docs/api/crm/crm-custom-objects) to use as a data source. You'll also need [user permission for the object](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#custom-object-access), such as _Companies_ or _Custom Objects_ access. 
*   Records created under the object you're using, such as individual products or custom object records. Records can be [created in HubSpot’s UI](https://knowledge.hubspot.com/crm-setup/use-custom-objects#desktop) or via [API endpoints](https://developers.hubspot.com/docs/api/crm/understanding-the-crm).

Prepare your CRM object[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/crm-objects#prepare-your-crm-object)
---------------------------------------------------------------------------------------------------------------------------

Each dynamic page will pull its metadata from the properties of the individual records of your selected CRM object. The values contained in these properties should uniquely identify the content of the page to stand out in search results. Metadata includes:

*   Page slug
*   Page title
*   Meta description
*   Featured image

For the page title, meta description, and featured image, you can use any of the object's existing single-line text properties. However, the dynamic page slug must be a property configured with `"hasUniqueValue": true`. Existing properties cannot be updated with this configuration, so you will need to create a new property for this field. For custom objects, create a new property by [updating the object schema](/docs/api/crm/crm-custom-objects). For standard objects, create a new property by [using the properties API](/docs/api/crm/properties). 

Dynamic page properties
| Dynamic page property | Property type | Description |
| --- | --- | --- |
| 
`Dynamic page slug`

Required



 | text | 

The slug that will be appended to the CMS page URL for each details page. The property needs to be configured with `"hasUniqueValue": true`.

The property value needs to be [URL friendly](https://developers.google.com/maps/documentation/urls/url-encoding), and must contain:

*   All lowercase characters.
*   No spaces or special characters, except `-`.
*   No leading slash. For example:
    *   **Incorrect:** `/property-value`
    *   **Correct:** `property-value`

 |
| 

`Page Title`

 | text | 

The page's title.

 |
| 

`Meta description`

 | text | 

The page's meta description.

 |
| 

`Featured image`

 | text | 

The page's featured image, which will appear when the page is shared.

 |

In our example, we’ll be using a custom property _VIN_ (Vehicle Identification Number) as a page slug, since we know each car’s _VIN_ is unique.

**Please note:** [content search](/docs/cms/features/content-search) will index up to 10,000 CRM records per set of dynamic pages. For example, if you build a set of dynamic pages based on a CRM object that has 15,000 records, only 10,000 of those pages will be indexed in the search feature. If you create another set of dynamic pages based on the same object, that set of pages will also be limited to 10,000 search-indexed pages.

Create a module to display details for a single record[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/crm-objects#create-a-module-to-display-details-for-a-single-record)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Individual detail pages will use this module to display the object record data. In our example, the module will display details for an individual car's page.

Within this module, you'll use the [`dynamic_page_crm_object`](/docs/cms/hubl/variables#crm-object-dynamic-pages) variable to access the data stored to the current dynamic page's object instance.

To set up the details module:

*   In the design manager, [create a new custom module](https://knowledge.hubspot.com/design-manager/create-and-edit-modules). 

Tip: naming the module something like _\[object type\] - detail_ can make it clear what this module does. For example, _Car - detail._

*   In the `module.html` field, add the following code:

{% if dynamic\_page\_crm\_object and !module.car %}{# detail page and content creator has not selected an object#} {% set car = dynamic\_page\_crm\_object %} {# easy variable to access the CRM objects properties from #} {# To see all of the properties your object during development, print it to the page with the |pprint filter #} <h1>{{car.year}} {{car.make}} {{model}} </h1> <div class="car"> <div class="carImage"> {% if car.image %} <img src="{{car.image}}" alt="{{car.year}} {{car.make}} {{car.model}}"> {% else %} <img src="https://f.hubspotusercontent20.net/hubfs/9307273/Imported%20images/plchldr255.png" alt="Picture coming soon"> {% endif %} </div> <div class="carDetails"> <div class="carPrice"> Price: {{ car.price|format\_currency("en-US") }} </div> <div class="carBody"> Body Type: {{ car.body\_style.name}} </div> <div class="carDescription"> {{ car.description }} </div> <div class="carDistance"> Distance from Cambridge: <span class="dealer\_location"> {{ car.location }}</span> Miles </div> <div class="carListingDate"> Time since listing: <span class="listing\_date">{{ car.date\_received }}</span> </div> </div> </div> {% else %}{# The page is not a dynamic page or the user selects a specific object, we can get the data from a CRM object field if there is data. #} {% set car = module.car.properties %} {# easy variable to access the CRM objects properties from #} {# To see all of the properties your object during development, print it to the page with the |pprint filter #} <section aria-label="featured car"> <div class="carImage"> {% if car.image %} <img src="{{car.image}}" alt="{{car.year}} {{car.make}} {{car.model}}"> {% else %} <img src="https://f.hubspotusercontent20.net/hubfs/9307273/Imported%20images/plchldr255.png" alt="Picture coming soon"> {% endif %} <h3 class="car-name">{{car.year}} {{car.make}} {{model}} </h3> <div class="price"> {{car.price|format\_currency("en-US")}} </div> </div> </section> {% endif %}

This code checks if the page is a CRM object dynamic page. If it is, use `dynamic_page_crm_object` to retrieve the object record data. Object record data will be retrieved based on the object type set in the page editor.

This makes the module useful outside of the context of a dynamic page as well, as you can use it to feature object records on dynamic pages by having multiple instances of the module.

In the above code, we’ve created a CRM object of _car_. To fit your use case, you can update the _module.car_ references in the code to your object's name.

After creating this module, you’ll then create the listing module to define the information that will appear on the general listing page.

Create a listing module[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/crm-objects#create-a-listing-module)
---------------------------------------------------------------------------------------------------------------------------

Depending on your use case, you may want the dynamic page's root URL to display a listing of your object's records. In our example, we would want the _https://website.com/cars_ page to display the listing of all of the available cars.

To do this, create a new custom module that will act as a listing of the object records. Within this module, use the [dynamic\_page\_crm\_object\_type\_fqn](https://developers.hubspot.com/docs/cms/hubl/variables#crm-object-dynamic-pages) variable to access the fully qualified name of the page's selected object.

Tip: naming the module something like _\[object type\] - listing_ can make it clear what this module does. For example, _Car - listing_.

You can use and modify the example code below to create a listing module:

{% if dynamic\_page\_crm\_object\_type\_fqn %}{# dynamic listing page #} {% set cars = crm\_objects(dynamic\_page\_crm\_object\_type\_fqn, "limit=200","vin, price, picture, location, body\_type, date\_received, image") %} {# To see all of the properties your object during development, print it to the page with the |pprint filter #} <div class="car\_\_listing"> {% for car in cars.results %} <div class="car\_\_card"> <a href="{{ request.path }}/{{ car.vin }}"> <div class="car\_\_image"> {% if car.image %} <img src="{{car.image}}" alt="{{car.year}} {{car.make}} {{car.model}}"> {% else %} <img src="https://f.hubspotusercontent20.net/hubfs/9307273/Imported%20images/plchldr255.png" alt="Picture coming soon"> {% endif %} </div> <div class="car\_\_details"> <div class="car\_\_price"> Price: {{car.price |format\_currency("en-US")}} </div> <div class="car\_\_body"> Body Type: {{ car.body\_type}} </div> <div class="car\_\_distance"> Distance from Cambridge: <span class="car\_\_dealer-location"> {{car.location}}</span> </div> <div class="car\_\_listing-date"> Time since listing: <span class="car\_\_listing-date"> {{car.date\_received }} </span> </div> </div> </a> </div> {% endfor %} </div> {% elif dynamic\_page\_crm\_object %} <!-- Listing module is hidden when viewing a dynamic pages detail page. --> {% else %}{# display simple listing for use on other pages #} {% set cars = crm\_objects("p9307273\_car", "limit=5","vin, price, location, body\_type, date\_received, image") %} {# To see all of the properties your object during development, print it to the page with the |pprint filter #} <section aria-labelledby="object-listing-heading"> <h3 id="object-listing-heading"> Available Cars </h3> <ul> {% for car in cars.results %} <li><a href="/cars/{{ car.vin }}">{{ car.body\_type }} ({{ car.price }}) in {{ car.location }}</a></li> {% endfor %} </ul> </section> {% endif %}

In this code we are checking if the current page is a CRM object dynamic listing page. If it is, the module will display a listing of items. If it’s a detail page, the module won’t display anything. If it's another CMS page, we show a simple listing of results.

Page setup[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/crm-objects#page-setup)
-------------------------------------------------------------------------------------------------

With the modules created, you can now add them to a page, then select the object as the data source.

1.  [Create a new page](https://knowledge.hubspot.com/cos-pages-editor/create-and-edit-pages-in-hubspot), selecting a page template that has a drag and drop area or flexible column. 
2.  In the page editor, click the **Settings** tab.
3.  Under _Page URL_, click the **pencil icon** to edit the page's URL. Set the URL to where you want your listing page to appear. In our car example our listing page will be at: `/cars`. 
4.  Click **Advanced options**, then scroll to the _Dynamic pages_ section.
5.  Under _Dynamic Pages_, click the **Data source** dropdown menu, then select your object. Then, click the **Dynamic page slug** dropdown menu and select the property to use as the page slug. Only single-line text properties set to  `"hasUniqueValue":true` will be available for selection. In our example, the page URL will use the _VIN_ property, which will generate detail pages with the URL slug of: `/cars/[VIN value]`  
      
    ![Screenshot of the page editor's page settings screen. It's cropped to only show the data source, and dynamic page slug fields for dynamic pages.](https://developers.hubspot.com/hs-fs/hubfs/Dynamic%20Pages.png?width=964&name=Dynamic%20Pages.png)
6.  Under _Metadata_, continue selecting the properties that will populate the page’s metadata. In our example, we’re setting the featured image to a property that contains an image URL for a picture of each car.
7.  After setting up your metadata, at the top of the page, click the **Content** tab to return to the editor.
8.  In the left sidebar, in the _Add_ tab, search for your detail and listing modules, then drag them into the page editor.
9.  To preview your page, click **Preview** in the upper right.
10.  When ready, publish your page by clicking **Publish** in the upper right.

You've now successfully created dynamic pages based on your data source. With our example page set up, when a user updates a car record in HubSpot, the listing and detail pages will update automatically to reflect the changes. Newly created records of that object type will also automatically create new pages using the dynamic page slug and be linked to from the listing page.

[Learn more about creating listings with the crm\_objects function](/docs/cms/features/custom-objects#displaying-the-properties-for-multiple-crm-objects-using-the-crm-objects-function).

More CRM object resources[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/crm-objects#more-crm-object-resources)
-------------------------------------------------------------------------------------------------------------------------------

*   [CRM objects in CMS Hub](https://developers.hubspot.com/docs/cms/features/custom-objects)
*   [Custom Object documentation](https://developers.hubspot.com/docs/api/crm/crm-custom-objects) 

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/crm-objects#page-feedback)
-------------------------------------------------------------------------------------------------------------

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
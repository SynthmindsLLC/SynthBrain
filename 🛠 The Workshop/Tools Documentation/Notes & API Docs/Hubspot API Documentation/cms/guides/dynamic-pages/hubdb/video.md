---
Please provide me with more context! I need to know what the mission is about. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a personal goal, a video game, a book, etc.? "
* **What is the overall objective?** What are you trying to achieve? 
* **What are the key elements?** What are the important components of the mission?

Once you provide me with more information, I can help you write a compelling and effective mission statement.
---

How to add videos to dynamic pages in HubDB


===============================================

Last updated: June 25, 2021

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Professional or Enterprise

A [dynamic website page](/docs/cms/data/dynamic-pages) is a CMS page whose content changes based on the path of the URL requested by an end user. [HubDB](/docs/cms/features/hubdb) already allows you to store, filter, and display data in your HubSpot website pages. Multilevel dynamic pages take this concept further, allowing you to create up to five levels of pages within one dynamic template.

Each dynamic page includes its own unique, SEO-friendly URL, and offers page-specific analytics. 

This tutorial assumes you already have multiple HubDB tables created. Please see the [HubDB documentation](/docs/cms/features/hubdb) if you are unfamiliar with HubDB or want to create your first HubDB tables.

1\. Add a 'VIDEO' column to your table.[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/video#add-a-video-column-to-your-table-)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Navigate to [HubDB](https://app.hubspot.com/l/hubdb) in your HubSpot portal, and edit the table you would like to be a parent of other tables. Click "Add new column" and create a column with type "Video".

![HubDB add column modal showing video column type selected](https://developers.hubspot.com/hs-fs/hubfs/hubdb-add-video.png?width=447&height=431&name=hubdb-add-video.png "HubDB add column modal showing video column type selected")

2\. Select videos for each row.[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/video#select-videos-for-each-row-)
---------------------------------------------------------------------------------------------------------------------------------------

You can now add a video to your row by clicking the "choose" button in the video column.

![insert video interface screenshot](https://developers.hubspot.com/hs-fs/hubfs/insert%20video%20interface.png?width=550&height=269&name=insert%20video%20interface.png "insert video interface screenshot")

Selecting a video will store the video `player_id` as the column value in the row. The file thumbnail is used to visually represent the video in the UI.

![HubDB UI with videos selected](https://developers.hubspot.com/hs-fs/hubfs/HubDB-with-videos-selected.png?width=550&height=213&name=HubDB-with-videos-selected.png "HubDB UI with videos selected")

3\. Add the video player widget to your dynamic template[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/video#add-the-video-player-widget-to-your-dynamic-template)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can now reference the row data in your dynamic template to build a `[video_player](/docs/cms/hubl/tags#video-player)` tag.

{% if dynamic\_page\_hubdb\_row %} {% video\_player "embed\_player" player\_id="{{dynamic\_page\_hubdb\_row.video}}" %} {% endif %}

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb/video#page-feedback)
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
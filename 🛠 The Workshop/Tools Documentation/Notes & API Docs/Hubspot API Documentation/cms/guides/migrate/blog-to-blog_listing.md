---
Please provide me with more information about the mission you'd like to create. I need some context to help you write a compelling mission statement. 

For example, tell me: "* **What is the purpose of this mission?** What are you trying to achieve?"
* **Who is the target audience?** Who will be impacted by this mission?
* **What are the key values and principles?** What are the guiding forces behind this mission?

Once you provide me with these details, I can help you craft a clear, concise, and inspiring mission statement.
---

How to migrate from a blog template to a blog\_listing template


===================================================================

Last updated: July 12, 2021

While `blog` templates do support the same functionality as a `blog_listing` template, they can provide a more confusing experience for both developers and content creators. Using explicit `blog_listing` and `blog_post` templates causes them to be listed appropriately in the blog settings, and makes the markup easier to maintain as a developer.

How to migrate[](https://developers.hubspot.com/docs/cms/guides/migrate/blog-to-blog_listing#how-to-migrate)
------------------------------------------------------------------------------------------------------------

Migration to the new template type is easy. First determine if your existing `blog` template is currently being used for both the listing and post detail template, or just the listing template.

If you have a `blog` template that is intended solely for creating a listing view.

1.  change the `templateType` to `blog_listing`.
2.  Verify under blog settings that the correct blog template is selected.

If your `blog` template is a shared template for both your blog listing and blog post views.

1.  clone your template.
2.  Change the `templateType` to `blog_listing`.
3.  Set your template's `label` to something easy to differentiate from the old version.
4.  Change the selected template under settings for your listing view to be your newly created template.

You could do the same for the `blog_post` template. But changing `templateType` to `blog_post`.

To make your code simpler and easier to read you can remove the `if is_listing_view` statement and leave only your listing code in your listing template, and only your post code in your post template.

Related Articles[](https://developers.hubspot.com/docs/cms/guides/migrate/blog-to-blog_listing#related-articles)
----------------------------------------------------------------------------------------------------------------

*   [Blog variables](https://developers.hubspot.com/docs/cms/hubl/variables#blog-variables)
*   [Blog templates](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog-template-markup)
*   [Blog Listing Templates](/docs/cms/building-blocks/templates/blog/listing)
*   [HubSpot Theme Boilerplate](https://developers.hubspot.com/docs/cms/building-blocks/themes/hubspot-cms-boilerplate)
*   [How to create a blog](https://knowledge.hubspot.com/blog/create-a-new-blog)
*   [Import your blog into HubSpot](https://knowledge.hubspot.com/blog/import-a-blog-into-hubspot)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/migrate/blog-to-blog_listing#page-feedback)
----------------------------------------------------------------------------------------------------------------

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
---
Please provide me with the context or details about the mission you are referring to. I need more information to help you with this. For example: "* **What is the mission about?** (e.g., a business mission statement, a personal goal, a scientific expedition, a game objective)"
* **What is the purpose of the mission?** (e.g., to achieve a specific goal, to explore new frontiers, to solve a problem)
* **What are the key objectives of the mission?** (e.g., to increase profits, to discover new planets, to improve healthcare)

Once you provide me with more context, I can help you create a compelling and impactful mission statement.
---

Memberships


===============

Last updated: March 29, 2024

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Enterprise

Memberships is a feature that makes it possible to require visitors to have an account in order to access content. The account system leverages the HubSpot CRM and CRM Lists together with the ability for a visitor to create a password for their account. Marketers can easily [create pages on their sites that only contacts on specific lists in the CRM can access](https://knowledge.hubspot.com/cms-pages-editor/control-audience-access-to-pages).  You can additionally restrict access to [knowledge base articles](https://knowledge.hubspot.com/cms-pages-editor/control-audience-access-to-pages#set-up-membership-registration-for-your-knowledge-base) and [blogs](https://knowledge.hubspot.com/cms-pages-editor/control-audience-access-to-pages#set-up-membership-registration-for-your-blog) using memberships.

Membership user flow[](https://developers.hubspot.com/docs/cms/data/memberships#membership-user-flow)
-----------------------------------------------------------------------------------------------------

When contacts are granted access to content, which can occur when they join lists or though manual assignment, they are sent an email to register for your website, where they set a password to access content they have permission to access. 

Imagine a gym, which wishes to allow visitors to register for classes and view the classes they have registered for. When a visitor registers for a class, the form submission creates a contact in the HubSpot CRM and that contact is added to a list based on the form submission, which is used to grant access to a "My Events" page. 

![An example gym registration.](https://developers.hubspot.com/hs-fs/hubfs/signup.gif?width=1259&name=signup.gif)

The visitor receives a membership registration email that allows them to create a password for their membership account. 

![Registration form](https://developers.hubspot.com/hs-fs/hubfs/register%20account.png?width=400&name=register%20account.png)

Now, when the visitors log in to their account, the user can log in to the private "My Events" page using the email and password they set. Because the visitor is logged in, the developer who created the private content can render data about the logged in contact using data from the CRM. 

![A visitor uses their account to log in and see classes they registered for.](https://developers.hubspot.com/hs-fs/hubfs/my_events.gif?width=1259&name=my_events.gif)  

Membership HubL variables[](https://developers.hubspot.com/docs/cms/data/memberships#membership-hubl-variables)
---------------------------------------------------------------------------------------------------------------

For some businesses, it may make sense to show different content based on if a user is signed in or not. There are HubL variables which developers can use to check to see if a contact is currently logged in on a website.

The HubL variable [`request_contact.is_logged_in`](/docs/cms/hubl/variables#website-pages-variables) indicates if the current visitor is signed in to the website through memberships. It can be used within an `if` statement to conditionally render certain content, allowing you to individually cater your visitor's experience.

{% if request\_contact.is\_logged\_in %} You're signed in! {% else %} <a href="/\_hcms/mem/login">Log In</a> {% endif %}

If you want to display different content on the same page based on list membership, you can check the signed-in contacts list memberships using [`request_contact.list_memberships`](/docs/cms/hubl/variables#website-pages-variables) HubL variable, which returns a dict of list IDs the logged in contact is a member of.

To personalize content without using memberships, you can use the [contact variable](/docs/cms/hubl/variables#general-variables) if a visitor has submitted a form on your website.

CRM object HubL functions[](https://developers.hubspot.com/docs/cms/data/memberships#crm-object-hubl-functions)
---------------------------------------------------------------------------------------------------------------

In addition to general content displayed conditionally on a page, it’s possible to pull information about objects within your HubSpot account such as contacts, companies, deals, and products using the functions:

*   [CRM Associations](/docs/cms/hubl/functions#crm-associations)
*   [CRM Object](/docs/cms/hubl/functions#crm-object)
*   [CRM Objects](/docs/cms/hubl/functions#crm-objects) 

For security purposes, only product and marketing event objects can be retrieved on a publicly accessible page; to pull information about other object types, a page must be behind membership. 

{% if request\_contact.is\_logged\_in %} {% set membership\_contact = crm\_object('contact', request.contact.contact\_vid, 'firstname,lastname') %} Welcome back, {{ membership\_contact.firstname }} {{ membership\_contact.lastname }} {% else %} <a href="/\_hcms/mem/login">Log In</a> {% endif %}

Private blog posts with self-registration[](https://developers.hubspot.com/docs/cms/data/memberships#private-blog-posts-with-self-registration)
-----------------------------------------------------------------------------------------------------------------------------------------------

When you [enable self-registration for private blog content](https://knowledge.hubspot.com/blog/use-self-registration-for-private-blog-content), you can limit access to specific blog posts so that visitors must register to view them. On the blog listing page, posts enabled for self-registration will display with a lock icon when using the default blog listing module.

![locked-post-listing-page](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/locked-post-listing-page.png?width=336&height=331&name=locked-post-listing-page.png)In the blog post, the content above the Read More separator will display, then prompt the user to log in to keep reading. Visitors can then sign up to read the rest of the blog post.

![blog-post-locked](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/blog-post-locked.png?width=799&height=420&name=blog-post-locked.png)

### Customization with HubL[](https://developers.hubspot.com/docs/cms/data/memberships#customization-with-hubl)

If you're using HubSpot's default blog listing module, the lock icon styling is handled for you. However, if you want to build your own solution with HubL, you can use the [flag\_content\_for\_access\_check](/docs/cms/hubl/functions#flag-content-for-access-check) function to check whether or not a blog post is visible to the currently logged in visitor. If the user is not currently logged in, the function will check whether the blog post is private.

When called, the function is replaced with the following attribute, which shows whether the visitor has access to the content:

`hs-member-content-access=<true/false>`

When `true`, the content is private and cannot be viewed by a viewer who is not logged in. 

For example, you could update your blog listing template with the following. Note that the `lock-icon` class can be any value, as long as you use the same value in your CSS to style the locked post indicator.

{% for content in contents %} <article {{ flag\_content\_for\_access\_check(content.id) }}> <div class="image-container">...</div> <div class="content-container"> <h3>Lorem Heading<img class="lock-icon" src="path/to/lock-icon.png"></h3> ... </div> </article> {% endfor %}

This would result in the following HTML output after the script runs to and finds that a blog post is private:

<!-- HTML output after script runs --> <article hs-member-content-access="true"> <div class="image-container">...</div> <div class="content-container"> <h3>Lorem Heading<img class="lock-icon" src="path/to/lock-icon.png"></h3> ... </div> </article>

You could then handle the locked/unlocked styling through CSS using the `hs-member-content-access` attribute. Note that the `lock-icon` class is just an example; you can use any value, as long as it matches the HTML class shown in the first code example above.

article\[hs-member-content-access\] .lock-icon { display: none; } article\[hs-member-content-access="true"\] .lock-icon { display: inline-block; }

### Customization with JavaScript[](https://developers.hubspot.com/docs/cms/data/memberships#customization-with-javascript)

Behind the scenes, the `flag_content_for_access_check()` function is calling an API to check whether the current visitor has access to the content based on the visitor cookies that are passed along with the request. If you'd like to create your own JavaScript solution, you can call this API directly. 

To check whether or not a post is locked to the current visitor, you can make a `POST` request to `https://your-domain.com/_hcms/content-access/get-gated-content-ids-for-member`. The request body should include an object with a `contentIds` array containing the IDs of the blog posts that you want to check member access for.

For example, if you wanted to check whether blog posts with the IDs of `10`, `11`, and `12` are locked to the visitor, your request body would be:

// Example request body { "contentIds": \[ 10, 11, 12 \] }

The response will contain the IDs of the blog posts that are locked to the user that is currently viewing the page:

// Example response { "gatedContentIds": \[ 10 \] }

See below for a full example of a custom JavaScript implementation.

// Custom JS example const hsFlaggedContentIds = <Array of content ID's> // an array of target id's to test against const gatedAttributeName = 'hs-member-content-access'; const customEventName = "hsAccessCheckFinished" async function getGatedContentIds(idsToCheck) { const options = { method: 'POST', body: JSON.stringify({ contentIds: idsToCheck }), headers: { 'Content-Type': 'application/json', }, }; const fetchGatedIds = await fetch( '/\_hcms/content-access/get-gated-content-ids-for-member', options ); const response = await fetchGatedIds.json(); return response\['gatedContentIds'\]; } function setGatedElementAttribute(element, gatedContentIds) { const contentId = parseInt(element.getAttribute(gatedAttributeName)); if (contentId && gatedContentIds.includes(contentId)) { // content is gated element.setAttribute(gatedAttributeName, true); } else { // content is not gated element.setAttribute(gatedAttributeName, false); } return element } getGatedContentIds(hsFlaggedContentIds).then((gatedContentIds) => { const flaggedElementsToCheckIfGated = document.querySelectorAll( '\[' + gatedAttributeName + '\]' ); // split the original array into 2 arrays and wrap in an object // that will be passed into the custom event. Event handlers will have // access to both gated and ungated arrays. return \[...flaggedElementsToCheckIfGated\].reduce((acc, item) => { let processedElement = setGatedElementAttribute(item, gatedContentIds); if (processedElement.getAttribute(gatedAttributeName) === "true" ) { acc.gatedContentElements.push(item); } else { acc.ungatedContentElements.push(item); } return acc }, { gatedContentElements: \[\], ungatedContentElements: \[\] }); }).then(processedGatedElements => { document.dispatchEvent( new CustomEvent( customEventName, { detail: { gatedContentElements: processedGatedElements } }) ); }).catch(err => { console.error(err) });

Register, login, and log out[](https://developers.hubspot.com/docs/cms/data/memberships#register-login-and-log-out)
-------------------------------------------------------------------------------------------------------------------

When a contact is granted access to any content on your website through memberships, they will receive an email to register for your website where they can set a password to access content they have permission to view. In the event you need to resend a contact a link to register, you can [resend their registration email](https://knowledge.hubspot.com/cms-pages-editor/control-audience-access-to-pages#resend-the-registration-email-to-a-specific-contact).

The URL paths for user sign-in/out are consistent for all HubSpot CMS sites with the membership functionality.  

*   `<your domain>/_hcms/mem/login`
*   `<your domain>/_hcms/mem/logout`

When a visitor logs in to their website, a cookie is sent to their browser, allowing them to browse through your website and access pages they have access to through memberships without having to log in again. If a visitor logs out, or has never logged in to your website in their browser, they will be prompted to log in before being able to view the content.

Membership templates[](https://developers.hubspot.com/docs/cms/data/memberships#membership-templates)
-----------------------------------------------------------------------------------------------------

Sites with memberships have a few special pages that are needed to facilitate the memberships functionality. These are dictated by special system templates. These system templates are editable, allowing you to control the look and feel of the various membership steps. To set which templates you are using, go to **Settings >** [**Private Content**](https://app.hubspot.com/l/settings/content-membership/all-domains/general) and choose the ["Templates" tab](https://app.hubspot.com/l/settings/content-membership/all-domains/templates). To create a template to set in these settings, go to **Marketing > Files and Templates > Design Tools**, then in the top left click **File > New File > HTML & HUBL** and select the appropriate Template Type from the dropdown. 

For a comprehensive list of the membership templates, refer to the [membership section of the templates documentation](/docs/cms/building-blocks/templates#membership). 

Only [HTML + HubL templates](/docs/cms/building-blocks/templates/html-hubl-templates) can be membership templates.

Membership audit logging[](https://developers.hubspot.com/docs/cms/data/memberships#membership-audit-logging)
-------------------------------------------------------------------------------------------------------------

In [Settings > Private Content](https://app.hubspot.com/l/settings/content-membership/all-domains/general), you can view an audit log of what visitors have been interacting with content behind memberships. This allows you to see which visitors are viewing private content.

![Audit log of private content viewership](https://developers.hubspot.com/hs-fs/hubfs/Screen%20Shot%202020-02-22%20at%2012.24.54%20PM.png?width=1290&name=Screen%20Shot%202020-02-22%20at%2012.24.54%20PM.png)

SSO for Memberships[](https://developers.hubspot.com/docs/cms/data/memberships#sso-for-memberships)
---------------------------------------------------------------------------------------------------

You can also manage all of your businesses access permission and authentication needs in a single system with [Single Sign-on (SSO) for Memberships.](/docs/cms/features/memberships/sso-for-memberships)

### Social logins[](https://developers.hubspot.com/docs/cms/data/memberships#social-logins)

You can provide users in your list a way to sign in using Google or Facebook instead of entering their email address and password. The social login provider sends the email address associated with the logged in social account. That email address is then used to validate if that contact is in a contact list with access to the content. This feature does not require you to have configured SSO settings. 

You need to have a page set to "Private registration required" with a contact list. Additionally your login template needs to have the `membership_social_logins` module.

[Add social login to your membership pages](/docs/cms/guides/membership/social)

Membership related articles and resources[](https://developers.hubspot.com/docs/cms/data/memberships#membership-related-articles-and-resources)
-----------------------------------------------------------------------------------------------------------------------------------------------

*   [HubSpot Essentials for Developers: Getting Started with Memberships](/blog/essentials-for-getting-started-with-memberships)
*   [Creating menus that adapt to whether the user is logged in or not](/blog/creating-a-header-nav-that-adapts-to-if-the-contact-is-logged-in) 

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/data/memberships#page-feedback)
---------------------------------------------------------------------------------------------

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
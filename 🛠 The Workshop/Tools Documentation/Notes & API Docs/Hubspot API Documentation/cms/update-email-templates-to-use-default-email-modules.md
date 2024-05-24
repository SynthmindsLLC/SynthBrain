Update email templates to use default email modules


=======================================================

When building email templates, HubSpot provides a set of [default email modules](/docs/cms/building-blocks/modules/default-email-modules) to get you started. These modules are similar to [default web modules](/docs/cms/building-blocks/modules/default-modules), but are split up to enable HubSpot to release updates to these modules for better email client support, while also releasing updates to the web versions of the modules separately. Existing email templates using the web modules will still function, but you'll need to update your email templates to use these new modules for forwards compatibility and to avoid errors in the design manager and CLI.

The following are the new email-specific modules that should replace existing usage of the web default modules:

*   [email\_cta](/docs/cms/building-blocks/modules/default-email-modules#email-call-to-action) (replaces `cta`)
*   [email\_header](/docs/cms/building-blocks/modules/default-email-modules#email-header) (replaces `header`)
*   [email\_linked\_image](/docs/cms/building-blocks/modules/default-email-modules#email-linked-image) (replaces `linked_image`)
*   [email\_logo](/docs/cms/building-blocks/modules/default-email-modules#email-logo) (replaces `logo`)
*   [email\_post\_filter](/docs/cms/building-blocks/modules/default-email-modules#email-blog-post-filter) (replaces `post_filter`)
*   [email\_post\_listing](/docs/cms/building-blocks/modules/default-email-modules#email-blog-post-listing) (replaces `post_listing`)
*   [email\_section\_header](/docs/cms/building-blocks/modules/default-email-modules#email-section-header) (replaces `section_header`)
*   [email\_social\_sharing](/docs/cms/building-blocks/modules/default-email-modules#email-social-sharing) (replaces `social_sharing`)
*   [email\_text](/docs/cms/building-blocks/modules/default-email-modules#email-one-line-of-text) (replaces `text`)

Below, read more about the new email modules and how to update your email templates to use them.

Updating to the new modules[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#updating-to-the-new-modules)
------------------------------------------------------------------------------------------------------------------------------------------------------

To update an email template to use the new default email modules, you'll need to update either the module path or ID. All email module paths are prepended by `email_`, and all email modules have been assigned a new ID. You can r[eview the section below](#new-default-email-modules) for a full list of new module paths and IDs.

Below is an example of updating an email template to use the new email logo module, either by referencing its new path or ID.

### Updating the module by path[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#updating-the-module-by-path)

Original

{% module "logo\_with\_path" path="@hubspot/logo" %}

Updated

{% module "logo\_with\_path" path="@hubspot/email\_logo" %}

### Updating the module by ID[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#updating-the-module-by-id)

Original

{% module "logo\_with\_id" module\_id="1155232" label="Logo" %}

Updated

{% module "logo\_with\_id" module\_id="122980089981" label="Logo" %}

New default email modules[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#new-default-email-modules)
--------------------------------------------------------------------------------------------------------------------------------------------------

The following modules have been added for email templates. When reference these modules in your email templates, you can use either the module path or ID.

*   [Email blog post filter](#email-blog-post-filter)
*   [Email blog post listing](#email-blog-post-listing)
*   [Email call-to-action](#email-call-to-action)
*   [Email header](#email-header)
*   [Email linked image](#email-linked-image)
*   [Email logo](#email-logo)
*   [Email one line of text](#email-one-line-of-text)
*   [Email section header](#email-section-header)
*   [Email social sharing](#email-social-sharing)

### Email blog post filter[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#email-blog-post-filter)

{% module "email\_post\_filter" path="@hubspot/email\_post\_filter" %}

**Path**

**ID**

*   **Old:** `@hubspot/post_filter`
*   **New:** `@hubspot/email_post_filter`

*   **Old:** `1366743`
*   **New:** `122980089983`

### Email blog post listing[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#email-blog-post-listing)

{% module "email\_post\_listing" path="@hubspot/email\_post\_listing" %}

**Path**

**ID**

*   **Old:** `@hubspot/post_listing`
*   **New:** `@hubspot/email_post_listing`

*   **Old:** `1367088`
*   **New:** `122980089986`

### Email call-to-action[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#email-call-to-action)

{% module "email\_cta" path="@hubspot/email\_cta" %}

**Path**

**ID**

*   **Old:** `@hubspot/cta`
*   **New:** `@hubspot/email_cta`

*   **Old:** `@hubspot/cta`
*   **New:** `@hubspot/email_cta`

### Email header[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#email-header)

{% module "email\_header" path="@hubspot/email\_header" %}

**Path**

**ID**

*   **Old:** `@hubspot/header`
*   **New:** `@hubspot/email_header`

*   **Old:** `1155826`
*   **New:** `122980089978`

### Email linked image[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#email-linked-image)

{% module "email\_linked\_image" path="@hubspot/email\_linked\_image" %}

**Path**

**ID**

*   **Old:** `@hubspot/linked_image`
*   **New:** `@hubspot/email_linked_image`

*   **Old:** `1155231`
*   **New:** `122960526478`

### Email logo[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#email-logo)

{% module "email\_logo" path="@hubspot/email\_logo" %}

**Path**

**ID**

*   **Old:** `@hubspot/logo`
*   **New:** `@hubspot/email_logo`

*   **Old:** `1155232`
*   **New:** `122980089981`

### Email one line of text[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#email-one-line-of-text)

{% module "email\_text" path="@hubspot/email\_text" %}

**Path**

**ID**

*   **Old:** `@hubspot/text`
*   **New:** `@hubspot/email_text`

*   **Old:** `1843376`
*   **New:** `122980089988`

### Email section header[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#email-section-header)

{% module "email\_section\_header" path="@hubspot/email\_section\_header" %}

**Path**

**ID**

*   **Old:** `@hubspot/section_header`
*   **New:** `@hubspot/email_section_header`

*   **Old:** `1155240`
*   **New:** `122980089987`

### Email social sharing[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#email-social-sharing)

{% module "email\_social\_sharing" path="@hubspot/email\_social\_sharing" %}

**Path**

**ID**

*   **Old:** `@hubspot/social_sharing`
*   **New:** `@hubspot/email_social_sharing`

*   **Old:** `1155241`
*   **New:** `122980537516`

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/update-email-templates-to-use-default-email-modules#page-feedback)
--------------------------------------------------------------------------------------------------------------------------------

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
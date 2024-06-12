---
Please provide me with the context or the topic of the mission so I can help you write a compelling mission statement. For example, tell me: "* **What is the mission for?** Is it for a company, a project, a personal goal, a non-profit organization, or something else?"
* **What is the purpose of the mission?** What do you want to achieve with this mission?
* **Who are you trying to reach with this mission?** Who is your target audience? 

Once you give me more information, I can help you craft a strong, clear, and inspiring mission statement.
---

Deprecated HubL filters and functions


=========================================

Last updated: September 21, 2023

The following is a list of HubL filters and functions that are deprecated. While these filters and functions still operate as intended, they've been replaced by newer ones that are more streamlined and optimized.

For all new and future projects we encourage using our [current HubL functions](/docs/cms/hubl/functions) instead of deprecated ones.

Deprecated filters[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#deprecated-filters)
----------------------------------------------------------------------------------------------------------

The following filters have been deprecated:

*   [datetimeformat](#datetimeformat)
*   [format\_currency](#format-currency)

### datetimeformat[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#datetimeformat)

This function has been replaced by [format\_datetime](/docs/cms/hubl/filters#format-datetime).

{{ content.updated|datetimeformat("%B %e, %Y") }} {{ content.publish\_date|datetimeformat("%B %e, %Y %l %p") }} {{ content.publish\_date|datetimeformat("%B %e, %Y %l %p", "America/Los\_Angeles") }} {{ content.publish\_date|datetimeformat("%B %e, %Y %l %p", "America/Los\_Angeles", "es-US") }}October 17, 2020 October 1, 2020 4 PM October 1, 2020 9 AM octubre 1, 2020 9 a.m.

### format\_currency[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#format-currency)

This function has been replaced by [format\_currency\_value](/docs/cms/hubl/filters#format-currency-value).

{% set price = 100 %} {{ price|format\_currency("en-US") }} {{ price|format\_currency("fr-FR") }} {{ price|format\_currency("jp-JP", "JPY", true) }}$100<br> 100 $<br> ￥ 100

Deprecated functions[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#deprecated-functions)
--------------------------------------------------------------------------------------------------------------

The following functions have been deprecated:

*   [blog\_post\_by\_id](#blog-post-by-id)
*   [blog\_topics](#blog-topics)
*   [blog\_recent\_topic\_posts](#blog-recent-topic-posts)
*   [datetimeformat](#datetimeformat-nbsp-)
*   [get\_public\_template\_url](#get-public-template-url)
*   [include\_css](#include-css)
*   [include\_javascript](#include-javascript)
*   [page\_by\_id](#page-by-id)

### blog\_post\_by\_id[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#blog-post-by-id)

This function has been replaced by [**content\_by\_id()**](/docs/cms/hubl/functions#content-by-id).

{% set my\_post = blog\_post\_by\_id(4715624297) %} <ul> <li> <a href="{{ my\_post.absolute\_url }}">{{my\_post.title}}</a> </li> </ul><ul> <li> <a href="//www.hubspot.com/blog/articles/kcs\_article/email/how-do-i-create-default-values-for-my-email-personalization-tokens">How do I create default values for my email or smart content personalization tokens?</a> </li> </ul>

### blog\_topics[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#blog-topics)

This function has been renamed to [**blog\_tags()**](/docs/cms/hubl/functions#blog-tags).

{{ blog\_topics("default", 250) }} {% set my\_tags = blog\_topics("default", 250) %} <ul> {% for item in my\_tags %} <li><a href="{{ blog\_tag\_url(group.id, item.slug) }}">{{ item }}</a></li> {% endfor %} </ul>\[Insider\] <ul> <li><a href="https://www.ajlaporte.dev/blog/tag/insider">Insider</a></li> </ul>

### blog\_recent\_topic\_posts[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#blog-recent-topic-posts)

This function has been renamed to [blog\_recent\_tag\_posts()](/docs/cms/hubl/functions#blog-recent-tag-posts).

{{ blog\_recent\_topic\_posts("default", "culture", 5) }}

### datetimeformat [](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#datetimeformat-nbsp-)

This function has been replaced by [format\_datetime()](https://developers.hubspot.com/docs/cms/hubl/functions#format-datetime).

{{ datetimeformat(content.publish\_date\_local\_time, "%B %e, %Y") }} February 27, 2020

### get\_public\_template\_url[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#get-public-template-url)

This function has been replaced by [**get\_asset\_url()**](/docs/cms/hubl/functions#get-asset-url).

{{ get\_public\_template\_url("custom/page/Designers\_2015/designer-doc-2105.js") }} //cdn2.hubspot.net/hub/327485/hub\_generated/style\_manager/1431479563436/custom/page/Designers\_2015/designer-doc-2105.min.html

### include\_css[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#include-css)

This function has been replaced by [**require\_css()**](/docs/cms/hubl/functions#require-css).

{{ include\_css("custom/page/Designers\_2015/designers-doc-2015.css") }} <link rel="stylesheet" href="//cdn2.hubspot.net/hub/327485/hub\_generated/style\_manager/1431477077901/custom/page/Designers\_2015/designers-doc-2015.min.css">

### include\_javascript[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#include-javascript)

This function has been replaced by [**require\_js()**](/docs/cms/hubl/functions#require-js).

{{ include\_javascript("custom/page/Designers\_2015/designer-doc-2105.js") }} <script type="text/javascript" src="//cdn2.hubspot.net/hub/327485/hub\_generated/style\_manager/1431479563436/custom/page/Designers\_2015/designer-doc-2105.min.js"></script>

### page\_by\_id[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#page-by-id)

This function has been replaced by [**content\_by\_id()**](/docs/cms/hubl/functions#content-by-id).

{% set my\_page = page\_by\_id(4715624297) %} <ul> <li> <a href="{{ my\_page.absolute\_url }}">{{ my\_page.title }}</a> </li> </ul><ul> <li> <a href="//www.hubspot.com/email/how-do-i-create-default-values-for-my-email-personalization-tokens">How do I create default values for my email or smart content personalization tokens?</a> </li> </ul>

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/functions/deprecated#page-feedback)
------------------------------------------------------------------------------------------------------

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
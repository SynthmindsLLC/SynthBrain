---
Please provide me with more context! To help you craft a compelling mission statement, I need to know: "* **What is the purpose of your mission?**  Are you describing a mission for a company, a project, a personal goal, or something else?"
* **What are your goals?** What do you want to achieve with this mission?
* **Who are you targeting?** Who will be affected by this mission?
* **What are your values?** What principles will guide your actions in fulfilling this mission?

Once I have this information, I can help you create a strong and impactful mission statement that captures the essence of your vision.
---

Optimizing your HubSpot CMS site for performance


====================================================

Last updated: March 16, 2024

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Professional or Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Starter, Professional, or Enterprise

Great user experience is a factor of content quality, speed, security and [accessibility.](/docs/cms/developer-reference/accessibility) Optimizing for these generally also improves Search Engine Optimization (SEO).

Better performance is all about providing a better experience for end users. Achieving better performance is all about solving for your individual site's bottlenecks.

Common website performance bottlenecks[](https://developers.hubspot.com/docs/cms/guides/speed#common-website-performance-bottlenecks)
-------------------------------------------------------------------------------------------------------------------------------------

Most web performance optimization techniques and best practices are not HubSpot-specific. Instead, they fall into a few categories:

*   **Loading performance:** the efficiency of transferring all of the files needed for your web page to the user's browser. The quantity of files, size of files, and the delivery speed of those files determines loading performance.
*   **Rendering performance:** the efficiency for the browser to take everything it downloaded, process it, and display the computed end result to the user. 

Rendering performance in particular is complex and is impacted by several factors, including:

*   The loading of Cascading Style Sheets (CSS)
*   The loading of JavaScript (JS)
*   The loading of media, such as images and videos
*   The device or web browser the visitor is using
*   The speed of response to user interactions

CSS is render-blocking, which means that poorly written CSS can cause Cumulative Layout Shift (CLS) during page rendering. Images can cause CLS, and take up RAM. Video players can cause CLS, some file formats require more processing work. JS can manipulate the [Document Object Model (DOM)](https://developer.mozilla.org/en-US/docs/Glossary/DOM) and [Cascading Style Sheet Object Model (CSSOM)](https://developer.mozilla.org/en-US/docs/Glossary/CSSOM)of a page, causing any of those issues. JS can also be resource intensive. All of these factors need to be balanced and best practices followed to ensure a fast experience for all visitors.

What HubSpot handles for you[](https://developers.hubspot.com/docs/cms/guides/speed#what-hubspot-handles-for-you)
-----------------------------------------------------------------------------------------------------------------

HubSpot's CMS automatically handles many common performance issues, including:

*   CDN with Image optimization and automatic WebP conversion
*   HTTP2
*   Javascript and CSS minification
*   Browser and server caching
*   [Prerendering](/docs/cms/developer-reference/cdn/prerendering)
*   [Domain Rewriting](/docs/cms/developer-reference/cdn)
*   [Brotli compression (with fallback to GZIP Compression)](/docs/cms/developer-reference/cdn#text-compression)
*   [HubSpot Blog posts support AMP](/docs/cms/developer-reference/cdn#accelerated-mobile-pages-amp-)

When including CSS in a custom module, HubSpot intelligently loads `module.css` only when a module is used on a page, and only loads it once regardless of how many instances of the module are on the page. By default, `module.css` does not load asynchronously, but you can change this by including [css\_render\_options](/docs/cms/building-blocks/modules/configuration) in the module’s `meta.json` file.

Improve your Website speed further[](https://developers.hubspot.com/docs/cms/guides/speed#improve-your-website-speed-further)
-----------------------------------------------------------------------------------------------------------------------------

Along with everything that HubSpot handles, there are some things you can do as a developer that have a big impact on your site's performance.

### Start with a good foundation[](https://developers.hubspot.com/docs/cms/guides/speed#start-with-a-good-foundation)

It's easier to build from a great foundation that was built with performance in mind, than trying to fix performance issues later. Building a fast car from the ground up is easier than buying a slow car and trying to make it fast.

The [HubSpot CMS Boilerplate](/docs/cms/building-blocks/themes/hubspot-cms-boilerplate) was built to be fast, and encourage best practices. See the [GitHub README](https://github.com/HubSpot/cms-theme-boilerplate) to review the current scores in Lighthouse and Website Grader.

By building from the boilerplate, you're already starting from a set of high scores. This means that you can focus your attention on the code you want to add on top of the boilerplate. 

[Build a site based on the boilerplate](https://developers.hubspot.com/cs/c/?cta_guid=13a1e730-f310-4137-997e-1822eec9a4e0&signature=AAH58kGmSYOtkzTVPJUMOUmj06g5rwoiAg&portal_id=53&pageId=65056559120&placement_guid=bdf71810-13e6-494f-8dbd-f733d5451ad5&click=226eb8cb-c159-46f7-b00c-bb38131f84d7&redirect_url=APefjpE89DUKpE_BO3R3aJEXsZMhU1vUGc4_CcmSwvKOogYTy0-raO9i8MVC-J1zWROL2y1EQxKJrH9RybL50x70okMJsbJeqEUcT1GaCDk-ijTCQJ1KXXsUhYqPyvhqdZddWA63IK6KNtrkc-tC4HkxOpQkn-Wl5O_knzx6vu8rV6kqxtXIrFg&hsutk=d3ee94511ad5cdbcd855d239974f0a81&canon=https%3A%2F%2Fdevelopers.hubspot.com%2Fdocs%2Fcms%2Fguides%2Fspeed&__hstc=20629287.d3ee94511ad5cdbcd855d239974f0a81.1715711069169.1715711069169.1715711069169.1&__hssc=20629287.1.1715711069169&__hsfp=1511885054&contentType=standard-page "Build a site based on the boilerplate") hbspt.cta.\_relativeUrls=true;hbspt.cta.load(53, 'bdf71810-13e6-494f-8dbd-f733d5451ad5', {"useNewLoader":"true","region":"na1"});

### Images[](https://developers.hubspot.com/docs/cms/guides/speed#images)

Images are prevalent on almost every page on the web. Images are usually the largest files on a page. The more images, and the larger the images, the longer your page will take to load. Animated images such as gifs and animated webp files also take up more space than non-animated images of the same size. Some image formats also are more performant than others, and better for certain scenarios.

#### What you can do[](https://developers.hubspot.com/docs/cms/guides/speed#what-you-can-do)

1.  The most important thing you can do is [optimize your images](https://blog.hubspot.com/marketing/compress-image) for the web. Image optimization is very much a shared responsibility among both content creators and developers. While HubSpot converts your images to webp and you can resize images using `[resize_image_url()](/docs/cms/hubl/functions#resize-image-url)`, uploading a non webp file that is already sized appropriately can help.
2.  Use fewer images per page.
3.  [Use the right image format for the use-case](https://blog.hubspot.com/insiders/different-types-of-image-files).
4.  Use Scalable Vector Graphics (SVGs) where possible. SVGs can scale in size infinitely without losing quality. Inlining your SVGs makes sense when you are making animations. In static graphics creating an SVG sprite sheet or simply treating it as a normal img element, or background image is typically better for performance.
5.  Intelligently [lazy load images](/docs/cms/guides/speed/lazy-loading).
6.  Make sure `img` elements contain height and width HTML attributes. This makes it so web browsers can intelligently optimize for [cumulative layout shift](https://web.dev/cls/) during render time and also makes it so HubSpot can generate a `srcset` for you.
7.  Use the [CSS aspect-ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio) property to reserve space when img dimensions may change.
8.  Use `[resize_image_url](/docs/cms/hubl/functions#resize-image-url)` to force images to be resized to a certain resolution.
9.  For background images, [use media queries](https://web.dev/optimize-css-background-images-with-media-queries/) in combination with `resize_image_url` to deliver images at sizes that make sense for the device.
10.  For large hero images - you can preload them by using `<link rel="preload" as="image" href="http://example.com/img_url.jpg">` within a [`require_head` tag](/docs/cms/hubl/tags#require-head). Use this technique sparingly, overusing it can actually hurt performance.
11.  If you fully control the HTML for an `img` and can predict it's sizes at different viewport sizes, providing a custom `srcset` and `sizes` attribute can help. You can use the`[resize_image_url](/docs/cms/hubl/functions#resize-image-url)` function to generate the alternate sizes. A custom tailored `srcset` and `sizes` based on the actual usage of the `img` element, will likely be more effective than the HubSpot generated one, but the automatically generated one is better than nothing.
12.  Add to your `img` element [`decoding="async"`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decoding). This tells the browser that it can start loading other content on the page at the same time as it's loading and processing the image.

### Autoplaying video[](https://developers.hubspot.com/docs/cms/guides/speed#autoplaying-video)

Video backgrounds and auto-playing videos can certainly set a website apart. Unfortunately they come at a cost. Video backgrounds are often used for website headers. When a video auto-plays, it means the browser needs to start loading the video right away. This can be especially problematic for users on slower connections or using cellphone data. 

#### What you can do[](https://developers.hubspot.com/docs/cms/guides/speed#what-you-can-do)

1.  Avoid using autoplaying video. If what you're showing is a background animation, consider using CSS animations or javascript animations. If you must display an autoplaying video:
2.  Choose a reasonable resolution for the video based on your use-case, and apply an effect over the video to make a lower resolution less noticeable.
3.  Make sure the video scales in quality based on the device and connection, the best way to do this is using a video sharing/hosting service like YouTube, Vidyard, or Vimeo.
4.  Disable autoplaying on mobile, show a fallback image instead.
5.  If the video is loaded by iframe, add `loading="lazy"`. This tells the browser it can wait to render and process the iframe until the user is close to displaying it on screen.

### JavaScript[](https://developers.hubspot.com/docs/cms/guides/speed#javascript)

JavaScript (JS) is useful for adding interactivity to your website. Loading a lot of JS code in general increases the file size of the JS files and the amount of time it takes for the browser to render interactive elements. Loading JS in the `<head>` can also be a problem as javaScript is [render blocking resource](https://web.dev/render-blocking-resources/) by default. Additionally JS is running on the visitors device, meaning it is limited to the resources that device has.

#### What you can do[](https://developers.hubspot.com/docs/cms/guides/speed#what-you-can-do)

1.  When HubSpot's CMS first came out jQuery was loaded in the `<head>` by default. You can remove it entirely in **Settings > Website > Pages,** or [upgrade to the latest version of jQuery](/cms/guides/jquery/upgrade). Take care when changing these settings on older websites if you did not build them, they may have been built reliant on jQuery or based on jQuery loading in the header.
2.  Ensure javascript is loaded just before the `</body>` to prevent render blocking. You can use `require_js` to load js for modules or templates only when needed and without accidentally loading the javascript multiple times for multiple instances of a module.
3.  Consider refactoring your JS to be more efficient. Use fewer JS plugins, use semantic HTML where it can help. For example for dropdowns, use `<details>` and `<summary>`. For modals use `<dialog>`.
4.  If you're using a giant JS library just for a few small features, consider using vanilla JS or loading a subset of the library if possible.
5.  Use [require\_js](/docs/cms/hubl/functions#require-js) to load JS only when necessary and only once per page. When using `require_js`, use `async` or `defer` attributes to improve page performance.
6.  To control where and when a module's JavaScript loads, use [js\_render\_options](https://developers.hubspot.com/docs/cms/building-blocks/modules/configuration) in the module's meta.json file.
7.  If loading external resources use [preconnect and DNS prefetch](https://web.dev/preconnect-and-dns-prefetch/) appropriately to deliver a faster experience.
8.  Limit the number of tracking scripts you use. Tracking scripts often try to understand all of the actions a user is taking on a page to provide you insights. That is a lot of code analyzing what the user is doing. Each tracking script amplifies this.
9.  When [handling interactions from a user, prioritize how you respond](https://web.dev/articles/optimize-inp#optimize_interactions) to focus on what's most important to be done right away, and defer through `setTimeOut` and/or `RequestAnimationFrame` any code that needs to happen in response to the user interaction, but can happen later or is not going to be visible to the user right away.

SEO recommendations tool[](https://developers.hubspot.com/docs/cms/guides/speed#seo-recommendations-tool)
---------------------------------------------------------------------------------------------------------

The HubSpot Recommendations tool is a great way to get performance and SEO feedback specific to your website.  

[Learn more about the recommendations tool](https://knowledge.hubspot.com/seo/view-seo-recommendations-in-hubspot)

Code Alerts[](https://developers.hubspot.com/docs/cms/guides/speed#code-alerts)
-------------------------------------------------------------------------------

Code Alerts is a CMS Hub Enterprise feature which acts as a centralized overview of issues that are identified inside of your HubSpot CMS website. Fixing issues that are identified in Code Alerts can help to optimize your website performance. Issues identified comprise several different areas from HubL limits to CSS issues.

[Learn more about Code Alerts.](/docs/cms/developer-reference/debugging-and-errors/code-alerts)

Additional resources for improving your site's speed[](https://developers.hubspot.com/docs/cms/guides/speed#additional-resources-for-improving-your-site-s-speed)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

There is a lot that can be done to optimize a site for speed and many of the topics warrant a further breakdown. We've compiled some great resources we encourage you to check out when working on optimizing your site.

*   [Site Speed and Performance: what you can do, and how HubSpot Helps](https://designers.hubspot.com/blog/site-speed-and-performance-what-we-do-and-what-you-can-do)
*   [How we improved page speed on HubSpot.com](https://developers.hubspot.com/blog/how-we-improved-page-speed-on-hubspot.com)
*   [15 tips to speed up your website](https://designers.hubspot.com/blog/15-tips-to-speed-up-your-website)
*   [5 easy ways to help reduce your website page's loading time](https://blog.hubspot.com/marketing/how-to-reduce-your-websites-page-speed)
*   [8 step guide to achieving 100% Google Page Speed](https://blog.hubspot.com/marketing/google-page-speed)
*   [Website Optimization - HubSpot Academy](https://academy.hubspot.com/courses/website-optimization)
*   [Web.dev](https://web.dev/learn/)
*   [How we optimize the HubSpot CMS - Jeff Boulter](https://www.youtube.com/watch?v=VpArzDy5ny4&t=14670s)
*   [The humble img element and Core Web Vitals - Smashing Magazine](https://www.smashingmagazine.com/2021/04/humble-img-element-core-web-vitals/)

### Image Optimization[](https://developers.hubspot.com/docs/cms/guides/speed#image-optimization)

Optimizing your images for the web prior to uploading and serving them helps ensure you won't serve an oversized image for the screen and use-case. 

**Popular image optimization tools:**

*   [ImageOptim](https://imageoptim.com/mac)
*   [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)
*   [Adobe Illustrator](https://www.adobe.com/products/illustrator.html)
*   [Optimizilla](https://imagecompressor.com/)

### Performance testing[](https://developers.hubspot.com/docs/cms/guides/speed#performance-testing)

Testing performance and optimizing for it should be apart of any website build out. There are many tools available for testing a website's speed, some of which grade and some of which only measure. It's important to understand these tools and how they work, so you can make educated decisions around performance improvements.

Popular performance tools include:

*   [Website Grader](https://website.grader.com/)
*   [GTMetrix](https://gtmetrix.com/)
*   [Google Page Speed Insights](https://developers.google.com/speed/pagespeed/insights/)and other [Google performance tools](https://developers.google.com/web/fundamentals/performance/speed-tools).
*   [Pingdom](https://www.pingdom.com/)
*   [WebPageTest](https://www.webpagetest.org/)

#### Measurement tools

Tools that measure will usually test the follow aspects of a page:

*   Loading time
*   Script execution time
*   Time until first contentful paint
*   Network times for assets downloading

These tools will generally provide results that state specific times for each of these metrics. If you retest, generally the measurements will shift slightly because not every page load is exactly the same.

#### Grading tools

In addition to measuring, grading tools will assign a grade to your page based on its testing, often in a letter or percent form. While these tools are intended to motivate making improvements, there are many different metrics and aspects to performance that need to be taken into account when reviewing results.

*   It's recommended to use multiple tools and strive for the best score you can in each. Understand, though, they will weight things differently. Efforts that may improve a score in one tool may not improve it in others.
*   It's not recommended to base your overall performance off of one metric's grade. Some metrics have different levels of affect on perceived performance, which results in some tools weighing these metrics differently to calculate their final grade.
*   There is no industry-wide standard for how to weigh metrics for grading. Over time, weights can and will change, as has occurred with [Google Page Speed](https://googlechrome.github.io/lighthouse/scorecalc/). There is also no industry-wide accepted for what is considered the minimum or maximum "good" value for individual metrics. Some tools base this off of a percentile of websites that have been tested., meaning that your scores are being compared to other sites.
*   Over time, a high grade for speed range has become more difficult to attain. Some tools instead look at user experience, visitor retention, and ROI-based research to determine what the threshold for a good score should be.
*   Not all tools take into account subsequent page load performance. For example, the HubSpot module system separates CSS and JS for individual modules, and only loads those assets when the module is actually placed on the page. This can result in several smaller CSS files, which could get flagged by Google Page Speed Insights. But by doing this, the next page load won't need to download any of the CSS or JS for any modules that repeat on the next page, as they're cached. This means that subsequent page loads would be kilobytes instead of a monolithic file.

**Related:**

*   [How Lighthouse performance scoring works](https://web.dev/performance-scoring/?utm_source=email&utm_medium=webdev_news)
*   [Website Optimization Roadmap (Core Web Vitals) | Mark Ryba](https://www.youtube.com/watch?v=js58KiXthJ4)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/speed#page-feedback)
-----------------------------------------------------------------------------------------

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
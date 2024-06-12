---
Please provide me with more context! I need to know what the mission is about in order to help you complete it. 

For example, tell me: "* **What is the purpose of the mission?** What are you trying to achieve?"
* **Who is involved?** Is it a personal mission, a team mission, or a mission for a larger organization?
* **What are the goals and objectives?** What specific things do you want to accomplish?
* **What is the time frame?** When do you hope to achieve the mission?

Once I have this information, I can help you with things like: "* **Developing a mission statement.**"
* **Creating a plan of action.**
* **Identifying resources and support.**
* **Measuring progress and success.** 

Let's get started!  Tell me more about your mission.
---

CDN, security, and performance overview


===========================================

Last updated: March 30, 2023

By default, HubSpot's CMS includes [security](https://legal.hubspot.com/security), [reliability](https://www.hubspot.com/reliability), and performance solutions so that you can focus on writing code and creating delightful user experiences. Below, learn more about HubSpot's content delivery network, security features, and performance enhacements.

In addition to the features listed in this article, you can also [further optimize performance on HubSpot CMS.](/docs/cms/guides/speed)

Content Delivery Network (CDN)[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#content-delivery-network-cdn-)
-------------------------------------------------------------------------------------------------------------------------------

HubSpot's CMS content is powered by a globally distributed Content Delivery Network that ensures faster page load times regardless of where your visitors are. No configuration, setup, or additional accounts are required to take advantage of the CDN for hosting media or pages, as HubSpot automatically handles distribution and cache validation. The CDN also features a web application firewall and built-in security to provide peace of mind against online attacks. 

HubSpot's [content prerendering service](/docs/cms/developer-reference/cdn/prerendering) also takes advantage of the CDN by storing local copies of prerendered pages across the globe. This enables users worldwide to load your pages faster based on their location. When a page or any dependency of a page, such as a template or module, changes, HubSpot automatically expire the server caches for that page.

Secure Socket Layer (SSL)[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#secure-socket-layer-ssl-)
---------------------------------------------------------------------------------------------------------------------

SSL is included and automatically provisioned for free on all [connected domains.](https://knowledge.hubspot.com/domains-and-urls/connect-a-domain-to-hubspot) Each domain is provisioned its own SAN certificate, with configurable options such as disabling support for select versions of TLS, redirecting requests made over HTTP to HTTPS, and serving the HSTS header so future requests are made over HTTPS. Per request, custom SSL certificates can be hosted with the [custom SSL add-on](https://legal.hubspot.com/hubspot-product-and-services-catalog).

HTTP/2[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#http-2)
--------------------------------------------------------------------------------

All SSL traffic on HubSpot hosted websites is served using [HTTP/2](https://http2.github.io/). HTTP/2 is a replacement for how HTTP is expressed “on the wire.” It is not a ground-up rewrite of the protocol; HTTP methods, status codes, and semantics are the same, and it's possible to use the same APIs as HTTP/1.x (possibly with some small additions) to represent the protocol.

The focus of the protocol is on performance; specifically, end-user perceived latency, network and server resource usage. One major goal is to allow the use of a single connection from browsers to a website.

IPv6[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#ipv6)
----------------------------------------------------------------------------

All HubSpot hosted websites include IPv6 addresses so they can be natively accessed over [IPv6](https://www.google.com/intl/en/ipv6/index.html). IPv6 is the most recent version of the Internet Protocol and expands the number of available addresses to a virtually limitless amount–340 trillion trillion trillion addresses. Because the internet is running out of IPv4 addresses, transition to IPv6 enables the internet to continue to grow and enables new, innovative services to be developed because more devices can connect to it.

JavaScript and CSS minification[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#javascript-and-css-minification)
----------------------------------------------------------------------------------------------------------------------------------

When writing JavaScript and CSS for HubSpot pages, you can expect the following minification behavior:

*   HubSpot automatically minifies JavaScript and CSS included in the design manager to remove unnecessary spaces, line breaks, and comments. This also applies to JavaScript and CSS [uploaded to the design manager through the CLI](/docs/cms/guides/getting-started-with-local-development). 

**Please note:** because HubSpot automatically minifies JavaScript and CSS in the design manager, you should not add minified code directly to the design manager.

To include minified code, you should instead upload the file to the [file manager](/docs/cms/features/file-manager), then attach the file through the design manager. To link a minified file to a module locally, you can [update the module's meta.json to include css\_assets or js\_assets](/docs/cms/building-blocks/modules/configuration#adding-css-and-javascript-dependencies).

*   HubSpot does not minify JavaScript or CSS files that are uploaded to the file manager or referenced via external links. You should ensure these files are minified before upload.
*   Every time you update a JavaScript or CSS file in the design manager or through local upload, HubSpot will automatically re-minify it. This can result in a short delay before you see the `.min.js` version of your file being served on live pages. During that period, HubSpot will serve the unminified version to ensure site visitors still get the latest version of your files. 
*   Syntax errors can prevent HubSpot from being able to minify a file.

In addition to minification, you can [use HubL includes to combine multiple CSS files into one file](/docs/cms/hubl#including-files-in-files) to further increase performance.

Domain rewriting[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#domain-rewriting)
----------------------------------------------------------------------------------------------------

Each additional domain used on your website incurs an additional DNS lookup and connection. The fewer domains you use, the faster your website will load. HTTP/2 supports loading multiple files simultaneously over the same connection, so the old guidelines for “sharding” your assets amongst multiple domains no longer apply.

The URLs of assets referenced in CMS pages such as developer file system files, CSS, JS, and images are automatically rewritten to match the domain of the current page when possible. So if you reference an image at [http://cdn2.hubspot.net/hubfs/53/HubSpot\_Logos/HSLogo\_gray.svg](https://cdn2.hubspot.net/hubfs/53/HubSpot_Logos/HSLogo_gray.svg) on a page served on [www.hubspot.com](https://www.hubspot.com/), the URL will automatically update to [https://www.hubspot.com/hubfs/HubSpot\_Logos/HSLogo\_gray.svg](https://www.hubspot.com/hubfs/HubSpot_Logos/HSLogo_gray.svg).

Text compression[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#text-compression)
----------------------------------------------------------------------------------------------------

Text-based files such as HTML, CSS, and JS are all compressed using [brotli](https://github.com/google/brotli) before they are served to browsers. Compression with brotli is even more significant than GZIP. If the client does not indicate that Brotli compression is supported, then gzip compression will be applied.

While minification speeds up the parse time of CSS and JS files in the browser, compression gets those files to the browser faster.

Image compression, optimization, and automatic resizing[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#image-compression-optimization-and-automatic-resizing)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you upload an image to the file manager, images are automatically optimized. Specifically, JPEGs and PNGs are stripped of their metadata (such as EXIF data). All images except for GIF files are recompressed to be visually lossless. Additionally, HubSpot may serve images in a different encoding if it can be represented as a smaller PNG than a JPEG.

Images are re-saved at the web-standard 72dpi regardless of their original resolution. For example, if you upload a file at 300dpi, originally created for print, it will be converted to 72dpi.

HubSpot automatically serves images in a WebP format for browsers that support it when the WebP format is a smaller file size than the original image. This conversion happens server-side and does not change the file extension in the URL. To ensure that links to the image work for all visitors regardless of WebP support,  image URLs maintain their original format, meaning an image uploaded as a `.jpg`, will still show as a `.jpg` in the URL but will be served as a WebP.

HubSpot-hosted images in CMS content are also automatically resized by appending height and/or width query parameters to the `src` URL for any images that have a height or width attribute. If a page is requested before an image is resized, the non-resized image will be served for that request. Browsers are given multiple options for the image resolution to load, ensuring that images look crisp on standard and high-resolution displays.

![Screenshot of img element with srcset automatically added with different resize URLs](https://developers.hubspot.com/hubfs/img_opt.png "Screenshot of img element with srcset automatically added with different resize URLs")

For individual jpg files if the image url has the `quality=high` query parameter, the image will not be compressed.

In addition, you can provide HubSpot with additional context to images to further control image resizing. This is done through the [resize\_image\_url()](/docs/cms/hubl/functions#resize-image-url) function, which prevents content creators from displaying oversized images on pages and emails. The function can also be useful when an image's size is not dictated by height and width attributes within the HTML, such as a background image.

Accelerated Mobile Pages (AMP)[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#accelerated-mobile-pages-amp-)
-------------------------------------------------------------------------------------------------------------------------------

AMP, or Accelerated Mobile Pages, is a mobile-specific page format that loads content nearly instantaneously, and can be enabled for HubSpot blog posts in your account settings. Learn more about [using Accelerated Mobile Pages (AMP) in HubSpot](https://knowledge.hubspot.com/cos-general/how-to-use-accelerated-mobile-pages-amp-in-hubspot).

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/developer-reference/cdn#page-feedback)
----------------------------------------------------------------------------------------------------

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
---
Please provide me with the context for the mission you want to create. To help me craft a compelling mission statement, tell me: "* **What is the overall goal or purpose of this mission?** (e.g., to explore a new planet, to solve a global problem, to create a better world)"
* **Who is involved in this mission?** (e.g., a team of astronauts, a group of activists, a company)
* **What are the specific objectives of the mission?** (e.g., to collect data, to raise awareness, to develop a new technology)
* **What are the values that guide this mission?** (e.g., innovation, collaboration, sustainability)

Once I have this information, I can write a strong and impactful mission statement for you.
---

How to use JavaScript frameworks and libraries on HubSpot


=============================================================

Last updated: November 29, 2023

Using the HubSpot CMS, you can create JavaScript-based web applications. 

What tier of HubSpot CMS is needed?[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#what-tier-of-hubspot-cms-is-needed-)
---------------------------------------------------------------------------------------------------------------------------------------

If your website requires server-side code or a content membership mechanism, you can take advantage of HubSpot's [serverless functions](https://developers.hubspot.com/docs/cms/features/serverless-functions) and the [content membership](/docs/cms/data/memberships) feature if you have an Enterprise subscription. However, you could alternatively build your own system using third-party providers such as AWS Lambda combined with an API gateway to run server-side code.

If you're building a web application that needs to hit API endpoints that require authentication such a [private app access token](/docs/api/private-apps), you shouldn't run that code in the browser. You would be exposing your credentials to anyone who views the page. The right approach is to create a layer of abstraction between the browser and the authenticated API: a custom API endpoint that does not require exposing your credentials and is served from the same domain as the website calling it.

Hitting the custom API endpoint will run server-side code that can make the authenticated request. Then you can do any formatting of the data or business logic you want to keep secret, and send the result to the browser. 

Commonly, serverless functions are used to do this because they have incredible scalability, and they don't require managing and maintaining your own server. You can use providers like AWS Lambda combined with an API gateway, or you can use HubSpot's first-party [serverless functions](https://developers.hubspot.com/docs/cms/features/serverless-functions). The advantage of HubSpot serverless functions is that you don't need to manage multiple separate services. The experience is simplified and directly integrated with the same developer file system which themes, templates and modules all exist in.

  
If you don't need to make authenticated API calls, then you don't need enterprise for your app. React and Vue are front end frameworks that don't need serverless functions to work, it is what you do with them that matters.

Frameworks and libraries[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#frameworks-and-libraries)
-----------------------------------------------------------------------------------------------------------------

For web applications, developers commonly use JavaScript frameworks that help manage state and User Interface (UI).

CMS Hub was not purpose-built to work with a specific framework in mind, but many common JavaScript frameworks work on HubSpot CMS. Building on HubSpot, you may need to think about how you work with those frameworks differently. But the core things needed to work with these frameworks are available:  the ability to write [custom templates](https://developers.hubspot.com/docs/cms/building-blocks/templates), [modules](https://developers.hubspot.com/docs/cms/building-blocks/modules), and JavaScript. We also enable you to do your [coding locally](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli), so that you can use a build step.

What you should know[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#what-you-should-know)
---------------------------------------------------------------------------------------------------------

We are collaborating with our developer community to establish the best practices for building with common JavaScript frameworks on HubSpot. While it is possible to do it, there are aspects of how the HubSpot CMS works that may require you to consciously set up your project differently than you might on a simple HTML page.

There may also be some parts of your development workflow that aren't what you're used to. We ask that you let us know your feedback so we can improve the experience for all developers. Currently the best place to do that is our [Developer forum](https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers). As we experiment and learn, we will continue to update our documentation accordingly.

### Things to consider when building[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#things-to-consider-when-building)

The HubSpot CMS has a powerful [module system](/docs/cms/building-blocks/modules), enabling you to create re-usable chunks of CSS, JavaScript and HTML with access to [HubL, the HubSpot templating language](/docs/cms/hubl). HubSpot modules provide a way for you to give a lot of control and power to content creators. Modern JavaScript frameworks often have their own module systems. These systems are all built independent from each other and as a result often have different solutions for issues you might encounter. 

#### Server-side rendering and client side rendering[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#server-side-rendering-and-client-side-rendering)

Server-side rendering is when the HTML for a page is generated from templating logic on the server before sending any HTML to a browser. 

Client-side rendering is when a lighter or "incomplete" version of the HTML is sent from the server, and JavaScript is used to generate the HTML. This transfers the processing of logic from the server to the web browser (the client).

Hydration is the act of combining both techniques. First, on the server, as much HTML as possible is generated. Then JavaScript evaluates the HTML provided and makes smaller changes to it as needed when the user interacts with the page or data is received. This reduces the load on the client and potentially reduces the time it takes for the user to see the loaded content.

On HubSpot CMS, HubL is processed server-side and then cached at the CDN level. You can then use JavaScript to hydrate or client-side render the HTML the browser serves to the site visitor.

#### Single Page App (SPA) analytics[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#single-page-app-spa-analytics)

Analytics is important for your company's ability to grow and adapt to solve for your customers and prospects. When building a single page app that contains multiple views, you may want to track the visitor seeing different views, as pages.  
  
Most analytics platforms provide a way to do this with JavaScript, HubSpot is no different. [Push the page-view](/docs/api/events/tracking-code#tracking-in-single-page-apps) when your app changes views.

#### Building your app utilizing HubSpot modules[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#building-your-app-utilizing-hubspot-modules)

HubSpot's module system is a server-side module system, generating an HTML document from HubL + HTML partials and generating minified CSS and JavaScript for each module within a page.

If you build using HubSpot modules, there are several benefits that come along with it: 

*   Content creators can add your module to pages that have drag and drop areas or flexible columns. They can also move and remove the module themselves.
*   You can provide fields to the content creator that let them configure settings for your app.
*   Your code is only rendered to the page only if the module is actually used.
*   `Module.css` and `module.js` is automatically minified. 

The cost of using the HubSpot module system is that it requires modules to be made up of specific files and in different places than you might normally place your code.

#### Building a full template instead[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#building-a-full-template-instead)

You could also build your application as a template rather than within the module framework. This gives you more flexibility with your file structure. But you do not get the benefits that modules provide; content creators will not be able to add this application to pages within drag and drop areas and flexible columns. 

#### Delimiters[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#delimiters)

Some JavaScript frameworks use curly braces `{ }` to delimit their code. The HubL language uses these braces, as well. There are three strategies you can use to ensure you don't have conflicts between your framework and HubL: You can use the raw HubL tag to wrap around your JSX, set the framework to use a different delimiter, or use a build step that compiles the JavaScript beforehand.

VueJS[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#vuejs)
---------------------------------------------------------------------------

The popular [Vue.js](https://vuejs.org/) framework can be used with and without a build step. See [Vue's own documentation](https://vuejs.org/v2/guide/installation.html) for a more detailed breakdown of the pros and cons of each method. On HubSpot there are specific pros and cons you should also be keeping in mind.

### Without a build step[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#without-a-build-step)

Integrating Vue.js without a build step into a module is easy. 

#### Add the vue library to your module[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#add-the-vue-library-to-your-module)

In your `module.html` file, use `[require_js](https://developers.hubspot.com/docs/cms/hubl/functions#require-js)` to add the [Vue library](https://vuejs.org/v2/guide/installation.html#Direct-lt-script-gt-Include) ensuring it will only load once when your module is added to a page.

While developing, use the dev build to get useful information for debugging. Once in production, it is recommended to use either the CDN URL for the specific Vue version, or download that file and host it as a JavaScript file in the HubSpot [developer file system](https://developers.hubspot.com/docs/cms/key-concepts#developer-file-system).

#### Add the HTML code[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#add-the-html-code)

Copy the HTML code from the [Vue.js introduction](https://vuejs.org/v2/guide/index.html#Declarative-Rendering), and paste it into your `module.html` file. Wrap this code in a HubL raw tag to prevent it from being evaluated as HubL.

{# raw prevents code within it from being evaluated as HubL #} {% raw %} <div id="app"> {{ message }} </div> {% endraw %}

#### Add your JavaScript code[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#add-your-javascript-code)

Copy the JavaScript from the [Vue.js introduction](https://vuejs.org/v2/guide/index.html#Declarative-Rendering), and paste it into your `module.js`. Wrap this code in an [event listener to ensure it's executed once the DOM content has finished loading](https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event). Publish your module, and preview it. **You should now see your basic Vue app working.**

var app = new Vue({ el: '#app', data: { message: 'Hello Vue!' } })

### With a build step[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#with-a-build-step)

We've built a [boilerplate](https://github.com/HubSpot/cms-vue-boilerplate) \[BETA\] to help you get up and running with the HubSpot module approach to building a VueJS application. The easiest way to take advantage of it is to run the `hs create vue-app` command from the [CMS CLI](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli). Directions can be found in the [repository](https://github.com/HubSpot/cms-vue-boilerplate/).

This boilerplate is new and we would love to hear your feedback! Let us know what could be improved and any issues you encounter. The best way to provide feedback is by [submitting issues to the GitHub repository](https://github.com/HubSpot/cms-vue-boilerplate/issues).

### Working with HubSpot forms and CTAs within Vue components[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#working-with-hubspot-forms-and-ctas-within-vue-components)

HubSpot CTAs and forms have their own script tags, and manage their own HTML themselves. To ensure your vue component doesn't modify the form or CTA, create an HTML element around the CTA/form embed code. [Apply `v-once` to that element.](https://vuejs.org/v2/api/#v-once) This ensures the code will be rendered once and then ignored by your Vue component.

ReactJS[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#reactjs)
-------------------------------------------------------------------------------

Rather than using HubL to build modules and partials, you can use [JavaScript and React](/docs/cms/building-blocks/modules/build-modules-and-partials-with-react). In addition to stitching server-rendered React components into the HTML generated by HubL, JavaScript modules and partials support both server-side and client-side interactivity. Learn more in HubSpot's [Introduction to JS Building Blocks](https://github.hubspot.com/cms-js-building-block-examples/).

You can also check out the [React boilerplate](https://github.com/HubSpot/cms-react-boilerplate) to get up and running quickly with a [React](https://reactjs.org/) app inside of a HubSpot module. The easiest way to take advantage of it is to run the `hs create react-app` command from the [CMS CLI](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli). From there follow the instructions in the [repository](https://github.com/HubSpot/cms-react-boilerplate).

This boilerplate is new and we would love to hear your feedback! Let us know what could be improved and any issues you run into. The best way to provide feedback is by [submitting issues to the GitHub repository](https://github.com/HubSpot/cms-react-boilerplate/issues).

Other JavaScript libraries[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#other-javascript-libraries)
---------------------------------------------------------------------------------------------------------------------

There are a lot of JavaScript libraries out there and it is impossible for us to document all of them individually. There are some core best practices to know and understand when using JavaScript libraries on HubSpot.

### Use require\_js instead of script tags[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#use-require-js-instead-of-script-tags)

You can have dozens of modules, and templates that use shared JavaScript libraries, and not worry about loading those libraries multiple times. To do this you need to use the `[require_js](/docs/cms/hubl/functions#require-js)` HubL function. Scripts loaded using this function will only load once per page regardless of how many modules, partials, and the template, requires them.

HubL

Copy all

    {{ require_js(get_asset_url('/js/jquery-latest.js')) }}
    
    {{ require_js("https://cdnjs.cloudflare.com/ajax/libs/d3/6.2.0/d3.min.js") }}

Use `get_asset_url()` to require files stored within the developer file system. The advantage aside from just co-locating your development files and consolidating security of these files, is that it will result in fewer DNS lookups.

Using require can be amazing for performance, because not only will you only load the file once. If assets on a page page don't need that library, it won't be loaded at all. You can even use requires with HubL logic to load resources only when you truly need it.

Recommended tutorials and guides[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#recommended-tutorials-and-guides)
---------------------------------------------------------------------------------------------------------------------------------

*   [Optimizing for performance](/docs/cms/guides/speed)
*   [Accessibility is not a feature](/docs/cms/developer-reference/accessibility)
*   [How to use web components on HubSpot](/blog/use-web-components-in-hubspot-cms-development)
*   [Getting started with modules](/docs/cms/guides/getting-started-with-modules)
*   [Getting started with serverless functions](/docs/cms/guides/getting-started-with-serverless-functions)
*   [Creating an efficient developer workflow](/docs/cms/guides/creating-an-efficient-development-workflow)
*   [Building dynamic pages with HubDB](/docs/cms/guides/building-dynamic-pages-with-hubdb)
*   [Build modules and partials with JavaScript](/docs/cms/building-blocks/modules/build-modules-and-partials-with-react)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/js-frameworks#page-feedback)
-------------------------------------------------------------------------------------------------

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
Accessibility


=================

Last updated: October 5, 2023

As websites continue to become more and more critical to businesses, ensuring that content on websites is accessible to all visitors has become more vital than ever. In the United States, this is often called [section 508](http://www.section508.gov/) compliance, which refers to the section of the Reauthorized Rehabilitation Act of 1998 that requires federal agencies to make electronic and information technology accessible to people with disabilities. While section 508 compliance is a good baseline, increasingly the [Web Content Accessibility Guidelines (WCAG)](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG) are being used as the standard for creating accessible content on the web.

Accessibility is not a feature[](https://developers.hubspot.com/docs/cms/guides/accessibility#accessibility-is-not-a-feature)
-----------------------------------------------------------------------------------------------------------------------------

The legal aspect shouldn't be your motivator for providing a good experience for your users. [One in four Americans have a disability according to the CDC](https://www.cdc.gov/ncbddd/disabilityandhealth/infographic-disability-impacts-all.html). Choosing not to provide a good experience for 25% of visitors is like a physical store denying every fourth visitor from entering. Not only will those customers be unhappy, they likely will not come back or recommend your services.

A common phrase among developers is that "accessibility is not a feature". The idea is don't treat accessibility like a bonus thing to add, or something to deal with at the end of a project.

Accessibility requires thought, empathy, and understanding. When approached early on in a project you can design and develop solutions instead of needing to re-architect something later.

**Often times solving for accessibility solves for your other priorities as a developer**, user experience, performance, and SEO are a few top concerns that are directly intertwined with accessibility. Improving one often improves the other.

Empathy is a huge part of accessibility that is easy to overlook. As developers we want to automate everything, if something is hard or time-consuming to do, we want tools to either do it for us or tell us the right way to do it. Unfortunately, these tools can only scratch the surface, because they are not human, they can't truly experience the page the way a human can. **It is technically possible to create a web page that passes most automated accessibility tests with flying colors but is completely unusable to all humans, sighted, blind, deaf, color blind, limited or unlimited motor function.** You can technically meet requirements, but provide an unusable frustrating experience that completely alienates people. The takeaway is this: don't rely on the tools, test your work, empathize with your users, collect feedback.

While not a definitive guide, here are some steps that you can take to make your content accessible, as well as resources for further diving in.

Provide text alternatives for any non-text content[](https://developers.hubspot.com/docs/cms/guides/accessibility#provide-text-alternatives-for-any-non-text-content)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

All images, icons, videos, and buttons that convey meaning or are interactive should have a text alternative. Not only is this good for visitors that are consuming your content via a screen reader, but it is also great for search engines. The alternative text should describe the content of the image. Most images on your site can likely be edited in the page editor, [setting alt text in the page editor is easy](https://knowledge.hubspot.com/cos-pages-editor/how-do-i-add-alt-text-to-my-image). Inside of custom modules and templates, however, you need to make sure that alt text specified in page editors is honored.

This means making sure if you have an `<img>` element that the alt text the user provides is actually used.

Good: <img src="{{ module.image.src }}" alt="{{ module.image.alt }}"> Bad: <img src="{{ module.image.src }}">

If for some reason you are not making an image editable in the page editor, you should hard-code the alt text.

There is one exception to this alt text rule. If your image provides no additional context and is purely just presentational it is better to have a ["null" alt text](https://www.w3.org/WAI/tutorials/images/tips/) value than to go without an alt attribute altogether.

Good if only presentational: <img src="{{ module.image.src }}" alt="">

For videos, use a service that supports captions and consider including a transcript. Some services that support uploading transcripts include [Vidyard](https://knowledge.vidyard.com/hc/en-us/articles/360009876234-Make-your-Vidyard-players-accessible), [YouTube](https://support.google.com/youtube/answer/2734799?hl=en), [Vimeo](https://help.vimeo.com/hc/en-us/articles/224968828-Captions-and-subtitles), and [Wistia](https://wistia.com/support/player/captions).

### Use a11y friendly lazy loading solutions[](https://developers.hubspot.com/docs/cms/guides/accessibility#use-a11y-friendly-lazy-loading-solutions)

Lazy image loading is a common performance enhancement technique for building websites. The method used to actually lazy load matters for accessibility.

JavaScript solutions for this typically rely on the `src` attribute of images to be something untrue (like a small `.gif` file) instead of the true source of the image, which is held in a `data-src` attribute until the user scrolls the image close to view. This means that initially the image is inaccessible to a screen reader user who is navigating the page, especially one using a rotor to look through the entire page's contents without even scrolling. Additionally, if JavaScript isn't loaded on a page, these lazy loading solutions will fail, and therefore, leave assistive technology users without the proper images on the page.

Using [native image lazy loading](https://web.dev/native-lazy-loading/) avoids this problem, keeping the image markup the same, regardless of whether JavaScript loads.

Good: <img src="{{ module.image.src }}" alt="{{ module.image.alt }}" loading="lazy" height="200px" width="400px"> Bad: <img src="1px.gif" data-src="{{ module.image.src }}" alt="{{ module.image.alt }}">

HubSpot supports [browser-based lazy loading](/docs/cms/guides/speed/lazy-loading) in custom modules. It is recommended you use it.

Make sure that all links and form inputs have descriptive text[](https://developers.hubspot.com/docs/cms/guides/accessibility#make-sure-that-all-links-and-form-inputs-have-descriptive-text)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Links, buttons, and form elements all need to have actual text that indicates what it does or where it goes. Otherwise screen readers will read out that the user has a link or button selected, but will have no idea what it does.

If using an icon, provide screen reader text. For example, some standard HubSpot templates use an icon shortcode:

<a href="https://www.facebook.com"><i class="fab fa-facebook-f"></i><span class="screen-reader-text">Facebook</span></a>

Don’t use `'display: none'` to hide form labels and other descriptive text. This prevents text from being read aloud for those with difficulty seeing, as well as hurts users who can see but have trouble seeing the text due to lack of contrast on the placeholder text. Not to mention, who hasn't started filling out a form or had a form get auto-filled for them, but had no idea if it was entered correctly because the form field labels were invisible.

If you absolutely have to have hidden text or hidden text could provide additional context that a sighted user wouldn't need. Use CSS that makes the text invisible without hiding it from screen readers or add the `'.screen-reader-text'` class.

.screen-reader-text { clip: rect(1px, 1px, 1px, 1px); height: 1px; overflow: hidden; position: absolute !important; width: 1px; }

Adding a skip to content link[](https://developers.hubspot.com/docs/cms/guides/accessibility#adding-a-skip-to-content-link)
---------------------------------------------------------------------------------------------------------------------------

When a visitor is navigating using a screen reader, or just simply using their keyboard, it is super helpful if there is a way to skip over the portions of the page that are repeated such as a header. We can do this by adding a link that points to the main content of the page.

In your header, add HTML with the following content:

<a href="#content" class="screen-reader-text">Five ways to make your site more accessible</a>

Then, in every template ensure that there is an element with an ID attribute of content. In our example, we used the article title as the text to jump to. This enables search engines to understand what is being linked to. It's a more semantic way of jumping to the content.

<main id="content"> <!-- your page or post's actual content --> </main>

Use semantic markup[](https://developers.hubspot.com/docs/cms/guides/accessibility#use-semantic-markup)
-------------------------------------------------------------------------------------------------------

Semantic markup is HTML that conveys meaning. Some examples of elements that are semantic are `<header>`, `<main>`, `<footer>`, `<nav>`, `<time>`, `<code>`, `<aside>`, and `<article>`.

Some examples of elements that are not semantic are `<div>` and `<span>`. Non semantic elements still have their place, but should be used primarily for presentation and not for conveying meaning.

Semantic elements can be understood by search engines and assistive technologies, both positively affecting SEO and improving your user experience.

Do not use `<div>` elements as interactive elements like buttons, tabs, or links unless you're sure you've provided a good experience via aria attributes.

Use links (`<a />`) and `<button />` appropriately.

Use links for linking to sections of a page and navigating to other pages.

Use Buttons for interactions that do not result in leaving the page or navigating to an ID.

When working with tables - if a table has a descriptive title include it in a `<caption>` element just after the `<table>` element.

Use `<th>` elements with the proper scope attribute in tables for column and row headings and `<thead>`, `<tbody>`, and `<tfoot>` to denote sections.

Use the scope attribute on `<th>` attributes to denote whether the heading is for the row or column.

Need an accordion? Don't forget about the `<details>` and `<summary>` elements they give you most of this functionality for free, and it's accessible. [Be sure to add a polyfill or fallback if you need to support old browsers](https://caniuse.com/#feat=details).

Keyboard navigation[](https://developers.hubspot.com/docs/cms/guides/accessibility#keyboard-navigation)
-------------------------------------------------------------------------------------------------------

Some users use their keyboard to navigate webpages and forms out of preference. Some visitors must use the keyboard or some sort of assistive device that emulates a keyboard to navigate websites.

*   Make sure that [':focus'](https://www.w3schools.com/cssref/sel_focus.asp) is styled so that when a user is navigating via the keyboard they can see what is focused. Only disable the CSS outline property if you are providing an acceptable alternate visual indicator. Use [:focus-within](https://css-tricks.com/almanac/selectors/f/focus-within/) if it can help direct users attention usefully.
*   When hiding/showing portions of the page with [':hover'](https://www.w3schools.com/cssref/sel_hover.asp) or via Javascript, make sure that users are also able to navigate those controls via Javascript or that there is alternative path to the information.
*   Make sure your site's main navigation supports keyboard navigation, a commonly missed issue is that drop-downs and fly-outs are not made accessible. This prevents users from getting to parts of websites that may be critical.
*   Provide and update `hidden`, `aria-expanded`, `aria-current`, `aria-selected`, and other state attributes as necessary to ensure screen readers properly communicate the state of  elements.

Fallback to roles if needed[](https://developers.hubspot.com/docs/cms/guides/accessibility#fallback-to-roles-if-needed)
-----------------------------------------------------------------------------------------------------------------------

When creating templates or coded files, you should use correct semantic elements (`<header>`, `<main>`, `<footer>`, `<nav>`, `<dialog>`, etc.) to communicate to web browsers and screen readers what type of content is inside your elements.

In the off-chance semantic elements are not appropriate for your scenario you should add [role attributes](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles). 

Adding landmarks make it easier for users that are using screen readers to jump between the major sections of a web page. HubSpot includes 'role' attributes to the menu, simple menu, and Google Search modules.

Additional design tips[](https://developers.hubspot.com/docs/cms/guides/accessibility#additional-design-tips)
-------------------------------------------------------------------------------------------------------------

1.  Make sure that when a user zooms their browser to 200% content remains visible and readable.
2.  It is not advised to make fonts much smaller than 16px as it may become hard for visitors to read.
3.  Avoid using color as the only way of communicating information. A surprising percentage of the world population is color blind.
4.  Make sure that there is sufficient contrast between the color of text and the background so that users with limited vision can read the content.
5.  Avoid animations that flash rapidly (more than three times per second) as it could trigger seizures in some visitors.
6.  Consider supporting [prefers-reduced-motion](https://css-tricks.com/introduction-reduced-motion-media-query/) if you have animations on your site.
7.  Today building a responsive website is considered a must. Make sure all interactive elements function as expected on mobile. Interactive elements must be easy to tap, and there should plenty of room between tap regions.

Content writing[](https://developers.hubspot.com/docs/cms/guides/accessibility#content-writing)
-----------------------------------------------------------------------------------------------

An easy thing to forget is that accessibility should also be considered in your text content.

1.  Avoid directional language "see sidebar on the left". If the user is on mobile, odds are this makes no sense to them as content usually stacks on mobile.
2.  Use headings like `<h1>` `<h2>` etc. and nest them consecutively. Do not skip a heading for visual effect.
3.  When adding a link, never have the link text be "Click here", it conveys no meaning to screen readers, doesn't make any sense on touch screens or other types of devices. Instead, your text should state what is at that link. This is also better for SEO, because search engines understand what is being linked to.
4.  Make sure if you use any special styles on the text to convey meaning, you are using the appropriate `<mark>` `<strong>` `<em>` `<sup>` etc. semantic tag, otherwise your meaning may be lost to some visitors.
5.  If you are targeting visitors worldwide, avoid jokes that are region specific. If you are having your site translated, avoid puns. As much as we love a good dad joke, they often don't translate well.
6.  Use tools to help improve your grammar and spelling. This helps comprehension and results in better translations.
7.  Write your content in a way that fits your site's audience. You wouldn't explain astrophysics to 5th grader, the same as you would an accomplished physicist. That said, avoid fancy words just for the sake of using them, [plain is better](https://www.nngroup.com/articles/plain-language-experts/).

HubSpot specific recommendations[](https://developers.hubspot.com/docs/cms/guides/accessibility#hubspot-specific-recommendations)
---------------------------------------------------------------------------------------------------------------------------------

Most of the work toward improving accessibility is not HubSpot specific. That said we want to set you up for success on HubSpot and there are some things you can do either as a developer or content creator to provide a better experience for users.

### Use custom modules and templates that follow a11y best practices[](https://developers.hubspot.com/docs/cms/guides/accessibility#use-custom-modules-and-templates-that-follow-a11y-best-practices)

Whether you are installing a module or template from the marketplace, developing them or having them built for you, one of the best things you can do is to make sure they follow a11y best practices. Custom Modules can have the greatest impact on the accessibility of your site because they are often used many times over, sometimes even on the same page. Similarly, a single template may be used hundreds or thousands of times on a single site. If your site is not accessible you are likely cutting your profits. Like with advertising it naturally makes sense to pay a little more to make sure your website reaches a wider audience. One of the benefits of modules is that you can often improve the code later as guidelines and best practices evolve, improving accessibility for every page that module lives on at once.

On the HubSpot marketplace look for modules and templates that talk about accessibility, and meeting WCAG requirements in their descriptions. If you're working with a developer tell them from the beginning that accessibility is important for you. Not all developers build with a11y in mind from the start. Telling them late in a project will likely cost you more than telling them from the get-go because instead of prioritizing it from the beginning, they now need to retroactively fix accessibility issues.

If you are a developer, build modules and templates that make meeting a11y guidelines easy for content creators. Use appropriate headings, semantic HTML, make interactive elements provide proper roles, and context. Content creators that are aware of accessibility issues are generally happy to pay a little more for modules and templates that are inclusive, that said you need to show that your modules take accessibility into account. Include skip links in templates, make global groups and global partials used in your templates a11y friendly, these get used throughout an entire website and can have the greatest impact on the usability of a site.

If you build for the HubSpot marketplace know that your content could get used across thousands, even millions of pages on the web. You make a choice that affects people when publishing your content and sharing your work, whether your work is inclusive or not.

Beware of one-stop solutions[](https://developers.hubspot.com/docs/cms/guides/accessibility#beware-of-one-stop-solutions)
-------------------------------------------------------------------------------------------------------------------------

There are dozens of tools that make claims like _"Just add our script to your website and your site will be accessible"_. 

Some of these tools will try to make sense of parts of the page and change html and attributes to try to fix some issues. That said they are guessing, and can be wrong or could break functionality on your site or make matters worse for users.

These tools may not always operate as expected, sometimes supplying their own screen reader system. If you have a complicated UI, your website may actually become harder to operate through the injected tool. 

Because of these issues tools like this are not a substitute for building your site with accessibility in mind. Invest time and money into providing the best experience for all of your users. Reliance on one-stop solutions could cost you the same or more, than simply building things the correct way. By testing and building with accessibility in mind you'll also get the benefit of empathy and understanding of your customers.

To be clear this is not referring to testing tools, specifically this is regarding tools that claim to solve accessibility woes for you. Testing tools themselves are great and you should be using them, in-addition to manual testing. 

[Learn more about accessibility scripts/overlays.](https://overlayfactsheet.com/)

HubSpot Developer Podcast[](https://developers.hubspot.com/docs/cms/guides/accessibility#hubspot-developer-podcast)
-------------------------------------------------------------------------------------------------------------------

In January 2021 HubSpotters along with Jon Sasala of Morey Creative chatted about accessibility.

More accessibility information[](https://developers.hubspot.com/docs/cms/guides/accessibility#more-accessibility-information)
-----------------------------------------------------------------------------------------------------------------------------

There are some really great resources out there for building accessible-minded websites. We highly, highly encourage you to check them out.

*   [The A11Y Project](https://a11yproject.com/)
*   [MDN Accessibility Docs](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
*   [Web Accessibility Initiative](https://www.w3.org/WAI/) 
*   [WebAIM](https://webaim.org/) 
*   [Simplified WCAG 2 checklist](https://webaim.org/standards/wcag/checklist) 
*   [Section 508 checklist](https://webaim.org/standards/508/checklist) 
*   [Detailed WCAG 2.2 recommendations](https://www.w3.org/TR/WCAG22/) 
*   [AXE by Deque](https://www.deque.com/axe/)
*   [WAVE](https://wave.webaim.org/) - a tool for testing the accessibility of a webpage
*   [The Ultimate guide to web accessibility](https://blog.hubspot.com/website/web-accessibility)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/accessibility#page-feedback)
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
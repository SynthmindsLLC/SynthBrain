---
title: "Custom quote templates"
description: "Information on how to use and build custom quote templates in HubSpot."
type: "concept"
tags:
- "HubSpot"
- "Quotes"
- "Templates"
- "Customization"
relationships:
- "#used_by [[Sales Hub]]"
- "#has_part [[Custom quote variable reference]]"
- "#similar_to [[Custom page templates]]"
- "#derived_from [[Proposal templates]]"
- "#related_to [[Sales process]]"
- "#related_to [[E-signatures]]"
- "#related_to [[Payment processing]]"
- "#related_to [[Deal management]]"
- "#related_to [[Contact management]]"
- "#related_to [[Print media]]"
- "#related_to [[PDF]]"
- "#related_to [[CSS]]"
- "#related_to [[HubL]]"
latest_update: "2023-12-12"
---

Custom quote templates


==========================

Last updated: December 12, 2023

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Professional or Enterprise

In the sales process, a sales rep [creates a deal](https://knowledge.hubspot.com/deals/create-deals), then the sales rep [creates a quote associated with that deal](https://knowledge.hubspot.com/deals/use-quotes). The sales rep sends the quote URL or PDF to a prospect. The prospect then accepts or declines the quote. In some cases payment is exchanged right away, in some cases an e-signature is used.

**Please note:** you can create custom quote themes and templates with any HubSpot subscription, including _**CMS Free**_, but an account will need _**Sales Hub**_ _Professional_ or _Enterprise_ to use those templates for their quotes.

If you previous built proposal templates, learn [how to migrate an existing proposal template to quotes.](https://docs.google.com/document/d/1Cv3p4wnbjkNmkvvU_r9A_wjFZVuN_gLuUJpp4SO4Tyw/edit?usp=sharing)

Overview[](https://developers.hubspot.com/docs/cms/building-blocks/templates/quotes#overview)
---------------------------------------------------------------------------------------------

Custom quote templates are built using the same underlying systems that other types of templates use. For example:

*   Domain-level settings apply to quotes, including head and footer HTML and domain stylesheets. You can disable domain stylesheets using [template annotations.](/docs/cms/building-blocks/templates/html-hubl-templates#template-annotations)
*   Most of HubL's functionality works on quote templates, including functions, filters, if conditions, imports, and includes.
*   When using [personalization tokens](https://knowledge.hubspot.com/website-pages/personalize-your-content) in a quote, HubSpot will not render them dynamically. Instead, the token is rendered at the time of publishing the quote, and will not update upon signing. For this reason, you should not use personalization tokens for properties that are updated after a quote is published, including:
    *   Payment status
    *   Payment date
    *   Esign date
    *   Esign completed signatures

Due to the specific use-case of quotes, however, there are some key differences between how quotes work from the way page and email templates work:

*   More data is available to the quote template that is restricted for other template types. For example, quote and deal-related data is available to a quote template. You can also include contact data for quote recipients in a quote template.
*   There is not currently a [drag and drop](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas) editor for building quote templates. Instead, there is a module-based editor for customizing or hiding the modules that are already in a template.

Because more data is available to quote templates without requiring password protection. You should take care to only expose information that is truly required for the purpose of the quote.

Print and PDF versions of custom quotes[](https://developers.hubspot.com/docs/cms/building-blocks/templates/quotes#print-and-pdf-versions-of-custom-quotes)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Because quotes are web pages, you can use the same CSS you would use to optimize a web page for printing to provide a formatted PDF or print version of a custom quote template.

To do this, you can use a [CSS media query for print](https://developer.mozilla.org/en-US/docs/Web/CSS/@media#media_types) to target the print experience. You can test this experience by [using your browser's developer tools.](https://developers.google.com/web/tools/chrome-devtools/css/print-preview)

If you'd like to print, it's recommended to use the [download module](/docs/cms/building-blocks/modules/default-modules#quote-download). Alternatively, since a quote is a web page you can [use JavaScript and a button element](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_print) to provide an easy way to print the quote.

Related Resources[](https://developers.hubspot.com/docs/cms/building-blocks/templates/quotes#related-resources)
---------------------------------------------------------------------------------------------------------------

*   [Getting started with the CMS quotes theme](/getting-started-from-the-cms-quotes-theme-beta)
*   [Custom quote variable reference](/docs/cms/hubl/variables/quotes)
*   [Create and use custom quote templates (from the sales, sales ops/manager perspective)](https://knowledge.hubspot.com/deals/create-custom-quote-templates-beta)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/templates/quotes#page-feedback)
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
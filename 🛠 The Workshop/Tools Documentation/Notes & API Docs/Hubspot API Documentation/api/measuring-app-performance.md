---
title: "Measuring app performance in the App Marketplace"
description: "Guide on viewing and measuring app performance metrics, including installs, uninstall feedback, and engagement through UTM parameters for better analytics tracking."
type: "guide"
tags:
- "App Performance"
- "HubSpot Developer Account"
- "UTM Parameters"
- "SEO Strategies"
relationships:
- "#part_of [[App Marketplace]]"
- "#requires [[Log in to developer account]]"]]
- "#has_participant [[Marketer]], [[Sales Rep]], [[Product Manager]]"
- "#related_to [[Certification Requirements]], [[Listing Requirements]]"
- "#uses [[UTM Parameters]]"
- "#enables [[Traffic Analytics with HubSpot or Google Analytics]]"]]
- "#contributes_to [[SEO Strategies]]"
created: "2023-06-10"
---

Measuring app performance
=========================

You can view performance metrics for any app listed in the [App Marketplace](https://ecosystem.hubspot.com/marketplace/apps) in your developer account.

Log in to your developer account. If you're a marketer, sales rep, product manager, or in another non-developer role, you may need to be added to this account. If you don't see it listed as an option, ask an admin or someone on your IT team for help.

*   From the main menu in your developer account, navigate to **App Marketplace > Listings**. 
*   Scroll down to the app you’d like to evaluate and hover to the right. Click **More > View listing details**.  
    ![](https://lh5.googleusercontent.com/JCfE-Gp-t-VnoOEf6r1xxd_mfdPU8e4vTYpvd1BIIYygCQZiGknq08Lr9VH6PUfJRx1YW1aEdAMAcgzZaifLk-MqIO6imucwNHxkWTZrewnPa9WBPI-mMLMZx36pGies9ZP1nJvb)
*   On the _Listing Details_ tab, view the details for your app:
    *   **App installs:** the total number of times the app has been installed. Some ways to use this metric include:
        *   tracking your monthly install count in a spreadsheet to report on month-over-month growth.
        *   measuring the effectiveness of your app marketing campaigns by noting the install count before and after a campaign.
        *   tracking your progress towards the minimum 6+ active installs needed for [certification](/blog/how-to-build-customer-trust-through-certification) in the App Marketplace.
    *   **App uninstall feedback:** surveys that users can submit when uninstalling the app, including a count of surveys submitted and a download link. You can use this data to inform your product roadmap, adjust pricing, fix a bug, and better understand your users. When uninstalling, users go through the following flow:  
        *   After confirming the uninstall, the user will be prompted to fill out an exit survey.  
            ![Integrations_Home](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/Integrations_Home.png?width=440&name=Integrations_Home.png)
        *   Based on the user's answer, they may be prompted to fill out additional fields.
        *   A user can also choose to skip the survey and uninstall without providing a response.
    *   **App Partner Manager:** a HubSpot point of contact who can act as a thought-partner and answer questions that aren't answered by documentation.For all questions or initiatives regarding your integration with HubSpot, include your designated App Partner Manager. For other technical questions or issues regarding your integration with HubSpot, please contact [appsupport@hubspot.com](mailto:appsupport@hubspot.com) and cc your App Partner Manager.

![](https://lh3.googleusercontent.com/nFpSF3p38cnFc32YxCXD86sxQSmLMo-H-xWWQrAGcsbdZqReKC1K7lXfBo8AWwtToTsrkCeKq0U8sURbPfeCk_owYV67indlhWFqsD5ODdv-kcV9pIgNShF-wQt-Sd1jTCih_U7q)

Add UTM tags to your listing page content[](https://developers.hubspot.com/docs/api/measuring-app-performance#add-utm-tags-to-your-listing-page-content)
--------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to the above metrics, you can further measure engagement by including UTM parameters in the URLs on your app listing page. This enables you to view how much traffic is coming to your website from your listing page, using HubSpot, Google Analytics, or other analytics platforms of your choosing. 

It's recommended to add UTM parameters to the following URLs included on your listing page:

*   Supporting content on your App Marketplace listing page, such as your company website, supporting documentation, case study, and privacy policy.
*   The OAuth install URL that customers use when installing the app. 

For example, you could add the following string of UTM parameters to the end of your documentation URL:

`?utm_campaign=appmarketplacelisting&utm_medium=referral&utm_source=hubspot`

**Please note:** it's recommended to use UTM parameters that are consistent with other UTM tracking you or your marketing team may be using. Learn more about the [basics of UTM parameters](https://blog.hubspot.com/customers/understanding-basics-utm-parameters) and how to create UTM tracking URLs with [HubSpot](https://knowledge.hubspot.com/settings/how-do-i-create-a-tracking-url) and [Google Analytics](https://blog.hubspot.com/marketing/what-are-utm-tracking-codes-ht).

To add UTM parameters to the OAuth install URL:

*   In your app developer account, navigate to **Apps**.
*   Click the **name** of the app to edit its details.
*   In the left sidebar, navigate to **Basic info**.
*   Click the **Auth** tab.
*   In the _Redirect URLs_ section, update your redirect URL to contain your UTM parameters. This will update the app's install URL after saving, so you'll need to be sure you've updated any user-facing links to use the new URL. 

![update-redirect-url](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/update-redirect-url.png?width=934&name=update-redirect-url.png)

*   Click **Save**.

**Please note:** the install button URL field has a limit of 250 characters. If your UTM parameters result in exceeding that limit, you may need to use a url shortener, such as [Bitly](https://bitly.com/). 

To add UTM parameters to the app's supporting content:

*   In your app developer account, navigate to **App Marketplace** \> **Listings**.
*   In the _Marketplace Listings_ table, click the **name** of the app.
*   On the _Listing info_ tab, update the URL in the _Install button URL_ field with your UTM parameters.  
    ![install-button-url](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/install-button-url.png?width=595&name=install-button-url.png)
*   Click the **Support info** tab.
*   In the _Contact info_, _Support resources_, and _Terms of Service and Privacy Policy_, sections, update the URLs with your UTM parameters.  
    ![support-resources-section](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/support-resources-section.png?width=591&name=support-resources-section.png)
*   Once you've updated your URLs, click **Submit for review** in the top right corner.

Once reviewed and approved, the URLs on your app's listing page will be updated with your UTM parameters. You can then use analytics tools, such as [HubSpot](https://knowledge.hubspot.com/reports/analyze-your-site-traffic-with-the-traffic-analytics-tool) or Google Analytics, to view traffic coming from your URLs as categorized by your UTM parameters.

**Please note:** because your app listing can be found through Google and other search engines, it's also important to ensure your listing is SEO-friendly. One recommended strategy to improve your SEO is through backlinks. Whether you're writing website content, sending out email newsletters, or drafting social media messages, consider adding links to your listing page, along with relevant information about your integration. You can further expand your reach through strategies like [guest blogging](https://blog.hubspot.com/marketing/guest-blogging) to improve SEO authority.

Learn more about [creative ways to earn backlinks](https://blog.hubspot.com/marketing/backlink-strategies), and check out [HubSpot Academy's free lesson on link building](https://academy.hubspot.com/lessons/link-building-tutorial).

#### Related docs

[App certification requirements](/docs/api/certification-requirements)

[App listing requirements](/docs/api/app-marketplace-listing-requirements)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/measuring-app-performance#page-feedback)
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
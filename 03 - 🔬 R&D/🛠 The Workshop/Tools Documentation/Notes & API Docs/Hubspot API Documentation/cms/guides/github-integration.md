Set up continuous integration with a GitHub repository using GitHub Actions


===============================================================================

Last updated: August 29, 2023

As a part of your [development workflow](/docs/cms/guides/creating-an-efficient-development-workflow), you might prefer to keep your production codebase source of truth in version control. This would be especially helpful if you work as a part of a development team so that you can track changes and quickly roll them back if needed.

Using [GitHub Actions](https://github.com/features/actions), you can set up a continuous integration with a GitHub repository. This guide walks through the integration process, and assumes that you're familiar with:

*   [Using Git](https://docs.github.com/en/get-started/using-git) and GitHub
*   Building websites using the [HubSpot CLI](/docs/cms/guides/getting-started-with-local-development)

Below, learn how to set up the integration using the HubSpot CMS Deploy GitHub Action (recommended) or manually.

Send local files to GitHub[](https://developers.hubspot.com/docs/cms/guides/github-integration#send-local-files-to-github)
--------------------------------------------------------------------------------------------------------------------------

Before you can integrate with GitHub, you'll first need to gather your files locally.

*   If you have an existing CMS asset that lives in HubSpot, such as a theme or set of templates, you can fetch it by running the [fetch](/docs/cms/developer-reference/local-development-cli#fetch) command as follows: `hs fetch <HubSpot_src> <local_dest>`. Alternatively, you can download all files in the account's [developer file system](https://developers.hubspot.com/docs/cms/key-concepts#developer-file-system) by running `hs fetch /`.
*   To create a new local project, it's recommended to start with the [CMS theme boilerplate](/docs/cms/building-blocks/themes/hubspot-cms-boilerplate). If you haven't worked with the CMS theme boilerplate before, check out the [quickstart guide](/docs/cms/guides/getting-started). If you've already installed the HubSpot CLI and configured your local environment, you can create a new local theme from the boilerplate by running `hs create website-theme <new-theme-name>`. You'll then need to upload your files to HubSpot with the [hs upload](/docs/cms/developer-reference/local-development-cli#upload) command.

With your code available locally, you'll then [add it to a GitHub repository](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github). After adding your files to GitHub, proceed to the next step to either install HubSpot's pre-made GitHub Action (recommended) or [configure the Action manually](#manually-configure-the-action).

Use the HubSpot CMS Deploy GitHub Action (recommended)[](https://developers.hubspot.com/docs/cms/guides/github-integration#use-the-hubspot-cms-deploy-github-action-recommended-)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To streamline the process, HubSpot created a GitHub Action that you can install to your GitHub project to handle automatically deploying changes from a branch to your production HubSpot account.

[Install automatic CMS deploy GitHub action](https://developers.hubspot.com/cs/c/?cta_guid=a0ef9341-ea79-4df2-a97d-10414fd859be&signature=AAH58kESGH7NohDbLL89WS2F3yr-0XcUFg&portal_id=53&pageId=29844611101&placement_guid=e0132707-395d-4617-bd9d-0b21c8b129d5&click=7816d79e-5534-4736-935c-fefc20c275b9&redirect_url=APefjpEfxyErJIc4Y3m32lAjCvxhR5BZq-mg9Cdns1no6tVpAKpXleyb9B02p44mFW0CWnhP6P4s2Fx7DXPhyfsQMN6r3qXbMY2oee9W_PVOV_aE5rKzF6YOwAS_nknfKDtASJldUvdbu3JooQCG1pj3zHKEOqL8Sg&hsutk=5fd4c3e0bcba17d529a26524e9531de3&canon=https%3A%2F%2Fdevelopers.hubspot.com%2Fdocs%2Fcms%2Fguides%2Fgithub-integration&__hstc=20629287.5fd4c3e0bcba17d529a26524e9531de3.1715711068576.1715711068576.1715711068576.1&__hssc=20629287.1.1715711068576&__hsfp=1511885054&contentType=standard-page "Install automatic CMS deploy GitHub action") hbspt.cta.\_relativeUrls=true;hbspt.cta.load(53, 'e0132707-395d-4617-bd9d-0b21c8b129d5', {"useNewLoader":"true","region":"na1"});

Create and merge a pull request in main[](https://developers.hubspot.com/docs/cms/guides/github-integration#create-and-merge-a-pull-request-in-main)
----------------------------------------------------------------------------------------------------------------------------------------------------

*   With your secrets, workflows, and scripts in your GitHub repository, create a pull request and merge it into main. 
*   After merging the pull request, navigate to **Actions**. You should see your deploy Action run, which will then deploy your code to your HubSpot account.

Lock your asset in the design manager[](https://developers.hubspot.com/docs/cms/guides/github-integration#lock-your-asset-in-the-design-manager)
------------------------------------------------------------------------------------------------------------------------------------------------

Now that your source of truth lives in GitHub, you should lock your asset in HubSpot to prevent edits from being made there. This ensures that changes only come through the deploy action.

To lock assets in the design manager:

*   In your HubSpot account, navigate to **Marketing** > **Files and Templates** > **Design Tools**.
*   Locate your asset's folder in the left sidebar, then **right-click** and select **Lock folder**.

![design-manager-lock-folder](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/design-manager-lock-folder.png?width=343&height=339&name=design-manager-lock-folder.png)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/github-integration#page-feedback)
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
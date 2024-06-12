---
Please provide me with more information about the mission you want to describe. I need context to create a compelling mission statement. 

For example, tell me: "* **What is the purpose of the mission?** What are you trying to achieve?"
* **Who is the target audience?** Who will benefit from this mission?
* **What are the key values and principles that guide the mission?** 
* **What are some specific goals or objectives within the mission?**

The more information you give me, the better I can help you craft a strong and effective mission statement.
---

Link a GitHub repository to a project (BETA)
============================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

Connect a GitHub account to HubSpot to automatically trigger a new project build when your team pushes a change to an associated GitHub repository. You can then use familiar GitHub tools and workflows to streamline development on your project. Follow the instructions below to create a new project and associate it with an existing GitHub repository.

Before you link your repository, make sure you've run `hs project create` in the root directory of your repository, and you've committed and pushed the resulting code to GitHub. You can use the [getting started project template](https://github.com/HubSpot/getting-started-project-template) as a reference for the proper directory structure. If you're creating a project for the first time, check out the [setup guide](/docs/platform/developer-projects-setup) to help you configure your local environment.

To link your GitHub repository to a new project:

*   In your HubSpot account, navigate to **CRM Development**.
*   In the left sidebar menu, select **Projects**.
*   In the top right, click **New project**.
*   In the dialog box, select **Project from GitHub**, then click **Connect to GitHub**.
*   Log into your GitHub account, then authorize the HubSpot Projects integration:
    *   To grant HubSpot full access to all repositories in your account, select **All repositories**. If you only want to link a single repository to a project, select **Only select repositories**, then select a **repository**. After you've installed the integration, you can always authorize other repositories if needed by updating repository access in the _HubSpot Projects_ application configuration in your [GitHub account settings](https://github.com/settings/installations/).
    *   Click **Install & Authorize**.

![hs-projects-authorize-gh-integration](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hs-projects-authorize-gh-integration.png?width=400&name=hs-projects-authorize-gh-integration.png)

*   Back in HubSpot, in the dialog box, select the **radio button** next to the repository you want to link to your new project. 
*   Click the **Select branch** dropdown menu and select a **branch** that will trigger new builds when you or a team member pushes a change.
*   Click **Link GitHub repo**.

![hs-projects-confirm-gh-repo](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hs-projects-confirm-gh-repo.png?width=550&name=hs-projects-confirm-gh-repo.png)

Once linked, HubSpot will create a new build of your project any time someone pushes a change to the repository. If you've turned on [auto-deploy](/docs/platform/build-and-deploy-using-hubspot-projects#builds-and-deploying), the project will be deployed after the build completes.

![hs-projects-gh-integration-build-details-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hs-projects-gh-integration-build-details-tab.png?width=992&name=hs-projects-gh-integration-build-details-tab.png)

**Please note:**

*   When a project is linked to a GitHub repository, team members cannot upload code directly to the project using the [HubSpot CLI](/docs/platform/project-cli-commands#upload-to-hubspot).
*   After linking a GitHub repository, if you upgrade your GitHub plan to Enterprise and enforce SAML SSO, you'll need to reauthorize the HubSpot connection. Otherwise, HubSpot will not be able to retrieve existing project repositories or link new ones. Learn more about [SAML SSO for GitHub Enterprise](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/about-authentication-with-saml-single-sign-on#about-oauth-apps-github-apps-and-saml-sso).

Link and unlink a repository[](https://developers.hubspot.com/docs/platform/link-a-github-repository-to-a-project#link-and-unlink-a-repository)
-----------------------------------------------------------------------------------------------------------------------------------------------

In addition to creating a new project from an existing repository, you can also link an existing project to a repository. To link a GitHub repository to a project:

*   In your HubSpot account, navigate to **CRM Development**.
*   In the left sidebar menu, select **Projects**.
*   In the project, click the **Settings** tab.
*   Under _GitHub connection_, click **Link now**.   
    ![link-github-repo](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/link-github-repo.png?width=568&name=link-github-repo.png)
*   In the right sidebar, select the **repository** and **branch** to connect to, then click **Link GitHub repo**.

To unlink a GitHub repository from one of your projects:

*   In your HubSpot account, navigate to **CRM** **Development**.
*   In the left sidebar menu, select **Projects**.
*   Click the **name** of a project.
*   Click the **Settings** tab.
*   Under _GitHub Connection_, click **Unlink project from GitHub.**

![hs-projects-unlink-project-from-github](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hs-projects-unlink-project-from-github.png?width=831&name=hs-projects-unlink-project-from-github.png)

*   In the dialog box, click **Unlink project**.

Uninstall the HubSpot app in your GitHub account[](https://developers.hubspot.com/docs/platform/link-a-github-repository-to-a-project#uninstall-the-hubspot-app-in-your-github-account)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To fully disconnect GitHub from your HubSpot account:

*   In your HubSpot account, navigate to **Settings**.
*   In the left sidebar menu, navigate to **Integrations** > **Connected Apps**.
*   On the GitHub integration tile, click **Actions**, then select **Uninstall**.

The GitHub account will then be disconnected from the account, unlinking any projects in the account that have been linked to the connected branch. Commits to the branch will no longer trigger new builds in HubSpot.

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/link-a-github-repository-to-a-project#page-feedback)
-----------------------------------------------------------------------------------------------------------------------

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
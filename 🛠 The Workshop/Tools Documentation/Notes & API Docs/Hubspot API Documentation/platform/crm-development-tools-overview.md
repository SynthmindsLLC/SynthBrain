CRM development tools overview (BETA)
=====================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

HubSpot's CRM development tools enable you to customize your CRM with UI extensions, with features like development sandboxes, version control, and GitHub integration to streamline your development process. Starting in your local environment, you can use these tools to build and deploy UI extensions across CRM records to customize user experience along with sending and retrieving data as needed.

For example, you can build a custom card that retrieves data from an external source.

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="width: 49.9464%; padding: 4px; border: 0;"><p><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example-code-2.png?width=457&amp;height=339&amp;name=custom-extension-example-code-2.png" width="457" height="339" loading="lazy" alt="custom-extension-example-code-2" style="height: auto; max-width: 100%; width: 457px;" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example-code-2.png?width=229&amp;height=170&amp;name=custom-extension-example-code-2.png 229w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example-code-2.png?width=457&amp;height=339&amp;name=custom-extension-example-code-2.png 457w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example-code-2.png?width=686&amp;height=509&amp;name=custom-extension-example-code-2.png 686w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example-code-2.png?width=914&amp;height=678&amp;name=custom-extension-example-code-2.png 914w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example-code-2.png?width=1143&amp;height=848&amp;name=custom-extension-example-code-2.png 1143w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example-code-2.png?width=1371&amp;height=1017&amp;name=custom-extension-example-code-2.png 1371w" sizes="(max-width: 457px) 100vw, 457px"></p></td><td style="width: 49.9464%; padding: 4px; border: 0;"><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example.png?width=405&amp;height=375&amp;name=custom-extension-example.png" width="405" height="375" loading="lazy" alt="custom-extension-example" style="height: auto; max-width: 100%; width: 405px;" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example.png?width=203&amp;height=188&amp;name=custom-extension-example.png 203w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example.png?width=405&amp;height=375&amp;name=custom-extension-example.png 405w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example.png?width=608&amp;height=563&amp;name=custom-extension-example.png 608w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example.png?width=810&amp;height=750&amp;name=custom-extension-example.png 810w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example.png?width=1013&amp;height=938&amp;name=custom-extension-example.png 1013w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/custom-extension-example.png?width=1215&amp;height=1125&amp;name=custom-extension-example.png 1215w" sizes="(max-width: 405px) 100vw, 405px"></td></tr></tbody></table>

Below, learn more about the CRM development tools and how to get started using them.

CRM development tools[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#crm-development-tools)
--------------------------------------------------------------------------------------------------------------------------

### Projects[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#projects)

Projects are the highest-level container that you'll create using the CRM development tools. Projects enable you to locally build and deploy private apps, UI extensions, and serverless functions using the CLI. Once deployed to an account, you can view and manage the project and its apps and UI extensions in HubSpot. This includes viewing build history and monitoring API calls. 

Learn more about [creating projects](/docs/platform/create-a-project), and check out HubSpot's growing list of [sample projects](/docs/platform/sample-projects) to see examples of what's possible.

### Private apps[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#private-apps)

Private apps enable you to send and retrieve data using the private app's access token for authentication. Private apps also execute serverless functions that server as the backend for UI extensions. A project can contain one private app, and each private app can contain multiple UI extensions and serverless functions. 

Learn more about [creating private apps](/docs/platform/create-private-apps-with-projects-ui-extensions).

Private apps built with projects currently only support building UI extensions. If you'd like to build a private app to work with HubSpot's other extensions, learn more about the [different types of apps and what they support](/docs/api/developer-tools-overview).

### UI extensions[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#ui-extensions)

UI extensions are custom UI elements that users in the HubSpot account can view and interact with. At this time, custom cards for CRM records are the only available UI extension. For example, you can create a custom card that enables users to submit form data to an external database from any contact record. 

UI extensions are built using projects and consist of a front end and back end:

*   **UI extension front end:** the user-facing part of the extension, which consists of [HubSpot-built components](/docs/platform/ui-extension-components). Along with displaying information, users can interact with components to perform a variety of actions. You'll build the frontend with either React or TypeScript.
*   **UI extension back end:** the [serverless function](/docs/platform/serverless-functions) which enables a UI extension to send, and retrieve data to display in components. Powered by the project's private app, a serverless function can be reused by multiple components as needed. 

The custom cards you can build with projects are separate from [HubSpot's other custom card API extension](/docs/api/crm/extensions/overview), and they cannot be built interchangeably.

Learn more about [how UI extensions work](/docs/platform/ui-extensions-overview).

### Serverless functions[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#serverless-functions)

A serverless function executes server-side JavaScript to provide back end functionality to a UI extensions. Serverless functions are contained within private apps. Serverless functions consist of a folder that contains one or more JavaScript files that export a `main` function, and a `serverless.json` file that registers and configures your functions.

Learn more about [creating serverless functions with projects](https://developers.hubspot.com/docs/platform/serverless-functions).

While similar in concept, serverless functions used in projects are different from the serverless functions used by the HubSpot CMS. Some of these differences include:

*   You cannot create a serverless function in a project with the `hs create function` command.
*   Serverless functions created in projects cannot be used for CMS pages.
*   Serverless functions created in projects don't appear in the design manager.

To build serverless functions for CMS pages, check out the [CMS developer documentation](/docs/cms/guides/getting-started-with-serverless-functions).

### Development sandboxes[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#development-sandboxes)

Development sandboxes enable you to develop projects in a lightweight testing environment to ensure your project's components work as expected before deploying to a [standard sandbox or production account](https://developers.hubspot.com/docs/api/account-types).

Development sandboxes are created through the CLI and can be accessed within the production HubSpot account. Development sandboxes sync some account assets on creation, but not all, and have additional limits compared to standard sandboxes.

Learn more about [setting up a development sandbox](/docs/platform/developer-projects-setup).

### GitHub integration[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#github-integration)

If you prefer to use GitHub for version control, you can connect a [GitHub repository to a project](/docs/platform/link-a-github-repository-to-a-project) to automatically trigger project builds when you push a change to the connected repository. This enables you to use GitHub tools and workflows to streamline development, whether you work alone or with a team.

Get started[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#get-started)
------------------------------------------------------------------------------------------------------

If you're not currently enrolled in the CRM development tools beta, you can join directly form your HubSpot account:

*   In your HubSpot account, click your **account name** in the top right corner, then click **Product updates**.
*   In the left sidebar, select **In beta**.
*   In the list of betas, search for or scroll to the **CRM development tools to build UI extensions with React as frontend** beta, then click **Join beta**.  
    ![crm-development-tools-join-beta](https://developers.hubspot.com/hs-fs/hubfs/crm-development-tools-join-beta.png?width=2252&height=880&name=crm-development-tools-join-beta.png)

After joining the beta, get started with any of the following options:

*   Follow the [quickstart guide](/docs/platform/ui-extensions-quickstart) to quickly build and deploy a working example custom card.
*   Check out [HubSpot's sample projects](/docs/platform/sample-projects) to see examples of what's possible.
*   Build your project from scratch by starting with the [HubSpot projects guide](/docs/platform/create-a-project).

More resources[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#more-resources)
------------------------------------------------------------------------------------------------------------

*   [CRM development tools on the HubSpot Community](https://community.hubspot.com/t5/CRM-Development-Tools-Beta/gh-p/crm-development-tools-beta)
*   [CRM development tools on the HubSpot Developer Blog](/blog/crm-development-tools-for-hubspot-developers-beta)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#page-feedback)
----------------------------------------------------------------------------------------------------------------

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
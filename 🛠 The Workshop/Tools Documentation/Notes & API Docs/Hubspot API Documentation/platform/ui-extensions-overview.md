UI Extensions overview (BETA)
=============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

HubSpot UI extensions enable you to customize HubSpot’s CRM record UI to suit your needs. UI extensions can interact with both HubSpot and external data so that you can quickly access data from within and outside of the account. 

React-based UI extensions differ from the previously released JSON-based extensions by offering:

*   More interactivity and flexibility, whereas JSON-based custom cards could be considered more static.
*   A full-stack approach with a separation between the UI component front end from the serverless function back end. One serverless function can be reused by multiple UI components as needed.

By building full-stack UI extensions with React, you can create interactive, state-based experiences for HubSpot users across CRM record pages.

How UI extensions work[](https://developers.hubspot.com/docs/platform/ui-extensions-overview#how-ui-extensions-work)
--------------------------------------------------------------------------------------------------------------------

Full-stack UI extensions are built using React as a primary front end framework and HubSpot's serverless functions as a backend for operations such as fetching data. Extensions are built locally using the HubSpot CLI, which you'll use to run a HubSpot local development server for the front end and deploy back end changes to the HubSpot account. Extensions are powered by the UI extensions SDK, which offers a number of actions, utilities, and UI components. The UI extensions SDK is published as an [npm package](https://www.npmjs.com/package/@hubspot/ui-extensions/v/next), which you'll include in the `package.json` file within the `extensions` directory. 

The UI extensions SDK enables you to:

*   Register an extension with HubSpot
*   Run serverless functions
*   Add actions to your extension, such as opening an iframe in a modal, adding success and failure alerts, and fetching CRM properties

*   Build the extension's UI with components
*   Fetch user and account data[](#fetch-user-and-account-data)

Learn about [adding functionality to your extension through the SDK](/docs/platform/create-ui-extensions#add-ui-extension-functionality).

While a _**Sales Hub**_ or **_Service Hub_** _Enterprise_ account is needed to create UI extensions, a paid seat is not required to view UI extensions or custom tabs on CRM records. Any user in the account will be able to view and use UI extensions once uploaded to the account.

### Structure and schema[](https://developers.hubspot.com/docs/platform/ui-extensions-overview#structure-and-schema)

A UI extension is built using developer projects and is contained within a private app. The extension then uses components to render a UI and display information retrieved by the app’s serverless function. UI components are provided by the UI Extension SDK and can be customized through their included fields. Because you’re using React, you can also create your own component building blocks by packaging these components and importing them as needed.

At a high level, a React-based UI extension consists of:

*   **Serverless function back end:** an `app.functions` directory containing the serverless function .js file and a .json configuration. You can also add a `package.json` file to include any needed dependencies. The serverless function sends/fetches data that your React components can later use.
*   **React front end:** an extensions directory containing `.jsx` or `.tsx` files to render components, along with the card’s `.json` configuration and a required `package.json` that includes any needed dependencies.

![ui-extension](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension.png?width=477&height=440&name=ui-extension.png)

As shown in the screenshot above, the front end and back end directories both include their own `package.json` file. You can use these files to include dependencies as needed.

Working with data[](https://developers.hubspot.com/docs/platform/ui-extensions-overview#working-with-data)
----------------------------------------------------------------------------------------------------------

You can fetch data in multiple ways, depending on the data source:

*   To fetch third-party data, you can make API requests authenticated by secrets.
*   To fetch HubSpot data, you can:  
    *   use the `fetchCrmObjectProperties` action to fetch data from the currently displaying CRM record.
    *   use HubSpot's API endpoints to fetch data outside of the currently displaying CRM record.
    *   use GraphQL to query CRM data directly. 

### Fetch data via API call[](https://developers.hubspot.com/docs/platform/ui-extensions-overview#fetch-data-via-api-call)

*   To work with external, non-HubSpot data, you can use an API client, such as Axios or other third-party clients, in your serverless function. To authenticate these requests, learn how to [create and use secrets in serverless functions](/docs/platform/serverless-functions#including-secrets-in-a-function).
*   You can similarly fetch data via HubSpot's APIs, but instead of authenticating with a secret, you'll use the private app's access token. Learn more about [authenticating HubSpot API calls with private app access tokens](/docs/platform/serverless-functions#authenticate-hubspot-api-calls).

The code below shows an example of how to fetch third-party API data in the serverless function, then pull that data into UI components with React. This example is taken from the [get-started project template](https://github.com/HubSpot/ui-extensions-react-examples/tree/main/get-started), which you can create by running `hs project create --templateSource "HubSpot/ui-extensions-react-examples"`. 

// Fetch data with Axios const axios = require("axios"); // Fetch data with HubSpot's API client const hubSpotClient = new hubspot.Client({ accessToken: process.env.PRIVATE\_APP\_ACCESS\_TOKEN})

### Fetch HubSpot CRM data[](https://developers.hubspot.com/docs/platform/ui-extensions-overview#fetch-hubspot-crm-data)

To fetch data from the HubSpot account, such as displaying property data from the record you’re viewing, you’ll pass the `fetchCrmObjectProperties` method to the extension via `hubspot.extend()` in your React files. This method automatically handles authentication, so you don't need to include a private app access token. Learn more about [the fetchCrmObjectProperties method](/docs/platform/create-ui-extensions#fetch-crm-property-data).

hubspot.extend(({ actions }) => ( <HelloWorld fetchProperties={actions.fetchCrmObjectProperties} /> )); const HelloWorld = ({ runServerless, fetchProperties }) => { const \[firstName, setFirstName\] = useState(""); const \[lastName, setLastName\] = useState(""); useEffect(() => { fetchProperties(\["firstname", "lastname"\]) .then(properties => { setFirstName(properties.firstname); setLastName(properties.lastname); }); }, \[fetchProperties\]); return ( <Text>Hello {firstName} {lastName}</Text> ); }

In addition to using `fetchCrmObjectProperties`, [CRM data components](/docs/platform/ui-components/crm-data-components) can fetch and visualize HubSpot data out of the box.

If you want to fetch HubSpot data outside of the CRM record, you'll need to make a [HubSpot API call](#fetch-data-via-api-call) instead. You can also use GraphQL to query CRM data through the `/collector/graphql` endpoint. Learn more about [querying CRM data using GraphQL](https://developers.hubspot.com/docs/cms/data/query-hubspot-data-using-graphql).

Best practices[](https://developers.hubspot.com/docs/platform/ui-extensions-overview#best-practices)
----------------------------------------------------------------------------------------------------

### Using serverless functions

For security, the React front end cannot fetch data directly with APIs. Instead, you'll use HubSpot serverless functions to fetch the data you need. Then, with React you'll use `runServerlessFunction` to call the serverless function and send your JSON payload as parameters. Learn more about [runServerlessFunction](/docs/platform/ui-extensions-sdk#runserverlessfunction).

Because UI extensions are split between front end and back end, you can call multiple serverless functions from the same card. Or, you can reuse the same serverless function to run different operations and pass them as needed to the front end.

If your serverless function requires secrets, learn more about [managing secrets for deployed serverless functions and local development](https://developers.hubspot.com/docs/platform/serverless-functions#managing-secrets).

### Handling failure with serverless functions

There are two ways that `runServerlessFunction` can fail:

*   A failure in executing the serverless function
*   A failure in executing your code inside the serverless function

You can handle both scenarios by catching the error inside your serverless function with `try ... catch` blocks. On the React front end side, you'll need to check for `status` in the response, treating `SUCCESS` and `ERROR` appropriately. To ensure a good user experience in HubSpot, you can use the [ErrorState component](/docs/platform/ui-components/errorstate) to communicate error messages with next steps.

![FE-BE-diagram](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/FE-BE-diagram.png?width=1400&height=642&name=FE-BE-diagram.png)

**Please note:** functions have a response limit of 15 seconds. Functions that take longer to execute will fail. 

Limitations[](https://developers.hubspot.com/docs/platform/ui-extensions-overview#limitations)
----------------------------------------------------------------------------------------------

In rendering React-based, full-stack UI extensions, HubSpot uses [sandboxed iframes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#sandbox) for isolation, [web workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) for untrusted code execution, and [Shopfiy's remote-ui library](https://shopify.engineering/remote-rendering-ui-extensibility) for UI abstraction. This enables you to build with familiar tools like React and JavaScript, and `remote-ui` translates that into specific components to the host via `postmessage`. This process is essentially serializing a React element tree and sending it through `postmessage` for the host to evaluate. This results in benefits, such as:

*   Helping to protect both you and HubSpot with a sound and resilient solution for isolated code execution, while ensuring a consistent in-app user experience through the use of HubSpot's component library.
*   Providing you with a productive and delightful developer experience by leveraging mainstream frameworks like React.

However, it also separates the UI extensions from typical web applications built with React. Below, learn more about some of differences you can expect when developing React-based UI extensions.

### Non-HubSpot component libraries

When building UI extensions on HubSpot, you can only use the [components](/docs/platform/ui-components) provided through the [UI extensions SDK](/docs/platform/create-ui-extensions#add-ui-extension-functionality). Each component has a set of parameters that you can use for customization, but these components cannot be customized beyond those parameters. 

### Accessing DOM elements

Because UI extensions are rendered through sandboxed iframes, they cannot directly access the DOM. This restriction means that common methods of DOM manipulation and event listening, such as `document.getElementById` or `document.addEventListener`, are unavailable within the iframe's local script context. However, some components provide callback functions that you can use for certain events, like clicks, focus, and input.

#### Examples of unsupported hooks

*   React Router's `useNavigate()` hook will not function as expected within a UI extension. This hook manipulates the browser's window object to change the URL, which is not allowed within a sandboxed iframe.
*   The `useForm()` hook from react-hook-form is not supported because it relies on creating event listeners directly on DOM elements for form validation and submission, which is not allowed within a sandboxed iframe.

### Custom styles on HubSpot components

Because you can't access the DOM and components don't pass the `style` prop to the renderer, you can only style components with the provided component props.

### Making client-side HTTP requests

You cannot make client-side HTTP requests through UI extensions, meaning browser features like `fetch` and `XMLHttpRequest` will not work, nor will libraries like Axios, which is built around those features. Instead, requests should be made through the serverless function, executed by HubSpot behind the scenes.

### Using cookies to store session information

Requests made within the sandbox do not contain cookies, so rather than trying to store session information with cookies, you can look to the `context` object, which is passed to the extension component via `hubspot.extend`. This object contains information related to the authenticated user and HubSpot account. Learn more about [fetching account and user data](/docs/platform/create-ui-extensions#fetch-account-and-user-information).

Related content[](https://developers.hubspot.com/docs/platform/ui-extensions-overview#related-content)
------------------------------------------------------------------------------------------------------

*   [UI extensions quickstart guide (BETA)](/docs/platform/ui-extensions-quickstart)
*   [Create UI extensions with React (BETA)](https://developers.hubspot.com/docs/platform/create-ui-extensions)
*   [UI extension components (BETA)](/docs/platform/ui-components)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-extensions-overview#page-feedback)
--------------------------------------------------------------------------------------------------------

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
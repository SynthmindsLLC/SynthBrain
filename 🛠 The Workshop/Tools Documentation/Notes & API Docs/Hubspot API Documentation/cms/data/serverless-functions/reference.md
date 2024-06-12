---
Please provide me with the context or topic for the mission!  

For example, tell me: "* **What is the mission about?** (e.g., a space exploration mission, a community service project, a business venture) "
* **Who is involved?** (e.g., a team of astronauts, a group of volunteers, a company)
* **What is the goal?** (e.g., to explore Mars, to help the homeless, to become the leading provider of sustainable energy) 

Once I have this information, I can help you craft a compelling and impactful mission statement!
---

Serverless functions reference


==================================

Last updated: April 26, 2024

**Please note:** if you're building a serverless function as a part of a [developer project](/platform/create-a-project-for-ui-extensions), visit the [developer projects serverless function documentation](/docs/platform/serverless-functions) instead. The documentation below is for building serverless functions outside of the developer project platform.

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Enterprise

In this article, learn about the files found inside of a [serverless `.functions` folder](/docs/cms/features/serverless-functions#serverless-function-folders) and the CLI commands you can use with serverless functions.

For a high-level overview of serverless functions, see the [serverless functions overview](/docs/cms/features/serverless-functions).

For more information about building serverless functions with projects for [JavaScript rendered modules and partials](https://github.hubspot.com/cms-js-building-block-examples/), see the [developer projects documentation](/docs/platform/serverless-functions).

Serverless.json[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#serverless-json)
--------------------------------------------------------------------------------------------------------------

In the [`.functions` folder](/docs/cms/features/serverless-functions#serverless-function-folders), the `serverless.json` file stores the serverless function configuration. This is a required file, and maps your functions to their [endpoints](#endpoints).

// serverless.json { "runtime": "nodejs18.x", "version": "1.0", "environment": { "globalConfigKey": "some-value" }, "secrets": \["secretName"\], "endpoints": { "events": { "file": "function1.js", "method":"GET" }, "events/update": { "method": "POST", "file": "action2.js", "environment": { "CONFIG\_KEY": "some-other-value" }, "secrets": \["googleKeyName","otherkeyname"\] } } }

Use this table to describe parameters / fields
| key | Type | Description |
| --- | --- | --- |
| 
`runtime`

required



 | String | 

The runtime environment. Supports the following [Node.js](https://nodejs.org/en/about/) versions:

*   Node 20 (`nodejs20.x`) (recommended)
*   Node 18 (`nodejs18.x`)

Note that HubSpot will [no longer support Node 16](/changelog/deprecation-of-node-v16-in-all-serverless-functions) beyond July 12, 2024.

 |
| 

`version`

required



 | String | 

HubSpot serverless function schema version. (Current version 1.0)

 |
| 

`environment`

 | Object | 

Configuration variables passed to the executing function as [environment variables](https://nodejs.org/docs/latest-v10.x/api/process.html#process_process_env) at runtime. You might use this to add logic for using a testing version of an API instead of the real thing based on an environment variable.

 |
| 

`secrets`

 | Array | 

An array containing the names of the secrets your serverless function will use for authentication. Do not store secret values directly in this file, only reference secret names. 

 |
| 

`endpoints`

required



 | Object | 

Endpoints define the paths that are exposed and their mapping to specific JavaScript files, within your functions folder. Learn more about endpoints below.

 |

**Please note:** do not assign the same name to your secrets and environment variables. Doing so will result in conflicts when returning their values in the function.

### Endpoints[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#endpoints)

Each endpoint can have its own [environment variables](https://nodejs.org/docs/latest-v10.x/api/process.html#process_process_env) and secrets. Variables specified outside of endpoints should be used for configuration settings that apply to all functions and endpoints.

"events/update": { "method": "POST", "file": "action2.js", "environment": { "configKey": "some-other-value" }, "secrets": \["googleAPIKeyName","otherKeyName"\] }

Endpoints have a couple unique keys.

Use this table to describe parameters / fields
| key | Type | Description |
| --- | --- | --- |
| 
`method`

 | String or array of strings | 

[HTTP method or methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) that the endpoint supports. Defaults to [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET).

 |
| 

`file`

required



 | String | 

Path to JavaScript function file with the implementation for the endpoint.

 |

Serverless functions are exposed through a path at your HubSpot CMS account’s domain. This includes default `.hs-sites.com` sub-domains.

You can access these functions at the following URL: 

`https://{domainName}/_hcms/api/{endpoint-name/path}?portalid={hubId}`.

Below, learn about each URL component:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`domainName`

 | 

Your domain name.

 |
| 

`/_hcms/api/`

 | 

The path reserved for serverless functions. All endpoints exist inside this path.

 |
| 

`endpoint-name/path`

 | 

The endpoint name or path that you specified in the `serverless.json` file.

 |
| 

`hubId`

 | 

Your Hub ID. Providing this in the request will enable you to test your functions within module and template previews.

 |

Function file[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#function-file)
----------------------------------------------------------------------------------------------------------

In addition to the `serverless.json` configuration file, the `.functions` folder will also contain a [Node.js](https://nodejs.org/en/) JavaScript file that defines the function. You can also leverage the [request](https://github.com/request/request#readme) library to make HTTP request to [HubSpot APIs](https://developers.hubspot.com/docs/api/overview) and other APIs.

For example:

// Require axios library, to make API requests. const axios = require('axios'); // Environment variables from your serverless.json // process.env.globalConfigKey exports.main = (context, sendResponse) => { // your code called when the function is executed // context.params // context.body // context.accountId // context.limits // secrets created using the CLI are available in the environment variables. // process.env.secretName //sendResponse is what you will send back to services hitting your serverless function. sendResponse({body: {message:"my response"}, statusCode: 200}); };

### Context object[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#context-object)

The context object contains contextual information about the function's execution, stored in the following parameters.

Context Object Keys
| Parameter | Description |
| --- | --- |
| 
`accountId`

 | 

The HubSpot account ID containing the function.

 |
| 

`body`

 | 

Populated if the request is sent as a `POST` with a content type of `application/json`.

 |
| 

`contact`

 | 

If the request is from a cookied contact, the contact object will be populated with a set of basic contact properties along with the following information:

*   `vid`: The contact’s visitor ID.
*   `isLoggedIn`: when using CMS Memberships, this will be `true` if the contact is logged in to the domain.
*   `listMemberships`: an array of contact list IDs that this contact is a member of.

 |
| 

`headers`

 | 

Contains the [headers](#headers) sent from the client hitting your endpoint.

 |
| 

`params`

 | 

Populated with query string values along with any HTML Form-POSTed values. These are structured as a map with strings as keys and an array of strings for each value.

`context.params.yourvalue`

 |
| 

`limits`

 | 

Returns how close you are to hitting the [serverless function rate limits](/docs/cms/features/serverless-functions#know-your-limits).

*   `executionsRemaining`: how many executions per minute are remaining.
*   `timeRemaining`: how much allowed execution time is remaining.

 |

### Headers[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#headers)

If you need to know the headers of the client that's hitting your endpoint, you can access them through `context.headers`, similar to how you would access information through `context.body`.

Below, review some of the common headers that HubSpot provides. For a full list, see [MDN's HTTP headers documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).

Use this table to describe parameters / fields
| header | Description |
| --- | --- |
| 
`accept`

 | 

Communicates which content types expressed as [MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types), the client understands. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept).

 |
| 

`accept-encoding`

 | 

Communicates the content encoding the client understands. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-encoding).

 |
| 

`accept-language`

 | 

Communicates which human language and locale is preferred. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-language).

 |
| 

`cache-control`

 | 

Holds directives for caching. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control).

 |
| 

`connection`

 | 

Communicates whether the network connection stays open. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/connection).

 |
| 

`cookie`

 | 

Contains cookies by sent the client. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/cookie).

 |
| 

`host`

 | 

Communicates the domain name and TCP port number of a listening server. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/host).

 |
| 

`true-client-ip`

 | 

IP address of the end-user. [See Cloudflare true-client-ip](https://support.cloudflare.com/hc/en-us/articles/206776727-What-is-True-Client-IP-).

 |
| 

`upgrade-insecure-requests`

 | 

Communicates the clients preference for an encrypted and authenticated response. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Upgrade-Insecure-Requests).

 |
| 

`user-agent`

 | 

Vendor defined string identifying the application, operating system, application vendor, and version. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent).

 |
| 

`x-forwarded-for`

 | 

Identifies the originating IP address of a client through a proxy or load balancer. [See MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For).

 |

#### Redirect by sending a header[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#redirect-by-sending-a-header)

You can perform a redirect from your serverless function by  sending a response with a _location_ header and `301` statusCode.

sendResponse({ statusCode: 301, headers: { "Location": "https://www.example.com" } });

### Set cookies from your endpoint[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#set-cookies-from-your-endpoint)

From your serverless function you can tell the client (web browser) to set a cookie.

exports.main = (context, sendResponse) => { sendResponse({ body: { ... }, 'Set-Cookie': 'myCookie1=12345; expires=...; Max-Age=...', statusCode: 200 }); }

### Set multiple values for a single header[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#set-multiple-values-for-a-single-header)

For headers that support multiple values, you can use `multiValueHeaders`, to pass the values. For example: you can tell the browser to set multiple cookies.

exports.main = (context, sendResponse) => { sendResponse({ body: { ... }, multiValueHeaders: { 'Set-Cookie': \[ 'myCookie1=12345; expires=...; Max-Age=...', 'myCookie2=56789; expires=...; Max-Age=...' \] }, statusCode: 200 }); }

Secrets[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#secrets)
----------------------------------------------------------------------------------------------

When you need to authenticate a serverless function request, you'll use secrets to store values such as API keys or private app access tokens. Using the CLI, you can add secrets to your HubSpot account to store those values, which you can later access through environment variables (`process.env.secretName`). Secrets are managed through the HubSpot CLI using the following commands:

*   [`hs secrets list`](/docs/cms/developer-reference/local-development-cms-cli#list-secrets)
*   [`hs secrets add`](/docs/cms/developer-reference/local-development-cms-cli#add-secret)
*   [`hs secrets delete`](/docs/cms/developer-reference/local-development-cms-cli#remove-secret)

Once added through the CLI, secrets can be made available to functions by including a `secrets` array containing the name of the secret. This enables you to store your function code in [version control](/docs/cms/guides/github-integration) and use secrets without exposing them. However, you should never return your secret's value through console logging or as a response, as this will expose the secret in logs or in front-end pages that call your serverless function.

**Please note:** due to caching, it can take about one minute to see updated secret values. If you've just updated a secret but are still seeing the old value, check again after about a minute.

Using serverless functions with the form element[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#using-serverless-functions-with-the-form-element)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When submitting serverless functions use javascript to handle the form submission, and use the `"contentType" : "application/json"` header in your request. Do not use the `<form>` elements `action` attribute.

CORS[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#cors)
----------------------------------------------------------------------------------------

[**Cross Origin Resource Sharing (CORS)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature. By default browsers restrict cross-origin requests initiated by javascript. This prevents malicious code running on a different domain, from affecting your site. This is called the same-origin policy. Because sending and retrieving data from other servers is sometimes a necessity, the external server, can supply HTTP headers that communicate which origins are permitted to read the information from a browser.

You should not run into CORS issues calling your serverless function within your HubSpot hosted pages. If you do, verify you are using the correct protocol.

**Getting this CORS error?**  
_"Access to fetch at \[your function url\] from origin \[page making request\] has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled."_

**Is your request to a different origin than the site calling it?**

*   If the domain name is different, yes.
*   If using a different protocol(http, https), yes.

If using a different protocol, simply change the protocol to match and that will fix it. 

You can't modify HubSpot's `Access-Control-Allow-Origin` header at this time.

[See MDN for further detailed CORS error troubleshooting.](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors)

### Get requests[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#get-requests)

Get requests may be able to make [CORS requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) depending on the client. Do not make [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) requests write anything, just return data.

Preloaded packages[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#preloaded-packages)
--------------------------------------------------------------------------------------------------------------------

HubSpot serverless functions currently come preloaded with the following packages:

*   [@hubspot/api-client](https://www.npmjs.com/package/@hubspot/api-client): ^1.0.0-beta
*   [axios](https://www.npmjs.com/package/axios): ^0.19.2
*   [request](https://www.npmjs.com/package/request): ^2.88.0
*   [requests](https://www.npmjs.com/package/requests): ^0.2.2

To use the latest supported version of a preloaded package, or to use a newly added package:

1.  Clone or copy your function file.
2.  Change your function's endpoint in the `serverless.json` file to point to your new function file. You can safely delete the old version.

If you want to include packages outside of the preloaded package set, you can use [webpack](https://webpack.js.org/) to combine your node modules and have your bundled files be your function files.

Limits[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#limits)
--------------------------------------------------------------------------------------------

Serverless functions are intended to be fast and have a narrow focus. To enable quick calls and responses, HubSpot serverless functions have the following limits:

*   50 secrets per account.
*   128MB of memory.
*   No more than 100 endpoints per HubSpot account.
*   You must use `contentType` `application/json` when calling a function.
*   Serverless function logs are stored for 90 days.
*   6MB on an AWS Lambda invocation payload.

**Execution limits**

*   Each function has a maximum of 10 seconds of execution time.
*   Each account is limited to 600 total execution seconds per minute.

This means either of these scenarios can happen:

*   60 function executions that take 10 seconds each to complete.
*   6,000 function executions that take 100 milliseconds to complete.

Functions that exceed those limits will throw an error. Execution count and time limits will return a `429` response. The execution time of each function is included in the [serverless function logs](/docs/cms/developer-reference/local-development-cli#logs).  
  
To assist in avoiding these limits, limit data is provided automatically to the [function context](/docs/cms/features/serverless-functions/reference#function-file) during execution. You can use that to influence your application to stay within those limits. For example, if your application requires polling your endpoint, then you can return with your data a variable to influence the frequency of the polling. That way when traffic is high you can slow the rate of polling avoiding hitting limits, then ramp it back up when traffic is low.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/data/serverless-functions/reference#page-feedback)
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
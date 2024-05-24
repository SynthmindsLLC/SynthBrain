Client Libraries[](https://developers.hubspot.com/docs/api/client-libraries#client-libraries)
---------------------------------------------------------------------------------------------

Client libraries are designed to help you interact with the HubSpot APIs with less friction.  They are written in several different languages and help bridge the gap between your application and HubSpot’s APIs. They take away the need to know the exact URL and HTTP method to use for each API call among other things leaving you more time to focus on making your application.

Starting from the source code that powers the HubSpot application, HubSpot generate documents that describe our APIs using the [Open API](https://www.openapis.org/) format. Those documents are fed into the [Open API code generator](https://github.com/OpenAPITools/openapi-generator), these generated files end up in the libraries, but this isn’t the end of the story. A team of developers at HubSpot take the output of this code generation and add more value to it by adding utility functions to help with things like rate limiting as well as number of example applications to show how to use the libraries in practice. These examples cover a wide range of use cases so be sure to take advantage of them.

Use the endpoint below to access the available Open API specifications

`GET: [https://api.hubspot.com/api-catalog-public/v1/apis](https://api.hubspot.com/api-catalog-public/v1/apis)`

| 
###           **Language**

 | 

### Package Link

 | 

### [![github](https://53.fs1.hubspotusercontent-na1.net/hub/53/file-1741252957.svg)](https://github.com/HubSpot/hubspot-api-nodejs)Source Code

 |
| --- | --- | --- |
| 

![iconfinder_nodejs-512_339733](https://developers.hubspot.com/hs-fs/hubfs/iconfinder_nodejs-512_339733.png?width=60&name=iconfinder_nodejs-512_339733.png)**Node.js**

 | 

[npm install @hubspot/api-client](https://www.npmjs.com/package/@hubspot/api-client)

 | 

[hubspot-api-nodejs](https://github.com/HubSpot/hubspot-api-nodejs)

 |
| 

![new-php-logo](https://developers.hubspot.com/hs-fs/hubfs/new-php-logo.png?width=60&name=new-php-logo.png)

**PHP**

 | 

[composer require hubspot/api-client](https://packagist.org/packages/hubspot/api-client)

 | 

[hubspot-api-php](https://github.com/HubSpot/hubspot-api-php)

 |
| 

![ruby](https://developers.hubspot.com/hs-fs/hubfs/ruby.png?width=50&name=ruby.png)

**Ruby**

 | 

[gem install hubspot-api-client](https://rubygems.org/gems/hubspot-api-client)

 | 

[hubspot-api-ruby](https://github.com/HubSpot/hubspot-api-ruby)

 |
| 

![iconfinder_267_Python_logo_4375050](https://developers.hubspot.com/hs-fs/hubfs/iconfinder_267_Python_logo_4375050.png?width=60&name=iconfinder_267_Python_logo_4375050.png)

**Python**

 | 

[pip install hubspot-api-client](https://pypi.org/project/hubspot-api-client/)

 | 

[hubspot-api-python](https://github.com/HubSpot/hubspot-api-python)

 |

Get started[](https://developers.hubspot.com/docs/api/client-libraries#get-started)
-----------------------------------------------------------------------------------

To start using these client libraries, you'll need a HubSpot account, either a standard account or an app developer account.  This will enable you to create a [private app](/docs/api/private-apps) so that you can [use the private app token to authenticate your calls](/docs/api/private-apps#make-api-calls-with-your-app-s-access-token). You can also create a [HubSpot developer account](https://developers.hubspot.com/docs/api/developer-tools-overview) and use [OAuth](https://developers.hubspot.com/docs/api/working-with-oauth) to authenticate your calls.

Once you have a HubSpot account and a private app access token or OAuth token, you can install the library. Below, see an example of installing the Node.JS client, instantiating the client, and general usage.

### Install 

npm install @hubspot/api-client

### **Instantiate client**

//Authenticate via private app access token stored as a secret const hubspot = require('@hubspot/api-client') const hubspotClient = new hubspot.Client({ accessToken: process.env.secretName }) //Or via OAuth const hubspotClient = new hubspot.Client({ accessToken: YOUR\_ACCESS\_TOKEN })

### **Usage**

//Example call hubspotClient.crm.contacts.basicApi .getPage(limit, after, properties, associations, archived) .then((results) => { console.log(results.body) }) .catch((err) => { console.error(err) })

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/client-libraries#page-feedback)
---------------------------------------------------------------------------------------------

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
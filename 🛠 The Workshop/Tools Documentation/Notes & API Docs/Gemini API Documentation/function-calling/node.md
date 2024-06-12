---
Please provide me with more context!  To help you create a compelling mission statement, I need to know: "* **What is the purpose of this mission statement?** Is it for a company, a project, a personal goal, or something else entirely? "
* **What are the goals and values of the entity this mission statement is for?**  
* **What makes this entity unique or special?** 
* **What impact do you want to have on the world?** 

Once you provide me with this information, I can help you craft a powerful and meaningful mission statement that reflects your vision and inspires action.
---

*   On this page
*   [Set up your project](#set-up-project)
    *   [Set up and secure your API key](#set-up-secure-api-key)
    *   [Install the SDK package](#add-sdk)
    *   [Initialize the generative model](#initialize-model)
*   [Set up a function call](#set-up-function-call)
    *   [Step 1: Create the function that makes the API request](#create-function-for-request)
    *   [Step 2: Create a function declaration](#create-function-declaration)
    *   [Step 3: Specify the function declaration during model initialization](#specify-function-declaration-during-model-initialization)
    *   [Step 4: Generate a function call](#generate-function-call)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Join the Gemini API Developer Competition! [Learn more](/competition)

*   [Google AI for Developers](https://ai.google.dev/)
*   [Gemini API](https://ai.google.dev/gemini-api)
*   [Docs](https://ai.google.dev/gemini-api/docs)

Was this helpful?

Send feedback

Tutorial: Function calling with the Gemini API
==============================================

bookmark\_borderbookmark Stay organized with collections Save and categorize content based on your preferences.

*   On this page
*   [Set up your project](#set-up-project)
    *   [Set up and secure your API key](#set-up-secure-api-key)
    *   [Install the SDK package](#add-sdk)
    *   [Initialize the generative model](#initialize-model)
*   [Set up a function call](#set-up-function-call)
    *   [Step 1: Create the function that makes the API request](#create-function-for-request)
    *   [Step 2: Create a function declaration](#create-function-declaration)
    *   [Step 3: Specify the function declaration during model initialization](#specify-function-declaration-during-model-initialization)
    *   [Step 4: Generate a function call](#generate-function-call)

Python Node.js Go Dart (Flutter) Android Swift Web

  

Function calling makes it easier for you to get structured data outputs from generative models. You can then use these outputs to call other APIs and return the relevant response data to the model. In other words, function calling helps you connect generative models to external systems so that the generated content includes the most up-to-date and accurate information.

You can provide Gemini models with descriptions of functions. These are functions that you write in the language of your app (that is, they're not Google Cloud Functions). The model may ask you to call a function and send back the result to help the model handle your query.

If you haven't already, check out the [Introduction to function calling](/gemini-api/docs/function-calling) to learn more.

Set up your project
-------------------

Before calling the Gemini API, you need to set up your project, which includes setting up your API key, installing the SDK package, and initializing the model.

### Set up and secure your API key

To use the Gemini API, you'll need an API key. If you don't already have one, create a key in Google AI Studio.

[Get an API key](https://aistudio.google.com/app/apikey)

#### Secure your API key

It's strongly recommended that you do _not_ check an API key into your version control system. Instead, you should use a secrets store for your API key.

All the snippets in this tutorial assume that you're accessing your API key as an environment variable.

### Install the SDK package

To use the Gemini API in your own application, you need to install the `GoogleGenerativeAI` package for Node.js:

npm install @google/generative-ai

### Initialize the generative model

Before you can make any API calls, you need to import and initialize the generative model. This is the basic initialization; later in this tutorial you'll update it for function calling.

    const { GoogleGenerativeAI } = require("@google/generative-ai");// Access your API key as an environment variable (see "Set up your API key" above)const genAI = new GoogleGenerativeAI(process.env.API_KEY);// ...// Use a model that supports function calling, like a Gemini 1.5 modelconst model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});// ...

Set up a function call
----------------------

For this tutorial, you'll have the model interact with a hypothetical currency exchange API that supports the following parameters:

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `currencyFrom` | string | yes | Currency to convert from |
| `currencyTo` | string | yes | Currency to convert to |

#### Example API request

    {  "currencyFrom": "USD",  "currencyTo": "SEK"}

#### Example API response

    {  "base": "USD",  "rates": {"SEK": 0.091}}

### **Step 1**: Create the function that makes the API request

If you haven't already, start by creating the function that makes an API request.

For demonstration purposes in this tutorial, rather than sending an actual API request, you'll be returning hardcoded values in the same format that an actual API would return.

    async function makeApiRequest(currencyFrom, currencyTo) {  // This hypothetical API returns a JSON such as:  // {"base":"USD","rates":{"SEK": 0.091}}  return {    base: currencyFrom,    rates: { [currencyTo]: 0.091 },  };}

### **Step 2**: Create a function declaration

Create the function declaration that you'll pass to the generative model (next step of this tutorial).

Include as much detail as possible in the function and parameter descriptions. The generative model uses this information to determine which function to select and how to provide values for the parameters in the function call.

    // Function declaration, to pass to the model.const getExchangeRateFunctionDeclaration = {  name: "getExchangeRate",  parameters: {    type: "OBJECT",    description: "Get the exchange rate for currencies between countries",    properties: {      currencyFrom: {        type: "STRING",        description: "The currency to convert from.",      },      currencyTo: {        type: "STRING",        description: "The currency to convert to.",      },    },    required: ["currencyTo", "currencyFrom"],  },};// Executable function code. Put it in a map keyed by the function name// so that you can call it once you get the name string from the model.const functions = {  getExchangeRate: ({ currencyFrom, currencyTo }) => {    return makeApiRequest( currencyFrom, currencyTo)  }};

### **Step 3**: Specify the function declaration during model initialization

Specify the function declaration when initializing the generative model by setting the model's `tools` parameter:

    const { GoogleGenerativeAI } = require("@google/generative-ai");// Access your API key as an environment variable (see "Set up your API key" above)const genAI = new GoogleGenerativeAI(process.env.API_KEY);// ...const generativeModel = genAI.getGenerativeModel({  // Use a model that supports function calling, like a Gemini 1.5 model  model: "gemini-1.5-flash",  // Specify the function declaration.  tools: {    functionDeclarations: [getExchangeRateFunctionDeclaration],  },});

### **Step 4**: Generate a function call

Now you can prompt the model with the defined function.

The recommended way to use function calling is through the chat interface, since function calls fit nicely into chat's multi-turn structure.

    const chat = generativeModel.startChat();const prompt = "How much is 50 US dollars worth in Swedish krona?";// Send the message to the model.const result = await chat.sendMessage(prompt);// For simplicity, this uses the first function call found.const call = result.response.functionCalls()[0];if (call) {  // Call the executable function named in the function call  // with the arguments specified in the function call and  // let it call the hypothetical API.  const apiResponse = await functions[call.name](call.args);  // Send the API response back to the model so it can generate  // a text response that can be displayed to the user.  const result2 = await chat.sendMessage([{functionResponse: {    name: 'getExchangeRate',    response: apiResponse  }}]);  // Log the text response.  console.log(result2.response.text());}

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-06 UTC.
---
Please provide me with more information about the mission you'd like to write about! 

To help me craft a compelling mission statement, tell me: "* **What is the mission about?** Is it a personal mission, a business mission, a mission for a project, etc.?"
* **What are the goals?** What do you want to achieve?
* **What are the values?** What principles will guide your actions?
* **Who is the audience?** Who are you trying to reach with this mission?

Once I have this information, I can help you write a clear, concise, and inspiring mission statement.
---

*   On this page
*   [Set up your project](#set-up-project)
    *   [Set up and secure your API key](#set-up-secure-api-key)
    *   [Add the SDK dependency to your project](#add-sdk)
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
    *   [Add the SDK dependency to your project](#add-sdk)
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

**Note:** Function calling isn't yet supported for Java on Android. The samples in this guide are Kotlin.

Set up your project
-------------------

Before calling the Gemini API, you need to set up your Android project, which includes setting up your API key, adding the SDK dependencies to your Android project, and initializing the model.

### Set up and secure your API key

To use the Gemini API, you'll need an API key. If you don't already have one, create a key in Google AI Studio.

[Get an API key](https://aistudio.google.com/app/apikey)

#### Secure your API key

It's strongly recommended that you do _not_ check an API key into your version control system. Instead, you should store it in a `local.properties` file (which is located in your project's root directory, but excluded from version control), and then use the [Secrets Gradle plugin for Android](https://github.com/google/secrets-gradle-plugin) to read your API key as a Build Configuration variable.

    // Access your API key as a Build Configuration variableval apiKey = BuildConfig.apiKey

All the snippets in this tutorial utilize this best practice. Also, if you want to see the implementation of the Secrets Gradle plugin, you can review the [sample app](http://github.com/google/generative-ai-android/tree/main/generativeai-android-sample) for this SDK or use the latest preview of Android Studio Iguana which has a [_Gemini API Starter_ template](https://developer.android.com/studio/preview/gemini-template) (which includes the `local.properties` file to get you started).

### Add the SDK dependency to your project

1.  In your **module (app-level)** Gradle configuration file (like `<project>/<app-module>/build.gradle.kts`), add the dependency for the Google AI SDK for Android:
    
        dependencies {  // ... other androidx dependencies  // add the dependency for the Google AI client SDK for Android  implementation("com.google.ai.client.generativeai:generativeai:0.6.0")}
    
2.  Sync your Android project with Gradle files.
    

### Initialize the generative model

Before you can make any API calls, you need to initialize the `GenerativeModel` object. This is the basic initialization; later in this tutorial you'll update it for function calling.

    val generativeModel = GenerativeModel(    // Use a model that supports function calling, like a Gemini 1.5 model    modelName = "gemini-1.5-flash",    // Access your API key as a Build Configuration variable (see "Set up your API key" above).    apiKey = BuildConfig.apiKey)

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

    suspend fun makeApiRequest(    currencyFrom: String,    currencyTo: String): JSONObject {    // This hypothetical API returns a JSON such as:    // {"base":"USD","rates":{"SEK": 0.091}}    return JSONObject().apply {        put("base", currencyFrom)        put("rates", hashMapOf(currencyTo to 0.091))    }}

### **Step 2**: Create a function declaration

Create the function declaration that you'll pass to the generative model (next step of this tutorial).

Include as much detail as possible in the function and parameter descriptions. The generative model uses this information to determine which function to select and how to provide values for the parameters in the function call.

    val getExchangeRate = defineFunction(  name = "getExchangeRate",  description = "Get the exchange rate for currencies between countries",  Schema.str("currencyFrom", "The currency to convert from."),  Schema.str("currencyTo", "The currency to convert to.")) { from, to ->    // Call the function that you declared above    makeApiRequest(from, to)}

### **Step 3**: Specify the function declaration during model initialization

Specify the function declaration when initializing the generative model by passing it into the model's `tools` parameter:

    val generativeModel = GenerativeModel(  // Use a model that supports function calling, like a Gemini 1.5 model  modelName = "gemini-1.5-flash",  // Access your API key as a Build Configuration variable (see "Set up your API key" above)  apiKey = BuildConfig.apiKey,  // Specify the function declaration.  tools = listOf(Tool(listOf(getExchangeRate))))

### **Step 4**: Generate a function call

Now you can prompt the model with the defined function.

The recommended way to use function calling is through the chat interface, since function calls fit nicely into chat's multi-turn structure.

    val chat = generativeModel.startChat()val prompt = "How much is 50 US dollars worth in Swedish krona?"// Send the message to the generative modelvar response = chat.sendMessage(prompt)// Check if the model responded with a function callresponse.functionCall?.let { functionCall ->  // Try to retrieve the stored lambda from the model's tools and  // throw an exception if the returned function was not declared  val matchedFunction = generativeModel.tools?.flatMap { it.functionDeclarations }      ?.first { it.name == functionCall.name }      ?: throw InvalidStateException("Function not found: ${functionCall.name}")  // Call the lambda retrieved above  val apiResponse: JSONObject = matchedFunction.execute(functionCall)  // Send the API response back to the generative model  // so that it generates a text response that can be displayed to the user  response = chat.sendMessage(    content(role = "function") {        part(FunctionResponsePart(functionCall.name, apiResponse))    }  )}// Whenever the model responds with text, show it in the UIresponse.text?.let { modelResponse ->    println(modelResponse)}

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-06 UTC.
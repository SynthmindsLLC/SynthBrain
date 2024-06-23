[

Libraries
=========

](/docs/libraries/libraries)

[

Python library
--------------

](/docs/libraries/python-library)

We provide a [Python library](https://github.com/openai/openai-python), which you can install by running:

    pip install openai

Once installed, you can use the library and your secret key to run the following:

    1
    2
    3
    4
    5
    6
    7
    8
    9
    from openai import OpenAI
    client = OpenAI(
        # Defaults to os.environ.get("OPENAI_API_KEY")
    )
    
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello world"}]
    )

The bindings also will install a command-line utility you can use as follows:

    $ openai api chat_completions.create -m gpt-3.5-turbo -g user "Hello world"

* * *

[

TypeScript / JavaScript library
-------------------------------

](/docs/libraries/typescript-javascript-library)

We provide a [TypeScript / JavaScript library](https://github.com/openai/openai-node) with support for Node.js and various [other runtimes](https://deno.land/x/openai). Install it by running:

    1
    2
    3
    npm install --save openai
    # or
    yarn add openai

Once installed, you can use the library and your secret key to run the following:

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    import OpenAI from "openai";
    
    const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
    });
    
    const chatCompletion = await openai.chat.completions.create({
        messages: [{ role: "user", content: "Say this is a test" }],
        model: "gpt-3.5-turbo",
    });

* * *

[

.NET library

Beta


--------------------

](/docs/libraries/dotnet-library)

We provide a [.NET library](https://github.com/openai/openai-dotnet), which you can install by running:

    dotnet add package OpenAI --prerelease

Once installed, you can use the library and your secret key to run the following:

    1
    2
    3
    4
    5
    6
    7
    8
    using OpenAI.Chat;
    
    ChatClient client = new("gpt-3.5-turbo", Environment.GetEnvironmentVariable("OPENAI_API_KEY"));
    
    ChatCompletion chatCompletion = client.CompleteChat(
        [
            new UserChatMessage("Say 'this is a test.'"),
        ]);

* * *

[

Azure OpenAI libraries
----------------------

](/docs/libraries/azure-openai-libraries)

Microsoft's Azure team maintains libraries that are compatible with both the OpenAI API and Azure OpenAI services. Read the library documentation below to learn how you can use them with the OpenAI API.

*   [Azure OpenAI client library for .NET](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/openai/Azure.AI.OpenAI)
*   [Azure OpenAI client library for JavaScript](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai)
*   [Azure OpenAI client library for Java](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/openai/azure-ai-openai)
*   [Azure OpenAI client library for Go](https://github.com/Azure/azure-sdk-for-go/tree/main/sdk/ai/azopenai)

* * *

[

Community libraries
-------------------

](/docs/libraries/community-libraries)

The libraries below are built and maintained by the broader developer community. If you'd like to add a new library here, please follow the instructions in our [help center article](https://help.openai.com/en/articles/6684216-adding-your-api-client-to-the-community-libraries-page) on adding community libraries. You can also [watch our OpenAPI specification](https://github.com/openai/openai-openapi) repository on GitHub to get timely updates on when we make changes to our API.

Please note that OpenAI does not verify the correctness or security of these projects. **Use them at your own risk!**

[

### C# / .NET

](/docs/libraries/c-net)

*   [Betalgo.OpenAI](https://github.com/betalgo/openai) by [Betalgo](https://github.com/betalgo)
*   [OpenAI-API-dotnet](https://github.com/OkGoDoIt/OpenAI-API-dotnet) by [OkGoDoIt](https://github.com/OkGoDoIt)
*   [OpenAI-DotNet](https://github.com/RageAgainstThePixel/OpenAI-DotNet) by [RageAgainstThePixel](https://github.com/RageAgainstThePixel)

[

### C++

](/docs/libraries/c)

*   [liboai](https://github.com/D7EAD/liboai) by [D7EAD](https://github.com/D7EAD)

[

### Clojure

](/docs/libraries/clojure)

*   [openai-clojure](https://github.com/wkok/openai-clojure) by [wkok](https://github.com/wkok)

[

### Crystal

](/docs/libraries/crystal)

*   [openai-crystal](https://github.com/sferik/openai-crystal) by [sferik](https://github.com/sferik)

[

### Dart/Flutter

](/docs/libraries/dart-flutter)

*   [openai](https://github.com/anasfik/openai) by [anasfik](https://github.com/anasfik)

[

### Delphi

](/docs/libraries/delphi)

*   [DelphiOpenAI](https://github.com/HemulGM/DelphiOpenAI) by [HemulGM](https://github.com/HemulGM)

[

### Elixir

](/docs/libraries/elixir)

*   [openai.ex](https://github.com/mgallo/openai.ex) by [mgallo](https://github.com/mgallo)

[

### Go

](/docs/libraries/go)

*   [go-gpt3](https://github.com/sashabaranov/go-gpt3) by [sashabaranov](https://github.com/sashabaranov)

[

### Java

](/docs/libraries/java)

*   [openai-java](https://github.com/TheoKanning/openai-java) by [Theo Kanning](https://github.com/TheoKanning)

[

### Julia

](/docs/libraries/julia)

*   [OpenAI.jl](https://github.com/rory-linehan/OpenAI.jl) by [rory-linehan](https://github.com/rory-linehan)

[

### Kotlin

](/docs/libraries/kotlin)

*   [openai-kotlin](https://github.com/Aallam/openai-kotlin) by [Mouaad Aallam](https://github.com/Aallam)

[

### Node.js

](/docs/libraries/node-js)

*   [openai-api](https://www.npmjs.com/package/openai-api) by [Njerschow](https://github.com/Njerschow)
*   [openai-api-node](https://www.npmjs.com/package/openai-api-node) by [erlapso](https://github.com/erlapso)
*   [gpt-x](https://www.npmjs.com/package/gpt-x) by [ceifa](https://github.com/ceifa)
*   [gpt3](https://www.npmjs.com/package/gpt3) by [poteat](https://github.com/poteat)
*   [gpts](https://www.npmjs.com/package/gpts) by [thencc](https://github.com/thencc)
*   [@dalenguyen/openai](https://www.npmjs.com/package/@dalenguyen/openai) by [dalenguyen](https://github.com/dalenguyen)
*   [tectalic/openai](https://github.com/tectalichq/public-openai-client-js) by [tectalic](https://tectalic.com/)

[

### PHP

](/docs/libraries/php)

*   [orhanerday/open-ai](https://packagist.org/packages/orhanerday/open-ai) by [orhanerday](https://github.com/orhanerday)
*   [tectalic/openai](https://github.com/tectalichq/public-openai-client-php) by [tectalic](https://tectalic.com/)
*   [openai-php client](https://github.com/openai-php/client) by [openai-php](https://github.com/openai-php)

[

### Python

](/docs/libraries/python)

*   [chronology](https://github.com/OthersideAI/chronology) by [OthersideAI](https://www.othersideai.com/)

[

### R

](/docs/libraries/r)

*   [rgpt3](https://github.com/ben-aaron188/rgpt3) by [ben-aaron188](https://github.com/ben-aaron188)

[

### Ruby

](/docs/libraries/ruby)

*   [openai](https://github.com/nileshtrivedi/openai/) by [nileshtrivedi](https://github.com/nileshtrivedi)
*   [ruby-openai](https://github.com/alexrudall/ruby-openai) by [alexrudall](https://github.com/alexrudall)

[

### Rust

](/docs/libraries/rust)

*   [async-openai](https://github.com/64bit/async-openai) by [64bit](https://github.com/64bit)
*   [fieri](https://github.com/lbkolev/fieri) by [lbkolev](https://github.com/lbkolev)

[

### Scala

](/docs/libraries/scala)

*   [openai-scala-client](https://github.com/cequence-io/openai-scala-client) by [cequence-io](https://github.com/cequence-io)

[

### Swift

](/docs/libraries/swift)

*   [OpenAIKit](https://github.com/dylanshine/openai-kit) by [dylanshine](https://github.com/dylanshine)
*   [OpenAI](https://github.com/MacPaw/OpenAI/) by [MacPaw](https://github.com/MacPaw)

[

### Unity

](/docs/libraries/unity)

*   [OpenAi-Api-Unity](https://github.com/hexthedev/OpenAi-Api-Unity) by [hexthedev](https://github.com/hexthedev)
*   [com.openai.unity](https://github.com/RageAgainstThePixel/com.openai.unity) by [RageAgainstThePixel](https://github.com/RageAgainstThePixel)

[

### Unreal Engine

](/docs/libraries/unreal-engine)

*   [OpenAI-Api-Unreal](https://github.com/KellanM/OpenAI-Api-Unreal) by [KellanM](https://github.com/KellanM)
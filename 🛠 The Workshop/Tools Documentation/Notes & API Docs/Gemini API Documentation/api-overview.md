---
Please provide me with more context. What is the mission about?  I need more information to help you write a mission statement. For example, tell me: "* **What is the purpose of this mission?** Is it for a company, a project, a personal goal, or something else?"
* **What are the key objectives or values that this mission should reflect?** 
* **What is the desired outcome of this mission?**

Once I have a better understanding of your needs, I can help you write a compelling and effective mission statement.
---

*   이 페이지의 내용
*   [모델](#models)
*   [프롬프트 데이터 및 설계](#prompt_data_design)
    *   [프롬프트 설계 및 텍스트 입력](#prompt_design)
*   [콘텐츠 생성](#generate_content)
    *   [텍스트 및 이미지 입력](#text_image_input)
    *   [텍스트 전용 입력](#text_input)
    *   [멀티턴 대화 (채팅)](#chat)
    *   [스트리밍 응답](#stream)
    *   [JSON 형식 응답](#json)
*   [임베딩](#embedding)
*   [다음 단계](#next-steps)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

Gemini API 개요
=============

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [모델](#models)
*   [프롬프트 데이터 및 설계](#prompt_data_design)
    *   [프롬프트 설계 및 텍스트 입력](#prompt_design)
*   [콘텐츠 생성](#generate_content)
    *   [텍스트 및 이미지 입력](#text_image_input)
    *   [텍스트 전용 입력](#text_input)
    *   [멀티턴 대화 (채팅)](#chat)
    *   [스트리밍 응답](#stream)
    *   [JSON 형식 응답](#json)
*   [임베딩](#embedding)
*   [다음 단계](#next-steps)

Gemini API를 사용하면 Google의 최신 생성 모델에 액세스할 수 있습니다. API를 통해 사용할 수 있는 일반 기능에 익숙해졌다면 선택한 언어에 대한 튜토리얼을 진행하여 개발을 시작합니다.

**참고:** 생성형 AI 모델을 처음 사용한다면 [생성형 모델 가이드](https://ai.google.dev/gemini-api/docs/models/generative-models?hl=ko)를 방문하거나 [Google AI Studio](https://aistudio.google.com?hl=ko)에서 프롬프트 프로토타입 제작을 시작하세요.

모델
--

Gemini는 Google에서 개발한 일련의 멀티모달 생성형 AI 모델입니다. Gemini 모델은 선택한 모델 변형에 따라 프롬프트에서 텍스트 및 이미지를 허용하고 텍스트 응답을 출력할 수 있습니다.

자세한 모델 정보는 [Gemini 모델](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko) 페이지를 참고하세요. [`list_models`](https://ai.google.dev/api/python/google/generativeai/list_models?hl=ko) 메서드를 사용하여 사용 가능한 모든 모델을 나열한 다음 [`get_model`](https://ai.google.dev/api/python/google/generativeai/get_model?hl=ko) 메서드를 사용하여 특정 모델의 메타데이터를 가져올 수도 있습니다.

프롬프트 데이터 및 설계
-------------

특정 Gemini 모델은 텍스트 데이터와 미디어 파일을 모두 입력으로 허용합니다. 이 기능은 콘텐츠 생성, 데이터 분석, 문제 해결을 위한 많은 추가 가능성을 만듭니다. 사용 중인 모델의 일반적인 입력 토큰 한도를 비롯하여 고려해야 할 몇 가지 제한사항과 요구사항이 있습니다. 특정 모델의 토큰 한도에 대한 자세한 내용은 [Gemini 모델](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko)을 참조하세요.

Gemini API를 사용하는 프롬프트는 20MB를 초과할 수 없습니다. Gemini API는 프롬프트에 사용할 미디어 파일을 임시로 저장하는 [File API](https://ai.google.dev/api/rest/v1beta/files?hl=ko)를 제공하므로 20MB 제한을 초과하는 프롬프트 데이터를 제공할 수 있습니다. 메시지 표시에 지원되는 파일 형식 및 Files API 사용에 관한 자세한 내용은 [미디어 파일로 메시지 표시](https://ai.google.dev/tutorials/prompting_with_media?hl=ko)를 참고하세요.

### 프롬프트 설계 및 텍스트 입력

효과적인 프롬프트, 즉 프롬프트 엔지니어링은 예술과 과학의 결합입니다 프롬프트에 접근하는 방법에 대한 안내는 [프롬프트 소개](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ko)를 참고하고, 다양한 프롬프트 접근 방식에 대해서는 [프롬프트 기초](https://ai.google.dev/gemini-api/docs/models/generative-models?hl=ko#prompt101) 가이드를 참고하세요.

콘텐츠 생성
------

Gemini API를 사용하면 사용하는 모델 변형에 따라 프롬프트에 텍스트 데이터와 이미지 데이터를 모두 사용할 수 있습니다. 예를 들어 Gemini 1.5 모델을 사용하여 텍스트 전용 프롬프트 또는 멀티모달 프롬프트에서 텍스트를 생성할 수 있습니다. 이 섹션에서는 각각의 기본 코드 예를 제공합니다. 모든 매개변수를 다루는 자세한 예는 [`generateContent`](https://ai.google.dev/api/rest/v1beta/models/generateContent?hl=ko) API 참조를 확인하세요.

### 텍스트 및 이미지 입력

이미지가 포함된 텍스트 프롬프트를 Gemini 1.5 모델에 전송하여 비전 관련 작업을 수행할 수 있습니다. 예를 들어 이미지에 캡션을 추가하거나 이미지에 포함된 이미지를 식별합니다.

**참고:** Gemini 1.0 Pro Vision 모델에는 텍스트 전용 메시지를 보낼 수 없습니다. 대신 Gemini 1.5 모델 또는 Gemini 1.0 Pro 모델을 사용하세요.

다음 코드 예에서는 지원되는 각 언어에 대한 텍스트 및 이미지 프롬프트의 기본 구현을 보여줍니다.

[Python](#python) [Go](#go) [Node.js](#node.js)[웹](#웹) [Dart (Flutter)](#dart-flutter) [Swift](#swift)[Android](#android)[cURL](#curl) [더보기](#)

    model = genai.GenerativeModel('gemini-1.5-flash')cookie_picture = {    'mime_type': 'image/png',    'data': pathlib.Path('cookie.png').read_bytes()}prompt = "Do these look store-bought or homemade?"response = model.generate_content(    model="gemini-1.5-flash",    content=[prompt, cookie_picture])print(response.text)

전체 코드 스니펫은 [Python 가이드](https://ai.google.dev/gemini-api/docs/get-started/python?hl=ko)를 참조하세요.

    vmodel := client.GenerativeModel("gemini-1.5-flash")data, err := os.ReadFile(filepath.Join("path-to-image", imageFile))if err != nil {  log.Fatal(err)}resp, err := vmodel.GenerateContent(ctx, genai.Text("Do these look store-bought or homemade?"), genai.ImageData("jpeg", data))if err != nil {  log.Fatal(err)}

전체 예는 [Go 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/go?hl=ko)을 참조하세요.

    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });const prompt = "Do these look store-bought or homemade?";const image = {  inlineData: {    data: Buffer.from(fs.readFileSync("cookie.png")).toString("base64"),    mimeType: "image/png",  },};const result = await model.generateContent([prompt, image]);console.log(result.response.text());

전체 예시는 [Node.js 가이드](https://ai.google.dev/gemini-api/docs/get-started/node?hl=ko)를 참조하세요.

    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });const prompt = "Do these look store-bought or homemade?";const image = {  inlineData: {    data: base64EncodedImage /* see JavaScript quickstart for details */,    mimeType: "image/png",  },};const result = await model.generateContent([prompt, image]);console.log(result.response.text());

전체 예는 [웹 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/web?hl=ko)을 참조하세요.

    final model = GenerativeModel(model: 'gemini-1.5-flash', apiKey: apiKey);final prompt = 'Do these look store-bought or homemade?';final imageBytes = await File('cookie.png').readAsBytes();final content = [  Content.multi([    TextPart(prompt),    DataPart('image/png', imageBytes),  ])];final response = await model.generateContent(content);print(response.text);

전체 예는 [Dart (Flutter) 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/dart?hl=ko)을 참고하세요.

    let model = GenerativeModel(name: "gemini-1.5-flash", apiKey: "API_KEY")let cookieImage = UIImage(...)let prompt = "Do these look store-bought or homemade?"let response = try await model.generateContent(prompt, cookieImage)

전체 예는 [Swift 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/swift?hl=ko)을 참고하세요.

    val generativeModel = GenerativeModel(    modelName = "gemini-1.5-flash",    apiKey = BuildConfig.apiKey)val cookieImage: Bitmap = // ...val inputContent = content() {  image(cookieImage)  text("Do these look store-bought or homemade?")}val response = generativeModel.generateContent(inputContent)print(response.text)

전체 예는 [Android 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/android?hl=ko)을 참고하세요.

    curl https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key=${API_KEY} \    -H 'Content-Type: application/json' \    -X POST \    -d @<(echo'{          "contents":[            { "parts":[                {"text": "Do these look store-bought or homemade?"},                { "inlineData": {                    "mimeType": "image/png",                    "data": "'$(base64 -w0 cookie.png)'"                  }                }              ]            }          ]         }')

자세한 내용은 [REST API 가이드](https://ai.google.dev/gemini-api/docs/get-started/rest?hl=ko)를 참조하세요.

### 텍스트 전용 입력

Gemini API는 텍스트 전용 입력도 처리할 수 있습니다. 이 기능을 사용하면 텍스트 완성 및 요약과 같은 자연어 처리 (NLP) 작업을 실행할 수 있습니다.

다음 코드 예는 지원되는 각 언어에 대한 텍스트 전용 프롬프트의 기본 구현을 보여줍니다.

[Python](#python) [Go](#go) [Node.js](#node.js)[웹](#웹) [Dart (Flutter)](#dart-flutter) [Swift](#swift)[Android](#android)[cURL](#curl) [더보기](#)

    model = genai.GenerativeModel('gemini-1.5-flash')prompt = "Write a story about a magic backpack."response = model.generate_content(prompt)

전체 예는 [Python 가이드](https://ai.google.dev/gemini-api/docs/get-started/python?hl=ko)를 참조하세요.

    ctx := context.Background()client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("API_KEY")))if err != nil {  log.Fatal(err)}defer client.Close()model := client.GenerativeModel("gemini-1.5-flash")resp, err := model.GenerateContent(ctx, genai.Text("Write a story about a magic backpack."))if err != nil {  log.Fatal(err)}

전체 예는 [Go 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/go?hl=ko)을 참조하세요.

    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });const prompt = "Write a story about a magic backpack.";const result = await model.generateContent(prompt);console.log(result.response.text());

전체 예시는 [Node.js 가이드](https://ai.google.dev/gemini-api/docs/get-started/node?hl=ko)를 참조하세요.

    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });const prompt = "Write a story about a magic backpack.";const result = await model.generateContent(prompt);console.log(result.response.text());

전체 예는 [웹 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/web?hl=ko)을 참조하세요.

    final model = GenerativeModel(model: 'gemini-1.5-flash', apiKey: apiKey);final prompt = 'Write a story about a magic backpack.';final content = [Content.text(prompt)];final response = await model.generateContent(content);print(response.text);

전체 예는 [Dart (Flutter) 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/dart?hl=ko)을 참고하세요.

    let model = GenerativeModel(name: "gemini-1.5-flash", apiKey: "API_KEY")let prompt = "Write a story about a magic backpack."let response = try await model.generateContent(prompt)

전체 예는 [Swift 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/swift?hl=ko)을 참고하세요.

    val generativeModel = GenerativeModel(    modelName = "gemini-1.5-flash",    apiKey = BuildConfig.apiKey)val prompt = "Write a story about a magic backpack."val response = generativeModel.generateContent(prompt)print(response.text)

전체 예는 [Android 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/android?hl=ko)을 참고하세요.

    curl https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key=$API_KEY \    -H 'Content-Type: application/json' \    -X POST \    -d '{ "contents":[      { "parts":[{"text": "Write a story about a magic backpack"}]}    ]}'

자세한 내용은 [REST API 가이드](https://ai.google.dev/gemini-api/docs/get-started/rest?hl=ko)를 참조하세요.

### 멀티턴 대화 (채팅)

Gemini API를 사용하여 사용자를 위한 대화형 채팅 환경을 빌드할 수 있습니다. API의 채팅 기능을 사용하면 여러 차례의 질문과 응답을 수집할 수 있으므로 사용자는 점진적으로 답변을 얻거나 여러 부분으로 구성된 문제에 대한 도움을 받을 수 있습니다. 이 기능은 챗봇, 대화형 강사, 고객 지원 어시스턴트와 같이 지속적인 커뮤니케이션이 필요한 애플리케이션에 적합합니다.

다음 코드 예는 지원되는 각 언어에 채팅 상호작용의 기본 구현을 보여줍니다.

[Python](#python) [Go](#go) [Node.js](#node.js)[웹](#웹) [Dart (Flutter)](#dart-flutter) [Swift](#swift)[Android](#android)[cURL](#curl) [더보기](#)

  model = genai.GenerativeModel('gemini-1.5-flash')  chat = model.start_chat(history=[])  response = chat.send_message(      "Pretend you\'re a snowman and stay in character for each response.")  print(response.text)  response = chat.send_message(      "What\'s your favorite season of the year?")  print(response.text)

전체 예는 [Python 가이드](https://ai.google.dev/gemini-api/docs/get-started/python?hl=ko)의 채팅 데모를 참조하세요.

    model := client.GenerativeModel("gemini-1.5-flash")cs := model.StartChat()cs.History = []*genai.Content{  &genai.Content{    Parts: []genai.Part{      genai.Text("Pretend you're a snowman and stay in character for each response."),    },    Role: "user",  },  &genai.Content{    Parts: []genai.Part{      genai.Text("Hello! It's cold! Isn't that great?"),    },    Role: "model",  },}resp, err := cs.SendMessage(ctx, genai.Text("What's your favorite season of the year?"))if err != nil {  log.Fatal(err)}

전체 예는 [Go 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/go?hl=ko)의 채팅 데모를 참조하세요.

    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});const chat = model.startChat({  history: [    {      role: "user",      parts: "Pretend you're a snowman and stay in character for each response.",    },    {      role: "model",      parts: "Hello! It's cold! Isn't that great?",    },  ],  generationConfig: {    maxOutputTokens: 100,  },});const msg = "What's your favorite season of the year?";const result = await chat.sendMessage(msg);console.log(result.response.text());

전체 예시는 [Node.js 가이드](https://ai.google.dev/gemini-api/docs/get-started/node?hl=ko)의 채팅 데모를 참조하세요.

    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});const chat = model.startChat({  history: [    {      role: "user",      parts: "Pretend you're a snowman and stay in character for each response.",    },    {      role: "model",      parts: "Hello! It's so cold! Isn't that great?",    },  ],  generationConfig: {    maxOutputTokens: 100,  },});const msg = "What's your favorite season of the year?";const result = await chat.sendMessage(msg);console.log(result.response.text());

전체 예는 [웹 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/web?hl=ko)의 채팅 데모를 참조하세요.

    final model = GenerativeModel(model: 'gemini-1.5-flash', apiKey: apiKey);final chat = model.startChat(history: [  Content.text(      "Pretend you're a snowman and stay in character for each response."),  Content.model([TextPart("Hello! It's cold! Isn't that great?")]),]);final content = Content.text("What's your favorite season of the year?");final response = await chat.sendMessage(content);print(response.text);

전체 예는 [Dart (Flutter) 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/dart?hl=ko)의 채팅 데모를 참고하세요.

    let model = GenerativeModel(name: "gemini-1.5-flash", apiKey: "API_KEY")let chat = model.startChat()var message = "Pretend you're a snowman and stay in character for each response."var response = try await chat.sendMessage(message)message = "What\'s your favorite season of the year?"response = try await chat.sendMessage(message)

전체 예는 [Swift 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/swift?hl=ko)의 채팅 데모를 참조하세요.

    val generativeModel = GenerativeModel(    modelName = "gemini-1.5-flash",    apiKey = BuildConfig.apiKey)val chat = generativeModel.startChat()val response = chat.sendMessage("Pretend you're a snowman and stay in        character for each response.")print(response.text)

전체 예는 [Android 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/android?hl=ko)을 참고하세요.

    curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$API_KEY \    -H 'Content-Type: application/json' \    -X POST \    -d '{      "contents": [        {"role":"user",         "parts":[{           "text": "Pretend you're a snowman and stay in character for each        {"role": "model",            response."}]},         "parts":[{           "text": "Hello! It's so cold! Isn't that great?"}]},        {"role": "user",         "parts":[{           "text": "What\'s your favorite season of the year?"}]},       ]    }' 2> /dev/null | grep "text"

자세한 내용은 [REST API 가이드](https://ai.google.dev/gemini-api/docs/get-started/rest?hl=ko)를 참조하세요.

### 스트리밍 응답

Gemini API는 생성형 AI 모델에서 응답을 데이터 스트림으로 수신하는 추가적인 방법을 제공합니다. 스트리밍된 응답은 모델에서 생성되는 증분 데이터의 조각을 애플리케이션으로 다시 보냅니다. 이 기능을 사용하면 사용자 요청에 빠르게 응답하여 진행 상황을 표시하고 대화형 환경을 만들 수 있습니다.

스트리밍 응답은 자유 형식 프롬프팅 및 Gemini 모델과의 채팅을 위한 옵션입니다. 다음 코드 예에서는 지원되는 각 언어의 프롬프트에 스트리밍된 응답을 요청하는 방법을 보여줍니다.

[Python](#python) [Go](#go) [Node.js](#node.js)[웹](#웹) [Dart (Flutter)](#dart-flutter) [Swift](#swift)[Android](#android)[cURL](#curl) [더보기](#)

    prompt = "Write a story about a magic backpack."response = genai.stream_generate_content(    model="models/gemini-1.5-flash",    prompt=prompt)

전체 코드 스니펫은 [Python 가이드](https://ai.google.dev/gemini-api/docs/get-started/python?hl=ko)를 참조하세요.

    ctx := context.Background()client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("API_KEY")))if err != nil {  log.Fatal(err)}defer client.Close()model := client.GenerativeModel("gemini-1.5-flash")iter := model.GenerateContentStream(ctx, genai.Text("Write a story about a magic backpack."))for {  resp, err := iter.Next()  if err == iterator.Done {    break  }  if err != nil {    log.Fatal(err)  }  // print resp}

전체 예는 [Go 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/go?hl=ko)을 참조하세요.

    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });const prompt = "Write a story about a magic backpack.";const result = await model.generateContentStream([prompt]);// print text as it comes infor await (const chunk of result.stream) {  const chunkText = chunk.text();  console.log(chunkText);}

전체 예시는 [Node.js 가이드](https://ai.google.dev/gemini-api/docs/get-started/node?hl=ko)를 참조하세요.

    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });const prompt = "Write a story about a magic backpack.";const result = await model.generateContentStream([prompt]);// print text as it comes infor await (const chunk of result.stream) {  const chunkText = chunk.text();  console.log(chunkText);}

전체 예는 [웹 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/web?hl=ko)을 참조하세요.

    final model = GenerativeModel(model: 'gemini-1.5-flash', apiKey: apiKey);final prompt = 'Write a story about a magic backpack.';final content = [Content.text(prompt)];final response = model.generateContentStream(content);await for (final chunk in response) {  print(chunk.text);}

전체 예는 [Dart (Flutter) 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/dart?hl=ko)을 참고하세요.

    let model = GenerativeModel(name: "gemini-1.5-flash", apiKey: "API_KEY")let prompt = "Write a story about a magic backpack."let stream = model.generateContentStream(prompt)for try await chunk in stream {  print(chunk.text ?? "No content")}

전체 예는 [Swift 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/swift?hl=ko)을 참고하세요.

    val generativeModel = GenerativeModel(    modelName = "gemini-1.5-flash",    apiKey = BuildConfig.apiKey)val inputContent = content {  text("Write a story about a magic backpack.")}var fullResponse = ""generativeModel.generateContentStream(inputContent).collect { chunk ->  print(chunk.text)  fullResponse += chunk.text}

전체 예는 [Android 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/android?hl=ko)을 참고하세요.

    curl https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:streamGenerateContent?key=${API_KEY} \    -H 'Content-Type: application/json' \    --no-buffer \    -d '{ "contents":[            {"role": "user",              "parts":[{"text": "Write a story about a magic backpack."}]            }          ]        }' > response.json

자세한 내용은 [REST API 가이드](https://ai.google.dev/gemini-api/docs/get-started/rest?hl=ko)를 참조하세요.

### JSON 형식 응답

특히 응답을 사용하여 프로그래밍 인터페이스를 채우는 경우 애플리케이션에 따라 프롬프트에 대한 응답을 구조화된 데이터 형식으로 반환할 수 있습니다. Gemini API는 JSON 형식의 응답을 요청하는 구성 매개변수를 제공합니다.

**참고:** 이 응답 구성 옵션은 Gemini 1.5 Pro 및 1.5 Flash 모델에서만 지원됩니다.

`response_mime_type` 구성 옵션을 `application/json`로 설정하여 모델 출력 JSON을 생성할 수 있습니다. 프롬프트에서 응답으로 원하는 JSON 형식을 설명합니다.

[Python](#python)[cURL](#curl) [더보기](#)

    model = genai.GenerativeModel('gemini-1.5-flash',                              generation_config={"response_mime_type": "application/json"})prompt = """  List 5 popular cookie recipes.  Using this JSON schema:    Recipe = {"recipe_name": str}  Return a `list[Recipe]`  """response = model.generate_content(prompt)print(response.text)

    curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$API_KEY \    -H 'Content-Type: application/json' \    -X POST \    -d '{      "contents": [        {          "parts": [            {              "text": "\nList 5 popular cookie recipes.\n\nUsing this JSON schema:\n\n  Recipe = {\"recipe_name\": str}\n\nReturn a `list[Recipe]`\n      "            }          ]        }      ]      "generationConfig": {            "response_mime_type": "application/json",      }    }'

Gemini 1.5 플래시 모델은 반환하려는 JSON 스키마의 _텍스트_ 설명만 허용하지만 Gemini 1.5 Pro 모델을 사용하면 스키마 객체 (또는 상응하는 Python 유형)를 전달할 수 있으며 모델 출력은 이 스키마를 엄격하게 따릅니다. 이를 _제어된 생성_ 또는 _제한된 디코딩_이라고도 합니다.

예를 들어 `Recipe` 객체의 목록을 가져오려면 `list[Recipe]`를 `generation_config` 인수의 `response_schema` 필드에 전달합니다.

[Python](#python)[cURL](#curl) [더보기](#)

    import typing_extensions as typingclass Recipe(typing.TypedDict):  recipe_name: strmodel = genai.GenerativeModel(model_name="models/gemini-1.5-pro")result = model.generate_content(  "List 5 popular cookie recipes",  generation_config=genai.GenerationConfig(response_mime_type="application/json",                                           response_schema = list[Recipe]))print(result.text)

  curl https://generativelanguage.googleapis.com/v1beta/models/models/gemini-1.5-pro:generateContent?      -H 'Content-Type: application/json'      -X POST \      -d '{        "contents": [          {            "parts": [              {                "text": "List 5 popular cookie recipes"              }            ]          }        ],        "generationConfig": {          "responseMimeType": "application/json",          "responseSchema": {            "type": "ARRAY",            "items": {              "type": "OBJECT",              "properties": {                "recipe_name": {                  "type": "STRING"                }              }            }          }        }      }'  ```

자세한 내용은 [Gemini API 설명서](https://github.com/google-gemini/cookbook/tree/main)의 [JSON 모드 빠른 시작](https://github.com/google-gemini/cookbook/blob/main/quickstarts/JSON_mode.ipynb)을 참조하세요.

임베딩
---

Gemini API의 임베딩 서비스는 단어, 구문, 문장에 대한 최첨단 임베딩을 생성합니다. 그런 다음 그 결과 임베딩을 시맨틱 검색, 텍스트 분류, 클러스터링과 같은 NLP 태스크에 사용할 수 있습니다. 임베딩의 정의와 임베딩 서비스의 주요 사용 사례를 알아보려면 [임베딩 가이드](https://ai.google.dev/gemini-api/docs/embeddings?hl=ko)를 참고하세요.

다음 단계
-----

*   [Google AI Studio 빠른 시작](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=ko)을 사용하여 Google AI Studio UI 시작하기
*   [Python](https://ai.google.dev/gemini-api/docs/get-started/python?hl=ko), [Go](https://ai.google.dev/gemini-api/docs/get-started/go?hl=ko), [Node.js](https://ai.google.dev/gemini-api/docs/get-started/node?hl=ko) 튜토리얼을 통해 Gemini API에 대한 서버 측 액세스를 사용해 보세요.
*   [웹 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/web?hl=ko)을 따라 웹용 빌드를 시작하세요.
*   [Swift 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/swift?hl=ko) 또는 [Android 튜토리얼](https://ai.google.dev/gemini-api/docs/get-started/android?hl=ko)을 따라 모바일 앱 빌드를 시작하세요.
*   기존 Google Cloud 사용자이거나 Vertex에서 Gemini를 사용하여 강력한 Google Cloud 생태계를 활용하려는 경우 [Vertex AI의 생성형 AI](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/overview?hl=ko)에서 자세한 내용을 확인하세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-30(UTC)
*   이 페이지의 내용
*   [기본 요건](#prerequisites)
*   [프로젝트 설정](#set-up-project)
    *   [API 키 설정](#set-up-api-key)
    *   [프로젝트에 SDK 종속 항목 추가](#add-sdk)
    *   [생성 모델 초기화](#initialize-model)
*   [일반적인 사용 사례 구현](#implement-common-use-cases)
    *   [텍스트 전용 입력에서 텍스트 생성](#generate-text-from-text-input)
    *   [텍스트 및 이미지 입력에서 텍스트 생성 (멀티모달)](#generate-text-from-text-and-image-input)
    *   [멀티턴 대화 만들기 (채팅)](#multi-turn-conversations-chat)
    *   [스트리밍으로 더 빠른 상호작용](#streaming)
*   [고급 사용 사례 구현](#implement-advanced-use-cases)
    *   [함수 호출](#function-calling)
    *   [토큰 개수](#count-tokens)
*   [콘텐츠 생성을 제어하는 옵션](#control-content-generation)
    *   [모델 매개변수 구성](#model-parameters)
    *   [안전 설정 사용](#use-safety-settings)
*   [다음 단계](#whats-next)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

튜토리얼: Gemini API 시작하기
=====================

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [기본 요건](#prerequisites)
*   [프로젝트 설정](#set-up-project)
    *   [API 키 설정](#set-up-api-key)
    *   [프로젝트에 SDK 종속 항목 추가](#add-sdk)
    *   [생성 모델 초기화](#initialize-model)
*   [일반적인 사용 사례 구현](#implement-common-use-cases)
    *   [텍스트 전용 입력에서 텍스트 생성](#generate-text-from-text-input)
    *   [텍스트 및 이미지 입력에서 텍스트 생성 (멀티모달)](#generate-text-from-text-and-image-input)
    *   [멀티턴 대화 만들기 (채팅)](#multi-turn-conversations-chat)
    *   [스트리밍으로 더 빠른 상호작용](#streaming)
*   [고급 사용 사례 구현](#implement-advanced-use-cases)
    *   [함수 호출](#function-calling)
    *   [토큰 개수](#count-tokens)
*   [콘텐츠 생성을 제어하는 옵션](#control-content-generation)
    *   [모델 매개변수 구성](#model-parameters)
    *   [안전 설정 사용](#use-safety-settings)
*   [다음 단계](#whats-next)

Python Node.js 웹 REST Go Dart (Flutter) Android Swift

  

**주의:** **Android용 Google AI 클라이언트 SDK는 프로토타입 제작에만 사용하는 것이 좋습니다.** 프로토타입 제작이 아닌 사용 사례의 경우 백엔드 SDK를 사용하여 Google AI Gemini API에 액세스하는 것이 좋습니다. API 키를 Android 앱에 직접 삽입하거나 런타임에 원격으로 가져올 경우 API 키가 악의적인 행위자에게 노출될 위험이 있습니다.

이 튜토리얼에서는 Android용 Google AI 클라이언트 SDK를 사용하여 Android 앱에서 직접 Gemini API에 액세스하는 방법을 보여줍니다. Android 앱에서 Gemini 모델에 액세스하기 위해 REST API 또는 서버 측 코드(예: Python)로 직접 작업하지 않으려는 경우 이 클라이언트 SDK를 사용할 수 있습니다.

이 튜토리얼에서는 다음 작업을 수행하는 방법을 알아봅니다.

*   [API 키를 포함하여 프로젝트 설정](#set-up-project)
*   [텍스트 전용 입력에서 텍스트 생성](#generate-text-from-text-input)
*   [텍스트 및 이미지 입력에서 텍스트 생성 (멀티모달)](#generate-text-from-text-and-image-input)
*   [멀티턴 대화 만들기 (채팅)](#multi-turn-conversations-chat)
*   [스트리밍을 통한 빠른 상호작용](#streaming)

또한 이 가이드에는 고급 사용 사례 (예: [토큰 계산](#count-tokens))와 [콘텐츠 생성 제어](#control-content-generation) 옵션에 대한 섹션이 포함되어 있습니다.

**도움말:** 이 SDK를 빠르게 사용해 보거나 다양한 사용 사례의 완전한 구현을 확인하려면 **[샘플 앱](http://github.com/google/generative-ai-android/tree/main/generativeai-android-sample) 또는 [Android 스튜디오의 내장 템플릿](https://developer.android.com/studio/preview/gemini-template?hl=ko)**을 확인하세요.

샘플 앱 또는 템플릿을 실행하려면 이 가이드에 설명된 대로 기본 요건과 API 키가 필요합니다. 새 프로젝트 마법사에서 _Gemini API Starter_ 템플릿에 액세스하려면 [최신 미리보기 버전의 Android 스튜디오 Iguana](https://developer.android.com/studio/preview?hl=ko)가 필요합니다.

#### 기기에서 Gemini에 액세스하는 것을 고려해 보세요.

이 가이드에서 설명하는 Android용 클라이언트 SDK를 사용하면 _Google 서버에서 실행_되는 Gemini Pro 모델에 액세스할 수 있습니다. 민감한 정보 처리, 오프라인 가용성이 필요한 사용 사례 또는 자주 사용하는 사용자 흐름의 비용 절감을 위해 _기기에서 실행_되는 Gemini Nano 액세스를 고려할 수 있습니다. 자세한 내용은 [Android (기기 내) 튜토리얼](https://ai.google.dev/tutorials/android_aicore?hl=ko)을 참고하세요.

기본 요건
-----

이 가이드에서는 개발자가 Android 스튜디오를 사용하여 Android 앱을 개발하는 데 익숙하다고 가정합니다.

이 튜토리얼을 완료하려면 개발 환경과 Android 앱이 다음 요구사항을 충족해야 합니다.

*   Android 스튜디오 (최신 버전)
*   Android 앱은 API 수준 21 이상을 타겟팅해야 합니다.

프로젝트 설정
-------

Gemini API를 호출하기 전에 Android 프로젝트를 설정해야 합니다. 여기에는 API 키 설정, Android 프로젝트에 SDK 종속 항목 추가, 모델 초기화가 포함됩니다.

### API 키 설정

Gemini API를 사용하려면 API 키가 필요합니다. 아직 키가 없으면 Google AI Studio에서 키를 만듭니다

[API 키 가져오기](https://aistudio.google.com/app/apikey?hl=ko)

#### API 키 보호

API 키를 버전 제어 시스템에 체크인하지 _않는_ 것이 좋습니다. 대신 `local.properties` 파일(프로젝트 루트 디렉터리에 있지만 버전 제어에서 제외됨)에 저장한 후 [Android용 Secrets Gradle 플러그인](https://github.com/google/secrets-gradle-plugin)을 사용하여 API 키를 빌드 구성 변수로 읽어야 합니다.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

    // Access your API key as a Build Configuration variableval apiKey = BuildConfig.apiKey

    // Access your API key as a Build Configuration variableString apiKey = BuildConfig.apiKey;

이 튜토리얼의 모든 스니펫에는 이 권장사항이 활용됩니다. 또한 Secrets Gradle 플러그인의 구현을 확인하려면 이 SDK의 [샘플 앱](http://github.com/google/generative-ai-android/tree/main/generativeai-android-sample)을 검토하거나 [_Gemini API Starter_ 템플릿](https://developer.android.com/studio/preview/gemini-template?hl=ko)(시작하는 데 사용할 `local.properties` 파일이 포함되어 있음)이 있는 Android 스튜디오 Iguana의 최신 미리보기를 사용하면 됩니다.

### 프로젝트에 SDK 종속 항목 추가

1.  **모듈 (앱 수준)** Gradle 구성 파일 (예: `<project>/<app-module>/build.gradle.kts`)에서 Android용 Google AI SDK의 종속 항목을 추가합니다.
    
    [Kotlin](#kotlin) [Java](#java) [더보기](#)
    
        dependencies {  // ... other androidx dependencies  // add the dependency for the Google AI client SDK for Android  implementation("com.google.ai.client.generativeai:generativeai:0.6.0")}
    
    Java의 경우 라이브러리 두 개를 추가해야 합니다.
    
        dependencies {    // ... other androidx dependencies    // add the dependency for the Google AI client SDK for Android    implementation("com.google.ai.client.generativeai:generativeai:0.6.0")    // Required for one-shot operations (to use `ListenableFuture` from Guava Android)    implementation("com.google.guava:guava:31.0.1-android")    // Required for streaming operations (to use `Publisher` from Reactive Streams)    implementation("org.reactivestreams:reactive-streams:1.0.4")}
    
2.  Android 프로젝트를 Gradle 파일과 동기화합니다.
    

### 생성 모델 초기화

API를 호출하려면 먼저 생성 모델을 초기화해야 합니다.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

    val generativeModel = GenerativeModel(    // The Gemini 1.5 models are versatile and work with most use cases    modelName = "gemini-1.5-flash",    // Access your API key as a Build Configuration variable (see "Set up your API key" above)    apiKey = BuildConfig.apiKey)

자바의 경우 `GenerativeModelFutures` 객체도 초기화해야 합니다.

    // Use a model that's applicable for your use case// The Gemini 1.5 models are versatile and work with most use casesGenerativeModel gm = new GenerativeModel(/* modelName */ "gemini-1.5-flash",// Access your API key as a Build Configuration variable (see "Set up your API key" above)    /* apiKey */ BuildConfig.apiKey);// Use the GenerativeModelFutures Java compatibility layer which offers// support for ListenableFuture and Publisher APIsGenerativeModelFutures model = GenerativeModelFutures.from(gm);

모델을 지정할 때는 다음 사항에 유의하세요.

*   사용 사례에 맞는 모델을 사용하세요 (예: `gemini-pro-vision`은 멀티모달 입력용). 이 가이드 내에서 각 구현의 안내에는 사용 사례별 권장 모델이 나열되어 있습니다.
    
    **참고:** 기능 및 비율 제한을 포함하여 사용 가능한 모델에 대한 자세한 내용은 [Gemini 모델](https://ai.google.dev/models/gemini?hl=ko)을 참고하세요. Gemini Pro 모델의 비율 제한은 분당 요청 수 (RPM) 60회이며 [비율 한도 상향 요청](https://ai.google.dev/docs/increase_quota?hl=ko) 옵션을 제공합니다.
    

일반적인 사용 사례 구현
-------------

이제 프로젝트가 설정되었으므로 Gemini API를 사용하여 다양한 사용 사례를 구현할 수 있습니다.

*   [텍스트 전용 입력에서 텍스트 생성](#generate-text-from-text-input)
*   [텍스트 및 이미지 입력에서 텍스트 생성 (멀티모달)](#generate-text-from-text-and-image-input)
*   [멀티턴 대화 만들기 (채팅)](#multi-turn-conversations-chat)
*   [스트리밍을 통한 빠른 상호작용](#streaming)

### 텍스트 전용 입력에서 텍스트 생성

프롬프트 입력에 텍스트만 포함된 경우 `generateContent`와 함께 Gemini 1.5 모델 또는 Gemini 1.0 Pro 모델을 사용하여 텍스트 출력을 생성합니다.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

`generateContent()`는 정지 함수이며 코루틴 범위에서 호출되어야 합니다. 코루틴에 관해 잘 모른다면 [Android의 Kotlin 코루틴](https://developer.android.com/kotlin/coroutines?hl=ko)을 참고하세요.

    val generativeModel = GenerativeModel(    // The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts    modelName = "gemini-1.5-flash",    // Access your API key as a Build Configuration variable (see "Set up your API key" above)    apiKey = BuildConfig.apiKey)val prompt = "Write a story about a magic backpack."val response = generativeModel.generateContent(prompt)print(response.text)

`generateContent()`는 `ListenableFuture`를 반환합니다. 이 API에 익숙하지 않으면 [`ListenableFuture` 사용](https://developer.android.com/guide/background/asynchronous/listenablefuture?hl=ko)에 관한 Android 문서를 참고하세요.

    // The Gemini 1.5 models are versatile and work with both text-only and multimodal promptsGenerativeModel gm = new GenerativeModel(/* modelName */ "gemini-1.5-flash",// Access your API key as a Build Configuration variable (see "Set up your API key" above)    /* apiKey */ BuildConfig.apiKey);GenerativeModelFutures model = GenerativeModelFutures.from(gm);Content content = new Content.Builder()    .addText("Write a story about a magic backpack.")    .build();Executor executor = // ...ListenableFuture<GenerateContentResponse> response = model.generateContent(content);Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {    @Override    public void onSuccess(GenerateContentResponse result) {        String resultText = result.getText();        System.out.println(resultText);    }    @Override    public void onFailure(Throwable t) {        t.printStackTrace();    }}, executor);

**참고:** Gemini API는 스트리밍도 지원합니다. 자세한 내용은 [더 빠른 상호작용을 위한 스트리밍 사용](#streaming) (이 가이드의)을 참고하세요.

### 텍스트 및 이미지 입력에서 텍스트 생성 (멀티모달)

Gemini는 텍스트와 이미지를 모두 입력할 수 있도록 멀티모달 입력(Gemini 1.5 모델 및 Gemini 1.0 Pro Vision)을 처리할 수 있는 다양한 모델을 제공합니다. [프롬프트의 이미지 요구사항](https://ai.google.dev/docs/gemini_api_overview?hl=ko#image_requirements)을 검토하세요.

프롬프트 입력에 텍스트와 이미지가 모두 포함되어 있으면 Gemini 1.5 모델 또는 `generateContent`와 함께 Gemini 1.0 Pro Vision 모델을 사용하여 텍스트 출력을 생성합니다.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

`generateContent()`는 정지 함수이며 코루틴 범위에서 호출되어야 합니다. 코루틴에 관해 잘 모른다면 [Android의 Kotlin 코루틴](https://developer.android.com/kotlin/coroutines?hl=ko)을 참고하세요.

    val generativeModel = GenerativeModel(    // The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts    modelName = "gemini-1.5-flash",    // Access your API key as a Build Configuration variable (see "Set up your API key" above)    apiKey = BuildConfig.apiKey)val image1: Bitmap = // ...val image2: Bitmap = // ...val inputContent = content {    image(image1)    image(image2)    text("What's different between these pictures?")}val response = generativeModel.generateContent(inputContent)print(response.text)

`generateContent()`는 `ListenableFuture`를 반환합니다. 이 API에 익숙하지 않으면 [`ListenableFuture` 사용](https://developer.android.com/guide/background/asynchronous/listenablefuture?hl=ko)에 관한 Android 문서를 참고하세요.

    // The Gemini 1.5 models are versatile and work with both text-only and multimodal promptsGenerativeModel gm = new GenerativeModel(/* modelName */ "gemini-1.5-flash",// Access your API key as a Build Configuration variable (see "Set up your API key" above)    /* apiKey */ BuildConfig.apiKey);GenerativeModelFutures model = GenerativeModelFutures.from(gm);Bitmap image1 = // ...Bitmap image2 = // ...Content content = new Content.Builder()    .addText("What's different between these pictures?")    .addImage(image1)    .addImage(image2)    .build();Executor executor = // ...ListenableFuture<GenerateContentResponse> response = model.generateContent(content);Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {    @Override    public void onSuccess(GenerateContentResponse result) {        String resultText = result.getText();        System.out.println(resultText);    }    @Override    public void onFailure(Throwable t) {        t.printStackTrace();    }}, executor);

**참고:** Gemini API는 스트리밍도 지원합니다. 자세한 내용은 [더 빠른 상호작용을 위한 스트리밍 사용](#streaming) (이 가이드의)을 참고하세요.

### 멀티턴 대화 만들기 (채팅)

Gemini를 사용하면 여러 차례에 걸쳐 자유 형식으로 대화를 만들 수 있습니다. SDK는 대화 상태를 관리하여 프로세스를 간소화하므로 `generateContent`와 달리 대화 기록을 직접 저장할 필요가 없습니다.

멀티턴 대화 (예: 채팅)를 빌드하려면 Gemini 1.5 모델 또는 Gemini 1.0 Pro 모델을 사용하고 `startChat()`를 호출하여 채팅을 초기화합니다. 그런 다음 `sendMessage()`를 사용하여 새 사용자 메시지를 보내면 메시지와 응답도 채팅 기록에 추가됩니다.

대화의 콘텐츠와 연결된 `role`에는 두 가지 가능한 옵션이 있습니다.

*   `user`: 프롬프트를 제공하는 역할입니다. 이 값은 `sendMessage` 호출의 기본값입니다.
    
*   `model`: 응답을 제공하는 역할입니다. 이 역할은 기존 `history`로 `startChat()`를 호출할 때 사용할 수 있습니다.
    

**참고:** Gemini 1.0 Pro Vision 모델 (텍스트 및 이미지 입력용)은 아직 멀티턴 대화에 최적화되지 않았습니다. 대신 Gemini 1.5 모델 또는 Gemini 1.0 Pro 모델을 사용하세요.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

`generateContent()`는 정지 함수이며 코루틴 범위에서 호출되어야 합니다. 코루틴에 관해 잘 모른다면 [Android의 Kotlin 코루틴](https://developer.android.com/kotlin/coroutines?hl=ko)을 참고하세요.

    val generativeModel = GenerativeModel(    // The Gemini 1.5 models are versatile and work with multi-turn conversations (like chat)    modelName = "gemini-1.5-flash",    // Access your API key as a Build Configuration variable (see "Set up your API key" above)    apiKey = BuildConfig.apiKey)val chat = generativeModel.startChat(    history = listOf(        content(role = "user") { text("Hello, I have 2 dogs in my house.") },        content(role = "model") { text("Great to meet you. What would you like to know?") }    ))chat.sendMessage("How many paws are in my house?")

`generateContent()`는 `ListenableFuture`를 반환합니다. 이 API에 익숙하지 않으면 [`ListenableFuture` 사용](https://developer.android.com/guide/background/asynchronous/listenablefuture?hl=ko)에 관한 Android 문서를 참고하세요.

    // The Gemini 1.5 models are versatile and work with multi-turn conversations (like chat)GenerativeModel gm = new GenerativeModel(/* modelName */ "gemini-1.5-flash",// Access your API key as a Build Configuration variable (see "Set up your API key" above)    /* apiKey */ BuildConfig.apiKey);GenerativeModelFutures model = GenerativeModelFutures.from(gm);// (optional) Create previous chat history for contextContent.Builder userContentBuilder = new Content.Builder();userContentBuilder.setRole("user");userContentBuilder.addText("Hello, I have 2 dogs in my house.");Content userContent = userContentBuilder.build();Content.Builder modelContentBuilder = new Content.Builder();modelContentBuilder.setRole("model");modelContentBuilder.addText("Great to meet you. What would you like to know?");Content modelContent = userContentBuilder.build();List<Content> history = Arrays.asList(userContent, modelContent);// Initialize the chatChatFutures chat = model.startChat(history);// Create a new user messageContent userMessage = new Content.Builder()    .setRole("user")    .addText("How many paws are in my house?")    .build();Executor executor = // ...// Send the messageListenableFuture<GenerateContentResponse> response = chat.sendMessage(userMessage);Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {    @Override    public void onSuccess(GenerateContentResponse result) {        String resultText = result.getText();        System.out.println(resultText);    }    @Override    public void onFailure(Throwable t) {        t.printStackTrace();    }}, executor);

**참고:** Gemini API는 스트리밍도 지원합니다. 자세한 내용은 [더 빠른 상호작용을 위한 스트리밍 사용](#streaming) (이 가이드의)을 참고하세요.

### 스트리밍으로 더 빠른 상호작용

기본적으로 모델은 전체 생성 프로세스를 완료한 후 응답을 반환합니다. 전체 결과를 기다리지 않고 스트리밍을 사용하여 부분 결과를 처리하면 상호작용을 더 빠르게 달성할 수 있습니다.

다음 예는 텍스트 및 이미지 입력 프롬프트에서 텍스트를 생성하기 위해 `generateContentStream`로 스트리밍을 구현하는 방법을 보여줍니다.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

`generateContentStream()`는 정지 함수이며 코루틴 범위에서 호출되어야 합니다. 코루틴에 관해 잘 모른다면 [Android의 Kotlin 코루틴](https://developer.android.com/kotlin/coroutines?hl=ko)을 참고하세요.

    val generativeModel = GenerativeModel(    // The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts    modelName = "gemini-1.5-flash",    // Access your API key as a Build Configuration variable (see "Set up your API key" above)    apiKey = BuildConfig.apiKey)val image1: Bitmap = // ...val image2: Bitmap = // ...val inputContent = content {    image(image1)    image(image2)    text("What's the difference between these pictures?")}var fullResponse = ""generativeModel.generateContentStream(inputContent).collect { chunk ->    print(chunk.text)    fullResponse += chunk.text}

이 SDK의 자바 스트리밍 메서드는 [Reactive Streams](https://www.reactive-streams.org/) 라이브러리에서 `Publisher` 유형을 반환합니다.

    // The Gemini 1.5 models are versatile and work with both text-only and multimodal promptsGenerativeModel gm = new GenerativeModel(/* modelName */ "gemini-1.5-flash",// Access your API key as a Build Configuration variable (see "Set up your API key" above)    /* apiKey */ BuildConfig.apiKey);GenerativeModelFutures model = GenerativeModelFutures.from(gm);Bitmap image1 = // ...Bitmap image2 = // ...Content content = new Content.Builder()    .addText("What's different between these pictures?")    .addImage(image1)    .addImage(image2)    .build();Publisher<GenerateContentResponse> streamingResponse =    model.generateContentStream(content);final String[] fullResponse = {""};streamingResponse.subscribe(new Subscriber<GenerateContentResponse>() {    @Override    public void onNext(GenerateContentResponse generateContentResponse) {        String chunk = generateContentResponse.getText();        fullResponse[0] += chunk;    }    @Override    public void onComplete() {        System.out.println(fullResponse[0]);    }    @Override    public void onError(Throwable t) {        t.printStackTrace();    }    @Override    public void onSubscribe(Subscription s) { }});

텍스트 전용 입력 및 채팅 사용 사례에도 비슷한 접근 방식을 사용할 수 있습니다.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

`generateContentStream()`는 정지 함수이며 코루틴 범위에서 호출되어야 합니다. 코루틴에 관해 잘 모른다면 [Android의 Kotlin 코루틴](https://developer.android.com/kotlin/coroutines?hl=ko)을 참고하세요.

    // Use streaming with text-only inputgenerativeModel.generateContentStream(inputContent).collect { chunk ->    print(chunk.text)}

    // Use streaming with multi-turn conversations (like chat)val chat = generativeModel.startChat()chat.sendMessageStream(inputContent).collect { chunk ->    print(chunk.text)}

이 SDK의 자바 스트리밍 메서드는 [Reactive Streams](https://www.reactive-streams.org/) 라이브러리에서 `Publisher` 유형을 반환합니다.

    // Use streaming with text-only inputPublisher<GenerateContentResponse> streamingResponse =    model.generateContentStream(inputContent);final String[] fullResponse = {""};streamingResponse.subscribe(new Subscriber<GenerateContentResponse>() {    @Override    public void onNext(GenerateContentResponse generateContentResponse) {        String chunk = generateContentResponse.getText();        fullResponse[0] += chunk;    }    @Override    public void onComplete() {        System.out.println(fullResponse[0]);    }    // ... other methods omitted for brevity});

    // Use streaming with multi-turn conversations (like chat)ChatFutures chat = model.startChat(history);Publisher<GenerateContentResponse> streamingResponse =    chat.sendMessageStream(inputContent);final String[] fullResponse = {""};streamingResponse.subscribe(new Subscriber<GenerateContentResponse>() {    @Override    public void onNext(GenerateContentResponse generateContentResponse) {        String chunk = generateContentResponse.getText();        fullResponse[0] += chunk;    }    @Override    public void onComplete() {        System.out.println(fullResponse[0]);    }    // ... other methods omitted for brevity});

고급 사용 사례 구현
-----------

이 튜토리얼의 이전 섹션에 설명된 일반적인 사용 사례를 참고하면 Gemini API 사용에 익숙해질 수 있습니다. 이 섹션에서는 더 고급화된 것으로 간주될 수 있는 몇 가지 사용 사례를 설명합니다.

### 함수 호출

함수 호출을 사용하면 생성 모델에서 구조화된 데이터 출력을 더 쉽게 얻을 수 있습니다. 그런 다음 이러한 출력을 사용하여 다른 API를 호출하고 관련 응답 데이터를 모델에 반환할 수 있습니다. 즉, 함수 호출은 생성된 콘텐츠에 가장 정확한 최신 정보가 포함되도록 생성 모델을 외부 시스템에 연결하는 데 도움이 됩니다. 자세한 내용은 [함수 호출 튜토리얼](https://ai.google.dev/gemini-api/docs/function-calling/android?hl=ko)을 참조하세요.

### 토큰 개수

긴 프롬프트를 사용할 때는 모델에 콘텐츠를 보내기 전에 토큰을 세는 것이 유용할 수 있습니다. 다음 예는 다양한 사용 사례에 `countTokens()`를 사용하는 방법을 보여줍니다.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

`countTokens()`는 정지 함수이며 코루틴 범위에서 호출되어야 합니다. 코루틴에 관해 잘 모른다면 [Android의 Kotlin 코루틴](https://developer.android.com/kotlin/coroutines?hl=ko)을 참고하세요.

    // For text-only inputval (totalTokens) = generativeModel.countTokens("Write a story about a magic backpack.")// For text-and-image input (multi-modal)val multiModalContent = content {    image(image1)    image(image2)    text("What's the difference between these pictures?")}val (totalTokens) = generativeModel.countTokens(multiModalContent)// For multi-turn conversations (like chat)val history = chat.historyval messageContent = content { text("This is the message I intend to send")}val (totalTokens) = generativeModel.countTokens(*history.toTypedArray(), messageContent)

`countTokens()`는 `ListenableFuture`를 반환합니다. 이 API에 익숙하지 않으면 [`ListenableFuture` 사용](https://developer.android.com/guide/background/asynchronous/listenablefuture?hl=ko)에 관한 Android 문서를 참고하세요.

    Content text = new Content.Builder()    .addText("Write a story about a magic backpack.")    .build();Executor executor = // ...// For text-only inputListenableFuture<CountTokensResponse> countTokensResponse = model.countTokens(text);Futures.addCallback(countTokensResponse, new FutureCallback<CountTokensResponse>() {    @Override    public void onSuccess(CountTokensResponse result) {        int totalTokens = result.getTotalTokens();        System.out.println("TotalTokens = " + totalTokens);    }    @Override    public void onFailure(Throwable t) {        t.printStackTrace();    }}, executor);// For text-and-image inputBitmap image1 = // ...Bitmap image2 = // ...Content multiModalContent = new Content.Builder()    .addImage(image1)    .addImage(image2)    .addText("What's different between these pictures?")    .build();ListenableFuture<CountTokensResponse> countTokensResponse = model.countTokens(multiModalContent);// For multi-turn conversations (like chat)List<Content> history = chat.getChat().getHistory();Content messageContent = new Content.Builder()    .addText("This is the message I intend to send")    .build();Collections.addAll(history, messageContent);ListenableFuture<CountTokensResponse> countTokensResponse = model.countTokens(history.toArray(new Content[0]));

콘텐츠 생성을 제어하는 옵션
---------------

모델 매개변수를 구성하고 안전 설정을 사용하여 콘텐츠 생성을 제어할 수 있습니다.

### 모델 매개변수 구성

모델에 전송하는 모든 프롬프트에는 모델의 응답 생성 방식을 제어하는 매개변수 값이 포함됩니다. 모델은 서로 다른 매개변수 값에 대해 서로 다른 결과를 생성할 수 있습니다. [모델 매개변수](https://ai.google.dev/docs/concepts?hl=ko#model_parameters)에 대해 자세히 알아보세요.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

    val config = generationConfig {    temperature = 0.9f    topK = 16    topP = 0.1f    maxOutputTokens = 200    stopSequences = listOf("red")}val generativeModel = GenerativeModel(    // The Gemini 1.5 models are versatile and work with most use cases    modelName = "gemini-1.5-flash",    apiKey = BuildConfig.apiKey,    generationConfig = config)

    GenerationConfig.Builder configBuilder = new GenerationConfig.Builder();configBuilder.temperature = 0.9f;configBuilder.topK = 16;configBuilder.topP = 0.1f;configBuilder.maxOutputTokens = 200;configBuilder.stopSequences = Arrays.asList("red");GenerationConfig generationConfig = configBuilder.build();// The Gemini 1.5 models are versatile and work with most use casesGenerativeModel gm = new GenerativeModel(    "gemini-1.5-flash",    BuildConfig.apiKey,    generationConfig);GenerativeModelFutures model = GenerativeModelFutures.from(gm);

### 안전 설정 사용

안전 설정을 사용하여 유해한 것으로 간주될 수 있는 응답을 받을 가능성을 조정할 수 있습니다. 기본적으로 안전 설정은 모든 측정기준에서 보통 또는 높은 가능성이 있는 콘텐츠를 차단합니다. [안전 설정](https://ai.google.dev/docs/safety_setting?hl=ko)에 관해 자세히 알아보세요.

하나의 안전 설정을 지정하는 방법은 다음과 같습니다.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

    val generativeModel = GenerativeModel(    // The Gemini 1.5 models are versatile and work with most use cases    modelName = "gemini-1.5-flash",    apiKey = BuildConfig.apiKey,    safetySettings = listOf(        SafetySetting(HarmCategory.HARASSMENT, BlockThreshold.ONLY_HIGH)    ))

    SafetySetting harassmentSafety = new SafetySetting(HarmCategory.HARASSMENT,    BlockThreshold.ONLY_HIGH);// The Gemini 1.5 models are versatile and work with most use casesGenerativeModel gm = new GenerativeModel(    "gemini-1.5-flash",    BuildConfig.apiKey,    null, // generation config is optional    Collections.singletonList(harassmentSafety));GenerativeModelFutures model = GenerativeModelFutures.from(gm);

다음과 같이 두 개 이상의 안전 설정을 지정할 수도 있습니다.

[Kotlin](#kotlin) [Java](#java) [더보기](#)

    val harassmentSafety = SafetySetting(HarmCategory.HARASSMENT, BlockThreshold.ONLY_HIGH)val hateSpeechSafety = SafetySetting(HarmCategory.HATE_SPEECH, BlockThreshold.MEDIUM_AND_ABOVE)val generativeModel = GenerativeModel(    // The Gemini 1.5 models are versatile and work with most use cases    modelName = "gemini-1.5-flash",    apiKey = BuildConfig.apiKey,    safetySettings = listOf(harassmentSafety, hateSpeechSafety))

    SafetySetting harassmentSafety = new SafetySetting(HarmCategory.HARASSMENT,    BlockThreshold.ONLY_HIGH);SafetySetting hateSpeechSafety = new SafetySetting(HarmCategory.HATE_SPEECH,    BlockThreshold.MEDIUM_AND_ABOVE);// The Gemini 1.5 models are versatile and work with most use casesGenerativeModel gm = new GenerativeModel(    "gemini-1.5-flash",    BuildConfig.apiKey,    null, // generation config is optional    Arrays.asList(harassmentSafety, hateSpeechSafety));GenerativeModelFutures model = GenerativeModelFutures.from(gm);

다음 단계
-----

*   _프롬프트 설계_는 언어 모델에서 원하는 응답을 유도하는 프롬프트를 만드는 프로세스입니다. 체계적인 메시지 작성은 언어 모델의 정확하고 고품질 응답을 보장하는 필수 부분입니다. [프롬프트 작성 권장사항](https://ai.google.dev/docs/prompt_best_practices?hl=ko)에 대해 알아보기
    
*   Gemini는 입력 유형 및 복잡성, 채팅 또는 기타 대화상자 언어 작업의 구현, 크기 제약 조건과 같은 다양한 사용 사례의 요구사항을 충족하기 위해 여러 모델 변형을 제공합니다. [사용 가능한 Gemini 모델](https://ai.google.dev/models/gemini?hl=ko)을 알아보세요.
    
*   Gemini는 [비율 한도 증가를 요청](https://ai.google.dev/docs/increase_quota?hl=ko)하는 옵션을 제공합니다. Gemini Pro 모델의 비율 한도는 분당 요청 수 (RPM) 60개입니다.
    
*   이 가이드에서 설명하는 Android용 클라이언트 SDK를 사용하면 _Google 서버에서 실행_되는 Gemini Pro 모델에 액세스할 수 있습니다. 민감한 정보 처리, 오프라인 가용성이 필요한 사용 사례 또는 자주 사용하는 사용자 흐름의 비용 절감을 위해 _기기에서 실행_되는 Gemini Nano 액세스를 고려할 수 있습니다. 자세한 내용은 [Android (기기 내) 튜토리얼](https://ai.google.dev/tutorials/android_aicore?hl=ko)을 참고하세요.
    

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-06-06(UTC)
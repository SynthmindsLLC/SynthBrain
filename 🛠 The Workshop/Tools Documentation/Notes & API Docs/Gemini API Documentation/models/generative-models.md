*   이 페이지의 내용
*   [예시 애플리케이션](#example-applications)
    *   [시 생성](#generate-poem)
    *   [목록 생성](#generate-list)
*   [프롬프트 설계의 기초](#prompt101)
    *   [프롬프트와 기존 소프트웨어 개발 비교](#prompting-versus)
*   [모델 매개변수](#model-parameters)
*   [메시지 유형](#prompt-types)
    *   [제로샷 프롬프트](#zero-shot-prompts)
    *   [원샷 프롬프트](#one-shot-prompts)
    *   [퓨샷 프롬프트](#few-shot-prompts)
*   [생성 모델 자세히 살펴보기](#under-the-hood)
*   [추가 자료](#further-reading)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

생성 모델 정보
========

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [예시 애플리케이션](#example-applications)
    *   [시 생성](#generate-poem)
    *   [목록 생성](#generate-list)
*   [프롬프트 설계의 기초](#prompt101)
    *   [프롬프트와 기존 소프트웨어 개발 비교](#prompting-versus)
*   [모델 매개변수](#model-parameters)
*   [메시지 유형](#prompt-types)
    *   [제로샷 프롬프트](#zero-shot-prompts)
    *   [원샷 프롬프트](#one-shot-prompts)
    *   [퓨샷 프롬프트](#few-shot-prompts)
*   [생성 모델 자세히 살펴보기](#under-the-hood)
*   [추가 자료](#further-reading)

Gemini 모델 제품군과 같은 생성형 인공지능 (AI) 모델은 텍스트, 이미지, 오디오 등 다양한 유형의 데이터 입력으로 콘텐츠를 만들 수 있습니다. 이러한 모델은 가장 기본적인 수준에서 정교한 자동 완성 애플리케이션처럼 작동합니다. 입력 텍스트 ('말을 물가게 할 수 있음')가 주어지면 생성 모델은 학습 데이터에서 학습한 패턴을 기반으로 통계적으로 따를 가능성이 있는 출력 텍스트 ('하지만 마실 수는 없음')를 예측할 수 있습니다. 생성 모델의 이러한 기본 속성을 다양한 애플리케이션에 사용할 수 있습니다.

*   시, 단편 소설, 은유, 블로그 게시물과 같은 창의적인 글쓰기
*   구조화된 데이터를 자유 형식 텍스트로 변환
*   자유 형식 텍스트에서 정보 추출 및 요약
*   코드 생성
*   언어 간 번역

생성 모델을 사용하여 이러한 특성을 빌드하는 데는 머신러닝 (ML) 전문 지식이 필요하지 않습니다. 대규모 데이터 세트를 수집하거나 모델을 학습시킬 필요가 없습니다. 첫 번째 프로토타입을 시작하기 위해서는 모델이 수행할 작업을 몇 문장으로 설명하기만 하면 됩니다.

텍스트 입력과 출력만 처리하는 생성 모델을 _대규모 언어 모델_ (LLM)이라고도 합니다. Gemini 제품군은 텍스트 데이터보다 더 많은 기능을 처리할 수 있으며 LLM의 기능을 수행할 수 있지만 _생성 모델_이라고 더 잘 알려져 있습니다.

예시 애플리케이션
---------

다음 예는 생성 모델에 대한 일반적인 텍스트 입력과 생성 모델에서의 출력을 보여줍니다.

### 시 생성

사용자 입력: `Write me a four-line poem about puppies and Android phones. Make sure it rhymes.`

모델 출력:

Puppies are cute,
    Android phones are neat,
    They both bring joy,
    And make life complete.

### 목록 생성

사용자 입력: `Generate a bulleted list of items I need to pack for a three-day camping trip.`

모델 출력:

*   Tent
    *   Sleeping bag
    *   Sleeping pad
    *   Camp stove
    *   Pots and pans
    *   Utensils
    *   Food
    *   Water
    *   First-aid kit
    *   Sunscreen
    *   Insect repellent
    *   ...

적절한 입력 텍스트를 작성하기만 하면 **프롬프트**라고도 하는 이와 같은 온갖 종류의 유용한 동작을 생성할 수 있는 생성 모델을 만들 수 있습니다. 생성 모델이 원하는 작업을 수행하도록 올바른 문구를 찾는 기술을 **프롬프트 설계**('프롬프트 엔지니어링' 또는 간단히 '프롬프팅'이라고도 함)라고 합니다.

프롬프트 설계의 기초
-----------

이전 섹션에서는 '시를 써 줘'와 같이 안내가 포함된 프롬프트의 예를 알아보았습니다. 이러한 종류의 지침은 특정 유형의 작업에 적합할 수 있습니다. 하지만 다른 애플리케이션에서는 **퓨샷 프롬프팅**이라는 다른 프롬프팅 기술이 더 효과적일 수 있습니다. 퓨샷 프롬프트는 대규모 언어 모델이 텍스트 데이터의 패턴을 놀라울 정도로 인식하고 복제할 수 있다는 사실을 활용합니다. 학습한 텍스트 패턴을 생성 모델에 전송하여 완성하도록 하는 것입니다. 예를 들어 국가 이름을 입력으로 받아 주도를 출력하는 애플리케이션을 빌드한다고 가정해 보겠습니다. 다음은 이를 위한 텍스트 프롬프트입니다.

Italy : Rome
    France : Paris
    Germany :

이 프롬프트에서는 `[country] : [capital]` 패턴을 설정합니다. 이 프롬프트를 대규모 언어 모델에 보내면 패턴이 자동 완성되고 다음과 같은 결과가 반환됩니다.

     Berlin
    Turkey : Ankara
    Greece : Athens

이 모델의 응답은 약간 이상하게 보일 수 있습니다. 이 모델은 직접 작성한 프롬프트의 마지막 국가인 독일의 대문자뿐 아니라 추가적인 국가와 수도 쌍의 전체 목록도 반환했습니다. 그 이유는 생성 모델이 '패턴을 연속적으로 유지'하고 있기 때문입니다. 입력 국가의 수도 ('독일 : 베를린')를 알려주는 함수를 빌드하기만 하면 '베를린' 다음에 모델이 생성하는 텍스트에는 별로 관심이 없을 것입니다. 실제로 애플리케이션 디자이너는 이러한 관련 없는 예를 잘라야 할 수 있습니다. 또한 독일이 고정 문자열이 아니라 최종 사용자가 제공하는 변수가 되도록 입력을 **매개변수화**할 수 있습니다.

Italy : Rome
    France : Paris
    <user input here> :

방금 국가 수도를 만들기 위한 몇 샷 프롬프트를 작성했습니다.

이 **퓨샷 프롬프트** 템플릿을 따르면 많은 태스크를 수행할 수 있습니다. 다음은 Python을 자바스크립트로 변환하는 약간 다른 형식의 몇 가지 프롬프트입니다.

Convert Python to JavaScript.
    Python: print("hello world")
    JavaScript: console.log("hello world")
    Python: for x in range(0, 100):
    JavaScript: for(var i = 0; i < 100; i++) {
    Python: ${USER INPUT HERE}
    JavaScript:

또는 이 '역사전' 프롬프트를 사용합니다. 정의가 주어지면 해당 정의에 맞는 단어가 반환됩니다.

Given a definition, return the word it defines.
    Definition: When you're happy that other people are also sad.
    Word: schadenfreude
    Definition: existing purely in the mind, but not in physical reality
    Word: abstract
    Definition: ${USER INPUT HERE}
    Word:

이러한 퓨샷 프롬프트의 정확한 패턴이 약간씩 다릅니다. 예시가 포함된 것 외에도 프롬프트에 지침을 제공하는 것은 프롬프트를 직접 작성할 때 고려할 추가 전략입니다. 모델에 인텐트를 전달하는 데 도움이 되기 때문입니다.

### 프롬프트와 기존 소프트웨어 개발 비교

신중하게 작성된 사양에 맞게 설계된 기존 소프트웨어와 달리 생성 모델의 동작은 모델 트레이너에게도 대체로 불투명합니다. 따라서 특정 모델에 어떤 유형의 프롬프트 구조가 가장 적합한지 미리 예측할 수 없는 경우가 많습니다. 게다가 생성 모델의 동작은 대체로 학습 데이터에 의해 결정되며, 모델이 새로운 데이터 세트에 맞춰 지속적으로 조정되므로 모델이 의도치 않게 변경되어 프롬프트 구조가 가장 효과적인 경우가 종종 있습니다. 크리에이터에게 미치는 영향 실험해 보세요. 다양한 프롬프트 형식을 사용해 보세요.

모델 매개변수
-------

모델에 전송하는 모든 프롬프트에는 모델의 응답 생성 방식을 제어하는 매개변수 값이 포함됩니다. 모델은 서로 다른 매개변수 값에 대해 서로 다른 결과를 생성할 수 있습니다. 가장 일반적인 모델 매개변수는 다음과 같습니다.

1.  **Max output token(최대 출력 토큰):** 응답에서 생성할 수 있는 최대 토큰 수를 지정합니다. 토큰 1개는 약 4자(영문 기준)입니다. 토큰 100개는 약 60~80개 단어에 해당합니다.
    
2.  **강도:** 강도는 토큰 선택의 무작위성 수준을 제어합니다. 온도는 `topP` 및 `topK`가 적용될 때 발생하는 응답 생성 중 샘플링에 사용됩니다. 강도가 낮을수록 보다 확정적이거나 덜 개방적인 응답이 필요한 프롬프트에 적합한 반면, 강도가 높을수록 보다 다양하거나 창의적인 결과로 이어질 수 있습니다. 온도가 0이면 확정적입니다. 즉, 확률이 가장 높은 응답이 항상 선택됩니다.
    
3.  **`topK`:** `topK` 매개변수는 모델이 출력용 토큰을 선택하는 방식을 변경합니다. `topK`이 1이면 선택된 토큰이 모델의 어휘에 포함된 모든 토큰 중에서 가장 확률이 높다는 의미입니다 (그리디 디코딩이라고도 함). 반면 `topK`가 3이면 강도를 사용하여 가장 가능성이 높은 토큰 세 개 중에서 다음 토큰이 선택된다는 의미입니다. 각 토큰 선택 단계에서 확률이 가장 높은 `topK` 토큰이 샘플링됩니다. 그런 다음 토큰은 `topP`을 기준으로 추가로 필터링되고 최종 토큰은 온도 샘플링을 사용하여 선택됩니다.
    
4.  **`topP`:** `topP` 매개변수는 모델이 출력용 토큰을 선택하는 방식을 변경합니다. 토큰의 확률 합계가 `topP` 값과 같아질 때까지 확률이 가장 높은 순에서 낮은 순으로 토큰이 선택됩니다. 예를 들어 토큰 A, B, C의 확률이 0.3, 0.2, 0.1이고 `topP` 값이 0.5이면 모델이 온도를 사용하여 다음 토큰으로 A 또는 B를 선택하고 C를 후보로 제외합니다. 기본 `topP` 값은 0.95입니다.
    
5.  **`stop_sequences`:** 콘텐츠 생성을 중지하도록 모델에 지시하는 중지 시퀀스를 설정합니다. 중지 시퀀스는 임의의 문자 시퀀스일 수 있습니다. 생성된 콘텐츠에 나타날 수 있는 문자 시퀀스를 사용하지 마세요.
    

메시지 유형
------

메시지에 포함된 문맥 정보의 수준에 따라 프롬프트는 크게 세 가지 유형으로 분류됩니다.

### 제로샷 프롬프트

이러한 프롬프트에는 복제할 모델의 예시가 포함되어 있지 않습니다. 제로샷 프롬프트는 기본적으로 모델이 추가 예시나 정보 없이 프롬프트를 완료할 수 있는 능력을 보여줍니다. 모델이 그럴듯한 답변을 생성하려면 기존 지식을 사용해야 한다는 의미입니다.

일반적으로 사용되는 제로샷 프롬프트 패턴은 다음과 같습니다.

*   안내 콘텐츠

<Overall instruction>
    <Content to operate on>

예를 들면 다음과 같습니다.

Summarize the following into two sentences at the third-grade level:
    
    Hummingbirds are the smallest birds in the world, and they are also one of the
    most fascinating. They are found in North and South America, and they are known
    for their long, thin beaks and their ability to fly at high speeds.
    
    Hummingbirds are made up of three main parts: the head, the body, and the tail.
    The head is small and round, and it contains the eyes, the beak, and the brain.
    The body is long and slender, and it contains the wings, the legs, and the
    heart. The tail is long and forked, and it helps the hummingbird to balance
    while it is flying.
    
    Hummingbirds are also known for their coloration. They come in a variety of
    colors, including green, blue, red, and purple. Some hummingbirds are even able
    to change their color!
    
    Hummingbirds are very active creatures. They spend most of their time flying,
    and they are also very good at hovering. Hummingbirds need to eat a lot of food
    in order to maintain their energy, and they often visit flowers to drink nectar.
    
    Hummingbirds are amazing creatures. They are small, but they are also very
    powerful. They are beautiful, and they are very important to the ecosystem.

*   안내-콘텐츠-안내

<Overall instruction or context setting>
    <Content to operate on>
    <Final instruction>

예를 들면 다음과 같습니다.

Here is some text I'd like you to summarize:
    
    Hummingbirds are the smallest birds in the world, and they are also one of the
    most fascinating. They are found in North and South America, and they are known
    for their long, thin beaks and their ability to fly at high speeds. Hummingbirds
    are made up of three main parts: the head, the body, and the tail. The head is
    small and round, and it contains the eyes, the beak, and the brain. The body is
    long and slender, and it contains the wings, the legs, and the heart. The tail
    is long and forked, and it helps the hummingbird to balance while it is flying.
    Hummingbirds are also known for their coloration. They come in a variety of
    colors, including green, blue, red, and purple. Some hummingbirds are even able
    to change their color! Hummingbirds are very active creatures. They spend most
    of their time flying, and they are also very good at hovering. Hummingbirds need
    to eat a lot of food in order to maintain their energy, and they often visit
    flowers to drink nectar. Hummingbirds are amazing creatures. They are small, but
    they are also very powerful. They are beautiful, and they are very important to
    the ecosystem.
    
    Summarize it in two sentences at the third-grade reading level.

*   계속. 모델이 아무런 안내 없이 텍스트를 계속 실행하도록 할 수도 있습니다. 예를 들어 다음은 모델이 제공된 입력을 계속 사용하도록 하는 제로샷 프롬프트입니다.

Once upon a time, there was a little sparrow building a nest in a farmer's
    barn. This sparrow

제로샷 프롬프트를 사용하여 시, 코드, 스크립트, 음악 작품, 이메일, 편지 등의 광고 소재 텍스트 형식을 생성합니다.

### 원샷 프롬프트

이 프롬프트는 모델에 패턴을 하나 더 복제하고 계속하기 위한 예시를 제공합니다. 이렇게 하면 모델에서 예측 가능한 응답을 생성할 수 있습니다.

예를 들어 다음과 같은 음식 페어링을 생성할 수 있습니다.

Food: Apple
    Pairs with: Cheese
    Food: Pear
    Pairs with:

### 퓨샷 프롬프트

이러한 프롬프트는 모델에 복제할 여러 예시를 제공합니다. 퓨샷 프롬프트를 사용하여 패턴을 기반으로 데이터를 합성하는 것과 같은 복잡한 작업을 완료합니다.

프롬프트의 예는 다음과 같습니다.

Generate a grocery shopping list for a week for one person. Use the JSON format
    given below.
    {"item": "eggs", "quantity": "6"}
    {"item": "bread", "quantity": "one loaf"}

생성 모델 자세히 살펴보기
--------------

이 섹션에서는 **_생성 모델의 응답에 임의성이 있나요? 아니면 확정적인가요?_**라는 질문에 답하는 것을 목표로 합니다.

간단히 말씀드리자면, 두 경우 모두에 '예'입니다. 생성 모델을 프롬프트하면 텍스트 응답이 2단계로 생성됩니다. 첫 번째 단계에서는 생성 모델이 입력 프롬프트를 처리하고 다음에 올 가능성이 높은 토큰 (단어)에 대해 **확률 분포**를 생성합니다. 예를 들어 입력 텍스트 'The dog인이 모델을 뛰어넘었습니다'가 포함된 프롬프트를 입력하면 생성 모델은 다음에 나올 가능성이 큰 단어의 배열을 생성합니다.

[("fence", 0.77), ("ledge", 0.12), ("blanket", 0.03), ...]

이 프로세스는 확정적입니다. 생성 모델은 동일한 프롬프트 텍스트를 입력할 때마다 동일한 분포를 생성합니다.

두 번째 단계에서 생성 모델은 여러 디코딩 전략 중 하나를 통해 이러한 분포를 실제 텍스트 응답으로 변환합니다. 간단한 디코딩 전략으로는 모든 시간 단계마다 가능성이 가장 높은 토큰을 선택할 수 있습니다. 이 프로세스는 항상 확정적입니다. 하지만 모델이 반환한 분포를 _무작위 샘플링_하여 응답을 생성할 수도 있습니다. 이 프로세스는 확률적 (무작위)입니다. 온도를 설정하여 이 디코딩 프로세스에서 허용되는 무작위성의 수준을 제어합니다. 온도가 0이면 가장 가능성이 높은 토큰만 선택되며 임의성이 없습니다. 반대로, 고온은 모델이 선택한 토큰에 높은 수준의 무작위성을 주입하므로, 더 예상치 못한 놀라운 모델 응답이 생성됩니다.

추가 자료
-----

*   프롬프트와 생성 모델에 대해 자세히 알아보았으니 이제 [Google AI 스튜디오](https://aistudio.google.com?hl=ko)를 사용하여 나만의 프롬프트를 작성해 보세요.
*   프롬프트 만들기 권장사항에 대한 자세한 내용은 [프롬프트 가이드라인](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ko)을 참조하세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-04-18(UTC)
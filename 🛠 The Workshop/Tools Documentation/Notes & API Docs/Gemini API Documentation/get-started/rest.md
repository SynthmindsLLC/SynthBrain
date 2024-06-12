---
Please provide me with more context! I need to know what the mission is for. 

For example, tell me: "* **What is the mission for?** (A company, a project, a personal goal, etc.)"
* **What are the goals of the mission?**
* **What are the key values or principles behind the mission?**

Once you give me more information, I can help you craft a compelling mission statement.
---

*   이 페이지의 내용
*   [API 키 설정](#set_up_your_api_key_3)
*   [Gemini 및 Content 기반 API](#gemini_and_content_based_apis)
    *   [텍스트 전용 입력](#text-only_input)
    *   [텍스트 및 이미지 입력](#text-and-image_input)
    *   [멀티턴 대화 (채팅)](#multi-turn_conversations_chat)
    *   [구성](#configuration)
    *   [스트림 생성 콘텐츠](#stream_generate_content)
    *   [토큰 개수](#count_tokens_4)
    *   [임베딩](#embedding)
*   [모델 정보](#model_info)
    *   [모델 가져오기](#get_model)
    *   [모델 나열](#list_models_2)

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
*   [API 키 설정](#set_up_your_api_key_3)
*   [Gemini 및 Content 기반 API](#gemini_and_content_based_apis)
    *   [텍스트 전용 입력](#text-only_input)
    *   [텍스트 및 이미지 입력](#text-and-image_input)
    *   [멀티턴 대화 (채팅)](#multi-turn_conversations_chat)
    *   [구성](#configuration)
    *   [스트림 생성 콘텐츠](#stream_generate_content)
    *   [토큰 개수](#count_tokens_4)
    *   [임베딩](#embedding)
*   [모델 정보](#model_info)
    *   [모델 가져오기](#get_model)
    *   [모델 나열](#list_models_2)

Python Node.js 웹 REST Go Dart (Flutter) Android Swift

  

<table align="left" class="tfo-notebook-buttons"><tbody><tr><td><a href="https://ai.google.dev/gemini-api/docs/get-started/rest?hl=ko" target="_blank"><img height="32" src="https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png?hl=ko" width="32">ai.google.dev에서 보기</a></td><td><a href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/rest.ipynb?hl=ko" target="_blank"><img src="https://www.tensorflow.org/images/colab_logo_32px.png?hl=ko">Google Colab에서 실행</a></td><td><a href="https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/rest.ipynb" target="_blank"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=ko">GitHub에서 소스 보기</a></td></tr></tbody></table>

Gemini API를 빠르게 사용해 보려면 `curl` 명령어를 사용하여 REST API에서 메서드를 호출하면 됩니다. 이 튜토리얼의 예에서는 각 API 메서드의 호출을 보여줍니다.

[Colab](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/tutorials/rest_quickstart.ipynb?hl=ko)은 Python 코드를 사용하여 환경 변수를 설정하고 이미지를 표시하지만 Colab에서 REST API를 사용할 필요는 없습니다. 다음 섹션에 설명된 대로 `API_KEY`가 설정되어 있으면 Colab 외부에서 모든 `curl` 예를 수정 없이 실행할 수 있습니다.

각 `curl` 명령어에 관련 모델 이름과 API 키를 지정해야 합니다.

### API 키 설정

Gemini API를 사용하려면 API 키가 필요합니다. 아직 키가 없으면 Google AI Studio에서 키를 만듭니다.

[API 키 가져오기](https://makersuite.google.com/app/apikey?hl=ko)

Colab에서 왼쪽 패널의 'boot' 아래에 있는 보안 비밀 관리자에 키를 추가합니다. 이름을 `GOOGLE_API_KEY`로 지정합니다. 그런 다음 환경 변수로 추가하여 curl 호출에서 키를 전달할 수 있습니다.

터미널에서 `GOOGLE_API_KEY="Your API Key"`를 실행하면 됩니다.

    import osfrom google.colab import userdataos.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')

Gemini 및 `Content` 기반 API
-------------------------

### 텍스트 전용 입력

입력 메시지가 지정된 모델에서 응답을 생성하려면 `generateContent` 메서드를 사용합니다. 입력에 텍스트만 포함된 경우 Gemini 1.5 모델 또는 Gemini 1.0 Pro 모델을 사용합니다.

    curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY \

{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "text": "In the quaint town of Willow Creek, nestled amidst rolling hills and whispering willows, there lived an ordinary boy named Ethan. Ethan's life took an extraordinary turn the day he stumbled upon an enigmatic backpack hidden in the depths of his attic.\\n\\nCuriosity ignited within Ethan as he lifted the worn leather straps and unzipped its mysterious contents. Inside lay a shimmering array of vibrant objects and peculiar trinkets. There was a glowing orb that pulsated with an ethereal glow, a feather that seemed to have a life of its own, and a small, enigmatic key.\\n\\nAs Ethan explored each item, he realized they possessed astonishing abilities. The orb illuminated his path, casting a warm glow in the darkest of nights. The feather granted him the power of flight, allowing him to soar through the skies with newfound freedom. And the key opened a portal to a hidden world, a realm of endless wonder.\\n\\nArmed with his magical backpack, Ethan embarked on countless adventures. He flew over the towering mountains of Willow Creek, exploring their hidden secrets. He navigated the treacherous depths of the Enchanted Forest, where he encountered mythical creatures and ancient spirits. And he ventured into distant, unknown lands, uncovering lost civilizations and forgotten treasures.\\n\\nWith each adventure, Ethan's knowledge and abilities grew. He learned to harness the power of his backpack wisely, using its magic to help others and protect the world from evil forces. The backpack became an extension of himself, a symbol of hope and wonder in the face of adversity.\\n\\nAs the years went by, Ethan's reputation as the boy with the magic backpack spread far and wide. People from all walks of life came to him, seeking his guidance and protection. And Ethan never hesitated to lend a helping hand, using his extraordinary abilities to make the world a better place.\\n\\nIn the end, the magic backpack became more than just a collection of objects. It was a representation of Ethan's unwavering spirit, his boundless imagination, and his unwavering belief in the power of dreams. And as long as Ethan carried it with him, the magic of Willow Creek would live on, illuminating the darkest corners of the world with hope, wonder, and the limitless possibilities that resided within the heart of a child."
          }
        \],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0,
      "safetyRatings": \[
        {
          "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HATE\_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
          "probability": "NEGLIGIBLE"
        }
      \]
    }
  \],
  "promptFeedback": {
    "safetyRatings": \[
      {
        "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HATE\_SPEECH",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HARASSMENT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
        "probability": "NEGLIGIBLE"
      }
    \]
  }
}

### 텍스트 및 이미지 입력

Gemini는 텍스트와 이미지를 모두 입력할 수 있도록 멀티모달 입력(Gemini 1.5 모델 및 Gemini 1.0 Pro Vision)을 처리할 수 있는 다양한 모델을 제공합니다. [프롬프트의 이미지 요구사항](https://ai.google.dev/docs/gemini_api_overview?hl=ko#image_requirements)을 검토하세요.

프롬프트 입력에 텍스트와 이미지가 모두 포함된 경우 Gemini 1.5 모델 또는 Gemini 1.0 Pro Vision 모델을 사용합니다.

다음 스니펫은 요청을 빌드하고 REST API로 전송하는 데 도움이 됩니다.

    curl -o image.jpg https://storage.googleapis.com/generativeai-downloads/images/scones.jpg

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  385k  100  385k    0     0  2053k      0 --:--:-- --:--:-- --:--:-- 2050k

    import PIL.Imageimg = PIL.Image.open("image.jpg")img.resize((512, int(img.height*512/img.width)))

![png](https://ai.google.dev/static/gemini-api/docs/get-started/rest_files/output_dpu7vQA7-_VR_0.png?hl=ko)

    echo '{

    curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GOOGLE_API_KEY} \

"text": " The picture shows a table with a white tablecloth. On the table are two cups of coffee, a bowl of blueberries, and a plate of scones. There are also some flowers on the table."

### 멀티턴 대화 (채팅)

Gemini를 사용하면 여러 차례에 걸쳐 자유 형식으로 대화를 만들 수 있습니다.

    curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY \

"text": "In the quaint village of Fleur-de-Lys, nestled amidst the rolling hills of 17th century France, lived a young maiden named Antoinette. She possessed a heart brimming with curiosity and a spirit as vibrant as the wildflowers that bloomed in the meadows.\\n\\nOne sunny morn, as Antoinette strolled through the cobblestone streets, her gaze fell upon a peculiar sight—a weathered leather backpack resting atop a mossy stone bench. Intrigued, she cautiously approached the bag, her fingers tracing the intricate carvings etched into its surface. As her fingertips grazed the worn leather, a surge of warmth coursed through her body, and the backpack began to emit a soft, ethereal glow."

**참고:** Gemini 1.0 Pro Vision 모델 (텍스트 및 이미지 입력용)은 아직 멀티턴 대화에 최적화되지 않았습니다. 대신 Gemini 1.5 모델 또는 Gemini 1.0 Pro 모델을 사용하세요.

### 구성

모델에 전송하는 모든 프롬프트에는 모델의 응답 생성 방식을 제어하는 매개변수 값이 포함됩니다. 모델은 서로 다른 매개변수 값에 대해 서로 다른 결과를 생성할 수 있습니다. [모델 매개변수](https://ai.google.dev/docs/concepts?hl=ko#model_parameters) 자세히 알아보기

또한 안전 설정을 사용하여 유해한 것으로 간주될 수 있는 응답을 받을 가능성을 조정할 수도 있습니다. 기본적으로 안전 설정은 모든 측정기준에서 보통 또는 높은 확률로 안전하지 않은 콘텐츠를 차단합니다. [안전 설정](https://ai.google.dev/docs/concepts?hl=ko#safety_setting)에 대해 자세히 알아보기

다음 예시에서는 `generateContent` 메서드의 모든 매개변수의 값을 지정합니다.

    curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY \

"text": "Once upon a time, in a small town nestled at the foot of a majestic mountain range, lived a young girl named Lily. Lily was a bright and curious child who loved to explore the world around her. One day, while playing in the forest near her home, she stumbled upon a hidden cave. Intrigued, she stepped inside, and to her amazement, she discovered a dusty old backpack lying in a corner.\\n\\nCuriosity piqued, Lily reached out and picked up the backpack. As soon as her fingers brushed against the worn leather, she felt a strange tingling sensation coursing through her body. Suddenly, the backpack began to glow, emitting a soft, ethereal light that filled the cave.\\n\\nWith wide-eyed wonder, Lily opened the backpack to find it filled with an assortment of magical objects. There was a compass that always pointed to the nearest adventure, a magnifying glass that could reveal hidden secrets, a telescope that allowed her to see distant lands, and a book that contained the knowledge of the universe.\\n\\nOverjoyed with her discovery, Lily took the magic backpack home and began using its contents to explore the world in ways she had never imagined. She followed the compass to discover hidden treasures, used the magnifying glass to uncover the secrets of nature, gazed through the telescope to witness the wonders of the cosmos, and delved into the book to learn about the mysteries of the universe.\\n\\nAs Lily's adventures continued, she realized that the magic backpack was more than just a collection of enchanted items. It was a symbol of her own limitless potential and the power of her imagination. It taught her that with curiosity, courage, and a touch of magic, anything was possible.\\n\\nNews of Lily's magical backpack spread throughout the town, and soon, children from all around came to her, eager to learn about its wonders. Lily welcomed them with open arms, sharing her stories and inspiring them to embark on their own adventures.\\n\\nAnd so, the magic backpack became a beacon of hope and wonder, reminding everyone that the world is full of hidden treasures waiting to be discovered, if only one has the courage to step into the unknown."

### 스트림 생성 콘텐츠

`generateContent` 메서드는 전체 생성 프로세스를 완료한 후 응답을 반환합니다. 전체 결과를 기다리지 않고 대신 `streamGenerateContent`를 사용하여 부분 결과를 반환하여 상호작용을 더 빠르게 달성할 수 있습니다.

**중요:** URL 매개변수에 `alt=sse`를 설정해야 합니다. 각 줄은 `candidates[0].content.parts[0].text`에 출력 텍스트 청크가 있는 [GenerateContentResponse](https://ai.google.dev/api/rest/v1beta/GenerateContentResponse?hl=ko) 객체입니다.

    !curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:streamGenerateContent?alt=sse&key=${GOOGLE_API_KEY}" \        -H 'Content-Type: application/json' \        --no-buffer \        -d '{ "contents":[{"parts":[{"text": "Write long a story about a magic backpack."}]}]}' \        2> /dev/null

data: {"candidates": \[{"content": {"parts": \[{"text": "In the quaint little town of Willow Creek, nestled among rolling hills and whispering willows"}\],"role": "model"},"finishReason": "STOP","index": 0,"safetyRatings": \[{"category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HATE\_SPEECH","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HARASSMENT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT","probability": "NEGLIGIBLE"}\]}\],"promptFeedback": {"safetyRatings": \[{"category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HATE\_SPEECH","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HARASSMENT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT","probability": "NEGLIGIBLE"}\]} }

data: {"candidates": \[{"content": {"parts": \[{"text": ", there existed an extraordinary backpack that possessed an astonishing secret. Its unassuming canvas exterior and worn leather straps held a hidden realm brimming with wonder and endless possibilities."}\],"role": "model"},"finishReason": "STOP","index": 0,"safetyRatings": \[{"category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HATE\_SPEECH","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HARASSMENT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT","probability": "NEGLIGIBLE"}\]}\]}

data: {"candidates": \[{"content": {"parts": \[{"text": "\\n\\nYoung Oliver, a curious and imaginative boy, stumbled upon this magical backpack in the dusty attic of his grandmother's house. Intrigued by its enigmatic aura, he unzipped it cautiously, revealing a seemingly ordinary interior. But as his fingers brushed against the lining, an ethereal glow emanated from within.\\n\\n"}\],"role": "model"},"finishReason": "STOP","index": 0,"safetyRatings": \[{"category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HATE\_SPEECH","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HARASSMENT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT","probability": "NEGLIGIBLE"}\]}\]}

data: {"candidates": \[{"content": {"parts": \[{"text": "With a gasp of surprise, Oliver watched as the backpack transformed before his very eyes. Its fabric shimmered and flowed like liquid silver, morphing into a portal that connected him to a hidden dimension. Step by step, he ventured into this enchanted realm, his heart pounding with a mixture of trepidation and exhilaration.\\n\\nThe backpack's interior was a vast and wondrous labyrinth filled with towering bookshelves, bubbling potions, and ethereal artifacts. Each turn offered a new discovery: a self-playing piano, a talking mirror that whispered ancient wisdom, and a compass that pointed to the furthest reaches of the imagination.\\n\\nOliver soon realized"}\],"role": "model"},"finishReason": "STOP","index": 0,"safetyRatings": \[{"category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HATE\_SPEECH","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HARASSMENT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT","probability": "NEGLIGIBLE"}\]}\]}

data: {"candidates": \[{"content": {"parts": \[{"text": " that this backpack was no mere container but a sentient being, capable of aiding him in his quests and expanding his horizons. It granted him the gift of tongues, allowing him to speak with animals and creatures from distant lands. It gifted him a quill that wrote stories that danced off the page, bringing his wildest dreams to life.\\n\\nTogether, Oliver and the backpack embarked on extraordinary adventures. They soared through the skies on the back of a majestic griffon, traversed treacherous terrains with the aid of a shape-shifting fox, and solved mysteries that had long baffled the wisest minds in Willow Creek.\\n\\nAs the days turned into weeks, Oliver's imagination flourished beyond measure. He painted vibrant landscapes with words, composed symphonies that echoed through the hidden realm, and invented gadgets that defied the laws of physics. The backpack became an extension of his boundless creativity, nurturing his wonder and fueling his aspirations.\\n\\nNews of Oliver's extraordinary backpack spread throughout the town and beyond. People flocked from far and wide to witness its marvels. Scholars sought its wisdom, artists sought its inspiration, and children dreamed of experiencing its boundless adventures.\\n\\nHowever, not all who approached the backpack with pure intentions. One fateful day, a greedy sorcerer named Maldred attempted to seize its power for himself. But"}\],"role": "model"},"finishReason": "STOP","index": 0,"safetyRatings": \[{"category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HATE\_SPEECH","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HARASSMENT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT","probability": "NEGLIGIBLE"}\]}\]}

data: {"candidates": \[{"content": {"parts": \[{"text": " the backpack, sensing his malevolent nature, resisted his grasp and summoned a legion of fantastical creatures to its defense.\\n\\nIn a fierce battle that shook the very fabric of the hidden realm, Oliver and the backpack allied with brave heroes and wise wizards to defeat Maldred and his wicked forces. The town of Willow Creek was forever grateful, and the backpack became a symbol of hope and imagination for all who knew of its existence.\\n\\nAs the years passed, Oliver grew into a wise and compassionate leader, using the magic backpack to spread joy, inspire creativity, and unlock the potential of those around him. The hidden realm within its depths became a sanctuary for dreamers, inventors, and anyone who dared to embrace the wonders of the unknown.\\n\\nAnd so, the tale of the magic backpack was passed down through generations, a timeless testament to the power of imagination and the boundless possibilities that lie when wonder and curiosity ignite the human spirit."}\],"role": "model"},"finishReason": "STOP","index": 0,"safetyRatings": \[{"category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HATE\_SPEECH","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_HARASSMENT","probability": "NEGLIGIBLE"},{"category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT","probability": "NEGLIGIBLE"}\]}\]}

**참고:** 먼저 전체 스트림을 읽지 않고 이를 처리하려면 스트리밍 JSON 파서가 필요합니다.

### 토큰 개수

긴 프롬프트를 사용할 때는 모델에 콘텐츠를 보내기 전에 토큰을 세는 것이 유용할 수 있습니다.

    curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY \

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100   127    0    23  100   104    105    477 --:--:-- --:--:-- --:--:--   585

    cat response.json

{
  "totalTokens": 8
}

### 임베딩

임베딩은 배열의 부동 소수점 숫자 목록으로 정보를 표현하는 데 사용되는 기법입니다. Gemini를 사용하면 텍스트 (단어, 문장, 텍스트 블록)를 벡터화된 형식으로 표시할 수 있으므로 임베딩을 더 쉽게 비교하고 대조할 수 있습니다. 예를 들어 비슷한 주제나 감정을 공유하는 두 텍스트는 코사인 유사성과 같은 수학적 비교 기술을 통해 식별할 수 있는 비슷한 임베딩을 사용해야 합니다.

`embedding-001` 모델을 `embedContents` 또는 `batchEmbedContents`와 함께 사용합니다.

    curl https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent?key=$GOOGLE_API_KEY \

{
  "embedding": {
    "values": \[
      0.008624583,
      -0.030451821,
      -0.042496547,
      -0.029230341,
      0.05486475,
      0.006694871,
      0.004025645,

    curl https://generativelanguage.googleapis.com/v1beta/models/embedding-001:batchEmbedContents?key=$GOOGLE_API_KEY \

{
  "embeddings": \[
    {
      "values": \[
        0.008624583,
        -0.030451821,
        -0.042496547,
        -0.029230341,
        0.05486475,
        0.006694871,

모델 정보
-----

### 모델 가져오기

모델의 URL을 `GET`하면 API에서 `get` 메서드를 사용하여 버전, 표시 이름, 입력 토큰 한도 등의 모델에 대한 정보를 반환합니다.

    curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro?key=$GOOGLE_API_KEY

{
  "name": "models/gemini-pro",
  "version": "001",
  "displayName": "Gemini Pro",
  "description": "The best model for scaling across a wide range of tasks",
  "inputTokenLimit": 30720,
  "outputTokenLimit": 2048,
  "supportedGenerationMethods": \[
    "generateContent",
    "countTokens"
  \],
  "temperature": 0.9,
  "topP": 1,
  "topK": 1
}

### 모델 나열

`models` 디렉터리를 `GET`하면 `list` 메서드를 사용하여 Gemini 및 PaLM 계열 모델을 포함하여 API를 통해 사용 가능한 모든 모델을 나열합니다.

    curl https://generativelanguage.googleapis.com/v1beta/models?key=$GOOGLE_API_KEY

{
  "models": \[
    {
      "name": "models/chat-bison-001",
      "version": "001",
      "displayName": "Chat Bison",
      "description": "Chat-optimized generative language model.",
      "inputTokenLimit": 4096,
      "outputTokenLimit": 1024,
      "supportedGenerationMethods": \[
        "generateMessage",
        "countMessageTokens"
      \],
      "temperature": 0.25,
      "topP": 0.95,
      "topK": 40
    },
    {
      "name": "models/text-bison-001",
      "version": "001",
      "displayName": "Text Bison",
      "description": "Model targeted for text generation.",
      "inputTokenLimit": 8196,
      "outputTokenLimit": 1024,
      "supportedGenerationMethods": \[
        "generateText",
        "countTextTokens",
        "createTunedTextModel"
      \],
      "temperature": 0.7,
      "topP": 0.95,
      "topK": 40
    },
    {
      "name": "models/embedding-gecko-001",
      "version": "001",
      "displayName": "Embedding Gecko",
      "description": "Obtain a distributed representation of a text.",
      "inputTokenLimit": 1024,
      "outputTokenLimit": 1,
      "supportedGenerationMethods": \[
        "embedText",
        "countTextTokens"
      \]
    },
    {
      "name": "models/embedding-gecko-002",
      "version": "002",
      "displayName": "Embedding Gecko 002",
      "description": "Obtain a distributed representation of a text.",
      "inputTokenLimit": 2048,
      "outputTokenLimit": 1,
      "supportedGenerationMethods": \[
        "embedText",
        "countTextTokens"
      \]
    },
    {
      "name": "models/gemini-pro",
      "version": "001",
      "displayName": "Gemini Pro",
      "description": "The best model for scaling across a wide range of tasks",
      "inputTokenLimit": 30720,
      "outputTokenLimit": 2048,
      "supportedGenerationMethods": \[
        "generateContent",
        "countTokens"
      \],
      "temperature": 0.9,
      "topP": 1,
      "topK": 1
    },
    {
      "name": "models/gemini-pro-vision",
      "version": "001",
      "displayName": "Gemini Pro Vision",
      "description": "The best image understanding model to handle a broad range of applications",
      "inputTokenLimit": 12288,
      "outputTokenLimit": 4096,
      "supportedGenerationMethods": \[
        "generateContent",
        "countTokens"
      \],
      "temperature": 0.4,
      "topP": 1,
      "topK": 32
    },
    {
      "name": "models/gemini-ultra",
      "version": "001",
      "displayName": "Gemini Ultra",
      "description": "The most capable model for highly complex tasks",
      "inputTokenLimit": 30720,
      "outputTokenLimit": 2048,
      "supportedGenerationMethods": \[
        "generateContent",
        "countTokens"
      \],
      "temperature": 0.9,
      "topP": 1,
      "topK": 32
    },
    {
      "name": "models/embedding-001",
      "version": "001",
      "displayName": "Embedding 001",
      "description": "Obtain a distributed representation of a text.",
      "inputTokenLimit": 2048,
      "outputTokenLimit": 1,
      "supportedGenerationMethods": \[
        "embedContent",
        "countTextTokens"
      \]
    },
    {
      "name": "models/aqa",
      "version": "001",
      "displayName": "Model that performs Attributed Question Answering.",
      "description": "Model trained to return answers to questions that are grounded in provided sources, along with estimating answerable probability.",
      "inputTokenLimit": 7168,
      "outputTokenLimit": 1024,
      "supportedGenerationMethods": \[
        "generateAnswer"
      \],
      "temperature": 0.2,
      "topP": 1,
      "topK": 40
    }
  \]
}

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-06-06(UTC)
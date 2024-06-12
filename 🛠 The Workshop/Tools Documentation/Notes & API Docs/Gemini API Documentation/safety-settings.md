---
Please provide me with the context or details for the mission you want to create. For example, tell me: "* **What is the mission about?** (e.g., Saving the world, finding a lost treasure, exploring a new planet, etc.)"
* **Who are the characters involved?** (e.g., A team of heroes, a lone adventurer, a group of friends, etc.)
* **What are the challenges they face?** (e.g., Dangerous enemies, tricky puzzles, time limits, etc.)
* **What is the ultimate goal?** (e.g., Defeating the villain, finding the treasure, completing the mission, etc.)

Once you give me more information, I can help you write a compelling and engaging mission statement.
---

*   이 페이지의 내용
*   [안전 필터](#safety-filters)
    *   [확률과 심각도 비교](#probability-vs)
    *   [안전 설정](#safety-settings)
    *   [안전 피드백](#safety-feedback)
*   [Google AI Studio의 안전 설정](#safety-settings-ai-studio)
*   [코드 예](#code-examples)
    *   [요청 예](#request-example)
    *   [응답 예](#response-example)
*   [다음 단계](#next-steps)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

안전 설정
=====

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [안전 필터](#safety-filters)
    *   [확률과 심각도 비교](#probability-vs)
    *   [안전 설정](#safety-settings)
    *   [안전 피드백](#safety-feedback)
*   [Google AI Studio의 안전 설정](#safety-settings-ai-studio)
*   [코드 예](#code-examples)
    *   [요청 예](#request-example)
    *   [응답 예](#response-example)
*   [다음 단계](#next-steps)

이 가이드에서는 Gemini API에서 사용할 수 있는 조정 가능한 안전 설정을 설명합니다. 프로토타입 제작 단계에서 4가지 차원에서 안전 설정을 조정하여 애플리케이션에 필요한 구성이 더 많거나 덜 필요한지 빠르게 평가할 수 있습니다. 기본적으로 안전 설정은 모든 측정기준에서 안전하지 않을 확률이 보통 이상인 콘텐츠 (메시지 포함)를 차단합니다. 이 기준 안전성은 대부분의 사용 사례에 적합하도록 설계되었으므로 애플리케이션에서 일관되게 필요한 경우에만 안전 설정을 조정해야 합니다.

**참고:** 낮은 안전성 설정으로 조정하면 애플리케이션의 심층 검토 프로세스가 트리거됩니다.

안전 필터
-----

조정 가능한 안전 필터 외에도 Gemini API에는 아동 안전을 위협하는 콘텐츠와 같은 핵심 피해에 대한 보호 기능이 내장되어 있습니다. 이러한 유형의 피해는 항상 차단되며 조정할 수 없습니다.

조정 가능한 안전 필터는 다음 카테고리를 다룹니다.

*   괴롭힘
*   증오심 표현
*   음란물
*   위험한 카테고리

이러한 설정을 통해 개발자는 사용 사례에 적합한 설정을 결정할 수 있습니다. 예를 들어 비디오 게임 대사를 만드는 경우 게임의 특성상 위험하다고 평가된 콘텐츠를 더 많이 허용해도 된다고 간주할 수 있습니다. 다음은 이러한 안전 설정에서 유연성이 필요할 수 있는 몇 가지 다른 사용 사례입니다.

| 사용 사례 | 카테고리 |
| --- | --- |
| 괴롭힘 방지 교육 앱 | 증오심 표현, 음란물 |
| 시나리오 작가 | 음란물, 위험 |
| 유해성 분류기 | 괴롭힘, 위험 |

### 확률과 심각도 비교

Gemini API는 콘텐츠가 안전하지 않고 심각도가 **아닌** 콘텐츠의 **가능성**을 기준으로 콘텐츠를 차단합니다. 일부 콘텐츠는 유해한 심각도가 여전히 높더라도 안전하지 않을 가능성이 낮을 수 있으므로 이 점을 고려해야 합니다. 예를 들어 문장을 비교해 보겠습니다.

1.  로봇이 나를 때렸습니다.
2.  로봇이 나를 베었습니다.

문장 1은 안전하지 않을 가능성이 더 높을 수 있지만 폭력 측면에서 2번 문장이 더 높은 심각도로 간주될 수 있습니다.

따라서 각 개발자는 최종 사용자에게 미치는 피해를 최소화하면서 주요 사용 사례를 지원하는 데 필요한 적절한 차단 수준을 신중하게 테스트하고 고려해야 합니다.

### 안전 설정

안전 설정은 생성 서비스에 전송하는 요청의 일부입니다. 이 설정은 API에 전송하는 각 요청에 맞게 조정할 수 있습니다. 다음 표에는 개발자가 설정할 수 있는 카테고리와 각 카테고리에 포함되는 피해의 유형이 나와 있습니다.

| 카테고리 | 내용 입력란 |
| --- | --- |
| 괴롭힘 | ID 또는 보호 속성을 대상으로 하는 부정적이거나 유해한 댓글 |
| 증오심 표현 | 무례하거나 모욕적이거나 욕설이 있는 콘텐츠 |
| 음란물 | 성행위 또는 기타 외설적인 콘텐츠에 대한 참조가 포함 |
| 위험한 카테고리 | 유해한 행위를 조장, 촉진 또는 장려합니다. |

이러한 정의는 [API 참조](https://ai.google.dev/api/rest/v1/HarmCategory?hl=ko)에도 나와 있습니다. Gemini 모델은 `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_DANGEROUS_CONTENT`만 지원합니다. 다른 카테고리는 PaLM2(기존) 모델에서 사용됩니다.

다음 표에서는 각 카테고리에서 조정할 수 있는 블록 설정을 설명합니다. 예를 들어 **증오심 표현** 카테고리의 차단 설정을 **소수 차단**으로 설정하면 증오심 표현 콘텐츠일 가능성이 높은 모든 콘텐츠가 차단됩니다. 하지만 가능성이 낮은 모든 항목이 허용됩니다.

정책을 설정하지 않으면 기본 차단 설정은 모든 카테고리에 대해 **일부 차단**입니다.

| 기준 (Google AI Studio) | 기준(API) | 설명 |
| --- | --- | --- |
| 차단 안함 | BLOCK\_NONE | 안전하지 않은 콘텐츠 가능성과 관계없이 항상 표시 |
| 소수 차단 | BLOCK\_ONLY\_HIGH | 안전하지 않은 콘텐츠일 가능성이 높은 경우 차단 |
| 일부 차단 | BLOCK\_MEDIUM\_AND\_ABOVE | 안전하지 않은 콘텐츠일 가능성이 중간 또는 높은 경우 차단 |
| 대부분 차단 | BLOCK\_LOW\_AND\_ABOVE | 안전하지 않은 콘텐츠일 가능성이 낮거나 중간 또는 높은 경우 차단 |
|  | HARM\_BLOCK\_THRESHOLD\_UNSPECIFIED | 기준점이 지정되지 않았습니다. 기본 기준점을 사용하여 차단합니다. |

생성형 서비스에 전송하는 각 요청에 대해 이러한 설정을 지정할 수 있습니다. 자세한 내용은 [`HarmBlockThreshold`](https://ai.google.dev/api/rest/v1/SafetySetting?hl=ko#harmblockthreshold) API 참조를 확인하세요.

### 안전 피드백

[`generateContent`](https://ai.google.dev/api/rest/v1/models/generateContent?hl=ko)는 안전 의견이 포함된 [`GenerateContentResponse`](https://ai.google.dev/api/rest/v1/GenerateContentResponse?hl=ko)를 반환합니다.

프롬프트 피드백은 [`promptFeedback`](https://ai.google.dev/api/rest/v1/GenerateContentResponse?hl=ko#PromptFeedback)에 포함되어 있습니다. [`promptFeedback.blockReason`](https://ai.google.dev/api/rest/v1/GenerateContentResponse?hl=ko#blockreason)가 설정되면 메시지 콘텐츠가 차단됩니다.

응답 후보 의견은 [`finishReason`](https://ai.google.dev/api/rest/v1/GenerateContentResponse?hl=ko#FinishReason) 및 [`safetyRatings`](https://ai.google.dev/api/rest/v1/GenerateContentResponse?hl=ko#safetyrating)에 포함됩니다. 응답 콘텐츠가 차단되고 `finishReason`가 `SAFETY`이면 `safetyRatings`를 검사하여 자세한 내용을 확인할 수 있습니다. 안전성 등급에는 카테고리 및 위험 분류 확률이 포함됩니다. 차단된 콘텐츠는 반환되지 않습니다.

반환되는 확률은 다음 표와 같이 블록 신뢰 수준에 해당합니다.

| 확률 | 설명 |
| --- | --- |
| 무시할 수 있음 | 콘텐츠가 안전하지 않을 가능성이 거의 없습니다. |
| 낮음 | 콘텐츠가 안전하지 않을 가능성이 낮음 |
| 중간 정도의 참여 | 콘텐츠가 안전하지 않을 가능성이 중간입니다. |
| 높음 | 콘텐츠가 안전하지 않을 가능성이 높습니다. |

예를 들어 괴롭힘 카테고리가 확률이 높기 때문에 콘텐츠가 차단되었다면 반환된 안전성 평점은 카테고리가 `HARASSMENT`이고 피해 확률은 `HIGH`로 설정됩니다.

Google AI Studio의 안전 설정
-----------------------

Google AI Studio에서 안전 설정을 조정할 수도 있지만 사용 중지할 수는 없습니다. 사용 중지하려면 **설정 실행**에서 **안전 설정 수정**을 클릭합니다.

![안전 설정 버튼](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_button.png?hl=ko)

또한 노브를 사용해 각 설정을 다음과 같이 조정합니다.

![안전 설정 버튼](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=ko)

콘텐츠가 차단되면 warning **콘텐츠 없음** 메시지가 표시됩니다. 자세한 내용을 보려면 포인터를 **콘텐츠 없음** 위로 가져가고 warning **안전**을 클릭합니다.

코드 예
----

이 섹션에서는 Python 클라이언트 라이브러리를 사용하여 코드에서 안전 설정을 사용하는 방법을 보여줍니다.

### 요청 예

다음은 `GenerateContent` 호출에서 안전 설정을 지정하는 방법을 보여주는 Python 코드 스니펫입니다. 이렇게 하면 피해 카테고리 `Harassment` 및 `Hate speech`가 `BLOCK_LOW_AND_ABOVE`로 설정되어 괴롭힘 또는 증오심 표현이 될 가능성이 낮거나 높은 콘텐츠를 차단합니다.

    from google.generativeai.types import HarmCategory, HarmBlockThresholdmodel = genai.GenerativeModel(model_name='gemini-1.5-flash')response = model.generate_content(    ['Do these look store-bought or homemade?', img],    safety_settings={        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,    })

### 응답 예

다음은 응답에서 안전 의견을 파싱하는 코드 스니펫입니다.

    try:  print(response.text)except ValueError:  # If the response doesn't contain text, check if the prompt was blocked.  print(response.prompt_feedback)  # Also check the finish reason to see if the response was blocked.  print(response.candidates[0].finish_reason)  # If the finish reason was SAFETY, the safety ratings have more details.  print(response.candidates[0].safety_ratings)

다음 단계
-----

*   전체 API에 대해 자세히 알아보려면 [API 참조](https://ai.google.dev/api?hl=ko)를 확인하세요.
*   LLM으로 개발할 때 안전 고려사항에 관한 일반적인 내용은 [안전 안내](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ko)를 참조하세요.
*   확률과 심각도를 비교하는 [Jigsaw팀](https://developers.perspectiveapi.com/s/about-the-api-score) 자세히 알아보기
*   [Perspective API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7)와 같이 안전 솔루션에 기여하는 제품에 관해 자세히 알아보세요.
*   이러한 안전 설정을 사용하여 유해 분류 기준을 만들 수 있습니다. 시작하려면 [분류 예](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=ko)를 참고하세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-24(UTC)
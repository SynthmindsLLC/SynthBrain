---
Please provide me with more information about the mission you want to write about. I need some context to be able to write a compelling mission statement. 

For example, tell me: "* **What is the mission about?**  Is it about a company, a project, a personal goal, a community initiative?"
* **What is the purpose?** What are you trying to achieve?
* **What are the key values?** What principles are guiding your actions?
* **Who is the target audience?** Who will be affected by this mission?

The more information you give me, the better I can help you create a powerful and effective mission statement.
---

*   이 페이지의 내용
*   [기본 요건](#prerequisites)
*   [API 키 설정](#set-up-api-key)
*   [SDK 설치](#install-sdk)
*   [생성 모델 초기화](#initialize-generative)
*   [텍스트 생성](#generate-text)
*   [다음 단계](#what's-next)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

Gemini API 빠른 시작
================

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [기본 요건](#prerequisites)
*   [API 키 설정](#set-up-api-key)
*   [SDK 설치](#install-sdk)
*   [생성 모델 초기화](#initialize-generative)
*   [텍스트 생성](#generate-text)
*   [다음 단계](#what's-next)

이 빠른 시작에서는 원하는 SDK를 사용하여 Gemini API를 시작하는 방법을 보여줍니다.

Python Node.js Go Dart (Flutter) Android Swift 웹

  

기본 요건
-----

<table align="left" class="tfo-notebook-buttons"><tbody><tr><td><a href="https://ai.google.dev/gemini-api/docs/quickstart?hl=ko" target="_blank"><img height="32" src="https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png?hl=ko" width="32">Google AI에서 보기</a></td><td><a href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/tutorials/quickstart_colab.ipynb?hl=ko" target="_blank"><img src="https://www.tensorflow.org/images/colab_logo_32px.png?hl=ko">Google Colab에서 실행</a></td><td><a href="https://github.com/google/generative-ai-docs/blob/main/site/en/tutorials/quickstart_colab.ipynb" target="_blank"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=ko">GitHub에서 노트북 보기</a></td></tr></tbody></table>

이 빠른 시작을 로컬에서 완료하려면 개발 환경이 다음 요구사항을 충족하는지 확인하세요.

*   Python 3.9 이상
*   노트북을 실행할 `jupyter` 설치

API 키 설정
--------

Gemini API를 사용하려면 API 키가 필요합니다. 아직 키가 없으면 Google AI Studio에서 키를 만듭니다

[API 키 가져오기](https://makersuite.google.com/app/apikey?hl=ko)

그런 다음 키를 구성합니다.

버전 제어 시스템에 API 키를 체크인하지 _않는_ 것이 좋습니다. 이 빠른 시작에서는 API 키에 환경 변수로 액세스한다고 가정합니다.

API 키를 환경 변수에 할당합니다.

    export API_KEY=<YOUR_API_KEY>

SDK 설치
------

Gemini API용 Python SDK는 [`google-generativeai`](https://pypi.org/project/google-generativeai/) 패키지에 포함되어 있습니다. pip를 사용하여 종속 항목을 설치합니다.

    pip install -q -U google-generativeai

생성 모델 초기화
---------

API를 호출하려면 먼저 생성 모델을 가져오고 초기화해야 합니다.

    import google.generativeai as genaigenai.configure(api_key=os.environ["API_KEY"])# The Gemini 1.5 models are versatile and work with both text-only and multimodal promptsmodel = genai.GenerativeModel('gemini-1.5-flash')

텍스트 생성
------

    response = model.generate_content("Write a story about a magic backpack.")print(response.text)

다음 단계
-----

Gemini API 작업에 관한 자세한 내용은 선택한 언어의 가이드를 참고하세요.

*   [Python](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python&hl=ko)
*   [Go](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=go&hl=ko)
*   [Node.js](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=node&hl=ko)
*   [웹](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=web&hl=ko)
*   [Dart (Flutter)](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=dart&hl=ko)
*   [Swift](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=swift&hl=ko)
*   [Android](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=android&hl=ko)
*   [Android (온디바이스)](https://ai.google.dev/gemini-api/docs/get-started/android_aicore?hl=ko)

`curl` 명령어를 사용하여 Gemini API를 사용해 볼 수도 있습니다.

*   [REST API](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=rest&hl=ko)

생성형 AI 모델을 처음 사용하는 경우 빠른 시작을 사용해 보기 전에 [개념 가이드](https://ai.google.dev/docs/concepts?hl=ko) 및 [Gemini API 개요](https://ai.google.dev/docs/gemini_api_overview?hl=ko)를 살펴보는 것이 좋습니다.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-24(UTC)
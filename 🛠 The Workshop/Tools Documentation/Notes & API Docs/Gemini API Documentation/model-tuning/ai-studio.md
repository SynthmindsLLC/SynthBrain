*   이 페이지의 내용
*   [조정 데이터 세트 만들기](#dataset)
*   [조정된 모델 만들기](#create-tuned)
*   [조정된 모델 사용](#using-tuned)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

Google AI Studio로 모델 조정하기
=========================

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [조정 데이터 세트 만들기](#dataset)
*   [조정된 모델 만들기](#create-tuned)
*   [조정된 모델 사용](#using-tuned)

Gemini 인공지능 (AI) 모델로 애플리케이션을 빌드할 때는 [자유 형식 프롬프트](https://ai.google.dev/tutorials/ai-studio_quickstart?hl=ko#freeform_example) 또는 [구조화된 프롬프트](https://ai.google.dev/tutorials/ai-studio_quickstart?hl=ko#structured_example)를 사용할 때보다 모델이 안내 또는 요청에 응답하는 방식에 관한 더 강력한 안내를 제공해야 할 수 있습니다. 모델 _조정_을 사용하면 모델의 동작을 더 크게 변경할 수 있으며 일반적인 프롬프트에 적합한 것보다 훨씬 더 많은 학습 예시 데이터가 필요합니다. 조정된 모델의 또 다른 이점은 두 개 이상의 프롬프트에 사용할 수 있다는 점입니다 모델 조정에 대한 자세한 내용은 [모델 조정 가이드](https://ai.google.dev/docs/model_tuning_guidance?hl=ko)를 참조하세요.

이 가이드에서는 Google AI Studio로 조정된 모델을 만들고 사용하는 방법을 설명합니다.

조정 데이터 세트 만들기
-------------

모델을 조정하려면 표준 프롬프팅 기법보다 더 많은 예 또는 학습 데이터가 필요합니다. 최소 20개의 예시로 모델을 조정할 수 있습니다. 일반적으로 모델의 동작을 크게 변경하려면 100~500개의 예가 필요합니다. 이 크기 이상의 학습 데이터 세트가 없는 경우 먼저 [구조화된 프롬프트](https://ai.google.dev/tutorials/ai-studio_quickstart?hl=ko#structured_example)를 사용해 보세요. 이 기능을 통해 최소 3~4개의 학습 예시로 모델의 동작을 안내할 수 있습니다.

조정 데이터 세트에서 제공하는 학습 예시는 생성 모델이 응답을 생성하는 과정을 안내합니다. 데이터 세트의 각 레코드에는 최소한 프롬프트 명령을 나타내는 입력 값과 생성 모델의 예상 응답을 나타내는 출력 값이 있어야 합니다.

다음은 이 프롬프트의 입력 및 출력 값의 예입니다. 이 경우 _제품 이름_은 모델에 대한 입력 또는 프롬프트이고 _제품 사본_은 예상 출력입니다.

| 제품 이름 (입력) | 제품 문구 (출력) |
| --- | --- |
| 올드 스쿨 스니커즈 | 끈을 묶어 보세요. 다른 신발과는 전혀 다른 스타일과 기능을 제공하는 동시에 상징적인 스타일과 독특한 색상 팔레트를 표시할 수 있습니다. |
| 슈퍼소프트 후드티 | 새로운 남녀공용 후드티로 아늑하고 스타일리시하게 입으세요. 100% 면으로 만든 이 후드티는 부드럽고 하루 종일 편안한 착용감을 선사합니다. 내부에 약간 브러시 처리되어 가장 추운 날에도 따뜻하게 유지됩니다. |

학습 데이터 세트에는 두 개 이상의 입력과 두 개 이상의 출력이 있을 수 있으며, 각 레코드에는 하나 이상의 입력과 출력이 _있어야 합니다_. AI Studio의 [구조화된 프롬프트](https://ai.google.dev/tutorials/ai-studio_quickstart?hl=ko#structured_example) 사용자 인터페이스를 사용하여 데이터 세트를 만들거나 CSV (쉼표로 구분된 값) 데이터 파일 또는 Google Sheets 스프레드시트에서 데이터를 가져올 수 있습니다.

조정된 모델 만들기
----------

조정 데이터 세트를 만든 후 AI 스튜디오에서 데이터 세트를 제공하고 일부 구성 매개변수를 설정하여 조정된 버전의 Gemini 모델을 빌드할 수 있습니다. 필요한 입력을 제공하면 시스템에서 조정된 모델을 만들고 프롬프트에서 이를 사용할 수 있습니다.

조정된 모델을 만들려면 다음 안내를 따르세요.

1.  AI Studio 웹 앱의 인터페이스 왼쪽에서 **조정된 모델** 옵션을 선택합니다.
2.  **조정할 데이터 선택** 대화상자에서 _구조화된 프롬프트_를 선택하여 조정 데이터 세트를 연결하거나 **가져오기** 버튼을 클릭하여 쉼표로 구분된 값 (.CSV) 형식 파일 또는 Google 스프레드시트 스프레드시트로 데이터를 로드합니다.
3.  **조정된 모델 이름** 필드에 조정된 모델의 이름을 입력합니다. 조정 작업이 완료되면 이 이름이 선택 가능한 모델로 표시됩니다.
4.  **설명** 필드에 조정된 모델의 설명(선택사항)을 입력합니다.
5.  **모델** 필드에서 조정된 모델의 기반으로 사용할 기반 모델을 선택합니다.
6.  필요에 따라 조정된 모델을 만들기 위한 **고급 설정**을 지정할 수 있습니다. 이러한 설정에 대한 자세한 내용은 [모델 조정 가이드](https://ai.google.dev/docs/model_tuning_guidance?hl=ko#advanced-settings)를 참조하세요.
7.  **조정**을 선택하여 조정된 모델을 만드는 프로세스를 시작합니다.

크기나 데이터 세트, 지정된 _에포크_ 수, 현재 시스템 부하에 따라 시스템에서 조정된 버전을 빌드하는 데 몇 분 이상 걸릴 수 있습니다. 애플리케이션 왼쪽에 있는 **내 라이브러리**를 선택하고 조정된 모델의 이름을 찾아 조정 프로세스의 상태를 확인할 수 있습니다.

**참고:** Google AI Studio에서 PaLM 기존 모델을 조정하려면 **설정**에서 **기존 모델 표시** 옵션을 켭니다.

조정된 모델 사용
---------

모델 조정 빌드가 완료되면 프롬프트에서 사용할 모델을 선택할 수 있습니다. 프롬프트가 조정된 데이터 세트의 예시 구조를 준수하는 한 기존 또는 새로운 자유 형식 또는 구조화된 프롬프트와 함께 조정된 모델을 사용할 수 있습니다.

조정된 모델을 사용하려면 다음 안내를 따르세요.

1.  AI Studio 웹 앱에서 기존 프롬프트를 열거나 새 프롬프트를 시작합니다.
2.  **실행 설정** 섹션에서 _모델_ 드롭다운을 선택하고 조정된 모델의 이름을 선택합니다.
3.  프롬프트를 작성하거나 업데이트하고 **실행**을 선택하여 조정된 모델을 사용합니다.

조정 시 생성 모델의 동작을 변경하려면 상당한 양의 데이터가 필요합니다. 프롬프트가 원하는 동작을 생성하지 않으면 [조정 데이터 세트](#dataset), [조정 매개변수](https://ai.google.dev/docs/model_tuning_guidance?hl=ko#advanced-settings)를 평가하고 예시를 더 추가해 보세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-04-18(UTC)
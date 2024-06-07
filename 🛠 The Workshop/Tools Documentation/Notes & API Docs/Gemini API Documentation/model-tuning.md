*   이 페이지의 내용
*   [모델 조정의 원리](#how-model)
*   [지원되는 모델](#supported-models)
*   [모델 조정을 위한 워크플로](#model-tuning-workflow)
*   [데이터 세트 준비](#prepare-dataset)
    *   [형식](#format)
    *   [학습 데이터 크기](#size-recommendation)
*   [조정 데이터 세트 업로드](#upload-tuning)
*   [고급 조정 설정](#advanced-settings)
    *   [추천 구성](#recommended-configurations)
*   [조정 작업 상태 확인](#check-tuning-status)
*   [오류 문제 해결하기](#troubleshoot-errors)
    *   [인증](#authentication)
    *   [취소된 모델](#canceled-models)
*   [다음 단계](#what's-next)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

모델 조정 소개
========

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [모델 조정의 원리](#how-model)
*   [지원되는 모델](#supported-models)
*   [모델 조정을 위한 워크플로](#model-tuning-workflow)
*   [데이터 세트 준비](#prepare-dataset)
    *   [형식](#format)
    *   [학습 데이터 크기](#size-recommendation)
*   [조정 데이터 세트 업로드](#upload-tuning)
*   [고급 조정 설정](#advanced-settings)
    *   [추천 구성](#recommended-configurations)
*   [조정 작업 상태 확인](#check-tuning-status)
*   [오류 문제 해결하기](#troubleshoot-errors)
    *   [인증](#authentication)
    *   [취소된 모델](#canceled-models)
*   [다음 단계](#what's-next)

퓨샷 프롬프팅과 같은 프롬프트 설계 전략은 필요한 결과를 항상 생성하는 것은 아닙니다. 모델 조정을 사용하여 특정 작업에서 모델의 성능을 개선하거나, 안내가 충분하지 않고 원하는 출력을 보여주는 일련의 예시가 있는 경우 모델이 특정 출력 요구사항을 준수하도록 할 수 있습니다.

이 페이지에서는 Gemini API 텍스트 서비스의 텍스트 모델을 조정하는 방법을 안내합니다.

**참고:** `gemini-1.5-flash` 조정이 곧 제공될 예정입니다.  
[Google AI Studio](https://ai.google.dev/gemini-api/docs/model-tuning/ai-studio?hl=ko), [Python SDK](https://ai.google.dev/gemini-api/docs/model-tuning/python?hl=ko) 또는 [REST API](https://ai.google.dev/gemini-api/docs/model-tuning/rest?hl=ko)를 사용하여 모델을 조정할 수 있습니다.

모델 조정의 원리
---------

모델 조정의 목표는 특정 태스크에 맞게 모델 성능을 추가로 향상시키는 것입니다. 모델 조정은 모델에 많은 태스크 예시가 포함된 학습 데이터 세트를 제공하는 방식으로 작동합니다. 틈새 태스크의 경우 적당한 예시 개수로 모델을 조정하여 모델 성능을 크게 향상시킬 수 있습니다.

학습 데이터는 프롬프트 입력과 예상 응답 출력이 포함된 예시로 구성되어야 합니다. Google AI Studio에서 직접 예시 데이터를 사용하여 모델을 조정할 수도 있습니다. 목표는 원하는 동작이나 작업을 보여주는 다양한 예를 제공하여 모델이 원하는 행동이나 작업을 모방하도록 학습시키는 것입니다.

조정 작업을 실행하면 모델은 원하는 작업을 수행하거나 원하는 동작을 학습하는 데 필요한 정보를 인코딩하는 데 도움이 되는 추가 매개변수를 학습합니다. 그런 후 이러한 매개변수를 추론 시점에 사용할 수 있습니다. 조정 작업의 출력은 새로 학습된 매개변수와 원래 모델의 사실상 조합인 새 모델입니다.

지원되는 모델
-------

다음 기반 모델은 모델 조정을 지원합니다. _싱글턴_ 텍스트 완성만 지원됩니다.

*   `gemini-1.0-pro-001`

Gemini 1.5 플래시의 조정 기능이 곧 제공될 예정입니다. [1.5 Flash의 기능 및 요금제](https://developers.googleblog.com/en/gemini-15-pro-and-15-flash-now-available/)에 관해 자세히 알아보세요.

모델 조정을 위한 워크플로
--------------

모델 조정 워크플로는 다음과 같습니다.

1.  데이터 세트를 준비합니다.
2.  Google AI Studio를 사용하는 경우 데이터 세트를 가져옵니다.
3.  조정 작업을 시작합니다.

모델 조정이 완료되면 조정된 모델의 이름이 표시됩니다. Google AI Studio에서 새 프롬프트를 만들 때 사용할 모델로 선택할 수도 있습니다.

데이터 세트 준비
---------

조정을 시작하려면 모델을 조정할 데이터 세트가 필요합니다. 최상의 성능을 위해서는 데이터 세트의 예시가 품질이 높고, 다양하며, 실제 입력과 출력을 나타내야 합니다.

### 형식

**참고:** 조정은 입력 / 출력 쌍 예시만 지원합니다. 채팅 스타일의 멀티턴 대화는 현재 지원되지 않습니다.

데이터 세트에 포함된 예시는 예상되는 프로덕션 트래픽과 일치해야 합니다. 데이터 세트에 특정 형식, 키워드, 안내 또는 정보가 포함된 경우 프로덕션 데이터의 형식이 동일한 방식으로 지정되어야 하며 동일한 안내를 포함해야 합니다.

예를 들어 데이터 세트의 예시에 `"question:"`과 `"context:"`가 포함된 경우 프로덕션 트래픽 형식 지정 시 `"question:"`과 `"context:"`가 데이터 세트 예시를 표시하는 것과 동일한 순서로 포함되어야 합니다. 컨텍스트를 제외하면 정확한 질문이 데이터 세트의 예시에 있더라도 모델이 패턴을 인식할 수 없습니다.

데이터 세트의 각 예시에 프롬프트 또는 프리앰블을 추가하면 조정된 모델의 성능을 개선할 수 있습니다. 프롬프트 또는 프리앰블이 데이터 세트에 포함된 경우 추론 시 조정된 모델에 대한 프롬프트에도 포함되어야 합니다.

### 학습 데이터 크기

20개 정도의 예시로 모델을 조정할 수 있으며, 데이터가 추가되면 일반적으로 응답 품질이 향상됩니다. 애플리케이션에 따라 100~500개의 예를 타겟팅해야 합니다. 다음 표는 다양한 일반적인 태스크에서 텍스트 모델을 조정할 때 권장되는 데이터 세트 크기를 보여줍니다.

| 작업 | 데이터 세트에 있는 예의 개수 |
| --- | --- |
| 분류 | 100+ |
| 요약 | 100-500+ |
| 문서 검색 | 100+ |

조정 데이터 세트 업로드
-------------

데이터는 API를 사용하여 인라인으로 전달되거나 Google AI Studio에 업로드된 파일을 통해 전달됩니다.

**가져오기** 버튼을 사용하여 파일에서 데이터를 가져오거나 조정 데이터 세트로 가져올 예시가 포함된 구조화된 프롬프트를 선택합니다.

#### 클라이언트 라이브러리

클라이언트 라이브러리를 사용하려면 `createTunedModel` 호출에 데이터 파일을 제공합니다. 파일 크기는 4MB로 제한됩니다. 시작하려면 [Python을 사용한 빠른 시작 조정](https://ai.google.dev/gemini-api/docs/model-tuning/python?hl=ko)을 참조하세요.

#### Curl

Curl을 사용하여 REST API를 호출하려면 `training_data` 인수에 JSON 형식의 학습 예시를 제공합니다. 시작하려면 [Curl을 사용한 빠른 시작 미세 조정](https://ai.google.dev/gemini-api/docs/model-tuning/rest?hl=ko)을 참조하세요.

고급 조정 설정
--------

조정 작업을 만들 때 다음과 같은 고급 설정을 지정할 수 있습니다.

*   **에포크** - 각 예시가 한 번씩 처리되도록 전체 학습 세트에 대한 전체 학습 패스입니다.
*   **배치 크기** - 한 번의 학습 [반복](https://developers.google.com/machine-learning/glossary?hl=ko#iteration)에 사용되는 예시의 집합입니다. 배치 크기에 따라 배치의 예 수가 결정됩니다.
*   **학습률** - 각 반복에서 모델 매개변수를 얼마나 강하게 조정할지 알고리즘에 알려주는 부동 소수점 수입니다. 예를 들어 학습률이 0.3이면 0.1의 학습률보다 3배 더 강력한 가중치와 편향이 조정됩니다. 높은 학습률과 낮은 학습률은 저마다 고유한 장단점이 있으며 사용 사례에 따라 조정해야 합니다.
*   **학습률 배율** - 비율 배율은 모델의 원래 학습률을 수정합니다. 값이 1이면 모델의 원래 학습률을 사용합니다 값이 1보다 크면 학습률이 높아지고 값이 1~0이면 학습률이 낮아집니다.

### 추천 구성

다음 표는 기반 모델을 조정하는 데 권장되는 구성을 보여줍니다.

| 초매개변수 | 기본값 | 권장 조정 |
| --- | --- | --- |
| 세대 | 5 | 손실이 5세대 이전에 정체되기 시작하면 더 작은 값을 사용합니다.  
손실이 수렴하고 있고 안정기처럼 보이지 않으면 더 높은 값을 사용합니다. |
| 배치 크기 | 4 |  |
| 학습률 | 0.001 | 데이터 세트가 작으면 더 작은 값을 사용하세요. |

손실 곡선은 각 에포크 후 모델의 예측이 학습 예시의 이상적인 예측에서 얼마나 벗어나는지 보여줍니다. 곡선의 정체 직전에 있는 가장 낮은 지점에서 학습을 중지하는 것이 이상적입니다. 예를 들어 아래 그래프는 약 에포크 4~6에 손실 곡선이 정체되어 있음을 보여줍니다. 즉, 에포크 매개변수를 4로 설정해도 동일한 성능을 유지할 수 있습니다.

![손실 곡선](https://ai.google.dev/static/docs/images/loss_curve.png?hl=ko)

조정 작업 상태 확인
-----------

Google AI Studio UI의 **내 라이브러리** 탭에서 또는 Gemini API에서 조정된 모델의 `metadata` 속성을 사용하여 조정 작업의 상태를 확인할 수 있습니다.

오류 문제 해결하기
----------

이 섹션에는 조정된 모델을 만드는 동안 발생할 수 있는 오류를 해결하는 방법에 대한 팁이 포함되어 있습니다.

### 인증

API 및 클라이언트 라이브러리를 사용하여 조정하려면 사용자 인증이 필요합니다. API 키만으로는 충분하지 않습니다. `'PermissionDenied: 403 Request had insufficient authentication scopes'` 오류가 표시되면 사용자 인증을 설정해야 합니다.

Python용 OAuth 사용자 인증 정보를 구성하려면 [OAuth 설정 가이드](https://ai.google.dev/gemini-api/docs/oauth?hl=ko)를 참조하세요.

### 취소된 모델

작업이 완료되기 전에 언제든지 모델 조정 작업을 취소할 수 있습니다. 하지만 취소된 모델의 추론 성능은 특히 학습 초기에 조정 작업이 취소된 경우 예측할 수 없습니다. 이전 에포크에서 학습을 중지하기 위해 학습을 취소한 경우 새 조정 작업을 만들고 이 에포크를 더 낮은 값으로 설정해야 합니다.

다음 단계
-----

*   [책임감 있는 AI 권장사항](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ko)에 대해 알아보세요.
*   [Python을 사용한 빠른 시작](https://ai.google.dev/gemini-api/docs/model-tuning/python?hl=ko) 또는 [Curl을 사용한 빠른 시작](https://ai.google.dev/gemini-api/docs/model-tuning/rest?hl=ko)으로 시작해 보세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-30(UTC)
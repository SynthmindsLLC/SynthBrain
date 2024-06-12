---
Please provide me with more context!  I need to know what kind of mission you're writing about in order to help you write it. 

For example: "* **What is the mission for?** Is it for a company, a non-profit organization, a team, or something else?"
* **What is the purpose of the mission?** What are the goals and objectives you want to achieve? 
* **What are the key values and principles that will guide the mission?** 
* **What is the target audience for the mission?** Who are you trying to reach with this statement? 

Once I have a better understanding of the context, I can offer you suggestions for writing a powerful and effective mission statement.
---

*   이 페이지의 내용
*   [어떤 경우에 비용이 청구되나요?](#what-am-i-billed-for)
*   [할당량은 어디에서 확인할 수 있나요?](#where-can-i-view-my-quota)
*   [GetToken은 요금이 청구되나요?](#is-gettokens-billed)
*   [무료 등급에서 100만 개의 토큰을 사용할 수 있나요?](#can-i-use-1m-tokens-for-free)
*   [사용 중인 토큰 수는 어떻게 계산하나요?](#count-tokens)
*   [결제는 어떻게 처리되나요?](#how-is-billing-handled)
*   [Cloud Billing을 사용 설정하려면 어떻게 해야 하나요?](#enable-cloud-billing)
*   [실패한 요청에 대해 요금이 부과되나요?](#am-i-charged-for-failed-requests)
*   [모델 미세 조정에는 비용이 드나요?](#is-fine-tuning-free)
*   [EEA (EU 포함), 영국, 스위스에서 Gemini API를 무료로 사용할 수 있나요?](#is-Gemini-free-in-EEA-UK-CH)
*   [Gemini API로 결제를 설정하면 Google AI Studio 사용량에 대한 요금이 청구되나요?](#is-AI-Studio-free)
*   [결제에 대한 도움말은 어디에서 얻을 수 있나요?](#get-help)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

Gemini API 결제 FAQ
=================

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [어떤 경우에 비용이 청구되나요?](#what-am-i-billed-for)
*   [할당량은 어디에서 확인할 수 있나요?](#where-can-i-view-my-quota)
*   [GetToken은 요금이 청구되나요?](#is-gettokens-billed)
*   [무료 등급에서 100만 개의 토큰을 사용할 수 있나요?](#can-i-use-1m-tokens-for-free)
*   [사용 중인 토큰 수는 어떻게 계산하나요?](#count-tokens)
*   [결제는 어떻게 처리되나요?](#how-is-billing-handled)
*   [Cloud Billing을 사용 설정하려면 어떻게 해야 하나요?](#enable-cloud-billing)
*   [실패한 요청에 대해 요금이 부과되나요?](#am-i-charged-for-failed-requests)
*   [모델 미세 조정에는 비용이 드나요?](#is-fine-tuning-free)
*   [EEA (EU 포함), 영국, 스위스에서 Gemini API를 무료로 사용할 수 있나요?](#is-Gemini-free-in-EEA-UK-CH)
*   [Gemini API로 결제를 설정하면 Google AI Studio 사용량에 대한 요금이 청구되나요?](#is-AI-Studio-free)
*   [결제에 대한 도움말은 어디에서 얻을 수 있나요?](#get-help)

이 페이지에서는 Gemini API 결제와 관련하여 자주 묻는 질문(FAQ)의 답변을 제공합니다. 가격 정보는 [가격 페이지](https://ai.google.dev/pricing?hl=ko)를 참조하세요. 법률 조항은 [서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko#paid-services)을 참조하세요.

어떤 경우에 비용이 청구되나요?
-----------------

Gemini API 가격은 총 토큰 수를 기준으로 책정되며 입력 토큰과 출력 토큰의 가격은 다릅니다. 가격 정보는 [가격 책정 페이지](https://ai.google.dev/pricing?hl=ko)를 참조하세요.

할당량은 어디에서 확인할 수 있나요?
--------------------

[Google Cloud 콘솔](https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas?hl=ko)에서 할당량 및 시스템 한도를 확인할 수 있습니다.

GetToken은 요금이 청구되나요?
--------------------

GetTokens API에 대한 요청은 요금이 청구되지 않으며 추론 할당량에 포함되지 않습니다.

무료 등급에서 100만 개의 토큰을 사용할 수 있나요?
------------------------------

Gemini API의 무료 등급은 선택한 모델에 따라 다릅니다. 지금은 다음과 같은 방법으로 1M 토큰 환경설정 기간을 사용해 볼 수 있습니다.

*   Google AI Studio에서
*   사용한 만큼만 지불하는 요금제 사용
*   일부 모델은 무료 요금제 제공

모델별 최신 무료 요율 한도는 [가격 책정 페이지](https://ai.google.dev/pricing?hl=ko)에서 확인하세요.

사용 중인 토큰 수는 어떻게 계산하나요?
----------------------

토큰 수를 집계하려면 [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko#count_tokens) 메서드를 사용합니다. 토큰에 대한 자세한 내용은 [토큰 가이드](https://ai.google.dev/gemini-api/docs/tokens?hl=ko)를 참조하세요.

결제는 어떻게 처리되나요?
--------------

Gemini API 결제는 [Cloud Billing](https://cloud.google.com/billing/docs/concepts?hl=ko) 시스템에서 처리됩니다.

Cloud Billing을 사용 설정하려면 어떻게 해야 하나요?
-----------------------------------

Google AI Studio에서 Cloud Billing을 사용 설정할 수 있습니다.

1.  [Google AI 스튜디오](https://aistudio.google.com/?hl=ko)를 엽니다.
    
2.  왼쪽 사이드바 하단의 **설정**으로 이동합니다.
    
3.  **계정 설정**에서 **계획 정보**를 클릭합니다.
    
    계정에 연결된 Google Cloud 프로젝트가 나열됩니다.
    
4.  선택한 프로젝트의 **결제 설정**을 클릭하여 Cloud Billing을 사용 설정합니다.
    

실패한 요청에 대해 요금이 부과되나요?
---------------------

400 또는 500 오류로 요청이 실패하면 사용된 토큰에 대한 비용이 청구되지 않습니다.

모델 미세 조정에는 비용이 드나요?
-------------------

[모델 조정](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ko)은 무료이지만 조정된 모델에 대한 추론은 기본 모델과 동일한 요율로 청구됩니다.

EEA (EU 포함), 영국, 스위스에서 Gemini API를 무료로 사용할 수 있나요?
-------------------------------------------------

API를 통해 사용할 수 있는 모델은 두 가지입니다.

1.  Gemini 1.5 Flash, Gemini 1.5 Pro, Gemini 1.0 Pro가 포함된 유료 모델입니다. 이러한 모델에는 EEA (EU 포함), 영국, 스위스에서는 무료 등급이 제공되지 않습니다. 개발자는 결제 계정을 설정하고 사용 요금을 지불하는 데 필요한 단계를 거쳐야 합니다.
2.  일부 모델은 Gemini API에서 무료로 액세스할 수 있습니다. (요금이 청구되는 모델에 대한 자세한 내용은 [ai.google.dev/pricing](https://ai.google.dev/pricing?hl=ko)을 참조하세요. 다른 모델은 무료입니다). 하지만 이러한 모델을 사용하려면 결제 계정을 설정해야 합니다.

Gemini API로 결제를 설정하면 Google AI Studio 사용량에 대한 요금이 청구되나요?
--------------------------------------------------------

아니요. Google AI Studio는 결제 설정 여부와 관계없이 무료로 제공됩니다.

결제에 대한 도움말은 어디에서 얻을 수 있나요?
--------------------------

결제에 대해 도움이 필요하면 [Cloud Billing 지원 받기](https://cloud.google.com/support/billing?hl=ko)를 참조하세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-31(UTC)
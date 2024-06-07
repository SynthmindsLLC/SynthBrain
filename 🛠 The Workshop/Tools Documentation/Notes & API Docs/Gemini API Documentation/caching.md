*   이 페이지의 내용
*   [컨텍스트 캐싱을 사용해야 하는 경우](#when-to-use-caching)
*   [캐싱을 통한 비용 효율성](#cost-efficiency)
*   [곧 컨텍스트 캐싱 시작하기](#get-started)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

컨텍스트 캐싱 가이드
===========

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [컨텍스트 캐싱을 사용해야 하는 경우](#when-to-use-caching)
*   [캐싱을 통한 비용 효율성](#cost-efficiency)
*   [곧 컨텍스트 캐싱 시작하기](#get-started)

Gemini API 컨텍스트 캐싱 기능은 입력 토큰 수가 많은 반복 콘텐츠가 포함된 요청의 비용을 절감하도록 설계되었습니다.

컨텍스트 캐싱을 사용해야 하는 경우
-------------------

컨텍스트 캐싱은 특히 짧은 요청에서 상당한 초기 컨텍스트를 반복적으로 참조하는 시나리오에 적합합니다. 다음과 같은 사용 사례에 컨텍스트 캐싱을 사용하는 것이 좋습니다.

*   광범위한 시스템 지침을 제공하는 챗봇
*   긴 동영상 파일의 반복적인 분석
*   대규모 문서 세트에 대한 반복 쿼리
*   빈번한 코드 저장소 분석 또는 버그 수정

캐싱을 통한 비용 효율성
-------------

컨텍스트 캐싱은 전반적인 운영 비용을 절감하도록 설계된 유료 기능입니다. 결제는 다음 요소를 기준으로 합니다.

1.  **캐시 토큰 수:** 캐시된 입력 토큰 수. 이후 프롬프트에 포함되는 경우 더 낮은 요율로 청구됩니다.
2.  **저장 기간:** 캐시된 토큰이 저장된 시간이며, 시간 단위로 청구됩니다.
3.  **기타 요인:** 캐시되지 않은 입력 토큰 및 출력 토큰 등의 기타 요금이 적용됩니다.

최신 가격 세부정보는 Gemini API [가격 책정 페이지](https://ai.google.dev/pricing?hl=ko)를 참조하세요. 토큰을 계산하는 방법은 [토큰](https://ai.google.dev/gemini-api/docs/tokens?hl=ko)을 참조하세요.

곧 컨텍스트 캐싱 시작하기
--------------

기술 문서 및 SDK 지원과 함께 컨텍스트 캐싱이 곧 출시될 예정입니다.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-30(UTC)
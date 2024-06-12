---
Please provide me with more context!  What kind of mission are you talking about? I need more information to help you write a good mission statement. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a team, a personal goal?"
* **What are the goals of this mission?** What are you trying to achieve?
* **What are the values that will guide the mission?** What principles are important to you?

Once I have a better understanding of your needs, I can help you write a strong and compelling mission statement!
---

*   이 페이지의 내용
*   [기본 요건](#prerequisites)
*   [사전 체험판 앱 사용 설정하기](#turn-on-early-access)
*   [문제 해결](#troubleshooting)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

Workspace 계정으로 Google AI 스튜디오에 액세스
==================================

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [기본 요건](#prerequisites)
*   [사전 체험판 앱 사용 설정하기](#turn-on-early-access)
*   [문제 해결](#troubleshooting)

이 페이지에서는 조직의 Google Workspace 사용자가 Google AI Studio를 사용 설정하는 방법을 설명합니다. Workspace 계정으로 Google AI Studio에 액세스하는 데 문제가 있는 경우 [문제 해결](#troubleshooting)을 참조하세요.

기본 요건
-----

현재 계정에 이 단계를 수행할 권한이 없을 수 있습니다. 계속하려면 _관리자 계정_에 로그인했는지 확인하세요. [자세히 알아보기](https://support.google.com/a/answer/182076?hl=ko)

관리자는 어떤 사용자가 사전 체험판 앱을 사용할 수 있는지 관리할 수 있습니다.

*   사전 체험판 앱은 모든 버전에서 기본적으로 사용 중지되어 있습니다.
*   이 설정을 사용하면 모든 사전 체험판 앱을 사용 또는 사용 중지할 수 있습니다. 개별 앱을 개별적으로 사용 또는 사용 중지할 수는 없습니다.
*   Google Workspace for Education 버전: 만 18세 미만의 사용자는 Google Workspace for Education 계정으로 사전 체험판 앱을 사용할 수 없습니다. 사전 체험판 앱이 사용 설정된 경우에도 마찬가지입니다. 자세한 내용은 [연령별로 Google 서비스에 대한 액세스 권한 관리하기](https://support.google.com/a/answer/10651918?hl=ko)를 참고하세요.
*   핵심 서비스에 대한 사전 체험판 앱 액세스도 기본적으로 사용 중지되어 있습니다.

사전 체험판 앱 사용 설정하기
----------------

특정 사용자에게 설정을 적용하려면 해당 사용자의 계정을 [조직 단위](https://support.google.com/a/answer/182433?hl=ko)(부서별로 설정하려는 경우) 또는 [구성 적용 그룹](https://support.google.com/a/answer/9224126?hl=ko)(여러 부서 간 또는 부서 내 사용자에 대해 설정하려는 경우)에 추가하세요.

1.  작업공간 **관리** 콘솔에서 **메뉴** -> **앱** -> **추가 Google 서비스**로 이동합니다.
2.  모든 서비스 목록에서 **사전 체험판 앱**으로 스크롤하여 클릭합니다. 사전 체험판 앱 설정 페이지가 열립니다.
3.  사전 체험판 앱 설정 페이지에서 **서비스 상태**를 클릭합니다.
4.  서비스를 사용 또는 사용 중지하려면 **사용** 또는 **사용 중지**를 선택한 다음 **저장**을 클릭합니다.
5.  조직 또는 조직 내 그룹에 대해 서비스를 사용 설정하거나 중지하려면 [지원 문서](https://support.google.com/a/answer/13515709?hl=ko)의 세부 단계를 참조하세요.

문제 해결
-----

다음과 유사한 오류가 표시되는 경우:

`We are sorry, but you do not have access to Google AI Studio. Please contact your Organization Administrator for access.`

Workspace 계정을 사용하여 Google AI Studio에 액세스하려는 경우 해당 계정에서 사전 체험판 앱을 사용 설정해야 할 수 있습니다.

Google AI Studio는 사전 체험판 앱입니다. 사전 체험판 앱은 Google팀에서 개발한 서비스 및 제품입니다. [사전 체험판 앱 지원 설정 페이지](https://support.google.com/a/answer/13515709?hl=ko)에서 사전 체험판 앱에 관해 자세히 알아보세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-04-18(UTC)
*   이 페이지의 내용
*   [임베딩이란 무엇인가요?](#what-are-embeddings)
*   [사용 사례](#use-cases)
*   [탄력적 임베딩](#elastic-embedding)
*   [다음 단계](#whats-next)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

임베딩 가이드
=======

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [임베딩이란 무엇인가요?](#what-are-embeddings)
*   [사용 사례](#use-cases)
*   [탄력적 임베딩](#elastic-embedding)
*   [다음 단계](#whats-next)

Gemini API의 임베딩 서비스는 단어, 구문, 문장에 대한 최첨단 임베딩을 생성합니다. 이렇게 생성된 임베딩은 시맨틱 검색, 텍스트 분류, 클러스터링과 같은 여러 개의 NLP 작업에 사용할 수 있습니다. 이 페이지에서는 임베딩에 대해 설명하고 시작하는 데 도움이 되는 임베딩 서비스의 주요 사용 사례를 소개합니다.

임베딩이란 무엇인가요?
------------

텍스트 임베딩은 텍스트를 숫자 벡터로 변환하는 자연어 처리 (NLP) 기술입니다. 임베딩은 의미론적 의미와 컨텍스트를 캡처하므로 의미가 비슷한 텍스트가 더 가까운 임베딩을 갖습니다. 예를 들어 '내 강아지를 수의사에게 데려갔습니다'와 '내 고양이를 수의사에게 데려갔습니다'라는 문장은 비슷한 컨텍스트를 설명하므로 벡터 공간에서 서로 가까운 임베딩을 갖게 됩니다.

이것이 중요한 이유는 텍스트에서 직접 작동할 수 없지만 벡터에서는 작동할 수 있는 많은 알고리즘을 잠금 해제하기 때문입니다.

이러한 임베딩 또는 벡터를 사용하여 서로 다른 텍스트를 비교하고 어떻게 연관되는지 파악할 수 있습니다. 예를 들어 'cat'과 'dog'라는 텍스트의 임베딩이 서로 가까이 있으면 두 단어의 의미나 문맥 또는 둘 다 유사하다고 추론할 수 있습니다. 이 기능을 사용하면 다음 섹션에서 설명하는 다양한 사용 사례를 사용할 수 있습니다.

사용 사례
-----

텍스트 임베딩은 다양한 NLP 사용 사례를 지원합니다. 예를 들면 다음과 같습니다.

*   정보 검색: 목표는 입력 텍스트에서 의미론적으로 유사한 텍스트를 검색하는 것입니다. 시맨틱 검색, 질문 답변, 요약과 같은 정보 검색 시스템에서 다양한 애플리케이션을 지원할 수 있습니다. 예시는 [문서 검색 노트북](https://ai.google.dev/gemini-api/tutorials/document_search?hl=ko)을 참조하세요.
*   분류: 임베딩을 사용하면 문서를 카테고리로 분류하도록 모델을 학습시킬 수 있습니다. 예를 들어 사용자 댓글을 음성 또는 양성으로 분류하려면 임베딩 서비스를 사용해 각 댓글의 벡터 표현을 가져와 분류기를 학습시킬 수 있습니다. 자세한 내용은 [Gemini 분류기 예](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=ko)를 참고하세요.
*   클러스터링: 텍스트 벡터를 비교하면 텍스트 벡터가 얼마나 비슷하거나 다른지 보여줄 수 있습니다. 이 기능은 [유사한 텍스트 또는 문서를 함께 그룹화하는 클러스터링 모델을 학습](https://ai.google.dev/examples/clustering_with_embeddings?hl=ko)시키고 [데이터의 이상을 감지](https://ai.google.dev/examples/anomaly_detection?hl=ko)하는 데 사용할 수 있습니다.
*   벡터 DB: 생성된 임베딩을 벡터 DB에 저장하여 NLP 애플리케이션의 정확성과 효율성을 개선할 수 있습니다. [벡터 DB를 사용하여 텍스트 프롬프트를 숫자 벡터로 변환](https://cloud.google.com/alloydb/docs/ai/work-with-embeddings?hl=ko)하는 방법을 알아보려면 이 페이지를 참조하세요.

탄력적 임베딩
-------

`text-embedding-004`로 시작하는 [Gemini 텍스트 임베딩 모델](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#text-embedding)은 768 미만의 탄력적 임베딩 크기를 제공합니다. 탄력적 임베딩을 사용하면 출력 차원을 더 작게 생성하고, 약간의 성능 손실로 컴퓨팅 및 스토리지 비용을 절감할 수 있습니다.

다음 단계
-----

*   개발을 시작할 준비가 되었다면 [Python](https://ai.google.dev/tutorials/python_quickstart?hl=ko#use_embeddings), [Go](https://ai.google.dev/tutorials/go_quickstart?hl=ko#embeddings), [Node.js](https://ai.google.dev/tutorials/node_quickstart?hl=ko#embeddings), [Dart (Flutter)](https://ai.google.dev/tutorials/dart_quickstart?hl=ko#embeddings)의 빠른 시작에서 완전한 실행 가능한 코드를 찾을 수 있습니다.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-14(UTC)
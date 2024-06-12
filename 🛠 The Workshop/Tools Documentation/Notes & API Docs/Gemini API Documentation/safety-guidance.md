---
Please provide me with the rest of the mission statement. I need more context to understand what you're trying to achieve. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a personal goal, etc.?"
* **What are the key values or objectives?** What do you want to accomplish? 
* **What makes this mission unique or important?**

Once I have more information, I can help you complete the mission statement and make it powerful and impactful.
---

*   이 페이지의 내용
*   [애플리케이션의 안전 위험 이해](#understand_the_safety_risks_of_your_application)
*   [안전 위험 완화를 위한 조정 고려](#consider_adjustments_to_mitigate_safety_risks)
*   [사용 사례에 적합한 안전 테스트 수행](#perform_safety_testing_appropriate_to_your_use_case)
*   [문제 모니터링](#monitor_for_problems)
*   [다음 단계](#next_steps)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

안전 안내
=====

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [애플리케이션의 안전 위험 이해](#understand_the_safety_risks_of_your_application)
*   [안전 위험 완화를 위한 조정 고려](#consider_adjustments_to_mitigate_safety_risks)
*   [사용 사례에 적합한 안전 테스트 수행](#perform_safety_testing_appropriate_to_your_use_case)
*   [문제 모니터링](#monitor_for_problems)
*   [다음 단계](#next_steps)

대규모 언어 모델 (LLM)이 유용한 이유 중 하나는 다양한 언어 작업을 처리할 수 있는 창의적인 도구라는 점입니다. 하지만 이는 대규모 언어 모델이 불쾌감을 주거나, 민감하지 않거나, 사실과 다른 텍스트를 포함하여 예상하지 못한 출력을 생성할 수도 있음을 의미합니다. 게다가 이러한 모델의 탁월한 다목적성으로 인해 정확히 어떤 종류의 바람직하지 않은 출력을 생성할지 예측하기가 어렵습니다. Gemini API는 [Google의 AI 원칙](https://ai.google/principles/?hl=ko)을 염두에 두고 설계되었지만 이러한 모델을 책임감 있게 적용할 책임은 개발자에게 있습니다. 개발자가 안전하고 책임감 있는 애플리케이션을 만들 수 있도록 Gemini API에는 콘텐츠 필터링과 피해의 4가지 차원에 조정 가능한 안전 설정이 내장되어 있습니다. 자세한 내용은 [안전 설정](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ko) 가이드를 참고하세요.

이 문서에서는 LLM을 사용할 때 발생할 수 있는 몇 가지 안전 위험을 소개하고 새로운 안전 설계 및 개발 권장사항을 권장합니다. 법률 및 규정에도 제한사항이 있을 수 있지만 이러한 고려사항은 이 가이드에서 다루지 않습니다.

LLM으로 애플리케이션을 빌드하는 경우 다음 단계를 따르는 것이 좋습니다.

*   애플리케이션의 안전 위험 이해
*   안전 위험 완화를 위한 조정 고려
*   사용 사례에 적합한 안전 테스트 수행
*   사용자 의견 요청 및 사용 모니터링

조정 및 테스트 단계는 애플리케이션에 적합한 성능에 도달할 때까지 반복되어야 합니다.

![모델 구현 주기](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=ko)

애플리케이션의 안전 위험 이해
----------------

여기에서 안전성은 LLM이 악의적인 언어 또는 고정관념을 조장하는 콘텐츠를 생성하는 등의 방법으로 사용자에게 해를 입히지 않는 능력으로 정의됩니다. Gemini API를 통해 제공되는 모델은 [Google의 AI 원칙](https://ai.google/principles/?hl=ko)을 염두에 두고 설계되었으며 사용 시 [생성형 AI 금지된 사용 정책](https://policies.google.com/terms/generative-ai/use-policy?hl=ko)이 적용됩니다. 이 API는 악의적인 표현 및 증오심 표현과 같은 몇 가지 일반적인 언어 모델 문제를 해결하고 포용성과 고정 관념을 피하기 위해 노력하는 데 도움이 되는 안전 필터를 기본 제공합니다. 그러나 각 애플리케이션은 사용자에게 서로 다른 위험을 초래할 수 있습니다. 따라서 애플리케이션 소유자는 사용자 및 애플리케이션으로 인해 발생할 수 있는 잠재적인 피해를 파악하고 애플리케이션이 LLM을 안전하고 책임감 있게 사용하도록 할 책임이 있습니다.

이 평가의 일부로 피해가 발생할 가능성을 고려하고 그 심각성과 완화 조치를 판단해야 합니다. 예를 들어 사실에 기반한 사건을 기반으로 에세이를 생성하는 앱은 엔터테인먼트를 위해 가상의 이야기를 생성하는 앱에 비해 잘못된 정보를 방지하는 데 더 주의해야 합니다. 잠재적인 안전 위험을 살펴보기 위한 좋은 방법은 최종 사용자와 애플리케이션 결과의 영향을 받을 수 있는 다른 사용자를 연구하는 것입니다. 이러한 활동에는 앱 도메인의 최신 연구 조사, 유사한 앱 사용 방식 관찰, 사용자 연구나 설문조사 진행, 잠재 사용자와 비공식 인터뷰 실시 등 다양한 형태가 있을 수 있습니다.

#### 고급 도움말

*   잠재적 위험에 대한 더 넓은 관점을 얻고 필요에 따라 다양성 기준을 조정할 수 있도록 타겟 집단 내의 다양한 잠재 사용자와 애플리케이션 및 의도된 목적에 대해 논의합니다.
*   미국 정부의 국립 표준 기술 연구소 (NIST)에서 발표한 [AI 위험 관리 프레임워크](https://www.nist.gov/itl/ai-risk-management-framework)는 AI 위험 관리를 위한 보다 자세한 지침과 추가 학습 리소스를 제공합니다.
*   [언어 모델로 인한 피해의 윤리적, 사회적 위험](https://arxiv.org/abs/2112.04359) 에 대한 DeepMind의 간행물에서는 언어 모델 애플리케이션이 피해를 유발할 수 있는 방식을 자세히 설명합니다.

안전 위험 완화를 위한 조정 고려
------------------

위험을 이해했으니 이제 위험을 완화하는 방법을 결정할 수 있습니다. 소프트웨어 프로젝트에서 버그를 선별하는 것과 마찬가지로 우선순위를 부여할 위험과 이러한 위험을 방지하기 위해 해야 할 일을 결정하는 것은 중요한 결정입니다. 우선순위를 결정했으면 가장 적절한 완화 유형에 대해 생각해 볼 수 있습니다. 종종 사소한 변화가 차이를 이루고 위험을 줄일 수 있습니다.

예를 들어 애플리케이션을 설계할 때 다음을 고려하세요.

*   애플리케이션 컨텍스트에서 허용되는 값을 더 잘 반영하도록 **모델 출력 조정** 조정은 모델의 출력을 예측 가능하고 일관성 있게 만들 수 있으므로 특정 위험을 완화하는 데 도움이 될 수 있습니다.
*   **더 안전한 출력을 위한 입력 방법 제공** LLM에 제공하는 정확한 입력에 따라 출력 품질이 달라질 수 있습니다. 사용 사례에서 가장 안전하게 작동하는 것을 찾기 위해 입력 프롬프트를 실험하는 것은 노력할 만한 가치가 있습니다. 그런 다음 이를 용이하게 하는 UX를 제공할 수 있기 때문입니다. 예를 들어 사용자가 입력 프롬프트의 드롭다운 목록에서만 선택하도록 제한하거나 애플리케이션 컨텍스트에서 안전하게 수행된 것으로 확인된 설명 문구와 함께 팝업 추천을 제공할 수 있습니다.
*   **안전하지 않은 입력 차단 및 출력 필터링: 사용자에게 표시되기 전에 차단.** 간단한 상황에서 차단 목록은 프롬프트나 대답에서 안전하지 않은 단어나 문구를 식별 및 차단하거나, 검토자가 이러한 콘텐츠를 수동으로 변경 또는 차단하도록 할 수 있습니다.
    
    **참고:** 정적 목록을 기반으로 한 자동 차단은 차단 목록에서 일반적으로 어휘를 사용하는 특정 그룹을 타겟팅하는 등 의도하지 않은 결과를 초래할 수 있습니다.
    
*   **학습된 분류기를 사용하여 각 프롬프트에 잠재적 피해 또는 적대적 신호로 라벨을 지정합니다.** 그런 다음 감지된 피해 유형에 따라 다양한 전략을 사용하여 요청을 처리할 수 있습니다. 예를 들어 입력이 과도하게 적대적이거나 악의적인 경우라면 차단되고 대신 사전 스크립트로 작성된 응답을 출력할 수 있습니다.
    
    #### 고급 팁
    
    *   신호가 유해한 출력을 판단하는 경우 애플리케이션은 다음 옵션을 사용할 수 있습니다.
        *   오류 메시지 또는 사전 스크립트화된 출력을 제공합니다.
        *   안전한 대체 출력이 생성되면 프롬프트를 다시 시도해 보세요. 동일한 프롬프트가 다른 출력을 생성하는 경우도 있기 때문입니다.
    
*   **고의적인 오용을 방지하기 위한 보호 장치를 마련**합니다. 예를 들어 각 사용자에게 고유 ID를 할당하고 지정된 기간 동안 제출할 수 있는 사용자 쿼리의 양을 제한합니다. 또 다른 보호 방법은 프롬프트 삽입을 방지하여 보호하는 것입니다 프롬프트 삽입은 SQL 삽입과 마찬가지로 악의적인 사용자가 모델의 출력을 조작하는 입력 프롬프트를 설계하는 방법입니다. 예를 들어 모델이 이전 예시를 무시하도록 지시하는 입력 프롬프트를 전송할 수 있습니다. 고의적인 오용에 대한 자세한 내용은 [생성형 AI 금지된 사용 정책](https://policies.google.com/terms/generative-ai/use-policy?hl=ko)을 참조하세요.
    
*   **본질적으로 위험이 낮은 기능에 맞게 기능 조정** 범위가 더 좁거나 (예: 텍스트 문구에서 키워드 추출) 사람의 감독이 더 큰 작업 (예: 사람이 검토할 짧은 형식의 콘텐츠 생성)은 위험성이 낮은 경우가 많습니다. 예를 들어 처음부터 이메일 답장을 작성하는 애플리케이션을 만드는 대신 개요를 확장하거나 대체 문구를 제안하도록 애플리케이션을 제한할 수 있습니다.
    

사용 사례에 적합한 안전 테스트 수행
--------------------

테스트는 강력하고 안전한 애플리케이션을 빌드하는 핵심 부분이지만 테스트의 범위와 범위, 전략은 다를 수 있습니다. 예를 들어 단순한 하이쿠 생성기는 법률 회사에서 법률 문서를 요약하고 계약서 초안을 작성하는 데 사용하도록 설계된 애플리케이션보다 덜 심각한 위험을 초래할 수 있습니다. 그러나 하이쿠 생성기는 더 다양한 사용자가 사용할 수 있으므로 적대적 시도나 의도치 않은 유해한 입력의 가능성이 더 커질 수 있습니다. 구현 상황도 중요합니다. 예를 들어, 조치를 취하기 전에 전문가가 결과를 검토한 애플리케이션은 이러한 감독 없이 동일한 애플리케이션보다 유해한 출력을 생성할 가능성이 낮다고 간주될 수 있습니다.

비교적 위험이 낮은 애플리케이션일지라도 출시 준비가 되었다는 확신을 얻기 전에 변경 및 테스트를 여러 번 반복하는 것은 드문 일이 아닙니다. 두 가지 종류의 테스트가 특히 AI 애플리케이션에 유용합니다

*   **안전 벤치마킹**에는 애플리케이션 사용 가능성 측면에서 애플리케이션이 안전하지 않을 수 있는 방식을 반영하는 안전성 측정항목을 설계한 다음 평가 데이터 세트를 사용하여 측정항목에서 애플리케이션의 성능을 테스트하는 작업이 포함됩니다. 1) 이러한 기대치에 따라 테스트 결과를 평가하고 2) 가장 중요한 측정항목을 평가하는 테스트를 기반으로 평가 데이터 세트를 수집할 수 있도록 테스트하기 전에 허용 가능한 최소 수준의 안전성 측정항목을 고려하는 것이 좋습니다.
    
    #### 고급 도움말
    
    *   애플리케이션의 맥락에 완전히 맞출 수 있도록 수동 평가자를 통해 자체 테스트 데이터 세트를 구축해야 할 수 있으므로 '즉시 사용 가능'한 접근 방식에 너무 의존하지 않도록 주의하세요.
    *   측정항목이 2개 이상인 경우, 한 측정항목이 개선되면 다른 측정항목에 부정적인 영향을 미칠 경우 어떻게 균형을 유지할지 결정해야 합니다. 다른 성능 엔지니어링과 마찬가지로 평균 성능보다는 평가 세트 전체에서 최악의 성능에 집중하는 것이 좋습니다.
    
*   **적대적 테스트**에는 애플리케이션을 중단하려는 시도가 포함됩니다. 목표는 취약점을 파악하여 적절한 조치를 취할 수 있도록 하는 것입니다. 공격자 테스트에는 애플리케이션에 대한 전문 지식을 갖춘 평가자가 상당한 시간과 노력을 들일 수 있습니다. 하지만 더 많이 수행할수록 문제를 발견하게 될 가능성이 커집니다. 특히 애플리케이션을 반복적으로 실행한 후에만 또는 거의 발생하지 않는 테스트에는 더욱 그렇습니다.
    
    *   적대적 테스트는 ML 모델이 악의적이거나 의도치 않게 유해한 입력이 제공되었을 때 어떻게 동작하는지 학습하기 위해 ML 모델을 체계적으로 평가하는 방법입니다.
        *   안전하지 않거나 유해한 출력을 생성하는 것이 명백한 입력은 악성일 수 있습니다. 예를 들어 텍스트 생성 모델에 특정 종교에 대한 혐오 발언을 하도록 요청하는 경우가 있습니다.
        *   입력 자체가 무해할 수 있지만 유해한 출력을 생성하는 경우 입력은 의도치 않게 유해합니다. 예를 들어 텍스트 생성 모델에 특정 민족을 설명하도록 요청하고 인종차별적인 출력을 받는 경우입니다.
    *   적대적 테스트와 표준 평가의 차이점은 테스트에 사용되는 데이터의 구성입니다. 적대적 테스트의 경우 모델에서 문제가 되는 출력을 도출할 가능성이 가장 높은 테스트 데이터를 선택합니다. 즉, 드물거나 흔하지 않은 예와 안전 정책과 관련된 극단적인 사례를 비롯하여 가능한 모든 유형의 유해한 결과에 대해 모델의 동작을 프로브해야 합니다. 또한 구조, 의미, 길이와 같은 문장의 다양한 차원의 다양성을 포함해야 합니다. 테스트 데이터 세트를 빌드할 때 고려해야 할 사항에 대한 자세한 내용은 [Google의 책임감 있는 AI 공정성 관행](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=ko)을 참조하세요.
        
        #### 고급 도움말
        
        *   '레드팀'에 합류하여 애플리케이션을 중단시키는 기존의 방법 대신 [자동 테스트](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models)를 사용합니다. 자동화된 테스트에서 '레드팀'은 테스트 중인 모델에서 유해한 출력을 생성하는 입력 텍스트를 찾는 또 다른 언어 모델입니다.
        
    
    **참고:** LLM은 때때로 동일한 입력 프롬프트에 대해 다른 출력을 생성하는 것으로 알려져 있습니다. 문제가 있는 출력을 더 많이 포착하려면 테스트를 여러 번 거쳐야 할 수 있습니다.
    

문제 모니터링
-------

아무리 많이 테스트하고 완화해도 완벽을 보장할 수는 없으므로 발생하는 문제를 어떻게 발견하고 처리할 것인지 미리 계획해야 합니다. 일반적인 방법으로는 사용자가 의견을 공유할 수 있도록 모니터링 채널을 설정하고(예: 좋아요/싫어요 평가) 사용자 연구를 실행하여 다양한 사용자로부터 사전에 의견을 얻는 방법이 있습니다. 이는 사용 패턴이 기대와 다른 경우 특히 유용합니다.

#### 고급 도움말

*   사용자가 AI 제품에 의견을 제공하면 예를 들어 프롬프트 조정에 더 나은 예시를 선택할 수 있도록 지원하여 시간이 지남에 따라 AI 성능과 사용자 환경을 크게 개선할 수 있습니다. [Google 인력 및 AI 가이드북](https://pair.withgoogle.com/guidebook/chapters)의 [피드백 및 통제 챕터](https://pair.withgoogle.com/chapter/feedback-controls/)에서는 피드백 메커니즘을 설계할 때 고려해야 할 주요 고려사항을 중점적으로 설명합니다.

다음 단계
-----

*   Gemini API를 통해 제공되는 조정 가능한 안전 설정에 관한 자세한 내용은 [안전 설정](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ko) 가이드를 참고하세요.
*   첫 번째 프롬프트 작성을 시작하려면 [프롬프트 소개](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ko)를 참고하세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-21(UTC)
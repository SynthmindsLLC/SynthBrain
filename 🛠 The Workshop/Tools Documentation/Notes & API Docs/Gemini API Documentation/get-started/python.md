*   이 페이지의 내용
*   [기본 요건](#prerequisites)
*   [설정](#setup)
    *   [Python SDK 설치](#install_the_python_sdk)
    *   [패키지 가져오기](#import_packages)
    *   [API 키 설정](#setup_your_api_key)
*   [모델 나열](#list_models)
*   [텍스트 입력에서 텍스트 생성](#generate_text_from_text_inputs)
*   [이미지 및 텍스트 입력에서 텍스트 생성](#generate_text_from_image_and_text_inputs)
*   [채팅 대화](#chat_conversations)
*   [토큰 개수](#count_tokens)
*   [임베딩 사용](#use_embeddings)
*   [고급 사용 사례](#advanced_use_cases)
    *   [안전 설정](#safety_settings)
    *   [메시지 인코딩](#encode_messages)
    *   [멀티턴 대화](#multi-turn_conversations)
    *   [생성 구성](#generation_configuration)
*   [다음 단계](#whats_next)

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
*   [기본 요건](#prerequisites)
*   [설정](#setup)
    *   [Python SDK 설치](#install_the_python_sdk)
    *   [패키지 가져오기](#import_packages)
    *   [API 키 설정](#setup_your_api_key)
*   [모델 나열](#list_models)
*   [텍스트 입력에서 텍스트 생성](#generate_text_from_text_inputs)
*   [이미지 및 텍스트 입력에서 텍스트 생성](#generate_text_from_image_and_text_inputs)
*   [채팅 대화](#chat_conversations)
*   [토큰 개수](#count_tokens)
*   [임베딩 사용](#use_embeddings)
*   [고급 사용 사례](#advanced_use_cases)
    *   [안전 설정](#safety_settings)
    *   [메시지 인코딩](#encode_messages)
    *   [멀티턴 대화](#multi-turn_conversations)
    *   [생성 구성](#generation_configuration)
*   [다음 단계](#whats_next)

Python Node.js 웹 REST Go Dart (Flutter) Android Swift

  

<table align="left" class="tfo-notebook-buttons"><tbody><tr><td><a href="https://ai.google.dev/gemini-api/docs/get-started/python?hl=ko" target="_blank"><img height="32" src="https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png?hl=ko" width="32">Google AI에서 보기</a></td><td><a href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb?hl=ko" target="_blank"><img src="https://www.tensorflow.org/images/colab_logo_32px.png?hl=ko">Google Colab에서 실행</a></td><td><a href="https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb" target="_blank"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=ko">GitHub에서 소스 보기</a></td></tr></tbody></table>

이 빠른 시작에서는 Google의 Gemini 대규모 언어 모델에 액세스할 수 있는 Gemini API용 Python SDK를 사용하는 방법을 보여줍니다. 이 빠른 시작에서는 다음과 같은 방법을 학습합니다.

1.  Gemini를 사용하려면 개발 환경 및 API 액세스를 설정합니다.
2.  텍스트 입력에서 텍스트 응답을 생성합니다.
3.  멀티모달 입력 (텍스트 및 이미지)에서 텍스트 응답을 생성합니다.
4.  멀티턴 대화 (채팅)에 Gemini를 사용합니다.
5.  대규모 언어 모델에 임베딩을 사용합니다.

기본 요건
-----

[Google Colab](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb?hl=ko)에서 빠른 시작을 실행할 수 있습니다. Google Colab에서는 이 노트북이 브라우저에서 직접 실행되며 추가 환경 구성이 필요하지 않습니다.

또는 이 빠른 시작을 로컬에서 완료하려면 개발 환경이 다음 요구사항을 충족하는지 확인하세요.

*   Python 3.9 이상
*   노트북을 실행할 `jupyter` 설치

설정
--

### Python SDK 설치

Gemini API용 Python SDK는 [`google-generativeai`](https://pypi.org/project/google-generativeai/) 패키지에 포함되어 있습니다. pip를 사용하여 종속 항목을 설치합니다.

    pip install -q -U google-generativeai

### 패키지 가져오기

필요한 패키지를 가져옵니다.

    import pathlibimport textwrapimport google.generativeai as genaifrom IPython.display import displayfrom IPython.display import Markdowndef to_markdown(text):  text = text.replace('•', '  *')  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    # Used to securely store your API keyfrom google.colab import userdata

### API 키 설정

Gemini API를 사용하려면 먼저 API 키를 가져와야 합니다. 아직 키가 없으면 Google AI Studio에서 클릭 한 번으로 키를 만듭니다.

[API 키 가져오기](https://makersuite.google.com/app/apikey?hl=ko)

Colab에서 왼쪽 패널의 'boot' 아래에 있는 보안 비밀 관리자에 키를 추가합니다. 이름을 `GOOGLE_API_KEY`로 지정합니다.

API 키가 있으면 SDK에 전달합니다. 여기에는 두 가지 방법이 있습니다.

*   `GOOGLE_API_KEY` 환경 변수에 키를 배치합니다 (SDK가 자동으로 거기에서 가져옴).
*   `genai.configure(api_key=...)`에 키 전달

    # Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')genai.configure(api_key=GOOGLE_API_KEY)

모델 나열
-----

이제 Gemini API를 호출할 준비가 되었습니다. `list_models`를 사용하여 사용 가능한 Gemini 모델을 확인합니다.

*   `gemini-pro`: 텍스트 전용 메시지에 최적화되었습니다.
*   `gemini-pro-vision`: 텍스트 및 이미지 프롬프트에 최적화되었습니다.

    for m in genai.list_models():  if 'generateContent' in m.supported_generation_methods:    print(m.name)

**참고:** 기능 및 비율 제한을 포함하여 사용 가능한 모델에 관한 자세한 내용은 [Gemini 모델](https://ai.google.dev/models/gemini?hl=ko)을 참고하세요. [비율 한도 상향 조정](https://ai.google.dev/docs/increase_quota?hl=ko)을 요청할 수 있는 옵션이 있습니다. Gemini-Pro 모델의 비율 한도는 분당 요청 수 (RPM) 60개입니다.

`genai` 패키지는 PaLM 모델 제품군도 지원하지만 Gemini 모델만 `generateContent` 메서드의 일반적인 멀티모달 기능을 지원합니다.

텍스트 입력에서 텍스트 생성
---------------

텍스트 전용 프롬프트의 경우 Gemini 1.5 모델 또는 Gemini 1.0 Pro 모델을 사용합니다.

    model = genai.GenerativeModel('gemini-1.5-flash')

`generate_content` 메서드는 기본 모델에서 지원하는 항목에 따라 멀티턴 채팅 및 멀티모달 입력을 비롯한 다양한 사용 사례를 처리할 수 있습니다. 사용 가능한 모델은 텍스트와 이미지만 입력으로, 텍스트만 출력으로 지원합니다.

가장 간단한 경우 프롬프트 문자열을 [`GenerativeModel.generate_content`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko#generate_content) 메서드에 전달할 수 있습니다.

    %%timeresponse = model.generate_content("What is the meaning of life?")

CPU times: user 110 ms, sys: 12.3 ms, total: 123 ms
Wall time: 8.25 s

간단한 경우에는 `response.text` 접근자만 있으면 됩니다. 형식이 지정된 마크다운 텍스트를 표시하려면 `to_markdown` 함수를 사용합니다.

    to_markdown(response.text)

> 삶의 목적을 묻는 질문은 수백 년, 문화, 대륙에 걸쳐 많은 사람들을 당황하게 합니다. 보편적으로 인정되는 반응은 없지만 많은 아이디어가 내렸으며 개인의 생각, 신념, 삶의 경험에 따라 그 반응이 달라지는 경우가 많습니다.
> 
> 1.  **행복과 웰빙:** 많은 사람들이 삶의 목표가 개인적인 행복과 웰빙을 얻는 것이라고 믿습니다. 여기에는 즐거움을 주는 추구를 찾고, 중요한 유대감을 쌓고, 신체적 및 정신적 건강을 돌보고, 개인적인 목표와 관심사를 추구하는 것이 포함될 수 있습니다.
>     
> 2.  **의미 있는 기여:** 세상에 의미 있는 기여를 하는 것이 삶의 목표라고 생각하는 사람들도 있습니다. 여기에는 다른 사람에게 도움이 되는 직업을 추구하거나, 자원봉사 또는 자선 활동에 참여하거나, 예술 또는 문학을 창작하거나, 발명을 하는 것이 포함될 수 있습니다.
>     
> 3.  **자아실현과 자기계발:** 자아실현과 자기개발의 추구는 인생의 또 다른 공통 목표입니다. 여기에는 새로운 기술을 배우고, 경계를 허물고, 개인적인 장애물에 부딪히고, 한 사람으로 진화하는 것이 수반될 수 있습니다.
>     
> 4.  **윤리적 및 도덕적 행동:** 어떤 사람들은 삶의 목표가 윤리적이고 도덕적으로 행동하는 것이라고 생각합니다. 그러려면 도덕적 원칙을 준수하고, 어려운 상황에서도 옳은 일을 하며, 더 나은 세상을 만들려는 노력이 수반될 수 있습니다.
>     
> 5.  **영적 성취:** 어떤 경우에는 삶의 목적이 영적 또는 종교적 신념과 관련되어 있습니다. 여기에는 더 높은 힘과의 관계를 추구하거나, 종교 의식을 행하거나, 영적인 가르침을 따르는 것이 포함될 수 있습니다.
>     
> 6.  **인생을 최대한 경험하기:** 어떤 사람들은 삶의 목표가 그 모든 것을 경험하는 것이라고 생각합니다. 여행, 새로운 것 시도, 위험 감수, 새로운 만남 수용이 수반될 수 있습니다.
>     
> 7.  **유산과 영향:** 삶의 목적이 평생에 남는 유산과 세상에 영향을 미치는 것이라고 믿는 사람들도 있습니다. 여기에는 주목할 만한 일을 하거나, 다른 사람의 기여로 기억되거나, 다른 사람들에게 영감을 주고 동기를 부여하는 것이 포함될 수 있습니다.
>     
> 8.  **균형과 조화 추구:** 삶의 모든 측면에서 균형과 조화를 이루는 것이 삶의 목표입니다. 여기에는 개인적, 직업적, 사회적 의무를 넘나들고, 내면의 평화와 만족을 찾고, 자신의 가치와 신념에 따른 삶을 사는 것이 수반될 수 있습니다.
>     
> 
> 궁극적으로 삶의 의미는 개인적인 여정이며, 각 개인은 경험, 생각, 주변 세계와의 상호작용을 통해 고유한 목적을 발견할 수 있습니다.

API가 결과를 반환하지 않으면 [`GenerateContentResponse.prompt_feedback`](https://ai.google.dev/api/python/google/generativeai/protos/GenerateContentResponse?hl=ko#prompt_feedback)를 사용하여 메시지와 관련된 안전 문제로 인해 차단되었는지 확인합니다.

    response.prompt_feedback

safety\_ratings {
  category: HARM\_CATEGORY\_SEXUALLY\_EXPLICIT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HATE\_SPEECH
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HARASSMENT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_DANGEROUS\_CONTENT
  probability: NEGLIGIBLE
}

Gemini는 단일 프롬프트에 대해 가능한 여러 응답을 생성할 수 있습니다. 이러한 가능한 응답을 `candidates`라고 하며, 이를 검토하여 가장 적합한 응답을 응답으로 선택할 수 있습니다.

[`GenerateContentResponse.candidates`](https://ai.google.dev/api/python/google/generativeai/protos/GenerateContentResponse?hl=ko#candidates)를 사용하여 응답 후보를 확인합니다.

    response.candidates

\[content {
  parts {
    text: "The query of life\\'s purpose has perplexed people across centuries, cultures, and continents. While there is no universally recognized response, many ideas have been put forth, and the response is frequently dependent on individual ideas, beliefs, and life experiences.\\n\\n1. \*\*Happiness and Well-being:\*\* Many individuals believe that the goal of life is to attain personal happiness and well-being. This might entail locating pursuits that provide joy, establishing significant connections, caring for one\\'s physical and mental health, and pursuing personal goals and interests.\\n\\n2. \*\*Meaningful Contribution:\*\* Some believe that the purpose of life is to make a meaningful contribution to the world. This might entail pursuing a profession that benefits others, engaging in volunteer or charitable activities, generating art or literature, or inventing.\\n\\n3. \*\*Self-realization and Personal Growth:\*\* The pursuit of self-realization and personal development is another common goal in life. This might entail learning new skills, pushing one\\'s boundaries, confronting personal obstacles, and evolving as a person.\\n\\n4. \*\*Ethical and Moral Behavior:\*\* Some believe that the goal of life is to act ethically and morally. This might entail adhering to one\\'s moral principles, doing the right thing even when it is difficult, and attempting to make the world a better place.\\n\\n5. \*\*Spiritual Fulfillment:\*\* For some, the purpose of life is connected to spiritual or religious beliefs. This might entail seeking a connection with a higher power, practicing religious rituals, or following spiritual teachings.\\n\\n6. \*\*Experiencing Life to the Fullest:\*\* Some individuals believe that the goal of life is to experience all that it has to offer. This might entail traveling, trying new things, taking risks, and embracing new encounters.\\n\\n7. \*\*Legacy and Impact:\*\* Others believe that the purpose of life is to leave a lasting legacy and impact on the world. This might entail accomplishing something noteworthy, being remembered for one\\'s contributions, or inspiring and motivating others.\\n\\n8. \*\*Finding Balance and Harmony:\*\* For some, the purpose of life is to find balance and harmony in all aspects of their lives. This might entail juggling personal, professional, and social obligations, seeking inner peace and contentment, and living a life that is in accordance with one\\'s values and beliefs.\\n\\nUltimately, the meaning of life is a personal journey, and different individuals may discover their own unique purpose through their experiences, reflections, and interactions with the world around them."
  }
  role: "model"
}
finish\_reason: STOP
index: 0
safety\_ratings {
  category: HARM\_CATEGORY\_SEXUALLY\_EXPLICIT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HATE\_SPEECH
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HARASSMENT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_DANGEROUS\_CONTENT
  probability: NEGLIGIBLE
}
\]

기본적으로 모델은 전체 생성 프로세스가 완료되면 응답을 반환합니다. 또한 생성되는 동안 응답을 스트리밍할 수 있으며 모델은 생성되는 즉시 응답 청크를 반환합니다.

응답을 스트리밍하려면 [`GenerativeModel.generate_content(..., stream=True)`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko#generate_content)을 사용합니다.

    %%timeresponse = model.generate_content("What is the meaning of life?", stream=True)

CPU times: user 102 ms, sys: 25.1 ms, total: 128 ms
Wall time: 7.94 s

    for chunk in response:  print(chunk.text)  print("_"*80)

The query of life's purpose has perplexed people across centuries, cultures, and
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
 continents. While there is no universally recognized response, many ideas have been put forth, and the response is frequently dependent on individual ideas, beliefs, and life experiences
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
.

1. \*\*Happiness and Well-being:\*\* Many individuals believe that the goal of life is to attain personal happiness and well-being. This might entail locating pursuits that provide joy, establishing significant connections, caring for one's physical and mental health, and pursuing personal goals and aspirations.

2. \*\*Meaning
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
ful Contribution:\*\* Some believe that the purpose of life is to make a meaningful contribution to the world. This might entail pursuing a profession that benefits others, engaging in volunteer or charitable activities, generating art or literature, or inventing.

3. \*\*Self-realization and Personal Growth:\*\* The pursuit of self-realization and personal development is another common goal in life. This might entail learning new skills, exploring one's interests and abilities, overcoming obstacles, and becoming the best version of oneself.

4. \*\*Connection and Relationships:\*\* For many individuals, the purpose of life is found in their relationships with others. This might entail building
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
 strong bonds with family and friends, fostering a sense of community, and contributing to the well-being of those around them.

5. \*\*Spiritual Fulfillment:\*\* For those with religious or spiritual beliefs, the purpose of life may be centered on seeking spiritual fulfillment or enlightenment. This might entail following religious teachings, engaging in spiritual practices, or seeking a deeper understanding of the divine.

6. \*\*Experiencing the Journey:\*\* Some believe that the purpose of life is simply to experience the journey itself, with all its joys and sorrows. This perspective emphasizes embracing the present moment, appreciating life's experiences, and finding meaning in the act of living itself.

7. \*\*Legacy and Impact:\*\* For others, the goal of life is to leave a lasting legacy or impact on the world. This might entail making a significant contribution to a particular field, leaving a positive mark on future generations, or creating something that will be remembered and cherished long after one's lifetime.

Ultimately, the meaning of life is a personal and subjective question, and there is no single, universally accepted answer. It is about discovering what brings you fulfillment, purpose, and meaning in your own life, and living in accordance with those values.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

스트리밍할 때 모든 응답 청크를 반복할 때까지 일부 응답 속성을 사용할 수 없습니다. 이에 대한 설명은 아래에 나와 있습니다.

    response = model.generate_content("What is the meaning of life?", stream=True)

`prompt_feedback` 속성은 다음과 같이 작동합니다.

    response.prompt_feedback

safety\_ratings {
  category: HARM\_CATEGORY\_SEXUALLY\_EXPLICIT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HATE\_SPEECH
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HARASSMENT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_DANGEROUS\_CONTENT
  probability: NEGLIGIBLE
}

그러나 `text`와 같은 속성은 다음을 수행하지 않습니다.

    try:  response.textexcept Exception as e:  print(f'{type(e).__name__}: {e}')

IncompleteIterationError: Please let the response complete iteration before accessing the final accumulated
attributes (or call \`response.resolve()\`)

이미지 및 텍스트 입력에서 텍스트 생성
---------------------

**참고:** 프롬프트의 크기가 20MB를 초과하면 [File API](https://ai.google.dev/tutorials/prompting_with_media?hl=ko)를 사용하여 미디어 파일을 업로드하세요.

Gemini는 텍스트와 이미지를 모두 입력할 수 있도록 멀티모달 입력(Gemini 1.5 모델 및 Gemini 1.0 Pro Vision)을 처리할 수 있는 다양한 모델을 제공합니다. [프롬프트의 이미지 요구사항](https://ai.google.dev/docs/gemini_api_overview?hl=ko#image_requirements)을 검토하세요.

프롬프트 입력에 텍스트와 이미지가 모두 포함되어 있으면 Gemini 1.5 모델 또는 Gemini 1.0 Pro Vision 모델을 `GenerativeModel.generate_content` 메서드와 함께 사용하여 텍스트 출력을 생성합니다.

이미지를 포함시켜 보겠습니다.

    curl -o image.jpg https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQ_Kevbk21QBRy-PgB4kQpS79brbmmEG7m3VOTShAn4PecDU5H5UxrJxE3Dw1JiaG17V88QIol19-3TM2wCHw

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  405k  100  405k    0     0  6982k      0 --:--:-- --:--:-- --:--:-- 7106k

    import PIL.Imageimg = PIL.Image.open('image.jpg')img

![png](https://ai.google.dev/static/gemini-api/docs/get-started/python_files/output_CjnS0vNTsVis_0.png?hl=ko)

Gemini 1.5 모델을 사용하고 `generate_content`를 사용하여 이미지를 모델에 전달합니다.

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(img)to_markdown(response.text)

> 현미와 구운 브로콜리, 피망이 어우러진 닭고기 데리야키 요리용 조리 덮밥입니다.

프롬프트에 텍스트와 이미지를 모두 제공하려면 문자열과 이미지가 포함된 목록을 전달합니다.

    response = model.generate_content(["Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.", img], stream=True)response.resolve()

    to_markdown(response.text)

> 식사 준비는 시간과 비용을 절약할 수 있는 좋은 방법일 뿐만 아니라 더 건강한 음식을 먹는 데도 도움이 될 수 있습니다. 이 음식은 미리 손쉽게 준비할 수 있는 건강하고 맛있는 식사의 좋은 예입니다.
> 
> 현미, 구운 야채, 치킨 데리야키가 포함된 식사입니다. 현미는 섬유질과 영양분이 풍부한 통곡물입니다. 구운 채소는 비타민과 미네랄을 매일 섭취하는 데 좋은 방법입니다. 치킨 데리야키는 단백질 원료로 다양한 맛도 담겨 있습니다.
> 
> 이 식사는 미리 준비하기가 쉽습니다. 현미를 끓이고 채소를 구운 다음 치킨 데리야키를 요리하기만 하면 됩니다. 그런 다음 음식을 개별 용기로 나눠 냉장고에 보관합니다. 식사를 할 준비가 되면 용기를 가지고 데우기만 하면 됩니다.
> 
> 이 식사는 건강하고 맛있는 식사 방법을 찾는 바쁜 사람들에게 안성맞춤입니다. 또한 체중을 감량하거나 건강한 체중을 유지하려는 사람들에게도 좋은 식사입니다.
> 
> 미리 쉽게 준비할 수 있는 건강하고 맛있는 식사를 찾고 있다면 이 식사가 훌륭한 선택입니다. 지금 바로 사용해 보세요.

채팅 대화
-----

Gemini를 사용하면 여러 차례에 걸쳐 자유 형식으로 대화를 나눌 수 있습니다. `ChatSession` 클래스는 대화 상태를 관리하여 프로세스를 단순화합니다. 따라서 `generate_content`와 달리 대화 기록을 목록으로 저장할 필요가 없습니다.

채팅을 초기화합니다.

    model = genai.GenerativeModel('gemini-1.5-flash')chat = model.start_chat(history=[])chat

<google.generativeai.generative\_models.ChatSession at 0x7b7b68250100>

**참고:** Gemini 1.0 Pro Vision 모델 (텍스트 및 이미지 입력용)은 아직 멀티턴 대화에 최적화되지 않았습니다. 대신 Gemini 1.5 모델 또는 Gemini 1.0 Pro 모델을 사용하세요.

[`ChatSession.send_message`](https://ai.google.dev/api/python/google/generativeai/ChatSession?hl=ko#send_message) 메서드는 [`GenerativeModel.generate_content`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko#generate_content)와 동일한 `GenerateContentResponse` 유형을 반환합니다. 또한 메시지와 응답이 채팅 기록에 추가됩니다.

    response = chat.send_message("In one sentence, explain how a computer works to a young child.")to_markdown(response.text)

> 컴퓨터는 우리의 지시를 이해하고 따를 수 있고 우리의 업무를 도울 수 있으며 심지어 우리와 함께 게임도 할 수 있는 아주 스마트한 기계라고 할 수 있습니다.

    chat.history

\[parts {
   text: "In one sentence, explain how a computer works to a young child."
 }
 role: "user",
 parts {
   text: "A computer is like a very smart machine that can understand and follow our instructions, help us with our work, and even play games with us!"
 }
 role: "model"\]

대화를 계속하려면 메시지를 계속 보낼 수 있습니다. `stream=True` 인수를 사용하여 채팅을 스트리밍합니다.

    response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)for chunk in response:  print(chunk.text)  print("_"*80)

A computer works by following instructions, called a program, which tells it what to
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
 do. These instructions are written in a special language that the computer can understand, and they are stored in the computer's memory. The computer's processor
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
, or CPU, reads the instructions from memory and carries them out, performing calculations and making decisions based on the program's logic. The results of these calculations and decisions are then displayed on the computer's screen or stored in memory for later use.

To give you a simple analogy, imagine a computer as a
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
 chef following a recipe. The recipe is like the program, and the chef's actions are like the instructions the computer follows. The chef reads the recipe (the program) and performs actions like gathering ingredients (fetching data from memory), mixing them together (performing calculations), and cooking them (processing data). The final dish (the output) is then presented on a plate (the computer screen).

In summary, a computer works by executing a series of instructions, stored in its memory, to perform calculations, make decisions, and display or store the results.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

`genai.protos.Content` 객체에는 각각 텍스트 (문자열) 또는 inline\_data (`genai.protos.Blob`)가 포함된 `genai.protos.Part` 객체 목록이 포함됩니다. 여기서 blob에는 바이너리 데이터와 `mime_type`가 포함됩니다. 채팅 기록은 [`ChatSession.history`](https://ai.google.dev/api/python/google/generativeai/ChatSession?hl=ko#history)에서 `genai.protos.Content` 객체 목록으로 확인할 수 있습니다.

    for message in chat.history:  display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))

> **사용자**: 어린 자녀가 컴퓨터가 어떻게 작동하는지 한 문장으로 설명합니다.

> **model**: 컴퓨터는 매우 똑똑한 기계와도 같습니다. 이 기계는 우리의 지시를 이해하고 따를 수 있고, 우리의 업무를 도울 수 있으며, 심지어 우리와 함께 게임도 할 수 있습니다.

> **사용자**: 알겠습니다. 고등학생에게 좀 더 자세한 설명을 해주시겠어요?

> **model**: 컴퓨터는 해야 할 일을 알려주는 프로그램이라는 명령을 따릅니다. 이러한 명령은 컴퓨터가 이해할 수 있는 특별한 언어로 작성되며 컴퓨터의 메모리에 저장됩니다. 컴퓨터의 프로세서 또는 CPU는 메모리에서 명령을 읽고 실행하여 프로그램의 논리에 따라 계산을 수행하고 결정을 내립니다. 이러한 계산 및 결정의 결과는 컴퓨터 화면에 표시되거나 나중에 사용할 수 있도록 메모리에 저장됩니다.
> 
> 간단한 비유를 위해 컴퓨터가 조리법을 따르는 요리사라고 가정해 보겠습니다. 조리법은 프로그램과 같고 요리사의 행동은 컴퓨터가 따르는 지침과 같습니다. 셰프는 레시피 (프로그램)를 읽고 재료 수집 (메모리에서 데이터 가져오기), 함께 섞기 (계산 수행), 요리 (데이터 처리)와 같은 작업을 수행합니다. 그런 다음 최종 요리 (결과물)를 접시 (컴퓨터 화면)에 담습니다.
> 
> 요약하면, 컴퓨터는 메모리에 저장된 일련의 명령을 실행하여 계산을 수행하고, 결정을 내리고, 결과를 표시하거나 저장합니다.

토큰 개수
-----

대규모 언어 모델에는 컨텍스트 기간이 있으며 컨텍스트 길이는 주로 **토큰 수**를 기준으로 측정됩니다. Gemini API를 사용하면 `genai.protos.Content` 객체당 토큰 수를 확인할 수 있습니다. 가장 간단한 경우 다음과 같이 쿼리 문자열을 [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko#count_tokens) 메서드에 전달할 수 있습니다.

    model.count_tokens("What is the meaning of life?")

total\_tokens: 7

마찬가지로 `token_count`에서 `ChatSession`를 확인할 수 있습니다.

    model.count_tokens(chat.history)

total\_tokens: 501

임베딩 사용
------

[임베딩](https://developers.google.com/machine-learning/glossary?hl=ko#embedding-vector)은 배열의 부동 소수점 숫자 목록으로 정보를 표현하는 데 사용되는 기법입니다. Gemini를 사용하면 텍스트 (단어, 문장, 텍스트 블록)를 벡터화된 형식으로 표시할 수 있으므로 임베딩을 더 쉽게 비교하고 대조할 수 있습니다. 예를 들어 비슷한 주제나 감정을 공유하는 두 텍스트는 코사인 유사성과 같은 수학적 비교 기술을 통해 식별할 수 있는 비슷한 임베딩을 사용해야 합니다. 임베딩을 사용하는 방법과 이유에 대한 자세한 내용은 [임베딩 가이드](https://ai.google.dev/docs/embeddings_guide?hl=ko)를 참조하세요.

`embed_content` 메서드를 사용하여 임베딩을 생성합니다. 이 메서드는 다음 작업 (`task_type`)의 삽입을 처리합니다.

| 작업 유형 | 설명 |
| --- | --- |
| RETRIEVAL\_QUERY | 지정된 텍스트가 검색/가져오기 설정의 쿼리임을 지정합니다. |
| RETRIEVAL\_DOCUMENT | 지정된 텍스트가 검색/가져오기 설정의 문서임을 지정합니다. 이 작업 유형을 사용하려면 `title`가 필요합니다. |
| SEMANTIC\_SIMILARITY | 지정된 텍스트를 시맨틱 텍스트 유사성(STS)에 사용하도록 지정합니다. |
| 분류 | 임베딩이 분류에 사용되도록 지정합니다. |
| 클러스터링 | 클러스터링에 임베딩을 사용하도록 지정합니다. |

다음은 문서 검색을 위해 단일 문자열의 임베딩을 생성합니다.

    result = genai.embed_content(    model="models/embedding-001",    content="What is the meaning of life?",    task_type="retrieval_document",    title="Embedding of single string")# 1 input > 1 vector outputprint(str(result['embedding'])[:50], '... TRIMMED]')

\[-0.003216741, -0.013358698, -0.017649598, -0.0091 ... TRIMMED\]

**참고:** `retrieval_document` 작업 유형은 제목을 허용하는 유일한 작업입니다.

문자열 배치를 처리하려면 `content`에 문자열 목록을 전달합니다.

    result = genai.embed_content(    model="models/embedding-001",    content=[      'What is the meaning of life?',      'How much wood would a woodchuck chuck?',      'How does the brain work?'],    task_type="retrieval_document",    title="Embedding of list of strings")# A list of inputs > A list of vectors outputfor v in result['embedding']:  print(str(v)[:50], '... TRIMMED ...')

\[0.0040260437, 0.004124458, -0.014209415, -0.00183 ... TRIMMED ...
\[-0.004049845, -0.0075574904, -0.0073463684, -0.03 ... TRIMMED ...
\[0.025310587, -0.0080734305, -0.029902633, 0.01160 ... TRIMMED ...

`genai.embed_content` 함수는 간단한 문자열이나 문자열 목록을 수락하지만 실제로는 `genai.protos.Content` 유형 (예: [`GenerativeModel.generate_content`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko#generate_content))을 기반으로 합니다. `genai.protos.Content` 객체는 API에서 대화의 기본 단위입니다.

`genai.protos.Content` 객체는 멀티모달이지만 `embed_content` 메서드는 텍스트 임베딩만 지원합니다. 이러한 설계는 API가 멀티모달 임베딩으로 확장될 _가능성_을 제공합니다.

    response.candidates[0].content

parts {
  text: "A computer works by following instructions, called a program, which tells it what to do. These instructions are written in a special language that the computer can understand, and they are stored in the computer\\'s memory. The computer\\'s processor, or CPU, reads the instructions from memory and carries them out, performing calculations and making decisions based on the program\\'s logic. The results of these calculations and decisions are then displayed on the computer\\'s screen or stored in memory for later use.\\n\\nTo give you a simple analogy, imagine a computer as a chef following a recipe. The recipe is like the program, and the chef\\'s actions are like the instructions the computer follows. The chef reads the recipe (the program) and performs actions like gathering ingredients (fetching data from memory), mixing them together (performing calculations), and cooking them (processing data). The final dish (the output) is then presented on a plate (the computer screen).\\n\\nIn summary, a computer works by executing a series of instructions, stored in its memory, to perform calculations, make decisions, and display or store the results."
}
role: "model"

    result = genai.embed_content(    model = 'models/embedding-001',    content = response.candidates[0].content)# 1 input > 1 vector outputprint(str(result['embedding'])[:50], '... TRIMMED ...')

\[-0.013921871, -0.03504407, -0.0051786783, 0.03113 ... TRIMMED ...

마찬가지로 채팅 기록에는 `embed_content` 함수에 직접 전달할 수 있는 `genai.protos.Content` 객체 목록이 포함되어 있습니다.

    chat.history

\[parts {
   text: "In one sentence, explain how a computer works to a young child."
 }
 role: "user",
 parts {
   text: "A computer is like a very smart machine that can understand and follow our instructions, help us with our work, and even play games with us!"
 }
 role: "model",
 parts {
   text: "Okay, how about a more detailed explanation to a high schooler?"
 }
 role: "user",
 parts {
   text: "A computer works by following instructions, called a program, which tells it what to do. These instructions are written in a special language that the computer can understand, and they are stored in the computer\\'s memory. The computer\\'s processor, or CPU, reads the instructions from memory and carries them out, performing calculations and making decisions based on the program\\'s logic. The results of these calculations and decisions are then displayed on the computer\\'s screen or stored in memory for later use.\\n\\nTo give you a simple analogy, imagine a computer as a chef following a recipe. The recipe is like the program, and the chef\\'s actions are like the instructions the computer follows. The chef reads the recipe (the program) and performs actions like gathering ingredients (fetching data from memory), mixing them together (performing calculations), and cooking them (processing data). The final dish (the output) is then presented on a plate (the computer screen).\\n\\nIn summary, a computer works by executing a series of instructions, stored in its memory, to perform calculations, make decisions, and display or store the results."
 }
 role: "model"\]

    result = genai.embed_content(    model = 'models/embedding-001',    content = chat.history)# 1 input > 1 vector outputfor i,v in enumerate(result['embedding']):  print(str(v)[:50], '... TRIMMED...')

\[-0.014632266, -0.042202696, -0.015757175, 0.01548 ... TRIMMED...
\[-0.010979066, -0.024494737, 0.0092659835, 0.00803 ... TRIMMED...
\[-0.010055617, -0.07208932, -0.00011750793, -0.023 ... TRIMMED...
\[-0.013921871, -0.03504407, -0.0051786783, 0.03113 ... TRIMMED...

고급 사용 사례
--------

다음 섹션에서는 Gemini API용 Python SDK의 고급 사용 사례와 하위 수준 세부정보를 설명합니다.

### 안전 설정

`safety_settings` 인수를 사용하면 모델이 프롬프트와 응답 모두에서 차단하고 허용하는 항목을 구성할 수 있습니다. 기본적으로 안전 설정은 모든 측정기준에서 보통 또는 높은 확률로 안전하지 않은 콘텐츠를 차단합니다. [안전 설정](https://ai.google.dev/docs/safety_setting?hl=ko)에 대해 자세히 알아보기

의심스러운 프롬프트를 입력하고 기본 안전 설정으로 모델을 실행하면 후보가 반환되지 않습니다.

    response = model.generate_content('[Questionable prompt here]')response.candidates

\[content {
  parts {
    text: "I\\'m sorry, but this prompt involves a sensitive topic and I\\'m not allowed to generate responses that are potentially harmful or inappropriate."
  }
  role: "model"
}
finish\_reason: STOP
index: 0
safety\_ratings {
  category: HARM\_CATEGORY\_SEXUALLY\_EXPLICIT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HATE\_SPEECH
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HARASSMENT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_DANGEROUS\_CONTENT
  probability: NEGLIGIBLE
}
\]

`prompt_feedback`에서 메시지를 차단한 안전 필터를 알려줍니다.

    response.prompt_feedback

safety\_ratings {
  category: HARM\_CATEGORY\_SEXUALLY\_EXPLICIT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HATE\_SPEECH
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_HARASSMENT
  probability: NEGLIGIBLE
}
safety\_ratings {
  category: HARM\_CATEGORY\_DANGEROUS\_CONTENT
  probability: NEGLIGIBLE
}

이제 새로 구성된 안전 설정을 사용하여 모델에 동일한 프롬프트를 제공하면 응답을 받을 수 있습니다.

    response = model.generate_content('[Questionable prompt here]',                                  safety_settings={'HARASSMENT':'block_none'})response.text

또한 프롬프트는 통과했지만 개별 응답이 안전 확인을 통과하지 못한 경우 각 후보에는 자체 `safety_ratings`가 있습니다.

### 메시지 인코딩

이전 섹션에서는 API에 프롬프트를 쉽게 보낼 수 있도록 SDK를 사용했습니다. 이 섹션에서는 이전 예와 완전히 일치하는 항목을 제공하므로 SDK가 메시지를 인코딩하는 방법에 대한 하위 수준의 세부정보를 더 잘 이해할 수 있습니다.

Python SDK의 기반은 [`google.ai.generativelanguage`](https://ai.google.dev/api/python/google/generativeai/protos?hl=ko) 클라이언트 라이브러리입니다.

SDK는 메시지를 `genai.protos.Content` 객체로 변환하려고 시도합니다. 이 객체에는 각각 다음 중 하나를 포함하는 `genai.protos.Part` 객체 목록이 포함되어 있습니다.

1.  [`text`](https://www.tensorflow.org/text/api_docs/python/text?hl=ko) (문자열)
2.  `inline_data` (`genai.protos.Blob`) - blob에 바이너리 `data` 및 `mime_type`가 포함됨

이러한 클래스를 동등한 사전으로 전달할 수도 있습니다.

**참고:** 허용되는 MIME 유형은 일부 이미지 유형(`image/*`)뿐입니다.

따라서 이전 예와 완전히 일치하는 항목은 다음과 같습니다.

    model = genai.GenerativeModel('gemini-1.5-flash')response = model.generate_content(    genai.protos.Content(        parts = [            genai.protos.Part(text="Write a short, engaging blog post based on this picture."),            genai.protos.Part(                inline_data=genai.protos.Blob(                    mime_type='image/jpeg',                    data=pathlib.Path('image.jpg').read_bytes()                )            ),        ],    ),    stream=True)

    response.resolve()to_markdown(response.text[:100] + "... [TRIMMED] ...")

> 식사 준비는 시간과 비용을 절약할 수 있는 좋은 방법일 뿐만 아니라 더 건강한 음식을 먹는 데도 도움이 될 수 있습니다. ... \[TRIMMED\] ...

### 멀티턴 대화

앞에서 설명한 `genai.ChatSession` 클래스는 많은 사용 사례를 처리할 수 있지만 몇 가지 가정을 합니다. 사용 사례가 이 채팅 구현에 맞지 않는 경우 `genai.ChatSession`는 [`GenerativeModel.generate_content`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko#generate_content)의 래퍼일 뿐이라는 점을 기억하는 것이 좋습니다. 단일 요청 외에도 멀티턴 대화를 처리할 수 있습니다.

개별 메시지는 이전 섹션에서 본 `genai.protos.Content` 객체 또는 호환되는 사전입니다. 사전으로서 메시지에는 `role` 및 `parts` 키가 필요합니다. 대화의 `role`는 프롬프트를 제공하는 `user` 또는 응답을 제공하는 `model`일 수 있습니다.

`genai.protos.Content` 객체의 목록을 전달하면 멀티턴 채팅으로 처리됩니다.

    model = genai.GenerativeModel('gemini-1.5-flash')messages = [    {'role':'user',     'parts': ["Briefly explain how a computer works to a young child."]}]response = model.generate_content(messages)to_markdown(response.text)

> 컴퓨터를 많은 것을 도울 수 있는 정말 똑똑한 친구라고 상상해 보세요. 생각하고 학습할 뇌가 있는 것처럼 컴퓨터도 프로세서라고 하는 뇌가 있습니다. 마치 컴퓨터의 사장이 해야 할 일을 알려주는 것과 같습니다.
> 
> 컴퓨터 안에는 메모리라는 특별한 공간이 있는데, 이것은 큰 저장 상자와 같습니다. 게임 열기나 동영상 재생과 같이 사용자가 지시하는 모든 내용을 기억합니다.
> 
> 키보드의 버튼을 누르거나 마우스로 화면의 항목을 클릭하면 메시지가 컴퓨터로 전송됩니다. 이러한 메시지는 케이블이라고 하는 특수선을 통해 프로세서로 이동합니다.
> 
> 프로세서는 메시지를 읽고 해야 할 일을 컴퓨터에 알려줍니다. 프로그램을 열거나, 사진을 표시하거나, 음악을 재생할 수도 있습니다.
> 
> 화면에 표시되는 모든 것은 그래픽 카드를 통해 만들어지며, 그래픽 카드는 컴퓨터 안에 있는 마술 아티스트와 같습니다. 이 백도어는 프로세서의 지시를 받아 다채로운 색상의 사진과 비디오를 만듭니다.
> 
> 좋아하는 게임, 동영상, 사진을 저장하기 위해 컴퓨터는 하드 드라이브라고 하는 특별한 저장 공간을 사용합니다. 컴퓨터가 소중한 물건을 모두 안전하게 지킬 수 있는 거대한 도서관과 같습니다.
> 
> 또한 인터넷에 연결하여 친구와 게임을 하거나 재미있는 동영상을 보고 싶을 때 컴퓨터는 네트워크 카드라는 것을 사용하여 인터넷 케이블이나 Wi-Fi 신호를 통해 메시지를 주고받습니다.
> 
> 따라서 뇌가 학습과 놀이를 돕는 것처럼 컴퓨터의 프로세서, 메모리, 그래픽 카드, 하드 드라이브 및 네트워크 카드가 모두 함께 작동하여 컴퓨터를 놀라운 일을 할 수 있도록 도와주는 매우 똑똑한 친구가 됩니다.

대화를 계속하려면 응답과 다른 메시지를 추가하세요.

**참고:** 멀티턴 대화의 경우 각 요청과 함께 전체 대화 기록을 전송해야 합니다. API는 **스테이트리스(Stateless)**입니다.

    messages.append({'role':'model',                 'parts':[response.text]})messages.append({'role':'user',                 'parts':["Okay, how about a more detailed explanation to a high school student?"]})response = model.generate_content(messages)to_markdown(response.text)

> 본질적으로 컴퓨터는 일련의 명령을 수행하도록 프로그래밍할 수 있는 기계입니다. 이 API는 함께 작동하여 정보를 처리, 저장 및 표시하는 몇 가지 필수 요소로 구성됩니다.
> 
> **1\. 프로세서 (CPU):** - 컴퓨터의 두뇌입니다. - 명령을 실행하고 계산을 수행합니다. - 기가헤르츠 (GHz) 단위로 측정된 속도입니다. - 일반적으로 GHz가 많을수록 더 빠른 처리를 의미합니다.
> 
> **2\. 메모리 (RAM):** - 처리 중인 데이터를 위한 임시 저장소입니다. - 프로그램이 실행되는 동안 명령과 데이터를 보관합니다. - 기가바이트 (GB) 단위로 측정됩니다. - RAM이 많을수록 더 많은 프로그램을 동시에 실행할 수 있습니다.
> 
> **3\. 저장소 (HDD/SSD):** - 데이터를 위한 영구 저장소입니다. - 운영 체제, 프로그램 및 사용자 파일을 저장합니다. - 기가바이트 (GB) 또는 테라바이트 (TB)로 측정됩니다. - 하드 디스크 드라이브 (HDD)는 일반적이며 느리고 저렴합니다. - 솔리드 스테이트 드라이브 (SSD)는 더 새롭고 더 빠르고 더 비쌉니다.
> 
> **4\. 그래픽 카드 (GPU):** - 이미지를 처리하고 표시합니다. - 게임, 동영상 편집, 기타 그래픽 집약적인 작업에 필수적입니다. - 비디오 RAM (VRAM) 및 클록 속도로 측정됩니다.
> 
> **5\. 마더보드:** - 모든 구성요소를 연결합니다. - 전력 및 통신 경로 제공
> 
> **6\. 입출력 (I/O) 기기:** - 사용자가 컴퓨터와 상호작용할 수 있습니다. - 예: 키보드, 마우스, 모니터, 프린터
> 
> **7\. 운영체제 (OS):** - 컴퓨터의 리소스를 관리하는 소프트웨어입니다. - 사용자 인터페이스 및 기본 기능을 제공합니다. - 예: Windows, macOS, Linux
> 
> 컴퓨터에서 프로그램을 실행하면 다음과 같은 결과가 발생합니다.
> 
> 1.  프로그램 명령은 저장소에서 메모리로 로드됩니다.
> 2.  프로세서는 메모리에서 명령을 읽고 명령을 하나씩 실행합니다.
> 3.  명령어에 계산이 포함된 경우 프로세서는 산술 논리 유닛 (ALU)을 사용하여 계산을 수행합니다.
> 4.  명령에 데이터가 포함된 경우 프로세서는 메모리를 읽거나 씁니다.
> 5.  계산이나 데이터 조작의 결과는 메모리에 저장됩니다.
> 6.  프로그램이 화면에 무언가를 표시해야 하는 경우 필요한 데이터를 그래픽 카드로 보냅니다.
> 7.  그래픽 카드가 데이터를 처리하여 모니터로 보내어 표시합니다.
> 
> 이 프로세스는 프로그램이 작업을 완료하거나 사용자가 종료할 때까지 계속됩니다.

### 생성 구성

`generation_config` 인수를 사용하면 생성 매개변수를 수정할 수 있습니다. 모델에 전송하는 모든 프롬프트에는 모델의 응답 생성 방식을 제어하는 매개변수 값이 포함됩니다.

    model = genai.GenerativeModel('gemini-1.5-flash')response = model.generate_content(    'Tell me a story about a magic backpack.',    generation_config=genai.types.GenerationConfig(        # Only one candidate for now.        candidate_count=1,        stop_sequences=['x'],        max_output_tokens=20,        temperature=1.0))

    text = response.textif response.candidates[0].finish_reason.name == "MAX_TOKENS":    text += '...'to_markdown(text)

> 옛날 울창한 언덕으로 둘러싸인 작은 마을에 한 소녀가...

다음 단계
-----

*   프롬프트 설계는 언어 모델에서 원하는 응답을 유도하는 프롬프트를 만드는 프로세스입니다. 잘 구조화된 프롬프트를 작성하는 것은 언어 모델에서 정확하고 고품질의 응답을 보장하는 데 필수적입니다. [프롬프트 작성](https://ai.google.dev/docs/prompt_best_practices?hl=ko) 권장사항에 대해 알아보기
*   Gemini는 입력 유형 및 복잡성, 채팅 또는 기타 대화상자 언어 작업의 구현, 크기 제약 조건과 같은 다양한 사용 사례의 요구사항을 충족하기 위해 여러 모델 변형을 제공합니다. 사용 가능한 [Gemini 모델](https://ai.google.dev/models/gemini?hl=ko)에 대해 자세히 알아보세요.
*   Gemini에서는 [비율 한도 상향](https://ai.google.dev/docs/increase_quota?hl=ko)을 요청할 수 있는 옵션을 제공합니다. Gemini-Pro 모델의 비율 한도는 분당 요청 수 (RPM) 60개입니다.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-06-06(UTC)
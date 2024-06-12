---
Please provide me with the context or the specific mission you want me to write about.  

For example, tell me: "* **What kind of mission is it?** (e.g., a company mission, a personal mission, a mission for a project, a mission for a team)"
* **What is the purpose or goal of the mission?** 
* **What are the key values or principles that guide the mission?** 
* **Who is the target audience for the mission statement?**

Once I have this information, I can help you craft a compelling and effective mission statement.
---

*   이 페이지의 내용
*   [설정](#setup)
    *   [Python SDK 설치](#install_the_python_sdk)
    *   [패키지 가져오기](#import_packages)
    *   [API 키 설정](#set_up_your_api_key)
*   [함수 호출의 기본사항](#basics_of_function_calling)
*   [병렬 함수 호출](#parallel_function_calling)
*   [(선택사항) 낮은 수준의 액세스](#optional_low_level_access)
*   [요약](#summary)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

튜토리얼: Gemini API로 함수 호출
=======================

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [설정](#setup)
    *   [Python SDK 설치](#install_the_python_sdk)
    *   [패키지 가져오기](#import_packages)
    *   [API 키 설정](#set_up_your_api_key)
*   [함수 호출의 기본사항](#basics_of_function_calling)
*   [병렬 함수 호출](#parallel_function_calling)
*   [(선택사항) 낮은 수준의 액세스](#optional_low_level_access)
*   [요약](#summary)

Python Node.js Go Dart (Flutter) Android Swift 웹

  

<table align="left" class="tfo-notebook-buttons"><tbody><tr><td><a href="https://ai.google.dev/gemini-api/docs/function-calling/python?hl=ko" target="_blank"><img height="32" src="https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png?hl=ko" width="32">ai.google.dev에서 보기</a></td><td><a href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/function-calling/python.ipynb?hl=ko" target="_blank"><img src="https://www.tensorflow.org/images/colab_logo_32px.png?hl=ko">Google Colab에서 실행</a></td><td><a href="https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/function-calling/python.ipynb" target="_blank"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=ko">GitHub에서 소스 보기</a></td></tr></tbody></table>

함수 호출을 사용하여 맞춤 함수를 정의하고 Gemini에 전달합니다. 모델은 이러한 함수를 직접 호출하지 않고 대신 함수 이름과 추천 인수를 지정하는 구조화된 데이터 출력을 생성합니다. 이 출력을 통해 외부 API를 호출할 수 있으며, 그 결과 생성된 API 출력을 모델에 다시 통합할 수 있어 더 포괄적인 쿼리 응답이 가능합니다. 함수 호출은 LLM이 실시간 정보 및 데이터베이스, 고객 관계 관리 시스템, 문서 저장소와 같은 다양한 서비스와 상호작용할 수 있도록 지원하여 관련성 있는 상황별 답변을 제공하는 능력을 강화합니다. Gemini 모델에 함수 설명을 제공할 수 있습니다. 모델이 쿼리를 처리할 수 있도록 함수를 호출하고 결과를 돌려보내도록 요청할 수 있습니다.

아직 확인하지 않았다면 [함수 호출 소개](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)를 확인하여 자세히 알아보세요.

설정
--

### Python SDK 설치

Gemini API용 Python SDK는 [`google-generativeai`](https://pypi.org/project/google-generativeai/) 패키지에 포함되어 있습니다. pip를 사용하여 종속 항목을 설치합니다.

    pip install -U -q google-generativeai

### 패키지 가져오기

필요한 패키지를 가져옵니다.

    import pathlibimport textwrapimport timeimport google.generativeai as genaifrom IPython import displayfrom IPython.display import Markdowndef to_markdown(text):  text = text.replace('•', '  *')  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

### API 키 설정

Gemini API를 사용하려면 먼저 API 키를 가져와야 합니다. 아직 키가 없으면 Google AI Studio에서 클릭 한 번으로 키를 만듭니다.

[API 키 가져오기](https://makersuite.google.com/app/apikey?hl=ko)

Colab에서 왼쪽 패널의 'boot' 아래에 있는 보안 비밀 관리자에 키를 추가합니다. 이름을 `API_KEY`로 지정합니다.

API 키가 있으면 SDK에 전달합니다. 여기에는 두 가지 방법이 있습니다.

*   `GOOGLE_API_KEY` 환경 변수에 키를 배치합니다 (SDK가 자동으로 거기에서 가져옴).
*   `genai.configure(api_key=...)`에 키 전달

    try:    # Used to securely store your API key    from google.colab import userdata    # Or use `os.getenv('API_KEY')` to fetch an environment variable.    GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')except ImportError:    import os    GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']genai.configure(api_key=GOOGLE_API_KEY)

함수 호출의 기본사항
-----------

함수 호출을 사용하려면 [`GenerativeModel`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko)를 만들 때 함수 목록을 `tools` 매개변수에 전달합니다. 모델은 함수 이름, docstring, 매개변수, 매개변수 유형 주석을 사용하여 프롬프트에 가장 잘 대답하는 함수가 필요한지 결정합니다.

**중요:** SDK는 함수 매개변수 유형 주석을 API가 이해하는 형식 (`genai.protos.FunctionDeclaration`)으로 변환합니다. API는 일부 매개변수 유형만 지원하며 Python SDK의 자동 변환은 그 하위 집합만 지원합니다. `AllowedTypes = int | float | bool | str | list['AllowedTypes'] | dict`

    def multiply(a:float, b:float):    """returns a * b."""    return a*bmodel = genai.GenerativeModel(model_name='gemini-1.5-flash',                              tools=[multiply])model

genai.GenerativeModel(
    model\_name='models/gemini-1.5-flash',
    generation\_config={},
    safety\_settings={},
    tools=<google.generativeai.types.content\_types.FunctionLibrary object at 0x10e73fe90>,
)

채팅 인터페이스를 통해 함수 호출을 사용하는 것이 좋습니다. 이는 함수 호출이 사용자와 모델 간의 양방향 상호작용을 포착하므로 [멀티턴 채팅](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ko#multi-turn)에 자연스럽게 부합하기 때문입니다. Python SDK의 [`ChatSession`](https://ai.google.dev/api/python/google/generativeai/ChatSession?hl=ko)는 대화 기록을 처리하므로 채팅용으로 좋은 인터페이스이며 `enable_automatic_function_calling` 매개변수를 사용하면 함수 호출이 훨씬 더 간소화됩니다.

    chat = model.start_chat(enable_automatic_function_calling=True)

자동 함수 호출이 사용 설정되면 모델에서 요청하는 경우 `chat.send_message`가 함수를 자동으로 호출합니다.

정답이 포함된 텍스트 응답을 단순히 반환하는 것 같습니다.

    response = chat.send_message('I have 57 cats, each owns 44 mittens, how many mittens is that in total?')response.text

'The total number of mittens is 2508.'

    57*44

2508

채팅 기록을 검토하여 대화의 흐름과 대화 내에서 함수 호출이 어떻게 통합되는지 확인합니다.

`ChatSession.history` 속성은 사용자와 Gemini 모델 간의 대화의 시간순 기록을 저장합니다. 대화의 각 차례는 다음 정보가 포함된 [`genai.protos.Content`](https://ai.google.dev/api/python/google/generativeai/protos/Content?hl=ko) 객체로 표현됩니다.

*   **역할**: 콘텐츠의 출처가 '사용자'인지 '모델'인지 식별합니다.
*   **부분**: 메시지의 개별 구성요소를 나타내는 [`genai.protos.Part`](https://ai.google.dev/api/python/google/generativeai/protos/Part?hl=ko) 객체의 목록입니다. 텍스트 전용 모델에서 이러한 부분은 다음과 같습니다.
    *   **텍스트**: 일반 문자 메시지입니다.
    *   **함수 호출** ([`genai.protos.FunctionCall`](https://ai.google.dev/api/python/google/generativeai/protos/FunctionCall?hl=ko)): 제공된 인수로 특정 함수를 실행하기 위한 모델의 요청입니다.
    *   **함수 응답** ([`genai.protos.FunctionResponse`](https://ai.google.dev/api/python/google/generativeai/protos/FunctionResponse?hl=ko)): 요청된 함수를 실행한 후 사용자가 반환한 결과입니다.

벙어리 장갑 계산을 사용한 이전 예에서 내역은 다음과 같은 순서를 보여줍니다.

1.  **사용자**: 장갑의 총 개수를 묻습니다.
2.  **모델**: 곱하기 함수가 유용한지 확인하고 사용자에게 FunctionCall 요청을 보냅니다.
3.  **사용자**: `ChatSession`는 `enable_automatic_function_calling`가 설정되어 있어 자동으로 함수를 실행하고 계산된 결과와 함께 `FunctionResponse`를 반환합니다.
4.  **모델**: 함수의 출력을 사용하여 최종 답변을 작성하고 텍스트 응답으로 표시합니다.

    for content in chat.history:    part = content.parts[0]    print(content.role, "->", type(part).to_dict(part))    print('-'*80)

user -> {'text': 'I have 57 cats, each owns 44 mittens, how many mittens is that in total?'}
--------------------------------------------------------------------------------
model -> {'function\_call': {'name': 'multiply', 'args': {'a': 57.0, 'b': 44.0} } }
--------------------------------------------------------------------------------
user -> {'function\_response': {'name': 'multiply', 'response': {'result': 2508.0} } }
--------------------------------------------------------------------------------
model -> {'text': 'The total number of mittens is 2508.'}
--------------------------------------------------------------------------------

일반적으로 상태 다이어그램은 다음과 같습니다.

![모델은 항상 텍스트 또는 FunctionCall로 응답할 수 있습니다. 모델이 FunctionCall을 전송하면 사용자는 FunctionResponse로 응답해야 합니다.](https://ai.google.dev/images/tutorials/function_call_state_diagram.png?hl=ko)

모델은 텍스트 응답을 반환하기 전에 여러 함수 호출로 응답할 수 있으며 함수 호출은 텍스트 응답 앞에 옵니다.

이 모든 작업은 자동으로 처리되지만 더 세부적으로 관리할 수 있는 방법은 다음과 같습니다.

*   기본 `enable_automatic_function_calling=False`를 그대로 두고 `genai.protos.FunctionCall` 응답을 직접 처리합니다.
*   또는 채팅 기록도 관리해야 하는 `GenerativeModel.generate_content`를 사용합니다.

병렬 함수 호출
--------

위에서 설명한 기본 함수 호출 외에도 한 차례에 여러 함수를 호출할 수 있습니다. 이 섹션에서는 병렬 함수 호출을 사용하는 방법에 대한 예를 보여줍니다.

도구를 정의합니다.

    def power_disco_ball(power: bool) -> bool:    """Powers the spinning disco ball."""    print(f"Disco ball is {'spinning!' if power else 'stopped.'}")    return Truedef start_music(energetic: bool, loud: bool, bpm: int) -> str:    """Play some music matching the specified parameters.    Args:      energetic: Whether the music is energetic or not.      loud: Whether the music is loud or not.      bpm: The beats per minute of the music.    Returns: The name of the song being played.    """    print(f"Starting music! {energetic=} {loud=}, {bpm=}")    return "Never gonna give you up."def dim_lights(brightness: float) -> bool:    """Dim the lights.    Args:      brightness: The brightness of the lights, 0.0 is off, 1.0 is full.    """    print(f"Lights are now set to {brightness:.0%}")    return True

이제 지정된 모든 도구를 사용할 수 있는 명령으로 모델을 호출합니다.

    # Set the model up with tools.house_fns = [power_disco_ball, start_music, dim_lights]model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools=house_fns)# Call the API.chat = model.start_chat()response = chat.send_message("Turn this place into a party!")# Print out each of the function calls requested from this single call.for part in response.parts:    if fn := part.function_call:        args = ", ".join(f"{key}={val}" for key, val in fn.args.items())        print(f"{fn.name}({args})")

power\_disco\_ball(power=True)
start\_music(energetic=True, loud=True, bpm=120.0)
dim\_lights(brightness=0.3)

출력된 각 결과는 모델이 요청한 단일 함수 호출을 반영합니다. 결과를 다시 보내려면 요청된 순서와 동일한 순서로 응답을 포함하세요.

    # Simulate the responses from the specified tools.responses = {    "power_disco_ball": True,    "start_music": "Never gonna give you up.",    "dim_lights": True,}# Build the response parts.response_parts = [    genai.protos.Part(function_response=genai.protos.FunctionResponse(name=fn, response={"result": val}))    for fn, val in responses.items()]response = chat.send_message(response_parts)print(response.text)

Let's get this party started! I've turned on the disco ball, started playing some upbeat music, and dimmed the lights. 🎶✨  Get ready to dance! 🕺💃

(선택사항) 낮은 수준의 액세스
-----------------

모든 경우에 Python 함수에서 스키마 자동 추출이 작동하지는 않습니다. 예를 들어 중첩된 사전 객체의 필드를 설명하는 사례는 처리하지 않지만 API는 이를 지원합니다. API는 다음 유형을 설명할 수 있습니다.

    AllowedType = (int | float | bool | str | list['AllowedType'] | dict[str, AllowedType]

[`google.ai.generativelanguage`](https://ai.google.dev/api/python/google/generativeai/protos?hl=ko) 클라이언트 라이브러리는 하위 수준 유형에 대한 액세스를 제공하여 완전한 제어 기능을 제공합니다.

먼저 모델의 `_tools` 속성을 살펴보면 모델에 전달한 함수를 어떻게 설명하는지 확인할 수 있습니다.

    def multiply(a:float, b:float):    """returns a * b."""    return a*bmodel = genai.GenerativeModel(model_name='gemini-1.5-flash',                             tools=[multiply])model._tools.to_proto()

\[function\_declarations {
   name: "multiply"
   description: "returns a \* b."
   parameters {
     type\_: OBJECT
     properties {
       key: "b"
       value {
         type\_: NUMBER
       }
     }
     properties {
       key: "a"
       value {
         type\_: NUMBER
       }
     }
     required: "a"
     required: "b"
   }
 }\]

이렇게 하면 API로 전송될 `genai.protos.Tool` 객체 목록이 반환됩니다. 출력된 형식이 익숙하지 않은 경우 Google protobuf 클래스이기 때문입니다. 각 `genai.protos.Tool` (여기서는 1)에는 함수와 인수를 설명하는 `genai.protos.FunctionDeclarations` 목록이 포함됩니다.

다음은 `genai.protos` 클래스를 사용하여 작성된 동일한 곱셈 함수에 관한 선언입니다.

이러한 클래스는 API의 함수를 설명할 뿐이며 함수의 구현을 포함하지 않습니다. 따라서 자동 함수 호출에서는 이를 사용할 수 없지만 함수에 항상 구현이 필요하지는 않습니다.

    calculator = genai.protos.Tool(    function_declarations=[      genai.protos.FunctionDeclaration(        name='multiply',        description="Returns the product of two numbers.",        parameters=genai.protos.Schema(            type=genai.protos.Type.OBJECT,            properties={                'a':genai.protos.Schema(type=genai.protos.Type.NUMBER),                'b':genai.protos.Schema(type=genai.protos.Type.NUMBER)            },            required=['a','b']        )      )    ])

마찬가지로 이를 JSON 호환 객체로 설명할 수 있습니다.

    calculator = {'function_declarations': [      {'name': 'multiply',       'description': 'Returns the product of two numbers.',       'parameters': {'type_': 'OBJECT',       'properties': {         'a': {'type_': 'NUMBER'},         'b': {'type_': 'NUMBER'} },       'required': ['a', 'b']} }]}

    genai.protos.Tool(calculator)

function\_declarations {
  name: "multiply"
  description: "Returns the product of two numbers."
  parameters {
    type\_: OBJECT
    properties {
      key: "b"
      value {
        type\_: NUMBER
      }
    }
    properties {
      key: "a"
      value {
        type\_: NUMBER
      }
    }
    required: "a"
    required: "b"
  }
}

어느 쪽이든 `genai.protos.Tool` 표현 또는 도구 목록을

    model = genai.GenerativeModel('gemini-1.5-flash', tools=calculator)chat = model.start_chat()response = chat.send_message(    f"What's 234551 X 325552 ?",)

모델이 계산기의 `multiply` 함수를 호출하는 `genai.protos.FunctionCall`를 반환하기 전과 같습니다.

    response.candidates

\[index: 0
content {
  parts {
    function\_call {
      name: "multiply"
      args {
        fields {
          key: "b"
          value {
            number\_value: 325552
          }
        }
        fields {
          key: "a"
          value {
            number\_value: 234551
          }
        }
      }
    }
  }
  role: "model"
}
finish\_reason: STOP
\]

함수를 직접 실행합니다.

    fc = response.candidates[0].content.parts[0].function_callassert fc.name == 'multiply'result = fc.args['a'] * fc.args['b']result

76358547152.0

결과를 모델에 전송하고 대화를 계속 진행합니다.

    response = chat.send_message(    genai.protos.Content(    parts=[genai.protos.Part(        function_response = genai.protos.FunctionResponse(          name='multiply',          response={'result': result}))]))

요약
--

SDK에서 기본 함수 호출이 지원됩니다. 자연스러운 양방향 구조 때문에 채팅 모드를 사용하면 더 쉽게 관리할 수 있습니다. 텍스트 응답을 생성할 수 있도록 실제로 함수를 호출하고 결과를 모델로 다시 전송하는 일을 담당합니다.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-06-06(UTC)
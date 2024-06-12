---
Please provide me with more information about the mission you want to write about! I need some context to create a compelling mission statement. 

For example, tell me: "* **What is the mission for?** (e.g., a company, a project, a team, a personal goal)"
* **What are the key objectives?** (e.g., to solve a specific problem, to achieve a certain outcome, to make a positive impact)
* **What are the values and principles that guide the mission?** (e.g., innovation, sustainability, customer focus)

Once you give me more details, I can help you craft a powerful and inspiring mission statement.
---

*   이 페이지의 내용
*   [함수 호출 작동 방식](#how_it_works)
*   [지원되는 모델](#supported-models)
*   [함수 호출 모드](#function_calling_mode)
*   [cURL 샘플을 호출하는 함수](#function-calling-curl-samples)
    *   [싱글턴 curl 샘플](#function-calling-single-turn-curl-sample)
    *   [ANY 모드를 사용한 싱글턴의 예](#single-turn-any-mode)
    *   [ANY 모드 및 허용되는 함수를 사용하는 싱글턴의 예](#single-turn-using-mode-and-allowed-functions)
    *   [멀티턴 curl 예시](#function-calling-one-and-a-half-turn-curl-sample)
*   [권장사항](#best-practices)
    *   [기능 키 필드](#key-parameters-best-practices)
    *   [사용자 프롬프트](#prompt-best-practices)
    *   [샘플링 매개변수](#sampling-parameters-best-practices)
    *   [API 호출](#invoke-api-best-practices)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

함수 호출
=====

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [함수 호출 작동 방식](#how_it_works)
*   [지원되는 모델](#supported-models)
*   [함수 호출 모드](#function_calling_mode)
*   [cURL 샘플을 호출하는 함수](#function-calling-curl-samples)
    *   [싱글턴 curl 샘플](#function-calling-single-turn-curl-sample)
    *   [ANY 모드를 사용한 싱글턴의 예](#single-turn-any-mode)
    *   [ANY 모드 및 허용되는 함수를 사용하는 싱글턴의 예](#single-turn-using-mode-and-allowed-functions)
    *   [멀티턴 curl 예시](#function-calling-one-and-a-half-turn-curl-sample)
*   [권장사항](#best-practices)
    *   [기능 키 필드](#key-parameters-best-practices)
    *   [사용자 프롬프트](#prompt-best-practices)
    *   [샘플링 매개변수](#sampling-parameters-best-practices)
    *   [API 호출](#invoke-api-best-practices)

커스텀 함수를 정의하고 함수 호출을 사용하여 생성형 AI 모델에 제공할 수 있습니다. 모델은 이러한 함수를 직접 호출하지 않고 대신 함수 이름과 추천 인수를 지정하는 구조화된 데이터 출력을 생성합니다. 이 출력을 통해 외부 API를 호출할 수 있으며, 생성된 API 출력을 모델에 다시 통합할 수 있으므로 보다 포괄적인 쿼리 응답이 가능합니다. 함수 호출은 LLM이 실시간 정보 및 데이터베이스, 고객 관계 관리 시스템, 문서 저장소와 같은 다양한 서비스와 상호작용할 수 있도록 지원하여 관련성 있는 상황별 답변을 제공하는 기능을 향상시킵니다.

**베타:** 이 기능은 베타 출시 버전입니다. 자세한 내용은 [API 버전](https://ai.google.dev/docs/api_versions?hl=ko) 페이지를 참조하세요.

함수 호출 작동 방식
-----------

함수는 _함수 선언_을 사용하여 설명됩니다. 쿼리의 함수 선언 목록을 언어 모델에 전달하면 모델은 함수 이름과 인수가 포함된 [OpenAPI 호환 스키마](https://spec.openapis.org/oas/v3.0.3#schema) 형식의 객체를 반환하고 반환된 함수 중 하나로 사용자 쿼리에 응답하려고 시도합니다. 언어 모델은 함수 선언을 분석하여 함수의 목적을 이해합니다. 모델은 실제로 함수를 호출하지 않습니다. 대신 개발자가 응답에서 [OpenAPI 호환 스키마](https://spec.openapis.org/oas/v3.0.3#schema) 객체를 사용하여 모델이 반환하는 함수를 호출합니다.

함수 호출을 구현할 때는 하나 이상의 _함수 선언_을 생성한 다음 모델에 전달되는 `tools` 객체에 함수 선언을 추가합니다. 각 함수 선언에는 다음을 포함하는 하나의 함수에 대한 정보가 포함됩니다.

*   함수 이름
*   [OpenAPI 호환 스키마](https://spec.openapis.org/oas/v3.0.3#schemawr) 형식의 함수 매개변수 [일부 하위 집합](https://ai.google.dev/api/rest/v1beta/Tool?hl=ko#Schema)이 지원됩니다. curl을 사용할 때는 JSON을 사용하여 스키마를 지정합니다.
*   함수 설명입니다(선택사항). 최상의 결과를 얻으려면 설명을 포함하는 것이 좋습니다.

Gemini API는 한 번에 여러 함수를 호출할 수 있는 동시 함수 호출도 지원합니다.

이 문서에는 `GenerativeModel` 클래스와 해당 메서드를 사용하여 REST 호출을 실행하는 curl 예가 포함되어 있습니다.

*   [함수 호출 curl 샘플](#function-calling-curl-samples)

지원되는 모델
-------

함수 호출을 지원하는 모델은 다음과 같습니다.

*   `gemini-1.0-pro`
*   `gemini-1.0-pro-001`
*   `gemini-1.5-flash-latest`
*   `gemini-1.5-pro-latest`

함수 호출 모드
--------

_mode_를 호출하는 함수를 사용하여 함수 호출의 실행 동작을 정의할 수 있습니다. 다음과 같은 세 가지 모드를 사용할 수 있습니다.

*   **`AUTO`**: 기본 모델 동작입니다. 모델은 함수 호출 또는 자연어 응답을 예측하기로 결정합니다
*   **`ANY`**: 모델은 항상 함수 호출을 예측하도록 제한됩니다. `allowed_function_names`가 제공되지 _않으면_ 모델은 사용 가능한 모든 함수 선언 중에서 선택합니다. `allowed_function_names`가 _제공_되면 모델은 허용되는 함수 집합 중에서 선택합니다.
*   **`NONE`**: 모델은 함수 호출을 예측하지 않습니다. 이 경우 모델 동작은 함수 선언을 전달하지 않는 경우와 동일합니다.

`allowed_function_names` 집합이 제공된 경우 모델이 호출할 함수를 제한하는 집합을 전달할 수도 있습니다. 모드가 `ANY`인 경우에만 `allowed_function_names`를 포함해야 합니다. 함수 이름은 함수 선언 이름과 일치해야 합니다. 모드가 `ANY`로 설정되고 `allowed_function_names`가 설정되면 모델은 제공된 함수 이름 집합에서 함수 호출을 예측합니다.

다음은 모드를 `ANY`로 설정하고 허용되는 함수 목록을 지정하는 [요청 예](#single-turn-using-mode-and-allowed-functions)의 일부입니다.

    "tool_config": {  "function_calling_config": {    "mode": "ANY",    "allowed_function_names": ["find_theaters", "get_showtimes"]  },}

cURL 샘플을 호출하는 함수
----------------

cURL을 사용하면 함수와 매개변수 정보가 `tools` 요소에 포함됩니다. `tools` 요소의 각 함수 선언에는 함수 이름, [OpenAPI 호환 스키마](https://spec.openapis.org/oas/v3.0.3#schema)를 사용하여 지정된 매개변수, 함수 설명이 포함됩니다. 다음 샘플은 함수 호출과 함께 curl 명령어를 사용하는 방법을 보여줍니다.

### 싱글턴 curl 샘플

싱글턴은 언어 모델을 한 번 호출하는 경우입니다. 함수 호출의 경우 싱글턴 사용 사례는 모델에 자연어 쿼리와 함수 목록을 제공하는 것일 수 있습니다. 이 경우 모델은 함수 이름, 매개변수, 설명이 포함된 함수 선언을 사용하여 호출할 함수와 호출할 인수를 예측합니다.

다음 curl 샘플은 영화 재생 위치에 관한 정보를 반환하는 함수의 설명을 전달하는 예입니다. 요청에는 `find_movies` 및 `find_theaters`와 같은 여러 함수 선언이 포함됩니다.

#### 싱글턴 함수 호출 curl 예시 응답

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": {
      "role": "user",
      "parts": {
        "text": "Which theaters in Mountain View show Barbie movie?"
    }
  },
  "tools": \[
    {
      "function\_declarations": \[
        {
          "name": "find\_movies",
          "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "description": {
                "type": "string",
                "description": "Any kind of description including category or genre, title words, attributes, etc."
              }
            },
            "required": \[
              "description"
            \]
          }
        },
        {
          "name": "find\_theaters",
          "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              }
            },
            "required": \[
              "location"
            \]
          }
        },
        {
          "name": "get\_showtimes",
          "description": "Find the start times for movies playing in a specific theater",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              },
              "theater": {
                "type": "string",
                "description": "Name of the theater"
              },
              "date": {
                "type": "string",
                "description": "Date for requested showtime"
              }
            },
            "required": \[
              "location",
              "movie",
              "theater",
              "date"
            \]
          }
        }
      \]
    }
  \]
}'
    

이 curl 예시에 대한 응답은 다음과 유사할 수 있습니다.

#### 싱글턴 함수 호출 curl 예시 응답

\[{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "functionCall": {
              "name": "find\_theaters",
              "args": {
                "movie": "Barbie",
                "location": "Mountain View, CA"
              }
            }
          }
        \]
      },
      "finishReason": "STOP",
      "safetyRatings": \[
        {
          "category": "HARM\_CATEGORY\_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HATE\_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
          "probability": "NEGLIGIBLE"
        }
      \]
    }
  \],
  "usageMetadata": {
    "promptTokenCount": 9,
    "totalTokenCount": 9
  }
}\]
    

### ANY 모드를 사용한 싱글턴의 예

다음 curl 예는 [싱글턴 예](#function-calling-single-turn-curl-sample)와 비슷하지만 [mode](#function_calling_mode)를 `ANY`로 설정합니다.

    "tool_config": {  "function_calling_config": {    "mode": "ANY"  },}

#### ANY 모드를 사용하여 싱글턴 함수 호출 (요청)

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": {
      "role": "user",
      "parts": {
        "text": "What movies are showing in North Seattle tonight?"
    }
  },
  "tools": \[
    {
      "function\_declarations": \[
        {
          "name": "find\_movies",
          "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "description": {
                "type": "string",
                "description": "Any kind of description including category or genre, title words, attributes, etc."
              }
            },
            "required": \[
              "description"
            \]
          }
        },
        {
          "name": "find\_theaters",
          "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              }
            },
            "required": \[
              "location"
            \]
          }
        },
        {
          "name": "get\_showtimes",
          "description": "Find the start times for movies playing in a specific theater",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              },
              "theater": {
                "type": "string",
                "description": "Name of the theater"
              },
              "date": {
                "type": "string",
                "description": "Date for requested showtime"
              }
            },
            "required": \[
              "location",
              "movie",
              "theater",
              "date"
            \]
          }
        }
      \]
    }
  \],
  "tool\_config": {
    "function\_calling\_config": {
      "mode": "ANY"
    },
  }
}'
    

응답은 다음과 비슷합니다.

#### ANY 모드를 사용하는 싱글턴 함수 호출 (응답)

{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "functionCall": {
              "name": "find\_movies",
              "args": {
                "description": "",
                "location": "North Seattle, WA"
              }
            }
          }
        \],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0,
      "safetyRatings": \[
        {
          "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HATE\_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
          "probability": "NEGLIGIBLE"
        }
      \]
    }
  \],
  "promptFeedback": {
    "safetyRatings": \[
      {
        "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HATE\_SPEECH",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HARASSMENT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
        "probability": "NEGLIGIBLE"
      }
    \]
  }
}
    

### ANY 모드 및 허용되는 함수를 사용하는 싱글턴의 예

다음 curl 예는 [싱글턴 예](#function-calling-single-turn-curl-sample)와 비슷하지만 [mode](#function_calling_mode)를 `ANY`로 설정하며 허용되는 함수 목록을 포함합니다.

    "tool_config": {  "function_calling_config": {    "mode": "ANY",    "allowed_function_names": ["find_theaters", "get_showtimes"]  },}

#### ANY 모드 및 허용된 함수 (요청)를 사용하는 싱글턴 함수 호출

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": {
      "role": "user",
      "parts": {
        "text": "What movies are showing in North Seattle tonight?"
    }
  },
  "tools": \[
    {
      "function\_declarations": \[
        {
          "name": "find\_movies",
          "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "description": {
                "type": "string",
                "description": "Any kind of description including category or genre, title words, attributes, etc."
              }
            },
            "required": \[
              "description"
            \]
          }
        },
        {
          "name": "find\_theaters",
          "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              }
            },
            "required": \[
              "location"
            \]
          }
        },
        {
          "name": "get\_showtimes",
          "description": "Find the start times for movies playing in a specific theater",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              },
              "theater": {
                "type": "string",
                "description": "Name of the theater"
              },
              "date": {
                "type": "string",
                "description": "Date for requested showtime"
              }
            },
            "required": \[
              "location",
              "movie",
              "theater",
              "date"
            \]
          }
        }
      \]
    }
  \],
  "tool\_config": {
    "function\_calling\_config": {
      "mode": "ANY",
      "allowed\_function\_names": \["find\_theaters", "get\_showtimes"\]
    },
  }
}'
    

모델은 허용되는 함수 목록에 없는 `find_movies` 함수를 예측할 수 없으므로 대신 다른 함수를 예측합니다. 응답은 다음과 유사할 수 있습니다.

#### ANY 모드 및 허용되는 함수를 사용하는 싱글턴 함수 호출 (응답)

{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "functionCall": {
              "name": "find\_theaters",
              "args": {
                "location": "North Seattle, WA",
                "movie": null
              }
            }
          }
        \],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0,
      "safetyRatings": \[
        {
          "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HATE\_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
          "probability": "NEGLIGIBLE"
        }
      \]
    }
  \],
  "promptFeedback": {
    "safetyRatings": \[
      {
        "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HATE\_SPEECH",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HARASSMENT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
        "probability": "NEGLIGIBLE"
      }
    \]
  }
}
    

### 멀티턴 curl 예시

다음을 수행하여 멀티턴 함수 호출 시나리오를 구현할 수 있습니다.

1.  언어 모델을 호출하여 함수 호출 응답을 가져옵니다. 이번이 첫 번째 회전입니다.
2.  첫 번째 차례에서 함수 호출 응답과 해당 함수 호출에서 가져온 함수 응답을 사용하여 언어 모델을 호출합니다. 두 번째 회전입니다.

두 번째 차례의 응답은 첫 번째 차례에서 쿼리에 답변하는 결과를 요약하거나 쿼리에 대한 자세한 정보를 얻는 데 사용할 수 있는 두 번째 함수 호출을 포함합니다.

이 주제에는 다음과 같은 두 가지 멀티턴 curl 예시가 포함됩니다.

*   [이전 차례의 함수 응답을 사용하는 curl 예시](#multi-turn-example-1)
*   [언어 모델을 여러 번 호출하는 curl의 예시](#multi-turn-example-2)

#### 이전 차례의 응답을 사용하는 curl 예시

다음 curl 샘플은 이전의 싱글턴 예시에서 반환된 함수와 인수를 호출하여 응답을 가져옵니다. 싱글턴 예에서 반환하는 메서드와 매개변수는 이 JSON에 있습니다.

    "functionCall": {  "name": "find_theaters",  "args": {    "movie": "Barbie",    "location": "Mountain View, CA"  }}

#### 멀티턴 함수 호출 curl 예시 요청

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": \[{
      "role": "user",
      "parts": \[{
        "text": "Which theaters in Mountain View show Barbie movie?"
    }\]
  }, {
    "role": "model",
    "parts": \[{
      "functionCall": {
        "name": "find\_theaters",
        "args": {
          "location": "Mountain View, CA",
          "movie": "Barbie"
        }
      }
    }\]
  }, {
    "role": "function",
    "parts": \[{
      "functionResponse": {
        "name": "find\_theaters",
        "response": {
          "name": "find\_theaters",
          "content": {
            "movie": "Barbie",
            "theaters": \[{
              "name": "AMC Mountain View 16",
              "address": "2000 W El Camino Real, Mountain View, CA 94040"
            }, {
              "name": "Regal Edwards 14",
              "address": "245 Castro St, Mountain View, CA 94040"
            }\]
          }
        }
      }
    }\]
  }\],
  "tools": \[{
    "functionDeclarations": \[{
      "name": "find\_movies",
      "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "description": {
            "type": "STRING",
            "description": "Any kind of description including category or genre, title words, attributes, etc."
          }
        },
        "required": \["description"\]
      }
    }, {
      "name": "find\_theaters",
      "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "movie": {
            "type": "STRING",
            "description": "Any movie title"
          }
        },
        "required": \["location"\]
      }
    }, {
      "name": "get\_showtimes",
      "description": "Find the start times for movies playing in a specific theater",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "movie": {
            "type": "STRING",
            "description": "Any movie title"
          },
          "theater": {
            "type": "STRING",
            "description": "Name of the theater"
          },
          "date": {
            "type": "STRING",
            "description": "Date for requested showtime"
          }
        },
        "required": \["location", "movie", "theater", "date"\]
      }
    }\]
  }\]
}'
    

이 curl 예에 대한 응답에는 `find_theaters` 메서드 호출의 결과가 포함됩니다. 응답은 다음과 비슷합니다.

#### 멀티턴 함수 호출 curl 예시 응답

{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "text": " OK. Barbie is showing in two theaters in Mountain View, CA: AMC Mountain View 16 and Regal Edwards 14."
          }
        \]
      }
    }
  \],
  "usageMetadata": {
    "promptTokenCount": 9,
    "candidatesTokenCount": 27,
    "totalTokenCount": 36
  }
}
    

#### 언어 모델을 여러 번 호출하는 curl의 예시

다음 curl 예에서는 언어 모델을 여러 번 호출하여 함수를 호출합니다. 모델이 함수를 호출할 때마다 다른 함수를 사용하여 요청 시 다른 사용자 쿼리에 응답할 수 있습니다.

#### 멀티턴 함수 호출 curl 예시 요청

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": \[{
      "role": "user",
      "parts": \[{
        "text": "Which theaters in Mountain View show Barbie movie?"
    }\]
  }, {
    "role": "model",
    "parts": \[{
      "functionCall": {
        "name": "find\_theaters",
        "args": {
          "location": "Mountain View, CA",
          "movie": "Barbie"
        }
      }
    }\]
  }, {
    "role": "function",
    "parts": \[{
      "functionResponse": {
        "name": "find\_theaters",
        "response": {
          "name": "find\_theaters",
          "content": {
            "movie": "Barbie",
            "theaters": \[{
              "name": "AMC Mountain View 16",
              "address": "2000 W El Camino Real, Mountain View, CA 94040"
            }, {
              "name": "Regal Edwards 14",
              "address": "245 Castro St, Mountain View, CA 94040"
            }\]
          }
        }
      }
    }\]
  },
  {
    "role": "model",
    "parts": \[{
      "text": " OK. Barbie is showing in two theaters in Mountain View, CA: AMC Mountain View 16 and Regal Edwards 14."
    }\]
  },{
    "role": "user",
    "parts": \[{
      "text": "Can we recommend some comedy movies on show in Mountain View?"
    }\]
  }\],
  "tools": \[{
    "functionDeclarations": \[{
      "name": "find\_movies",
      "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "description": {
            "type": "STRING",
            "description": "Any kind of description including category or genre, title words, attributes, etc."
          }
        },
        "required": \["description"\]
      }
    }, {
      "name": "find\_theaters",
      "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "movie": {
            "type": "STRING",
            "description": "Any movie title"
          }
        },
        "required": \["location"\]
      }
    }, {
      "name": "get\_showtimes",
      "description": "Find the start times for movies playing in a specific theater",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "movie": {
            "type": "STRING",
            "description": "Any movie title"
          },
          "theater": {
            "type": "STRING",
            "description": "Name of the theater"
          },
          "date": {
            "type": "STRING",
            "description": "Date for requested showtime"
          }
        },
        "required": \["location", "movie", "theater", "date"\]
      }
    }\]
  }\]
}'
    

#### 멀티턴 함수 호출 curl 예시 응답

\[{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "functionCall": {
              "name": "find\_movies",
              "args": {
                "description": "comedy",
                "location": "Mountain View, CA"
              }
            }
          }
        \]
      },
      "finishReason": "STOP",
      "safetyRatings": \[
        {
          "category": "HARM\_CATEGORY\_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HATE\_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
          "probability": "NEGLIGIBLE"
        }
      \]
    }
  \],
  "usageMetadata": {
    "promptTokenCount": 48,
    "totalTokenCount": 48
  }
}
\]
    

권장사항
----

함수 호출의 정확성과 안정성을 개선하려면 다음 권장사항을 따르세요.

### 기능 키 필드

요청에 함수를 통합할 때 함수를 정확하게 정의하는 것이 중요합니다. 각 함수는 모델의 동작과 상호작용을 안내하는 특정 매개변수를 사용합니다. 다음은 `functions_declarations` 배열 내에서 사용되는 주요 매개변수의 세부정보입니다.

**`function_declarations` (배열)**:

*   각각 고유한 함수를 나타내는 하나 이상의 객체를 포함합니다.

각 `function_declarations` 객체 내에서 다음을 실행합니다.

*   **`name` (문자열)**: API 호출 내 함수의 고유 식별자입니다.
    *   **권장사항**: 공백, 마침표 (`.`) 또는 대시 (`-`) 문자 없이 명확하고 설명이 포함된 이름을 사용하세요. 대신 밑줄 (`_`) 문자나 카멜 표기법을 사용하세요.
*   **`description` (문자열)**: 함수의 목적과 기능에 관한 포괄적인 설명입니다.
    *   **권장사항**: 상세하고 명확하며 구체적인 함수 설명을 작성하고 필요한 경우 예를 제공하세요. 예를 들어 `find theaters` 대신 `find theaters based on location and optionally movie title that is currently playing in theaters.`를 사용합니다. 지나치게 광범위하거나 모호한 설명은 피합니다.
*   **`parameters` (객체)**: 함수에 필요한 입력 데이터를 정의합니다.
    *   **`type` (문자열)**: 전체 데이터 유형 (예: `object`).
    *   **`properties` (객체)**:
        *   다음을 포함하는 개별 매개변수를 나열합니다.
            *   **`type` (문자열)**: 매개변수의 데이터 유형 (예: `string`, `integer`, `boolean`).
                *   **권장사항**: 강타입 매개변수를 사용하여 모델 할루시네이션을 줄이세요. 예를 들어 매개변수 값이 유한집합에서 비롯된 경우 설명에 값을 나열하는 대신 `enum` 필드를 사용합니다 (예: `"type": "enum", "values": ["now_playing", "upcoming"]`). 매개변수 값이 항상 정수이면 유형을 `number`가 아닌 `integer`로 설정합니다.
            *   **`description` (문자열)**: 매개변수의 목적과 예상 형식에 관한 명확한 설명
                *   **권장사항**: 구체적인 예와 제약 조건을 제공하세요. 예를 들어 `the location to search` 대신 `The city and state, e.g. San Francisco, CA or a zip code e.g. 95616`를 사용합니다.
    *   **`required` (배열)**:
        *   함수가 작동하는 데 필요한 매개변수 이름이 나열된 문자열 배열입니다.

### 사용자 프롬프트

최상의 결과를 얻으려면 사용자 쿼리 앞에 다음 세부정보를 추가합니다.

*   모델의 추가 컨텍스트입니다. 예: `You are a movie API assistant to help users find movies and showtimes based on their preferences.`
*   함수 사용 방법 및 시기에 대한 세부정보 또는 지침입니다. 예: `Don't make assumptions on showtimes. Always use a future date for showtimes.`
*   사용자 쿼리가 모호한 경우 명확한 질문을 하는 방법을 안내합니다. 예: `Ask clarifying questions if not enough information is available to complete the request.`

### 샘플링 매개변수

강도 매개변수에는 `0` 또는 다른 낮은 값을 사용합니다. 이렇게 하면 모델이 보다 신뢰할 수 있는 결과를 생성하도록 할 수 있고 할루시네이션을 줄일 수 있습니다.

### API 호출

모델이 주문을 전송하거나, 데이터베이스를 업데이트하거나, 그 밖의 이유로 중대한 결과가 발생할 수 있는 함수의 호출을 제안하는 경우에는 이를 실행하기 전에 사용자와 함께 함수 호출 유효성을 검사합니다.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-24(UTC)
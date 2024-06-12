---
Please provide me with the rest of the mission statement! I need more context to understand what the mission is about.  

For example, tell me: "* **What organization or entity is this mission for?** (A company, a school, a non-profit, etc.)"
* **What is the purpose or goal of this organization?** What does it aim to achieve?
* **What are the key values or principles that guide the organization?** 

Once I have this information, I can help you complete the mission statement and make it compelling and clear.
---

*   이 페이지의 내용
*   [설정](#setup)
    *   [인증](#authenticate)
*   [CURL로 REST API 호출](#calling_the_rest_api_with_curl)
    *   [변수 설정](#set_variables)
    *   [조정된 모델 나열](#list_tuned_models)
    *   [미세 조정된 모델 만들기](#create_tuned_model)
    *   [조정된 모델 상태 가져오기](#get_tuned_model_state)
    *   [추론 실행](#run_inference)
*   [Python 요청으로 REST API 호출](#call_the_rest_api_with_python_requests)
    *   [변수 설정](#set_variables_2)
    *   [조정된 모델 나열](#list_tuned_models_2)
    *   [미세 조정된 모델 만들기](#create_tuned_model_2)
    *   [조정된 모델 상태 가져오기](#get_tuned_model_state_2)
    *   [추론 실행](#run_inference_2)
*   [결론](#conclusion)
*   [다음 단계](#next_steps)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

REST API: 모델 조정
===============

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [설정](#setup)
    *   [인증](#authenticate)
*   [CURL로 REST API 호출](#calling_the_rest_api_with_curl)
    *   [변수 설정](#set_variables)
    *   [조정된 모델 나열](#list_tuned_models)
    *   [미세 조정된 모델 만들기](#create_tuned_model)
    *   [조정된 모델 상태 가져오기](#get_tuned_model_state)
    *   [추론 실행](#run_inference)
*   [Python 요청으로 REST API 호출](#call_the_rest_api_with_python_requests)
    *   [변수 설정](#set_variables_2)
    *   [조정된 모델 나열](#list_tuned_models_2)
    *   [미세 조정된 모델 만들기](#create_tuned_model_2)
    *   [조정된 모델 상태 가져오기](#get_tuned_model_state_2)
    *   [추론 실행](#run_inference_2)
*   [결론](#conclusion)
*   [다음 단계](#next_steps)

<table align="left" class="tfo-notebook-buttons"><tbody><tr><td><a href="https://ai.google.dev/gemini-api/docs/model-tuning/rest?hl=ko" target="_blank"><img height="32" src="https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png?hl=ko" width="32">ai.google.dev에서 보기</a></td><td><a href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/model-tuning/rest.ipynb?hl=ko" target="_blank"><img src="https://www.tensorflow.org/images/colab_logo_32px.png?hl=ko">Google Colab에서 실행</a></td><td><a href="https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/model-tuning/rest.ipynb" target="_blank"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=ko">GitHub에서 소스 보기</a></td></tr></tbody></table>

이 노트북에서는 curl 명령어 또는 Python 요청 API를 사용하여 Gemini API를 호출하여 Gemini API 조정 서비스를 시작하는 방법을 알아봅니다. 여기에서는 Gemini API의 텍스트 생성 서비스를 기반으로 텍스트 모델을 조정하는 방법을 알아봅니다.

**참고:** 현재 `gemini-1.0-pro-001` 모델에서만 미세 조정을 사용할 수 있습니다.

설정
--

### 인증

Gemini API를 사용하면 자체 데이터를 기반으로 모델을 조정할 수 있습니다. 사용자의 데이터와 조정된 모델이므로 API 키가 제공할 수 있는 것보다 더 엄격한 액세스 제어가 필요합니다.

이 튜토리얼을 실행하려면 먼저 [프로젝트의 OAuth를 설정](https://ai.google.dev/gemini-api/docs/oauth?hl=ko)해야 합니다.

Colab에서 가장 쉽게 설정하는 방법은 `client_secret.json` 파일의 콘텐츠를 Colab의 'Secret Manager'(왼쪽 패널의 열쇠 아이콘 아래)에 보안 비밀 이름(`CLIENT_SECRET`)으로 복사하는 것입니다.

이 gcloud 명령어는 `client_secret.json` 파일을 서비스 인증에 사용할 수 있는 사용자 인증 정보로 변환합니다.

> **중요:** Colab에서 이 프로그램을 실행하는 경우 **출력되는 링크를 클릭하지 마세요**. 이 작업은 실패합니다. 안내에 따라 출력되는 `gcloud` 명령어를 로컬 머신에 복사하여 거기에서 실행한 다음, 로컬 머신의 출력을 다시 여기에 붙여넣습니다.

    try:  from google.colab import userdata  import pathlib  pathlib.Path('client_secret.json').write_text(userdata.get('CLIENT_SECRET'))  # Use `--no-browser` in colab  !gcloud auth application-default login --no-browser --client-id-file client_secret.json --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.tuning'except ImportError:  !gcloud auth application-default login --client-id-file client_secret.json --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.tuning'

You are authorizing client libraries without access to a web browser. Please run the following command on a machine with a web browser and copy its output back here. Make sure the installed gcloud version is 372.0.0 or newer.

gcloud auth application-default login --remote-bootstrap="https://accounts.google.com/o/oauth2/auth?response\_type=code&client\_id=87071151422-n1a3cb6c7fvkfg4gmhdtmn5ulol2l4be.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgenerative-language.tuning&state=QIyNibWSaTIsozjmvZEkVBo6EcoW0G&access\_type=offline&code\_challenge=76c1ZiGvKN8cvlYfj3BmbCwE4e7tvrlwaX3REUX25gY&code\_challenge\_method=S256&token\_usage=remote"


Enter the output of the above command: https://localhost:8085/?state=QIyNibWSaTIsozjmvZEkVBo6EcoW0G&code=4/0AeaYSHBKrY911S466QjKQIFODoOPXlO1mWyTYYdrbELIDV6Hw2DKRAyro62BugroSvIWsA&scope=https://www.googleapis.com/auth/cloud-platform%20https://www.googleapis.com/auth/generative-language.tuning

Credentials saved to file: \[/content/.config/application\_default\_credentials.json\]

These credentials will be used by any library that requests Application Default Credentials (ADC).

CURL로 REST API 호출
-----------------

이 섹션에서는 REST API를 호출하는 curl 문의 예를 제공합니다. 조정 작업을 만들고 상태를 확인하며 완료되면 추론을 호출하는 방법을 알아봅니다.

### 변수 설정

나머지 REST API 호출에 사용할 반복 값의 변수를 설정합니다. 이 코드는 Python `os` 라이브러리를 사용하여 모든 코드 셀에서 액세스할 수 있는 환경 변수를 설정합니다.

이는 Colab 노트북 환경에만 적용됩니다. 다음 코드 셀의 코드는 bash 터미널에서 다음 명령어를 실행하는 것과 같습니다.

    export access_token=$(gcloud auth application-default print-access-token)export project_id=my-project-idexport base_url=https://generativelanguage.googleapis.com

    import osaccess_token = !gcloud auth application-default print-access-tokenaccess_token = '\n'.join(access_token)os.environ['access_token'] = access_tokenos.environ['project_id'] = "[Enter your project-id here]"os.environ['base_url'] = "https://generativelanguage.googleapis.com"

### 조정된 모델 나열

현재 사용 가능한 조정된 모델을 나열하여 인증 설정을 확인합니다.

    

### 미세 조정된 모델 만들기

조정된 모델을 만들려면 `training_data` 필드의 모델에 데이터 세트를 전달해야 합니다.

이 예에서는 시퀀스의 다음 숫자를 생성하도록 모델을 조정합니다. 예를 들어 입력이 `1`이면 모델은 `2`를 출력해야 합니다. 입력이 `one hundred`이면 출력은 `one hundred one`입니다.

    

{
  "name": "tunedModels/number-generator-model-dzlmi0gswwqb/operations/bvl8dymw0fhw",
  "metadata": {
    "@type": "type.googleapis.com/google.ai.generativelanguage.v1beta.CreateTunedModelMetadata",
    "totalSteps": 38,
    "tunedModel": "tunedModels/number-generator-model-dzlmi0gswwqb"
  }
}
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2280    0   296  100  1984    611   4098 --:--:-- --:--:-- --:--:--  4720

### 조정된 모델 상태 가져오기

학습 중에는 모델의 상태가 `CREATING`로 설정되며 완료되면 `ACTIVE`로 변경됩니다.

다음은 응답 JSON에서 생성된 모델 이름을 파싱하는 Python 코드입니다. 터미널에서 이를 실행하는 경우 bash JSON 파서를 사용하여 응답을 파싱해 볼 수 있습니다.

    import jsonfirst_page = json.load(open('tunemodel.json'))os.environ['modelname'] = first_page['metadata']['tunedModel']print(os.environ['modelname'])

tunedModels/number-generator-model-dzlmi0gswwqb

모델 이름으로 다른 `GET` 요청을 수행하여 상태 필드가 포함된 모델 메타데이터를 가져옵니다.

    

"state": "ACTIVE",
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  5921    0  5921    0     0  13164      0 --:--:-- --:--:-- --:--:-- 13157

### 추론 실행

조정 작업이 완료되면 이를 사용하여 텍스트 서비스로 텍스트를 생성할 수 있습니다. 로마 숫자(예: 63(LXIII)를 입력해 보세요.

    

{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "text": "LXIV"
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

모델의 출력이 올바르지 않을 수도 있습니다. 조정된 모델이 필요한 기준에 미치지 못하는 경우 고품질 예를 추가하거나 초매개변수를 조정하거나 예시에 서문을 추가해 볼 수 있습니다. 처음에 만든 모델을 기반으로 또 다른 조정된 모델을 만들 수도 있습니다.

성능 개선에 대한 자세한 안내는 [조정 가이드](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ko)를 참고하세요.

Python 요청으로 REST API 호출
-----------------------

http 요청 전송을 허용하는 모든 라이브러리에서 나머지 API를 호출할 수 있습니다. 다음 예제 세트에서는 Python 요청 라이브러리를 사용하며 몇 가지 고급 기능을 보여줍니다.

### 변수 설정

    access_token = !gcloud auth application-default print-access-tokenaccess_token = '\n'.join(access_token)project = '[Enter your project-id here]'base_url = "https://generativelanguage.googleapis.com"

`requests` 라이브러리를 가져옵니다.

    import requestsimport json

### 조정된 모델 나열

현재 사용 가능한 조정된 모델을 나열하여 인증 설정을 확인합니다.

    headers={  'Authorization': 'Bearer ' + access_token,  'Content-Type': 'application/json',  'x-goog-user-project': project}result = requests.get(  url=f'{base_url}/v1beta/tunedModels',  headers = headers,)

    result.json()

### 미세 조정된 모델 만들기

Curl 예와 마찬가지로 `training_data` 필드를 통해 데이터 세트를 전달합니다.

    operation = requests.post(    url = f'{base_url}/v1beta/tunedModels',    headers=headers,    json= {        "display_name": "number generator",        "base_model": "models/gemini-1.0-pro-001",        "tuning_task": {          "hyperparameters": {            "batch_size": 4,            "learning_rate": 0.001,            "epoch_count":5,          },          "training_data": {            "examples": {              "examples": [                {                    'text_input': '1',                    'output': '2',                },{                    'text_input': '3',                    'output': '4',                },{                    'text_input': '-3',                    'output': '-2',                },{                    'text_input': 'twenty two',                    'output': 'twenty three',                },{                    'text_input': 'two hundred',                    'output': 'two hundred one',                },{                    'text_input': 'ninety nine',                    'output': 'one hundred',                },{                    'text_input': '8',                    'output': '9',                },{                    'text_input': '-98',                    'output': '-97',                },{                    'text_input': '1,000',                    'output': '1,001',                },{                    'text_input': '10,100,000',                    'output': '10,100,001',                },{                    'text_input': 'thirteen',                    'output': 'fourteen',                },{                    'text_input': 'eighty',                    'output': 'eighty one',                },{                    'text_input': 'one',                    'output': 'two',                },{                    'text_input': 'three',                    'output': 'four',                },{                    'text_input': 'seven',                    'output': 'eight',                }              ]            }          }        }      })

    operation

<Response \[200\]>

    operation.json()

{'name': 'tunedModels/number-generator-wl1qr34x2py/operations/41vni3zk0a47',
 'metadata': {'@type': 'type.googleapis.com/google.ai.generativelanguage.v1beta.CreateTunedModelMetadata',
  'totalSteps': 19,
  'tunedModel': 'tunedModels/number-generator-wl1qr34x2py'} }

나머지 호출에 사용할 조정된 모델의 이름으로 변수를 설정합니다.

    name=operation.json()["metadata"]["tunedModel"]name

'tunedModels/number-generator-wl1qr34x2py'

### 조정된 모델 상태 가져오기

상태 필드를 확인하여 조정 작업의 진행 상황을 확인할 수 있습니다. `CREATING`은 조정 작업이 아직 진행 중임을 의미하며 `ACTIVE`는 학습이 완료되었으며 조정된 모델을 사용할 준비가 되었음을 의미합니다.

    tuned_model = requests.get(    url = f'{base_url}/v1beta/{name}',    headers=headers,)

    tuned_model.json()

아래 코드는 더 이상 `CREATING` 상태가 될 때까지 5초마다 상태 필드를 확인합니다.

    import timeimport pprintop_json = operation.json()response = op_json.get('response')error = op_json.get('error')while response is None and error is None:    time.sleep(5)    operation = requests.get(        url = f'{base_url}/v1/{op_json["name"]}',        headers=headers,    )    op_json = operation.json()    response = op_json.get('response')    error = op_json.get('error')    percent = op_json['metadata'].get('completedPercent')    if percent is not None:      print(f"{percent:.2f}% - {op_json['metadata']['snapshots'][-1]}")      print()if error is not None:    raise Exception(error)

100.00% - {'step': 19, 'epoch': 5, 'meanLoss': 1.402067, 'computeTime': '2024-03-14T15:11:23.766989274Z'}

### 추론 실행

조정 작업이 완료되면 기본 텍스트 모델과 동일한 방식으로 기본 텍스트 모델을 사용하여 텍스트를 생성할 수 있습니다. 일본어 숫자, 예를 들어 6 (사)을 입력해 봅니다.

    import timem = requests.post(    url = f'{base_url}/v1beta/{name}:generateContent',    headers=headers,    json= {         "contents": [{             "parts": [{                 "text": "六"             }]          }]    })

    import pprintpprint.pprint(m.json())

{'candidates': \[{'content': {'parts': \[{'text': '七'}\], 'role': 'model'},
                 'finishReason': 'STOP',
                 'index': 0,
                 'safetyRatings': \[{'category': 'HARM\_CATEGORY\_SEXUALLY\_EXPLICIT',
                                    'probability': 'NEGLIGIBLE'},
                                   {'category': 'HARM\_CATEGORY\_HATE\_SPEECH',
                                    'probability': 'NEGLIGIBLE'},
                                   {'category': 'HARM\_CATEGORY\_HARASSMENT',
                                    'probability': 'LOW'},
                                   {'category': 'HARM\_CATEGORY\_DANGEROUS\_CONTENT',
                                    'probability': 'NEGLIGIBLE'}\]}\],
 'promptFeedback': {'safetyRatings': \[{'category': 'HARM\_CATEGORY\_SEXUALLY\_EXPLICIT',
                                       'probability': 'NEGLIGIBLE'},
                                      {'category': 'HARM\_CATEGORY\_HATE\_SPEECH',
                                       'probability': 'NEGLIGIBLE'},
                                      {'category': 'HARM\_CATEGORY\_HARASSMENT',
                                       'probability': 'NEGLIGIBLE'},
                                      {'category': 'HARM\_CATEGORY\_DANGEROUS\_CONTENT',
                                       'probability': 'NEGLIGIBLE'}\]} }

모델의 출력이 올바르지 않을 수도 있습니다. 조정된 모델이 필요한 기준에 미치지 못하는 경우 고품질 예를 추가하거나 초매개변수를 조정하거나 예시에 서문을 추가해 볼 수 있습니다.

결론
--

학습 데이터에 로마나 일본어 숫자에 대한 언급은 없었지만, 미세 조정 후 모델은 일반화할 수 있었습니다. 이렇게 하면 사용 사례에 맞게 모델을 미세 조정할 수 있습니다.

다음 단계
-----

Gemini API용 Python SDK를 통해 조정 서비스를 사용하는 방법을 알아보려면 [Python을 사용한 조정 빠른 시작](https://ai.google.dev/tutorials/tuning_quickstart_python?hl=ko)을 참고하세요. Gemini API에서 다른 서비스를 사용하는 방법을 알아보려면 [Python 빠른 시작](https://ai.google.dev/tutorials/python_quickstart?hl=ko)을 방문하세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-04-26(UTC)
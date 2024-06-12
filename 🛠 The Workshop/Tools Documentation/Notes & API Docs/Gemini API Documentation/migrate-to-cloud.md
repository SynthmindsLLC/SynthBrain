---
Please provide me with more context!  I need to know what kind of mission you're writing about in order to help you complete it. 

For example, tell me: "* **What is the mission for?** (A company, a project, a personal goal?)"
* **What are the key objectives?** (What do you want to achieve?)
* **Who is the target audience?** (Who is this mission for?)
* **What are the values that guide this mission?** 

Once you give me more information, I can help you craft a compelling and impactful mission statement.
---

*   이 페이지의 내용
*   [Google AI 기반 Gemini에서 Vertex AI로 이전](#migrate-gemini)
    *   [Python: Google AI Gemini API에서 Vertex AI Gemini API로 마이그레이션](#python-migrate)
*   [사용하지 않는 API 키 삭제](#delete-unused-keys)
*   [다음 단계](#next-steps)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

Google Cloud에서 Gemini로 빌드
=========================

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [Google AI 기반 Gemini에서 Vertex AI로 이전](#migrate-gemini)
    *   [Python: Google AI Gemini API에서 Vertex AI Gemini API로 마이그레이션](#python-migrate)
*   [사용하지 않는 API 키 삭제](#delete-unused-keys)
*   [다음 단계](#next-steps)

Gemini를 처음 사용하는 경우 [빠른 시작](https://ai.google.dev/tutorials?hl=ko)을 사용하는 것이 가장 빠른 시작 방법입니다.

그렇지만 생성형 AI 솔루션이 발전함에 따라 생성형 AI 애플리케이션과 솔루션을 엔드 투 엔드로 빌드하고 배포하는 플랫폼이 필요할 수 있습니다. Google Cloud는 앱 개발 초기 단계에서 앱 배포, 앱 호스팅, 복잡한 데이터 관리에 이르기까지 개발자가 생성형 AI의 강력한 기능을 활용할 수 있도록 포괄적인 도구 생태계를 제공합니다.

Google Cloud의 Vertex AI 플랫폼은 효율성과 안정성을 위해 AI 모델의 사용, 배포, 모니터링을 간소화하는 MLOps 도구 모음을 제공합니다. 또한 데이터베이스, DevOps 도구, 로깅, 모니터링, IAM과 통합하는 경우 생성형 AI 전체 수명 주기 관리에 대한 종합적인 접근이 가능합니다.

다음 표에는 사용 사례에 적합한 옵션을 결정하는 데 도움이 되도록 Google AI와 Vertex AI의 주요 차이점이 요약되어 있습니다.

| **기능** | **Google AI Gemini API** | **Google Cloud Vertex AI Gemini API** |
| --- | --- | --- |
| 최신 Gemini 모델 | Gemini Pro 및 Gemini Ultra | Gemini Pro 및 Gemini Ultra |
| 가입 | Google 계정 | Google Cloud 계정(약관 동의 및 결제 포함) |
| 인증 | API 키 | Google Cloud 서비스 계정 |
| 사용자 인터페이스 플레이그라운드 | Google AI Studio | Vertex AI Studio |
| API 및 SDK | Python, Node.js, Android(Kotlin/Java), Swift, Go | SDK는 Python, Node.js, Java, Go를 지원합니다. |
| 무료 등급 | 예 | 신규 사용자의 경우 Google Cloud 크레딧 $300 |
| 할당량(분당 요청) | [60(증가를 요청할 수 있음)](https://ai.google.dev/docs/increase_quota?hl=ko) | 요청 시 증가(기본값: 60) |
| 엔터프라이즈 지원 | 아니요 | 고객 암호화 키  
Virtual Private Cloud  
데이터 상주  
액세스 투명성  
애플리케이션 호스팅을 위한 확장 가능한 인프라  
데이터베이스 및 데이터 스토리지 |
| MLOps | 아니요 | 완전한 Vertex AI 기반 MLOps(예: 모델 평가, 모델 모니터링, Model Registry) |

Google Cloud에서 생성형 AI 애플리케이션을 빌드하는 데 가장 적합한 제품, 프레임워크, 도구를 알아보려면 [Google Cloud에서 생성형 AI 애플리케이션 빌드](https://cloud.google.com/docs/ai-ml/generative-ai?hl=ko)를 참조하세요.

Google AI 기반 Gemini에서 Vertex AI로 이전
-----------------------------------

애플리케이션에서 Google AI Gemini API를 사용하는 경우 Google Cloud의 Vertex AI Gemini API로 마이그레이션해야 합니다.

이전하는 경우:

*   기존 Google Cloud 프로젝트(API 키를 생성하는 데 사용한 프로젝트)를 사용하거나 [새 Google Cloud 프로젝트를 생성](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ko)할 수 있습니다.
    
*   Google AI Studio와 Vertex AI 간에 지원되는 리전이 다를 수 있습니다. [Google Cloud에서 생성형 AI를 지원하는 리전](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations-genai?hl=ko) 목록을 참조하세요.
    
*   Google AI Studio에서 만든 모든 모델은 Vertex AI에서 재학습을 거쳐야 합니다.
    

### Python: Google AI Gemini API에서 Vertex AI Gemini API로 마이그레이션

다음 섹션에서는 Vertex AI Gemini API를 사용하도록 Python 코드를 마이그레이션하는 데 도움이 되는 코드 스니펫을 보여줍니다.

#### Vertex AI Python SDK 설정

Vertex AI에서는 API 키가 필요하지 않습니다. 대신 Vertex AI의 Gemini는 사용자, 그룹 또는 서비스 계정이 Vertex AI SDK를 통해 Gemini API를 호출할 수 있는 권한을 제어하는 IAM 액세스를 사용하여 관리합니다.

[인증하는 방법에는 여러 가지가 있지만](https://cloud.google.com/docs/authentication?hl=ko#auth-decision-tree) 개발 환경에서 인증하는 가장 쉬운 방법은 [Google Cloud CLI를 설치](https://cloud.google.com/sdk/docs/install?hl=ko)한 후 사용자 인증 정보를 사용하여 [CLI에 로그인](https://cloud.google.com/docs/authentication/gcloud?hl=ko#local)하는 것입니다.

Vertex AI에 추론 호출을 실행하려면 사용자 또는 서비스 계정에 [Vertex AI 사용자 역할](https://cloud.google.com/vertex-ai/docs/general/access-control?hl=ko#aiplatform.user)도 있어야 합니다.

#### 클라이언트를 설치하는 코드 예시

| Google AI | Vertex AI |
| --- | --- |
| `# To install the Python SDK, use this CLI command:   # pip install google-generativeai      from google.generativeai import GenerativeModel   from google.colab import userdata      genai.configure(userdata.get('API_KEY'))`         | `# To install the Python SDK, use this CLI command:   # pip install google-cloud-aiplatform      import vertexaifrom vertexai.generative_models          import GenerativeModel, ImagePROJECT_ID = ""REGION = ""  # e.g. us-central1   vertexai.init(project=PROJECT_ID, location=REGION)`         |

#### 텍스트 프롬프트에서 텍스트를 생성하는 코드 예시

| Google AI | Vertex AI |
| --- | --- |
| `model = GenerativeModel('gemini-1.0-pro')response = model.generate_content('The opposite of hot is')   print(response.text) #  The opposite of hot is cold.`         | `model = GenerativeModel('gemini-1.0-pro')response = model.generate_content('The opposite of hot is')   print(response.text) #  The opposite of hot is cold.`         |

#### 텍스트와 이미지에서 텍스트를 생성하는 코드 예

| Google AI | Vertex AI |
| --- | --- |
| `import PIL.Imagemultimodal_model = GenerativeModel('gemini-1.0-pro-vision')image = PIL.Image.open('image.jpg')response = multimodal_model.generate_content(['What is this picture?', image])   print(response.text) # A cat is shown in this picture.`         | `multimodal_model = GenerativeModel("gemini-1.0-pro-vision")image = Image.load_from_file("image.jpg")response = multimodal_model.generate_content(["What is shown in this image?", image])      print(response.text) # A cat is shown in this picture.`         |

#### 멀티턴 채팅을 생성하는 코드 예시

| Google AI | Vertex AI |
| --- | --- |
| `model = GenerativeModel('gemini-1.0-pro')chat = model.start_chat()      print(chat.send_message("How are you?").text)   print(chat.send_message("What can you do?").text)`         | `model = GenerativeModel("gemini-1.0-pro")chat = model.start_chat()      print(chat.send_message("How are you?").text)   print(chat.send_message("What can you do?").text)`         |

사용하지 않는 API 키 삭제
----------------

Google AI Gemini API 키를 더 이상 사용할 필요가 없으면 보안 권장사항에 따라 [삭제](https://developers.google.com/maps/api-security-best-practices?hl=ko#deleting-unused-apikeys)합니다.

다음 단계
-----

*   Vertex AI의 생성형 AI 솔루션에 대한 자세한 내용은 [Vertex AI 개요](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/overview?hl=ko)를 참조하세요.
*   [Vertex AI Gemini API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini?hl=ko) 자세히 알아보기

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-14(UTC)
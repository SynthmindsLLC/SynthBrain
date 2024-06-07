*   이 페이지의 내용
*   [목표](#objectives)
*   [기본 요건](#prerequisites)
*   [클라우드 프로젝트 설정](#set-cloud)
    *   [1\. API 사용 설정](#enable-api)
    *   [2\. OAuth 동의 화면 구성](#configure-oauth)
    *   [3\. 데스크톱 애플리케이션에 대한 사용자 인증 정보 승인](#authorize-credentials)
*   [애플리케이션 기본 사용자 인증 정보 설정](#set-application-default)
    *   [Curl](#curl)
    *   [Python](#python)
*   [다음 단계](#next-steps)
*   [사용자 인증 정보 직접 관리\[Python\]](#manage-credentials)
    *   [1\. 필요한 라이브러리 설치](#install-libs)
    *   [2\. 인증 관리자 작성](#write-credentials)
    *   [3\. 프로그램 작성](#write-program)
    *   [4\. 프로그램 실행](#run-program)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

OAuth를 통한 인증 빠른 시작
==================

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [목표](#objectives)
*   [기본 요건](#prerequisites)
*   [클라우드 프로젝트 설정](#set-cloud)
    *   [1\. API 사용 설정](#enable-api)
    *   [2\. OAuth 동의 화면 구성](#configure-oauth)
    *   [3\. 데스크톱 애플리케이션에 대한 사용자 인증 정보 승인](#authorize-credentials)
*   [애플리케이션 기본 사용자 인증 정보 설정](#set-application-default)
    *   [Curl](#curl)
    *   [Python](#python)
*   [다음 단계](#next-steps)
*   [사용자 인증 정보 직접 관리\[Python\]](#manage-credentials)
    *   [1\. 필요한 라이브러리 설치](#install-libs)
    *   [2\. 인증 관리자 작성](#write-credentials)
    *   [3\. 프로그램 작성](#write-program)
    *   [4\. 프로그램 실행](#run-program)

Gemini API를 사용하면 자체 데이터에 관해 시맨틱 검색을 실행할 수 있습니다. 이는 **사용자의 데이터**이므로 API 키보다 더 엄격한 액세스 제어가 필요합니다.

이 빠른 시작에서는 테스트 환경에 적합한 간소화된 인증 방식을 사용합니다. 프로덕션 환경의 경우 앱에 적합한 [액세스 사용자 인증 정보를 선택](https://developers.google.com/workspace/guides/create-credentials?hl=ko#choose_the_access_credential_that_is_right_for_you)하기 전에 [인증 및 승인](https://developers.google.com/workspace/guides/auth-overview?hl=ko)에 대해 알아보세요.

목표
--

*   OAuth를 위한 클라우드 프로젝트 설정
*   application-default-credentials 설정
*   `gcloud auth`를 사용하는 대신 프로그램에서 사용자 인증 정보 관리

기본 요건
-----

이 빠른 시작을 실행하려면 다음이 필요합니다.

*   [Google Cloud 프로젝트](https://developers.google.com/workspace/guides/create-project?hl=ko)
*   [gcloud CLI의 로컬 설치](https://cloud.google.com/sdk/docs/install?hl=ko)

클라우드 프로젝트 설정
------------

이 빠른 시작을 완료하려면 먼저 Cloud 프로젝트를 설정해야 합니다.

### 1. API 사용 설정

Google API를 사용하려면 먼저 Google Cloud 프로젝트에서 사용 설정해야 합니다.

*   Google Cloud 콘솔에서 Google Generative Language API를 사용 설정합니다.  
    
    [API 사용 설정](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=ko)
    

### 2\. OAuth 동의 화면 구성

이제 프로젝트의 OAuth 동의 화면을 구성하고 자신을 테스트 사용자로 추가합니다. Cloud 프로젝트에서 이 단계를 이미 완료했으면 다음 섹션으로 건너뛰세요.

1.  Google Cloud 콘솔에서 **메뉴** > **API 및 서비스** > **OAuth 동의 화면**으로 이동합니다.
    
    [OAuth 동의 화면으로 이동](https://console.cloud.google.com/apis/credentials/consent?hl=ko)
    
2.  앱의 사용자 유형 **외부**를 선택한 다음 **만들기**를 클릭합니다.
    
3.  앱 등록 양식을 작성한 다음 (대부분의 필드는 비워 둘 수 있음) **Save and Continue**를 클릭합니다.
    
4.  지금은 범위 추가를 건너뛰고 **저장 후 계속**을 클릭해도 됩니다. 향후 Google Workspace 조직 외부에서 사용할 앱을 만들 때는 앱에 필요한 승인 범위를 추가하고 확인해야 합니다.
    
5.  테스트 사용자 추가:
    
    1.  **테스트 사용자**에서 **사용자 추가**를 클릭합니다.
    2.  이메일 주소 및 승인된 다른 테스트 사용자를 입력한 다음 **저장하고 계속하기**를 클릭합니다.
6.  앱 등록 요약을 검토합니다. 변경하려면 **수정**을 클릭합니다. 앱 등록이 확인되면 **대시보드로 돌아가기**를 클릭합니다.
    

### 3\. 데스크톱 애플리케이션에 대한 사용자 인증 정보 승인

최종 사용자로 인증하고 앱의 사용자 데이터에 액세스하려면 OAuth 2.0 클라이언트 ID를 하나 이상 만들어야 합니다. 클라이언트 ID는 Google OAuth 서버에서 단일 앱을 식별하는 데 사용됩니다. 앱이 여러 플랫폼에서 실행되는 경우 플랫폼마다 별도의 클라이언트 ID를 만들어야 합니다.

1.  Google Cloud 콘솔에서 **메뉴** > **API 및 서비스** > **사용자 인증 정보**로 이동합니다.
    
    [사용자 인증 정보로 이동](https://console.cloud.google.com/apis/credentials?hl=ko)
    
2.  **사용자 인증 정보 만들기** > **OAuth 클라이언트 ID**를 클릭합니다.
    
3.  **애플리케이션 유형** > **데스크톱 앱**을 클릭합니다.
    
4.  **이름** 입력란에 사용자 인증 정보의 이름을 입력합니다. 이 이름은 Google Cloud 콘솔에만 표시됩니다.
    
5.  **만들기**를 클릭합니다. OAuth 클라이언트 생성 완료 화면이 표시되고 새 클라이언트 ID와 클라이언트 비밀번호가 표시됩니다.
    
6.  **확인**을 클릭합니다. 새로 만든 사용자 인증 정보가 **OAuth 2.0 클라이언트 ID**에 표시됩니다.
    
7.  다운로드 버튼을 클릭하여 JSON 파일을 저장합니다. `client_secret_<identifier>.json`로 저장되고 이름을 `client_secret.json`로 바꾼 후 작업 디렉터리로 이동합니다.
    

애플리케이션 기본 사용자 인증 정보 설정
----------------------

`client_secret.json` 파일을 사용 가능한 사용자 인증 정보로 변환하려면 파일 위치에 `gcloud auth application-default login` 명령어의 `--client-id-file` 인수를 전달합니다.

    gcloud auth application-default login \    --client-id-file=client_secret.json \    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'

이 튜토리얼에서 프로젝트를 간단하게 설정하면 **'Google에서 이 앱을 확인하지 않았습니다.'**라는 대화상자가 트리거됩니다. 정상적인 현상입니다. **'계속'**을 선택하세요.

이렇게 하면 결과 토큰이 잘 알려진 위치에 저장되므로 `gcloud` 또는 클라이언트 라이브러리에서 액세스할 수 있습니다.

**참고:** Colab에서 실행하는 경우 `--no-browser`를 포함하고 출력되는 안내를 주의 깊게 따르세요. 링크를 클릭하기만 하는 것이 아닙니다. 또한 로컬 `gcloud --version`이 Colab과 일치하는 [최신](https://cloud.google.com/sdk/docs/release-notes?hl=ko) 버전인지 확인하세요.

gcloud auth application-default login 
        --no-browser
        --client-id-file=client_secret.json 
        --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'

애플리케이션 기본 사용자 인증 정보 (ACD)를 설정하면 대부분의 언어로 된 클라이언트 라이브러리가 이를 찾는 데 도움이 되지 않으며 최소한으로 필요합니다.

### Curl

작동하는지 테스트하는 가장 빠른 방법은 curl을 사용하여 REST API에 액세스하는 것입니다.

    access_token=$(gcloud auth application-default print-access-token)project_id=<MY PROJECT ID>curl -X GET https://generativelanguage.googleapis.com/v1/models \    -H 'Content-Type: application/json' \    -H "Authorization: Bearer ${access_token}" \    -H "x-goog-user-project: ${project_id}" | grep '"name"'

### Python

Python에서 클라이언트 라이브러리는 이를 자동으로 찾습니다.

    pip install google-generativeai

테스트할 최소한의 스크립트는 다음과 같습니다.

    import google.generativeai as genaiprint('Available base models:', [m.name for m in genai.list_models()])

다음 단계
-----

이 방법이 효과가 있다면 [텍스트 데이터에서 시맨틱 검색](https://ai.google.dev/docs/semantic_retriever?hl=ko)을 사용해 볼 수 있습니다.

사용자 인증 정보 직접 관리\[Python\]
-------------------------

대부분의 경우 클라이언트 ID (`client_secret.json`)에서 액세스 토큰을 만드는 데 `gcloud` 명령어를 사용할 수 없습니다. Google은 앱 내에서 해당 프로세스를 관리할 수 있도록 다양한 언어로 라이브러리를 제공합니다. 이 섹션에서는 Python에서 이 프로세스를 보여줍니다. 다른 언어의 경우 [Drive API 문서](https://developers.google.com/drive/api/quickstart/python?hl=ko)에서 이러한 종류의 절차에 상응하는 예시를 확인할 수 있습니다.

### 1\. 필요한 라이브러리 설치

Python용 Google 클라이언트 라이브러리와 Gemini 클라이언트 라이브러리를 설치합니다.

    pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlibpip install google-generativeai

### 2\. 인증 관리자 작성

승인 화면을 클릭해야 하는 횟수를 최소화하려면 작업 디렉터리에 `load_creds.py`라는 파일을 만들어 나중에 재사용할 수 있도록 `token.json` 파일을 캐시하거나 만료되면 새로고침합니다.

다음 코드부터 시작하여 `client_secret.json` 파일을 `genai.configure`와 함께 사용할 수 있는 토큰으로 변환합니다.

    import os.pathfrom google.auth.transport.requests import Requestfrom google.oauth2.credentials import Credentialsfrom google_auth_oauthlib.flow import InstalledAppFlowSCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']def load_creds():    """Converts `client_secret.json` to a credential object.    This function caches the generated tokens to minimize the use of the    consent screen.    """    creds = None    # The file token.json stores the user's access and refresh tokens, and is    # created automatically when the authorization flow completes for the first    # time.    if os.path.exists('token.json'):        creds = Credentials.from_authorized_user_file('token.json', SCOPES)    # If there are no (valid) credentials available, let the user log in.    if not creds or not creds.valid:        if creds and creds.expired and creds.refresh_token:            creds.refresh(Request())        else:            flow = InstalledAppFlow.from_client_secrets_file(                'client_secret.json', SCOPES)            creds = flow.run_local_server(port=0)        # Save the credentials for the next run        with open('token.json', 'w') as token:            token.write(creds.to_json())    return creds

### 3\. 프로그램 작성

이제 `script.py`를 만듭니다.

    import pprintimport google.generativeai as genaifrom load_creds import load_credscreds = load_creds()genai.configure(credentials=creds)print()print('Available base models:', [m.name for m in genai.list_models()])

### 4\. 프로그램 실행

작업 디렉터리에서 샘플을 실행합니다.

    python script.py

스크립트를 처음 실행하면 브라우저 창이 열리고 액세스를 승인하라는 메시지가 표시됩니다.

1.  아직 Google 계정에 로그인하지 않았다면 로그인하라는 메시지가 표시됩니다. 여러 계정에 로그인되어 있는 경우 **프로젝트를 구성할 때 '테스트 계정'으로 설정한 계정을 선택해야 합니다.**
    
    **참고:** 이 튜토리얼의 간소화된 프로젝트 설정은 **'Google에서 이 앱을 확인하지 않았습니다.'** 대화상자를 트리거합니다. 정상적인 상황이므로 **'계속'**을 선택하세요.
    
2.  승인 정보는 파일 시스템에 저장되므로 다음에 샘플 코드를 실행할 때는 승인하라는 메시지가 표시되지 않습니다.
    

인증을 설정했습니다.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-14(UTC)
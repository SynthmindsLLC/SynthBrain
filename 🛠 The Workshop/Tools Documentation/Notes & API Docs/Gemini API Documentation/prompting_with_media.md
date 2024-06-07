*   이 페이지의 내용
*   [시작하기 전에: 프로젝트 및 API 키 설정](#set-up-project-and-api-key)
    *   [Python SDK 설치 및 패키지 가져오기](#install-sdk-and-import-packages)
    *   [API 키 보호 및 구성](#secure-and-configure-key)
*   [이미지로 메시지 표시](#prompting-with-images)
    *   [이미지 파일 업로드](#upload-image-file)
    *   [이미지 파일의 메타데이터 가져오기](#get-image-file-metadata)
    *   [업로드된 이미지 파일을 사용하여 콘텐츠 생성](#generate-content-from-image)
    *   [이미지 파일 삭제](#delete-image-file)
*   [동영상으로 메시지 표시](#prompting-with-videos)
    *   [동영상 파일 업로드](#upload-video-file)
    *   [동영상 파일의 업로드 상태 확인](#verify-upload-state)
    *   [동영상 파일의 메타데이터 가져오기](#get-video-file-metadata)
    *   [업로드된 동영상 파일을 사용하여 콘텐츠 생성](#generate-content-from-video)
    *   [동영상 파일 삭제](#delete-video-file)
*   [지원되는 파일 형식](#supported_file_formats)
    *   [이미지 형식](#image_formats)
    *   [오디오 형식](#audio_formats)
    *   [동영상 형식](#video_formats)
    *   [일반 텍스트 형식](#plain_text_formats)
*   [부록: Colab에 파일 업로드하기](#uploading_files_to_colab)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

미디어 파일로 메시지 표시
==============

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [시작하기 전에: 프로젝트 및 API 키 설정](#set-up-project-and-api-key)
    *   [Python SDK 설치 및 패키지 가져오기](#install-sdk-and-import-packages)
    *   [API 키 보호 및 구성](#secure-and-configure-key)
*   [이미지로 메시지 표시](#prompting-with-images)
    *   [이미지 파일 업로드](#upload-image-file)
    *   [이미지 파일의 메타데이터 가져오기](#get-image-file-metadata)
    *   [업로드된 이미지 파일을 사용하여 콘텐츠 생성](#generate-content-from-image)
    *   [이미지 파일 삭제](#delete-image-file)
*   [동영상으로 메시지 표시](#prompting-with-videos)
    *   [동영상 파일 업로드](#upload-video-file)
    *   [동영상 파일의 업로드 상태 확인](#verify-upload-state)
    *   [동영상 파일의 메타데이터 가져오기](#get-video-file-metadata)
    *   [업로드된 동영상 파일을 사용하여 콘텐츠 생성](#generate-content-from-video)
    *   [동영상 파일 삭제](#delete-video-file)
*   [지원되는 파일 형식](#supported_file_formats)
    *   [이미지 형식](#image_formats)
    *   [오디오 형식](#audio_formats)
    *   [동영상 형식](#video_formats)
    *   [일반 텍스트 형식](#plain_text_formats)
*   [부록: Colab에 파일 업로드하기](#uploading_files_to_colab)

Python Node.js Go

  

<table align="left" class="tfo-notebook-buttons"><tbody><tr><td><a href="https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=ko" target="_blank"><img height="32" src="https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png?hl=ko" width="32">ai.google.dev에서 보기</a></td><td><a href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/prompting_with_media.ipynb?hl=ko" target="_blank"><img src="https://www.tensorflow.org/images/colab_logo_32px.png?hl=ko">Google Colab에서 실행</a></td><td><a href="https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/prompting_with_media.ipynb" target="_blank"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=ko">GitHub에서 소스 보기</a></td></tr></tbody></table>

Gemini API는 텍스트, 이미지, 오디오, 동영상 데이터(_멀티모달_ 프롬프팅이라고도 함)를 사용한 프롬프팅을 지원합니다. 즉, 이러한 유형의 미디어 파일을 프롬프트에 포함할 수 있습니다. 작은 파일의 경우 프롬프트를 제공할 때 Gemini 모델을 로컬 파일로 직접 가리킬 수 있습니다. 더 큰 파일은 프롬프트에 포함하기 전에 [File API](https://ai.google.dev/api/rest/v1beta/files?hl=ko)를 사용하여 업로드하세요.

File API를 사용하면 프로젝트당 최대 20GB의 파일을 저장할 수 있으며 각 파일의 크기는 2GB를 넘지 않습니다. 파일은 48시간 동안 저장되며 이 기간 내에 생성을 위해 API 키를 사용하여 액세스할 수 있으며 API에서 다운로드할 수 없습니다. Files API는 [Gemini API가 제공되는](https://ai.google.dev/available_regions?hl=ko) 모든 리전에서 무료로 사용할 수 있습니다.

File API는 `model.generateContent` 또는 `model.streamGenerateContent`로 콘텐츠를 생성하는 데 사용할 수 있는 입력을 처리합니다. 유효한 파일 형식 (MIME 유형)과 지원되는 모델에 대한 자세한 내용은 [지원되는 파일 형식](#supported_file_formats)을 참조하세요.

이 가이드에서는 File API를 사용하여 미디어 파일을 업로드하고 Gemini API의 `GenerateContent` 호출에 포함하는 방법을 보여줍니다. 자세한 내용은 [코드 샘플](https://github.com/google-gemini/gemini-api-cookbook/tree/main/quickstarts/file-api)을 참고하세요.

시작하기 전에: 프로젝트 및 API 키 설정
------------------------

Gemini API (또는 File API)를 호출하기 전에 프로젝트를 설정하고 API 키를 구성해야 합니다.

**펼쳐서 프로젝트 및 API 키를 설정하는 방법 보기**

### Python SDK 설치 및 패키지 가져오기

Gemini API용 Python SDK는 [`google-generativeai`](https://pypi.org/project/google-generativeai/) 패키지에 포함되어 있습니다.

1.  pip를 사용하여 종속 항목을 설치합니다.
    
        pip install -q -U google-generativeai
    
2.  필요한 패키지를 가져옵니다.
    
        import google.generativeai as genaifrom IPython.display import Markdown
    

### API 키 보호 및 구성

Gemini API 및 File API를 호출하려면 API 키가 필요합니다. 아직 키가 없으면 Google AI Studio에서 키를 만듭니다.

[API 키 가져오기](https://aistudio.google.com/app/apikey?hl=ko)

`GOOGLE_API_KEY`라는 Colab 보안 비밀에 API 키를 저장합니다. Colab 보안 비밀에 익숙하지 않은 경우 [인증 빠른 시작](https://github.com/google-gemini/gemini-api-cookbook/blob/main/quickstarts/Authentication.ipynb)을 참조하세요.

    from google.colab import userdataGOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')genai.configure(api_key=GOOGLE_API_KEY)

**중요:** File API는 인증과 액세스에 API 키를 사용합니다. 업로드된 파일은 API 키에 연결된 기본 Google Cloud 프로젝트와 연결됩니다. API 키를 사용하는 다른 Gemini API와 달리 API 키는 File API를 사용하여 업로드한 데이터에 대한 액세스 권한도 부여하므로 API 키를 안전하게 보호해야 합니다. [키를 안전하게 보호](https://ai.google.dev/gemini-api/docs/api-key?hl=ko#security)하는 방법을 자세히 알아보세요.

이미지로 메시지 표시
-----------

이 튜토리얼에서는 File API를 사용하여 샘플 이미지를 업로드한 다음 이를 사용하여 콘텐츠를 생성합니다.

### 이미지 파일 업로드

자체 파일을 업로드하는 방법은 [부록 섹션](#uploading_files_to_colab)을 참고하세요.

1.  업로드할 샘플 이미지를 준비합니다.
    
      `curl -o image.jpg https://storage.googleapis.com/generativeai-downloads/images/jetpack.jpg`
2.  다른 API 호출을 통해 액세스할 수 있도록 [`media.upload`](https://ai.google.dev/api/rest/v1beta/media/upload?hl=ko)를 사용하여 해당 파일을 업로드합니다.
    
        sample_file = genai.upload_file(path="image.jpg",                            display_name="Sample drawing")print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
    

`response`는 업로드된 이미지가 지정된 `display_name`와 함께 저장되고 Gemini API 호출에서 파일을 참조하는 `uri`가 있음을 보여줍니다. `response`를 사용하여 업로드된 파일이 URI에 매핑되는 방식을 추적합니다.

사용 사례에 따라 URI를 구조(예: `dict` 또는 데이터베이스)에 저장할 수 있습니다.

### 이미지 파일의 메타데이터 가져오기

파일을 업로드한 후 SDK를 통해 [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=ko)를 호출하여 API가 파일을 성공적으로 저장했는지 확인하고 메타데이터를 가져올 수 있습니다.

이 메서드를 사용하면 API 키에 연결된 Google Cloud 프로젝트와 연결되어 업로드된 파일의 메타데이터를 가져올 수 있습니다. `name` (및 더 나아가 `uri`)만 고유합니다. 고유성을 직접 관리하는 경우에만 `display_name`를 사용하여 파일을 식별하세요.

    file = genai.get_file(name=sample_file.name)print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")

### 업로드된 이미지 파일을 사용하여 콘텐츠 생성

이미지를 업로드한 후 파일을 업로드하거나 직접 파일의 메타데이터를 가져와서 응답에서 `uri`를 참조하는 `GenerateContent` 요청을 실행할 수 있습니다.

이 예시에서는 텍스트로 시작하고 그 뒤에 업로드된 파일의 URI 참조가 나오는 프롬프트를 만듭니다.

    # The Gemini 1.5 models are versatile and work with multimodal promptsmodel = genai.GenerativeModel(model_name="models/gemini-1.5-flash")response = model.generate_content([sample_file, "Describe the image with a creative description."])Markdown(">" + response.text)

### 이미지 파일 삭제

파일은 48시간 후 자동으로 삭제됩니다. SDK를 통해 [`files.delete`](https://ai.google.dev/api/rest/v1beta/files/delete?hl=ko)를 사용하여 수동으로 삭제할 수도 있습니다.

    genai.delete_file(sample_file.name)print(f'Deleted {sample_file.display_name}.')

동영상으로 메시지 표시
------------

이 튜토리얼에서는 File API를 사용하여 샘플 동영상을 업로드한 다음 이를 사용하여 콘텐츠를 생성합니다.

### 동영상 파일 업로드

Gemini API는 동영상 파일 형식을 직접 허용합니다. 이 예에서는 단편 영화인 'Big Buck Bunny'를 사용합니다.

> 'Big Buck Bunny'는 (c) copyright 2008, Blender Foundation / www.bigbuckbunny.org에 있으며 크리에이티브 커먼즈 저작자 표시 3.0 라이선스에 따라 사용이 허가되었습니다.

자체 파일을 업로드하는 방법은 [부록 섹션](#uploading_files_to_colab)을 참고하세요.

1.  업로드할 샘플 동영상 파일을 준비합니다.
    
        wget https://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4
    
2.  다른 API 호출을 통해 액세스할 수 있도록 [`media.upload`](https://ai.google.dev/api/rest/v1beta/media/upload?hl=ko)를 사용하여 해당 파일을 업로드합니다.
    
        video_file_name = "BigBuckBunny_320x180.mp4"print(f"Uploading file...")video_file = genai.upload_file(path=video_file_name)print(f"Completed upload: {video_file.uri}")
    

**참고:** File API는 초당 1프레임 (FPS)으로 동영상을 샘플링합니다. 이 샘플링 레이트는 최상의 추론 품질을 제공하기 위해 변경될 수 있습니다.

### 동영상 파일의 업로드 상태 확인

SDK를 통해 [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=ko) 메서드를 호출하여 API에서 동영상 파일을 성공적으로 업로드했는지 확인합니다.

동영상 파일에는 File API의 `State` 필드가 있습니다. 동영상이 업로드되면 추론 준비가 될 때까지 `PROCESSING` 상태가 됩니다. **모델 추론에는 `ACTIVE` 파일만 사용할 수 있습니다.**

    import timewhile video_file.state.name == "PROCESSING":    print('.', end='')    time.sleep(10)    video_file = genai.get_file(video_file.name)if video_file.state.name == "FAILED":  raise ValueError(video_file.state.name)

### 동영상 파일의 메타데이터 가져오기

언제든지 SDK를 통해 [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=ko) 메서드를 호출하여 업로드된 동영상 파일의 메타데이터를 가져올 수 있습니다.

이 메서드를 사용하면 API 키에 연결된 Google Cloud 프로젝트와 연결되어 업로드된 파일의 메타데이터를 가져올 수 있습니다. `name` (및 더 나아가 `uri`)만 고유합니다. 고유성을 직접 관리하는 경우에만 `display_name`를 사용하여 파일을 식별하세요.

    file = genai.get_file(name=video_file.name)print(f"Retrieved file '{file.display_name}' as: {video_file.uri}")

### 업로드된 동영상 파일을 사용하여 콘텐츠 생성

동영상을 업로드한 후에는 파일을 업로드하거나 직접 파일의 메타데이터를 가져와서 응답에서 `uri`를 참조하는 `GenerateContent` 요청을 실행할 수 있습니다.

동영상에 대한 추론을 실행하기 전에 [동영상 파일의 업로드 상태를 확인](#verify-upload-state) (위 섹션)해야 합니다.

    # Create the prompt.prompt = "Describe this video."# The Gemini 1.5 models are versatile and work with multimodal promptsmodel = genai.GenerativeModel(model_name="models/gemini-1.5-flash")# Make the LLM request.print("Making LLM inference request...")response = model.generate_content([video_file, prompt],                                  request_options={"timeout": 600})print(response.text)

### 동영상 파일 삭제

파일은 48시간 후 자동으로 삭제됩니다. SDK를 통해 [`files.delete`](https://ai.google.dev/api/rest/v1beta/files/delete?hl=ko)를 사용하여 수동으로 삭제할 수도 있습니다.

    genai.delete_file(file_response.name)print(f'Deleted file {file_response.uri}')

지원되는 파일 형식
----------

Gemini 모델은 여러 파일 형식으로 프롬프팅을 지원합니다. 이 섹션에서는 메시지 표시에 일반 미디어 형식(특히 이미지, 오디오, 동영상, 일반 텍스트 파일)을 사용할 때의 고려사항을 설명합니다. 다음 표와 같이 특정 모델 버전에서만 프롬프트를 표시하는 미디어 파일을 사용할 수 있습니다.

| **모델** | **이미지** | **오디오** | **동영상** | **일반 텍스트** |
| --- | --- | --- | --- | --- |
| Gemini 1.5 Pro (버전 008 이상) | ✔ (최대 3,600개의 이미지 파일) | ✔ | ✔ | ✔ |
| Gemini Pro Vision | ✔ (최대 이미지 파일 16개) |  |  | ✔ |

### 이미지 형식

Gemini 1.5 모델 또는 Gemini 1.0 Pro Vision 모델로 프롬프트를 표시하는 데 이미지 데이터를 사용할 수 있습니다. 프롬프트를 위해 이미지를 사용할 때 다음과 같은 제한사항 및 요구사항이 적용됩니다.

*   이미지는 다음 이미지 데이터 [MIME 유형](https://developers.google.com/drive/api/guides/ref-export-formats?hl=ko) 중 하나여야 합니다.
    *   PNG - image/png
    *   JPEG - image/jpeg
    *   WEBP - image/webp
    *   HEIC - image/heic
    *   HEIF - image/heif
*   Gemini 1.0 Pro Vision 모델의 경우 최대 16개의 개별 이미지, Gemini 1.5 모델의 경우 3,600개의 개별 이미지.
*   이미지의 픽셀 수에는 특별한 제한이 없습니다. 그러나 더 큰 이미지는 원래 가로세로 비율을 유지하면서 최대 해상도 3072x3072에 맞게 축소됩니다.

### 오디오 형식

Gemini 1.5 모델에서 프롬프트를 표시하는 데 오디오 데이터를 사용할 수 있습니다. 메시지 표시에 오디오를 사용할 경우 다음과 같은 제한사항 및 요구사항이 적용됩니다.

*   오디오 데이터는 다음과 같은 일반적인 오디오 형식 [MIME 유형](https://developers.google.com/drive/api/guides/ref-export-formats?hl=ko)에서 지원됩니다.
    *   WAV - 오디오/wav
    *   MP3 - 오디오/mp3
    *   AIFF - 오디오/aiff
    *   AAC - 오디오/aac
    *   OGG Vorbis - 오디오/ogg
    *   FLAC - 오디오/flac
*   단일 프롬프트에서 지원되는 오디오 데이터의 최대 길이는 9.5시간입니다.
*   오디오 파일은 16Kbps 데이터 해상도로 리샘플링되며 여러 오디오 채널이 단일 채널로 결합됩니다.
*   단일 프롬프트의 오디오 파일 수에는 특별한 제한이 없습니다. 그러나 단일 프롬프트에서 모든 오디오 파일을 합한 총 길이는 9.5시간을 초과할 수 없습니다.

### 동영상 형식

Gemini 1.5 모델에서 프롬프트를 표시하는 데 동영상 데이터를 사용할 수 있습니다.

*   동영상 데이터는 다음과 같은 일반적인 동영상 형식 [MIME 유형](https://developers.google.com/drive/api/guides/ref-export-formats?hl=ko)에서 지원됩니다.
    
    *   video/mp4
    *   video/mpeg
    *   동영상/mov
    *   동영상/avi
    *   video/x-flv
    *   동영상/mpg
    *   동영상/webm
    *   동영상/wmv
    *   동영상/3gpp
*   File API 서비스는 초당 1프레임 (FPS)으로 동영상을 이미지로 샘플링하며 최상의 추론 품질을 제공하기 위해 변경될 수 있습니다. 개별 이미지는 해상도 및 품질에 **관계없이** 최대 258개의 토큰을 사용합니다.
    

### 일반 텍스트 형식

File API는 다음 MIME 유형의 일반 텍스트 파일 업로드를 지원합니다.

*   text/plain
*   text/html
*   text/css
*   text/javascript
*   application/x-javascript
*   텍스트/x-typescript
*   애플리케이션/x-typescript
*   text/csv
*   텍스트/마크다운
*   텍스트/x-python
*   application/x-python-code
*   application/json
*   text/xml
*   애플리케이션/rtf
*   텍스트/rtf

MIME 유형이 목록에 없는 일반 텍스트 파일의 경우 위의 MIME 유형 중 하나를 수동으로 지정해 볼 수 있습니다.

부록: Colab에 파일 업로드하기
-------------------

이 노트북은 인터넷에서 다운로드한 파일에 File API를 사용합니다. Colab에서 이 작업을 실행하고 자체 파일을 사용하려면 먼저 Colab 인스턴스에 파일을 업로드해야 합니다.

먼저 왼쪽 사이드바에서 **파일**을 클릭한 다음 **업로드** 버튼을 클릭합니다.

![](https://ai.google.dev/tutorials/images/colab_upload.png?hl=ko)

다음으로 이 파일을 File API에 업로드합니다. 아래 코드 셀 양식에 업로드한 파일의 파일 이름을 입력하고 파일의 적절한 표시 이름을 입력한 후 셀을 실행합니다.

    my_filename = "gemini_logo.png" # @param {type:"string"}my_file_display_name = "Gemini Logo" # @param {type:"string"}my_file = genai.upload_file(path=my_filename,                            display_name=my_file_display_name)print(f"Uploaded file '{my_file.display_name}' as: {my_file.uri}")

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-29(UTC)
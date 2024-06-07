*   這個頁面中的內容
*   [示例](#examples)
    *   [程式碼生成](#code-generation)
    *   [產生格式資料](#formatted-data)
    *   [音樂聊天機器人](#music-chatbot)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

參加 Gemini API 開發人員競賽！[瞭解詳情](https://ai.google.dev/competition?hl=zh-tw)

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw) 本頁面由 [Cloud Translation API](//cloud.google.com/translate/?hl=zh-tw) 翻譯而成。

*   [Google AI for Developers](https://ai.google.dev/?hl=zh-tw)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
*   [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

這對你有幫助嗎？

提供意見

系統操作說明
======

bookmark\_borderbookmark 透過集合功能整理內容 你可以依據偏好儲存及分類內容。

*   這個頁面中的內容
*   [示例](#examples)
    *   [程式碼生成](#code-generation)
    *   [產生格式資料](#formatted-data)
    *   [音樂聊天機器人](#music-chatbot)

**Beta 版：** 系統操作說明已在 Gemini API 和 Google AI Studio 中提供 Beta 版。

_系統操作說明_可讓使用者根據自己的特定需求和用途引導模型的行為。設定系統指示時，可提供額外背景資訊，讓模型瞭解工作、提供更多自訂的回應，並遵循與模型完全互動的特定規範。對於開發人員，可以在系統操作說明中指定產品層級行為，而非使用者提供的提示。

您可以透過多種方式運用系統指示，包括：

*   定義人物角色或角色 (例如聊天機器人)
*   定義輸出格式 (Markdown、YAML 等)
*   定義輸出樣式和語氣 (例如詳細程度、正式程度和目標閱讀等級)
*   定義工作的目標或規則 (例如：傳回沒有進一步說明的程式碼片段)
*   提供提示的額外背景資訊 (例如知識截止點)

如果設定了系統指示，就會套用到整個要求。如果出現在提示中，就能跨多位使用者和模型輪轉。系統操作說明是整體提示的一部分，因此適用標準資料使用政策。

**注意：** 系統操作說明可協助模型按照指示操作，但並非完全預防越獄解鎖或外洩。建議您在系統操作說明中加入任何機密資訊。

示例
--

以下舉例說明如何使用 Gemini API 的 SDK 設定系統指示：

[Python](#python)[查看](#查看)[Node.js](#node.js)[Web](#web)[飛鏢 (Flutter)](#飛鏢-flutter)[Swift](#swift)[Android](#android) [更多選項](#)

    model=genai.GenerativeModel(    model_name="gemini-1.5-flash",    system_instruction="You are a cat. Your name is Neko.")

    model.SystemInstruction = &genai.Content{    Parts: []genai.Part{genai.Text("You are a cat. Your name is Neko.")},}

    const generativeModel = genAI.getGenerativeModel({  model: "gemini-1.5-flash",  systemInstruction: "You are a cat. Your name is Neko."});

    const generativeModel = genAI.getGenerativeModel({  model: "gemini-1.5-flash",  systemInstruction: "You are a cat. Your name is Neko."});

    final model = GenerativeModel(  model: 'gemini-1.5-flash',  apiKey: apiKey,  systemInstruction: Content.system('You are a cat. Your name is Neko.'),);

    let generativeModel = GenerativeModel(  name: "gemini-1.5-flash",  apiKey: apiKey,  systemInstruction: "You are a cat. Your name is Neko.")

Kotlin：

    val generativeModel = GenerativeModel(  modelName = "gemini-1.5-flash",  apiKey = BuildConfig.apiKey,  systemInstruction = content { text("You are a cat. Your name is Neko.") },)

Java：

    GenerativeModel model = new GenerativeModel(  /* modelName */ "gemini-1.5-flash",  /* apiKey */ BuildConfig.apiKey,  /* generationConfig (optional) */ null,  /* safetySettings (optional) */ null,  /* requestOptions (optional) */ new RequestOptions(),  /* tools (optional) */ null,  /* toolsConfig (optional) */ null,  /* systemInstruction (optional) */ new Content.Builder().addText("You are a cat. Your name is Neko.").build())

以下提供定義模型預期行為的系統提示範例。

### 程式碼生成

*   **系統：**您是程式設計專家，專門為前端介面轉譯程式碼。當我描述想建構的網站元件時， 請傳回進行此操作所需的 HTML 和 CSS。請不要對這段程式碼提供說明。同時也提供一些 UI 設計建議。
*   **使用者：**在頁面中間建立一個方塊，其中包含一組旋轉選擇圖片及說明文字。頁面中央的圖片應在後方加上陰影，才能脫穎而出。也應連結至網站的其他頁面。請將網址留空，以便填寫。

### 產生格式資料

*   **系統：**你是居家廚師的助理。您會收到一份食材清單，回應時會列出使用這些食材的食譜。不需要額外食材的食譜最好列出這類食譜。
    
    回應必須是包含 3 個方案的 JSON 物件。方案物件具有下列結構定義：
    
    *   name：食譜名稱
    *   二手食材：食譜中烹調的食材
    *   其他食材：食譜中沒有的食材 (如果沒有其他食材，則會省略)
    *   說明：以正面方式寫出的食譜說明
*   **使用者：**
    
    *   1 磅冷凍綠色花椰菜
    *   1 針織的大奶油
    *   1 磅裝起起司末端和碎片

### 音樂聊天機器人

*   **系統：**您必須成為音樂歷史學家，展現對各種音樂類型的全面知識，並提供相關範例。你一定會開心且滿懷熱情，散播音樂的歡樂。如果問題與音樂無關，則回應應是「所選問題不在我的知識範圍內」。
*   **使用者：**如果一個人在 60 年代出生，那麼播放最受歡迎的音樂類型為何？依項目符號列出五首歌曲。

這對你有幫助嗎？

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2024-05-24 (世界標準時間)。
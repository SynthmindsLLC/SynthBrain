*   這個頁面中的內容
*   [2024 年 5 月 23 日](#05-23-24)
*   [2024 年 5 月 14 日](#05-14-24)
*   [2024 年 5 月 10 日](#05-10-24)
*   [2024 年 4 月 9 日](#04-09-24)
*   [2024 年 3 月 19 日](#03-09-24)
*   [2023 年 12 月 13 日](#12-13-23)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

參加 Gemini API 開發人員競賽！[瞭解詳情](https://ai.google.dev/competition?hl=zh-tw)

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw) 本頁面由 [Cloud Translation API](//cloud.google.com/translate/?hl=zh-tw) 翻譯而成。

*   [Google AI for Developers](https://ai.google.dev/?hl=zh-tw)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
*   [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

這對你有幫助嗎？

提供意見

版本資訊
====

bookmark\_borderbookmark 透過集合功能整理內容 你可以依據偏好儲存及分類內容。

*   這個頁面中的內容
*   [2024 年 5 月 23 日](#05-23-24)
*   [2024 年 5 月 14 日](#05-14-24)
*   [2024 年 5 月 10 日](#05-10-24)
*   [2024 年 4 月 9 日](#04-09-24)
*   [2024 年 3 月 19 日](#03-09-24)
*   [2023 年 12 月 13 日](#12-13-23)

本頁面說明 Gemini API 的更新內容。

2024 年 5 月 23 日
---------------

**模型更新**

*   [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-1.5-pro) (`gemini-1.5-pro-001`) 現已正式發布 (正式發布版)。
*   [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-1.5-flash) (`gemini-1.5-flash-001`) 已正式發布 (GA)。

2024 年 5 月 14 日
---------------

**API 更新**

*   針對 Gemini 1.5 Pro 推出 200 萬個背景觀看期 (等候名單)。
*   我們推出 Gemini 1.0 Pro 的即付即用[billing](https://ai.google.dev/gemini-api/docs/billing?hl=zh-tw)功能，即將支援 Gemini 1.5 Pro 和 Gemini 1.5 Flash 的計費方式。
*   針對即將到來的 Gemini 1.5 Pro 付費方案，增加頻率限制。
*   [File API](https://ai.google.dev/api/rest/v1beta/files?hl=zh-tw) 新增內建影片支援。
*   [File API](https://ai.google.dev/api/rest/v1beta/files?hl=zh-tw) 開始支援純文字。
*   開始支援平行函式呼叫，可一次傳回多次呼叫。

2024 年 5 月 10 日
---------------

**模型更新**

*   推出預先發布版 [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-1.5-flash) (`gemini-1.5-flash-latest`)。

2024 年 4 月 9 日
--------------

**模型更新**

*   推出 [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw#gemini-1.5-pro) (`gemini-1.5-pro-latest`) 預先發布版。
*   發布新的文字嵌入模型 `text-embeddings-004`，可支援低於 768 的[彈性嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-tw#elastic-embedding)大小。

**API 更新**

*   發布 [File API](https://ai.google.dev/api/rest/v1beta/files?hl=zh-tw) 以暫時儲存媒體檔案，以便在提示中使用。
*   新增對文字、圖片和音訊資料提示的支援，也稱為「多模態」提示。詳情請參閱「[使用媒體提示](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=zh-tw)」。
*   發布 Beta 版[系統操作說明](https://ai.google.dev/gemini-api/docs/system-instructions?hl=zh-tw)。
*   新增[函式呼叫模式](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#function_calling_mode)，可定義函式呼叫的執行行為。
*   新增對 `response_mime_type` 設定選項的支援，該選項可讓您要求 [JSON 格式](https://ai.google.dev/gemini-api/docs/api-overview?hl=zh-tw#json)的回應。

2024 年 3 月 19 日
---------------

*   新增在 Google AI Studio 或 Gemini API 中[調整 Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) 的支援功能。

2023 年 12 月 13 日
----------------

**4 種新模式：**

*   gemini-pro：新文字模型可處理各種工作在功能和效率之間取得平衡
*   gemini-pro-vision：最新多模態模型可處理多種工作。在功能和效率之間取得平衡。
*   嵌入功能 001：新的嵌入模型
*   aqa：經過特別調整的全新模型，經過訓練，可透過文字段落建立依據產生的答案來回答問題。

詳情請參閱 [Gemini 模型](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw)。

**API 版本更新：**

*   v1：穩定版 API。
*   v1beta：Beta 版。這個頻道的功能可能還在開發中。

詳情請參閱 [API 版本主題](https://ai.google.dev/gemini-api/docs/api-versions?hl=zh-tw)。

**API 更新**

*   `GenerateContent` 是即時通訊和文字的單一統一端點。
*   可透過 `StreamGenerateContent` 方法串流播放。
*   多模態功能：圖片是新支援的模型
*   全新 Beta 版功能：
    *   [函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)
    *   [語意擷取工具](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=zh-tw)
    *   歸因問題回答 (AQA)
*   更新後的候選數量：Gemini 模型只會傳回 1 個候選項目。
*   不同的安全設定和 SafetyRating 類別。詳情請參閱[安全性設定](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-tw)。
*   Gemini 模型尚未支援調整模型 (處理中)。

這對你有幫助嗎？

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2024-05-25 (世界標準時間)。
*   這個頁面中的內容
*   [使用 Gemini API 建構聊天機器人](#chatbot)
*   [使用 Gemini API 的多模態工作](#multimodal)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

參加 Gemini API 開發人員競賽！[瞭解詳情](https://ai.google.dev/competition?hl=zh-tw)

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw) 本頁面由 [Cloud Translation API](//cloud.google.com/translate/?hl=zh-tw) 翻譯而成。

*   [Google AI for Developers](https://ai.google.dev/?hl=zh-tw)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
*   [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

這對你有幫助嗎？

提供意見

Gemini API Firebase 擴充功能
========================

bookmark\_borderbookmark 透過集合功能整理內容 你可以依據偏好儲存及分類內容。

*   這個頁面中的內容
*   [使用 Gemini API 建構聊天機器人](#chatbot)
*   [使用 Gemini API 的多模態工作](#multimodal)

[Firebase](https://firebase.google.com/?hl=zh-tw) 是 Google 支援的應用程式開發平台，受到全球數百萬開發人員的信賴。如果您是 Firebase 開發人員，想使用 Gemini API 將應用程式新增至應用程式，我們有幾個 [Firebase 擴充功能](https://extensions.dev/extensions)可協助您完成此操作。這些預先封裝的解決方案可協助您快速將新功能部署至應用程式。

使用 Gemini API 建構聊天機器人
---------------------

[使用 Gemini API 建構聊天機器人](https://extensions.dev/extensions/googlecloud/firestore-genai-chatbot)擴充功能可讓您透過 Gemini API 使用 [Cloud Firestore](https://firebase.google.com/docs/firestore?hl=zh-tw) 做為資料庫，建立及管理使用者與大型語言模型之間的互動式對話。Cloud Firestore 中的集合代表每個即時通訊，擴充功能會監控新訊息的集合，然後查詢 Gemini API 以取得適當的回應，將即時通訊先前的訊息視為背景資訊。

整合 **Build Chatbot 與 Gemini API** 擴充功能後，您就能有效率地建立聊天機器人應用程式、提升使用者體驗和互動，同時省下自訂程式碼的開發時間和精力。

使用 Gemini API 的多模態工作
--------------------

[具備 Gemini API 的多模態工作](https://extensions.dev/extensions/googlecloud/firestore-multimodal-genai)擴充功能可讓您利用文字提示和 (選用) 圖片，在 Firestore 中的資料執行語言工作。

您可以設定每個擴充功能執行個體來執行單一特定工作。如果您有多項工作，可以安裝多個執行個體。

舉例來說，這個擴充功能可用來：

*   預測一組產品評論的星級評等。
*   將客戶意見回饋歸類為正面、負面或中立。
*   摘述長篇文章。
*   從文字中擷取已命名實體。
*   產生廣告素材文字，例如詩詞或程式碼。

這對你有幫助嗎？

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2024-04-18 (世界標準時間)。
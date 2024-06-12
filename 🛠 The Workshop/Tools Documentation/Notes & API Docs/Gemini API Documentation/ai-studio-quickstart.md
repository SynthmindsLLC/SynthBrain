---
Please provide me with the rest of the mission statement! I need more context to help you complete it. 

For example, tell me: "* **What is the mission for?**  Is it for a company, a project, a personal goal, a non-profit organization?"
* **What are the main goals or values?**  What does this mission aim to achieve? 
* **What is the target audience?** Who is this mission intended to benefit?

Once you provide me with more information, I can help you craft a compelling and effective mission statement.
---

*   這個頁面中的內容
*   [提示與模型調整](#prompts-and)
*   [聊天提示範例：建構自訂即時通訊應用程式](#chat_example)
    *   [步驟 1：建立聊天提示](#step-1-chat)
    *   [步驟 2 - 訓練機器人以提升即時通訊品質](#step-2-chat)
    *   [步驟 3：後續步驟](#step-3-chat)
*   [結構化提示範例：建立產品文案產生器](#structured_example)
    *   [步驟 1 - 建立結構化提示](#step_1_sp)
    *   [步驟 2 - 新增範例](#step-2-structured)
    *   [步驟 3：測試提示](#step-3-structured)
    *   [步驟 4 - 後續步驟](#step-4-structured)
*   [其他資訊](#further-reading)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

參加 Gemini API 開發人員競賽！[瞭解詳情](https://ai.google.dev/competition?hl=zh-tw)

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw) 本頁面由 [Cloud Translation API](//cloud.google.com/translate/?hl=zh-tw) 翻譯而成。

*   [Google AI for Developers](https://ai.google.dev/?hl=zh-tw)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
*   [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

這對你有幫助嗎？

提供意見

Google AI Studio 快速入門導覽課程
=========================

bookmark\_borderbookmark 透過集合功能整理內容 你可以依據偏好儲存及分類內容。

*   這個頁面中的內容
*   [提示與模型調整](#prompts-and)
*   [聊天提示範例：建構自訂即時通訊應用程式](#chat_example)
    *   [步驟 1：建立聊天提示](#step-1-chat)
    *   [步驟 2 - 訓練機器人以提升即時通訊品質](#step-2-chat)
    *   [步驟 3：後續步驟](#step-3-chat)
*   [結構化提示範例：建立產品文案產生器](#structured_example)
    *   [步驟 1 - 建立結構化提示](#step_1_sp)
    *   [步驟 2 - 新增範例](#step-2-structured)
    *   [步驟 3：測試提示](#step-3-structured)
    *   [步驟 4 - 後續步驟](#step-4-structured)
*   [其他資訊](#further-reading)

[Google AI Studio](https://aistudio.google.com/?hl=zh-tw) 是瀏覽器型 IDE，可用來使用生成式模型進行原型設計。您可以透過 Google AI Studio 快速試用模型 並嘗試不同的提示當您建構喜歡的內容時，可以將其匯出至偏好的程式設計語言，並搭配 [Gemini API](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-tw)。

提示與模型調整
-------

Google AI Studio 提供多個提示介面，專為不同用途而設計：

*   **即時通訊提示：**你可以使用聊天提示打造對話體驗。這項提示技術可讓多個輸入和回應輪流產生輸出內容。詳情請參閱下方的[即時通訊提示範例](#chat_example)。
*   **結構化提示：**這項提示技巧可讓您提供一組範例要求和回覆，引導模型輸出內容。當您需要進一步控管模型輸出的結構時，請使用這個方法。詳情請參閱下方的[結構化提示範例](#structured_example)。

Google AI Studio 還可讓您使用「調整」技巧來變更模型的行為：

*   **微調模型：**只要使用這項進階技巧，就能提供更多範例，改善模型針對特定工作提供的回應。[瞭解詳情](https://ai.google.dev/gemini-api/docs/model-tuning?hl=zh-tw)

聊天提示範例：建構自訂即時通訊應用程式
-------------------

如果您已使用 [Gemini](https://gemini.google.com/?hl=zh-tw) 等一般用途的聊天機器人，就已親身體驗生成式 AI 模型在開放式對話上有多大的強大之處。雖然這些一般用途的聊天機器人雖然很實用，但通常還是需要針對特定用途量身打造。舉例來說，假設您想要建構客戶服務聊天機器人，專門支援談論公司產品的對話。您可能會想建構具有特定語氣或風格的聊天機器人：能夠破解許多笑話的機器人、像詩般的韻律，或是在答案中使用大量表情符號。

本範例說明如何使用 Google AI Studio 建構友善的聊天機器人，以如同木星的其中一種衛星歐洲的外星人溝通。

### 步驟 1：建立聊天提示

如要建構聊天機器人，您需要提供使用者和聊天機器人之間的互動範例，引導模型依據您的需求提供回應。

如何建立聊天提示：

1.  開啟 [Google AI Studio](https://aistudio.google.com/?hl=zh-tw)。
    
2.  在「建立新提示」選單中，按一下「即時通訊提示」。
    
3.  按一下 expand\_more 展開箭頭，展開「System 表示」部分。將下列內容貼到文字輸入欄位中：
    
    You are an alien that lives on Europa, one of Jupiter's moons.
    

新增系統操作說明後，請與模型聊天，開始測試應用程式。

如何測試聊天機器人行為：

1.  在標示為「Type what」的文字輸入方塊中，輸入使用者可能會遇到的問題或觀察項目。例如：
    
    _使用者_：
    
    What's the weather like?
    
2.  按一下 spark「Run」按鈕，或按下 Enter 鍵，取得聊天機器人的回應。這則回應可能會像這樣：
    
    _模型_：
    
    As always, it is a frigid day on Europa. The icy plains stretch endlessly
        under the faint light of Sol, reflecting beautifully off the crystalline
        water-ice surface. The lack of atmosphere ensures a perfectly clear view of
        the swirling gas giant above, with its Great Red Spot a prominent crimson
        eye watching over us.
    

### 步驟 2 - 訓練機器人以提升即時通訊品質

藉由提供單一指令，您就可以建構基本的歐式外星聊天機器人。不過，單一指示通常不足以確保模型回應中的一致性和品質。在沒有更具體的指令的情況下，模型對天氣問題的回應往往相當長，且似乎出自教科書，而不是來自友善外的外星人。

如要自訂聊天機器人的語氣，請在系統操作說明中加入：

1.  發起新的聊天提示。即時通訊工作階段開始後，即無法修改系統操作說明。
    
2.  在「系統說明」部分中，變更您已按照下列指示進行的操作：
    
    You are Tim, an alien that lives on Europa, one of Jupiter's moons.
        
        Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
        in your answers.
    
3.  重新輸入問題 (`What's the weather like?`)，然後按一下 spark「Run」按鈕或按下 Enter 鍵。現在，回應應如下所示：
    
    _型號：_
    
    Well, it's a bit nippy today! It's -170 degrees Celsius, but that's pretty
        average for Europa. We get a lot of snow, but it's not like the fluffy stuff
        you have. It's more like tiny ice pebbles.
        
        If you ever come visit, make sure you pack a warm jacket!
    

只要再新增一些指令，即可大幅改變聊天機器人的語氣。一般來說，當您為聊天機器人提供具體且定義的指示時，就能提高回應品質。

您可以運用這個方法為聊天機器人增添深度。提出更多問題、編輯答案，並改善聊天機器人的品質。繼續新增或修改操作說明，並測試它們如何改變聊天機器人行為。

**注意：** 提示中會納入模型和使用者之間的每則訊息，因此只要開啟對話，對話提示就能持續增加。最後，您可能會達到模型的權杖上限 (模型可接受的文字長度上限)。

### 步驟 3：後續步驟

與其他提示類型類似，當您完成提示原型設計後，便可使用「Get code」(取得程式碼) 按鈕開始編寫程式碼，或儲存提示供日後編輯及與他人分享。

結構化提示範例：建立產品文案產生器
-----------------

Google AI Studio 中的結構化提示可協助您結合操作說明與範例，讓模型顯示您想要的輸出類型，而不只是說出該怎麼做。如果您想讓模型維持一致的輸出格式 (即結構化 JSON)，或是難以以特定樣式描述模型。這種提示稱為[「少量樣本提示」](https://ai.google.dev/gemini-api/docs/models/generative-models?hl=zh-tw#prompt-types)便相當實用。本節將說明如何在 Google AI Studio 中建立結構化提示

**注意：** 您可以直接在 Google AI Studio 中開啟[範例圖片庫](https://ai.google.dev/examples?keywords=prompt&hl=zh-tw)中的類似範例。

### 步驟 1 - 建立結構化提示

在這個範例中，您會建立結構化提示，用來產生產品廣告文案。首先，您必須建立兩個資料欄來定義提示的結構：**Product** 輸入資料欄和 **Product copy** 輸出資料欄。

如何建立結構化提示：

1.  開啟 [Google AI Studio](https://aistudio.google.com/?hl=zh-tw)。
    
2.  在「建立新的提示」選單中，按一下「結構化提示」。
    
3.  在標示「可選用的語氣和樣式操作說明」的文字輸入方塊中，貼上以下內容：
    
    You are a product marketer targeting a Gen Z audience. Create exciting and
        fresh advertising copy for products and their simple description. Keep copy
        under a few sentences long.
    
4.  將預設的「Input」標題文字 (`input:`) 替換成 `Product:`。
    
5.  將預設的「Output」標題文字 (`output:`) 替換成 `Product copy:`。
    

**提示：** 在資料欄名稱結尾加上冒號，可讓模型更輕鬆地剖析結構。

### 步驟 2 - 新增範例

資料欄命名完畢後，現在請提供幾個範例資料列。這些資料列應包含輸入範例 (本例的產品名稱) 和輸出範例 (相對應的產品說明)。只要提供幾個範例產品說明，就能引導模型在產生自己的輸出內容時，複製類似的樣式。您可以手動輸入範例，也可以使用匯入資料選單從檔案匯入。

如何手動輸入範例：

1.  在上方範例資料表中，選取「Product:」標題下方的欄位，然後輸入產品說明。
    
2.  選取「Product copy:」標題下方的欄位，然後輸入這項產品的行銷文案。
    

以下是這個提示的輸入和輸出值範例：

| 產品： | 產品文案： |
| --- | --- |
| 復古球鞋 | 讓我們一起接場吧！有了 |
| 超柔軟連帽上衣 | 迎接全新的男女通用連帽衫，同時保持舒適與時尚！這款連帽衫採用 100% 純棉製成，既柔軟又舒適，整天佩戴也很舒適。即使在最寒冷的日子中，只要運用半刷而來的溫度就能保暖。 |

(選用) 如要從檔案匯入範例：

1.  在範例表格的右上角，依序點選「動作」>「匯入範例」。
    
2.  在對話方塊中，選取 Google 雲端硬碟中的 CSV 或 Google 試算表檔案，或是上傳電腦中的檔案。
    
3.  在匯入範例對話方塊中，選擇要匯入及排除的資料欄。對話方塊也可讓您指定要將哪些資料欄匯入結構化提示中的哪個資料表欄。
    

### 步驟 3：測試提示

取得顯示所需模型的範例後，請在底部的「Test yourPrompt」表格中輸入新輸入內容來測試提示。

舉例來說，您可以在輸入欄中輸入 `Vintage baseball cap` 之類的內容，按一下 spark「Run」按鈕或按下 Enter 鍵，然後查看模型的輸出。

#### 查看將範例傳送至模型的方式

基本上，Google AI Studio 會結合操作說明與您提供的範例，建立提示。新增更多範例時，系統會將這些樣本新增至傳送至模型的文字。視範例時間長度而定，您可能會開始達到模型的權杖上限。所有生成式 AI 模型都有符記限制，也就是可接受做為輸入內容的文字長度上限。

### 步驟 4 - 後續步驟

如果對提示感到滿意，請按一下「Save」按鈕，將專案儲存至 Google 雲端硬碟，或按一下「Get code」(取得程式碼) 按鈕，將專案匯出至程式碼。

您也可以將個別少量樣本匯出為 CSV 檔案或 Google 試算表。按一下「動作」選單中的「匯出範例」即可匯出範例。

其他資訊
----

*   如果您準備好開始進行程式碼，請參閱 [API 快速入門導覽課程](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-tw)。
*   如要瞭解如何編寫更符合需求的提示，請參閱「[提示設計指南](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=zh-tw)」。

這對你有幫助嗎？

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2024-05-14 (世界標準時間)。
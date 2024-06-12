---
Please provide me with the rest of the mission statement! I need more context to understand what your mission is about. 

For example, tell me: "* **What organization or project is this mission for?** "
* **What are the core values or goals of this organization/project?** 
* **What is the overall purpose or ambition of this mission?**

Once you give me more information, I can help you craft a compelling and impactful mission statement.
---

*   這個頁面中的內容
*   [錯誤代碼](#error-codes)
*   [查看 API 呼叫中的模型參數錯誤](#check-api)
*   [檢查您使用的模型是否正確](#check-if)
*   [安全性問題](#safety-issues)
*   [改善模型輸出內容](#improve-model)
*   [瞭解權杖限制](#understand-token)
*   [已知問題](#known-issues)
*   [回報錯誤](#file-bug)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

參加 Gemini API 開發人員競賽！[瞭解詳情](https://ai.google.dev/competition?hl=zh-tw)

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw) 本頁面由 [Cloud Translation API](//cloud.google.com/translate/?hl=zh-tw) 翻譯而成。

*   [Google AI for Developers](https://ai.google.dev/?hl=zh-tw)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
*   [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

這對你有幫助嗎？

提供意見

疑難排解指南
======

bookmark\_borderbookmark 透過集合功能整理內容 你可以依據偏好儲存及分類內容。

*   這個頁面中的內容
*   [錯誤代碼](#error-codes)
*   [查看 API 呼叫中的模型參數錯誤](#check-api)
*   [檢查您使用的模型是否正確](#check-if)
*   [安全性問題](#safety-issues)
*   [改善模型輸出內容](#improve-model)
*   [瞭解權杖限制](#understand-token)
*   [已知問題](#known-issues)
*   [回報錯誤](#file-bug)

本指南可協助您診斷及解決呼叫 Gemini API 時發生的常見問題。如果您遇到 API 金鑰問題，請務必根據 [API 金鑰設定指南](https://ai.google.dev/tutorials/setup?hl=zh-tw)，正確設定 API 金鑰。

錯誤代碼
----

下表列出您可能會遇到的常見錯誤代碼，以及這些代碼的原因與疑難排解步驟：

<table><tbody><tr><td><strong>HTTP 程式碼</strong></td><td><strong>狀態</strong></td><td><strong>說明</strong></td><td><strong>解決方案</strong></td></tr><tr><td>400</td><td>INVALID_ARGUMENT</td><td>要求主體格式錯誤。</td><td>如要瞭解要求格式、範例和支援的版本，請參閱 <a href="https://ai.google.dev/api?hl=zh-tw">API 參考資料</a>。如果使用包含舊版端點的新版 API 功能，可能會導致錯誤。</td></tr><tr><td>403</td><td>PERMISSION_DENIED</td><td>您的 API 金鑰沒有必要權限。</td><td>請確認 API 金鑰已設定完成，且有權存取。</td></tr><tr><td>404</td><td>NOT_FOUND</td><td>找不到要求的資源。</td><td>檢查<a href="https://ai.google.dev/docs/troubleshooting?hl=zh-tw#check-api">要求中的所有參數是否皆有效</a>適用於您的 API 版本。</td></tr><tr><td>429</td><td>RESOURCE_EXHAUSTED</td><td>您已超過頻率限制，</td><td>確認您符合模型的<a href="https://ai.google.dev/models/gemini?hl=zh-tw#model-variations">頻率限制</a>。如有需要，請<a href="https://ai.google.dev/docs/increase_quota?hl=zh-tw">要求提高配額</a>。</td></tr><tr><td>500</td><td>INTERNAL</td><td>Google 端發生未預期的錯誤，</td><td>請稍後再重試要求。如果重試後問題仍未解決，請使用 Google AI Studio 中的「提供意見」<b></b>按鈕來回報問題。</td></tr><tr><td>503</td><td>UNAVAILABLE</td><td>服務可能會暫時超載或停止運作。</td><td>請稍後再重試要求。如果重試後問題仍未解決，請使用 Google AI Studio 中的「提供意見」<b></b>按鈕來回報問題。</td></tr></tbody></table>

查看 API 呼叫中的模型參數錯誤
-----------------

請確認您的模型參數位於下列值內：

<table><tbody><tr><td><strong>模型參數</strong></td><td><strong>值 (範圍)</strong></td></tr><tr><td>候選數量</td><td>1 至 8 (整數)</td></tr><tr><td>溫度</td><td>0.0-1.0</td></tr><tr><td>輸出內容符記數量上限</td><td>請使用 <code dir="ltr" translate="no">get_<wbr>model</code> (<a href="https://ai.google.dev/api/python/google/generativeai/get_model?hl=zh-tw">Python</a>) 決定所用模型的權杖數量上限。</td></tr><tr><td>TopP</td><td>0.0-1.0</td></tr></tbody></table>

除了檢查參數值之外，請確認您使用的 [API 版本](https://ai.google.dev/gemini-api/docs/api-versions?hl=zh-tw)正確無誤 (例如`/v1` 或 `/v1beta`) 和支援所需功能的模型。舉例來說，如果功能仍為 Beta 版，則只能在 `/v1beta` API 版本中使用。

檢查您使用的模型是否正確
------------

確認您使用的是支援的模型。使用 `list_models` ([Python](https://ai.google.dev/api/python/google/generativeai/list_models?hl=zh-tw)) 即可取得可以使用的所有模型。

安全性問題
-----

如果您看到提示因 API 呼叫中的安全設定而遭到封鎖，請根據您在 API 呼叫中設定的篩選條件查看提示。

如果您看到 `BlockedReason.OTHER`，表示查詢或回應可能違反[服務條款](https://ai.google.dev/terms?hl=zh-tw)或不受支援。

改善模型輸出內容
--------

如要提高模型輸出內容的品質，請編寫更多結構化提示。[提示設計簡介](https://ai.google.dev/docs/prompt_best_practices?hl=zh-tw)頁面會介紹一些基本概念、策略和最佳做法，協助您快速上手。

如果您有數百個良好的輸入/輸出組合範例，也可以考慮[調整模型](https://ai.google.dev/docs/model_tuning_guidance?hl=zh-tw)。

瞭解權杖限制
------

使用 `ModelService` API 取得模型的[其他中繼資料](https://ai.google.dev/models/gemini?hl=zh-tw#model-metadata)，包括輸入和輸出權杖限制。

如要取得提示使用的權杖，請使用 [`countMessageTokens`](https://ai.google.dev/api/rest/v1beta/models/countMessageTokens?hl=zh-tw) 處理聊天模型，並將 [`countTextTokens`](https://ai.google.dev/api/rest/v1beta/models/countTextTokens?hl=zh-tw) 用於文字模型。

已知問題
----

*   Google AI Studio 行動裝置支援：雖然您可以在行動裝置上開啟網站，但網站並未針對小螢幕進行最佳化調整。
*   API 只支援英文。以不同語言提交提示可能會導致意外回應，甚至遭到封鎖。如需更新內容，請參閱[支援的語言](https://ai.google.dev/models/gemini?hl=zh-tw#available-languages)。

回報錯誤
----

在 GitHub 中提出問題或提交功能要求或錯誤。

*   [一般 API 使用情況問題](https://github.com/google/generative-ai-docs)
*   [Python 用戶端程式庫問題](https://github.com/google/generative-ai-python)
*   [Swift 用戶端程式庫問題](https://github.com/google/generative-ai-swift)

這對你有幫助嗎？

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2024-05-21 (世界標準時間)。
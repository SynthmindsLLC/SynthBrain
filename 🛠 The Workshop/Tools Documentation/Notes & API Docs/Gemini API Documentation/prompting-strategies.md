*   這個頁面中的內容
*   [提供清楚明確的指示](#give-clear-and-specific-instructions)
    *   [定義要執行的工作](#define-the-task-to-perform)
    *   [指定任何限制](#specify-any-constraints)
    *   [定義回應格式](#define-the-format-of-the-response)
*   [加入少量樣本](#include-few-shot-examples)
    *   [零樣本與少量樣本提示](#zero-shot-vs-few-shot-prompts)
    *   [找出最理想的樣本數量](#find-the-optimal-number-of-examples)
    *   [使用範例來呈現模式而非反模式](#use-examples-to-show-patterns-instead-of-antipatterns)
    *   [所有範例使用一致的格式](#use-consistent-formatting-across-examples)
*   [新增情境資訊](#add-contextual-information)
*   [新增前置字串](#add-prefixes)
*   [讓模型完成部分輸入內容](#let-the-model-complete-partial-input)
*   [將提示拆分為簡易元件](#break-down-prompts-into-simple-components)
    *   [詳細操作說明](#break-down-instructions)
    *   [鏈結提示](#chain-prompts)
    *   [匯總回應](#aggregate-responses)
*   [測試不同參數值](#experiment-with-different-parameter-values)
    *   [輸出內容符記數量上限](#max-output-tokens)
    *   [隨機性參數](#temperature)
    *   [Top-K](#top-k)
    *   [Top-P](#top-p)
*   [提示疊代策略](#prompt-iteration-strategies)
    *   [使用不同措辭](#use-different-phrasing)
    *   [切換到類似的工作](#switch-to-an-analogous-task)
    *   [變更提示內容的順序](#change-the-order-of-prompt-content)
*   [備用回應](#fallback-responses)
*   [應避免的事項](#things-to-avoid)
*   [後續步驟](#next-steps)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

參加 Gemini API 開發人員競賽！[瞭解詳情](https://ai.google.dev/competition?hl=zh-tw)

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw) 本頁面由 [Cloud Translation API](//cloud.google.com/translate/?hl=zh-tw) 翻譯而成。

*   [Google AI for Developers](https://ai.google.dev/?hl=zh-tw)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
*   [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

這對你有幫助嗎？

提供意見

提示設計策略
======

bookmark\_borderbookmark 透過集合功能整理內容 你可以依據偏好儲存及分類內容。

*   這個頁面中的內容
*   [提供清楚明確的指示](#give-clear-and-specific-instructions)
    *   [定義要執行的工作](#define-the-task-to-perform)
    *   [指定任何限制](#specify-any-constraints)
    *   [定義回應格式](#define-the-format-of-the-response)
*   [加入少量樣本](#include-few-shot-examples)
    *   [零樣本與少量樣本提示](#zero-shot-vs-few-shot-prompts)
    *   [找出最理想的樣本數量](#find-the-optimal-number-of-examples)
    *   [使用範例來呈現模式而非反模式](#use-examples-to-show-patterns-instead-of-antipatterns)
    *   [所有範例使用一致的格式](#use-consistent-formatting-across-examples)
*   [新增情境資訊](#add-contextual-information)
*   [新增前置字串](#add-prefixes)
*   [讓模型完成部分輸入內容](#let-the-model-complete-partial-input)
*   [將提示拆分為簡易元件](#break-down-prompts-into-simple-components)
    *   [詳細操作說明](#break-down-instructions)
    *   [鏈結提示](#chain-prompts)
    *   [匯總回應](#aggregate-responses)
*   [測試不同參數值](#experiment-with-different-parameter-values)
    *   [輸出內容符記數量上限](#max-output-tokens)
    *   [隨機性參數](#temperature)
    *   [Top-K](#top-k)
    *   [Top-P](#top-p)
*   [提示疊代策略](#prompt-iteration-strategies)
    *   [使用不同措辭](#use-different-phrasing)
    *   [切換到類似的工作](#switch-to-an-analogous-task)
    *   [變更提示內容的順序](#change-the-order-of-prompt-content)
*   [備用回應](#fallback-responses)
*   [應避免的事項](#things-to-avoid)
*   [後續步驟](#next-steps)

本頁將介紹一些一般提示設計策略，您可以在設計提示時運用這些策略。雖然設計提示的方法沒有正確或錯誤，但您可以使用一些常見策略來影響模型的回應。為最佳化模型效能，嚴謹的測試和評估仍相當重要。

大型語言模型 (LLM) 是以大量文字資料訓練而成，用於學習語言單位之間的模式和關係。提供某些文字 (提示) 時，語言模型可預測接下來可能出現的內容，例如精密的自動完成工具。因此，在設計提示時，請考慮會影響模型預測結果的不同因素。

提供清楚明確的指示
---------

向模型提供操作說明，是自訂模型行為的有效方法。請確認您提供的指示清楚明確。指示可以簡單當做逐步指示清單，也可以非常複雜，可對應至使用者的使用體驗和心態。

### 定義要執行的工作

請詳細說明您希望模型執行的工作。工作可以很簡單，像是提供逐步說明清單，或是複雜的對應使用者體驗和心態。以下提示會指示模型總結一段文字：

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded=""><strong>Summarize this text.</strong>
Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially
faster than any modern traditional computer. At very tiny scales, physical matter acts as both
particles and as waves, and quantum computing uses specialized hardware to leverage this behavior.
The operating principles of quantum devices is beyond the scope of classical physics. When deployed
at scale, quantum computers could be used in a wide variety of applications such as: in
cybersecurity to break existing encryption methods while helping researchers create new ones, in
meteorology to develop better weather forecasting etc. However, the current state of the art quantum
computers are still largely experimental and impractical.
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Quantum computers utilize quantum mechanical phenomena to perform computations significantly faster
than traditional computers. By exploiting the particle-wave duality of matter at tiny scales,
quantum computers leverage specialized hardware to solve problems beyond classical physics.
Potential applications include breaking encryption, developing better weather forecasting, and more.
However, current quantum computers are still largely experimental and impractical.
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

### 指定任何限制

指定讀取提示或產生回應的任何限制。您可以指示模型要執行的動作以及應執行的動作。以上一個例子來說，摘要的長度比原始文字短，但可能還希望摘要更短。在此情況下，您可以在提示中指定摘要的持續時間：

<table class="" style="background-color: gray"><tbody><tr><td><p><label><strong>提示：</strong></label></p><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded=""><strong>Summarize this text in two sentences.</strong>
Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially
faster than any modern traditional computer. At very tiny scales, physical matter acts as both
particles and as waves, and quantum computing uses specialized hardware to leverage this behavior.
The operating principles of quantum devices is beyond the scope of classical physics. When deployed
at scale, quantum computers could be used in a wide variety of applications such as: in
cybersecurity to break existing encryption methods while helping researchers create new ones, in
meteorology to develop better weather forecasting etc. However, the current state of the art quantum
computers are still largely experimental and impractical.
    </pre></devsite-code><p></p><p><label><strong>回應：</strong></label></p><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Quantum computers use quantum mechanical phenomena to perform calculations much faster than
traditional computers. They have the potential to revolutionize various fields, but current quantum
computers are still experimental and impractical.
    </pre></devsite-code><label style="text-align:right">(gemini-pro)</label><p></p></td></tr></tbody></table>

### 定義回應格式

您也可以提供指示，說明回應的格式。舉例來說，您可以要求回應採用表格、項目符號清單、電梯簡報、關鍵字、句子或段落格式。以下提示會指示模型在文字中列出重要資訊條目：

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded=""><strong>Summarize this text as bullets points of key information.</strong>
Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially
faster than any modern traditional computer. At very tiny scales, physical matter acts as both
particles and as waves, and quantum computing uses specialized hardware to leverage this behavior.
The operating principles of quantum devices is beyond the scope of classical physics. When deployed
at scale, quantum computers could be used in a wide variety of applications such as: in
cybersecurity to break existing encryption methods while helping researchers create new ones, in
meteorology to develop better weather forecasting etc. However, the current state of the art quantum
computers are still largely experimental and impractical.
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">- Quantum computers leverage quantum mechanical phenomena for exponentially faster calculations than
  traditional computers.
- Quantum devices utilize specialized hardware to exploit tiny-scale matter behavior as both
  particles and waves.
- Their operating principles transcend classical physics.
- Potential applications include cybersecurity, weather forecasting, and more.
- Current quantum computers are largely experimental and impractical.
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

### 摘要

*   向模型提供操作說明，指出該怎麼做。
*   提供清楚明確的操作說明。
*   指定輸出的任何限制條件或格式要求。

加入少量樣本
------

您可以在提示中加入範例，讓模型瞭解模型的預期結果。模型會嘗試從範例中找出模式和關係，並在產生回應時套用這些模式。包含幾個範例的提示稱為「少量樣本」提示，不提供範例的提示則稱為「零樣本提示」。少量提示通常用於調節模型回應的格式、構思、範圍或一般模式。使用具體且不同的範例，協助模型縮小聚焦範圍，產生更準確的結果。

建議你一律在提示中提供少量樣本。不含樣本範例的提示會說明如何套用操作說明，因此效果可能較差。事實上，如果範例夠清楚，可以顯示手邊的工作，就可以從提示中移除指示。

### 零樣本與少量樣本提示

下列零樣本提示要求模型選擇最佳說明。

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Please choose the best explanation to the question:

Question: How is snow formed?
Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the
atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and
accumulate on the ground.
Explanation2: Water vapor freezes into ice crystals forming snow.
Answer:
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Explanation1
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

如果您的用途需要模型產生精簡回應，您可以在提示中加入範例，讓回應內容優先於精簡。

下列提示提供兩個範例，說明較簡短的說明。在回應中，您可以看到範例引導模型選擇較短的解釋 (Explanation2)，而不是像之前說的冗長說明 (Explanation1)。

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Please choose the best explanation to the question:

<strong>Question: Why is sky blue?
Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue
wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look
blue.
Explanation2: Due to Rayleigh scattering effect.
Answer: Explanation2

Question: What is the cause of earthquakes?
Explanation1: Sudden release of energy in the Earth's crust.
Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a
release of energy that creates seismic waves that can shake the ground and cause damage.
Answer: Explanation1</strong>

Question: How is snow formed?
Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the
atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and
accumulate on the ground.
Explanation2: Water vapor freezes into ice crystals forming snow.
Answer:
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Explanation2
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

### 找出最理想的樣本數量

建議您嘗試在提示中提供要呈現最理想結果的範例數量。PaLM 和 Gemini 等模型通常可以運用幾個範例找出模式，不過您可能需要多測試幾個範例，才能達到想要的結果。如果是 BERT 等較簡單的模型，則可能需要更多範例。同時，如果您加入的樣本過多，模型可能會開始對範例[過度配適](https://developers.google.com/machine-learning/glossary?hl=zh-tw#overfitting)回應。

### 使用範例來呈現模式而非反模式

相較於使用範例來向模型展示應避免的反模式，使用範例來展示模型的做法比使用範例更好。

⛔ **負模式**：

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>範例</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Don't end haikus with a question:
Haiku are fun
A short and simple poem
Don't you enjoy them?
  </pre></devsite-code><br></td></tr></tbody></table>

✅ **正向模式**：

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>範例</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Always end haikus with an assertion:
Haiku are fun
A short and simple poem
A joy to write
  </pre></devsite-code><br></td></tr></tbody></table>

### 所有範例使用一致的格式

請確保少量樣本的結構和格式都相同，以免包含不想要格式的回應。在提示中加入少量樣本的主要目標之一，就是向模型展示回應格式。因此，請務必確保所有範例的格式一致，特別是留意 XML 標記、空白字元、換行符號和分割器範例。

### 摘要

*   在提示中加入提示/回應範例，可協助模型瞭解如何做出回應。
*   提供應遵循的模式範例，而非應避免的模式範例。
*   請嘗試納入提示數量。視模型而定，樣本數量過少，無法有效改變模型行為。範例過多會造成模型過度配適。
*   所有範例使用一致的格式

新增情境資訊
------

您可以在提示說明中納入模型解決問題所需的資訊，而不要假設模型具備所有必要資訊。這類情境資訊可協助模型瞭解您要求執行作業的限制和詳細資料。

以下範例要求模型提供路由器的疑難排解指引：

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and
blinking slowly.
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">1. **Check the Cables:**
- Make sure that all cables are securely connected to your Google Wifi router and modem.
- Try replacing the cables with new ones to ensure they are not faulty.


2. **Reboot the Router:**
- Unplug your Google Wifi router and modem from the power outlet.
- Wait for at least 30 seconds.
- Plug the modem and router back in and wait for them to start up.


3. **Factory Reset the Router:**
- Resetting the router will restore it to its default settings.
- Find the small reset button on the back of the router.
- Press and hold the reset button with a paper clip or similar object for 10 seconds.
- Release the button and wait for the router to restart.


4. **Check Your Internet Connection:**
- Use a wired connection to connect a device directly to your modem.
- If the internet works, the issue may be with your router.
- If the internet still doesn't work, contact your Internet Service Provider (ISP).


5. **Update Router's Firmware:**
- Check if there is a firmware update available for your Google Wifi router.
- Download and install the latest firmware update from the Google Wifi app.


6. **Interference and Obstacles:**
- Make sure the router is not near electronic devices that can cause interference, like microwaves or cordless phones.
- Remove any obstacles between the router and your devices, such as furniture or thick walls.


7. **Change Wi-Fi Channel:**
- In the Google Wifi app, go to Settings &gt; Network &amp; General &gt; Advanced Networking.
- Try changing the Wi-Fi channel to a less congested one.


8. **Contact Google Support:**
- If you've tried the above steps and the issue persists, contact Google support for further assistance.
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

回應看起來似乎是一般的疑難排解資訊，而該資訊不屬於路由器或 LED 指示燈的狀態。

如要自訂特定路由器的回應，您可以新增至提示路由器的疑難排解指南，做為提供回應時參考的內容。

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Answer the question using the text below. Respond with only the text provided.
Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.

Text:
Color: Slowly pulsing yellow
What it means: There is a network error.
What to do:
Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.

Color: Fast blinking yellow
What it means: You are holding down the reset button and are factory resetting this device.
What to do:
If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.

Color: Solid yellow
What it means: Router is factory resetting.
What to do:
This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.

Color: Solid red
What it means: Something is wrong.
What to do:
Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support.
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

### 摘要

*   在提示中納入您希望模型在產生回應時使用的資訊 (內容)。
*   向模型提供操作說明，說明如何使用背景資訊資訊。

新增前置字串
------

前置字串是指您在提示內容中新增的字詞或詞組，視前置字串的位置而定，可能有多種用途：

*   **輸入前置字串：**在輸入信號中新增前置字串，表示模型的輸入內容部分在語意上具有意義。舉例來說，「English:」和「法文:」前置字串可區分兩種不同的語言。
*   **輸出前置字串：**雖然輸出是由模型產生，但您可以在提示中為輸出新增前置字串。輸出前置字串會提供模型資訊，說明預期的回應內容。舉例來說，輸出前置字串「JSON:」會向模型發出信號，指出輸出內容應採用 JSON 格式。
*   **範例前置字串：**在少量提示的提示中新增前置字串，為範例提供標籤，讓模型在產生輸出內容時使用，進而更輕鬆地剖析輸出內容。

在以下範例中，「Text:」是輸入內容的前置字串，「答案為:」則是輸出前置字串。

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Classify the text as one of the following categories.
- large
- small
Text: Rhino
The answer is: large
Text: Mouse
The answer is: small
Text: Snail
The answer is: small
Text: Elephant
The answer is:
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">large
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

讓模型完成部分輸入內容
-----------

生成式語言模型的運作方式與進階自動完成工具類似。如果您提供部分內容，模型就能提供其餘內容，或是認為延續該內容做為回應。過程中，如果您納入任何範例或背景資訊，模型可能會將這些範例或背景資訊納入考量。

以下範例提供包含操作說明和實體輸入內容的提示：

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or
drink, with the value being the quantity.

Order: A burger and a drink.
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">```
{
"cheeseburger": 0,
"hamburger": 1,
"fries": 0,
"drink": 1
}
```
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

雖然模型是按照提示提供，但以自然語言寫出指令有時可能並不容易，甚至會導致模型的解讀作業耗費很多。例如，餐廳的菜單可能包含許多項目。如要縮減 JSON 回應的大小，建議您省略未排序的項目。在這種情況下，您可以提供範例和回應前置字串，讓模型加以完成：

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Valid fields are cheeseburger, hamburger, fries, and drink.
Order: Give me a cheeseburger and fries
Output:
```
{
  "cheeseburger": 1,
  "fries": 1
}
```
Order: I want two burgers, a drink, and fries.
Output:
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">```
{
"hamburger": 2,
"drink": 1,
"fries": 1
}
```
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

請注意，「起司漢堡」並非訂單的一部分，因此已從輸出結果中排除。

#### 提示模型設定回應格式

完成策略也有助於設定回應格式。以下範例會提示模型建立短文大綱：

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Create an outline for an essay about hummingbirds.
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">I. Introduction
A. Hook: Begin with an intriguing fact or description of hummingbirds.
B. Provide some background information on hummingbirds.
1. Mention their small size and long, thin beaks.
2. Highlight their unique ability to hover and fly backward.

II. Body
A. Anatomy and Physiology
1. Elaborate on their tiny size, making comparisons to other animals.
2. Describe their wings and how they enable hovering and swift flight.
3. Discuss their metabolism and energy requirements, emphasizing their caloric needs.

B. Feeding Habits and Diet
1. Explain their primary food source, nectar, and how they extract it from flowers.
2. Describe their ability to feed from a wide variety of flowers.
3. Mention their consumption of insects and the nutritional value they provide.

C. Migration Patterns
1. Discuss the incredible long-distance migrations of some hummingbird species.
2. Explain the phenomenon of seasonal migration and the environmental factors driving it.
3. Describe the routes taken by different species during migration.

D. Conservation and Threats
1. Highlight the importance of hummingbirds in ecosystems as pollinators.
2. Discuss the challenges and threats they face, such as habitat loss, nectar scarcity, and climate change.
3. Mention conservation efforts and ways to support hummingbird populations.

III. Conclusion
A. Summarize the main points covered in the essay.
B. Reinforce the importance of hummingbirds and their ecological role.
C. Provide a final thought or call to action to protect these fascinating creatures.
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

提示中並未指定大綱格式，模型已為您選擇格式。如要讓模型以特定格式傳回外框，您可以新增代表外框開頭的文字，讓模型根據您啟動的模式完成大綱。

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Create an outline for an essay about hummingbirds.
I. Introduction
   *
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">I. Introduction
* Capture the reader's attention with an interesting anecdote or fact about hummingbirds.
* Provide a brief background on hummingbirds, including their unique characteristics.
* State the main points that will be covered in the essay.

II. The Unique Characteristics of Hummingbirds
* Discuss the hummingbird's exceptionally rapid wing-beat, allowing them to hover and fly backward.
* Highlight their tiny size, making them the smallest birds in the world.
* Describe their long, slender beaks and tongues, allowing them to reach deep into flowers to extract nectar.
* Explain their iridescent plumage, which creates brilliant and vibrant colors.

III. Hummingbird Migration and Distribution
* Discuss the extensive migration patterns of hummingbirds, covering vast distances across continents.
* Describe the different habitats where hummingbirds can be found, including tropical rainforests, deserts, and urban areas.
* Explain the seasonal changes that influence hummingbird migration and habitat selection.

IV. Hummingbird Diet and Feeding Habits
* Focus on the hummingbird's primary food source, which is nectar from flowers.
* Describe their ability to consume insects, spiders, and other small invertebrates for protein.
* Explain how hummingbirds use their long, slender tongues to extract nectar from flowers.
* Discuss the importance of flowering plants in providing sustenance for hummingbirds.

V. Reproduction and Nesting Behavior
* Describe the mating rituals and courtship behavior of hummingbirds.
* Explain the process of nest-building, including the materials used and the unique characteristics of hummingbird nests.
* Discuss the role of the female hummingbird in laying and incubating eggs.
* Describe the development of hummingbird chicks and the role of both parents in providing care.

VI. Threats to Hummingbirds and Conservation Efforts
* Highlight habitat loss, climate change, and deforestation as significant threats to hummingbird populations.
* Describe the role of habitat conservation initiatives in protecting hummingbird habitats.
* Explain the importance of creating hummingbird-friendly gardens and landscapes.
* Discuss the efforts of organizations and individuals working to conserve hummingbird populations.

VII. Conclusion
* Summarize the main points covered in the essay, emphasizing the unique characteristics, migration patterns, diet, reproduction, and conservation of hummingbirds.
* Provide a closing statement that leaves a lasting impression on the reader and reinforces the significance of these fascinating creatures.
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

### 摘要

*   如果您向模型提供部分輸入內容，模型會根據提示中的任何可用範例或背景資訊完成輸入內容。
*   有時，讓模型完成輸入內容，可能會比使用自然語言描述工作來得容易。
*   在提示中加入部分答案，可以引導模型遵循所需的模式或格式。

將提示拆分為簡易元件
----------

如果是需要複雜提示的用途，您可以將所有內容細分為較簡單的元件，協助模型管理複雜性。

### 詳細操作說明

與其一次列出多個操作說明，只需為每個指令分別建立提示即可。您可以根據使用者的輸入內容選擇要處理的提示。

### 鏈結提示

如果是涉及多個依序完成步驟的複雜工作，請為每個步驟顯示提示，並將提示串聯成序列。在這類提示序列鏈中，序列中一則提示的輸出內容會成為下一個提示的輸入內容。序列中最後一個提示的輸出內容是最終輸出內容。

### 匯總回應

「匯總」可讓您對資料的不同部分執行不同的平行工作，然後匯總結果以產生最終輸出內容。舉例來說，您可以指示模型對資料的第一部分執行一項作業、對其他資料執行另一項作業並匯總結果。

### 摘要

*   將複雜的指令細分為每項指示的提示，並根據使用者輸入內容決定要套用哪種提示。
*   將多個依序步驟分成不同的提示並鏈結，讓上述提示中的輸出內容成為下列提示的輸入內容。
*   將平行工作細分並匯總回應，以產生最終輸出內容。

測試不同參數值
-------

您傳送至模型的每個呼叫都含有參數值，用來控制模型產生回應的方式。模型可能會為不同的參數值產生不同的結果。嘗試不同參數值，取得最適合任務的值。不同模型可用的參數可能會有所不同。最常見的參數如下：

*   輸出內容符記數量上限
*   隨機性參數
*   Top-K
*   Top-P

### 輸出內容符記數量上限

回應中可產生的權杖數量上限。符記約有四個字元。100 個符記對應約 20 個字詞。

如要取得較短的回覆，請指定較低的值；如要取得較長的回應，請調高此值。

### 隨機性參數

這個溫度會在產生回應時用於取樣，發生時遇到了套用 `topP` 和 `topK` 的情形。隨機性參數會決定選取符記的隨機程度。較低的隨機性參數適合需要具確定性、較不具開放性或創意回應的提示；而隨機性參數較高，則可能產生較多元或有創意的結果。隨機性參數為「`0`」具有確定性，即一律會選取可能性最高的回應。

以大部分用途來說，可以先嘗試將隨機性參數設為 `0.2`。如果模型的回覆太普通、太短或提供了備用回應，請試著調高隨機性參數。

### Top-K

「Top-K」會影響模型選取輸出符記的方式。如果「Top-K」設為「`1`」，代表下一個所選符記是模型詞彙表的所有符記中可能性最高者 (也稱為「貪婪解碼」)。如果「前 K 個」設為 `3`，則代表模型會依據隨機性參數，從可能性最高的 3 個符記中選取下一個符記。

在每個符記選取步驟中，模型會對機率最高的「前 K 個」符記取樣。接著進一步根據「Top-P」篩選符記，最後依隨機性參數選出最終符記。

如要取得較不隨機的回應，請指定較低的值；如要取得較隨機的回應，請調高此值。「前 K 個」的預設值為 `40`。

### Top-P

「Top-P」會影響模型選取輸出符記的方式。模型會按照機率最高 (請見「Top-K」) 到最低的順序選取符記，直到所選符記的機率總和等於「Top-P」值。舉例來說，如果符記 A、B 和 C 的可能性分別為 0.3、0.2 和 0.1，而「可能性總和為 P」的值為 `0.5`，則模型會依據隨機性參數選擇 A 或 B 做為下一個符記，並排除 C。

如要取得較不隨機的回應，請指定較低的值；如要取得較隨機的回應，請調高此值。「可能性總和為 P」的預設值為 `0.95`。

提示疊代策略
------

提示設計是一種疊代程序，通常需要經過多次疊代才能獲得一致的回應本節提供在提示疊代時可以嘗試的指南。

### 使用不同措辭

在提示中使用不同字詞或措辭通常會產生不同的回應，即使這些字的意思相同，也通常不會與模型產生不同。如果提示未達到預期的結果，請試著改寫提示。

<table class="" style="background-color: gray"><tbody><tr><td><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Version 1:
How do I bake a pie?

Version 2:
Suggest a recipe for a pie.

Version 3:
What's a good pie recipe?
  </pre></devsite-code><br></td></tr></tbody></table>

### 切換到類似的工作

如果您無法讓模型按照工作的操作說明進行，請嘗試為達到相同結果的類似工作給予指示。

這則提示會告知模型，使用預先定義的類別將書籍分類。

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Which category does The Odyssey belong to:
thriller
sci-fi
mythology
biography
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">The answer: mythology

Explanations:

The Odyssey is an epic poem in ancient Greek literature. It is one of two major ancient Greek epic
poems attributed to Homer. The Odyssey is an epic poem that tells the story of Odysseus, a Greek
hero who fought in the Trojan War and then spent ten years trying to return home to Ithaca. The
Odyssey is a work of mythology.
  </pre></devsite-code><label style="text-align:right">(text-bison@001)</label></td></tr></tbody></table>

回應正確，但模型並未保持在選項的邊界內。您也會希望模型只使用其中一個選項回應，而非完整的句子。在此情況下，您可以將操作說明改寫為選擇題，並要求模型選擇一個選項。

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>提示：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Multiple choice problem: Which of the following options describes the book The Odyssey?
Options:
- thriller
- sci-fi
- mythology
- biography
  </pre></devsite-code><label><strong>回應：</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">The answer is: mythology
  </pre></devsite-code><label style="text-align:right">(text-bison@001)</label></td></tr></tbody></table>

### 變更提示內容的順序

提示中的內容順序有時可能會影響回應。請嘗試變更內容順序，看看這會如何影響回應。

Version 1:
\[examples\]
\[context\]
\[input\]

Version 2:
\[input\]
\[examples\]
\[context\]

Version 3:
\[examples\]
\[input\]
\[context\]

備用回應
----

備用回應是在提示或回應觸發安全性篩選器時，模型傳回的回應。備用回應的示例為「我無法解決這個問題，因為我只是語言模型」。

如果模型傳回備用回應，請嘗試調高隨機性參數。

應避免的事項
------

*   避免仰賴模型產生事實資訊。
*   謹慎使用數學和邏輯問題。

後續步驟
----

*   現在您已對提示設計有更深入的瞭解，不妨使用 [Google AI Studio](http://makersuite.google.com?hl=zh-tw) 自行撰寫提示。
*   如要瞭解多模態提示，請參閱「[使用媒體檔案提示](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=zh-tw)」。

這對你有幫助嗎？

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2024-05-14 (世界標準時間)。
---
Please provide me with more context! I need to know what kind of mission you're trying to write about. 

For example, tell me: "* **What is the mission for?** Is it a company, a project, a personal goal, a video game, etc.? "
* **What is the overall objective?** What are you trying to achieve? 
* **Who is the target audience?** Who is this mission meant for?

Once you give me some more information, I can help you write a compelling and effective mission statement.
---

*   このページの内容
*   [403 アクセス制限付きエラーについて](#understand-403-errors)
*   [Google AI Studio で「コンテンツがない」というレスポンスを解決する](#resolve-no-content)
*   [トークンの使用量と上限を確認する](#check-token-usage)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API デベロッパー コンテストにご参加ください。[詳細](https://ai.google.dev/competition?hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja) このページは [Cloud Translation API](//cloud.google.com/translate/?hl=ja) によって翻訳されました。

*   [Google AI for Developers](https://ai.google.dev/?hl=ja)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
*   [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

この情報は役に立ちましたか？

フィードバックを送信

Google AI Studio のトラブルシューティング
=============================

bookmark\_borderbookmark コレクションでコンテンツを整理 必要に応じて、コンテンツの保存と分類を行います。

*   このページの内容
*   [403 アクセス制限付きエラーについて](#understand-403-errors)
*   [Google AI Studio で「コンテンツがない」というレスポンスを解決する](#resolve-no-content)
*   [トークンの使用量と上限を確認する](#check-token-usage)

このページでは、Google AI Studio で問題が発生した場合のトラブルシューティングについて説明します。

403 アクセス制限付きエラーについて
-------------------

403 アクセス制限エラーが表示される場合、[利用規約](https://ai.google.dev/terms?hl=ja)に従っていない方法で Google AI Studio を使用しています。よくある理由の 1 つは、お客様が[サポートされているリージョン](https://ai.google.dev/available_regions?hl=ja)にお住まいでないことです。

Google AI Studio で「コンテンツがない」というレスポンスを解決する
-----------------------------------------

なんらかの理由でコンテンツがブロックされると、Google AI Studio に warning \[**コンテンツがありません**\] というメッセージが表示されます。詳細を表示するには、\[**コンテンツなし**\] の上にポインタを置いて、warning \[**セーフティ**\] をクリックします。

[安全性設定](https://ai.google.dev/docs/safety_setting?hl=ja)が原因でレスポンスがブロックされ、ユースケースの[安全性リスク](https://ai.google.dev/docs/safety_guidance?hl=ja)を考慮した場合は、[安全性設定](https://ai.google.dev/docs/safety_setting?hl=ja#safety_settings_in_makersuite)を変更して、返されるレスポンスに影響を与えることができます。

レスポンスがブロックされたが、安全性設定によるものでない場合、クエリまたはレスポンスは[利用規約](https://ai.google.dev/terms?hl=ja)に違反しているか、それ以外の理由でサポートされていない可能性があります。

トークンの使用量と上限を確認する
----------------

プロンプトを開くと、画面下部の \[**Text Preview**\] ボタンに、プロンプトの内容に使用されている現在のトークンと、使用されているモデルの最大トークン数が表示されます。

この情報は役に立ちましたか？

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2024-04-19 UTC。
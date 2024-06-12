---
Please provide me with more context! I need to know what your mission is about in order to help you write it. 

For example, tell me: "* **What is the subject of the mission?** (e.g., a company, a project, a personal goal)"
* **What is the overall goal of the mission?** (e.g., to achieve success, to solve a problem, to make a difference)
* **What are the key objectives or steps involved in achieving the mission?** 

Once I have this information, I can help you craft a compelling and effective mission statement.
---

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API デベロッパー コンテストにご参加ください。[詳細](https://ai.google.dev/competition?hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja) このページは [Cloud Translation API](//cloud.google.com/translate/?hl=ja) によって翻訳されました。

*   [Google AI for Developers](https://ai.google.dev/?hl=ja)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
*   [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

この情報は役に立ちましたか？

フィードバックを送信

API バージョンの説明
============

bookmark\_borderbookmark コレクションでコンテンツを整理 必要に応じて、コンテンツの保存と分類を行います。

このドキュメントでは、G ミニ API の v1 バージョンと v1beta バージョンの違いの概要を説明します。

*   **v1**: 安定版の API。安定版の機能は、メジャー バージョンの全期間にわたって完全にサポートされます。互換性を破る変更がある場合は、API の次のメジャー バージョンが作成され、妥当な期間の経過後に既存のバージョンのサポートを終了します。メジャー バージョンを変更することなく、互換性を損なわない変更を API に導入できます。
*   **v1beta**: このバージョンには、開発中の早期アクセス機能が含まれており、互換性を破る変更が行われる可能性があります。また、ベータ版の機能が安定版に移行される保証もありません。不安定であるため、このバージョンで製品版アプリを起動しないでください。

| 機能 | v1 | v1beta |
| --- | --- | --- |
| コンテンツの生成 - テキストのみの入力 |  |  |
| コンテンツの生成 - テキストと画像の入力 |  |  |
| コンテンツの生成 - テキスト出力 |  |  |
| コンテンツの生成 - マルチターンの会話（チャット） |  |  |
| コンテンツの生成 - 関数呼び出し |  |  |
| コンテンツの生成 - ストリーミング |  |  |
| コンテンツの埋め込み - テキストのみの入力 |  |  |
| 回答を生成 |  |  |
| セマンティック レトリバー |  |  |
| テキストの生成（PaLM） |  |  |
| エンベディングの生成（PaLM） |  |  |
| メッセージの生成（PaLM） |  |  |
| チューニング（PaLM） |  |  |

*   \- 対応
*   \- 今後サポートされない

この情報は役に立ちましたか？

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2024-04-18 UTC。
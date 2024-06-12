---
Please provide me with the context for your mission statement! I need more information to help you write it effectively. 

For example, tell me: "* **What is the purpose of your mission?**  Is it for a company, a non-profit, a personal project, or something else?"
* **What are your goals?** What do you want to achieve with your mission?
* **What are your values?** What principles guide your work?
* **Who is your target audience?** Who will be impacted by your mission?

Once I have this information, I can help you craft a compelling and impactful mission statement.
---

*   このページの内容
*   [curl コマンドを使用して API キーを確認する](#verify-key-with-curl)
*   [API キーのセキュリティ確保](#security)
*   [次のステップ](#next-steps)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API デベロッパー コンテストにご参加ください。[詳細](https://ai.google.dev/competition?hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja) このページは [Cloud Translation API](//cloud.google.com/translate/?hl=ja) によって翻訳されました。

*   [Google AI for Developers](https://ai.google.dev/?hl=ja)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
*   [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

この情報は役に立ちましたか？

フィードバックを送信

API キーを取得する
===========

bookmark\_borderbookmark コレクションでコンテンツを整理 必要に応じて、コンテンツの保存と分類を行います。

*   このページの内容
*   [curl コマンドを使用して API キーを確認する](#verify-key-with-curl)
*   [API キーのセキュリティ確保](#security)
*   [次のステップ](#next-steps)

Gemini API を使用するには、API キーが必要です。Google AI Studio ではワンクリックでキーを作成できます。

[API キーを取得する](https://makersuite.google.com/app/apikey?hl=ja)

**重要:** API キーは安全に使用することを忘れないでください。[API キーを安全に保護する](#security)を確認した後、[API クイックスタート](https://ai.google.dev/tutorials?hl=ja)を確認し、API キーを保護するための言語別のベスト プラクティスを確認してください。

curl コマンドを使用して API キーを確認する
--------------------------

設定の確認には curl コマンドを使用します。API キーは、次のいずれかの URL で渡すことができます。

    API_KEY="YOUR_API_KEY"

または `x-goog-api-key` ヘッダーで次のようにします。

    API_KEY="YOUR_API_KEY"

API キーのセキュリティ確保
---------------

Gemini API キーは安全に保管することが重要です。Gemini API キーを使用する際は、以下の点にご注意ください。

*   Google AI Gemini API は、認証に API キーを使用します。他のユーザーが Gemini API キーにアクセスすると、そのユーザーはプロジェクトの割り当てを使用して呼び出しを行えるため、割り当ての消失や追加の課金が発生する可能性があります（課金が有効になっている場合）。API キーは、チューニング済みのモデルやファイルへのアクセスも保護します。
    
*   Google AI Studio で \[**API キーを取得**\] をクリックし、Gemini API キーを新規または既存の Google Cloud プロジェクトのどちらでプロビジョニングするかを選択します。[Google AI Studio の API キーリスト](https://aistudio.google.com/app/apikey?hl=ja)には、Google AI Gemini API で使用するために AI Studio がプロビジョニングしたすべての API キーと、関連するすべての Google Cloud プロジェクトが表示されます。
    
    *   ただし、Google Cloud プロジェクト内の_任意の_ API キーを使用して、Google AI Gemini API を呼び出すことができます。すべてのプロジェクトの API キーは、Google Cloud コンソールの [\[API とサービス\] > \[認証情報\] パネル](https://console.cloud.google.com/apis/credentials?project=_&hl=ja)で表示および管理できます。
*   [API キーの制限](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=ja#add-api-restrictions)を追加すると、各 API キーで使用できるサーフェス領域を制限できます。デフォルトでは、Google AI Studio によって生成された Genmini API キーは、Google AI Genmini API（正式には「Generative Language API」または `generativelanguage.googleapis.com` と呼ばれています）でのみ使用できます。
    
    *   Google Cloud プロジェクト内に API の制限がない API キーや、Generative Language API の許可リストに登録されている API キーがある場合、それらのキーは Google AI Gemini API で使用できます。各 API キーは、そのキーを使用して呼び出す API のみに制限することをおすすめします。
    *   API キーに制限があっても、悪意のある人物が API キーを取得すると、その API キーの許可リストに登録されたすべての API に対するプロジェクトの割り当てを使用して呼び出しが行われる可能性があります。
*   Gemini API キーのセキュリティ管理は、お客様の責任となります。
    
    *   Gemini API キーはソース管理に組み込まないでください。
    *   クライアントサイド アプリケーション（Android、Swift、ウェブ、Dart/Flutter）では、API キーが公開されるリスクがあるため、本番環境アプリで Google AI クライアント SDK を使用して、モバイルアプリやウェブアプリから直接 Google AI Gemini API を呼び出すことはおすすめしません。API キーを保護するための言語固有のベスト プラクティスについては、[SDK クイックスタート](https://ai.google.dev/tutorials?hl=ja)をご覧ください。

一般的なベスト プラクティスについては、こちらの[サポート記事](https://support.google.com/googleapi/answer/6310037?hl=ja)もご覧ください。

次のステップ
------

*   API キーを保護し、使用するためのベスト プラクティスについては、[API クイックスタート](https://ai.google.dev/tutorials?hl=ja)をご覧ください。

この情報は役に立ちましたか？

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2024-04-24 UTC。
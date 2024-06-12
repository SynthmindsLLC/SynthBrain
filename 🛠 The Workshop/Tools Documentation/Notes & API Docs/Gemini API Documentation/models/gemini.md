---
Please provide me with the context or the subject of the mission you want to create. For example: "* **What is the mission of your company?**"
* **What is the mission of your project?**
* **What is the mission of a space exploration team?**

Once you provide me with the context, I can help you craft a compelling and impactful mission statement.
---

*   このページの内容
*   [モデル バリエーション](#model-variations)
    *   [Gemini 1.5 Pro](#gemini-1.5-pro)
    *   [Gemini 1.5 Flash](#gemini-1.5-flash)
    *   [Gemini 1.0 Pro](#gemini-1.0-pro)
    *   [Gemini 1.0 Pro Vision](#gemini-1.0-pro-vision)
    *   [テキストの埋め込みと埋め込み](#text-embedding-and-embedding)
    *   [AQA](#aqa)
*   [モデル バージョン名のパターン](#model-versions)
*   [対応言語](#available-languages)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API デベロッパー コンテストにご参加ください。[詳細](https://ai.google.dev/competition?hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja) このページは [Cloud Translation API](//cloud.google.com/translate/?hl=ja) によって翻訳されました。

*   [Google AI for Developers](https://ai.google.dev/?hl=ja)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
*   [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

この情報は役に立ちましたか？

フィードバックを送信

Gemini
======

bookmark\_borderbookmark コレクションでコンテンツを整理 必要に応じて、コンテンツの保存と分類を行います。

*   このページの内容
*   [モデル バリエーション](#model-variations)
    *   [Gemini 1.5 Pro](#gemini-1.5-pro)
    *   [Gemini 1.5 Flash](#gemini-1.5-flash)
    *   [Gemini 1.0 Pro](#gemini-1.0-pro)
    *   [Gemini 1.0 Pro Vision](#gemini-1.0-pro-vision)
    *   [テキストの埋め込みと埋め込み](#text-embedding-and-embedding)
    *   [AQA](#aqa)
*   [モデル バージョン名のパターン](#model-versions)
*   [対応言語](#available-languages)

Gemini は、デベロッパーがコンテンツを生成して問題を解決できる生成 AI モデルのファミリーです。これらのモデルは、テキストと画像の両方を入力として処理するように設計、トレーニングされています。このガイドでは、各モデル バリアントに関する情報を提供し、どちらがユースケースに最も適しているかを判断するのに役立ちます。

モデル バリエーション
-----------

Gemini API には、特定のユースケース向けに最適化されたさまざまなモデルが用意されています。利用可能な Gemini のバリエーションの概要は次のとおりです。

| モデル バリアント | 入力 | 出力 | 最適な用途 |
| --- | --- | --- | --- |
| [Gemini 1.5 Pro](#gemini-1.5-pro)  
`gemini-1.5-pro` | 音声、画像、動画、テキスト | テキスト | 複雑な推論タスク（コードとテキストの生成、テキスト編集、問題解決、データの抽出、生成など） |
| [Gemini 1.5 Flash](#gemini-1.5-flash)  
`gemini-1.5-flash` | 音声、画像、動画、テキスト | テキスト | さまざまなタスクに対応する高速で汎用性の高いパフォーマンス |
| [Gemini 1.0 Pro](#gemini-1.0-pro)  
`gemini-1.0-pro` | テキスト | テキスト | 自然言語タスク、マルチターンのテキスト チャットとコードチャット、コード生成 |
| [Gemini 1.0 Pro Vision](#gemini-1.0-pro-vision)  
`gemini-pro-vision` | 画像、動画、テキスト | テキスト | 画像関連のタスク（画像の説明の生成や画像内のオブジェクトの識別など） |
| [テキスト エンベディング](#text-embedding-and-embedding)  
`text-embedding-004` | テキスト | テキスト エンベディング | テキスト文字列の関連性の測定 |

次の表に、すべてのモデル バリアントに共通する Gemini モデルの属性を示します。

| 属性 | 説明 |
| --- | --- |
| トレーニング データ | Gemini のナレッジの締め切りは 2023 年 11 月です。それ以降に発生したイベントに関する情報は制限されます。 |
| サポートされている言語 | [対応言語を見る](https://ai.google.dev/models/gemini?hl=ja#available-languages) |
| 構成可能なモデル パラメータ | 
*   トップ P
*   トップ K
*   Temperature
*   停車シーケンス
*   最大出力長
*   回答候補の数

 |

**注:** 構成可能なパラメータは、テキストとチャットのモデルのバリエーションにのみ適用され、エンベディングには適用されません。

これらの各パラメータの詳細については、生成モデルガイドの[モデル パラメータのセクション](https://ai.google.dev/gemini-api/docs/models/generative-models?hl=ja#model-parameters)をご覧ください。

### Gemini 1.5 Pro

Gemini 1.5 Pro は、次のような幅広い推論タスク向けに最適化された中規模のマルチモーダル モデルです。

*   コード生成
*   テキスト生成
*   テキスト編集
*   問題を解決する
*   推奨事項の生成
*   情報抽出
*   データの抽出または生成
*   AI エージェントの作成

1.5 Pro では、1 時間の動画、9.5 時間分の音声、30,000 行を超えるコードや 700,000 語を超えるコードベースなど、大量のデータを一度に処理できます。

1.5 Pro は、ゼロショット、ワンショット、少数ショット学習タスクに対応できます。

#### モデルの詳細

| プロパティ | 説明 |
| --- | --- |
| モデルコード | `models/gemini-1.5-pro-latest` |
| 入力 | 音声、画像、動画、テキスト |
| 出力 | テキスト |
| サポートされている生成方法 | `[generateContent](https://ai.google.dev/api/rest/v1/models/generateContent?hl=ja)` |
| 入力トークンの上限[\[\*\*\]](#token-size) | 1,048,576 |
| 出力トークンの上限 [\[\*\*\]](#token-size) | 8,192 |
| プロンプトあたりの画像の最大数 | 3,600 |
| 動画の長さの上限 | 1 時間 |
| 音声の最大長 | 約 9.5 時間 |
| プロンプトあたりの音声ファイルの最大数 | 1 |
| モデルの安全性 | 自動的に適用される安全性設定（デベロッパーが調整可能）。詳しくは、[安全性設定に関するページ](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja)をご覧ください。 |
| レート制限[\[\*\]](#rate-limits) | 
**無料:**

*   2 rpm
*   32,000 TPM
*   50 RPD
*   46,080,000 TPD

**Pay-as-you-go:**

*   360 rpm
*   200 万 TPM
*   10,000 RPD
*   14,400,000,000 TPD

**200 万件のコンテキスト:**

*   1 rpm
*   200 万 TPM
*   50 RPD



 |
| システム指示 | サポート対象 |
| JSON モード | サポート対象 |
| 最新バージョン | `gemini-1.5-pro-latest` |
| 最新の安定版 | `gemini-1.5-pro` |
| 安定版 | `gemini-1.5-pro-001` |
| 最新のアップデート | 2024 年 5 月 |

### Gemini 1.5 Flash

Gemini 1.5 Flash は、さまざまなタスクに合わせてスケーリングできる、高速で汎用性の高いマルチモーダル モデルです。

#### モデルの詳細

| プロパティ | 説明 |
| --- | --- |
| モデルコード | `gemini-1.5-flash-latest` |
| 入力 | 音声、画像、動画、テキスト |
| 出力 | テキスト |
| サポートされている生成方法 | `[generateContent](https://ai.google.dev/api/rest/v1/models/generateContent?hl=ja)` |
| 入力トークンの上限[\[\*\*\]](#token-size) | 1,048,576 |
| 出力トークンの上限 [\[\*\*\]](#token-size) | 8,192 |
| プロンプトあたりの画像の最大数 | 3,600 |
| 動画の長さの上限 | 1 時間 |
| 音声の最大長 | 約 9.5 時間 |
| プロンプトあたりの音声ファイルの最大数 | 1 |
| モデルの安全性 | 自動的に適用される安全性設定（デベロッパーが調整可能）。詳しくは、[安全性設定に関するページ](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja)をご覧ください。 |
| レート制限[\[\*\]](#rate-limits) | 
**無料:**

*   15rpm
*   100 万 TPM
*   1,500 RPD

**Pay-as-you-go:**

*   1,000 rpm
*   200 万 TPM



 |
| システム指示 | サポート対象 |
| JSON モード | サポート対象 |
| モデルのチューニング | 近日提供予定 |
| 最新バージョン | `gemini-1.5-flash-latest` |
| 最新の安定版 | `gemini-1.5-flash` |
| 安定版 | `gemini-1.5-flash-001` |
| 最新のアップデート | 2024 年 5 月 |

### Gemini 1.0 Pro

Gemini 1.0 Pro は、マルチターンのテキスト チャットやコードチャット、コード生成などのタスクを処理する NLP モデルです。

1.0 Pro は、ゼロショット、ワンショット、少数ショット学習タスクに対応できます。

#### モデルの詳細

| プロパティ | 説明 |
| --- | --- |
| モデルコード | `models/gemini-1.0-pro` |
| 入力 | テキスト |
| 出力 | テキスト |
| サポートされている生成方法 | 
Python: `[generate_content](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ja#generate_content)`

REST: `[generateContent](https://ai.google.dev/api/rest/v1/models/generateContent?hl=ja)`

 |
| レート制限[\[\*\]](#rate-limits) | 

**無料:**

*   15rpm
*   32,000 TPM
*   1,500 RPD
*   46,080,000 TPD

**Pay-as-you-go:**

*   360 rpm
*   120,000 TPM
*   30,000 RPD
*   172,800,000 TPD



 |
| システム指示 | サポート対象外 |
| JSON モード | サポート対象外 |
| モデルのチューニング | サポート対象: `gemini-1.0-pro-001` |
| 最新バージョン | `gemini-1.0-pro-latest` |
| 最新の安定版 | `gemini-1.0-pro` |
| 安定版 | `gemini-1.0-pro-001` |
| 最新のアップデート | 2024 年 2 月 |

**注:** `gemini-pro` は `gemini-1.0-pro` のエイリアスです。

### Gemini 1.0 Pro Vision

Gemini 1.0 Pro Vision は、パフォーマンスが最適化されたマルチモーダル モデルで、ビジュアル関連のタスクを実行できるものです。たとえば、1.0 Pro Vision では、画像の説明の生成、画像内のオブジェクトの特定、画像内の場所やオブジェクトに関する情報の提供などを行うことができます。

1.0 Pro Vision は、ゼロショット、ワンショット、少数ショットのタスクを処理できます。

#### モデルの詳細

| プロパティ | 説明 |
| --- | --- |
| モデルコード | `models/gemini-pro-vision` |
| 入力 | テキスト、動画、画像 |
| 出力 | テキスト |
| サポートされている生成方法 | 
Python: `[generate_content](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=ja#generate_content)`

REST: `[generateContent](https://ai.google.dev/api/rest/v1/models/generateContent?hl=ja)`

 |
| 入力トークンの上限 [\[\*\]](#token-size) | 12,288 |
| 出力トークンの上限 [\[\*\]](#token-size) | 4,096 |
| 最大画像サイズ | 上限なし |
| プロンプトあたりの画像の最大数 | 16 |
| 動画の長さの上限 | 2 分 |
| メッセージあたりの動画の最大数 | 1 |
| モデルの安全性 | 自動的に適用される安全性設定（デベロッパーが調整可能）。詳しくは、[安全性設定に関するページ](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja)をご覧ください。 |
| レート制限[\[\*\]](#rate-limits) | 1 分あたり 60 回のリクエスト |
| 最新バージョン | `gemini-1.0-pro-vision-latest` |
| 最新の安定版 | `gemini-1.0-pro-vision` |
| 最新のアップデート | 2023 年 12 月 |

### テキストの埋め込みと埋め込み

#### テキスト エンベディング

Text Embedding モデルを使用して、入力テキストの[テキスト エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)を生成できます。テキスト エンベディング モデルの詳細については、テキスト エンベディングに関する [Vertex AI の生成 AI のドキュメント](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings?hl=ja)をご覧ください。

Text Embedding モデルは、最大 2,048 トークンのテキストに対して 768 次元のエンベディングを作成するように最適化されています。テキスト エンベディングでは、768 未満のエラスティックなエンベディング サイズを使用できます。弾力性のあるエンベディングを使用すると、より小さな出力ディメンションを生成できます。また、パフォーマンスをわずかに低下させるだけで、コンピューティングとストレージの費用を節約できる可能性があります。

##### モデルの詳細

| プロパティ | 説明 |
| --- | --- |
| モデルコード | `models/text-embedding-004`（[Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings?hl=ja#latest_models) では `text-embedding-preview-0409`） |
| 入力 | テキスト |
| 出力 | テキスト エンベディング |
| 入力トークンの上限 | 2,048 |
| 出力ディメンション サイズ | 768 |
| サポートされている生成方法 | 
Python: `[embed_content](https://ai.google.dev/api/python/google/generativeai/embed_content?hl=ja)`

REST: `[embedContent](https://ai.google.dev/api/rest/v1/models/embedContent?hl=ja)`

 |
| モデルの安全性 | 調整可能な安全設定はありません。 |
| レート制限[\[\*\]](#rate-limits) | 1 分あたり 1,500 回のリクエスト |
| 最新のアップデート | 2024 年 4 月 |

#### エンベディング

**注:** テキスト エンベディングは、エンベディング モデルの新しいバージョンです。新しいプロジェクトを作成する場合は、テキスト埋め込みを使用します。

エンベディング モデルを使用すると、入力テキストの[テキスト エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)を生成できます。

エンベディング モデルは、最大 2,048 トークンのテキストに対して 768 次元のエンベディングを作成するように最適化されています。

##### エンベディング モデルの詳細

| プロパティ | 説明 |
| --- | --- |
| モデルコード | `models/embedding-001` |
| 入力 | テキスト |
| 出力 | テキスト エンベディング |
| 入力トークンの上限 | 2,048 |
| 出力ディメンション サイズ | 768 |
| サポートされている生成方法 | 
Python: `[embed_content](https://ai.google.dev/api/python/google/generativeai/embed_content?hl=ja)`

REST: `[embedContent](https://ai.google.dev/api/rest/v1/models/embedContent?hl=ja)`

 |
| モデルの安全性 | 調整可能な安全設定はありません。 |
| レート制限[\[\*\]](#rate-limits) | 1 分あたり 1,500 回のリクエスト |
| 最新のアップデート | 2023 年 12 月 |

### AQA

AQA モデルを使用すると、ドキュメント、コーパス、または一連の文に対して、[Attributed Question-Answering](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=ja)（AQA）関連のタスクを実行できます。AQA モデルは、回答可能な確率を推定し、提供された情報源に基づく質問への回答を返します。

#### モデルの詳細

| プロパティ | 説明 |
| --- | --- |
| モデルコード | `models/aqa` |
| 入力 | テキスト |
| 出力 | テキスト |
| サポートされている生成方法 | 
Python: `[GenerateAnswerRequest](https://ai.google.dev/api/python/google/ai/generativelanguage/GenerateAnswerRequest?hl=ja)`

REST: `[generateAnswer](https://ai.google.dev/api/rest/v1beta/models/generateAnswer?hl=ja)`

 |
| サポートされている言語 | 英語 |
| 入力トークンの上限[\[\*\*\]](#token-size) | 7,168 |
| 出力トークンの上限 [\[\*\*\]](#token-size) | 1,024 |
| モデルの安全性 | 自動的に適用される安全性設定（デベロッパーが調整可能）。詳しくは、[安全性設定に関するページ](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja)をご覧ください。 |
| レート制限[\[\*\]](#rate-limits) | 1 分あたり 60 回のリクエスト |
| 最新のアップデート | 2023 年 12 月 |

これらのモデル バリエーションの機能については、[例](https://ai.google.dev/examples?hl=ja)をご覧ください。

\[\*\] トークンは Gemini モデルで約 4 文字に相当します。100 トークンは約 60 ～ 80 英単語です。

\[\*\*\] _RPM: 1 分あたりのリクエスト数_  
_TPM: 1 分あたりのトークン数_  
_RPD: 1 日あたりのリクエスト数_  
_TPD: 1 日あたりのトークン数_  
  
容量制限により、指定された最大レート制限は保証されません。

モデル バージョン名のパターン
---------------

Gemini モデルには、_プレビュー_ バージョンと_安定版_があります。コードでは、次のいずれかのモデル名形式を使用して、使用するモデルとバージョンを指定できます。

*   **最新:** 指定した世代とバリエーションのモデルの最新バージョンを指します。基盤となるモデルは定期的に更新され、プレビュー版の場合もあります。このエイリアスは、探索的テストのアプリとプロトタイプにのみ使用してください。
    
    最新バージョンを指定するには、`<model>-<generation>-<variation>-latest` のパターンを使用します。例: `gemini-1.0-pro-latest`。
    
*   **最新の安定版:** 指定したモデル世代とバリエーション向けにリリースされた最新の安定版を指します。
    
    最新の安定版を指定するには、`<model>-<generation>-<variation>` のパターンを使用します。例: `gemini-1.0-pro`
    
*   **安定版:** 特定の安定版モデルを指します。安定版のモデルは変わりません。ほとんどの本番環境アプリは、特定の安定版モデルを使用する必要があります。
    
    安定版を指定するには、`<model>-<generation>-<variation>-<version>` のパターンを使用します。例: `gemini-1.0-pro-001`。
    

対応言語
----

Gemini モデルは、次の言語で動作するようにトレーニングされています。

*   アラビア語（`ar`）
*   ベンガル語（`bn`）
*   ブルガリア語（`bg`）
*   中国語（簡体および繁体）（`zh`）
*   クロアチア語（`hr`）
*   チェコ語（`cs`）
*   デンマーク語（`da`）
*   オランダ語（`nl`）
*   英語（`en`）,
*   エストニア語（`et`）
*   フィンランド語（`fi`）
*   フランス語（`fr`）
*   ドイツ語（`de`）
*   ギリシャ語（`el`）
*   ヘブライ語（`iw`）
*   ヒンディー語（`hi`）
*   ハンガリー語（`hu`）
*   インドネシア語（`id`）
*   イタリア語（`it`）
*   日本語（`ja`）
*   韓国語（`ko`）
*   ラトビア語（`lv`）,
*   リトアニア語（`lt`）
*   ノルウェー語（`no`）
*   ポーランド語（`pl`）
*   ポルトガル語（`pt`）
*   ルーマニア語（`ro`）
*   ロシア語（`ru`）
*   セルビア語（`sr`）
*   スロバキア語（`sk`）
*   スロベニア語（`sl`）
*   スペイン語（`es`）
*   スワヒリ語（`sw`）
*   スウェーデン語（`sv`）
*   タイ語（`th`）
*   トルコ語（`tr`）
*   ウクライナ語（`uk`）
*   ベトナム語（`vi`）

この情報は役に立ちましたか？

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2024-05-30 UTC。
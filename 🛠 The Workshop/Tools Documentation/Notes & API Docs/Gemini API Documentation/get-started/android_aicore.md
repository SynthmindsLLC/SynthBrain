*   このページの内容
*   [オンデバイス実行のメリット](#benefits-on-device)
*   [仕組み](#how-it)
*   [次のステップ](#whats-next)

Gemini API デベロッパー コンテストにご参加ください。[詳細](https://ai.google.dev/competition?hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja) このページは [Cloud Translation API](//cloud.google.com/translate/?hl=ja) によって翻訳されました。

*   [Google AI for Developers](https://ai.google.dev/?hl=ja)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
*   [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

この情報は役に立ちましたか？

フィードバックを送信

Android で Gemini Nano を使ってみる（デバイス上）
===================================

bookmark\_borderbookmark コレクションでコンテンツを整理 必要に応じて、コンテンツの保存と分類を行います。

*   このページの内容
*   [オンデバイス実行のメリット](#benefits-on-device)
*   [仕組み](#how-it)
*   [次のステップ](#whats-next)

Gemini モデル ファミリーの最小バージョンである Gemini Nano は、Google Pixel 8 Pro と Samsung S24 シリーズ以降の対応 Android デバイスでデバイス上で実行できます。

Android で Gemini Nano モデルを実行するには、次の処理を行う API を提供する Google AI Edge SDK for Android を使用する必要があります。

*   基盤となる Android 搭載デバイスがサポートされているかどうかを判断します。
*   Gemini Nano モデルにアクセスします。
*   安全性設定を調整する。
*   推論を高パフォーマンスで実行し、フォールバックを実装します。
*   必要に応じて、LoRA ファインチューニング ブロックを指定して、ユースケースのモデルのパフォーマンスを改善します。

Gemini Nano にアクセスするための API はテキストからテキストへのモダリティをサポートしており、今後さらに多くのモダリティが提供される予定です。

**重要:** Google AI Edge SDK for Android は、Gemini Nano を使用して革新的なアプリケーションを構築するデベロッパー向けの早期アクセス プレビュー版です。このようなアプリケーションの構築に関心をお持ちの場合は、[早期アクセス プレビューにお申し込みください](https://docs.google.com/forms/d/e/1FAIpQLSdDvg0eEzcUY_-CmtiMZLd68KD3F0usCnRzKKzWb4sAYwhFJg/viewform?usp=header_link&hl=ja)。

オンデバイス実行のメリット
-------------

オンデバイス実行により、次のことが可能になります。

*   **機密データのローカル処理**: データをローカルで処理すると、ユーザーデータのクラウドへの送信を回避できます。これは、エンドツーエンドの暗号化を使用するメッセージ アプリなど、センシティブ データを処理するアプリにとって重要です。
*   **オフライン アクセス**: インターネットに接続されていなくても AI 機能にアクセスできます。これは、オフラインや接続が不安定な状態で動作する必要があるアプリケーションに役立ちます。
*   **コスト削減**: 実行をコンシューマ ハードウェアにオフロードすることで、推論コストを削減できます。これにより、頻繁に使用されるユーザーフローを大幅に節約できます。

Gemini のデバイス上での実行には多くの利点があります。ただし、より大きな Gemini モデルを必要とするユースケースで、幅広いデバイスをサポートするには、Gemini API を使用してサーバー上の Gemini にアクセスすることをおすすめします。これは、バックエンドの統合（[Python](https://ai.google.dev/tutorials/python_quickstart?hl=ja)、[Go](https://ai.google.dev/tutorials/go_quickstart?hl=ja)、[Node.js](https://ai.google.dev/tutorials/node_quickstart?hl=ja)、または [REST](https://ai.google.dev/tutorials/rest_quickstart?hl=ja)）によって行うことも、新しい [Google AI Client SDK for Android](https://ai.google.dev/tutorials/android_quickstart?hl=ja) を介して Android アプリから直接行うこともできます。

仕組み
---

Gemini Nano のデバイス上での実行は **Android AICore** を利用しています。これは、Android 14 で導入された、デバイス上で実行するための基盤モデルへのアクセスを提供する新しいシステムレベルの機能です。基盤モデルは AICore を使用してプリインストールされているため、アプリ内でダウンロードしたり配布したりする必要はありません。LoRa を使用して、ダウンストリームのタスク用にこれらのモデルを微調整できます。Android AICore は現在、Google Pixel 8 Pro デバイスと Samsung S24 シリーズ デバイスで製品版として利用可能で、すでに Google アプリの革新的な機能を実現しています。

詳しくは、[Android AICore](https://developer.android.com/ml/aicore?hl=ja) をご覧ください。

![AICore アーキテクチャ](https://ai.google.dev/static/tutorials/images/gemini-architecture-google-ai-edge-sdk-for-android.png?hl=ja)

**図 1.** AICore アーキテクチャ

次のステップ
------

*   Android アプリで Google のサーバーで Gemini Pro 推論を利用する方法については、[Android 用 Google AI クライアント SDK のクイックスタート](https://ai.google.dev/tutorials/android_quickstart?hl=ja)をご覧ください。

この情報は役に立ちましたか？

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2024-05-14 UTC。
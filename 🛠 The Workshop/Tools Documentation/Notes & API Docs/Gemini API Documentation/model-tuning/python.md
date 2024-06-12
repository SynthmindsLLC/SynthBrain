---
Please provide me with more context! I need to know what kind of mission you're writing about to help you. 

For example, tell me: "* **What is the purpose of the mission?** Is it for a company, a project, a team, or something else?"
* **What are the goals of the mission?** What do you want to achieve?
* **Who is the target audience?** Who are you writing this mission statement for?

Once I have a better understanding of your needs, I can help you craft a compelling and effective mission statement.
---

*   このページの内容
*   [セットアップ](#setup)
    *   [認証](#authenticate)
    *   [クライアント ライブラリをインストールする](#install_the_client_library)
    *   [ライブラリをインポートする](#import_libraries)
*   [チューニング済みモデルを作成](#create_tuned_model)
    *   [チューニングの進行状況を確認する](#check_tuning_progress)
*   [モデルを評価する](#evaluate_your_model)
*   [説明を更新する](#update_the_description)
*   [モデルを削除する](#delete_the_model)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API デベロッパー コンテストにご参加ください。[詳細](https://ai.google.dev/competition?hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja) このページは [Cloud Translation API](//cloud.google.com/translate/?hl=ja) によって翻訳されました。

*   [Google AI for Developers](https://ai.google.dev/?hl=ja)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
*   [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

この情報は役に立ちましたか？

フィードバックを送信

Gemini API: Python を使用したモデルのチューニング
==================================

bookmark\_borderbookmark コレクションでコンテンツを整理 必要に応じて、コンテンツの保存と分類を行います。

*   このページの内容
*   [セットアップ](#setup)
    *   [認証](#authenticate)
    *   [クライアント ライブラリをインストールする](#install_the_client_library)
    *   [ライブラリをインポートする](#import_libraries)
*   [チューニング済みモデルを作成](#create_tuned_model)
    *   [チューニングの進行状況を確認する](#check_tuning_progress)
*   [モデルを評価する](#evaluate_your_model)
*   [説明を更新する](#update_the_description)
*   [モデルを削除する](#delete_the_model)

<table align="left" class="tfo-notebook-buttons"><tbody><tr><td><a href="https://ai.google.dev/gemini-api/docs/model-tuning/python?hl=ja" target="_blank"><img height="32" src="https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png?hl=ja" width="32">ai.google.dev で表示</a></td><td><a href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/model-tuning/python.ipynb?hl=ja" target="_blank"><img src="https://www.tensorflow.org/images/colab_logo_32px.png?hl=ja">Google Colab で実行</a></td><td><a href="https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/model-tuning/python.ipynb" target="_blank"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=ja">GitHub でソースを表示</a></td></tr></tbody></table>

このノートブックでは、Gemini API 用の Python クライアント ライブラリを使用してチューニング サービスを開始する方法を学習します。ここでは、Gemini API のテキスト生成サービスの背後にあるテキストモデルをチューニングする方法について説明します。

**注:** 現時点では、チューニングは `gemini-1.0-pro-001` モデルでのみ使用できます。

セットアップ
------

### 認証

Gemini API を使用すると、独自のデータでモデルをチューニングできます。利用者自身のデータと調整済みモデルであるため、API キーが提供できるものよりも厳密なアクセス制御が必要になります。

このチュートリアルを実行する前に、[プロジェクトに OAuth を設定](https://ai.google.dev/gemini-api/docs/oauth?hl=ja)する必要があります。

Colab で設定を行う最も簡単な方法は、`client_secret.json` ファイルのコンテンツを Colab の「シークレット マネージャー」（左側のパネルにある鍵アイコンの下）にシークレット名 `CLIENT_SECRET` でコピーすることです。

この gcloud コマンドは、`client_secret.json` ファイルを、サービスでの認証に使用できる認証情報に変換します。

> **重要:** Colab で実行する場合は、**表示されたリンクをクリックしないでください**。これでは失敗します。手順に沿って操作し、表示された `gcloud` コマンドをローカルマシンにコピーして実行し、ローカルマシンからの出力をここに貼り付けます。

    import osif 'COLAB_RELEASE_TAG' in os.environ:  from google.colab import userdata  import pathlib  pathlib.Path('client_secret.json').write_text(userdata.get('CLIENT_SECRET'))  # Use `--no-browser` in colab  !gcloud auth application-default login --no-browser --client-id-file client_secret.json --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.tuning'else:  !gcloud auth application-default login --client-id-file client_secret.json --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.tuning'

### クライアント ライブラリをインストールする

    pip install -q google-generativeai

### ライブラリをインポートする

    import google.generativeai as genai

既存のチューニング済みモデルは、`genai.list_tuned_model` メソッドで確認できます。

    for i, m in zip(range(5), genai.list_tuned_models()):  print(m.name)

tunedModels/my-model-8527
tunedModels/my-model-7092
tunedModels/my-model-2778
tunedModels/my-model-1298
tunedModels/my-model-3883

チューニング済みモデルを作成
--------------

チューニング済みモデルを作成するには、`genai.create_tuned_model` メソッドでデータセットをモデルに渡す必要があります。そのためには、呼び出しで入力値と出力値を直接定義するか、ファイルからデータフレームにインポートしてメソッドに渡します。

この例では、シーケンスの次の数値を生成するようにモデルをチューニングします。たとえば、入力が `1` の場合、モデルは `2` を出力する必要があります。入力が `one hundred` の場合、出力は `one hundred one` になります。

    base_model = [    m for m in genai.list_models()    if "createTunedModel" in m.supported_generation_methods][0]base_model

Model(name='models/gemini-1.0-pro-001',
      base\_model\_id='',
      version='001',
      display\_name='Gemini 1.0 Pro',
      description=('The best model for scaling across a wide range of tasks. This is a stable '
                   'model that supports tuning.'),
      input\_token\_limit=30720,
      output\_token\_limit=2048,
      supported\_generation\_methods=\['generateContent', 'countTokens', 'createTunedModel'\],
      temperature=0.9,
      top\_p=1.0,
      top\_k=1)

    import randomname = f'generate-num-{random.randint(0,10000)}'operation = genai.create_tuned_model(    # You can use a tuned model here too. Set `source_model="tunedModels/..."`    source_model=base_model.name,    training_data=[        {             'text_input': '1',             'output': '2',        },{             'text_input': '3',             'output': '4',        },{             'text_input': '-3',             'output': '-2',        },{             'text_input': 'twenty two',             'output': 'twenty three',        },{             'text_input': 'two hundred',             'output': 'two hundred one',        },{             'text_input': 'ninety nine',             'output': 'one hundred',        },{             'text_input': '8',             'output': '9',        },{             'text_input': '-98',             'output': '-97',        },{             'text_input': '1,000',             'output': '1,001',        },{             'text_input': '10,100,000',             'output': '10,100,001',        },{             'text_input': 'thirteen',             'output': 'fourteen',        },{             'text_input': 'eighty',             'output': 'eighty one',        },{             'text_input': 'one',             'output': 'two',        },{             'text_input': 'three',             'output': 'four',        },{             'text_input': 'seven',             'output': 'eight',        }    ],    id = name,    epoch_count = 100,    batch_size=4,    learning_rate=0.001,)

チューニング済みモデルはチューニング済みモデルのリストにすぐに追加されますが、モデルのチューニング中はステータスが「作成中」になります。

    model = genai.get_tuned_model(f'tunedModels/{name}')model

TunedModel(name='tunedModels/generate-num-2946',
           source\_model='models/gemini-1.0-pro-001',
           base\_model='models/gemini-1.0-pro-001',
           display\_name='',
           description='',
           temperature=0.9,
           top\_p=1.0,
           top\_k=1,
           state=<State.CREATING: 1>,
           create\_time=datetime.datetime(2024, 2, 21, 20, 4, 16, 448050, tzinfo=datetime.timezone.utc),
           update\_time=datetime.datetime(2024, 2, 21, 20, 4, 16, 448050, tzinfo=datetime.timezone.utc),
           tuning\_task=TuningTask(start\_time=datetime.datetime(2024, 2, 21, 20, 4, 16, 890698, tzinfo=datetime.timezone.utc),
                                  complete\_time=None,
                                  snapshots=\[\],
                                  hyperparameters=Hyperparameters(epoch\_count=100,
                                                                  batch\_size=4,
                                                                  learning\_rate=0.001)))

    model.state

<State.CREATING: 1>

### チューニングの進行状況を確認する

`metadata` を使用して状態を確認します。

    operation.metadata

total\_steps: 375
tuned\_model: "tunedModels/generate-num-2946"

`operation.result()` または `operation.wait_bar()` を使用してトレーニングが完了するまで待ちます。

    import timefor status in operation.wait_bar():  time.sleep(30)

0%|          | 0/375 \[00:00<?, ?it/s\]

チューニング ジョブは、`cancel()` メソッドを使用していつでもキャンセルできます。以下の行のコメント化を解除してコードセルを実行し、ジョブが完了する前にキャンセルします。

    # operation.cancel()

チューニングが完了すると、チューニングの結果から損失曲線を表示できます。[損失曲線](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ja#recommended_configurations)は、モデルの予測が理想的な出力からどの程度逸脱しているかを示します。

    import pandas as pdimport seaborn as snsmodel = operation.result()snapshots = pd.DataFrame(model.tuning_task.snapshots)sns.lineplot(data=snapshots, x = 'epoch', y='mean_loss')

<Axes: xlabel='epoch', ylabel='mean\_loss'>

![png](https://ai.google.dev/static/gemini-api/docs/model-tuning/python_files/output_bIiG57xWLhP7_1.png?hl=ja)

モデルを評価する
--------

`genai.generate_text` メソッドを使用して、モデルの名前を指定してモデルのパフォーマンスをテストできます。

    model = genai.GenerativeModel(model_name=f'tunedModels/{name}')

    result = model.generate_content('55')result.text

'56'

    result = model.generate_content('123455')result.text

'123456'

    result = model.generate_content('four')result.text

'five'

    result = model.generate_content('quatre') # French 4result.text                               # French 5 is "cinq"

'cinq'

    result = model.generate_content('III')    # Roman numeral 3result.text                               # Roman numeral 4 is IV

'IV'

    result = model.generate_content('七')  # Japanese 7result.text                            # Japanese 8 is 八!

'八'

例が限られているにもかかわらず、タスクに成功したように思えますが、「次」は単純な概念です。パフォーマンスを向上させる方法については、[チューニング ガイド](https://ai.google.dev/gemini-api/docs/model-tuning?hl=ja)をご覧ください。

説明を更新する
-------

チューニング済みモデルの説明は、`genai.update_tuned_model` メソッドを使用していつでも更新できます。

    genai.update_tuned_model(f'tunedModels/{name}', {"description":"This is my model."});

    model = genai.get_tuned_model(f'tunedModels/{name}')model.description

'This is my model.'

モデルを削除する
--------

チューニング済みモデルリストは、不要になったモデルを削除することでクリーンアップできます。モデルを削除するには、`genai.delete_tuned_model` メソッドを使用します。チューニング ジョブをキャンセルした場合は、パフォーマンスが予測できないため、これらのジョブを削除することをおすすめします。

    genai.delete_tuned_model(f'tunedModels/{name}')

モデルが存在しません:

    try:  m = genai.get_tuned_model(f'tunedModels/{name}')  print(m)except Exception as e:  print(f"{type(e)}: {e}")

<class 'google.api\_core.exceptions.NotFound'>: 404 Tuned model tunedModels/generate-num-2946 does not exist.

この情報は役に立ちましたか？

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2024-05-14 UTC。
---
Please provide me with the rest of the text so I can understand what your mission is.  For example, you could say: * **"Our mission is to..."** 
* **"The mission of this project is to..."**
* **"The company's mission is..."** 

Once you give me more context, I can help you complete the mission statement.
---

*   এই পৃষ্ঠায় যা যা আছে
*   [ওভারভিউ](#overview)
*   [সেটআপ](#setup)
    *   [জেনারেটিভ ল্যাঙ্গুয়েজ এপিআই আমদানি করুন](#import_the_generative_language_api)
*   [প্রমাণীকরণ](#authenticate)
    *   [পরিষেবা অ্যাকাউন্ট ব্যবহার করে OAuth সেটআপ করুন](#service-oauth)
*   [একটি কর্পাস তৈরি করুন](#create-corpus)
    *   [তৈরি করপাস পান](#get_the_created_corpus)
*   [একটি নথি তৈরি করুন](#create_a_document)
    *   [তৈরি নথি পান](#get_the_created_document)
*   [একটি ডকুমেন্ট ইনজেস্ট করুন এবং খণ্ড করুন](#ingest_chunk_a_document)
    *   [HtmlChunker এর মাধ্যমে HTML এবং খণ্ড গ্রহণ করুন](#ingest_html_and_chunk_via_htmlchunker)
*   [ব্যাচ খণ্ড তৈরি করুন](#batch_create_chunks)
    *   [Chunk তালিকাভুক্ত করুন এবং রাজ্য পান](#list_chunks_and_get_state)
*   [অন্য ডকুমেন্ট ইনজেস্ট করুন](#ingest_another_document)
*   [কর্পাস জিজ্ঞাসা](#query_the_corpus)
*   [গুণিত প্রশ্ন-উত্তর](#attributed_question-answering)
    *   [answerable\_probability এবং "আমি জানি না" সমস্যা](#answerable_probability_and_the_“i_don’t_know”_problem)
    *   [AQA সহায়ক টিপস](#aqa_helpful_tips)
    *   [আরও বিকল্প: AQA ইনলাইন প্যাসেজ ব্যবহার করে](#more_options_aqa_using_inline_passages)
*   [করপাস শেয়ার করুন](#share_the_corpus)
*   [কর্পাস মুছুন](#delete_the_corpus)
*   [সারাংশ এবং আরও পড়া](#summary_and_further_reading)
*   [পরিশিষ্ট: ব্যবহারকারীর শংসাপত্র সহ OAuth সেটআপ করুন](#user-oauth)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API বিকাশকারী প্রতিযোগিতায় যোগ দিন! [আরও জানুন](https://ai.google.dev/competition?hl=bn)

![](https://ai.google.dev/_static/images/translated.svg?hl=bn) এই পৃষ্ঠাটি [Cloud Translation API](//cloud.google.com/translate/?hl=bn) অনুবাদ করেছে।

*   [Google AI for Developers](https://ai.google.dev/?hl=bn)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
*   [ডক্স](https://ai.google.dev/gemini-api/docs?hl=bn)

এটি কাজে লেগেছে?

মতামত জানান

শব্দার্থিক পুনরুদ্ধার দিয়ে শুরু করুন
=====================================

bookmark\_borderbookmark সেভ করা পৃষ্ঠা গুছিয়ে রাখতে 'সংগ্রহ' ব্যবহার করুন আপনার পছন্দ অনুযায়ী কন্টেন্ট সেভ করুন ও সঠিক বিভাগে রাখুন।

*   এই পৃষ্ঠায় যা যা আছে
*   [ওভারভিউ](#overview)
*   [সেটআপ](#setup)
    *   [জেনারেটিভ ল্যাঙ্গুয়েজ এপিআই আমদানি করুন](#import_the_generative_language_api)
*   [প্রমাণীকরণ](#authenticate)
    *   [পরিষেবা অ্যাকাউন্ট ব্যবহার করে OAuth সেটআপ করুন](#service-oauth)
*   [একটি কর্পাস তৈরি করুন](#create-corpus)
    *   [তৈরি করপাস পান](#get_the_created_corpus)
*   [একটি নথি তৈরি করুন](#create_a_document)
    *   [তৈরি নথি পান](#get_the_created_document)
*   [একটি ডকুমেন্ট ইনজেস্ট করুন এবং খণ্ড করুন](#ingest_chunk_a_document)
    *   [HtmlChunker এর মাধ্যমে HTML এবং খণ্ড গ্রহণ করুন](#ingest_html_and_chunk_via_htmlchunker)
*   [ব্যাচ খণ্ড তৈরি করুন](#batch_create_chunks)
    *   [Chunk তালিকাভুক্ত করুন এবং রাজ্য পান](#list_chunks_and_get_state)
*   [অন্য ডকুমেন্ট ইনজেস্ট করুন](#ingest_another_document)
*   [কর্পাস জিজ্ঞাসা](#query_the_corpus)
*   [গুণিত প্রশ্ন-উত্তর](#attributed_question-answering)
    *   [answerable\_probability এবং "আমি জানি না" সমস্যা](#answerable_probability_and_the_“i_don’t_know”_problem)
    *   [AQA সহায়ক টিপস](#aqa_helpful_tips)
    *   [আরও বিকল্প: AQA ইনলাইন প্যাসেজ ব্যবহার করে](#more_options_aqa_using_inline_passages)
*   [করপাস শেয়ার করুন](#share_the_corpus)
*   [কর্পাস মুছুন](#delete_the_corpus)
*   [সারাংশ এবং আরও পড়া](#summary_and_further_reading)
*   [পরিশিষ্ট: ব্যবহারকারীর শংসাপত্র সহ OAuth সেটআপ করুন](#user-oauth)

<table class="tfo-notebook-buttons" align="left"><tbody><tr><td><a target="_blank" href="https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=bn"><img src="https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png?hl=bn" height="32" width="32"></a> ai.google.dev <a target="_blank" href="https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=bn">এ দেখুন</a></td><td><a target="_blank" href="https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/semantic_retrieval.ipynb?hl=bn"><img src="https://www.tensorflow.org/images/colab_logo_32px.png?hl=bn">Google Colab-এ চালান</a></td><td><a target="_blank" href="https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/semantic_retrieval.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=bn">GitHub-এ উৎস দেখুন</a></td></tr></tbody></table>

ওভারভিউ
-------

বড় ভাষা মডেল (LLMs) সরাসরি তাদের উপর প্রশিক্ষিত না হয়েই নতুন দক্ষতা শিখতে পারে। যাইহোক, এলএলএমগুলি "হ্যালুসিনেট" হিসাবে পরিচিত ছিল যখন তাদের প্রশিক্ষণ দেওয়া হয়নি এমন প্রশ্নের উত্তর দেওয়ার দায়িত্ব দেওয়া হয়েছিল। এটি আংশিকভাবে কারণ এলএলএমরা প্রশিক্ষণের পরে ঘটনা সম্পর্কে অবগত নয়। যে উৎস থেকে এলএলএম তাদের প্রতিক্রিয়া টেনেছে তা খুঁজে বের করাও খুব কঠিন। নির্ভরযোগ্য, পরিমাপযোগ্য অ্যাপ্লিকেশনগুলির জন্য, এটি গুরুত্বপূর্ণ যে একটি LLM এমন প্রতিক্রিয়া প্রদান করে যা সত্যের ভিত্তিতে এবং তার তথ্য উত্সগুলিকে উদ্ধৃত করতে সক্ষম।

এই সীমাবদ্ধতাগুলি কাটিয়ে উঠতে ব্যবহৃত একটি সাধারণ পদ্ধতিকে বলা হয় পুনরুদ্ধার অগমেন্টেড জেনারেশন (RAG), যা তথ্য পুনরুদ্ধার (IR) পদ্ধতির মাধ্যমে একটি বাহ্যিক জ্ঞানের ভিত্তি থেকে পুনরুদ্ধার করা প্রাসঙ্গিক ডেটা সহ একটি LLM-তে পাঠানো প্রম্পটকে বাড়িয়ে তোলে। নলেজ বেস হতে পারে আপনার নিজস্ব নথি, ডাটাবেস বা API-এর কর্পোরা।

এই নোটবুকটি আপনাকে LLM-এর প্রতিক্রিয়া উন্নত করার জন্য একটি কর্মপ্রবাহের মধ্য দিয়ে নিয়ে যায় যা বাহ্যিক টেক্সট কর্পোরার সাথে এর জ্ঞান বৃদ্ধি করে এবং জেনারেটিভ ল্যাঙ্গুয়েজ API-এর সেমান্টিক রিট্রিভার এবং অ্যাট্রিবিউটেড প্রশ্ন ও উত্তর (AQA) API ব্যবহার করে প্রশ্নের উত্তর দেওয়ার জন্য শব্দার্থিক তথ্য পুনরুদ্ধার করে।

**দ্রষ্টব্য:** এই APIটি বর্তমানে [বিটাতে](https://ai.google.dev/gemini-api/docs/api-versions?hl=bn) রয়েছে এবং [শুধুমাত্র নির্দিষ্ট অঞ্চলে উপলব্ধ](https://ai.google.dev/gemini-api/docs/available-regions?hl=bn) ৷

সেটআপ
-----

### জেনারেটিভ ল্যাঙ্গুয়েজ এপিআই আমদানি করুন

    # Install the Client library (Semantic Retriever is only supported for versions >0.4.0)

প্রমাণীকরণ
----------

Semantic Retriever API আপনাকে আপনার নিজের ডেটাতে শব্দার্থিক অনুসন্ধান করতে দেয়। যেহেতু এটি **আপনার ডেটা** , এর জন্য API কীগুলির চেয়ে কঠোর অ্যাক্সেস নিয়ন্ত্রণের প্রয়োজন৷ [পরিষেবা অ্যাকাউন্টের](#service_oauth) সাথে বা আপনার [ব্যবহারকারীর শংসাপত্রগুলির](#user_oauth) মাধ্যমে OAuth এর সাথে প্রমাণীকরণ করুন৷

এই কুইকস্টার্টটি পরীক্ষার পরিবেশের জন্য একটি সরলীকৃত প্রমাণীকরণ পদ্ধতি ব্যবহার করে এবং পরিষেবা অ্যাকাউন্ট সেটআপগুলি সাধারণত শুরু করা সহজ। একটি উত্পাদন পরিবেশের জন্য, আপনার অ্যাপের জন্য উপযুক্ত [অ্যাক্সেস শংসাপত্রগুলি](https://developers.google.com/workspace/guides/create-credentials?hl=bn#choose_the_access_credential_that_is_right_for_you) বেছে নেওয়ার আগে [প্রমাণীকরণ এবং অনুমোদন](https://developers.google.com/workspace/guides/auth-overview?hl=bn) সম্পর্কে জানুন৷

### পরিষেবা অ্যাকাউন্ট ব্যবহার করে OAuth সেটআপ করুন

পরিষেবা অ্যাকাউন্ট ব্যবহার করে OAuth সেটআপ করতে নীচের পদক্ষেপগুলি অনুসরণ করুন:

1.  [জেনারেটিভ ল্যাঙ্গুয়েজ এপিআই](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=bn) সক্ষম করুন।

![](https://ai.google.dev/tutorials/images/semantic_retriever_enable_api.png?hl=bn)

1.  [ডকুমেন্টেশন](https://developers.google.com/identity/protocols/oauth2/service-account?hl=bn#creatinganaccount) অনুসরণ করে পরিষেবা অ্যাকাউন্ট তৈরি করুন।
    
    *   পরিষেবা অ্যাকাউন্ট তৈরি করার পরে, একটি পরিষেবা অ্যাকাউন্ট কী তৈরি করুন।

![](https://ai.google.dev/tutorials/images/semantic_retriever_service_account.png?hl=bn)

1.  বাম সাইডবারে ফাইল আইকন, তারপর আপলোড আইকন ব্যবহার করে আপনার পরিষেবা অ্যাকাউন্ট ফাইল আপলোড করুন, যেমনটি নীচের স্ক্রিনশটে দেখানো হয়েছে।
    
    *   আপলোড করা ফাইলটির নাম `service_account_key.json` এ পরিবর্তন করুন বা নীচের কোডে পরিবর্তনশীল `service_account_file_name` পরিবর্তন করুন।

![](https://ai.google.dev/tutorials/images/colab_upload.png?hl=bn)

    pip install -U google-auth-oauthlib

    service_account_file_name = 'service_account_key.json'from google.oauth2 import service_accountcredentials = service_account.Credentials.from_service_account_file(service_account_file_name)scoped_credentials = credentials.with_scopes(    ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/generative-language.retriever'])

পরিষেবা অ্যাকাউন্টের শংসাপত্র ব্যবহার করে ক্লায়েন্ট লাইব্রেরি শুরু করুন।

    import google.ai.generativelanguage as glmgenerative_service_client = glm.GenerativeServiceClient(credentials=scoped_credentials)retriever_service_client = glm.RetrieverServiceClient(credentials=scoped_credentials)permission_service_client = glm.PermissionServiceClient(credentials=scoped_credentials)

একটি কর্পাস তৈরি করুন
---------------------

Semantic Retriever API আপনাকে প্রকল্প প্রতি 5টি পর্যন্ত কাস্টম টেক্সট কর্পোরা সংজ্ঞায়িত করতে দেয়। আপনার কর্পোরা সংজ্ঞায়িত করার সময় আপনি নিম্নলিখিত ক্ষেত্রগুলির যে কোনও একটি নির্দিষ্ট করতে পারেন:

*   `name` : `Corpus` রিসোর্স নাম (আইডি)। শুধুমাত্র সর্বোচ্চ 40টি বর্ণসংখ্যার অক্ষর থাকতে হবে। যদি সৃষ্টির সময় `name` খালি থাকে, তাহলে `display_name` থেকে একটি উপসর্গ এবং একটি 12 অক্ষর র্যান্ডম প্রত্যয় সহ সর্বাধিক 40 অক্ষরের দৈর্ঘ্য সহ একটি অনন্য নাম তৈরি করা হবে।
*   `display_name` : `Corpus` জন্য মানব-পাঠযোগ্য প্রদর্শন নাম। আলফানিউমেরিকস, স্পেস এবং ড্যাশ সহ সর্বাধিক 512টি অক্ষর থাকতে হবে।

    example_corpus = glm.Corpus(display_name="Google for Developers Blog")create_corpus_request = glm.CreateCorpusRequest(corpus=example_corpus)# Make the requestcreate_corpus_response = retriever_service_client.create_corpus(create_corpus_request)# Set the `corpus_resource_name` for subsequent sections.corpus_resource_name = create_corpus_response.nameprint(create_corpus_response)

name: "corpora/google-for-developers-blog-dqrtz8rs0jg"
display\_name: "Google for Developers Blog"
create\_time {
  seconds: 1713497533
  nanos: 587977000
}
update\_time {
  seconds: 1713497533
  nanos: 587977000
}

### তৈরি করপাস পান

আপনার উপরে তৈরি করা `Corpus` প্রোগ্রামেটিকভাবে অ্যাক্সেস করতে `GetCorpusRequest` পদ্ধতি ব্যবহার করুন। `name` প্যারামিটারের মানটি `Corpus` সম্পূর্ণ সংস্থান নামকে নির্দেশ করে এবং উপরের কক্ষে `corpus_resource_name` হিসাবে সেট করা হয়েছে। প্রত্যাশিত বিন্যাস হল `corpora/corpus-123` ।

    get_corpus_request = glm.GetCorpusRequest(name=corpus_resource_name)# Make the requestget_corpus_response = retriever_service_client.get_corpus(get_corpus_request)# Print the responseprint(get_corpus_response)

একটি নথি তৈরি করুন
------------------

একটি `Corpus` 10,000টি পর্যন্ত `Document` থাকতে পারে৷ আপনার নথিগুলি সংজ্ঞায়িত করার সময় আপনি নিম্নলিখিত ক্ষেত্রগুলির মধ্যে একটি নির্দিষ্ট করতে পারেন:

*   `name` : `Document` সম্পদের নাম (আইডি)। শুধুমাত্র সর্বোচ্চ 40টি অক্ষর থাকতে হবে (শুধুমাত্র বর্ণসংখ্যা বা ড্যাশ)। আইডি ড্যাশ দিয়ে শুরু বা শেষ হতে পারে না। নামটি তৈরিতে খালি থাকলে, 12টি অক্ষরের র্যান্ডম প্রত্যয় সহ `display_name` থেকে একটি অনন্য নাম প্রাপ্ত হবে।
*   `display_name` : মানুষের পাঠযোগ্য প্রদর্শন নাম। আলফানিউমেরিকস, স্পেস এবং ড্যাশ সহ সর্বাধিক 512টি অক্ষর থাকতে হবে।

`Document` 20টি পর্যন্ত ব্যবহারকারী-নির্দিষ্ট `custom_metadata` ক্ষেত্র সমর্থন করে, যা কী-মান জোড়া হিসাবে নির্দিষ্ট করা হয়েছে। কাস্টম মেটাডেটা স্ট্রিং, স্ট্রিংয়ের তালিকা বা সংখ্যাসূচক হতে পারে। মনে রাখবেন যে স্ট্রিংগুলির তালিকা সর্বাধিক 10টি মান সমর্থন করতে পারে এবং সাংখ্যিক মানগুলি এপিআই-এ ফ্লোটিং-পয়েন্ট সংখ্যা হিসাবে উপস্থাপিত হয়।

    # Create a document with a custom display name.example_document = glm.Document(display_name="Introducing Project IDX, An Experiment to Improve Full-stack, Multiplatform App Development")# Add metadata.# Metadata also supports numeric values not specified heredocument_metadata = [    glm.CustomMetadata(key="url", string_value="https://developers.googleblog.com/2023/08/introducing-project-idx-experiment-to-improve-full-stack-multiplatform-app-development.html")]example_document.custom_metadata.extend(document_metadata)# Make the request# corpus_resource_name is a variable set in the "Create a corpus" section.create_document_request = glm.CreateDocumentRequest(parent=corpus_resource_name, document=example_document)create_document_response = retriever_service_client.create_document(create_document_request)# Set the `document_resource_name` for subsequent sections.document_resource_name = create_document_response.nameprint(create_document_response)

### তৈরি নথি পান

আপনার উপরে তৈরি করা নথি প্রোগ্রামেটিকভাবে অ্যাক্সেস করতে `GetDocumentRequest` পদ্ধতি ব্যবহার করুন। `name` প্যারামিটারের মানটি নথির সম্পূর্ণ সংস্থানের নামকে নির্দেশ করে এবং উপরের ঘরে `document_resource_name` হিসাবে সেট করা হয়েছে। প্রত্যাশিত বিন্যাস হল `corpora/corpus-123/documents/document-123` ।

    get_document_request = glm.GetDocumentRequest(name=document_resource_name)# Make the request# document_resource_name is a variable set in the "Create a document" section.get_document_response = retriever_service_client.get_document(get_document_request)# Print the responseprint(get_document_response)

একটি ডকুমেন্ট ইনজেস্ট করুন এবং খণ্ড করুন
----------------------------------------

শব্দার্থক পুনরুদ্ধারের সময় ভেক্টর ডাটাবেস দ্বারা প্রত্যাবর্তিত বিষয়বস্তুর প্রাসঙ্গিকতা উন্নত করতে, নথিটি গ্রহণ করার সময় বড় নথিগুলিকে ছোট টুকরো বা **খণ্ডে** ভেঙ্গে ফেলুন।

একটি `Chunk` হল একটি `Document` একটি সাবপার্ট যা ভেক্টর প্রতিনিধিত্ব এবং স্টোরেজের উদ্দেশ্যে একটি স্বাধীন ইউনিট হিসাবে বিবেচিত হয়। একটি `Chunk` সর্বাধিক 2043 টোকেন থাকতে পারে। একটি `Corpus` সর্বোচ্চ 1 মিলিয়ন `Chunk` হতে পারে।

`Document` অনুরূপ, `Chunks` 20টি পর্যন্ত ব্যবহারকারী-নির্দিষ্ট `custom_metadata` ক্ষেত্রগুলিকে সমর্থন করে, যা কী-মান জোড়া হিসাবে নির্দিষ্ট করা হয়েছে। কাস্টম মেটাডেটা স্ট্রিং, স্ট্রিংয়ের তালিকা বা সংখ্যাসূচক হতে পারে। মনে রাখবেন যে স্ট্রিংগুলির তালিকা সর্বাধিক 10টি মান সমর্থন করতে পারে এবং সাংখ্যিক মানগুলি এপিআই-এ ফ্লোটিং-পয়েন্ট সংখ্যা হিসাবে উপস্থাপিত হয়।

এই নির্দেশিকাটি Google-এর [ওপেন সোর্স HtmlChunker](https://github.com/google/labs-prototypes/tree/main/seeds/chunker-python) ব্যবহার করে।

অন্যান্য chunkers আপনি ব্যবহার করতে পারেন [LangChain](https://python.langchain.com/docs/get_started/introduction) বা [LlamaIndex](https://www.llamaindex.ai/) অন্তর্ভুক্ত.

### HtmlChunker এর মাধ্যমে HTML এবং খণ্ড গ্রহণ করুন

    !pip install google-labs-html-chunkerfrom google_labs_html_chunker.html_chunker import HtmlChunkerfrom urllib.request import urlopen

একটি ওয়েবসাইটের জন্য HTML DOM পান। এখানে, এইচটিএমএল সরাসরি পড়া হয়, কিন্তু জাভাস্ক্রিপ্ট-ইনজেক্টেড এইচটিএমএল যেমন `document.documentElement.innerHTML` অন্তর্ভুক্ত করার জন্য HTML পোস্ট-রেন্ডারিং পেতে ভাল হবে।

    with(urlopen("https://developers.googleblog.com/2023/08/introducing-project-idx-experiment-to-improve-full-stack-multiplatform-app-development.html")) as f:  html = f.read().decode("utf-8")

পাঠ্য নথিটিকে প্যাসেজে ভেঙে দিন এবং এই প্যাসেজগুলি থেকে `Chunk` তৈরি করুন। এই ধাপটি নিজেরাই `Chunk` অবজেক্ট তৈরি করে এবং পরবর্তী বিভাগটি সেম্যান্টিক রিট্রিভার এপিআই-তে আপলোড করে।

    # Chunk the file using HtmlChunkerchunker = HtmlChunker(    max_words_per_aggregate_passage=200,    greedily_aggregate_sibling_nodes=True,    html_tags_to_exclude={"noscript", "script", "style"},)passages = chunker.chunk(html)print(passages)# Create `Chunk` entities.chunks = []for passage in passages:    chunk = glm.Chunk(data={'string_value': passage})    # Optionally, you can add metadata to a chunk    chunk.custom_metadata.append(glm.CustomMetadata(key="tags",                                                    string_list_value=glm.StringList(                                                        values=["Google For Developers", "Project IDX", "Blog", "Announcement"])))    chunk.custom_metadata.append(glm.CustomMetadata(key="chunking_strategy",                                                    string_value="greedily_aggregate_sibling_nodes"))    chunk.custom_metadata.append(glm.CustomMetadata(key = "publish_date",                                                    numeric_value = 20230808))    chunks.append(chunk)print(chunks)

ব্যাচ খণ্ড তৈরি করুন
--------------------

ব্যাচে খণ্ড তৈরি করুন। আপনি প্রতি ব্যাচ অনুরোধে সর্বাধিক 100 খণ্ড নির্দিষ্ট করতে পারেন।

একক খণ্ড তৈরির জন্য `CreateChunk()` ব্যবহার করুন।

    # Option 1: Use HtmlChunker in the section above.# `chunks` is the variable set from the section above.create_chunk_requests = []for chunk in chunks:  create_chunk_requests.append(glm.CreateChunkRequest(parent=document_resource_name, chunk=chunk))# Make the requestrequest = glm.BatchCreateChunksRequest(parent=document_resource_name, requests=create_chunk_requests)response = retriever_service_client.batch_create_chunks(request)print(response)

বিকল্পভাবে, আপনি HtmlChunker ব্যবহার না করে খণ্ড তৈরি করতে পারেন।

    # Add up to 100 CreateChunk requests per batch request.# document_resource_name is a variable set in the "Create a document" section.chunks = []chunk_1 = glm.Chunk(data={'string_value': "Chunks support user specified metadata."})chunk_1.custom_metadata.append(glm.CustomMetadata(key="section",                                                  string_value="Custom metadata filters"))chunk_2 = glm.Chunk(data={'string_value': "The maximum number of metadata supported is 20"})chunk_2.custom_metadata.append(glm.CustomMetadata(key = "num_keys",                                                  numeric_value = 20))chunks = [chunk_1, chunk_2]create_chunk_requests = []for chunk in chunks:  create_chunk_requests.append(glm.CreateChunkRequest(parent=document_resource_name, chunk=chunk))# Make the requestrequest = glm.BatchCreateChunksRequest(parent=document_resource_name, requests=create_chunk_requests)response = retriever_service_client.batch_create_chunks(request)print(response)

### `Chunk` তালিকাভুক্ত করুন এবং রাজ্য পান

[`Chunk.create_time`](https://ai.google.dev/api/python/google/ai/generativelanguage/Chunk?hl=bn#create_time) এর ক্রমবর্ধমান ক্রম অনুসারে সাজানো, প্রতি পৃষ্ঠায় সর্বাধিক 100 `Chunk` আকারের সীমা সহ সমস্ত উপলব্ধ `Chunk` একটি পৃষ্ঠাবদ্ধ তালিকা হিসাবে পেতে `ListChunksRequest` পদ্ধতিটি ব্যবহার করুন। যদি আপনি একটি সীমা নির্দিষ্ট না করেন, সর্বোচ্চ 10টি `Chunk` ফেরত দেওয়া হয়।

পরবর্তী পৃষ্ঠাটি পুনরুদ্ধার করার জন্য পরবর্তী অনুরোধের যুক্তি হিসাবে `ListChunksRequest` প্রতিক্রিয়াতে ফেরত দেওয়া `next_page_token` প্রদান করুন। মনে রাখবেন যে পেজিনেট করার সময়, `ListChunks` এ প্রদত্ত অন্যান্য সমস্ত প্যারামিটার অবশ্যই সেই কলের সাথে মিলবে যেটি পেজ টোকেন প্রদান করেছে।

সমস্ত `Chunk` একটি `state` ফিরে. একটি `Corpus` অনুসন্ধান করার আগে `Chunks` অবস্থা পরীক্ষা করতে এটি ব্যবহার করুন। `Chunk` অবস্থার মধ্যে রয়েছে - `UNSPECIFIED` , `PENDING_PROCESSING` , `ACTIVE` এবং `FAILED` ৷ আপনি শুধুমাত্র `ACTIVE` `Chunk` প্রশ্ন করতে পারেন।

    # Make the requestrequest = glm.ListChunksRequest(parent=document_resource_name)list_chunks_response = retriever_service_client.list_chunks(request)for index, chunks in enumerate(list_chunks_response.chunks):  print(f'\nChunk # {index + 1}')  print(f'Resource Name: {chunks.name}')  # Only ACTIVE chunks can be queried.  print(f'State: {glm.Chunk.State(chunks.state).name}')

অন্য ডকুমেন্ট ইনজেস্ট করুন
--------------------------

HtmlChunker এর মাধ্যমে অন্য `Document` যোগ করুন এবং ফিল্টার যোগ করুন।

    # Create a document with a custom display name.example_document = glm.Document(display_name="How it’s Made: Interacting with Gemini through multimodal prompting")# Add document metadata.# Metadata also supports numeric values not specified heredocument_metadata = [    glm.CustomMetadata(key="url", string_value="https://developers.googleblog.com/2023/12/how-its-made-gemini-multimodal-prompting.html")]example_document.custom_metadata.extend(document_metadata)# Make the CreateDocument request# corpus_resource_name is a variable set in the "Create a corpus" section.create_document_request = glm.CreateDocumentRequest(parent=corpus_resource_name, document=example_document)create_document_response = retriever_service_client.create_document(create_document_request)# Set the `document_resource_name` for subsequent sections.document_resource_name = create_document_response.nameprint(create_document_response)# Chunks - add another webpage from Google for Developerswith(urlopen("https://developers.googleblog.com/2023/12/how-its-made-gemini-multimodal-prompting.html")) as f:  html = f.read().decode("utf-8")# Chunk the file using HtmlChunkerchunker = HtmlChunker(    max_words_per_aggregate_passage=100,    greedily_aggregate_sibling_nodes=False,)passages = chunker.chunk(html)# Create `Chunk` entities.chunks = []for passage in passages:    chunk = glm.Chunk(data={'string_value': passage})    chunk.custom_metadata.append(glm.CustomMetadata(key="tags",                                                    string_list_value=glm.StringList(                                                        values=["Google For Developers", "Gemini API", "Blog", "Announcement"])))    chunk.custom_metadata.append(glm.CustomMetadata(key="chunking_strategy",                                                    string_value="no_aggregate_sibling_nodes"))    chunk.custom_metadata.append(glm.CustomMetadata(key = "publish_date",                                                    numeric_value = 20231206))    chunks.append(chunk)# Make the requestcreate_chunk_requests = []for chunk in chunks:  create_chunk_requests.append(glm.CreateChunkRequest(parent=document_resource_name, chunk=chunk))request = glm.BatchCreateChunksRequest(parent=document_resource_name, requests=create_chunk_requests)response = retriever_service_client.batch_create_chunks(request)print(response)

কর্পাস জিজ্ঞাসা
---------------

প্রাসঙ্গিক প্যাসেজ পেতে শব্দার্থক অনুসন্ধান করতে `QueryCorpusRequest` পদ্ধতি ব্যবহার করুন।

*   `results_count` : ফেরত দেওয়ার জন্য প্যাসেজের সংখ্যা উল্লেখ করুন। সর্বোচ্চ হল 100। অনির্দিষ্ট থাকলে, API সর্বোচ্চ 10টি `Chunk` প্রদান করে।
*   `metadata_filters` : `chunk_metadata` বা `document_metadata` দ্বারা ফিল্টার করুন। প্রতিটি `MetadataFilter` একটি অনন্য কী-এর সাথে সঙ্গতিপূর্ণ হতে হবে। একাধিক `MetadataFilter` অবজেক্ট লজিক্যাল `AND` s দ্বারা যুক্ত হয়। অনুরূপ মেটাডেটা ফিল্টার শর্ত লজিক্যাল `OR` s দ্বারা যোগ করা হয়. কিছু উদাহরণ:

    (year >= 2020 OR year < 2010) AND (genre = drama OR genre = action)metadata_filter = [  {    key = "document.custom_metadata.year"    conditions = [      {int_value = 2020, operation = GREATER_EQUAL},      {int_value = 2010, operation = LESS}]  },  {    key = "document.custom_metadata.genre"    conditions = [      {string_value = "drama", operation = EQUAL},      {string_value = "action", operation = EQUAL} }]  }]

মনে রাখবেন যে শুধুমাত্র সাংখ্যিক মান একই কী-এর জন্য "AND" সমর্থন করে। স্ট্রিং মান শুধুমাত্র একই কী-এর জন্য "OR" সমর্থন করে।

    ("Google for Developers" in tags) and (20230314 > publish_date)metadata_filter = [ {    key = "chunk.custom_metadata.tags"    conditions = [    {string_value = 'Google for Developers', operation = INCLUDES},  },  {    key = "chunk.custom_metadata.publish_date"    conditions = [    {numeric_value = 20230314, operation = GREATER_EQUAL}]  }]

    user_query = "What is the purpose of Project IDX?"results_count = 5# Add metadata filters for both chunk and document.chunk_metadata_filter = glm.MetadataFilter(key='chunk.custom_metadata.tags',                                           conditions=[glm.Condition(                                              string_value='Google For Developers',                                              operation=glm.Condition.Operator.INCLUDES)])# Make the request# corpus_resource_name is a variable set in the "Create a corpus" section.request = glm.QueryCorpusRequest(name=corpus_resource_name,                                 query=user_query,                                 results_count=results_count,                                 metadata_filters=[chunk_metadata_filter])query_corpus_response = retriever_service_client.query_corpus(request)print(query_corpus_response)

গুণিত প্রশ্ন-উত্তর
------------------

আপনার নথি, কর্পাস বা প্যাসেজের একটি সেটের উপর অ্যাট্রিবিউটেড প্রশ্ন-উত্তর সম্পাদন করতে [`GenerateAnswer`](https://ai.google.dev/api/python/google/ai/generativelanguage/GenerateAnswerRequest?hl=bn) পদ্ধতি ব্যবহার করুন।

অ্যাট্রিবিউটেড প্রশ্ন-উত্তর (AQA) বলতে বোঝায় একটি প্রদত্ত প্রেক্ষাপটের উপর ভিত্তি করে প্রশ্নের উত্তর দেওয়া এবং হ্যালুসিনেশন কমানোর সময় বৈশিষ্ট্য(গুলি) প্রদান করা।

`GenerateAnswer` একটি untuned LLM ব্যবহার করার জন্য বিভিন্ন সুবিধা প্রদান করে, যেখানে AQA কাঙ্খিত হয়:

*   অন্তর্নিহিত মডেলটিকে শুধুমাত্র সরবরাহকৃত প্রেক্ষাপটে ভিত্তি করে উত্তর দেওয়ার জন্য প্রশিক্ষণ দেওয়া হয়েছে।
*   এটি অ্যাট্রিবিউশন সনাক্ত করে (সরবরাহকৃত প্রেক্ষাপটের সেগমেন্ট যা উত্তরে অবদান রাখে)। অ্যাট্রিবিউশন ব্যবহারকারীকে উত্তর যাচাই করতে সক্ষম করে।
*   এটি একটি প্রদত্ত (প্রশ্ন, প্রসঙ্গ) জোড়ার জন্য `answerable_probability` অনুমান করে, যা আপনাকে আরও ক্ষমতা দেয় যে প্রত্যাবর্তিত উত্তরটি গ্রাউন্ডেড এবং সঠিক হওয়ার সম্ভাবনা কতটা নির্ভর করে তার উপর নির্ভর করে পণ্যের আচরণ পরিবর্তন করতে।

**দ্রষ্টব্য:** AQA বর্তমানে শুধুমাত্র ইংরেজিতে প্রশ্ন সমর্থন করে।

### `answerable_probability` এবং "আমি জানি না" সমস্যা

কিছু ক্ষেত্রে, প্রশ্নটির সর্বোত্তম উত্তর হল "আমি জানি না"। উদাহরণস্বরূপ, যদি প্রদত্ত প্রসঙ্গে প্রশ্নের উত্তর না থাকে, তাহলে প্রশ্নটিকে "উত্তরযোগ্য" হিসাবে বিবেচনা করা হয়।

AQA মডেল এই ধরনের ক্ষেত্রে স্বীকৃতি দিতে অত্যন্ত পারদর্শী। এটি এমনকি জবাবদিহিতা এবং উত্তরহীনতার ডিগ্রির মধ্যে পার্থক্য করতে পারে।

যাইহোক, `GenerateAnswer` API আপনার হাতে চূড়ান্ত সিদ্ধান্ত নেওয়ার ক্ষমতা রাখে:

*   _সর্বদা_ একটি গ্রাউন্ডেড উত্তর ফেরত দেওয়ার চেষ্টা করা - এমনকি যখন সেই উত্তরটি গ্রাউন্ডেড এবং সঠিক হওয়ার সম্ভাবনা কম।
*   একটি মান `answerable_probability` প্রদান করা - সম্ভাব্যতার মডেলের অনুমান যে উত্তরটি ভিত্তি এবং সঠিক।

একটি কম `answerable_probability` নিম্নলিখিত বিষয়গুলির মধ্যে 1 বা তার বেশি দ্বারা ব্যাখ্যা করা যেতে পারে:

*   মডেল আত্মবিশ্বাসী নয় যে তার উত্তর সঠিক।
*   মডেলটি আত্মবিশ্বাসী নয় যে এর উত্তর উদ্ধৃত প্যাসেজে ভিত্তি করে রয়েছে; উত্তর বিশ্ব জ্ঞানের পরিবর্তে উদ্ভূত হতে পারে। উদাহরণস্বরূপ: `question="1+1=?", passages=["2+2=4”]` → `answer=2, answerable_probability=0.02`
*   মডেলটি প্রাসঙ্গিক তথ্য প্রদান করেছে যা প্রশ্নের সম্পূর্ণ উত্তর দেয়নি। উদাহরণ: `question="Is it available in my size?, passages=["Available in sizes 5-11"]` → `answer="Yes it is available in sizes 5-11", answerable_probability=0.03"`
*   GenerateAnswerRequest এ কোন সুগঠিত প্রশ্ন জিজ্ঞাসা করা হয়নি।

যেহেতু একটি কম `answerable_probability` ইঙ্গিত করে যে GenerateAnswerResponse.answer সম্ভবত ভুল বা ভিত্তিহীন, **তাই `answerable_probability` পরিদর্শন করে প্রতিক্রিয়াটি আরও প্রক্রিয়া করার জন্য অত্যন্ত সুপারিশ করা হয়** ।

`answerable_probability` কম হলে, কিছু ক্লায়েন্ট চাইলে:

*   শেষ ব্যবহারকারীর কাছে "সেই প্রশ্নের উত্তর দিতে পারিনি" এর প্রভাবে একটি বার্তা প্রদর্শন করুন।
*   একটি সাধারণ-উদ্দেশ্য এলএলএম-এ ফিরে যান যা বিশ্ব জ্ঞান থেকে প্রশ্নের উত্তর দেয়। এই ধরনের ফলব্যাকের থ্রেশহোল্ড এবং প্রকৃতি পৃথক ব্যবহারের ক্ষেত্রে নির্ভর করবে। `answerable_probability` একটি মান <= 0.5 একটি ভাল শুরুর প্রান্তিক।

### AQA সহায়ক টিপস

সম্পূর্ণ API স্পেসিফিকেশনের জন্য, [`GenerateAnswerRequest` API রেফারেন্স](https://ai.google.dev/api/python/google/ai/generativelanguage/GenerateAnswerRequest?hl=bn) দেখুন।

*   _উত্তরণ দৈর্ঘ্য_ : প্রতি উত্তরণ 300 টোকেন পর্যন্ত সুপারিশ করা হয়।
*   _উত্তরণ বাছাই_ :
    *   আপনি যদি [`GenerateAnswerRequest.inline_passages`](https://ai.google.dev/api/python/google/ai/generativelanguage/GenerateAnswerRequest?hl=bn#inline_passages) প্রদান করেন, তাহলে প্যাসেজগুলিকে প্রশ্নের সাথে প্রাসঙ্গিকতার ক্রমানুসারে সাজানো উচিত। মডেলের প্রসঙ্গ দৈর্ঘ্য সীমা অতিক্রম করা হলে, শেষ (সর্বনিম্ন-প্রাসঙ্গিক) প্যাসেজ বাদ দেওয়া হবে।
    *   আপনি যদি [`GenerateAnswerRequest.semantic_retriever`](https://ai.google.dev/api/python/google/ai/generativelanguage/GenerateAnswerRequest?hl=bn#semantic_retriever) প্রদান করেন, তাহলে আপনার জন্য প্রাসঙ্গিকতা বাছাই স্বয়ংক্রিয়ভাবে সম্পন্ন হবে।
*   _সীমাবদ্ধতা_ : AQA মডেলটি প্রশ্ন-উত্তর দেওয়ার জন্য বিশেষায়িত। অন্যান্য ব্যবহারের ক্ষেত্রে যেমন সৃজনশীল লেখা, সারসংক্ষেপ ইত্যাদির জন্য, অনুগ্রহ করে GenerateContent-এর মাধ্যমে একটি সাধারণ-উদ্দেশ্য মডেল কল করুন।
    *   _চ্যাট_ : যদি ব্যবহারকারীর ইনপুট এমন একটি প্রশ্ন হিসাবে পরিচিত হয় যা একটি নির্দিষ্ট প্রেক্ষাপট থেকে উত্তরযোগ্য হতে পারে, তাহলে AQA চ্যাট প্রশ্নের উত্তর দিতে পারে। কিন্তু যদি ব্যবহারকারীর ইনপুট কোনো ধরনের এন্ট্রি হতে পারে, তাহলে একটি সাধারণ-উদ্দেশ্য মডেল একটি ভাল পছন্দ হতে পারে।
*   _তাপমাত্রা_ :
    *   সাধারণত, সঠিক AQA-এর জন্য তুলনামূলকভাবে কম (~0.2) তাপমাত্রা সুপারিশ করা হয়।
    *   যদি আপনার ব্যবহারের ক্ষেত্রে নির্ধারক আউটপুটের উপর নির্ভর করে, তাহলে তাপমাত্রা=0 সেট করুন।

    user_query = "What is the purpose of Project IDX?"answer_style = "ABSTRACTIVE" # Or VERBOSE, EXTRACTIVEMODEL_NAME = "models/aqa"# Make the request# corpus_resource_name is a variable set in the "Create a corpus" section.content = glm.Content(parts=[glm.Part(text=user_query)])retriever_config = glm.SemanticRetrieverConfig(source=corpus_resource_name, query=content)req = glm.GenerateAnswerRequest(model=MODEL_NAME,                                contents=[content],                                semantic_retriever=retriever_config,                                answer_style=answer_style)aqa_response = generative_service_client.generate_answer(req)print(aqa_response)

    # Get the metadata from the first attributed passages for the sourcechunk_resource_name = aqa_response.answer.grounding_attributions[0].source_id.semantic_retriever_chunk.chunkget_chunk_response = retriever_service_client.get_chunk(name=chunk_resource_name)print(get_chunk_response)

### আরও বিকল্প: AQA ইনলাইন প্যাসেজ ব্যবহার করে

বিকল্পভাবে, আপনি `inline_passages` পাস করে Semantic Retriever API ব্যবহার না করে সরাসরি AQA এন্ডপয়েন্ট ব্যবহার করতে পারেন।

    user_query = "What is AQA from Google?"user_query_content = glm.Content(parts=[glm.Part(text=user_query)])answer_style = "VERBOSE" # or ABSTRACTIVE, EXTRACTIVEMODEL_NAME = "models/aqa"# Create the grounding inline passagesgrounding_passages = glm.GroundingPassages()passage_a = glm.Content(parts=[glm.Part(text="Attributed Question and Answering (AQA) refers to answering questions grounded to a given corpus and providing citation")])grounding_passages.passages.append(glm.GroundingPassage(content=passage_a, id="001"))passage_b = glm.Content(parts=[glm.Part(text="An LLM is not designed to generate content grounded in a set of passages. Although instructing an LLM to answer questions only based on a set of passages reduces hallucination, hallucination still often occurs when LLMs generate responses unsupported by facts provided by passages")])grounding_passages.passages.append(glm.GroundingPassage(content=passage_b, id="002"))passage_c = glm.Content(parts=[glm.Part(text="Hallucination is one of the biggest problems in Large Language Models (LLM) development. Large Language Models (LLMs) could produce responses that are fictitious and incorrect, which significantly impacts the usefulness and trustworthiness of applications built with language models.")])grounding_passages.passages.append(glm.GroundingPassage(content=passage_c, id="003"))# Create the requestreq = glm.GenerateAnswerRequest(model=MODEL_NAME,                                contents=[user_query_content],                                inline_passages=grounding_passages,                                answer_style=answer_style)aqa_response = generative_service_client.generate_answer(req)print(aqa_response)

করপাস শেয়ার করুন
-----------------

আপনি [`CreatePermissionRequest`](https://ai.google.dev/api/python/google/ai/generativelanguage/CreatePermissionRequest?hl=bn) API ব্যবহার করে অন্যদের সাথে কর্পাস শেয়ার করতে পারেন।

সীমাবদ্ধতা:

*   ভাগ করার জন্য 2টি ভূমিকা রয়েছে: `READER` এবং `EDITOR` ৷
    *   একজন `READER` কর্পাস প্রশ্ন করতে পারেন।
    *   একজন `WRITER` পাঠকের অনুমতি আছে এবং অতিরিক্ত সম্পাদনা ও শেয়ার করতে পারে।
*   `EVERYONE` `user_type` পঠিত অ্যাক্সেস হিসাবে মঞ্জুর করে একটি কর্পাস সর্বজনীন হতে পারে৷

    # Replace your-email@gmail.com with the email added as a test user in the OAuth Quickstartshared_user_email = "TODO-your-email@gmail.com" #  @param {type:"string"}user_type = "USER"role = "READER"# Make the request# corpus_resource_name is a variable set in the "Create a corpus" section.request = glm.CreatePermissionRequest(    parent=corpus_resource_name,    permission=glm.Permission(grantee_type=user_type,                              email_address=shared_user_email,                              role=role))create_permission_response = permission_service_client.create_permission(request)print(create_permission_response)

কর্পাস মুছুন
------------

একটি ব্যবহারকারী কর্পাস এবং সমস্ত সংশ্লিষ্ট `Document` এবং `Chunk` মুছে ফেলতে [`DeleteCorpusRequest`](https://ai.google.dev/api/python/google/ai/generativelanguage/DeleteCorpusRequest?hl=bn) ব্যবহার করুন।

মনে রাখবেন যে অ-খালি কর্পোরা একটি `force=True` পতাকা নির্দিষ্ট না করেই একটি ত্রুটি নিক্ষেপ করবে। আপনি `force=True` সেট করলে, এই `Document` সাথে সম্পর্কিত যেকোন `Chunk` এবং বস্তুগুলিও মুছে ফেলা হবে।

যদি `force=False` (ডিফল্ট) এবং `Document` কোনো `Chunk` থাকে, তাহলে একটি `FAILED_PRECONDITION` ত্রুটি ফেরত দেওয়া হবে।

    # Set force to False if you don't want to delete non-empty corpora.req = glm.DeleteCorpusRequest(name=corpus_resource_name, force=True)delete_corpus_response = retriever_service_client.delete_corpus(req)print("Successfully deleted corpus: " + corpus_resource_name)

সারাংশ এবং আরও পড়া
-------------------

এই গাইডটি জেনারেটিভ ল্যাঙ্গুয়েজ এপিআই-এর সেমান্টিক পুনরুদ্ধার এবং অ্যাট্রিবিউটেড প্রশ্ন ও উত্তর (AQA) API-এর প্রবর্তন করেছে এবং দেখিয়েছে যে আপনি কীভাবে আপনার কাস্টম পাঠ্য ডেটাতে শব্দার্থিক তথ্য পুনরুদ্ধার করতে এটি ব্যবহার করতে পারেন। মনে রাখবেন যে এই API [LlamaIndex](https://www.llamaindex.ai/) ডেটা ফ্রেমওয়ার্কের সাথেও কাজ করে। আরও জানতে [টিউটোরিয়াল](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/managed/GoogleDemo.ipynb) পড়ুন।

এছাড়াও অন্যান্য উপলব্ধ কার্যকারিতা সম্পর্কে আরও জানতে [API ডক্স](https://ai.google.dev/api?hl=bn) দেখুন।

পরিশিষ্ট: ব্যবহারকারীর শংসাপত্র সহ OAuth সেটআপ করুন
---------------------------------------------------

OAuth প্রমাণীকরণ সেটআপ করতে [OAuth Quickstart](https://ai.google.dev/docs/oauth_quickstart?hl=bn) থেকে নীচের পদক্ষেপগুলি অনুসরণ করুন৷

1.  [OAuth সম্মতি স্ক্রিন কনফিগার করুন](https://ai.google.dev/docs/oauth_quickstart?hl=bn#configure-oauth) ।
    
2.  [একটি ডেস্কটপ অ্যাপ্লিকেশনের জন্য শংসাপত্র অনুমোদন করুন](https://ai.google.dev/docs/oauth_quickstart?hl=bn#authorize-credentials) । Colab-এ এই নোটবুকটি চালানোর জন্য, প্রথমে আপনার ক্রেডেনশিয়াল ফাইলের (সাধারণত `client_secret_*.json` ) নাম পরিবর্তন করে শুধু `client_secret.json` করুন। তারপরে বাম সাইডবারে ফাইল আইকন ব্যবহার করে ফাইলটি আপলোড করুন, তারপরে আপলোড আইকন, নীচের স্ক্রিনশটে দেখানো হয়েছে।
    

![](https://ai.google.dev/tutorials/images/colab_upload.png?hl=bn)

    # Replace TODO-your-project-name with the project used in the OAuth Quickstartproject_name = "TODO-your-project-name" #  @param {type:"string"}# Replace TODO-your-email@gmail.com with the email added as a test user in the OAuth Quickstartemail = "TODO-your-email@gmail.com" #  @param {type:"string"}# Rename the uploaded file to `client_secret.json` OR# Change the variable `client_file_name` in the code below.client_file_name = "client_secret.json"# IMPORTANT: Follow the instructions from the output - you must copy the command# to your terminal and copy the output after authentication back here.!gcloud config set project $project_name!gcloud config set account $email# NOTE: The simplified project setup in this tutorial triggers a "Google hasn't verified this app." dialog.# This is normal, click "Advanced" -> "Go to [app name] (unsafe)"!gcloud auth application-default login --no-browser --client-id-file=$client_file_name --scopes="https://www.googleapis.com/auth/generative-language.retriever,https://www.googleapis.com/auth/cloud-platform"

ক্লায়েন্ট লাইব্রেরি শুরু করুন এবং [একটি কর্পাস তৈরি করুন](#create_corpus) থেকে শুরু করে নোটবুকটি পুনরায় চালান।

    import google.ai.generativelanguage as glmgenerative_service_client = glm.GenerativeServiceClient()retriever_service_client = glm.RetrieverServiceClient()permission_service_client = glm.PermissionServiceClient()

এটি কাজে লেগেছে?

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2024-06-06 UTC-তে শেষবার আপডেট করা হয়েছে।
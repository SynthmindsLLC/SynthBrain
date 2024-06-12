---
Please provide me with more information about the mission you want to describe. 

To help me write a compelling mission statement, tell me: "* **What is the purpose of this mission?** What are you trying to achieve?"
* **Who is this mission for?** Who are you trying to help or impact?
* **What are the core values that guide this mission?** What principles are important to your work?
* **What makes this mission unique?** What sets it apart from other similar initiatives?

Once I have this information, I can craft a mission statement that is clear, concise, and inspiring.
---

*   এই পৃষ্ঠায় যা যা আছে
*   [টোকেন সম্পর্কে](#about-tokens)
*   [প্রসঙ্গ উইন্ডোজ](#context-windows)
*   [টোকেন গণনা করুন](#count-tokens)
    *   [টেক্সট টোকেন](#text-tokens)
    *   [মাল্টি-টার্ন টোকেন](#multi-turn-tokens)
    *   [মাল্টি-মডেল টোকেন](#multi-modal-tokens)
    *   [মিডিয়া টোকেন গণনা](#media-token)
    *   [সিস্টেম নির্দেশাবলী এবং সরঞ্জাম](#system-instructions)
*   [আরও পড়া](#further-reading)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API বিকাশকারী প্রতিযোগিতায় যোগ দিন! [আরও জানুন](https://ai.google.dev/competition?hl=bn)

![](https://ai.google.dev/_static/images/translated.svg?hl=bn) এই পৃষ্ঠাটি [Cloud Translation API](//cloud.google.com/translate/?hl=bn) অনুবাদ করেছে।

*   [Google AI for Developers](https://ai.google.dev/?hl=bn)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
*   [ডক্স](https://ai.google.dev/gemini-api/docs?hl=bn)

এটি কাজে লেগেছে?

মতামত জানান

টোকেন
=====

bookmark\_borderbookmark সেভ করা পৃষ্ঠা গুছিয়ে রাখতে 'সংগ্রহ' ব্যবহার করুন আপনার পছন্দ অনুযায়ী কন্টেন্ট সেভ করুন ও সঠিক বিভাগে রাখুন।

*   এই পৃষ্ঠায় যা যা আছে
*   [টোকেন সম্পর্কে](#about-tokens)
*   [প্রসঙ্গ উইন্ডোজ](#context-windows)
*   [টোকেন গণনা করুন](#count-tokens)
    *   [টেক্সট টোকেন](#text-tokens)
    *   [মাল্টি-টার্ন টোকেন](#multi-turn-tokens)
    *   [মাল্টি-মডেল টোকেন](#multi-modal-tokens)
    *   [মিডিয়া টোকেন গণনা](#media-token)
    *   [সিস্টেম নির্দেশাবলী এবং সরঞ্জাম](#system-instructions)
*   [আরও পড়া](#further-reading)

এই নির্দেশিকাটি টোকেনগুলির একটি ভূমিকা প্রদান করে এবং ব্যাখ্যা করে কিভাবে Gemini API টোকেন ব্যবহার গণনা করা যায়। একটি সম্পর্কিত Colab টিউটোরিয়ালও উপলব্ধ।

<table class="tfo-notebook-buttons" align="left"><tbody><tr><td><a target="_blank" href="https://ai.google.dev/gemini-api/docs/tokens?hl=bn"><img src="https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png?hl=bn" height="32" width="32"></a> ai.google.dev <a target="_blank" href="https://ai.google.dev/gemini-api/docs/tokens?hl=bn">এ দেখুন</a></td><td><a target="_blank" href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=bn"><img src="https://www.tensorflow.org/images/colab_logo_32px.png?hl=bn">Google Colab-এ চালান</a></td><td><a target="_blank" href="https://github.com/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png?hl=bn">GitHub-এ উৎস দেখুন</a></td></tr></tbody></table>

**দ্রষ্টব্য:** এই গাইডের উদাহরণগুলি পাইথনে লেখা আছে, তবে আপনি অন্যান্য সমস্ত Google AI SDK ব্যবহার করেও টোকেন গণনা করতে পারেন।

টোকেন সম্পর্কে
--------------

জেমিনি এবং অন্যান্য জেনারেটিভ এআই মডেলগুলি একটি গ্রানুলিটিতে ইনপুট এবং আউটপুট প্রক্রিয়া করে যা একটি শব্দের চেয়ে ছোট কিন্তু একটি একক অক্ষর বা কোড-পয়েন্টের চেয়ে বড়: একটি _টোকেন_ ।

টোকেন `z` `the` মত একক অক্ষর বা সম্পূর্ণ শব্দের মত হতে পারে। দীর্ঘ শব্দগুলিকে কয়েকটি টোকেনে বিভক্ত করা যেতে পারে। মডেল দ্বারা ব্যবহৃত সমস্ত টোকেনের সেটকে _শব্দভাণ্ডার_ বলা হয় এবং টোকেনে পাঠ্য বিভক্ত করার প্রক্রিয়াটিকে _টোকেনাইজেশন_ বলা হয়।

মিথুন মডেলের জন্য, একটি টোকেন প্রায় 4টি অক্ষরের সমতুল্য।

**গুরুত্বপূর্ণ:** 100 টোকেন প্রায় 60-80 ইংরেজি শব্দের সমান।

যখন বিলিং সক্ষম করা হয়, একটি প্রদত্ত অনুরোধের মূল্য [ইনপুট এবং আউটপুট টোকেনের সংখ্যা](https://ai.google.dev/pricing?hl=bn) দ্বারা নির্ধারিত হয়, তাই টোকেনগুলি কীভাবে গণনা করতে হয় তা জানা সহায়ক হতে পারে৷

প্রসঙ্গ উইন্ডোজ
---------------

Gemini API-এর মাধ্যমে উপলব্ধ মডেলগুলিতে প্রসঙ্গ উইন্ডো রয়েছে যা টোকেনে পরিমাপ করা হয়। প্রসঙ্গ উইন্ডোটি নির্ধারণ করে যে আপনি কতটা ইনপুট দিতে পারবেন এবং মডেলটি কতটা আউটপুট তৈরি করতে পারে। আপনি [API এর](https://ai.google.dev/api/rest/v1/models/get?hl=bn) মাধ্যমে বা [মডেল](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn) ডকুমেন্টেশনের মাধ্যমে প্রসঙ্গ উইন্ডোর আকার নির্ধারণ করতে পারেন।

নিম্নলিখিত উদাহরণে আপনি দেখতে পাচ্ছেন যে `gemini-1.0-pro-latest` মডেলটিতে 30k টোকেনের একটি ইনপুট এবং 2k টোকেনের একটি আউটপুট রয়েছে, যা 32k টোকেনের মোট প্রসঙ্গ উইন্ডো দেয়।

    model_info = genai.get_model('models/gemini-1.0-pro-latest')(model_info.input_token_limit, model_info.output_token_limit)# (30720, 2048)

আপনি `gemini-1.5-pro-latest` এর মতো একটি মডেলও ব্যবহার করতে পারেন, যার একটি 1M টোকেন প্রসঙ্গ উইন্ডো রয়েছে৷

টোকেন গণনা করুন
---------------

Gemini API একটি অনুরোধে টোকেনের সংখ্যা গণনার জন্য একটি শেষ পয়েন্ট প্রদান করে: [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=bn#count_tokens) । আপনি [`GenerativeModel.generate_content`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=bn#generate_content) এর মতো একই আর্গুমেন্ট পাস করেন এবং পরিষেবাটি সেই অনুরোধে টোকেনের সংখ্যা ফেরত দেয়।

### টেক্সট টোকেন

এখানে পাঠ্য টোকেন গণনার একটি উদাহরণ রয়েছে:

    model = genai.GenerativeModel('models/gemini-1.0-pro-latest')model.count_tokens("The quick brown fox jumps over the lazy dog.")# total_tokens: 10

আপনি যখন `GenerativeModel.generate_content` (বা `ChatSession.send_message` ) কল করেন, তখন প্রতিক্রিয়া অবজেক্টের একটি `usage_metadata` বৈশিষ্ট্য থাকে যাতে ইনপুট এবং আউটপুট টোকেন উভয়ই থাকে ( `prompt_token_count` এবং `candidates_token_count` ):

    response = model.generate_content("The quick brown fox jumps over the lazy dog.")response.text# 'This sentence is an example of a pangram, which is a sentence that contains all of the letters of the alphabet.'

    response.usage_metadata# prompt_token_count: 10# candidates_token_count: 24

### মাল্টি-টার্ন টোকেন

মাল্টি-টার্ন কথোপকথন (চ্যাট) বস্তু একইভাবে কাজ করে।

    chat = model.start_chat(history=[{'role':'user', 'parts':'Hi my name is Bob'},  {'role':'model', 'parts':'Hi Bob!'}])model.count_tokens(chat.history)# total_tokens: 10

আপনার পরবর্তী কথোপকথনের পালা কত বড় হবে তা বোঝার জন্য, আপনি যখন `count_tokens` কল করবেন তখন আপনাকে এটি ইতিহাসে যুক্ত করতে হবে।

    from google.generativeai.types.content_types import to_contentsmodel.count_tokens(chat.history + to_contents('What is the meaning of life?'))# total_tokens: 17

### মাল্টি-মডেল টোকেন

এপিআই-এর সমস্ত ইনপুট টোকেনাইজড, ছবি এবং অন্যান্য অ-টেক্সট পদ্ধতি সহ।

#### ইনলাইন বিষয়বস্তু

মিডিয়া অবজেক্টগুলি অনুরোধের সাথে API ইনলাইনে পাঠানো যেতে পারে:

    your_image = # get image ...model.count_tokens(['Tell me about this image', your_image])# total_tokens: 263

#### ফাইল API

আপনি যদি ফাইল API এর পরিবর্তে প্রম্পটের অংশগুলি আপলোড করেন তবে মডেলটি অভিন্ন টোকেনগুলি দেখতে পায়:

    your_image_upload = genai.upload_file('image.jpg')model.count_tokens(['Tell me about this image', your_image_upload])# total_tokens: 263

### মিডিয়া টোকেন গণনা

অভ্যন্তরীণভাবে, চিত্রগুলি একটি নির্দিষ্ট আকার, তাই তারা প্রদর্শনের আকার নির্বিশেষে একটি নির্দিষ্ট সংখ্যক টোকেন গ্রহণ করে।

    image1 = # get image...image2 = # get image...

    print(image1.size)print(model.count_tokens(image1))print(image2.size)print(model.count_tokens(image2))# (2048, 1362)# total_tokens: 258# (1068, 906)# total_tokens: 258

অডিও এবং ভিডিও প্রতি মিনিটে টোকেনের একটি নির্দিষ্ট হারে টোকেনে রূপান্তরিত হয়।

    audio_sample = genai.upload_file('sample.mp3')model.count_tokens(audio_sample)# total_tokens: 83552

### সিস্টেম নির্দেশাবলী এবং সরঞ্জাম

সিস্টেম নির্দেশাবলী এবং সরঞ্জামগুলিও মোটের জন্য গণনা করে, যেমন এই উদাহরণগুলিতে দেখানো হয়েছে:

    genai    .GenerativeModel()    .count_tokens("The quick brown fox jumps over the lazy dog.")# total_tokens: 10

    genai    .GenerativeModel(system_instruction='Talk like a pirate!')    .count_tokens("The quick brown fox jumps over the lazy dog.")# total_tokens: 15

    def add(a:float, b:float):    """returns a + b."""    return a+bdef subtract(a:float, b:float):    """returns a - b."""    return a-bdef multiply(a:float, b:float):    """returns a * b."""    return a*bdef divide(a:float, b:float):    """returns a / b."""    return a*bmodel = genai.GenerativeModel(model_name='gemini-1.0-pro',                              tools=[add, subtract, multiply, divide])model.count_tokens("The quick brown fox jumps over the lazy dog.")# total_tokens: 194

আরও পড়া
--------

টোকেন গণনা সম্পর্কে আরও জানতে, API রেফারেন্স দেখুন।

*   [`countTokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=bn) (বিশ্রাম)
*   [`count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=bn#count_tokens) (পাইথন)

এটি কাজে লেগেছে?

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2024-05-30 UTC-তে শেষবার আপডেট করা হয়েছে।
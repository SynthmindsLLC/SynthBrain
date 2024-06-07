*   이 페이지의 내용
*   [프롬프트란 무엇인가요?](#what-is-a-prompt)
    *   [프롬프트 콘텐츠 유형](#prompt-content-types)
*   [다음 단계](#next-steps)

/\* Styles inlined from /site-assets/css/style.css \*/ /\* Ensure that full-bleed pages get the full width. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-main-content { max-width: none; padding: 0; } /\* And ensure that any site banners/ACL warnings/etc don't get hidden on \* full-bleed pages. \*/ body\[theme="googledevai-theme"\]\[layout="full"\] .devsite-banner { margin: 0; } tab:has(> a.hidden-tab) { display: none; } .landing-page-card { padding: 16px; box-shadow: 0 0 36px rgba(0,0,0,0.1); border-radius: 10px; } /\* Page section headings \*/ .landing-page-heading h2, h2.landing-page-heading { font-family: "Google Sans", sans-serif; color: #425066; font-size: 30px; font-weight: 700; line-height: 40px; } /\* Item title headings \*/ .landing-page-heading h3, h3.landing-page-heading, .landing-page-card h3, h3.landing-page-card { font-family: "Google Sans", sans-serif; color: #425066; font-size: 20px; font-weight: 500; line-height: 26px; } /\* Notebooks \*/ devsite-code .tfo-notebook-code-cell-output { max-height: 300px; overflow: auto; background: rgba(237, 247, 255, 1); /\* blue bg to distinguish from input code cells \*/ } devsite-code .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(237, 247, 255, .7); /\* blue bg to distinguish from input code cells \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output { background: rgba(64, 78, 103, 1); /\* medium slate \*/ } devsite-code\[dark-code\] .tfo-notebook-code-cell-output + .devsite-code-buttons-container button { background: rgba(64, 78, 103, .7); /\* medium slate \*/ } /\* override default table styles for notebook buttons \*/ .devsite-table-wrapper .tfo-notebook-buttons { display: inline-block; margin-left: 3px; width: auto; } .tfo-notebook-buttons td { padding-left: 0; padding-right: 20px; } /\* on rendered notebook page, remove link to webpage since we're already here \*/ .tfo-notebook-buttons:not(.tfo-api) td:first-child { display: none; } .tfo-notebook-buttons a, .tfo-notebook-buttons :link, .tfo-notebook-buttons :visited { border-radius: 8px; box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 1px 3px 1px rgba(60, 64, 67, .15); color: #202124; padding: 12px 17px; transition: box-shadow 0.2s; } .tfo-notebook-buttons a:hover, .tfo-notebook-buttons a:focus { box-shadow: 0 1px 2px 0 rgba(60, 64, 67, .3), 0 2px 6px 2px rgba(60, 64, 67, .15); } .tfo-notebook-buttons tr { background: 0; border: 0; } .tfo-notebook-buttons td > a { -webkit-box-align: center; -ms-flex-align: center; align-items: center; display: -webkit-box; display: -ms-flexbox; display: flex; } .tfo-notebook-buttons td > a > img { margin-right: 8px; }

Gemini API 개발자 대회에 참여하세요. [자세히 알아보기](https://ai.google.dev/competition?hl=ko)

![](https://ai.google.dev/_static/images/translated.svg?hl=ko) 이 페이지는 [Cloud Translation API](//cloud.google.com/translate/?hl=ko)를 통해 번역되었습니다.

*   [Google AI for Developers](https://ai.google.dev/?hl=ko)
*   [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
*   [Docs](https://ai.google.dev/gemini-api/docs?hl=ko)

도움이 되었나요?

의견 보내기

프롬프트 설계 소개
==========

bookmark\_borderbookmark 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요.

*   이 페이지의 내용
*   [프롬프트란 무엇인가요?](#what-is-a-prompt)
    *   [프롬프트 콘텐츠 유형](#prompt-content-types)
*   [다음 단계](#next-steps)

_프롬프트 설계_는 언어 모델에서 원하는 응답을 유도하는 프롬프트를 만드는 프로세스입니다. 체계적인 메시지 작성은 언어 모델의 정확하고 고품질 응답을 보장하는 필수 부분입니다. 이 페이지에서는 프롬프트 설계를 시작하기 위한 몇 가지 기본 개념, 전략, 권장사항을 소개합니다.

프롬프트란 무엇인가요?
------------

프롬프트는 응답을 받기 위해 언어 모델에 제출되는 자연어 요청입니다. 프롬프트에는 완료하거나 계속할 모델에 대한 질문, 안내, 문맥 정보, 예시, 부분 입력이 포함될 수 있습니다. 사용되는 모델 유형에 따라 모델에서 프롬프트를 수신한 후 텍스트, 임베딩, 코드, 이미지, 동영상, 음악 등을 생성할 수 있습니다.

### 프롬프트 콘텐츠 유형

프롬프트에는 다음 유형의 콘텐츠가 하나 이상 포함될 수 있습니다.

*   [입력(필수)](#input)
*   [컨텍스트(선택사항)](#context)
*   [예(선택사항)](#examples)

#### 입력

입력은 모델에 응답을 제공하려는 프롬프트의 텍스트이며 필수 콘텐츠 유형입니다. 입력은 모델에서 답하는 질문(질문 입력), 모델에서 수행하는 태스크(태스크 입력), 모델에서 작업하는 항목(항목 입력) 또는 모델에서 완료하거나 계속하는 부분 입력(완료 입력)일 수 있습니다.

##### 질문 입력

질문 입력은 모델에서 답변을 제공하는 질문입니다.

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>프롬프트:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">What's a good name for a flower shop that specializes in selling bouquets of
dried flowers?
  </pre></devsite-code><label><strong>응답:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">1. Everlasting Blooms
2. Timeless Petals
3. Dried Flower Paradise
4. Eternal Flora
5. Vintage Floral Treasures
6. Rustic Bloom Gallery
7. Ardent Adornment
8. Potpourri Dreams
9. Dried Daisy Days
10. Forever Floral Art
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

##### 태스크 입력

태스크 입력은 모델에서 수행할 태스크입니다. 예를 들어 아이디어나 제안을 제공하도록 모델에게 지시할 수 있습니다.

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>프롬프트:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Give me a simple list of things that I must bring on a camping trip.
  </pre></devsite-code><label><strong>응답:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">1. Tent
2. Sleeping bag
3. Sleeping pad
4. Pillow
5. Lantern or flashlight
6. Headlamp
7. Camp stove
8. Fuel for camp stove
9. Cooking pot and utensils
10. Food and water
11. First aid kit
12. Sunscreen
13. Insect repellent
14. Toiletries
15. Toilet paper
16. Fire starter
17. Map
18. Compass
19. Whistle
20. Multi-tool
21. Tarpaulin
22. Rope
23. Garbage bags
24. Camera
25. Binoculars
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

##### 항목 입력

항목 입력은 분류 또는 요약과 같이 모델에서 수행하는 작업입니다. 이러한 유형의 입력은 안내를 포함함으로써 이점을 얻을 수 있습니다.

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>프롬프트:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Classify the following items as [large, small].
Elephant
Mouse
Snail
  </pre></devsite-code><label><strong>응답:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">- Elephant: Large
- Mouse: Small
- Snail: Small
  </pre></devsite-code><label style="text-align:right">(gemini-pro)</label></td></tr></tbody></table>

##### 완료 입력

완료 입력은 모델이 완료하거나 계속해야 하는 텍스트입니다.

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>프롬프트:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Some simple strategies for overcoming writer's block include
  </pre></devsite-code><label><strong>응답:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">1. **Take a Break:** Step away from your writing for a bit. Go for a walk, listen to music, or do something else that helps you relax and clear your mind. When you come back to your writing, you may find that your thoughts are more organized and your ideas are flowing more easily.

2. **Change Your Environment:** Sometimes, a change of scenery can help spark creativity. Try writing in a different location, such as a coffee shop, a library, or a park. Being in a new environment can help you see things from a different perspective and break out of your writer's block.

3. **Freewrite or Brainstorm:** Set a timer for 10-15 minutes and just write whatever comes to mind, without worrying about grammar or spelling. This can help you get started and generate new ideas. You can also try brainstorming by writing down a list of words or phrases that are related to your topic. This can help you to free associate and come up with new ideas.

4. **Read or Research:** Sometimes, the best way to overcome writer's block is to read or research your topic. Reading can help you to learn new things and get inspired. Research can help you to gather information and facts that you can use in your writing.

5. **Talk to Someone:** Talk to a friend, family member, or writing partner about what you're struggling with. Sometimes, just talking about your ideas can help you to clarify them and see them from a new perspective. You can also ask for feedback and suggestions, which can help you to move forward with your writing.

6. **Try a Different Writing Style:** If you're stuck in a rut, try experimenting with a different writing style. For example, if you're used to writing formal essays, try writing a poem or a short story. Changing your writing style can help you to break out of your comfort zone and come up with new ideas.

7. **Set a Deadline:** Sometimes, the best way to overcome writer's block is to set a deadline for yourself. This can help you to focus and motivate yourself to finish your writing. When you know that you have a deadline, you're more likely to start writing and keep going until you're finished.
  </pre></devsite-code><label style="text-align:right">(text-bison@001)</label></td></tr></tbody></table>

#### 컨텍스트

컨텍스트는 다음 중 하나일 수 있습니다.

*   모델 동작 방법을 지정하는 안내입니다.
*   모델이 응답을 생성하기 위해 사용하거나 참조하는 정보입니다.

모델에 정보를 제공해야 할 때 프롬프트에 컨텍스트 정보를 추가하거나 프롬프트 내에 있는 정보만으로 응답 경계를 제한합니다.

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>프롬프트:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Marbles:
Color: red
Number: 12
Color: blue
Number: 28
Color: yellow
Number: 15
Color: green
Number: 17

How many green marbles are there?
  </pre></devsite-code><label><strong>응답:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">There are 17 green marbles.
  </pre></devsite-code><label style="text-align:right">(text-bison@001)</label></td></tr></tbody></table>

#### 예

예시는 모델에게 이상적인 응답 예시를 제공하도록 프롬프트에 포함하는 입력-출력 쌍입니다. 프롬프트에 예시를 포함하는 것은 응답 형식을 맞춤설정하는 효과적인 전략입니다.

<table class="" style="background-color: gray"><tbody><tr><td><label><strong>프롬프트:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">Classify the following.
Options:
- red wine
- white wine

Text: Chardonnay
The answer is: white wine
Text: Cabernet
The answer is: red wine
Text: Moscato
The answer is: white wine

Text: Riesling
The answer is:
  </pre></devsite-code><label><strong>응답:</strong></label><devsite-code no-copy="" data-copy-event-label=""><pre style="white-space: pre-line; border:1px solid Black;" translate="no" dir="ltr" is-upgraded="">white wine
  </pre></devsite-code><label style="text-align:right">(text-bison@001)</label></td></tr></tbody></table>

다음 단계
-----

*   이제 프롬프트 설계를 이해했으니 [Google AI 스튜디오](http://makersuite.google.com?hl=ko)를 사용하여 직접 프롬프트를 작성해 보세요.
*   프롬프트 설계에 대한 자세한 내용은 [프롬프트 전략](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ko) 주제를 참조하세요.
*   멀티모달 프롬프팅에 관한 자세한 내용은 [미디어 파일로 메시지 표시](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=ko)를 참고하세요.

도움이 되었나요?

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2024-05-14(UTC)
---
Publish Year: 'Error: `format` can only be applied to dates. Tried for format object'
Authors: "Rongxin Liu, Carter Zenke, Charlie Liu, Andrew Holmes, Patrick Thornton, David J Malan"
URL: ""
Zotero Link: "zotero://select/library/items/VREY7QNT"
tags:
  - ""
Published:
---
# Summary
## Purpose

## Methods

## Key Findings

## Discussion

## Critiques

# Annotations
incorporate generative AI into CS50, Harvard University’s introductory course in computer science for majors and non-majors alike.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/KU5DVR2J?page=1&annotation=BRQGMFYX)



embraced generative AI and harnessed its capabilities within the classroom, while also implementing guardrails to uphold academic integrity and promote meaningful learning.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/KU5DVR2J?page=1&annotation=RCX3EDE3)



In Summer 2023 and Fall 2023, we actively tested an AI-powered chatbot, implemented as a virtual rubber duck” Yellow Highlight [Page 1](zotero://open-pdf/library/items/KU5DVR2J?page=1&annotation=JI3V8UTL)



Teaching CS50 with AI was an attempt to confront the apprehension of AI in education.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/KU5DVR2J?page=1&annotation=QJ567C36)



Researchers at Stanford University have demonstrated the use of AI in education through a meta-learning ProtoTransformer, which provided feedback on student code with a precision higher than that of teaching assistants” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KU5DVR2J?page=2&annotation=2H4KAAA9)



Reis et al. conducted a study showing that AI-generated personalized hints significantly reduced student effort in deriving correct solutions” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KU5DVR2J?page=2&annotation=QB4G3A3I)



Emerging evidence suggests a potential for AI to improve the learning feedback process, promote critical thinking, and bolster problem-solving skills” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KU5DVR2J?page=2&annotation=X3GMACUB)



CS50’s massive open online course (MOOC) – which has more than 5 million registrants as of writing – it is often the case that the only humans a student may turn to for help are other students.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KU5DVR2J?page=2&annotation=FJDWZSIK)



our goal was to approximate a 1:1 teacher-to-student ratio, providing each student with a personal subject-matter expert by using generative LLMs like OpenAI’s GPT-4” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KU5DVR2J?page=2&annotation=WE5Z28CM)



“Explain Highlighted Code” (EHC) VS Code extension to emulate behavior by human instructors, providing students with immediate explanations in plain English for code snippets.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KU5DVR2J?page=2&annotation=RN79TLH3)



host a standalone website for the CS50 Duck. This allows students to interact directly with GPT-4 in a controlled manner,” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KU5DVR2J?page=2&annotation=WHRHLR9Y)



integrated the CS50 Duck into the platform by utilizing its HTTP request feature. As shown in Figure 3, the CS50 Duck participates in threads and answers questions as needed.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KU5DVR2J?page=3&annotation=27S73RDV)



we aimed to enrich the learning experience by providing students with access to immediate, carefully generated responses. By doing so, we seek to complement human instruction, not to replace it.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KU5DVR2J?page=3&annotation=ZW2VNKT3)



all of theCS50 Duck responses subject to endorsement, amendment, or deletion by a human staff member; Ed’s own user interface provides options for each.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KU5DVR2J?page=3&annotation=8SG75LMQ)



Student queries are first relayed to CS50.ai, where any personally identifiable information (PII) is removed. Then, the queries are further processed into structured queries, known as “prompts.” These prompts are constructed with coursespecific rules and guidelines – in addition to the original student queries – in order to guide GPT-4 towards generating context-aware responses with high accuracy.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KU5DVR2J?page=3&annotation=RPQT9QN5)



For student queries coming from the Ed discussion platform, CS50.ai uses a technique called “retrieval-augmented generation” (RAG) when generating responses.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KU5DVR2J?page=3&annotation=9FD7S6IA)



Factual information is added to our prompts to ground GPT-4 in generating responses that are (more likely) accurate and contextually relevant.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KU5DVR2J?page=3&annotation=3UQ6I6JB)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/liuTeachingCS50AI/image-3-x324-y347.png]]



Requests made from CS50.ai to GPT-4 always include a system prompt, which sets the course-specific rules and guidelines, and a user prompt, which includes the actual student query that GPT-4 answers.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KU5DVR2J?page=3&annotation=K99Y3FXH)



A conversation starts with a system prompt that sets the desired context and behavior for the assistant to follow. Subsequent user prompts contain the actual queries or statements for the LLM to respond to.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=9CHV5L7V)



utilize OpenAI’s Embeddings API to create text embeddings for CS50 lecture captions, forming a ground-truth external data source.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=7JTM5JU2)



These embeddings are vector representations (i.e. numerical values) that capture semantic meaning for machine learning algorithms, allowing for more effective interpretation and utilization of data.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=V8778MXP)



data preparation process involves segmenting English captions from the course’s lectures into short, self-contained 30-second segments.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=LAS4KUMR)



we also create embeddings for each incoming student query and perform an embedding search in the vector database to retrieve lecture caption segments ranked by relevance.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=CTER9HLR)



to produce an AI-generated response, we provide GPT-4 with the student query and the top-N most relevant lecture caption segments in plain text.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=SBBGXWWW)



implemented a “guard” feature in CS50.ai that checks every student request for atypical nonalphanumeric patterns, which could indicate a potential attack.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=ZI739GYX)



If the guard is triggered, CS50.ai consults GPT-4 through an independent API call to determine whether the student request is regular input or a prompt injection attack. If an attack is confirmed, the system immediately aborts the current user session, protecting itself from misuse.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=F93ZI56E)



When a student posts a thread, the CS50 Duck on Ed performs a series of checks to verify if the thread is a question, confirm that it wasn’t posted by a staff member, and check if it falls within certain predefined categories.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=XLWJKQS5)



CS50.ai implements a throttling mechanism via visually displayed hearts, where each student starts with 10 hearts and regains one heart every three minutes.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=CAIHBVJC)



Usage throttling also holds valuable pedagogical implications for students. First, it promotes thoughtful interaction with the CS50 Duck by encouraging students to carefully consider their questions.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=86W2J52T)



usage throttling encourages reflective breaks, nudging students to step back and revisit complex problems with a refreshed and renewed perspective.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=7HW3UP4F)



Students praised our AI tools for their helpfulness, effectiveness, and reliability in guiding them through challenging problems” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KU5DVR2J?page=4&annotation=EA2WBQX7)



Mid-semester, students reported varied but significant usage” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KU5DVR2J?page=5&annotation=UD49L9DF)



Anecdotally, we also found that many students would anthropomorphize the CS50 Duck, viewing it as a friendly face. We believe this effect contributed to the success of our AI tools, as students felt comfortable chatting with a lovable duck” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KU5DVR2J?page=5&annotation=IPEXSTUW)



However, there have been a few instances where our AI tools misunderstood questions and provided incorrect advice. Occasional inaccuracies alone would be permissible – human teachers are surely susceptible to error themselves — but AI tends to exhibit a tone of complete and authoritative confidence even when wrong, while humans might qualify the certainty of their answers.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KU5DVR2J?page=5&annotation=RLAYKGKB)



CS50.ai occasionally exhibits misguided confidence when “hallucinating” incorrect information, but recent work suggests that LLMs could soon be trained to express uncertainty when appropriate” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KU5DVR2J?page=5&annotation=DW88F3AB)



The CS50 Duck posted a total of 64 answers on Ed for our summer course, out of which 25 were related to curricular matters, while the remaining 39 were related to administrative matters. From this, we determined that: • 22 out of 25 (88%) curricular answers were correct. • 30 out of 39 (77%) administrative answers were correct.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KU5DVR2J?page=5&annotation=3CSYY8FS)



Of the CS50 Duck’s 180 answers in Fall 2023, only 70 were “endorsed” by human staff, which would seem to suggest an accuracy of only 39%” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KU5DVR2J?page=5&annotation=724VDNCS)



The number of daily unique active users has significantly increased, starting at approximately 200 in June 2023, rising to 1,000 in September 2023, and reaching 1,500 by November 2023. Current daily prompt creations have followed an upward trajectory and peaked thus far at 25,000 prompts per day” Yellow Highlight [Page 6](zotero://open-pdf/library/items/KU5DVR2J?page=6&annotation=ML3FUH7H)



Even with extensive user activity in November, our costs remain reasonable at approximately $1.90 per student per month and $0.05 per prompt, which is a worthwhile investment given the positive student feedback and enhanced learning experience.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/KU5DVR2J?page=6&annotation=ZSKA9PX3)



a significant aspect of evaluating students’ work involves assessing code design, which currently relies on manual grading by human staff.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/KU5DVR2J?page=6&annotation=4267D8ZG)



hope to develop design50, an AI tool that automates design grading.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/KU5DVR2J?page=6&annotation=UPS2MBSH)



train design50 on assignments previously graded by humans, enabling it to automatically learn and apply those same standards. Human staff would then only need to review and confirm the tool’s assessments, making the grading process faster and more standardized.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/KU5DVR2J?page=6&annotation=B9SN98CV)



we built a modular configuration system that automatically updates CS50.ai’s RAG knowledge base and prompt library, allowing us to tailor our AI tools to a new curriculum and pedagogical approach specific to each course.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/KU5DVR2J?page=6&annotation=WUJ7VLSQ)




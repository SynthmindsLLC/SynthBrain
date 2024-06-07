:root { --primary: 14 14 14; --primary-light: 212 162 127; --primary-dark: 14 14 14; --background-light: 253 253 247; --background-dark: 9 9 11; --gray-50: 243 243 243; --gray-100: 238 238 238; --gray-200: 222 222 222; --gray-300: 206 206 206; --gray-400: 158 158 158; --gray-500: 112 112 112; --gray-600: 80 80 80; --gray-700: 62 62 62; --gray-800: 37 37 37; --gray-900: 23 23 23; --gray-950: 10 10 10; }@font-face { font-family: 'Styrene Display'; src: url('https://www-cdn.anthropic.com/e8f9c8ca51b03efb6315db351446fc972ab15abe/StyreneA-Medium-Web.woff2') format('woff2'); font-weight: 500; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Styrene Display'; src: url('https://www-cdn.anthropic.com/e8f9c8ca51b03efb6315db351446fc972ab15abe/StyreneA-Medium-Web.woff2') format('woff2'); font-weight: 600; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Styrene'; src: url('https://www-cdn.anthropic.com/6f87b6d99aefde021ac24f21295bf9e70f71472f/StyreneBLC-Regular.woff2') format('woff2'); font-weight: 400; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Styrene'; src: url('https://www-cdn.anthropic.com/6f87b6d99aefde021ac24f21295bf9e70f71472f/StyreneBLC-Regular.woff2') format('woff2'); font-weight: 500; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Styrene'; src: url('https://www-cdn.anthropic.com/3611e9e4aaaf466dbd47e2686f561e7de694cb6c/StyreneBLC-Medium.woff2') format('woff2'); font-weight: 600; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Tiempos'; src: url('https://www-cdn.anthropic.com/c3e09cefbfeb4e5eaca56b7bc8b9a1aa1aeda025/TiemposText-Regular.woff2') format('woff2'); font-weight: 400; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Tiempos'; src: url('https://www-cdn.anthropic.com/b198ca4e31a323b2abb84b3eeeb1eed1f471afa0/TiemposText-Medium.woff2') format('woff2'); font-weight: 500; font-style: normal; font-stretch: normal; } @font-face { font-family: 'Tiempos'; src: url('https://www-cdn.anthropic.com/b198ca4e31a323b2abb84b3eeeb1eed1f471afa0/TiemposText-Medium.woff2') format('woff2'); font-weight: 600; font-style: normal; font-stretch: normal; } body, input, #category-select, .dropdown-item, #table-of-contents { font-family: 'Styrene', sans-serif; } .eyebrow { font-family: 'Styrene Display', sans-serif; text-transform: uppercase; letter-spacing: .02rem; } #content-container { font-family: 'Tiempos', serif; } #content-container h1, #content-container h2, #content-container h3, #content-container h4, #content-container h5, #content-container h6 { font-family: 'Styrene Display', sans-serif; } #content-container p { font-size: 1rem; line-height: 1.65rem; } .font-extrabold { font-weight: 600 !important; } .wide-table { width: 100%; overflow-x: auto; } .wide-table table { width: 175%; margin-bottom: 0; } /\* Prompt Library \*/ #prompt-library-container { margin: 4rem auto; max-width: 48rem; padding-left: 1.25rem; padding-right: 1.25rem; } .prompt-library-title { font-size: 24px; text-align: center; font-weight: 700; color: #1f2937; } .dark .prompt-library-title { color: #e5e7eb; } .prompt-library-description { margin-top: 1rem; text-align: center; } .main-content { margin-bottom: 10rem; max-width: 64rem; margin-left: auto; margin-right: auto; padding-left: 1.25rem; padding-right: 1.25rem; } .prompt-controllers { display: flex; gap: 0.5rem; } .prompt-search-container { position: relative; flex: 1 1 0%; } .prompt-search-icon-container { display: flex; position: absolute; top: 0; bottom: 0; left: 0; align-items: center; padding-left: 0.75rem; } .prompt-search-icon { margin-left: 0.25rem; margin-right: 0.75rem; flex: none; width: 1rem; height: 1rem; background-color: #6b7280; mask-image: url(https://mintlify.b-cdn.net/v6.5.1/solid/magnifying-glass.svg); mask-repeat: no-repeat; mask-position: center center; } input.prompt-search-bar { display: block; height: 2.5rem; padding-left: 2.5rem; border-radius: 0.75rem; border-width: 1px; background-color: #ffffff; width: 100%; color: #111827; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); } .dark input.prompt-search-bar { color: #ffffff; background-color: rgb(var(--background-dark)); border-color: #d1d5db1a; } input.prompt-search-bar:focus { outline-color: rgb(var(--primary)); } .dark input.prompt-search-bar:focus { outline-color: rgb(var(--primary-light)); } .dark .prompt-search-icon { background-color: #ffffff80; } #category-select { padding-left: 1rem; padding-right: 2.5rem; height: 2.5rem; display: flex; align-items: center; border-radius: 0.75rem; border-width: 1px; color: #111827; background-color: #ffffff; cursor: pointer; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); white-space: nowrap; } .dark #category-select { background-color: rgb(var(--background-dark)); border-color: #d1d5db1a; color: #ffffff; } #category-select:hover { background-color: #f9fafb; } .dark #category-select:hover { background-color: #ffffff0d; } #category-select:focus { outline-color: rgb(var(--primary)); } .dark #category-select:focus { outline-color: rgb(var(--primary-light)); } #categories-dropdown { top: calc(100% + 4px); padding: 0.5rem 0.5rem; display: none; position: absolute; z-index: 10; border-radius: 0.75rem; border-width: 1px; width: 100%; color: #111827; background-color: #ffffff; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); } .dark #categories-dropdown { background-color: rgb(var(--background-dark)); border-color: #d1d5db1a; color: #ffffff; } #categories-dropdown-clickout { position: fixed; top: 0; right: 0; bottom: 0; left: 0; z-index: 0; } .dropdown-icon-container { display: flex; position: absolute; top: 0; bottom: 0; right: 0; align-items: center; padding-right: 0.25rem; } .dropdown-icon { margin-left: 0.25rem; margin-right: 0.75rem; flex: none; width: 0.75rem; height: 0.75rem; background-color: #6b7280; mask-image: url(https://mintlify.b-cdn.net/v6.5.1/solid/caret-down.svg); mask-repeat: no-repeat; mask-position: center center; } .dark .dropdown-icon { background-color: #ffffff80; } #prompts-container { grid-template-columns: repeat(1, minmax(0, 1fr)); gap: 2rem; } .dropdown-item { padding: 0.25rem 0.5rem; border-radius: 0.375rem; display: flex; align-items: center; cursor: pointer; } .dropdown-item:hover { background-color: #f9fafb; } .dark .dropdown-item:hover { background-color: #ffffff0d; } .check-icon { mask-image: url(https://mintlify.b-cdn.net/v6.5.1/solid/check.svg); height: 0.875rem; width: 1rem; background-color: rgb(var(--primary-light)); mask-repeat: no-repeat; mask-position: center center; } .prompt-card { margin: -0.75rem; padding: 0.75rem; display: flex; border-radius: 1rem; } .prompt-card:hover { background-color: #03071208; } .dark .prompt-card:hover { background-color: #ffffff08; } .prompt-icon-container { display: flex; flex: none; align-items: center; justify-content: center; margin-right: 1.5rem; border-radius: 0.75rem; height: 4rem; width: 4rem; background-color: #cb785c1a; } .prompt-icon { height: 1.5rem; width: 1.5rem; background-color: rgb(var(--primary-light)); mask-repeat: no-repeat; mask-position: center center; } .prompt-title { color: rgb(31 41 55); font-weight: 600; } .dark .prompt-title { color: rgb(229 231 235); } .prompt-description { margin-top: 0.25rem; } #prompts-container { display: grid; margin-top: 2.5rem; } @media (min-width: 640px) { #category-select { width: 16rem; } } @media (min-width: 1024px) { #prompts-container { grid-template-columns: repeat(2, minmax(0, 1fr)); } } /\* Utility classes \*/ .relative { position: relative; } .flex-1 { flex: 1 1 0%; } .prompts-container { grid-template-columns: repeat(1, minmax(0, 1fr)); gap: 2rem; } @media (min-width: 1024px) { .prompts-container { grid-template-columns: repeat(2, minmax(0, 1fr)); } } .prompts-container { grid-template-columns: repeat(1, minmax(0, 1fr)); gap: 2rem; } @media (min-width: 1024px) { .prompts-container { grid-template-columns: repeat(2, minmax(0, 1fr)); } } .prompts-container { grid-template-columns: repeat(1, minmax(0, 1fr)); gap: 2rem; } @media (min-width: 1024px) { .prompts-container { grid-template-columns: repeat(2, minmax(0, 1fr)); } }

[Anthropic home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)

English

Search...Ctrl K

*   [Talk to Claude](https://claude.ai/)
*   [Research](https://www.anthropic.com/research)
*   [News](https://www.anthropic.com/news)
*   [
    
    Talk to Claude
    
    ](https://claude.ai/)

Switch theme

Search

Navigation

Production guides

Empirical performance evaluations

[User Guides](/en/docs/intro-to-claude)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)

*   [
    
    Developer Console](https://console.anthropic.com/)
*   [
    
    Developer Discord](https://www.anthropic.com/discord)
*   [
    
    Support](https://support.anthropic.com/)

##### Get Started

*   [
    
    Welcome to Claude
    
    
    
    ](/en/docs/intro-to-claude)
*   Quickstart guide
    
*   Models overview
    
*   [
    
    Glossary
    
    
    
    ](/en/docs/glossary)

##### Capabilities

*   Text generation
    
*   [
    
    Vision
    
    
    
    ](/en/docs/vision)
*   [
    
    Embeddings
    
    
    
    ](/en/docs/embeddings)
*   [
    
    Google Sheets add-on
    
    
    
    ](/en/docs/google-sheets-add-on)
*   Tool use (function calling)
    

##### Performance enhancement

*   Prompt engineering
    
*   [
    
    Reducing latency
    
    
    
    ](/en/docs/reducing-latency)
*   Troubleshooting
    

##### Production guides

*   [
    
    Use cases and capabilities
    
    
    
    ](/en/docs/use-cases-and-capabilities)
*   [
    
    Empirical performance evaluations
    
    
    
    ](/en/docs/empirical-performance-evaluations)
*   [
    
    Content moderation
    
    
    
    ](/en/docs/content-moderation)
*   [
    
    Classification
    
    
    
    ](/en/docs/classification)

Production guides

Empirical performance evaluations
=================================

> Check out our [evals cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building%5Fevals.ipynb) to go straight to code examples.

Optimizing Claude to give you the highest possible accuracy on a task is an empirical science and a process of continuous improvement. Whether you are trying to determine if a change to your prompt has improved Claude’s performance, testing different Claude models against each other, or assessing if your use case is ready for production, a well-designed evaluation system is critical for success.

In this guide, we’ll walk you through the prompt development lifecycle, the different types of evaluations (evals) you can use, their pros and cons, and provide some guidelines as to how to choose the best eval for your use case.

* * *

[​

](#how-to-use-evals)

How to use evals
--------------------------------------------

Evals should be an integral part of your entire production lifecycle when working with LLMs. They provide a quantitative measure of performance that allows you to track progress, identify issues, and make data-driven decisions. Here’s how evals fit into the different stages of the production lifecycle:

1.  **Prompt engineering**: The [prompt engineering](/en/docs/prompt-engineering) process should begin with building a rigorous set of evals, not writing a prompt. These evals will serve as the foundation for measuring the effectiveness of your prompts and help you iterate and improve them over time.
2.  **Development**: As you develop your application or workflow with Claude, use the evals you designed during the prompt engineering phase to regularly test the performance of your prompts, even if the prompts themselves have not changed. Parts of the workflow outside and downstream of the prompt can inadvertently affect model performance. This will help you catch any issues early on and ensure that your workflows are performing as expected.
3.  **Final testing**: Before deploying your application or workflow to production, create at least one additional set of evals that you have not used during the development phase. This held-out set of evals will help you assess the true performance of your prompts and ensure that they have not been overfit to the evals used during development.
4.  **Production**: Once your application or workflow is in production, continue to use evals to monitor performance and identify any potential issues. You can also use evals to compare the performance of different Claude models or versions of your prompts to make data-driven decisions about updates and improvements.

By incorporating evals throughout the production lifecycle, you can ensure that your prompts are performing optimally and that your application or workflow is delivering the best possible results.

* * *

[​

](#parts-of-an-eval)

Parts of an eval
--------------------------------------------

Evals typically have four parts:

1.  **Input prompt**: The prompt that is fed to the model. Claude generates a completion (a.k.a. output) based on this prompt. Often, when designing evals, the input column will contain a set of variable inputs that get fed into a prompt template at test time.
2.  **Output**: The text generated by running the input prompt through the model being evaluated.
3.  **Golden answer**: The correct answer to which the model output is compared. The golden answer could be a mandatory exact match or an example of a perfect answer meant to give a grader (human or LLM) a point of comparison for scoring.
4.  **Score**: A numerical value, generated by one of the grading methods discussed below, that represents how well the model performed on the question.

* * *

[​

](#eval-grading-methods)

Eval grading methods
----------------------------------------------------

There are two aspects of evals that can be time-consuming and expensive: writing the questions & golden answer pairs, and grading. While writing questions and golden answers is typically a one-time fixed cost, grading is a cost you will incur every time you re-run your eval, which you will likely do frequently. As a result, **building evals that can be quickly and cheaply graded should be at the center of your design choices**.

There are three common ways to grade evals:

1.  **Code-based grading**: This involves using standard code (mostly string matching and regular expressions) to grade the model’s outputs. Common versions include checking for an exact match against an answer or checking that a string contains some key phrase(s). This is the best grading method if you can design an eval that allows for it, as it is fast and highly reliable. However, many evaluations do not allow for this style of grading.
2.  **Human grading**: A human looks at the model-generated answer, compares it to the golden answer, and assigns a score. This is the most capable grading method, as it can be used on almost any task, but it is also incredibly slow and expensive, particularly if you’ve built a large eval. You should mostly try to avoid designing evals that require human grading if possible.
3.  **Model-based grading**: Claude is highly capable of grading itself and can be used to grade a wide variety of tasks that might have historically required humans, such as analysis of tone in creative writing or accuracy in free-form question answering. You can do this by writing a grader prompt for Claude.

* * *

[​

](#types-of-evaluations)

Types of evaluations
----------------------------------------------------

There are several types of evaluations you can use to measure Claude’s performance on a task. Each type has its own strengths and weaknesses.

| Eval Type | Description | Pros | Cons |
| --- | --- | --- | --- |
| Multiple choice question (MCQ) | Closed-form questions with multiple answers, at least one of which is correct | \- Easy to automate- Assesses general knowledge of a topic- Clear answer key- Easy to know what accurate looks like | \- Potential training leakage if the test is public- Limited in assessing more complex or open-ended tasks |
| Exact match (EM) | Checks whether the model’s answer is exactly the same string as the correct answer | \- Easy to automate- High precision in assessing specific knowledge or tasks- Easy to know what accurate looks like | \- Limited in assessing more complex or open-ended tasks- May not capture variations in correct answers |
| String match | Checks whether the model’s answer contains the answer string | \- Easy to automate- Assesses the presence of specific information in the model’s output | \- May not capture the full context or meaning of the model’s response- Can result in false positives or negatives |
| Open answer (OA) | Open-ended questions that can have multiple possible solutions or require multi-step processes to assess | \- Great for assessing advanced knowledge, tacit knowledge, or qualitative open-ended performance- Can be graded by humans or models | \- More difficult to automate- Requires a clear rubric for grading- Model-based grading may be less accurate than human grading |

* * *

[​

](#best-practices-for-designing-evals)

Best practices for designing evals
--------------------------------------------------------------------------------

When designing evals for your specific use case, keep the following best practices in mind:

1.  **Task-specific evals**: Make your evals specific to your task whenever possible, and try to have the distribution in your eval represent the real-life distribution of questions and question difficulties.
2.  **Test model-based grading**: The only way to know if a model-based grader can do a good job grading your task is to try it out and read some samples to see if your task is a good candidate.
3.  **Automate when possible**: Often, clever design can make an eval automatable. Try to structure questions in a way that allows for automated grading while still staying true to the task. Reformatting questions into multiple choice is a common tactic.
4.  **Prioritize volume over quality**: In general, prefer higher volume and lower quality of questions over very low volume with high quality.
5.  **Use the evals cookbook**: Our [evals cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building%5Fevals.ipynb) provides implemented examples of various types of human- and model-graded evals, including guidance and code you can copy.

By following these best practices and selecting the appropriate eval type for your use case, you can effectively measure Claude’s performance and make data-driven decisions to improve your prompts and workflows.

[Use cases and capabilities](/en/docs/use-cases-and-capabilities)[Content moderation](/en/docs/content-moderation)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [How to use evals](#how-to-use-evals)
*   [Parts of an eval](#parts-of-an-eval)
*   [Eval grading methods](#eval-grading-methods)
*   [Types of evaluations](#types-of-evaluations)
*   [Best practices for designing evals](#best-practices-for-designing-evals)
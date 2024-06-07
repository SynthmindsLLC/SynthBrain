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

Classification

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

Classification
==============

Claude excels at processing, understanding, and recognizing patterns in text, images, and data. These capabilities make Claude especially powerful for classification tasks.

In this guide we will walk through the process of determining the best approach for building a classifier with Claude and the essentials of end-to-end deployment for a Claude classifier — from use case exploration to back-end integration.

> Visit our [classification cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/classification/guide.ipynb) to see example classification implementations using Claude.

[​

](#when-to-use-claude-for-classification)

When to use Claude for classification
--------------------------------------------------------------------------------------

When should you consider using an LLM instead of a traditional ML approach for your classification tasks? Here are some key indicators:

1.  **Rule-based classes**: Use Claude when classes are defined by conditions rather than examples, as it can understand underlying rules.
2.  **Evolving classes**: Claude adapts well to new or changing domains with emerging classes and shifting boundaries.
3.  **Unstructured inputs**: Claude can handle large volumes of unstructured text inputs of varying lengths.
4.  **Limited labeled examples**: With few-shot learning capabilities, Claude learns accurately from limited labeled training data.
5.  **Reasoning Requirements**: Claude excels at classification tasks requiring semantic understanding, context, and higher-level reasoning.

* * *

[​

](#common-classification-use-cases)

Common classification use cases
--------------------------------------------------------------------------

Claude is used by companies across industries for intelligent classification tasks. Below is a non exhaustive list of common classification use cases where Claude excels by industry.

1.  **Tech & IT**
    *   [Content moderation](https://docs.anthropic.com/en/docs/content-moderation): Automatically identify and flag inappropriate, offensive, or harmful content in user-generated text, images, or videos.
    *   **Bug prioritization**: Classify software bug reports based on their severity, impact, or complexity to prioritize development efforts and allocate resources effectively.
2.  **Customer service**
    *   **Intent analysis**: Determine what the user wants to achieve or what action they want the system to perform based on their text inputs.
    *   **Support ticket routing**: Analyze customer interactions, such as call center transcripts or support tickets, to route issues to the appropriate teams, prioritize critical cases, and identify recurring problems for proactive resolution.
3.  **Healthcare**:
    *   **Patient triaging**: Classify customer intake conversations and data according to the urgency, topic, or required expertise for efficient triaging.
    *   **Clinical trial screening**: Analyze patient data and medical records to identify and categorize eligible participants based on specified inclusion and exclusion criteria.
4.  **Finance**:
    *   **Fraud detection**: Identify suspicious patterns or anomalies in financial transactions, insurance claims, or user behavior to prevent and mitigate fraudulent activities.
    *   **Credit risk assessment**: Classify loan applicants based on their creditworthiness into risk categories to automate credit decisions and optimize lending processes.
5.  **Legal**:
    *   **Legal document categorization**: Classify legal documents, such as pleadings, motions, briefs, or memoranda, based on their document type, purpose, or relevance to specific cases or clients.

* * *

[​

](#using-claude-for-classification)

Using Claude for classification
--------------------------------------------------------------------------

When deciding which Claude model to use, it is important to determine the intelligence, latency, and price requirements for your use case up front.

> [Learn more about how Opus, Sonnet, and Haiku compare](https://docs.anthropic.com/en/docs/models-overview#model-comparison) For classification, a smaller model like Claude 3 Haiku is typically ideal due to its speed and efficiency. For classification tasks where specialized knowledge or complex reasoning is required, Sonnet may be a better choice. Evaluations are a good way to gauge whether a Claude model is performing well enough on its classification task to launch into production. See our page [empirical performance evaluations](https://docs.anthropic.com/en/docs/empirical-performance-evaluations) for an overview of the evaluation process. For guidance on how to use Claude to automate the evaluation process, check out the [automated evaluations](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb) section of the Anthropic Cookbook.

### 

[​

](#1-build-a-strong-prompt)

1\. Build a strong prompt

While Claude offers high-level baseline performance out of the box, a strong input prompt helps get the best results. We provide a wide range of prompts to get you started in our prompt library, including prompts for a number of classification use cases, including:

*   [Sentiment analysis](https://docs.anthropic.com/en/prompt-library/tweet-tone-detector): Detect the tone and sentiment behind tweets.
*   [Content moderation](https://docs.anthropic.com/en/prompt-library/master-moderator): Evaluate user inputs for potential harmful or illegal content.
*   [Customer review classification](https://docs.anthropic.com/en/prompt-library/review-classifier): Categorize feedback into pre-specified tags and categorizations.

For a generic classifier that you can adapt to your specific use case, copy the starter prompt below into our developer Console

| ROLE | CONTENT |
| --- | --- |
| User | You will be building a text classifier that can automatically categorize text into a set of predefined categories.  
  
Here are the categories the classifier will use:  
<categories>  
{{CATEGORIES}}  
</categories>  
  
To help you understand how to classify text into these categories, here are some example texts that have already been labeled with their correct category:  
<examples>  
{{EXAMPLES}}  
</examples>  
  
Carefully study these examples to identify the key features and characteristics that define each category. Write out your analysis of each category inside <category\_analysis> tags, explaining the main topics, themes, writing styles, etc. that seem to be associated with each one.  
  
Once you feel you have a good grasp of the categories, your task is to take in new, unlabeled texts and output a prediction of which category it most likely belongs to.  
  
Before giving your final classification, show your step-by-step process and reasoning inside <classification\_process> tags. Weigh the evidence for each potential category. Then output your final <classification> for which category you think the example text belongs to.  
  
The goal is toaccurately categorize new texts into the most appropriate category, as defined by the examples. |

Our [prompt generator](https://docs.anthropic.com/en/docs/prompt-generator) and [prompt engineering guide](https://docs.anthropic.com/en/docs/prompt-engineering) can also help you craft the most effective prompts to optimize Claude 3’s output.

### 

[​

](#2-develop-your-test-cases)

2\. Develop your test cases

To run your classification evaluation, you will need test cases to run it on. We recommend gathering a wide range of realistic data that cover all of your predefined categories. Don’t forget to add in edge cases to test the guardrails!

Manually building test cases can be quite time consuming if you don’t have a dataset already available. Many customers use Claude to generate example test data. However, “golden answer” labels are best when manually generated, so as to limit model bias and establish a firm ground truth.

### 

[​

](#3-run-your-eval)

3\. Run your eval

You can run an evaluation via a script as is shown in our [classification cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/classification/guide.ipynb). AWS Bedrock also provides a [platform for model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html).

#### 

[​

](#evaluation-metrics)

Evaluation metrics

Some success metrics to consider when evaluating Claude’s classification performance include:

| Criteria | Description |
| --- | --- |
| Accuracy | The model’s output exactly matches the golden answer or correctly classifies the input according to the task’s requirements. This is typically calculated as (Number of correct predictions) / (Overall number of predictions). |
| F1 Score | The models output optimally balances precision and recall. |
| Consistency | The model’s output is consistent with its predictions for similar inputs or follows a logical pattern. |
| Structure | The model’s output follows the expected format or structure, making it easy to parse and interpret. For example, many classifiers are expected to output JSON format. |
| Speed | The model provides a response within the acceptable time limit or latency threshold for the task. |
| Bias and Fairness | If classifying data about people, is it important that the model does not demonstrate any biases based on gender, ethnicity, or other characteristics that would lead to its misclassification. |

* * *

[​

](#deploy-your-solution)

Deploy your solution
----------------------------------------------------

To see code examples of how to use Claude for classification, check out our [classification cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/classification/guide.ipynb) which contains a Jupyter notebook with ready-made code demonstrating how to use and evaluate Claude for classification scenarios.

[Content moderation](/en/docs/content-moderation)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

*   [When to use Claude for classification](#when-to-use-claude-for-classification)
*   [Common classification use cases](#common-classification-use-cases)
*   [Using Claude for classification](#using-claude-for-classification)
*   [1\. Build a strong prompt](#1-build-a-strong-prompt)
*   [2\. Develop your test cases](#2-develop-your-test-cases)
*   [3\. Run your eval](#3-run-your-eval)
*   [Evaluation metrics](#evaluation-metrics)
*   [Deploy your solution](#deploy-your-solution)
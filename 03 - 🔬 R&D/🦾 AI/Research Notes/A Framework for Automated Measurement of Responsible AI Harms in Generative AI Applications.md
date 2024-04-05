---
Publish Year: "2023"
Authors: Ahmed Magooda, Alec Helyar, Kyle Jackson, David Sullivan, Chad Atalla, Emily Sheng, Dan Vann, Richard Edgar, Hamid Palangi, Roman Lutz, Hongliang Kong, Vincent Yun, Eslam Kamal, Federico Zarfati, Hanna Wallach, Sarah Bird, Mei Chen
URL: http://arxiv.org/abs/2310.17750
Zotero Link: zotero://select/library/items/RUCZ9BJK
tags:
  - "#Computer-Science---Computation-and-Language"
Published: 2024-01-30
---
# Summary
## Purpose 
The paper presents a framework for automated measurement of responsible AI (RAI) metrics in large language models (LLMs), focusing on identifying and evaluating potential harms caused by these models.

## Methods 
- **Data Generation**: Using templates and parameters to simulate user-AI interactions in various scenarios, mimicking real-world use of LLMs.
- **Evaluation**: Applying annotation guidelines to assess LLM-generated content for potential harms, both quantitatively and qualitatively.

## Key Findings 
1. **Automated Harm Measurement**: The framework allows for automated, scalable harm measurement in LLMs.
2. **Use of GPT-4**: The utilization of GPT-4 for evaluating other LLMs in terms of harm generation.
3. **Experimental Design Efficacy**: The framework's efficacy demonstrated through experiments evaluating different LLMs for potential harm generation.
4. **Comparison of Models**: Insights into the relative performance of different LLMs regarding responsible AI principles.

## Discussion 
This research is pivotal in advancing the responsible use of LLMs. It addresses the need for scalable and automated methods to measure potential harms, which is essential given the rapid development and deployment of these models.

## Critiques 
1. **LLM-based Evaluation Risks**: The inherent risks in using LLMs for evaluating other LLMs, especially considering their propensity to generate harmful content.
2. **Data Generation Validity**: Concerns about the ecological validity of the data generated through simulated user interactions.
3. **Measurement Resource Development**: The challenges in developing reliable and valid measurement resources for assessing harms.

## Tags
#ResponsibleAI #LargeLanguageModels #AutomatedMeasurement #AIHarms #AIAlignment #GPT4 #AIethics #EvaluationFramework


# Annotations
as the availability and capabilities of LLMs grow, it is increasingly necessary to develop automated frameworks for measuring harms with a speed and scale that can match the pace of the technology’s proliferation.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/5R4IRSNA?page=1&annotation=XF8NGPPV)



we propose and implement a framework that harnesses the capabilities of LLMs to test other LLMs and assess their potential for causing harm.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/5R4IRSNA?page=1&annotation=APEZE7E3)



The core of our proposed framework comprises of two key components: (1) data generation from templates and (2) evaluation of generated outputs.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/5R4IRSNA?page=1&annotation=9XMATBAR)



we introduce an evaluation component that uses GPT-4 to assess LLM-generated content according to harm definitions. This component evaluates AI-generated content and produces both quantitative and qualitative outputs, yielding numerical annotations of harm severity and written snippets about annotation reasoning.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/5R4IRSNA?page=1&annotation=MYQUFE93)



The data generation component uses templates and parameters to simulate interactions with the LLM under test to generate data which approximates a user-AI interaction in some product or service. The templates and parameters are separately created by domain experts for each harm to ensure the reliability and validity of the resulting measurements.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/5R4IRSNA?page=1&annotation=6Q55HC2D)



the evaluation component produces annotations of the LLM’s output on the generated data by applying annotation guidelines. The annotation guidelines are provided by domain experts based on the harm definitions they create.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/5R4IRSNA?page=1&annotation=U799A7EU)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/magoodaFrameworkAutomatedMeasurement2023/image-2-x46-y564.png]]



The annotation process uses an LLM by providing it with annotation guidelines which are manually crafted by domain experts and include harm definitions, examples, and a defect definition. The defect definition specifies criteria for determining whether a data sample is considered desirable or allowable in the context of the LLM under test and any product or service it is embedded in.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/5R4IRSNA?page=2&annotation=VZY2UFSQ)



Automated annotation consists of multiple steps: the first step uses the annotation guidelines to annotate each sample. These annotations are initially created in text, where the LLM follows an annotation schema specified by few-shot examples in the annotation guidelines. The next step parses the annotation to extract expected metrics (e.g., defect score, reasoning, etc) according to the provided guidelines. The final step involves aggregating the extracted values and calculating a metric (e.g., defect rate.).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/5R4IRSNA?page=2&annotation=L6HINZJ3)



Ultimately, a defect rate is calculated, which represents the proportion of samples which were annotated as matching the defect definition. For example, one way defect definitions may work is through severity thresholds. Consider the case where we may wish to evaluate whether the LLM under test produces extreme violent content. The domain experts may build a severity scale (e.g., on an 1-10 scale where lower is less severe) for violent content, and a defect definition could be a threshold within this severity range or a particular severity scale (e.g., any sample with severity ≥ 7 is a defect).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/5R4IRSNA?page=2&annotation=DMMILGDC)



In other words, a 0% defect rate does not mean that there is zero chance of the measured harm occurring in the real world. Instead, a 0% defect rate may be interpreted to mean that the AI system under test did not appear to fail any tests in the current measurement set.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/5R4IRSNA?page=3&annotation=YEKGP5FE)



Notably, the generation of violent and hateful content is more prevalent compared to sexual content.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/5R4IRSNA?page=4&annotation=F8M2XYBI)



Of the different IP categories, songs exhibit the highest leakage rates, followed by books and news.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/5R4IRSNA?page=4&annotation=4XZ9CGLT)



Regarding jailbreak evaluations, Models 2 and 3 exhibit comparable defect rates, with leaking guidelines being the most successful attack vector compared to generating adult content or promoting illegal activities.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/5R4IRSNA?page=4&annotation=9PWX8A5R)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/magoodaFrameworkAutomatedMeasurement2023/image-5-x68-y617.png]]




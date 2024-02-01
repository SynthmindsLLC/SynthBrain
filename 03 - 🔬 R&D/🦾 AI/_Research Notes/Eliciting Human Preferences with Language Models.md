---
Publish Year: "2023"
Authors: Belinda Z. Li, Alex Tamkin, Noah Goodman, Jacob Andreas
URL: http://arxiv.org/abs/2310.11589
Zotero Link: zotero://select/library/items/ZC345Q6B
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#Computer-Science---Machine-Learning"
Published: 2024-04-23
---
# Summary
## Purpose 
The paper "Eliciting Human Preferences with Language Models" by Li et al. (2023) aims to address the challenge of encoding complex human preferences into machine learning systems. It introduces a novel framework called Generative Active Task Elicitation (GATE), which utilizes language models to interactively elicit and infer user preferences through language-based interaction.

## Methods 
- Developing the GATE framework for interactive task specification.
- Implementing various techniques like generative active learning, generating yes-or-no questions, and open-ended questions using language models.
- Conducting experiments across three domains: email validation, content recommendation, and moral reasoning.
- Comparing GATE with traditional methods like supervised learning and user-written prompts.
- Evaluating the effectiveness of GATE through user agreement and mental effort metrics.

## Key Findings 
1. GATE outperforms traditional methods in aligning models with complex human preferences.
2. Interactive elicitation methods are generally less mentally demanding than non-interactive prompting.
3. GATE improves over no elicitation in all domains, especially in content recommendation and email verification.
4. The flexibility of GATE allows for a broader range of user preference elicitation.
5. Generative yes/no questions within GATE are particularly effective across all settings.

## Discussion 
This research is significant in the field of AI and machine learning, particularly in the context of [[personalization]] and [[human-AI interaction]]. By leveraging language models for interactive elicitation, GATE represents a step forward in aligning AI systems more closely with individual human preferences and values, a key aspect of [[AI alignment]]. 

## Critiques 
1. The potential for automation bias in GATE, where users might overly rely on model predictions.
2. The study’s reliance on self-reported measures of mental effort, which can be subjective.
3. The possible lack of generalizability of findings beyond the specific domains tested.
4. The need for further exploration in more complex real-world tasks.
5. The absence of a direct comparison with other advanced language models besides GPT-4.

## Tags
#GATE #AIalignment #humanAIinteraction #personalization #languageModels


# Annotations
Until recently, the dominant approach in machine learning has specified preferences using examples: users first label a dataset with examples of the desired model behavior, then train a machine learning model on this dataset.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/SHJ2CCAA?page=1&annotation=YWZGIGXZ)



In more recent years, this paradigm has changed with the advent of instruction following methods (Brown et al., 2020a): by pre-training langauge models (LMs) on large-scale text corpora, it is possible to induce desired behaviors by conditioning only on natural language task specifications, in tasks as diverse as code generation and text summarization.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/SHJ2CCAA?page=1&annotation=UZLMT7BP)



complex behaviors require an increasing amount of prompt engineering or dataset design to overcome the imprecision of natural language and prevent models from misunderstanding or misgeneralizing from spurious features of prompts or examples” Yellow Highlight [Page 1](zotero://open-pdf/library/items/SHJ2CCAA?page=1&annotation=573WUL6H)



These challenges of task ambiguity (Finn et al., 2018; Tamkin et al., 2022a) loom large as models continue to be applied to more open-ended tasks and higher-stakes domains.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/SHJ2CCAA?page=1&annotation=Q64CD9UQ)



![[image-2-x59-y39.png]]



To address these challenges, we propose to use models themselves to help convert human preferences into automated decision-making systems.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/SHJ2CCAA?page=3&annotation=IVDAXNR9)



generative active task elicitation (GATE), a learning framework in which models elicit and infer user preferences through open-ended interaction.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/SHJ2CCAA?page=3&annotation=RFTWM5I3)



In pre-registered experiments, we find that LM-based task elicitation often yields more accurate models than existing prompting or active learning techniques while requiring comparable (or less) mental effort from users and surfacing novel considerations.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/SHJ2CCAA?page=3&annotation=8AJCZSRQ)



![[image-4-x77-y573.png]]



In interactive elicitation methods, queries can change depending on user responses (e.g., querying for the most useful information based on what is known thus far) while passive elicitation methods expect the user to provide specifications in a single shot.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/SHJ2CCAA?page=4&annotation=E6AWZP4D)



In active learning, the elicitation policy is interactive. Users first assemble a fixed pool of unlabeled inputs x. Next, E, selects from this pool an example whose label would be most informative. The user Hf provides a label for this example, then E selects the next-most-informative example, and so on (Cohn et al., 1994; Dagan & Engelson, 1995; Lewis & Gale, 1994; Settles, 2009)” Yellow Highlight [Page 4](zotero://open-pdf/library/items/SHJ2CCAA?page=4&annotation=V3R8H6Y6)



Modern pre-trained models allow for specifying tasks in more flexible ways than simply labeling examples. For example, models can be conditioned with a prompt describing the user’s intended task in natural language (Brown et al., 2020b)” Yellow Highlight [Page 4](zotero://open-pdf/library/items/SHJ2CCAA?page=4&annotation=252B5WNZ)



All of the methods above have important drawbacks: the burden typically falls upon the user to ensure that prompts or example sets are truly comprehensive specifications of the task, as any lack of clarity in the prompt could lead to task ambiguity” Yellow Highlight [Page 4](zotero://open-pdf/library/items/SHJ2CCAA?page=4&annotation=9PCHPXK8)



Resolving task ambiguity by crafting better prompts is challenging and time-consuming due to the difficulties of articulating nebulous personal preferences and anticipating edge cases that will emerge during deployment time.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/SHJ2CCAA?page=4&annotation=RLWXMEJE)



We explore whether it is possible to combine the flexibility and richness of prompting-based specifications with the advantages of interactive methods such as active learning, by having a model interactively query users for these rich specifications.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/SHJ2CCAA?page=4&annotation=7A4I9I83)



Generating yes-or-no questions We restrict the LM to generating binary yes-or-no questions.  This approach enables the model to elicit more abstract preferences while still being easy for the user to answer.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/SHJ2CCAA?page=5&annotation=45RDI865)



We use the GPT-4 model (gpt-4-0613 snapshot) (OpenAI, 2023) to both elicit user preferences (the elicitation policy E) and make predictions based on the elicited preferences (the predictor ˆf(s)). To elicit user preferences, we prompt GPT-4 with a domain description and the current interaction history, and ask it to generate an informative but easy-to-answer edge case (for generative active learning) or question (for generative yes-or-no questions and generative open-ended questions). To make predictions, we prompt GPT-4 with the task specification s and a test sample x and ask it to generate a prediction for the test sample.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/SHJ2CCAA?page=6&annotation=35KJI9VJ)



Overall, GATE improves over no elicitation, where the model is prompted to make decisions before any user interaction. This is the case across all domains studied (a positive score in Figure 3), with significance at the 0.05 level for all but the email domain, where only generative active learning was significant.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/SHJ2CCAA?page=7&annotation=5PSW9FX8)



GATE elicitation methods improve over user-written prompts.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/SHJ2CCAA?page=7&annotation=WWDWZELR)



generative yes/no questions improve over user-written prompts in every setting studied (although we lack enough power to assess significance in the moral reasoning domain).” Yellow Highlight [Page 7](zotero://open-pdf/library/items/SHJ2CCAA?page=7&annotation=YMM2JR5K)



![[image-8-x85-y485.png]]



past work has studied auto-induced distributional shift, where machine learning models shift human behavior to be easier to predict (Krueger et al., 2020)” Yellow Highlight [Page 8](zotero://open-pdf/library/items/SHJ2CCAA?page=8&annotation=I5Y8JIME)



![[image-9-x104-y575.png]]



A fundamental challenge across many fields is how to obtain information about people’s nebulous thoughts, preferences, and goals. In psychology and cognitive science, protocol analysis describes methods for how to obtaining and analyze verbal reports from subjects about cognitive processes including via think-aloud protocols” Yellow Highlight [Page 9](zotero://open-pdf/library/items/SHJ2CCAA?page=9&annotation=WM8R8R2B)



![[image-10-x64-y75.png]]



Perhaps most relevant to our work is active learning, a major subfield of machine learning that centers on how models can choose useful data points to learn from. Active learning has traditionally focused on pool-based methods, which choose points to label from a fixed reservoir” Yellow Highlight [Page 11](zotero://open-pdf/library/items/SHJ2CCAA?page=11&annotation=SNQNHF2D)



Recently, Tamkin et al. (2022b) found that the well-calibrated uncertainty scores of pretrained models can be used during active learning to clarify the user’s task preferences—for instance, by choosing examples that distinguish which of two correlated features are important for the task. We extend this line of investigation to the generative setting, clarifying user intent by querying a user with generated examples and questions.” Yellow Highlight [Page 11](zotero://open-pdf/library/items/SHJ2CCAA?page=11&annotation=2SVURU2V)



work on thin slicing (Ambady & Rosenthal, 1992) has demonstrated that small amounts of information about a user can sometimes be used to predict a broader range of personal characteristics, raising potential privacy considerations” Yellow Highlight [Page 12](zotero://open-pdf/library/items/SHJ2CCAA?page=12&annotation=67VP4EPL)



GATE also risks increasing automation bias (Goddard et al., 2012), where users place undue weight on a model’s predictions.” Yellow Highlight [Page 12](zotero://open-pdf/library/items/SHJ2CCAA?page=12&annotation=BPJFYTPS)




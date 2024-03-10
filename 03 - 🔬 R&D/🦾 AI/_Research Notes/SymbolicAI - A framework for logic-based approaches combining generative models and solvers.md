---
Publish Year: "2024"
Authors: Marius-Constantin Dinu, Claudiu Leoveanu-Condrei, Markus Holzleitner, Werner Zellinger, Sepp Hochreiter
URL: http://arxiv.org/abs/2402.00854
Zotero Link: zotero://select/library/items/ZV2W6RDJ
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Machine-Learning"
  - "#Computer-Science---Software-Engineering"
  - "#Computer-Science---Symbolic-Computation"
  - "#symbolic"
Published:
---
# Summary
# MISSION
Act as a professional research article summarizer. You are adept at looking at annotations of a research article, and distilling the insight in the below [FORMAT]

# FORMAT
## Purpose
- The research was initiated to address the limitations of current large language models (LLMs) in situational modeling, adaptability through contextual changes, and short-term problem-solving. It is a significant issue in the field of artificial intelligence. The purpose of the study was to develop a framework that combines generative models and solvers to enhance the capabilities of symbolic AI in handling real-world data's unpredictability and variability.

## Methods
- Development of SymbolicAI, a compositional neuro-symbolic (NeSy) framework.
- Utilization of large language models (LLMs) as semantic parsers.
- Implementation of in-context learning methodologies, including chain-of-thought (CoT) prompting and Tree of Thoughts (ToT).
- Construction of computational graphs through function composition.
- Development of a domain-specific language (DSL) for directing NeSy computation engines.

## Key Findings
- SymbolicAI can represent and manipulate multi-modal and self-referential structures, enhancing the problem-solving capabilities of AI systems.
- The framework leverages the in-context generalization capability of LLMs, constructing symbolic associations that aim to preserve and propagate situational context.
- SymbolicAI enables the construction of hierarchical computational graphs for self-referential meta-reasoning systems without the need for explicitly training a meta-learner.
- The use of ensemble techniques and the flexibility in domain and codomain alignment in SymbolicAI enhance the robustness, accuracy, and data flow flexibility of model predictions.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on artificial intelligence. It suggests that SymbolicAI represents a significant step towards developing AI systems capable of general problem-solving, mirroring the evolutionary and social learning processes observed in humans. The framework's ability to handle the unpredictability and variability of real-world data, combined with its enhanced problem-solving capabilities, contributes to the advancement of symbolic AI.

## Critiques
Upon evaluating the research, some critiques include:
    - The complexity of implementing and integrating the SymbolicAI framework with existing systems.
    - The potential challenges in scaling the framework for large-scale applications.
    - The need for further empirical evaluations to validate the framework's effectiveness across a wider range of tasks and domains.

## Tags
- #ArtificialIntelligence
- #MachineLearning
- #SymbolicComputation
- #NeuroSymbolicComputing
- #LargeLanguageModels
# Annotations
![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/dinuSymbolicAIFrameworkLogicbased2024/image-1-x76-y128.png]]



Consequently, operating LLMs through a purely inference-based approach confines their capabilities within their provided context window, severely limiting their horizon. This results in deficiencies for situational modeling, non-adaptability through contextual changes, and short-term problemsolving, amongst other capabilities. However, simply increasing the context length may not yield greater capabilities, as demonstrated by the observed U-shaped performance curve (Liu et al., 2023) where LLMs excel when using information at the beginning or end of the input context, but struggle with information located in the middle, especially as context increases” Yellow Highlight [Page 2](zotero://open-pdf/library/items/96K2TAIY?page=2&annotation=CE6MMVVD)



SymbolicAI, a compositional neuro-symbolic (NeSy) framework able to represent and manipulate multi-modal and self-referential structures (Schmidhuber, 2007; Fernando et al., 2023).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/96K2TAIY?page=2&annotation=8Z5I5N7Z)



In designing the architecture of SymbolicAI, we drew inspiration from the body of evidence that suggests the human brain possesses a selective language processing module (Macsweeney, 2002; Fedorenko et al., 2010; Menenti et al., 2011; Regev et al., 2013; Scott et al., 2016; Deniz et al., 2019; Hu et al., 2022), prior research on cognitive architectures (Newell & Simon, 1956; Newell et al., 1957; Newell & Simon, 1972; Newell, 1990; Laird, 2022), and the significance of language on the structure of semantic maps in the human brain (Huth et al., 2016)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/96K2TAIY?page=2&annotation=TS842HPT)



We consider language as a central processing module, distinct from other cognitive processes such as reasoning or memory (Paischer et al., 2022, 2023), that defines a stepping stone towards broad AI systems (see Section B).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/96K2TAIY?page=2&annotation=LY998E4J)



the Soar (Laird et al., 1987) cognitive architecture was developed, advancing the notion that intelligent behavior results from goal-oriented search through a problem space (Newell & Simon, 1972; McCarthy et al., 2006), with each step consisting of selecting and applying operators. Soar introduced components like reinforcement learning, impasses, substates, and chunking to enhance its problem-solving capabilities” Yellow Highlight [Page 3](zotero://open-pdf/library/items/96K2TAIY?page=3&annotation=Z3WLW773)



However, Santoro et al. (2022) emphasizes the subjectivity of symbols and suggests that human-like symbolic fluency could develop in machines through learning algorithms immersed in socio-cultural contexts” Yellow Highlight [Page 3](zotero://open-pdf/library/items/96K2TAIY?page=3&annotation=HQZ5VY4S)



The goal is to cultivate machines that demonstrate symbolic behaviors across a spectrum of competencies, potentially mirroring the evolutionary and social learning processes observed in humans. Lastly, symbolic AI struggles with real-world data’s unpredictability and variability. These challenges have led to the employment of statistical learning methodologies, like deep learning (Alom et al., 2018), which are more adept at managing noise and uncertain information through vector-valued representations.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/96K2TAIY?page=3&annotation=J38W9IM4)



While in-context learning bypasses the need for explicit retraining, it demands meticulous prompt design to steer models towards desired behaviors. Despite their versatility, current LLMs face challenges such as fallacious reasoning and the generation of erroneous content, commonly referred to as hallucinations (Jones & Steinhardt, 2022)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/96K2TAIY?page=3&annotation=E7Z8EWF8)



learning for reasoning methods treat the learning aspect as an accelerator for reasoning, in which deep neural networks are employed to reduce the search space for symbolic systems (Qu & Tang, 2019; Silver et al., 2016, 2017b,a; Schrittwieser et al., 2020)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/96K2TAIY?page=3&annotation=YRYYECBJ)



Secondly, reasoning for learning views reasoning as a way to regularize learning, in which symbolic knowledge acts as a guiding constraint that oversees machine learning tasks (Hu et al., 2016; Xu et al., 2018)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/96K2TAIY?page=3&annotation=6WMWM4VV)



Thirdly, the learning-reasoning category enables a symbiotic relationship between learning and reasoning. Here, both elements interact and share information to boost problem-solving capabilities (Donadello et al., 2017; Manhaeve et al., 2018; Mao et al., 2019; Ellis, 2023)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/96K2TAIY?page=3&annotation=W5Q34JGS)



This synergy further extends when considering graph-based methods” Yellow Highlight [Page 3](zotero://open-pdf/library/items/96K2TAIY?page=3&annotation=I7KLFRK6)



Research in this area, such as CycleGT (Guo et al., 2020) and Paper2vec (Ganguly & Pudi, 2017), explored unsupervised techniques for bridging graph and text representations. Subsequently, graph embeddings, when utilized within symbolic frameworks, can enhance knowledge graph reasoning tasks (Zhang et al., 2021), or more generally, provide the bedrock for learning domain-invariant representations (Park et al., 2023)” Yellow Highlight [Page 4](zotero://open-pdf/library/items/96K2TAIY?page=4&annotation=VYD8FWUT)



SymbolicAI conceptualizes the notion that symbols, and the expressions they form, are reflections of the information inherent in a system, and serve as surrogate for the interaction between the system and the problem space. Moreover, we argue that real patterns, as Dennett (1991) speaks of, can be effectively realized through the use of symbols because these symbols act as versatile abstractions that capture and represent the underlying structures and dynamics of these patterns, facilitating their interpretation and manipulation in computational models.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/96K2TAIY?page=4&annotation=TL32NEP2)



we adhere to the analogy of language representing the convex hull of the knowledge of our society, utilizing it as a fundamental tool to define symbols.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/96K2TAIY?page=4&annotation=VVRFCVZD)



this language-centric model does not inherently encompass all forms of representation, such as sensory inputs and non-discrete elements, requiring the establishment of additional mappings to fully capture the breadth of the world T” Yellow Highlight [Page 4](zotero://open-pdf/library/items/96K2TAIY?page=4&annotation=98RIEN4V)



developing SymbolicAI, we posit that all symbols can be represented as strings, augmented with conditional instructions and types derived from a domain-specific language (DSL) tailored for directing NeSy computation engines, like LLMs” Yellow Highlight [Page 5](zotero://open-pdf/library/items/96K2TAIY?page=5&annotation=6F5CCXBK)



we have seen in our empirical evaluations promising results utilizing LLMs as semantic parsers. This approach can be viewed as employing a form of flexible, context-sensitive grammar, which enables the processing of instructions and analogies with a nuanced understanding of language’s inherent variability and complexity.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/96K2TAIY?page=5&annotation=P69TTQUJ)



Recently, several in-context learning methodologies evolved to enable tool usage through LLMs (Schick et al., 2023), or refine the generative outcome of LLMs (Yang et al., 2023). This includes chain-ofthought (CoT) prompting, a method that conditions the model to reveal its step-by-step reasoning process (Wei et al., 2022b; Singhal et al., 2023). CoT prompting breaks down complex tasks into simpler, sequential steps, and helps with interpreting LLM’s output. Self-generated CoT, where models are encouraged to generate their own reasoning chains based on training examples, surpasses even expertly crafted CoT (Fernando et al., 2023). This observation echoes other reports that GPT-4 has an emergent self-improving capability through introspection, such as self-verification (Weng et al., 2023) or self-consistency (Wang et al., 2023b). Tree of Thoughts (ToT) enables LLMs to solve complex problems by exploring multiple reasoning paths through a search tree of coherent text units, demonstrating significant problemsolving enhancements in tasks requiring strategic planning and search (Yao et al., 2023a).” Yellow Highlight [Page 5](zotero://open-pdf/library/items/96K2TAIY?page=5&annotation=X4N888UJ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/dinuSymbolicAIFrameworkLogicbased2024/image-5-x71-y128.png]]



Ensemble techniques further enhance the robustness and accuracy of model predictions by combining several strategies to establish a consensus (Nori et al., 2023)” Yellow Highlight [Page 5](zotero://open-pdf/library/items/96K2TAIY?page=5&annotation=J4W4F2WT)



We believe that the extent of in-context learning is not yet exhausted, holding considerable promise when used alongside with task-specific fine-tuning and solvers. To develop learning and reasoning systems capable of general problem-solving, we adopt a hybrid methodology. This approach leverages the in-context generalization capability of LLMs, constructing symbolic associations that aim to preserve and propagate situational context, and validating solutions with established solvers.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/96K2TAIY?page=6&annotation=722GCBDS)



Through function composition, we construct computational graphs, in which intermediate symbols represent the nodes or states within these graphs. Formally, function composition is denoted by ◦, where combining functions f and g yields a new function h = g ◦ f, defined as h(x) = g(f(x)) For functions f : X → Y and g : Y → Z, their composition results in a function mapping elements from domain X to codomain Z through g(f(x)).” Yellow Highlight [Page 6](zotero://open-pdf/library/items/96K2TAIY?page=6&annotation=J3LHE42K)



SymbolicAI relaxes this constraint by allowing for any subset relationship between these domains and codomains, enhancing data flow flexibility. For example, this relaxed constraint in domain and codomain alignment is particularly beneficial for in-context learning. By leveraging functional few-shot learning, where few-shot examples act as dynamic elements of the function’s domain, SymbolicAI enhances its ability to interpret and respond to diverse input contexts. For instance, a function can classify a user request and select an appropriate engine to process the request.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/96K2TAIY?page=6&annotation=9A5ZYGWR)



Analogous to the Python object type, the base type of SymbolicAI is a symbol represented through its name equivalent base type Symbol. A Symbol object marks a non-reducible atomic unit” Yellow Highlight [Page 6](zotero://open-pdf/library/items/96K2TAIY?page=6&annotation=AK5EZMV9)



All other subtypes, such as Expression and its derivatives, are analogous to their mathematical namesakes, representing expressions or units that can be further evaluated and simplified. These subtypes inherit from Symbol the base attributes, primitive operators, and helper methods” Yellow Highlight [Page 6](zotero://open-pdf/library/items/96K2TAIY?page=6&annotation=6YVDGNIH)



each Symbol object contains valued and vectorvalued representations, obtained through value and embedding attributes. The latter, in particular, serve as a means to attribute a symbol’s current context, akin to embedding text and storing it as a PyTorch tensor (Paszke et al., 2019) or NumPy array (Harris et al., 2020)” Yellow Highlight [Page 6](zotero://open-pdf/library/items/96K2TAIY?page=6&annotation=QHDS285A)



vector-valued representations play a strategic role when 1) composite symbols coalesce into more complex expressions, and 2) these embedded tensors become amenable to updates through gradient-based optimization” Yellow Highlight [Page 6](zotero://open-pdf/library/items/96K2TAIY?page=6&annotation=KUAZ5WJG)



Polymorphism refers to the ability of different objects to be accessed through the same interface, or of a single identifier to represent different types based on the context of execution.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/96K2TAIY?page=6&annotation=XCPRJXSZ)



We designed the Symbol object to contain a global context, which is composed of static and dynamic context parts. The static context is class dependent and defined at design time. The dynamic context is runtime adaptable and can be changed to adhere to runtime specific logic and changes.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/96K2TAIY?page=7&annotation=H9EWCWKW)



Symbol objects can be easily manipulated through type specific attributions or symbolically evaluated by the NeSy engine. For example, a central operation for boolean logic is measuring equality between symbols. To evaluate the equality of symbols, we primarily adhere to the type specific implementation, because we prioritize strict comparisons over probabilistic evaluations. If the evaluation was unsuccessful, we then consider semantic equality through the NeSy engine” Yellow Highlight [Page 7](zotero://open-pdf/library/items/96K2TAIY?page=7&annotation=JBFZ3KQ6)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/dinuSymbolicAIFrameworkLogicbased2024/image-7-x70-y177.png]]



SymbolicAI augments the generative process by enabling systems to introspect and modify their behavior dynamically. We leverage LLMs to execute tasks based on both natural and formal language instructions, adhering to the specified user objectives and with innate self-referential structures. We derive subtypes from Expression and enclose their functionalities in task-specific components, which we then expose again through templating and the model-driven design of the NeSy engine” Yellow Highlight [Page 7](zotero://open-pdf/library/items/96K2TAIY?page=7&annotation=ZZ3MPCS3)



we utilize generalization properties from LLMs to interpret and formulate a set of operations that incorporate self-instructions (Wang et al., 2022). Consequently, the operations hold the flexibility to adapt to the context, and derive sub-processes that self-instruct LLMs to engage in situational modeling and context-sensitive problem-solving.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/96K2TAIY?page=7&annotation=SNYXK3VK)



enables the construction of hierarchical computational graphs for self-referential meta-reasoning systems without the need to explicitly training a meta-learner (Kirsch & Schmidhuber, 2022).” Yellow Highlight [Page 8](zotero://open-pdf/library/items/96K2TAIY?page=8&annotation=XCT86C3X)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/dinuSymbolicAIFrameworkLogicbased2024/image-11-x72-y340.png]]




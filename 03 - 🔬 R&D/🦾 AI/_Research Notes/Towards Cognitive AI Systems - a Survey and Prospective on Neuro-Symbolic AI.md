---
Publish Year: "2024"
Authors: Zishen Wan, Che-Kai Liu, Hanchen Yang, Chaojian Li, Haoran You, Yonggan Fu, Cheng Wan, Tushar Krishna, Yingyan Lin, Arijit Raychowdhury
URL: http://arxiv.org/abs/2401.01040
Zotero Link: zotero://select/library/items/9IS72VR4
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#knowledgegraph"
  - "#Computer-Science---Hardware-Architecture"
Published:
---
# Summary
## Purpose

- The research was initiated to address the challenges of sustainability, robustness, and explainability in AI, as well as the need for AI systems to collaborate with humans. The purpose of the study was to explore the potential of Neuro-symbolic AI (NSAI) to enhance AI capabilities in these areas.

## Methods

- Systematic categorization of NSAI algorithms into five paradigms.
- Profiling analysis of three NSAI models (LNN, LTN, NVSA) for runtime statistics.
- Use of the PyTorch Profiler to measure CPU and GPU runtimes at a per-function granularity.
- Classification of neuro and symbolic workloads into six operator categories.

## Key Findings

- NSAI integrates neural, symbolic, and probabilistic approaches to improve explainability, robustness, and data efficiency.
- Symbolic methods enhance explainability and reduce data dependence by incorporating physical world models.
- Probabilistic methods enable cognitive systems to handle uncertainty, improving robustness under unstructured conditions.
- NSAI represents an interdisciplinary approach combining symbolic reasoning with neural learning.
- Symbolic workloads are significant in computing latency and can become a system bottleneck.
- The runtime proportion of neuro vs. symbolic workloads remains stable across test sets, but total runtime increases quadratically with test set size, indicating scalability bottlenecks.

## Discussion

The discussion in the research article highlights the significance of NSAI in achieving human-like AI capabilities. It suggests that NSAI systems are currently limited to basic decision-making and reasoning problems and need more challenging datasets to advance their metacognitive capabilities. The article also envisions a unified framework for designing algorithms that combine neural, symbolic, and probabilistic components and calls for new software frameworks, programming models, compilers, and runtimes to realize the full promise of NSAI paradigms.

## Critiques

- The current applications of NSAI systems are limited and do not yet meet the broader vision of human cognitive abilities.
- There is a potential scalability bottleneck in NSAI models as the total runtime increases significantly with the size of the test set.
- Symbolic workloads may dominate runtime due to sequential and computationally intensive rule detection, which can be a critical path during inference.
- There is a need for new software frameworks and hardware architectures to support the complexities of NSAI workloads, which diverge from the current hardware roadmap focused on matrix multiplication and regular dataflows.

## Tags

- [#Computer-Science---Artificial-Intelligence](app://obsidian.md/index.html#Computer-Science---Artificial-Intelligence)
- [#knowledgegraph](app://obsidian.md/index.html#knowledgegraph)
- [#Computer-Science---Hardware-Architecture](app://obsidian.md/index.html#Computer-Science---Hardware-Architecture)
- [#NeuroSymbolicAI](app://obsidian.md/index.html#NeuroSymbolicAI)
- [#CognitiveAI](app://obsidian.md/index.html#CognitiveAI)
- [#SustainabilityInAI](app://obsidian.md/index.html#SustainabilityInAI)
- [#RobustnessAndExplainability](app://obsidian.md/index.html#RobustnessAndExplainability)

# Annotations
growing evidence that continuing our current trajectory may not be viable for realizing AI’s full potential. First, the escalating computational requirements and energy consumption associated with AI are on an unsustainable trajectory (Wu et al., 2022), threatening to reach a level that could stifle innovation by restricting it to a select few organizations.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/LLZC8JPZ?page=1&annotation=2SMKEW73)



Second, the lack of robustness and explainability remains a significant challenge, likely due to inherent limitations in current learning methodologies (Wan et al., 2021; Dwivedi et al., 2023)” Yellow Highlight [Page 1](zotero://open-pdf/library/items/LLZC8JPZ?page=1&annotation=YMD57DM9)



Third, contemporary AI systems mostly operate in isolation, with limited collaboration between humans and AI agents.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/LLZC8JPZ?page=1&annotation=M9XCT6VB)



Neuro-symbolic AI (NSAI) represents an emerging AI paradigm that integrates neural, symbolic, and probabilistic approaches to enhance explainability, robustness, and enable *Equal contribution 1Georgia Institute of Technology. Correspondence to: Tushar Krishna <tushar@ece.gatech.edu>, Yingyan (Celine) Lin <ylin715@gatech.edu>, Arijit Raychowdhury <arijit.raychowdhury@ece.gatech.edu>.  Workshop on Systems for Next-Gen AI Paradigms, 6 th Conference on Machine Learning and Systems (MLSys), June 4-8, 2023, Miami, FL, USA. Copyright 2023 by the author(s).  learning from much less data in AI (Fig. 1)” Yellow Highlight [Page 1](zotero://open-pdf/library/items/LLZC8JPZ?page=1&annotation=3CNXMME7)



symbolic methods enhance explainability and reduce the dependence on extensive training data by incorporating established models of the physical world, and probabilistic methods enable cognitive systems to more effectively handle uncertainty, resulting in improved robustness under unstructured conditions” Yellow Highlight [Page 1](zotero://open-pdf/library/items/LLZC8JPZ?page=1&annotation=IDUSS82S)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/wanCognitiveAISystems2024/image-1-x298-y67.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/wanCognitiveAISystems2024/image-2-x300-y539.png]]



NSAI represents an interdisciplinary approach that synergistically combines symbolic reasoning with neural network (NN) learning to create intelligent systems, leveraging the complementary strengths of both to enhance the accuracy and interpretability of the resulting models.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/LLZC8JPZ?page=2&annotation=GNQBWB9A)



Inspired by Henry Kautz’s NSAI taxonomy (Kaut, 2020), we systematically categorize these NSAI algorithms into five paradigms, as summarized in Tab. 1.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/LLZC8JPZ?page=2&annotation=CZX27JAX)



Neuro|Symbolic refers to a hybrid system that combines a neural system and a symbolic system in a pipeline, where each component typically specializes in complementary tasks within the pipeline” Yellow Highlight [Page 2](zotero://open-pdf/library/items/LLZC8JPZ?page=2&annotation=8FNC4UI3)



IBM’s neuro-vector-symbolic architecture (NVSA) (Hersche et al., 2023) uses an NN as the frontend for perception and semantic parsing, and a symbolic reasoner as the backend for probabilistic abductive reasoning” Yellow Highlight [Page 2](zotero://open-pdf/library/items/LLZC8JPZ?page=2&annotation=GHD8I5W3)



neuro-probabilistic soft logic (NeuPSL) (Pryor et al., 2022), neural probabilistic logic programming (DeepProbLog) (Manhaeve et al., 2021), neuro-answer set programming (NeurASP) (Yang et al., 2020), nerual symbolic dynamic reasoning (Yi et al., 2020), neural symbolic concept learner (NSCL) (Mao et al., 2019), abductive learning (ABL) (Dai et al., 2019), and neurosymbolic visual question answering (NSVQA) (Yi et al., 2018)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/LLZC8JPZ?page=2&annotation=5QNG6CVQ)



Neuro approach incorporates symbolic rules into NNs to guide the learning process, where symbolic knowledge is compiled into the structure of neural models for enhancing the model interpretability. For instance, logical NNs (LNNs) (Riegel et al., 2020) encode knowledge or domain expertise as symbolic rules (first-order logic or fuzzy logic) that act as constraints on the NN output. Other examples include deep learning for symbolic mathematics (Lample & Charton, 2019) and differentiable inductive logic programming (ILP) (Evans & Grefenstette, 2018).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/LLZC8JPZ?page=2&annotation=U87KCNK3)



It involves mapping symbolic logic rules onto embeddings that serve as soft constraints or regularizers on the NN’s loss function. Logical tensor networks (LTNs) (Badreddine et al., 2022), for instance, use logical formulas to define constraints on the tensor representations, which has proven successful in knowledge graph completion tasks.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/LLZC8JPZ?page=2&annotation=WTYKKBCT)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/wanCognitiveAISystems2024/image-3-x52-y624.png]]



deep ontology networks (Hohenecker & Lukas, 2020) and tensorization methods (Garcez et al., 2019).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/LLZC8JPZ?page=3&annotation=U7YTFFBQ)



Unlike Symbolic[Neuro], where symbolic reasoning is used to guide the neural model learning process, in Neuro[Symbolic], the neural model incorporates symbolic reasoning by paying attention to specific symbolics at certain conditions” Yellow Highlight [Page 3](zotero://open-pdf/library/items/LLZC8JPZ?page=3&annotation=RCT3ZEDH)



graph neural networks (GNNs) are often adopted as strong candidates for representing symbolic expressions when endowed with attention mechanisms (Lamb et al., 2020). In particular, this attention mechanism can be leveraged to incorporate symbolic rules into GNN models, enabling selective attention to pertinent symbolic information in the graph. Other examples include neural logic machines (NLM) (Dong et al., 2019).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/LLZC8JPZ?page=3&annotation=L2QZ886I)



We select three NSAI models for profiling analysis: an LNN on a logic program task (Riegel et al., 2020), an LTN on a binary classification task (Badreddine et al., 2022), and an NVSA (Hersche et al., 2023) on the Raven’s Progressive Matrices task (Zhang et al., 2019), representing Neuro:Symbolic→Neuro, NeuroSymbolic, and Neuro|Symbolic NSAI systems (Sec. 2), respectively” Yellow Highlight [Page 3](zotero://open-pdf/library/items/LLZC8JPZ?page=3&annotation=WEB5ZJRG)



We first conduct functionlevel profiling to capture runtime statistics, and then use the PyTorch Profiler (Maxim Lukiyanov, Guoliang Hua, Geeta Chauhan, and Gisle Dankel, 2021) to measure the CPU and GPU runtimes of each model at a per-function granularity.  The experiments are conducted on a system with an Intel Xeon Silver 4114 CPU and an Nvidia RTX 2080 Ti GPU.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/LLZC8JPZ?page=3&annotation=P9N99DTZ)



We classify each neuro and symbolic workload of the LNN, LTN, and NVSA models into six operator categories: convolution, matrix multiplication (MatMul), vector/element-wise operation (e.g., tensor add, div, and norm), data transformation (e.g., reshape and transpose), data movement (e.g., inter-device transfer), and others (e.g., fuzzy logic, and logic rule) (Susskind et al., 2021).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/LLZC8JPZ?page=3&annotation=UCSL2FTM)



symbolic workloads are not negligible in computing latency and may become a system bottleneck. Fig. 2(a) shows the runtime breakdown for each model, where the neuro (symbolic) workloads account for 54.6% (45.4%), 48.0% (52.0%), 7.9% (92.1%) runtime of the LNN, LTN, and NVSA models, respectively” Yellow Highlight [Page 3](zotero://open-pdf/library/items/LLZC8JPZ?page=3&annotation=L96D5RN8)



symbolic workload dominates the NVSA’s runtime, predominately due to the sequential and computational-intensive rule detection during the involved reasoning procedure. This reasoning computation depends on the result of the frontend neuro workload and thus lies on the critical path during inference;” Yellow Highlight [Page 3](zotero://open-pdf/library/items/LLZC8JPZ?page=3&annotation=LJYV4FZX)



We observe that the neuro vs. symbolic runtime proportion shown in Fig. 2(a) remains relatively stable across various test sets under the same size, whereas the total runtime increases quadratically with the test set size. For example, when the test set size increases from 2×2 to 3×3, the symbolic workload runtime percentage only increases from 92.06% to 94.71%, but the total runtime of the NVSA model increases by 5.02×, indicating the potential scalability bottleneck of NSAI models.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/LLZC8JPZ?page=3&annotation=DERFZQEZ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/wanCognitiveAISystems2024/image-3-x295-y66.png]]



The symbolic workload is dominated by vector and scalar operations exhibiting low operational intensities and complex control flows. Both LNN (symbolic) and LTN (symbolic) have a large number of logic operations, posing parallelism optimization opportunities in their database queries and arithmetic operations, especially for larger symbolic models. Meanwhile, LNN (symbolic) is severally data movement-bounded due to its sparse and irregular memory accesses and bidirectional inference, where model-aware dataflow architecture would likely be beneficial for alleviating this bottleneck. Notably, the elementwise operations usually stem from high-dimensional distributed vector computations (e.g., binding, bundling, and permutation) for symbolic representation, which is difficult to process efficiently on GPUs. Therefore, the challenges of accelerating these computations will become increasingly important as the task and feature complexities further grow.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/LLZC8JPZ?page=4&annotation=SRLTP6P6)



NSAI systems hold great potential in achieving human-like AI (Booch et al., 2021). However, their current applications are limited to basic decision-making and reasoning problems (Garcez et al., 2022), falling short of the broader vision of human cognitive abilities, such as interpretability, deductive reasoning, systematicity, productivity, compositionality, inferential coherence of mental thought, and causal and counterfactual thinking. To significantly advance the metacognitive capabilities of NSAI systems, more challenging and suitable datasets are highly desirable to unleash NSAI’s potential.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/LLZC8JPZ?page=4&annotation=YQUVH3IN)



We envision a unified framework to design algorithms that opportunistically combine neural, symbolic, and probabilistic components, and for quantifying scaling laws for neuroprobabilistic-symbolic inference versus large neural models” Yellow Highlight [Page 4](zotero://open-pdf/library/items/LLZC8JPZ?page=4&annotation=8C2MY29N)



new software frameworks are needed that can encompass a broad set of reasoning logical capabilities and provide practical syntactic and semantic extensions while being fast and memoryefficient. Moreover, new programming models, compilers, and runtimes that can facilitate the ease and efficient realization of the neuro-symbolic-probabilistic models are of significance to realize the full promise of NSAI paradigms.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/LLZC8JPZ?page=4&annotation=6JXVPHVG)



from an architectural and hardware perspective, we need modeling-simulation-characterization frameworks to enable the development of novel architectures for these workloads and build optimized modular blocks as libraries by leveraging workload characteristics, as other emerging domains (Krishnan et al., 2022a; Wan et al., 2022).” Yellow Highlight [Page 4](zotero://open-pdf/library/items/LLZC8JPZ?page=4&annotation=UPAPELHB)



This leads to an increasing divergence with the current hardware roadmap that largely focuses on matrix multiplication or nearest neighbor search, and regular dataflows, e.g., systolic arrays (Krishnan et al., 2022b) or compute-in-memory crossbars (Crafton et al., 2022). Therefore, we need novel architectures with dedicated processing units, memory hierarchies, and on-chip interconnects that can handle the additional complexities in computations and communications. Additionally, the architecture needs to provide flexibility with both configurable interconnects and full addressable memories to keep pace with NSAI algorithmic innovations.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/LLZC8JPZ?page=4&annotation=GUM25XL5)




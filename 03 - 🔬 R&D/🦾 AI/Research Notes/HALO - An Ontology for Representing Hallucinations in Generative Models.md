---
Publish Year: "2023"
Authors: Navapat Nananukul, Mayank Kejriwal
URL: http://arxiv.org/abs/2312.05209
Zotero Link: zotero://select/library/items/DMWUMCZF
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
Published: 2024-05-07
---
# Summary
The paper: http://arxiv.org/abs/2312.05209

## Purpose   
The paper addresses the challenge of hallucinations in generative AI, including LLMs like ChatGPT. It presents the Hallucination Ontology (HALO), a formal, extensible ontology written in OWL, offering support for various types of hallucinations and related metadata. This tool is designed to help better understand and categorize hallucinations in AI systems.  
  
## Methods   
- Development of the HALO ontology using the Linked Open Terms (LOT) methodology.  
- Identification of primary hallucination categories through literature review.  
- Integration of HALO with terms from existing vocabularies for interoperability.  
- Use of Google Forms and Python-based programs for data conversion into RDF/XML format.  
  
## Key Findings   
1. HALO supports six distinct types of hallucinations in LLMs, categorized under Factuality and Faithfulness Hallucinations.  
2. The ontology allows for systematic documentation of hallucinations, their metadata, and provenance.  
3. HALO is validated using competency questions (CQs) and SPARQL queries to demonstrate its utility in empirical studies of hallucinations.  
4. HALO is published under an open license and is accessible for public use and contribution.

## Hallucinations in HALO Ontology  
  
### Factuality Hallucinations  
1. **Factual Inconsistency**:   
   - Occurs when LLMs produce responses with contradictions or misinformation about real-world facts.  
   - Example: Incorrectly identifying "Yuri Gagarin" as the first person to land on the Moon.  
  
2. **Factual Fabrication**:   
   - Refers to LLMs creating responses with unverifiable supporting evidence.  
   - Example: Fabricating narratives about dragons existing on Earth without any empirical evidence.  
  
### Faithfulness Hallucination  
1. **Instruction Inconsistency**:   
   - Arises when LLM outputs do not align with the user’s prompt instructions.  
   - Example: The user requests a translation, but the LLM performs a question-answering task instead.  
  
2. **Context Inconsistency**:   
   - Occurs when the LLM’s response does not align with the provided context.  
   - Example: Providing dinner suggestions when asked about breakfast.  
  
3. **Logical Inconsistency**:   
   - Happens when an LLM’s output contains internal logical contradictions.  
   - Example: Correctly performing mathematical steps but concluding with an incorrect final answer.  
  
4. **Confidence Mismatch**:   
   - Involves LLMs displaying a high level of confidence in responses that are factually incorrect or nonsensical.  
   - Example: Asserting incorrect facts with high confidence.  
  
## Discussion   
This research provides a crucial tool for understanding and managing hallucinations in AI, an area increasingly important as AI systems like ChatGPT become more sophisticated and widely used. HALO bridges the gap between anecdotal observations and systematic study, offering a structured way to analyze hallucinations in LLMs.  
  
## Critiques   
1. The need for continuous evolution of HALO to capture new types of hallucinations as AI technology progresses.  
2. The challenge of ensuring comprehensive coverage of hallucination instances, given the decentralized nature of data sources.  
  
## Tags  
#AI #Hallucinations #LLMs #ChatGPT #Ontology #HALO #GenAI.
# Annotations
The issue of hallucinations, in particular, has raised some important concerns such as misinformation and over-reliance on the system’s output, especially when the system seems to be giving the correct answer in response to a prompt [” Yellow Highlight [Page 2](zotero://open-pdf/library/items/988DPHBL?page=2&annotation=MWS4NP5I)



Even ‘citizen scientists,’ who have been playing with models like ChatGPT owing to its easy-to-use interface, have documented a wide body of hallucinations even in common Web forums.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/988DPHBL?page=2&annotation=8KDX362L)



At the same time, any such ontology can only have practical utility if it is extensible, well-documented, and amenable to modeling both hallucination instances and their metadata, which include details such as what LLMs the hallucination instance was tried on, when it was tried, its provenance, and so on.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/988DPHBL?page=2&annotation=Q9G332LZ)



the Hallucination Ontology (HALO), a resource for modeling hallucination instances and their metadata.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/988DPHBL?page=2&annotation=QNC4LHQC)



we drew upon the Linked Open Terms (LOT) methodology [25] as our guiding framework. LOT’s methodology is particularly suited to our goal of developing a robust, extensible ontology from scratch.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/988DPHBL?page=3&annotation=RRAZAIGJ)



to connect hallucination in LLMs with existing classes and enhance interoperability, we also follow the Minimum Information to Reference an External Ontology Term (MIREOT) guidelines” Yellow Highlight [Page 3](zotero://open-pdf/library/items/988DPHBL?page=3&annotation=XEZL5WW5)



LOT methodology is structured around iterative cycles through a foundational workflow, including four phases: (i) ontological requirements specification, (ii) ontology implementation, (iii) ontology publication, and (iv) ontology maintenance” Yellow Highlight [Page 4](zotero://open-pdf/library/items/988DPHBL?page=4&annotation=Q26PZBVD)



HALO is created based on two existing primary vocabulary sources: (1) hallucination categories and (2) external classes/entities.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/988DPHBL?page=6&annotation=GJP878P2)



1. Factuality Hallucinations refers to errors in LLMs outputs by misrepresenting real-world facts. These errors manifest in two distinct ways: – Factual Inconsistency occurs when LLMs produce answers or responses that reference real-world facts but include contradictions or misinformation.  Example: LLMs incorrectly identify “Yuri Gagarin” as the first person to land on the Moon, a clear contradiction of established historical facts.  – Factual Fabrication refers to LLMs producing responses with supporting evidence that cannot be verified by established real-world information.  Example: An LLM fabricates a detailed historical narrative about dragons existing on Earth despite no empirical evidence or historical records supporting such a claim.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/988DPHBL?page=7&annotation=YIJVKKUA)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/nananukulHALOOntologyRepresenting2023/image-8-x122-y303.png]]



2. Faithfulness Hallucination refers to LLM outputs that fail to align faithfully with user instructions, when provided with context, including wellknown logical rules based in objective fields like math or physics,” Yellow Highlight [Page 8](zotero://open-pdf/library/items/988DPHBL?page=8&annotation=8AY8S69K)



– Instruction Inconsistency arises when LLM outputs do not follow the user’s prompt instructions. Example: Users intend to request a translation of a specific sentence, but the LLM erroneously performs a question-answering to that sentence instead of translating it. – Context Inconsistency occurs when the LLM’s output is not aligned to the user’s provided contextual information. Example: LLMs provided an answer about great food for dinner when a user asked about breakfast, and it clearly stated in the users’ prompt” Yellow Highlight [Page 8](zotero://open-pdf/library/items/988DPHBL?page=8&annotation=KCXPDBN6)



– Logical Inconsistency occurs when an LLM’s output exhibits internal logical contradictions, often observed in reasoning tasks4. Example: LLM might correctly perform mathematical steps, but then conclude with an incorrect final answer” Yellow Highlight [Page 9](zotero://open-pdf/library/items/988DPHBL?page=9&annotation=W2HVZ8IX)



here are two main branches from the major LLMsHallucination root class: (1) factualityHallucination which comprises two sub-classes FactualFabrication and factualInconsistency (2) faithfulnessHallucination which comprises of three sub-classes logicalInconsistency, instrctionInconsistency, and contextInconsistency.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/988DPHBL?page=9&annotation=FG8A5QMB)



Examples of external classes we connected to this module include foaf:person, foaf:document, schema:date, schema:schorlarlyArticle, etc.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/988DPHBL?page=9&annotation=V8X6PEI7)



The Metadata module represents the core concept and properties of the prompts and answers we gathered.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/988DPHBL?page=9&annotation=W5SFBNEI)



The module comprises four primary concepts: GenerativeAI, LargeLanguageModel, LLMsPrompt, and LLMsAnswers, each briefly described below: 1. GenerativeAI describes broadly the types of AI agents that showed hallucinations. The instance of this class can be an AI agent from any field such as text generation models, image generation models, or LLMs. Since our initial experiments are tested on LLMs, the GenerativeAI class has only one subclass (LargeLanguageModel ) for the current version of HALO. 2. LargeLanguageModel describes instances of LLMs that exhibit hallucination, including names and model versions. 3. LLMsPrompt instantiates the metadata of the collected prompts, with attributes such as (1) hasPromptID, an internal identifier for tracking prompts; (2) CollectedOn, the date of prompt acquisition; and (3) hasSource, the internet source we found the prompt. 4. LLMsAnswer encapsulates metadata about the LLMs’ responses, featuring (1) hasAnswerID for internal answer tracking and (2) hasAnswerDate for recording the date of the response. Additionally, LLMsAnswer serves as a bridge between the Metadata and Hallucination modules, linked by the relation metadata: hallucinationGeneratedBy, indicating that an LLM’s answer we add into our ontology generated a specific hallucination type.” Yellow Highlight [Page 10](zotero://open-pdf/library/items/988DPHBL?page=10&annotation=FDW6QJAZ)



When studying hallucinations in LLMs, an important analytical objective is to assess whether hallucinations persist across LLMs i.e., if a prompt led to a hallucination in ChatGPT, does it also lead to a hallucination in BARD, more often than not?” Yellow Highlight [Page 11](zotero://open-pdf/library/items/988DPHBL?page=11&annotation=KYYQC9RE)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/nananukulHALOOntologyRepresenting2023/image-12-x171-y279.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/nananukulHALOOntologyRepresenting2023/image-13-x145-y420.png]]




---
Publish Year: '2024'
Authors: "Kai Mei, Zelong Li, Shuyuan Xu, Ruosong Ye, Yingqiang Ge, Yongfeng Zhang"
URL: "http://arxiv.org/abs/2403.16971"
Zotero Link: "zotero://select/library/items/QYC9MRRS"
tags:
  - "#Computer-Science---Artificial-Intelligence, #Computer-Science---Computation-and-Language, #Computer-Science---Operating-Systems, #chatos"
Published:
---
# Summary

## Purpose
- The research was initiated to address the challenges in managing the concurrent operation of multiple LLM (Large Language Model) agents within an operating system, focusing on memory management, privacy, and access control. This is a significant issue in the field of **Computer Science**, particularly within the subfields of **Artificial Intelligence**, **Computation and Language**, and **Operating Systems**. The purpose of the study was to develop an LLM agent operating system (AIOS) that provides module isolation and aggregates functionalities of LLM and OS to efficiently manage tasks associated with LLM agents and those unrelated to LLM.

## Methods
- Design of an LLM-specific kernel to segregate OS-like duties related to the oversight of LLM agents, their resources, and development toolkits.
- Implementation of various managers within the AIOS architecture, including Agent Scheduler, Context Manager, Memory Manager, Storage Manager, Tool Manager, and Access Manager, to support the operation of multiple LLM agents.
- Development of the AIOS SDK to encapsulate LLM system calls, providing convenient agent library functions for agent developers.

## Key Findings
- The AIOS architecture effectively addresses potential conflicts between tasks associated with LLM and those unrelated to LLM through the design of an LLM-specific kernel.
- The introduction of various managers (Agent Scheduler, Context Manager, etc.) within the AIOS architecture enables efficient management of agent requests, memory, storage, and access control, facilitating the operation of multiple LLM agents.
- The AIOS SDK allows for the seamless integration of LLM reasoning and OS-level actions, enabling LLM agents to tackle complex, multi-modal tasks that require reasoning, execution, and interaction with the physical world.

## Discussion
The discussion in the research article highlights the significance of the AIOS architecture in enhancing the functionality and efficiency of LLM agents within an operating system. It suggests that the AIOS architecture and its components contribute significantly to the field of Computer Science, particularly in the areas of Artificial Intelligence and Operating Systems, by enabling multiple LLM agents to perform complex tasks more effectively. The research findings have the potential to impact the development of future LLM-based applications and systems.

## Critiques
Upon evaluating the research, some critiques include:
- The complexity of implementing the AIOS architecture in existing systems and ensuring compatibility with various LLM models and external APIs.
- The scalability of the AIOS architecture as the number of LLM agents and the complexity of tasks increase.
- The potential need for more sophisticated memory management mechanisms, such as shared memory pools among agents or hierarchical caches, which are suggested for future integration into AIOS.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Computation-and-Language
- #Computer-Science---Operating-Systems
- #chatos

# Annotations
the concurrent operation of multiple agents necessitates a robust system for memory management across different agents, while also ensuring stringent enforcement of privacy and access control measures.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/BRT5CK8K?page=2&annotation=3J2FYKIW)



AIOS, an LLM agent operating system (Figure 2) to provide module isolation and aggregations of LLM and OS functionalities. To address the potential conflicts arising between tasks associated with LLM and those unrelated to LLM, we propose the design of an LLM-specific kernel. This kernel segregates the OS-like duties, particularly those related to the oversight of LLM agents, their corresponding resources, and development toolkits” Yellow Highlight [Page 2](zotero://open-pdf/library/items/BRT5CK8K?page=2&annotation=REQ4MBTP)



Agent Scheduler: Prioritizes and schedules agent requests to optimize LLM utilization.  • Context Manager: Supports snapshot and restore the intermediate generation status in LLM and context window management of LLM.  • Memory Manager: Provides short-term memory for each agent’s interaction logs.  • Storage Manager: Persists agent interaction logs to long-term storage for future retrieval.  • Tool Manager: Manages agent’s calling of external API tools (e.g., search, scientific computing).  • Access Manager: Enforces privacy and access control policies between agents.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/BRT5CK8K?page=2&annotation=G37CX7W9)



we design the AIOS SDK to further encapsulate the LLM system calls, providing more convenient agent library functions for agent developers. With the AIOS architecture, an agent like the travel planner can break down its task into steps that fluidly combine LLM reasoning (e.g., plan generation and tool calling decision) and OS-level actions (e.g., accessing storage and executing software services). This synergistic combination of capabilities equips multiple LLM agents to tackle increasingly complex, multi-modal tasks that require reasoning, execution, and interaction with the physical world.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/BRT5CK8K?page=2&annotation=F4BFCXZ6)



LLM-based Single-Agent Systems. LLM-based single-agent systems (SAS) use a single LLM agent for complex task solving, such as travel planning, personalized recommendation, and artistic design [7]. The agent takes natural language instruction from users as input and decomposes the task into a multistep plan for task solving, where each step may call external tools to be completed, such as collecting information, executing specialized models, or interacting with the external world.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/BRT5CK8K?page=3&annotation=F4KLFG5K)



LLM-based Multi-Agent Systems. LLM-based multi-agent systems (MAS) leverage the interaction among multiple agents for problem solving. The relationship among the multiple agents could be cooperative, competitive, or a mixture of cooperation and competition [33]. In cooperative multi-agent systems, each agent takes and assesses the information provided by other agents, thereby working together to solve complex tasks, such as role playing [46], social simulation [47] and software development [48, 49, 50, 51]. In competitive multi-agent systems, agents may detabe, negotiate and compete with each other in a game environment to achieve their goals, such as improving negotiation skills [52] and debating about the correct answer [53, 54, 55]” Yellow Highlight [Page 3](zotero://open-pdf/library/items/BRT5CK8K?page=3&annotation=C4G9R65R)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/meiAIOSLLMAgent2024/image-4-x82-y477.png]]



the architecture of our AIOS is organized into three distinct layers: the application layer, the kernel layer, and the hardware layer” Yellow Highlight [Page 4](zotero://open-pdf/library/items/BRT5CK8K?page=4&annotation=HKZAL74L)



Each higher layer abstracts the complexities of the layers below it, facilitating interaction through interfaces or specific modules, thereby enhancing modularity and simplifying system interactions across different layers.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/BRT5CK8K?page=4&annotation=CI6KNKXW)



Kernel Layer. The kernel layer is divided into two primary components: the OS Kernel and the LLM Kernel, each serving the unique requirements of non-LLM and LLM-specific operations, respectively. This distinction allows the LLM kernel to focus on LLM specific tasks such as context management and agent scheduling, which are essential for handling LLM-related activities and are not typically within the purview of standard OS kernel functions.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/BRT5CK8K?page=4&annotation=FK2IDNHU)



The LLM kernel is equipped with several key modules, including the LLM system call interface, agent scheduler, context manager, memory manager, storage manager, tool manager, and access manager” Yellow Highlight [Page 4](zotero://open-pdf/library/items/BRT5CK8K?page=4&annotation=RX3528XY)



It is crucial to note that the LLM kernel’s system calls cannot directly interact with the hardware. Instead, these calls interface with the OS’s system calls, which in turn manage the hardware resources.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/BRT5CK8K?page=4&annotation=SIVSIIVS)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/meiAIOSLLMAgent2024/image-5-x307-y503.png]]



Agent scheduler is designed to manage the agent requests in an efficient way. Consider the various agents (denoted as A, B, and C) in Figure 3, each of which has several execution steps. In the sequential execution paradigm, the agent tasks are processed in a linear order, where steps from a same agent will be processed first. This can lead to potential increased waiting times for tasks queued later in the sequence.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/BRT5CK8K?page=5&annotation=LWDG9XY3)



The agent scheduler employs strategies such as First-In-First-Out (FIFO)7, Round Robin (RR)8 , and other scheduling algorithms to optimize this process.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/BRT5CK8K?page=5&annotation=LBCSYCRG)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/meiAIOSLLMAgent2024/image-5-x79-y96.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/meiAIOSLLMAgent2024/image-6-x302-y415.png]]



sider that the scheduler algorithms may involve time quantum operations (e.g., Round-Robin) and agent requests may be suspended by the scheduler. This suspension happens even if the response has not been fully generated yet by the LLM. Therefore, it necessitates a mechanism to preserve the state of the LLM’s generation process, ensuring that it can be accurately resumed once resources are available again.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/BRT5CK8K?page=6&annotation=JAC2ITXT)



AIOS provides the snapshot and restoration mechanisms in the context manager to address this issue, which can be seen from Figure 4. We use the beam search process9, a typical practice in LLMs [10, 57, 58], to illustrate the generative decoding process.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/BRT5CK8K?page=6&annotation=C9YID2V3)



When such generation process has been suspended by the scheduler at an intermediate step, the context manager uses the snapshot function to capture and store the current state of the LLM’s beam search tree, including all intermediate probabilities and paths being explored for generating the response.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/BRT5CK8K?page=6&annotation=KPCB3325)



Context Window Management. To address challenges posed by long contexts that surpass the context window limit of LLMs, context manager also needs to manage potential expansion of context window. Specifically, context manager in AIOS supports basic text summarization and incorporates other expansion techniques [59, 60] to manage the context window. In this way, it can help enhance the LLM’s ability to process and understand extensive contexts without compromising the integrity or relevance of the information.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/BRT5CK8K?page=6&annotation=J678QU7E)



The current AIOS supports storing each agent’s memory independently, each of which other agents have no direct access to, unless it is authorized by the access manager. More complicated memory mechanisms such as shared memory pools among agents or hierarchical caches can be considered and integrated into AIOS in the future.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/BRT5CK8K?page=6&annotation=L5SCGCKE)



the storage manager is responsible for the long-term preservation of data, overseeing the storage of information that needs to be retained indefinitely, beyond the active lifespan” Yellow Highlight [Page 6](zotero://open-pdf/library/items/BRT5CK8K?page=6&annotation=FSNF3VSI)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/meiAIOSLLMAgent2024/image-7-x100-y547.png]]



The storage manager supports retrieval augmentation [61]. Through storing user preferences and maintaining historical interaction logs, the storage manager can enrich the agent knowledge update and enhancing the long-term user experience.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/BRT5CK8K?page=7&annotation=JFDMUCVG)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/meiAIOSLLMAgent2024/image-7-x90-y131.png]]



The tool manager in the AIOS system manages a diverse array of API tools that enhance the functionality of LLMs” Yellow Highlight [Page 7](zotero://open-pdf/library/items/BRT5CK8K?page=7&annotation=JSJN9PNE)



The access manager orchestrates access control operations among distinct agents by administering a dedicated privilege group for each agent. Those other agents that are excluded from an agent’s privilege group are denied access to its resources, such as the interaction history” Yellow Highlight [Page 7](zotero://open-pdf/library/items/BRT5CK8K?page=7&annotation=JZF5ZQ7X)



The AIOS SDK is designed to equip developers with a versatile toolkit for crafting sophisticated agent applications within the AIOS” Yellow Highlight [Page 8](zotero://open-pdf/library/items/BRT5CK8K?page=8&annotation=LTFHQ9L4)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/meiAIOSLLMAgent2024/image-8-x100-y304.png]]




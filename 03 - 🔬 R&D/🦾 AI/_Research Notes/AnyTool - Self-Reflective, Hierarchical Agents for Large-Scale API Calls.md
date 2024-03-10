---
Publish Year: '2024'
Authors: "Yu Du, Fangyun Wei, Hongyang Zhang"
URL: "http://arxiv.org/abs/2402.04253"
Zotero Link: "zotero://select/library/items/DHQ7EMGJ"
tags:
  - "#Computer-Science---Computation-and-Language"
Published:
---
# Summary
## Purpose
- The research was initiated to address the challenge of effectively leveraging a large number of APIs (over 16,000) for user queries, which is a significant issue in the field of computer science and artificial intelligence. The purpose of the study was to develop a system, named AnyTool, that can efficiently identify and utilize the most relevant APIs for given user queries through a self-reflective, hierarchical agent structure.

## Methods
- Design of a hierarchical structure within the API retriever, inspired by the divide-and-conquer approach and incorporating API categorization.
- Implementation of a self-reflective mechanism where AnyTool, upon receiving a query, suggests a solution evaluated by GPT-4 for feasibility, with the ability to reconsider based on failure reasons and historical contexts.
- Utilization of a function calling process involving user input, GPT-4 generated requests, and execution of functions until a "Finish Function" signals query resolution.
- Exploration of two potential implementations for the solver: Depth-First Search-Based Decision Tree (DFSDT) or the Chain of Thought (CoT) approach.

## Key Findings
- AnyTool effectively reduces the search scope for each agent by leveraging a hierarchical structure, thus overcoming constraints related to the maximum context length in large language models (LLMs).
- The self-reflective mechanism of AnyTool enhances the efficiency and effectiveness of the query resolution process by reducing oversearch for simpler queries and providing a more in-depth search for complex queries.
- The function calling process allows for a dynamic and interactive solution generation, accommodating user goals and specific design requirements.
- The hierarchical structure, combined with the self-reflection mechanism and function calling process, enables AnyTool to directly search through an extensive API pool and analyze unsolved user queries by considering failure reasons and historical contexts.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on the field of artificial intelligence and API utilization. It suggests that AnyTool represents a significant advancement in efficiently managing and leveraging large-scale API calls for user queries. The system's ability to self-reflect and adapt based on the success of proposed solutions could lead to more intelligent and efficient query resolution mechanisms, potentially transforming how APIs are utilized in various applications.

## Critiques
Upon evaluating the research, some critiques include:
    - The complexity of the hierarchical structure and the self-reflective mechanism may introduce challenges in implementation and scalability.
    - The reliance on GPT-4 for evaluating the feasibility of solutions and for the function calling process may limit the system's applicability in environments where GPT-4 is not available or feasible.
    - The generalizability of the findings and the system's effectiveness across different domains and types of APIs remain to be fully explored.

## Tags
- #Computer-Science---Computation-and-Language
- #ArtificialIntelligence
- #APIUtilization
- #LargeLanguageModels

# Annotations
AnyTool, a GPT-4-empowered agent, as depicted in Figure 1a. It is designed to effectively leverage more than 16,000 APIs” Yellow Highlight [Page 1](zotero://open-pdf/library/items/EGQXP2LK?page=1&annotation=EALF8AQN)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/duAnyToolSelfReflectiveHierarchical2024/image-2-x48-y403.png]]



To identify the most relevant APIs for user queries, we design a hierarchical structure within our API retriever. This structure is composed of three tiers, each containing one or multiple agents with diverse roles.  This arrangement is inspired by the divide-and-conquer approach. Additionally, we effectively incorporate the API categorization suggested by Rapid API into our hierarchical structure. Consequently, this significantly reduces the search scope for each agent and overcomes constraints related to the maximum context length in LLMs” Yellow Highlight [Page 2](zotero://open-pdf/library/items/EGQXP2LK?page=2&annotation=NDITPHK4)



Our AnyTool is designed to address user queries through a process of initial attempt followed by reflection. Upon receiving a query, AnyTool suggests a solution, which is then evaluated for feasibility by GPT-4. In cases where the proposed solution is deemed impractical, AnyTool is re-activated, with the consideration of reasons for failure and relevant historical contexts.  This mechanism significantly reduces the tendency to “oversearch” for simpler queries, while also providing a more context-rich and in-depth search for complex queries. This closed-loop system enhances the efficiency and effectiveness of the query resolution process” Yellow Highlight [Page 2](zotero://open-pdf/library/items/EGQXP2LK?page=2&annotation=GDA8M6TR)



The process of function calling involves: 1) the user inputs both the query Q and the function list {Fi}M i=1, alongside a designated “Finish Function” F∗, into GPT-4; 2) GPT4 generates a function calling request for the user, with clear input parameters; 3) the user executes the specific function and provides the historical context and function response to GPT-4; 4) this cycle of steps two and three is repeated multiple times until GPT-4 activates the “Finish Function” F∗, signaling the resolution of query Q. Users have the option to either employ the output of F∗ directly, or to gather the interim results generated during the function calling process, according to their specific goals or design.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/EGQXP2LK?page=3&annotation=7AYHAZGZ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/duAnyToolSelfReflectiveHierarchical2024/image-4-x43-y533.png]]



it can directly search the entire API pool, which contains over 16K APIs, using a hierarchical structure and a divideand-conquer principle. Lastly, it is capable of self-reflection, enabling it to review and analyze unsolved user queries by taking into account reasons for failure and relevant historical contexts.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/EGQXP2LK?page=4&annotation=TTZ5GKTW)



the first tier is the category level, encompassing various domains such as “sports” and “finance”; the second tier, designated as the tool level, consists of tools that belong to specific categories; and the third tier focuses on individual APIs, with each API belonging to a specific tool, as illustrated in Figure 2. This hierarchical arrangement serves as a foundational guideline in the development of our API retriever.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/EGQXP2LK?page=5&annotation=554RI7NZ)



The intermediary tier is comprised of multiple category agents, each established by the meta-agent. These agents correspond to individual categories as defined by Rapid API, with their primary objective being to identify the most relevant tools for the query Q from their respective tool collections. Subsequently, these category agents initiate the creation of various tool agents. It is important to note that each tool agent may manage multiple tools, depending on the decisions made by the category agents. The goal of each tool agent is to search through its managed APIs for those that might solve the query Q, and then add these APIs to an API-candidate pool.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/EGQXP2LK?page=5&annotation=DHKHW6TA)



bootstrap prompt as outlined in Section B.1 of the appendix. This process heavily relies on the function calling feature of GPT-4 (refer to Section 3.1). Operating interactively, our system enables agents (starting with the meta-agent) to send requests for calling their managed functions. These functions may involve creating a specific agent (either a category agent or a tool agent) or executing a particular function, in accordance with the historical context.1 The requests are parsed, and the corresponding functions are executed. The results produced by these functions are subsequently incorporated into the historical context, which is then returned to the agents. This process repeats continuously until the termination criteria are met.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/EGQXP2LK?page=5&annotation=QI8MUNIG)



Two potential implementations for the solver are the DepthFirst Search-Based Decision Tree (DFSDT) or the Chain of Thought (CoT) approach.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/EGQXP2LK?page=5&annotation=VAQC3FQW)



The “finish” function yields one of three possible outcomes: “Give Solution”, “Try Backtrack”, or “Give Up”, with “Try Backtrack” being specific to the DFSDT implementation.  Each iteration involves: 1) the solver sending a request to call a function, 2) the interpretation of this request and the execution of the function, and 3) the integration of the function’s outcomes into the contextual history, which is then returned to the solver. This cycle continues until the solver gives a “Give Solution” or “Give Up” decision” Yellow Highlight [Page 5](zotero://open-pdf/library/items/EGQXP2LK?page=5&annotation=Q36C2WHN)



Our self-reflection mechanism first identifies the reason why a user query remains unsolved. In instances where the solver opts to “Give Up”, the rationale provided by the solver is utilized. Conversely, if the solver proposes a solution but GPT-4 assesses that it does not adequately address the query, the reasoning ascribed by GPT-4 is employed” Yellow Highlight [Page 5](zotero://open-pdf/library/items/EGQXP2LK?page=5&annotation=IPD8WDIU)




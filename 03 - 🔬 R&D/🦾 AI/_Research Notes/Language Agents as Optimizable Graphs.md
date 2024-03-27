---
Publish Year: '2024'
Authors: "Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, Jürgen Schmidhuber"
URL: "http://arxiv.org/abs/2402.16823"
Zotero Link: "zotero://select/library/items/ZBWBYLA4"
tags:
  - "#Computer-Science---Artificial-Intelligence, #Computer-Science---Computation-and-Language, #Computer-Science---Machine-Learning, #Computer-Science---Multiagent-Systems, #graph"
Published:
---
# Summary

## Purpose
The research was initiated to address the complexity and inefficiency in multi-agent systems where several Large Language Models (LLMs) take on different roles to solve a given task. The study aims to unify language agent systems by describing them as optimizable computational graphs, thereby simplifying the engineering efforts required in defining prompting schemes and workflows of agents in the field of Artificial Intelligence.

## Methods
- Modeling language agents querying LLMs and utilizing external tools as computational graphs, where each node is dedicated to a specific function.
- Defining a swarm as a composite graph, where each subgraph represents a collaborative agent, to create a deeper hierarchy of intelligence.
- Developing optimization methods for nodes and edges within these graphs to enable automatic improvements of agent prompts and inter-agent orchestration.
- Employing the REINFORCE algorithm for edge optimization and an iterative process for node optimization based on previous input and task feedback.

## Key Findings
- The graph representation of language agents allows for the unification of language agent systems and simplifies the construction of arbitrary agent systems by recombining fundamental operations.
- Optimization of edges in a composite graph can effectively filter adversarial agents from a swarm, improving the overall system performance.
- Node optimization, particularly through the addition of demonstration examples in prompts, significantly increases the accuracy of agents in solving tasks.
- The framework was validated on various benchmarks, including MMLU, Mini CrossWords, HumanEval, and GAIA, demonstrating the benefits of automatic graph optimization.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on Artificial Intelligence, specifically in the development and efficiency of multi-agent systems. It suggests that the proposed framework not only simplifies the engineering efforts required in multi-agent systems but also significantly improves their performance through optimization techniques. The approach of describing language agent systems as optimizable computational graphs is a novel contribution that could pave the way for more efficient and effective multi-agent systems.

## Critiques
Upon evaluating the research, some critiques include:
- The generalizability of the findings to other types of multi-agent systems beyond those tested in the benchmarks.
- The computational complexity and resource requirements of the optimization processes, especially in large-scale applications.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Computation-and-Language
- #Computer-Science---Machine-Learning
- #Computer-Science---Multiagent-Systems
- #Graph

# Annotations
In multi-agent frameworks (Zeng et al., 2022; Zhuge et al., 2023), several LLMs take on different roles (Li et al., 2023; Park et al., 2023; Qian et al., 2023; Wu et al., 2023), to communicate in natural language and collectively solve a given task. This approach often outperforms single agents, exploiting the specialization (Hong et al., 2023) of various LLM agents.  Unfortunately, it also leads to increasingly different and disparate code bases that require a lot of human engineering to define prompting schemes and the workflow of agents.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/MRX2E58R?page=1&annotation=DRHLWMRJ)



In a “society of mind” (SOM) (Minsky, 1988; Zhuge et al., 2023), higher-level intelligence emerges from the combination of simpler and modular cognitive components. Inspired by SOMs, we describe language agent systems through graph representations.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/MRX2E58R?page=1&annotation=KIFBFQIH)



Language agents querying LLMs and utilizing external tools are modeled as computational graphs where each node is dedicated to a specific function, while the edges define a topology of how inputs are processed across nodes, mirroring the prompting schemes in prior studies” Yellow Highlight [Page 1](zotero://open-pdf/library/items/MRX2E58R?page=1&annotation=6VS8E2EL)



A swarm is defined as a composite graph, where each subgraph represents a collaborative agent. This creates a deeper hierarchy of intelligence. Agent graphs combine basic LLM operations (Kennedy, 2006; Nepusz & Vicsek, 2013), and swarm graphs contain subgraphs representing agents. Approaches such as COT (Wei et al., 2022), TOT (Yao et al., 2023), and Self-Consistency (Wang et al., 2022) can be represented by our graphs.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/MRX2E58R?page=1&annotation=HQPIPIJJ)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhugeLanguageAgentsOptimizable2024/image-2-x48-y445.png]]



The graph connectivity (adjacency matrices) between agents can self-improve online as a task is being solved or its solution is transferred to another task.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MRX2E58R?page=2&annotation=LWVK9VFG)



As a proof-of-concept, we demonstrate how suboptimal agent organization can be overcome and how existing prompting techniques, such as Tree of Thought and Reflexion, can be automatically recombined by optimizing edges in a composite graph. Apart from edge optimization, our framework allows each node in the graph to self-improve by adapting its prompts based on previous input and task feedback.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MRX2E58R?page=2&annotation=TC7P4IFP)



Our contributions can be summarized as follows: (1) We unify language agent systems by describing them as optimizable computational graphs.  (2) We introduce an open-source framework that allows for constructing arbitrary agent systems by recombining fundamental operations. We describe these engineeringlevel contributions in Appendix A.  (3) We develop optimization methods for nodes and edges, enabling automatic improvements of agent prompts and inter-agent orchestration.  (4) We validate our framework on various benchmarks including MMLU, Mini CrossWords, HumanEval, and GAIA, with an emphasis on the benefits of automatic graph optimization.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MRX2E58R?page=2&annotation=X7G8D4BJ)



Taking inspiration from the society of mind (SOM) (Minsky, 1988; Zhuge et al., 2023), we propose to organize intelligence within a modular and hierarchical framework. This framework consists of nodes, graphs, and composite graphs, with each component playing a specific role” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MRX2E58R?page=2&annotation=9MGN4FX4)



A node represents a fundamental operation that includes, but is not limited to, LLM inference, tool use, function calls, and various embodied actions.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MRX2E58R?page=2&annotation=AHIEMQCP)



An agent, conceptualized as a graph, consists of multiple nodes that form a coherent functional entity. A swarm, or composite graph, represents a complex system of agents where the collective capabilities of this system may exceed those of individual agents.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MRX2E58R?page=2&annotation=GVL6XD7S)



the edges within an agent define its execution topology, while the edges between agents establish collaboration and communication among them.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MRX2E58R?page=2&annotation=7SMUQ6C9)



In this paper, we focus on directed acyclic graphs (DAGs)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/MRX2E58R?page=2&annotation=W6M5SHQ2)



Algorithm 1 Graph Execution Require: Computational graph G = (N, E, F, o), input x, empty context z for each node without predecessors.  for n in TopologicalSort(N) do zn ← {fn(zv, x) : v ∈ pre(n)} end for Ensure: fo(zo, x)” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MRX2E58R?page=3&annotation=JQB5XBD5)



In the context of language agents, for example, the input x may correspond to a question in natural language. Each node processes the input x and context information z from its predecessor nodes by applying a computational routine f.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MRX2E58R?page=3&annotation=STK3C8BD)



In a swarm of language agents, the newly specified edges represent communication channels between agents.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MRX2E58R?page=3&annotation=HN7TVHDT)



Given a task τ and its associated utility function uτ that maps the candidate graphs to real numbers, we formulate an optimization problem about the choice of additional edges. The goal is to identify the edges that connect various language agents in a swarm, maximizing the utility. This process involves determining the most effective patterns of communication and information exchange among agents for the task at hand.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MRX2E58R?page=3&annotation=V3SW7AT7)



We further restrict the search space to only consider composite graphs that are DAGs.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MRX2E58R?page=3&annotation=45Z22RJG)



DAG optimization through pruning of nodes and edges was already present in the first work on “deep learning” with deep feedforward networks (Ivakhnenko et al., 1965; Ivakhnenko, 1968). Due to the combinatorial complexity induced by DAGs, recent studies have increasingly focused on the continuous optimization approach (Vowels et al., 2022). This is particularly relevant in scenarios where most node executions require one or more queries to LLMs for moderate-scale applications.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MRX2E58R?page=3&annotation=9M7VX2DA)



Formally, rather than solving the maximum utility function arg maxE uτ (GE ), we propose solving arg max θ∈Θ EG′∼Dθ [uτ (G′)], (1) where Dθ is a parameterized distribution and Θ represents a feasible set of real-valued parameters.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MRX2E58R?page=3&annotation=5AP3ENDH)



A sampling method that realizes this distribution is first to initialize a graph G′ ← (N, E). Then, iteratively sample” Yellow Highlight [Page 3](zotero://open-pdf/library/items/MRX2E58R?page=3&annotation=ESKDQZTS)



Language Agents as Optimizable Graphs whether to include edge ei in G′ for all i’s. If including ei causes a cycle in current G′, then the edge would not be included. Otherwise, add the edge to G′ with probability θi.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=WLMGH6KS)



To optimize the objective function (Equation (1)), we apply the REINFORCE algorithm (Williams, 1992) by applying a gradient ascent variant (e.g., Adam (Kingma & Ba, 2014)) with an unbiased gradient estimation: ∇θ EGE ∼Dθ [uτ (GE )] ≈ 1 M M X i=1 ˆ uτ (Gi)∇θ log(pθ(Gi)), (2) where G1, G2, . . . , GN ∼ Dθ are mutually independent and ˆ uτ (Gi) is an independent unbiased estimate of uτ (Gi) for all i and some M ∈ N. Algorithm 2 describes the optimization algorithm with vanilla gradient ascent.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=WS8PW9RQ)



Algorithm 2 Edge Optimization with REINFORCE Require: A parameterized probabilistic distribution over computation graphs Dθ, an unbiased utility estimator ˆ uτ (·), and a learning rate α. Initialize θ ∈ Rd. while terminate condition not met do Sample Gi ∼ Dθ for i = 1, 2, . . . , M . Update θ ← θ + α M PM i=1 ˆ uτ (Gi)∇θ log(pθ(Gi)). end while” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=6DHEBMLE)



In our framework, each node implements a fundamental operation, such as querying an LLM, using a tool, calling an API, etc. In a language agent, most of these operations involve prompting an LLM once or several times. Optimizing the prompts of these nodes is crucial for improving the system’s overall performance.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=MC24JEPH)



Unlike many other works on prompt optimization, which optimize a single global prompt (e.g., Yang et al., 2023; Pryzant et al., 2023; Deng et al., 2022), our node optimization problem naturally involves several operations where each of them consists of a node-level prompt.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=FWNYKLA5)



our graph representation leads to a separation of concerns where each node has a specific purpose with its own associated prompt.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=K3QNEN22)



existing prompt optimization methods, such as OPRO (Yang et al., 2023), can be described as a function I that iteratively maps a prompt, a function description, and a set of node input-output pairs (which may include annotations such as a quality measure for each pair) to an improved prompt.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=P74QDZLG)



our method begins by initializing an empty history set, denoted hn, one for each node n ∈ N . The process then proceeds iteratively: first, the graph GP (x) is executed using a randomly sampled input x following Algorithm 1. Subsequently, for each node, a tuple consisting of the input to the node (zn, x), where zn is the context vector that includes the outputs of the predecessor nodes, and the node’s own output f pn n (zn, x), is added to the node’s history hn.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=LLGBXW5N)



The final step involves updating the node prompts. This is done by applying I to the node’s updated history, its current prompt, and its function description, resulting in an improved prompt I(hn, pn, dn). This iterative process, described in Algorithm 3, continuously improves the operations of the nodes in the entire graph.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=7FAQY8SP)



Algorithm 3 Node Optimization Require: A parameterized graph GP = (N, E, F P , o), natural language function descriptions D = {dn}n∈N , and a distribution of inputs DX . Initialize pn for all n ∈ N . Initialize hn ← ∅ for all n ∈ N . while terminate condition not met do Sample input x ∼ DX . y ← GP (x) following Algorithm 1. hn ← hn ∪ {((zn, x), f pn n (zn, x))} for all n ∈ N . pn ← I(hn, pn, dn), for all n ∈ N . end while” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=WKSLXZ3K)



GPTSwarm, introduces a graph-based design of agents and swarms. This design further simplifies the reuse of modular components (nodes & agents) and the integration of such modules.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/MRX2E58R?page=4&annotation=CXC6SSCF)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhugeLanguageAgentsOptimizable2024/image-5-x52-y532.png]]



In our first experiments, we demonstrate that edge optimization effectively filters adversarial agents from a swarm, mirroring a scenario in multi-agent systems where some agents are detrimental rather than beneficial. Ideally, optimization would automatically eliminate harmful agents.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MRX2E58R?page=5&annotation=VSHTHKBA)



Our setup involves initializing a swarm consisting of k Input-Output (IO) agents and k adversarial agents, following the terminology by Besta et al. (2023). The IO agents query an LLM and relay the LLM’s responses directly. In contrast, adversarial agents are deliberately programmed to manipulate the LLM to provide incorrect answers. The collective decision on the final answer is made through majority voting, bypassing any additional LLM query that could introduce corrective intelligence against adversarial influence.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MRX2E58R?page=5&annotation=FZ6DUZSB)



In Figure 2, we present the comparative performance scores of different swarm configurations: the baseline, the graph formed by sequentially including edges that do not create loops (denoted as the ‘full graph’), a randomly connected swarm sampled from the initial distribution Dθ with θ = 0.5, and the optimized swarm.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MRX2E58R?page=5&annotation=Z9ULXQ3I)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhugeLanguageAgentsOptimizable2024/image-5-x307-y506.png]]



process uses REINFORCE (Alg. 2) over 200 iterations. Each iteration assesses four graph samples, each on a specific problem sourced from the MMLU dev set. Throughout these experiments, we employed GPT-4-Turbo, with the token sampling temperature fixed at 0.2. Figure 9 demonstrates how the optimized swarm score aligns asymptotically with that of the baseline.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MRX2E58R?page=5&annotation=SP4Q2CNP)



We conduct our evaluation on the Mini Crosswords dataset1. A subset of 20 problems is used to optimize and evaluate our methods, in agreement with previous studies (Yao et al., 2023; Sel et al., 2023). The choice of Mini Crosswords for this analysis is strategic, as it highlights how the algorithmic structure of the solvers, such as the tree search employed by TOT, significantly influences their performance (Yao et al., 2023). Our hypothesis is that edge connections can meaningfully determine the algorithmic structure.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MRX2E58R?page=5&annotation=YRBCVYX4)



The first agent, which implements the TOT approach, iteratively branches over candidate solutions provided by an LLM, processing one word at each step.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MRX2E58R?page=5&annotation=R94T547M)



The second agent is based on the Reflexion method (Shinn et al., 2023). This agent first proposes a solution through a greedy approach and then creates an al1https://www.goobix.com/crosswords” Yellow Highlight [Page 5](zotero://open-pdf/library/items/MRX2E58R?page=5&annotation=52XAU28X)



Language Agents as Optimizable Graphs ternative solution informed by feedback from a critic, which is based on an LLM analysis of the initial solution.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/MRX2E58R?page=6&annotation=DTY8T26B)



The third agent we examine is a Chain of Thought (COT) agent consisting of three nodes. Each node within the COT performs an internal brute-force search to select the optimal subset of candidates generated by the LLM for the current state, scored by the LLM. The agent or swarm then returns all the solutions generated by their output node.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/MRX2E58R?page=6&annotation=QBN48UWU)



Figure 3 visualizes the evolution of probability parameters in the form of adjacency-like matrices over ten iterations. We observe that the parameters first change chaotically. However, after iteration 6, the parameters change almost monotonically.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/MRX2E58R?page=6&annotation=SUIFAWNG)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhugeLanguageAgentsOptimizable2024/image-6-x301-y499.png]]



It achieves an accuracy of 0.800(±0.0616), significantly exceeding the previous state-of-the-art performance of 0.675 (Yao et al., 2023). All reported metrics are summarized in Figure 4.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/MRX2E58R?page=6&annotation=HTHTAZWD)



In this section, we optimize the prompts of a ReAct-style (Yao et al., 2022) agent. The agent first generates a Python program in response to a given question. If the generated program passes all test cases included in the problem statement, then the program is returned. Otherwise, the agent regenerates a program based on the execution feedback. We experiment with two node-level optimization strategies: (1) modifying the instruction prompts and (2) adding demonstration examples to the prompts.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/MRX2E58R?page=6&annotation=ESMWVJW7)



Altering the instruction prompts rarely improved the results, possibly due to the limited sophistication of our current meta-prompts compared to OPRO (Yang et al., 2023) and PromptBreeder (Fernando et al., 2023).” Yellow Highlight [Page 6](zotero://open-pdf/library/items/MRX2E58R?page=6&annotation=BSWM36UD)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhugeLanguageAgentsOptimizable2024/image-7-x50-y532.png]]



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhugeLanguageAgentsOptimizable2024/image-7-x52-y350.png]]



as demonstration examples in the context of the nodes, increases the pass@1 accuracy from 77% to 89%” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MRX2E58R?page=7&annotation=DMBSTAEP)



GAIA is a benchmark specifically designed for testing the generality of AI assistants focusing on realworld questions (Mialon et al., 2023)” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MRX2E58R?page=7&annotation=RG9JE7ZI)



Using this benchmark, we evaluate the general applicability of our framework. We construct swarms with multiple agents of the same type and employ self-consistency (a prompt-based majority vote) for the final decision (Wang et al., 2022).” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MRX2E58R?page=7&annotation=G64BSV5G)



prompt-based self-consistency yields the best performance.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MRX2E58R?page=7&annotation=86IC2GLP)



Table 1 shows the results of our swarm with seven TOT agents and the self-consistency strategy for the final decision. We compare the performance of the GPT-Series (Achiam et al., 2023) with plugins and AutoGPT (Torantulino et al., 2023) performance as reported by Mialon et al. (2023). Our methods significantly outperform these baselines.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MRX2E58R?page=7&annotation=AKEW2ADS)



Our observations indicate that the time requirement of a swarm grows approximately linearly with the number of agents. Despite the increased computational time, incorporating more agents notably improves the overall performance of the system.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MRX2E58R?page=7&annotation=JVSL55H6)



a greater variety of node operations leads to better performance.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MRX2E58R?page=7&annotation=ZN4659PU)



we believe that enhancing web capabilities would further increase performance significantly.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MRX2E58R?page=7&annotation=2XIDWVEH)



In the space of LLM-based multiagent systems (Xie et al., 2023; Chen et al., 2023a;b), NLSOMs (Zhuge et al., 2023) employ various social structures for task-specific applications (inspired by SOMs (Minsky, 1988)),” Yellow Highlight [Page 7](zotero://open-pdf/library/items/MRX2E58R?page=7&annotation=UITPRX79)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/zhugeLanguageAgentsOptimizable2024/image-8-x50-y484.png]]



Besta et al. (2023) introduced LLM-based problem-solving with graphs; however, the approach only encompasses LLM prompting schemes without modeling other fundamental capabilities of language agents, such as use of external tools.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/MRX2E58R?page=8&annotation=SG2TCBDQ)



Unlike previous studies, our approach emphasizes the development of hierarchical intelligence, as discussed by Minsky (1988) and Kennedy (2006), through the construction of agent graphs and the composition of multiple graphs into swarms.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/MRX2E58R?page=8&annotation=2LG8JHG7)



at the edge level, we demonstrate the application of the REINFORCE algorithm (Williams, 1992) to optimize the potential connections between nodes.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/MRX2E58R?page=8&annotation=LR2F4G2C)



imilarly to our work, DSPy (Khattab et al., 2023) implements LLM pipelines as computational graphs with modular LLM queries as nodes, parameterized by prompts and neural network weights. It proposes a two-stage process to optimize the parameters of these nodes. Initially, it generates a set of candidate solutions for each node. Subsequently, it optimizes across the Cartesian product of these candidate solution sets, aiming to identify an effective combination of parameters for the entire graph.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/MRX2E58R?page=8&annotation=JPCNMEYB)



we propose an iterative optimization process. By virtue of decomposing a” Yellow Highlight [Page 8](zotero://open-pdf/library/items/MRX2E58R?page=8&annotation=YKSCULCK)



Language Agents as Optimizable Graphs solution into nodes with expected functions, at each iteration, we improve each node individually, conditioned on the execution history of the graph with the current prompts of each node.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/MRX2E58R?page=9&annotation=JGPUGJTN)




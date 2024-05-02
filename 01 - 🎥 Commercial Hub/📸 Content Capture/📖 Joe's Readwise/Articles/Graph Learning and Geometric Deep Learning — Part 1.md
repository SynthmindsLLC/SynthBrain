# Graph Learning and Geometric Deep Learning — Part 1

![rw-book-cover](https://miro.medium.com/max/1200/0*m7555FzS-X2sHcqT.jpg)

## Metadata
- Author: [[Flawnson Tong]]
- Date: 2020-11-21
- Full Title: Graph Learning and Geometric Deep Learning — Part 1
- Category: #articles
- Summary: Graph embedding techniques transform graphs into lower-dimensional spaces for machine learning, preserving structure and information. Different methods like DeepWalk, Node2vec, and SDNE use various approaches to embed graphs efficiently. These techniques are essential for optimizing proximity and simplifying complex graph structures for machine learning tasks.
- URL: https://towardsdatascience.com/overview-of-deep-learning-on-graph-embeddings-4305c10ad4a4

## Highlights
- [**DeepWalk —** Perozzi et al](https://arxiv.org/pdf/1403.6652.pdf)
  Deepwalk isn’t the first of it’s kind, but it is one of the first approaches that have been widely used as a benchmark in comparison with other graph learning approaches. Deepwalk belongs to the family of graph embedding techniques that uses walks, which are a concept in graph theory that enables the **traversal of a graph by moving from one node to another, as long as they are connected to a common edge.** ([View Highlight](https://read.readwise.io/read/01hwva6f9man3atj3ymz936pwg))
- Basically, you can use the truncated steps of graph traversals as input for an RNN. This is analogous to the way word vectors in a sentence are put together. ([View Highlight](https://read.readwise.io/read/01hwva781m1mwjw83z05md4dvs))
- The goal is to estimate the likelihood of observing node ***vi*** given all the previous nodes visited so far in the random walk, where ***Pr()*** is probability, Φ is a mapping function that represents the latent representation associated with each node **v** in the graph. ([View Highlight](https://read.readwise.io/read/01hwva7m3j2mqfvv0jpsyf2d9d))
- The method used to make predictions is **skip-gram**, just like in Word2vec architecture for text. Instead of running along the text corpus, DeepWalk runs along the graph to learn an embedding. ([View Highlight](https://read.readwise.io/read/01hwva891xw605zbpsybnmvf1n))
- The model can take a target node to predict it’s “context”, which in the case of a graph, means it’s connectivity, structural role, and node features. ([View Highlight](https://read.readwise.io/read/01hwva8h5nr69y285v9111qjrx))
- this approach is **transductive**, meaning whenever a new node is added, the model must be retrained to embed and learn from the new node. ([View Highlight](https://read.readwise.io/read/01hwva8z2x9jz2jf8c2ffv28pq))
- [**Node2vec — Grover et al**](https://cs.stanford.edu/people/jure/pubs/node2vec-kdd16.pdf)
  You’ve heard of Word2vec now prepare for… Node2vec ( [Aditya Grover](https://medium.com/u/b83b72c7aef4?source=post_page-----4305c10ad4a4--------------------------------) et al) ([View Highlight](https://read.readwise.io/read/01hwva98asdpba0awgc72rx1rf))
- If you turn each node in a graph into an embedding as you would words in sentence, a neural network can learn representations for each node. ([View Highlight](https://read.readwise.io/read/01hwva9sg1n6kcregtkhz4374e))
- Node2vec features a walk bias variable α, which is parameterized by *p* and *q*. The parameter *p* prioritizes a breadth-first-search (BFS) procedure, while the parameter *q* prioritizes a depth-first-search (DFS) procedure. ([View Highlight](https://read.readwise.io/read/01hwvaa79fks16aggdata5hds2))
- As the visualization implies, **BFS is ideal for learning local neighbors, while DFS is better for learning global variables.** Node2vec can switch to and from the two priorities depending on the task. ([View Highlight](https://read.readwise.io/read/01hwvaakrgqca235d3xwcen3dg))
- **BFS is better at classifying according to structural roles (hubs, bridges, outliers, etc.) while DFS returns a more community driven classification scheme.**
  Node2vec is one of the many graph learning project that have come out of [Stanford’s SNAP](http://snap.stanford.edu/index.html) research group dedicated to graph analytics. ([View Highlight](https://read.readwise.io/read/01hwvabbb7w0dmwz6y1h723ntc))
- [Graph2vec — Narayanan et al](https://arxiv.org/abs/1707.05005)
  A modification to the node2vec variant, graph2vec essentially learns to embed a graph’s sub-graphs. ([View Highlight](https://read.readwise.io/read/01hwvabrm7h50v34asg2470k3j))
- this equation can be written as: the probability of the word (**wj**) appearing in context given document (**d**) equals the exponential of the document embedding matrix (***d~***) multiplied by the word embedding matrix (***w~j*** is sampled from the document), divided by the sum of all the exponentials of the document embedding matrix multiplied by the word embedding matrix for each word in the vocab list (**V**) across all documents. ([View Highlight](https://read.readwise.io/read/01hwvacjtjtyx6rej5g14t3xp1))
- if a document is made of sentences (which is then made of words), then a graph is made of sub-graphs (which is then made of nodes). ([View Highlight](https://read.readwise.io/read/01hwvacvwbh68fz18tn2dzh9h1))
- [**Structural Deep Network embedding (SDNE) — Wang et al**](https://www.kdd.org/kdd2016/papers/files/rfp0191-wangAemb.pdf)
  Unlike the previous embedding techniques, SDNE does not use random walks. Instead, it tries to learn from two distinct metrics:
  • **First-order proximity:** two nodes are considered similar if they share an edge (pairwise similarity)
  • **Second-order proximity:** two nodes are considered similar if they share many neighboring/adjacent nodes ([View Highlight](https://read.readwise.io/read/01hwvadh2s71wsvbw7h4260913))
- Laplacian Eigenmap embedding algorithm **applies a penalty when similar nodes are mapped far from each other in the embedded space**, thus allowing for optimization by minimizing the space between similar nodes. ([View Highlight](https://read.readwise.io/read/01hwvaeawgpmf111qv304x9ayp))
- [Hierarchical Representation Learning for Networks — Chen et al](https://arxiv.org/abs/1706.07845)
  HARP is an improvement to the previously mentioned embedding/walking based models. Previous models risked getting stuck in local optima since their objective functions are non-convex. Basically this means, the ball can’t roll to the absolute bottom of the hill.
  ![](https://miro.medium.com/max/463/0*IoSNj7SCD2rZn95c) ([View Highlight](https://read.readwise.io/read/01hwvag6tp24ckb8m4ft6twydb))
- HARP is essentially a **graph-preprocessing step that simplifies the graph** to make for faster training. ([View Highlight](https://read.readwise.io/read/01hwvagp50hzkxdyn54r8nbegt))

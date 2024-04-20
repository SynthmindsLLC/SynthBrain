# Graphormer

![rw-book-cover](https://huggingface.co/front/thumbnails/docs/transformers.png)

## Metadata
- Author: [[huggingface.co]]
- Date: None
- Full Title: Graphormer
- Category: #articles
- Summary: The Graphormer model is a modified Graph Transformer designed for graph representation tasks, achieving excellent results on various challenges. It effectively encodes structural information of graphs into the model, outperforming traditional GNN variants. However, it may struggle on large graphs due to memory constraints beyond 100 nodes/edges.
- URL: https://huggingface.co/docs/transformers/model_doc/graphormer

## Highlights
- The Graphormer model was proposed in [Do Transformers Really Perform Bad for Graph Representation?](https://arxiv.org/abs/2106.05234) ([View Highlight](https://read.readwise.io/read/01hvaadmj0358v978t5mzdt139))
- It is a Graph Transformer model, modified to allow computations on graphs instead of text sequences by generating embeddings and features of interest during preprocessing and collation, then using a modified attention. ([View Highlight](https://read.readwise.io/read/01hvaadt7ra8aqaray7pv92f5c))
- This model will not work well on large graphs (more than 100 nodes/edges), as it will make the memory explode. You can reduce the batch size, increase your RAM, or decrease the `UNREACHABLE_NODE_DISTANCE` parameter in algos_graphormer.pyx, but it will be hard to go above 700 nodes/edges. ([View Highlight](https://read.readwise.io/read/01hvaae4p5jkaepncpww9atmst))
- This model does not use a tokenizer, but instead a special collator during training. ([View Highlight](https://read.readwise.io/read/01hvaaem3cve1h2z39vrjecafh))

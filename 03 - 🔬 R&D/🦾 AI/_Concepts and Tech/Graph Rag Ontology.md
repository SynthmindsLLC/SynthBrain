---
title: "Standardized Graph Network Ontology for Tagging in Obsidian YAML Front Matter"
description: "A proposal for a standardized ontology and tagging system using YAML front matter in Obsidian notes to enable rich graph network visualization and querying."
type: "concept"
tags: ["#obsidian", "#yaml", "#ontology", "#tagging", "#graphnetwork"]
relationships:
- "#related_to [[Obsidian Notes]]"
- "#developed_by [[Author's Name]]"
date: "2024-06-09"
---

To create a standardized graph network ontology for tagging notes using YAML front matter in Obsidian:

## Define the Ontology
- Determine the key concepts, entities and relationships you want to capture
- Organize these into a hierarchy or taxonomy 
- Use clear, concise names for each ontology term
- Document definitions and usage guidelines for each term

## Implement in YAML Front Matter
- Use the ontology terms as YAML keys
- Enclose ontology values in double quotes and square brackets to enable wikilinks:
```yaml
topics: ["[[Topic 1]]", "[[Topic 2]]"] 
```
- Use a consistent indentation and list format

## Update Obsidian Settings
- Enable the "Parse YAML front matter tags" option in Obsidian settings
- This will allow Obsidian to index the YAML tags and include them in graph view and search

## Use the Ontology Tags
- Apply the standardized ontology tags to your notes in the YAML front matter
- Use the tags for filtering and querying notes using Obsidian search and plugins like Dataview
- The ontology will provide a consistent structure for organizing notes and visualizing connections in graph view

## Iterate and Refine
- As you use the ontology, assess what works well and what needs improvement
- Evolve the ontology terms and relationships over time as needed
- Keep documentation updated as the ontology changes

## List of Relevant Backlinks
- [[Wikilinks in YAML front matter]]
- [[Add support for link types]]
- [[Customize Graph node appearance via YAML frontmatter]]
- [[Tags in the era of YAML front matter abundance]]
- [[Ontologies and tag-statistics]]

By defining a standardized tagging ontology and implementing it consistently using YAML front matter across your Obsidian notes, you can unlock powerful ways to organize, visualize and query your knowledge graph. The key is developing a well-structured ontology, using wikilinks within the YAML to connect entities, and keeping usage consistent. This will allow Obsidian's graph view and search capabilities to leverage the semantic relationships you've defined.

Citations:
[1] https://forum.obsidian.md/t/wikilinks-in-yaml-front-matter/10052
[2] https://forum.obsidian.md/t/add-support-for-link-types/6994
[3] https://link.springer.com/article/10.1007/s40595-014-0033-6
[4] https://forum.obsidian.md/t/frontmatter-tags-with-graph-view/27794
[5] https://forum.obsidian.md/t/customize-graph-node-appearance-via-yaml-frontmatter/5402
[6] https://iopscience.iop.org/article/10.1088/1367-2630/14/5/053009/pdf
[7] https://forum.obsidian.md/t/using-specific-yaml-tags-to-link-notes-in-graph-view/25442
[8] https://forum.obsidian.md/t/add-support-for-link-types/6994/21?u=achamess
[9] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7250628/
[10] https://forum.obsidian.md/t/tags-in-the-era-of-yaml-front-matter-abundance/18328
[11] https://forum.obsidian.md/t/frontmatter-link-in-the-graph/39851
[12] https://stackoverflow.com/questions/68398040/when-to-use-graph-databases-ontologies-and-knowledge-graphs
[13] https://forum.obsidian.md/t/tags-in-front-matter-dataview-and-search-confused/38988
[14] https://www.reddit.com/r/ObsidianMD/comments/1cutjqn/two_types_of_links_strong_and_weak_or_core_and/
[15] https://www.ontotext.com/knowledgehub/fundamentals/what-is-a-knowledge-graph/
[16] https://www.reddit.com/r/ObsidianMD/comments/vwchw2/yaml_tags_vs_normal_tags_in_obsidian/
[17] https://www.reddit.com/r/ObsidianMD/comments/znctl7/how_to_correctly_use_the_yaml_front_matter/
[18] https://community.openai.com/t/what-ontology-rag-and-graph-data-do-you-use-to-develop-intelligent-assistants/787860
[19] https://forum.obsidian.md/t/include-show-note-links-in-yaml-frontmatter-v0-8-5/4673
[20] https://www.reddit.com/r/ObsidianMD/comments/oaor0b/how_do_you_tag_your_notes/
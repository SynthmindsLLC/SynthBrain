---
title: "Cache Eviction Algorithms"
description: "Strategies used to manage data in a cache, particularly when the cache reaches its capacity and needs to make room for new data. These algorithms determine which cached items should be removed to accommodate new entries. The choice of eviction algorithm can significantly impact the performance of caching systems, such as databases and web servers."
type: "concept"
tags:
- "CacheEviction"
- "Algorithms"
- "ComputerScience"
- "MemoryManagement"
relationships:
- "#related_to [[Database Systems]]"
- "#related_to [[Web Servers]]"
birthdate: "N/A"
deathdate: "N/A"
---

## Cache Eviction Algorithms

Cache eviction algorithms are strategies used to manage data in a cache, particularly when the cache reaches its capacity and needs to make room for new data. These algorithms determine which cached items should be removed to accommodate new entries. The choice of eviction algorithm can significantly impact the performance of caching systems, such as databases and web servers[1][4][7][10][16][18].

### Common Cache Eviction Algorithms

- **[[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Least Recently Used (LRU)]]**: Evicts the least recently accessed items. It is based on the assumption that items not accessed recently are less likely to be accessed in the near future[1][4][7][10].
- **[[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/First-In, First-Out (FIFO)]]**: Evicts the oldest items in the cache, regardless of their access patterns. It is simple but may not perform well with certain access patterns[1][6][7][9][10].
- **[[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Least Frequently Used (LFU)]]**: Removes items that have been accessed the least frequently, under the assumption that less frequently accessed items are less likely to be needed again[1][4][7][10].
- **[[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Random Eviction]]**: Randomly selects an item to evict. This method is simple and can perform surprisingly well in certain scenarios, despite not considering access patterns[2][7][8][18].
- **[[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Most Recently Used (MRU)]]**: Opposite of LRU, it evicts the most recently used items. It can be useful in scenarios where the most recent items are less likely to be accessed again soon[4].
- **[[Synthbrain/03 - 🔬 R&D/🧮Math & Comp Sci/Concepts/Optimal Page Replacement (OPR)]]**: Evicts the page that will not be needed for the longest time in the future. It is theoretical and cannot be implemented without future knowledge[3][12][15][19][20].

### Factors Influencing Choice of Eviction Algorithm

- **Access Patterns**: The algorithm should match the data access patterns of the application to minimize cache misses[4][7][8].
- **System Resources**: The computational overhead and memory usage of the algorithm should be appropriate for the available system resources[7][8].
- **Performance Goals**: The algorithm should align with the performance goals, such as maximizing hit rates or minimizing latency[7][10][11].

### Conclusion

Selecting the right cache eviction algorithm is crucial for optimizing cache performance. While LRU and LFU are commonly used due to their balance between simplicity and effectiveness, other algorithms like FIFO and Random Eviction can be better suited for specific scenarios or system constraints[1][4][7][10][16][18].

- [[Cache Management]]
- [[Memory Management]]
- [[Operating Systems]]

Sources
[1] Cache Eviction Algorithms - Ehcache https://www.ehcache.org/documentation/2.8/apis/cache-eviction-algorithms.html
[2] Caches: LRU v. random - Dan Luu https://danluu.com/2choices-eviction/
[3] Optimal Page Replacement Algorithm - GeeksforGeeks https://www.geeksforgeeks.org/optimal-page-replacement-algorithm/
[4] Cache Eviction Policies - Codecademy https://www.codecademy.com/article/cache-eviction-policies
[5] LRU vs FIFO vs Random - algorithm - Stack Overflow https://stackoverflow.com/questions/6930899/lru-vs-fifo-vs-random
[6] Page Replacement Algorithms in Operating Systems - GeeksforGeeks https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/
[7] Cache replacement policies - Wikipedia https://en.wikipedia.org/wiki/Cache_replacement_policies
[8] When Are Randomized Algorithms Better Than LRU? (2014) https://news.ycombinator.com/item?id=19188642
[9] Page Replacement Algorithms in Operating Systems (OS) - Javatpoint https://www.javatpoint.com/os-page-replacement-algorithms
[10] Unlocking Efficiency: Exploring Cache Eviction Policies and Their Types - LinkedIn https://www.linkedin.com/pulse/unlocking-efficiency-exploring-cache-eviction-policies-baligh-mehrez
[11] [PDF] It's Time to Revisit LRU vs. FIFO - USENIX https://www.usenix.org/system/files/hotstorage20_paper_eytan.pdf
[12] What breaks a tie in Optimal Page Replacement? - Stack Overflow https://stackoverflow.com/questions/71945761/what-breaks-a-tie-in-optimal-page-replacement
[13] Researchers Design Simple, High-Performing Cache Eviction Algorithm https://www.cs.cmu.edu/news/2023/cache-eviction
[14] FIFO is Better than LRU: the Power of Lazy Promotion and Quick Demotion https://blog.jasony.me/system/cache/2023/06/24/fifo-lru
[15] Does optimal page replacement cause the same number of faults for ... https://cs.stackexchange.com/questions/151801/does-optimal-page-replacement-cause-the-same-number-of-faults-for-the-reverse-st
[16] Cache Eviction Strategies Every Redis Developer Should Know https://redis.com/blog/cache-eviction-strategies/
[17] Optimal Page Replacement Algorithm | Scaler Topics https://www.scaler.com/topics/optimal-page-replacement-algorithm/
[18] Brief Summary of Cache Modes & Cache Eviction Algorithms - Guanzhou Hu https://www.josehu.com/technical/2020/08/07/cache-eviction-algorithms.html
[19] Page Replacement Algorithms in Operating Systems (OS) | Core CS https://workat.tech/core-cs/tutorial/page-replacement-algorithms-in-operating-system-os-q0pioxh7iym5
[20] Page replacement Algorithms | OPTIMAL | Example | OS - YouTube https://youtube.com/watch?v=jeJIKKQcqpU

By Perplexity at https://www.perplexity.ai/search/First-in-first-7cmiTBbTR1iVl7J2sw6zHA
---
Date: [[2024-03-06]]
Tags: 
 - "#computer_networking"
 - "#interrupt_coalescing"
 - "#hardware_interrupts"
 - "#network_performance"
---

Interrupt coalescing, also known as interrupt moderation, is a network performance optimization technique where events that would normally trigger hardware interrupts are temporarily held back. This can be done until a certain amount of work is pending or a timeout timer triggers. The primary goal of interrupt coalescing is to reduce the number of interrupts that a CPU must handle, which can significantly lower the processing overhead and improve system performance[1][3][6].

This technique is particularly useful in high-speed networks where the rate of incoming packets is very high, such as in Gigabit Ethernet environments. Without interrupt coalescing, each packet would generate an interrupt, potentially leading to a situation known as receive livelock, where the CPU becomes so busy handling interrupts that it cannot process the actual data[3][7].

Interrupt coalescing can be implemented in hardware, often combined with a hardware FIFO or direct memory access (DMA), or in software by disabling interrupts in the interrupt controller and using timer-based polling[1][17]. It is a common feature in modern network cards and has been used since the early days of computing, dating back to devices like the 16550 UART chip[1].

While interrupt coalescing can greatly improve throughput by batching the processing of multiple packets, it may introduce a small latency penalty. Therefore, the technique must be carefully configured to balance the trade-off between throughput and latency. Parameters such as the maximum number of interrupts per second and the delay between packet arrival and interrupt generation can be adjusted to optimize performance[3][13].

- Important [[wikilinks]]:
  - [[Hardware Interrupts]]
  - [[Network Performance Optimization]]
  - [[Receive Livelock]]
  - [[Direct Memory Access (DMA)]]

Sources
[1] Interrupt coalescing - Wikipedia https://en.wikipedia.org/wiki/Interrupt_coalescing
[2] Performance doubling with message coalescing | Datastax https://www.datastax.com/blog/performance-doubling-message-coalescing
[3] [PDF] Effects of Interrupt Coalescence on Network Measurements * https://sites.cc.gatech.edu/fac/Constantinos.Dovrolis/Papers/intcoal_pam04.pdf
[4] What are the advantages NAPI before the IRQ Coalesce? - Server Fault https://serverfault.com/questions/662673/what-are-the-advantages-napi-before-the-irq-coalesce
[5] Interrupt coalescing - IBM https://www.ibm.com/docs/en/aix/7.1?topic=options-interrupt-coalescing
[6] What is packet coalescing? | Definition from TechTarget https://www.techtarget.com/whatis/definition/packet-coalescing
[7] (PDF) Analysis of interrupt coalescing schemes for receive-livelock ... https://www.academia.edu/2767216/Analysis_of_interrupt_coalescing_schemes_for_receive_livelock_problem_in_gigabit_ethernet_network_hosts
[8] Interrupt Coalescence - eduPERT KB - GÉANT federated confluence https://wiki.geant.org/display/EK/Interrupt%2BCoalescence
[9] What is Interrupt Coalescing? - Culttt https://culttt.com/2022/08/16/what-is-interrupt-coalescing
[10] What are the advantages NAPI before the IRQ Coalesce? - Stack Overflow https://stackoverflow.com/questions/28090086/what-are-the-advantages-napi-before-the-irq-coalesce
[11] [PDF] Dynamic EEE Coalescing: Techniques and Bounds - arXiv https://arxiv.org/pdf/1901.03215.pdf
[12] HPE 3PAR Interrupt Coalescing - ByteSizedAlex https://www.bytesizedalex.com/hpe-3par-interrupt-coalescing/
[13] What Do the Linux "ethtool" Interrupt Coalescing Values Mean? - Search - Informatica https://knowledge.informatica.com/s/article/80204?nocache=https%3A%2F%2Fknowledge.informatica.com%2Fs%2Farticle%2F80204
[14] [PDF] Best Practices for Performance Tuning of Latency-Sensitive Workloads in vSphere VMs - VMware https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/techpaper/vmw-tuning-latency-sensitive-workloads-white-paper.pdf
[15] How to achieve low latency with 10Gbps Ethernet https://blog.cloudflare.com/how-to-achieve-low-latency/
[16] Virtual Network Interrupt Coalescing - VMware Docs https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/vmc-aws-performance/GUID-E1BD6A18-02F3-4CF8-A77B-A45E7C48EB93.html
[17] Modern High-Speed Networking Techniques in Hardware and Software - LinkedIn https://www.linkedin.com/pulse/modern-high-speed-networking-techniques-hardware-john-velegrakis
[18] Interrupt Coalescence - Stack Overflow https://stackoverflow.com/questions/12480842/interrupt-coalescence
[19] [PDF] Optimizing Storage Performance with Calibrated Interrupts - USENIX https://www.usenix.org/system/files/osdi21-tai.pdf
[20] [PDF] vIC: Interrupt Coalescing for Virtual Machine Storage Device IO - USENIX https://www.usenix.org/legacy/event/atc11/tech/final_files/Ahmad.pdf
[21] Improving Performance on vSphere | Geode Docs https://geode.apache.org/docs/guide/114/managing/monitor_tune/performance_on_vsphere.html
[22] How to reduce latency in Windows by disabling the Interrupt coalescing - RTI Community https://community.rti.com/kb/how-reduce-latency-windows-disabling-interrupt-coalescing

By Perplexity at https://www.perplexity.ai/search/Correlated-equilibrium-O2a5mFcnSB6EMaEFN7s1bQ
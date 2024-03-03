---
Date: [[2024-03-02]]
Tags: 
 - "#FCFS"
 - "#CPUScheduling"
 - "#OperatingSystems"
 - "#ProcessManagement"
---

## First Come First Serve (FCFS) CPU Scheduling

**First Come First Serve (FCFS)**, also known as[[First-In, First-Out (FIFO)]], is the simplest te of CPU scheduling algorithm that schedules according to the arrival times of various processes. The core principle of FCFS scheduling is straightforward: the process that requests the CPU first is allocated the CPU first. This is implemented using a FIFO queue, where the [[Process Control Block (PCB) ]]of a process is linked to the tail of the queue when it enters the ready queue. The CPU is then allocated to the process at the head of the queue when the CPU becomes free, and the running process is removed from the queue once it is completed[1][3][4][5].

### Characteristics
- **Non-Preemptive**: Once a process is allocated the CPU, it runs to completion without being preempted by other processes[1][3][4].
- **Simple Implementation**: FCFS is easy to implement and understand, using a basic FIFO queue to manage processes[1][2][3].
- **Fairness**: It treats all processes equally, providing each process an equal opportunity to run[2].

### Advantages
- **Simplicity**: FCFS is straightforward to implement and use, making it an ideal choice for simple systems[2][7].
- **Low Scheduling Overhead**: It does not involve complex scheduling decisions or frequent context switches[2].
- **Guaranteed Execution**: Every process will eventually get a chance to execute as long as the system has enough resources[2].

### Disadvantages
- **Convoy Effect**: Short processes may get stuck waiting behind long processes, leading to inefficient CPU and device utilization[2][4][7].
- **High Average Waiting Time**: Processes, especially short ones, may experience long waiting times if a process with a large burst time is executing[1][2][4].
- **Poor Performance for Time-Sharing Systems**: FCFS is not suitable for systems where processes should get the CPU at regular intervals[2].

### Real-Life Example
A real-life analogy of FCFS scheduling is the queue at a ticket counter where the person who arrives first gets served first[7].

### Conclusion
While FCFS is the most basic and easy-to-understand CPU scheduling algorithm, its simplicity comes at the cost of efficiency, particularly in systems with diverse process burst times. The algorithm's fairness and low overhead make it suitable for systems with simple scheduling needs, but its disadvantages often outweigh its benefits in more complex or time-sensitive environments[1][2][3][4][7].

- [[CPU Scheduling]]
- [[Operating Systems]]
- [[Process Management]]

Sources
[1] First Come First Serve – CPU Scheduling (Non-Preemptive) https://www.geeksforgeeks.org/first-come-first-serve-cpu-scheduling-non-preemptive/
[2] Advantages and Disadvantages of various CPU scheduling algorithms https://www.geeksforgeeks.org/advantages-and-disadvantages-of-various-cpu-scheduling-algorithms/
[3] First-come, first-served (FCFS) scheduling algorithm - Educative.io https://www.educative.io/answers/first-come-first-served-fcfs-scheduling-algorithm
[4] FCFS Scheduling Algorithms in OS (Operating System) - Javatpoint https://www.javatpoint.com/os-fcfs-scheduling
[5] FCFS Scheduling in OS - DataFlair https://data-flair.training/blogs/fcfs-scheduling-in-os/
[6] First Come First Serve | CPU Scheduling - Gate Vidyalay https://www.gatevidyalay.com/first-come-first-serve-cpu-scheduling/
[7] FCFS Scheduling Algorithm: What is, Example Program - Guru99 https://www.guru99.com/fcfs-scheduling.html
[8] Advantages and Disadvantages of various Disk scheduling algorithms https://www.geeksforgeeks.org/advantages-and-disadvantages-of-various-disk-scheduling-algorithms/
[9] Program for FCFS CPU Scheduling | Set 1 - GeeksforGeeks https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-1/
[10] Advantages & disadvantages of FCFS Scheduling Algorithm - YouTube https://youtube.com/watch?v=y4_PCWofYnQ
[11] First Come First Serve(FCFS) Scheduling Algorithm - Studytonight https://www.studytonight.com/operating-system/first-come-first-serve
[12] [PDF] Strategy Description Advantages Disadvantages - LASS https://lass.cs.umass.edu/~shenoy/courses/fall14/discussions/discussion3/concepts.pdf
[13] First Come First Serve (FCFS) Scheduling - Scaler Topics https://www.scaler.com/topics/first-come-first-serve/
[14] FCFS SCHEDULING ALGORITHM - CONVOY EFFECTS - YouTube https://youtube.com/watch?v=vUCB7vuNBZI
[15] FCFS Scheduling - Tutorialspoint https://www.tutorialspoint.com/fcfs-scheduling
[16] Operating System Design/Scheduling Processes/FCFS - Wikibooks https://en.wikibooks.org/wiki/Operating_System_Design/Scheduling_Processes/FCFS
[17] FCFS Scheduling Algorithm in OS | Easy Explaination - YouTube https://youtube.com/watch?v=vlc0Ea4ID9s

By Perplexity at https://www.perplexity.ai/search/First-in-first-7cmiTBbTR1iVl7J2sw6zHA
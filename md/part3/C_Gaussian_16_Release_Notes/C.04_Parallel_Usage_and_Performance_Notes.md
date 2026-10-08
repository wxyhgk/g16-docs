### C.4 Parallel Usage and Performance Notes

#### C.4.1 Shared-memory parallelism

**Memory allocation.** Calculations involving larger molecules and basis sets benefit from larger memory allocations. 4 GB or more per processor is recommended for calculations involving 50 or more atoms and/or 500 or more basis functions. The freqmem utility estimates the optimal memory size per thread for groundstate frequency calculations, and the same value is reasonable for excited-state frequencies and is more than sufficient for ground and excited state optimizations.

The amount of memory allowed should rise with the number of processors: if 4 GB is reasonable for one processor, then the same job using 8 CPUs would run well in 32 GB. Of course, there may be limitations to smaller values imposed by the particular hardware, but scaling memory linearly with number of CPUs should be the goal. In particular, increasing only the number of CPUs with fixed memory size is unlikely to lead to good performance when using large numbers of processors.

For large frequency calculations and for large CCSD and EOM-CCSD energies, it is also desirable to leave enough memory to buffer the large disk files involved. Therefore, a Gaussian job should only be given 50-70% of the total memory on the system. For example, on a machine with a total of 128 GB, one should typically give 64-80 GB to a job which was using all the CPUs, and leave the remaining memory for the operating system to use as disk cache.

**Pinning threads to CPUs under Linux.** Efficiency is lost when threads are moved from one CPU to another, thereby invalidating the cache and causing other overhead. On most machines, Gaussian can tie threads to specific CPUs, and this is the recommended mode of operation, especially when using larger numbers of processors. The %CPU Link 0 line specifies the numbers of specific CPUs to be used. Thus, on a machine with one 8-core chip, one should use %CPU=07 rather than %NProc=8 because the former ties the first thread to CPU 0, the next to CPU 1, etc.

On some older Intel processors (Nehalem and before), there is not enough memory bandwidth to keep all the CPUs on a chip busy, and it is often preferable to use half the CPUs, each with twice as much memory as if all were used. For example, on such a machine with four 12-core chips and 128 GB of memory, with CPUs 0-11 on the first chip, 12-23 on the second, and so on, it is better to run using 24 processors (6 on each chip) and give them 72 GB/24 procs = 3 GB memory each, rather than use all 48 with only 1.5 GB of memory each. The required input directives would be:

```
%Mem=72GB
%CPU=0-47/2
```

where the /2 means to use every other core: i.e., cores 0, 2, 4, 6, 8, and 10 (on chip 0), 12, 14, 16, 18, 20, and 22 (on chip 1), etc.

With the most recent generations of Intel processors (Haswell and later), the memory bandwidth is better and using all the cores on each chip works well.

As long as sufficient memory is available and threads are tied to specific cores, then parallel efficiency on large molecules is good up to 64 or more cores.

**Disable hyperthreading**. Hyperthreading is not useful for Gaussian since it effectively divides resources such as memory bandwidth among threads on the same physical CPU. If hyperthreading cannot be turned off, Gaussian jobs should use only one hyperthread on each physical CPU. Under Linux, hyperthreads on different processors are grouped together. That is, if a machine has 2 chips each with 8 cores and 3-way hyperthreading, then “CPUs” 0-7 are across the 8 cores on chip 0, 8-15 are across the 8 cores on chip 1, and 16-23 are the second hyperthreads on the 8 cores of chip 0, and so on. So a job would run best with %CPU=015.

Under AIX, hyperthreads are grouped together with up 8 hyperthread numbers for each CPU even if fewer hyperthreads are in use, so with two 8 core chips and 4-way hyperthreading, “CPUs” 0-3 are all on core 0 of chip 0, 8-11 are on core 1 of chip 0, etc. Thus, one would want to use %CPU=0127/8 to select “CPUs” 0, 8, 16, ··· which are each using a distinct core.

#### C.4.2 Cluster (Linda) parallelism

**Availability.** Hartree-Fock and DFT energies, gradients and frequencies run in parallel across clusters, as do MP2 energies and gradients. MP2 frequencies, CCSD, and EOM-CCSD energies and optimizations are SMP parallel but not cluster parallel. Numerical derivatives, such as DFT anharmonic frequencies and CCSD frequencies, are parallelized across nodes of a cluster by doing a complete gradient or second derivative calculation on each node, splitting the directions of differentiation across workers in the cluster. **Combining with MP parallelism.** Shared-memory and cluster parallelism can be combined. Generally, one uses shared-memory parallelism across all CPUs in each node of the cluster. Note that %CPU and %Mem apply to each node of the cluster. Thus, if one has 3 nodes names *apple*, *banana* and *cherry*, each with two chips which have 8 CPUs each, then one might specify:

```
%Mem=64GB
%CPU=0-15
%LindaWorkers=apple,banana,cherry
```

`# B3LYP/6-311+G(2d,p) Freq`···

This would run 16 threads, each pinned to a CPU, on each of the 3 nodes, giving 4 GB to each of the 48 threads. For the special case of numerical differentiation only – e.g., Freq=Anharm, CCSD Freq, etc. – one extra worker is used to collect the results. So these jobs should be run with two workers on the master node (where Gaussian 16 is started). For the above example if the job was computing anharmonic frequencies, then one would use:

```
%Mem=64GB
%CPU=0-15
%LindaWorkers=apple:2,banana,cherry
```

`# B3LYP/6-311+G(2d,p) Freq=Anharm`··· where Gaussian 16 is assumed to be started on node *apple*. This will start 2 workers on node *apple*, one of which just collects results, and will do the computational work using the other worker on *apple* and those on *banana* and *cherry*.

### C.5 CCSD Performance

#### C.5.1 Memory requirements for CCSD, CCSD(T) and EOM-CCSD calculations

These calculations can use memory to avoid I/O and will run much more efficiently if they are allowed enough memory to store the amplitudes and product vectors in memory. If there are NO active occupied orbitals (NOA in the output) and NV virtual orbitals (NVB in the output) then approximately 9 *NO* 2 *NV* 2 words of memory are required. This does not depend on the number of processors used.

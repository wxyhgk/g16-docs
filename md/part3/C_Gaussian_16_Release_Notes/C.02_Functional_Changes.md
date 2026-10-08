### C.2 Functional Changes

#### C.2.1 Changes from Gaussian 16 Rev. A.03

- There have been minor modifications to the procedure for building from source code, which is documented at `http://gaussian.com/g16/g16src_install.pdf`.

#### C.2.2 Changes from Gaussian 09

Calculation Defaults

The following calculation defaults are different in Gaussian 16:

- Integral accuracy is 10
- 12 rather than 10
- 10 in Gaussian 09.
- The default DFT grid for general use is UltraFine rather than FineGrid in G09; the default grid for CPHF is SG1 rather than CoarseGrid. See the discussion of the Integral keyword for details.
- SCRF defaults to the symmetric form of IEFPCM [702] (not present in Gaussian 09) rather than the non-symmetric version.
- Physical constants use the 2010 values rather than the 2006 values in Gaussian 09. The first two items were changed to ensure accuracy in several new calculation types (e.g., TD-DFT frequencies, anharmonic ROA). For these reasons, Integral=(UltraFine,Acc2E=12) was made the default. Using these settings generally improve the reliability of calculations involving numerical integration, e.g., DFT optimizations in solution. There is a modest increase in the CPU requirements for these options compared to the Gaussian 09 defaults of Integral=(FineGrid,Acc2E=10). The G09Defaults keyword sets all four of these defaults back to the Gaussian 09 values. It is provided for compatibility with previous calculations, but the new defaults are strongly recommended for new studies.

Default Memory Use

Gaussian 16 defaults memory usage to %Mem=100MW (800MB). Even larger values are appropriate for calculations on larger molecules and when using many processors; refer to the *Parallel Jobs* tab for details.

TD-DFT Frequencies

TDDFT frequency calculations compute second derivatives analytically by default, since these are much faster than the numerical derivatives (the only choice in Gaussian 09).

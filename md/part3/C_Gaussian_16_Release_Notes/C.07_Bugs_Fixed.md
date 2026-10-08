### C.7 Bugs Fixed

The following bugs are fixed in Rev. B.01:

- A problem with restarting in the middle of a job step (from the RWF) when using SCF=QC was fixed.
- When doing the regular SCF part of SCF=XQC or SCF=YQC, the orbitals and density are only saved when a new lowest energy wavefunction is found. If L502 fails to converge and the calculation moves on to L508 (QC or steepest descent SCF) then the best wavefunction from the regular SCF iterations is used.
- Problems with restarting from the RWF in the middle of EOM-CC calculations were fixed.
- Problems with ROMP4 and with EOM-CC when there was an empty beta spin-space or a full alpha spin-space were fixed.
- The erroneous labels in the summary table for G4 and G4MP2 jobs were corrected.
- Problems with naming scratch files for NBO when the RWF was split across physical files were fixed.
- An allocation problem which caused CIS and TD frequency jobs on large molecules using very small amounts of memory to fail was fixed. These jobs now complete, but they would run much more efficiently if given more memory (i.e., a larger value to %Mem).
- A bug which caused jobs which used the FormCheck keyword to fail was fixed. This keyword is deprecated, and the -fchk command line option, which is more flexible, is the preferred alternative.
- Unnecessary warnings which were printed by formchk when operating on a checkpoint file from a calculation which included PCM solvation were removed.
- The route for Opt=(TS,ReCalcFC=N) was corrected.
- Molecular mechanics parameters are now stored correctly in formatted checkpoint files.
- The route for doing interaction deletions using NBO6 (Pop=NBO6Del) was corrected.
- A bug which prevented GPUs from being enabled in later steps of a compound job was fixed.
- A problem with parsing the obsolete keywords QMom and Magneton in atomic property lists was corrected.

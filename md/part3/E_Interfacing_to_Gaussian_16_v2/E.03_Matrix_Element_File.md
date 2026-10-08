### E.3 Matrix Element File

The matrix element file is a simple unformatted file designed to exchange data, such as the overlap and core Hamiltonian matrix and two-electron integrals, in an extensible format. It can be written either as a Fortran unformatted file, suitable for processing by other Fortran programs, or as a raw binary fine without any flags or lengths for records, suitable for processing in C/C++/Perl/Python. This file format can be used as input to and/or output from a program run via the external interface (using the External keyword), or written as file by Gaussian for separate use by another program (using the Output=MatrixElement or Output=RawMatrixElement keywords). Various options to Output in combination with one of these will select various additional data within the file (e.g., the two-electron integrals over MOs). Finally, the data within any internal Gaussian file can be included within the matrix element file via the Output=Files option. The structure of the unformatted matrix element is as follows. The initial section contains records relating to the molecular structure and other general job characteristics:

**Record Format and Description**

1`Character*64 LabFil, Integer IVers, Integer NLab, Character*64 GVers` A label for the file type, version number for the file format, the number of general data records which precede the matrix element data (including this record), and the version of Gaussian which wrote the file. 2`Character*64 Title, Integer NAtoms, Integer NBasis, NBsUse, ICharg, Multip,`

```
NE,Len12L,Len4L,IOpCl,ICGU
```

The first 64 characters of the title section from the run which created the file, and the number of atoms and basis functions. *NBsUse* is the number of linearly independent basis functions. *ICharg* is the molecular charge, *Multip* the spin multiplicity (1=singlet, etc.), and *NE* is the number of electrons. *Len12L* is the number of bytes used for the integer labels for sparse 1D and 2D matrices, and *Len4L* is the number of bytes used for 4D matrices (2 electron integrals). *Len12L* and *Len4L* will be 4 if the file is written in raw mode (i.e., all integers will be I*4), for compatibility with other languages.

*IOpCl* is the closed/open-shell flag, which set if the matrix element file is written after an initial guess or the SCF has completed (otherwise it is -1, meaning unspecified). *ICGU* encodes whether the calculation is complex and/or GHF in a simpler way than *IOpCl*. Its three-digit value is interpreted as *klm*, where *k* is 1 for the spin-aligned case and 2 for GHF; *l* is 1 for real and 2 for complex; and *m* is 1 for RHF/GHF and 2 for UHF (i.e., 1 vs. 2 spin blocks). When *k*=2, then *NBasis* is the number of spatial basis functions, but the operator matrices are over the spin orbital basis and hence have dimension *k*NBasis*. When the file is read back into Gaussian, *IOpCl* can be -1 to indicate that *ICGU* should be used to specify these parameters. If *IOpCl*≥*0* and *ICGU*≥*0*, then they are checked for consistency. 3`Integer IAn(NAtoms)` Atomic numbers, padded to an even number of integers if using I*4. 4`Integer IAtTyp(NAtoms)` Atom type information. The main aspect of interest to other programs is that negative values indicate inactive atoms during an ONIOM model system calculation. By default, the file is written with inactive atoms omitted from all arrays and *NAtoms* set to the number of active atoms, but all atoms can optionally be included. It is padded to an even number of integers if using I*4. 5`Real*8 AtmChg(NAtoms)` Nuclear charges; may be different from atomic numbers if ECPs were used. 6`Real*8 C(3,NAtoms)` Cartesian nuclear coordinates in Bohr.

```
Integer IBfAtm(NBasis), IBfTyp(NBasis) 7
```

*IBfAtm* is the map from basis functions to atoms. *IBfTyp* is a type flag for each basis function. Each is of the form *lllmmm*, where *lll* is the angular momentum and *mmm* is the component number. Negative values indicate pure functions, and positive values indicate Cartesian functions. Thus, Cartesian *d* functions are numbered 2001 through 2006, and pure *d* functions are -2001 through -2005. 8`Real*8 AtmWgt(NAtoms)` Atomic weights. 9`NFC, NFV, ITran, IDum` Window information for MO 2 electron integrals. The MOs include *NFC* frozen core orbitals and *NFV* frozen virtuals, so the MO 2 electron integrals will be over *NBsUse-NFC-NFV* orbitals. *ITran*=0 if no MO integrals were stored, *ITran*=4 if only MOs involving at least one occupied orbital were stored, or *ITran*=5 if a full transformation was done. 10 toOther scalar data about the calculation (if applicable). *NLab* Record 10 is only present when *NLab*>9. It contains *NLab*-10 integers, each of which specifies the number of 32-bit words in the corresponding initial record (allowing programs to skip them when the file is stored without record marks/lengths). E.g., if *NLab* were to be 13, record 10 will contain 3 integers, specifying the lengths of the eleventh through thirteenth initial records. Currently, *NLab*’s maximum value is 11, and record 10 contains the single integer **16**. 1116 additional integers, of which only the first five are currently used: *NShellAO*: Number of contracted shells of AO basis functions, needed if shell data is provided. *NPrimAO*: Number of primitive AO shells.

*NShellDB*: Number of contracted shells of density fitting functions, needed if fitting shell data is provided. *NPrimDB*: Number of primitive density fitting shells. *NBTot*: Total Number of bonds in connectivity data, if any.

In general, programs should read (or skip) *NLab* records at the beginning of the file in order to reach the matrix element data. Doing so will ensure that additional initial records added in subsequent versions of the matrix element file are handled properly. These *NLab* records are followed by zero or more matrix sections, each of which has an initial record:

```
Character*64Label,IntegerNI,NR,NTot,NPerRec,N1,N2,N3,N4,N5,ISym
```

where the fields contain a label, the number of integers and number of reals for each element, the total number of elements, and number of elements per record. *NI* can be zero for dense matrices (stored with zeros included). *NR* is negative to flag complex rather than real data. *N1* through *N5* are dimensions for the object as a matrix, with 0 for unused dimensions and negative values for ones which are lower triangular. For example, if *NBasis*=50 and *NBsUse*=49 then *N1* ··· *N5* would be **-50**

**50 0 0 0** for the overlap matrix and **50 49 0 0 0** for the transformation to an orthogonal basis. *ISym*=-1 for

anti-symmetric/Hermetian matrices. The end of the file is marked with a record whose label is **END** and having all 0 values for the integers. This initial record is followed by *(NTot+NPerRec-1)/NPerRec* records, each of the one of the following forms:

```
IntegerID(NI,NPerRec),Real*8DX(NR,NPerRec)
```

or just:

```
Real*8DX(NR,NPerRec)
```

If *NI*=0 or *NR*<0, then the format is:

```
IntegerID(NI,NPerRec),Complex*16DX(-NR,NPerRec)
```

or

```
Complex*16DX(NR,NPerRec)
```

with the labels (if any) in *ID*, and values in *DX*. All matrix elements are over pure or Cartesian basis functions in accord with that specified in the Gaussian route or defaulted for the particular basis set.

#### E.3.1 Labeled Sections

The possible labels and sections include the following:

```
OVERLAP
COREHAMILTONIANALPHA
COREHAMILTONIANBETA
KINETICENERGY
```

Each is a lower triangular matrix stored dense (all *N**(*N*+1)/2 elements with no labels). The two core Hamiltonians are identical unless a Fermi contact perturbation has been applied.

```
ORTHOGONALBASIS
```

If present, this is an (*NBasis*,*NBsUse*) matrix giving the transformation from AOs to a linearly independent orthonormal set.

```
DIPOLEINTEGRALS
```

If present, this includes three lower-triangular matrices holding the X, Y, and Z dipole matrix elements.

```
QUADRUPOLEINTEGRALS
OCTOPOLEINTEGRALS
HEXADECAPOLEINTEGRALS
```

If present, these items are the 6, 10 or 15 matrices of the Cartesian multipole integrals (respectively).

```
DIPVELINTEGRALS
RXDELINTEGRALS
```

If present, these are the 3 matrices of the Del and RxDel one-electron operators.

```
GIAOD2H/DBDM
```

If present, each is a 9×*NAtoms* lower triangular matrices holding the GIAO core Hamiltonian second derivatives with respect to an external field and nuclear magnetic moments (the matrix elements required for the diamagnetic shielding term).

```
GIAOL/R3
```

If present, this each is a 3×*NAtoms* lower triangular matrices holding the GIAO magnetic perturbations (the matrices required for the paramagnetic shielding term).

```
ALPHAORBITALENERGIES
```

If present, this is an *NBsUse* vector of initial guess or converged orbital energies.

```
ALPHAMOCOEFFICIENTS
```

If present, this is an *NBasis*×*NBsUse* matrix of initial guess or converged orbitals.

```
BETAORBITALENERGIES
```

If present, this is an *NBsUse* vector of initial guess or converged orbital energies.

```
BETAMOCOEFFICIENTS
```

If present, this is an *NBasis*×*NBsUse* matrix of initial guess or converged orbitals.

```
ALPHADENSITYMATRIX
```

If present, this is a lower-triangular matrix containing the alpha spin part of the density matrix selected by the options for population analysis, etc. If read back into Gaussian, it is stored in place of the SCF density.

```
BETADENSITYMATRIX
```

If present, this is a lower-triangular matrix containing the beta spin part of the density matrix selected by the options for population analysis, etc. If read back into Gaussian, it is stored in place of the SCF density.

```
ALPHASCFDENSITYMATRIX
```

If present, this is a lower-triangular matrix containing an initial guess or converged SCF density.

```
BETASCFDENSITYMATRIX
```

If present, this is a lower-triangular matrix containing an initial guess or converged SCF density.

```
[ALPHA,BETA][MP2,MP3,MP4,CI,QCI/CC]DENSITYMATRIX
```

If present, these are the alpha and beta densities computed including the indicated type of correlation.

```
[MULLIKEN,ESP,AIM,NPA,MBS]CHARGES
```

Atomic charges of the specific type. Multiple charge sections may be present depending on the options to the Population keyword. Note that all types of electrostatic potential-derived charges are labeled as “ESP CHARGES”.

```
GAUSSIANSCALARS
```

This a vector of labeled reals. Labels between 1 and 1000 refer to elements of the Gaussian /Gen/ file (for a table, see below). Labels higher than 1000 are reserved for specific scalars to/from the external program.

```
ALPHADENSITYDERIVATIVES
BETADENSITYDERIVATIVES
```

If present, these hold the lower triangular AO density derivatives with respect to whatever perturbations were applied during the CPHF. The number of matrices is the number of perturbations, and it varies.

```
ALPHAMODERIVATIVES
BETAMODERIVATIVES
```

If present, these are the (*NBasis*,*NAE*,3) and (*NBasis*,*NBE*,3) MO coefficient derivatives with respect to a magnetic field.

```
ALPHAFOCKMATRIX
```

If present, this is the alpha-spin Fock matrix, or the only Fock matrix for closed-shell and GHF.

```
BETAFOCKMATRIX
```

If present, this is the beta-spin Fock matrix for unrestricted SCF calculations.

```
NUCLEARGRADIENT
```

If present, there are the 3**NAtoms* derivatives of the energy with respect to the nuclear coordinates. This is more likely to be a field returned by an external program than one used as input to the external program.

```
NUCLEARFORCECONSTANTS
```

If present, these are the second derivatives of the energy with respect to the nuclear coordinates. This is more likely to be a field returned by an external program than one used as input to the external program. They are stored as a lower triangular matrix of dimension 3**NAtoms*.

```
ELECTRICDIPOLEMOMENT
ELECTRICDIPOLEDERIVATIVES
ELECTRICDIPOLEPOLARIZABILITY
DIPOLEPOLARIZABILITYDERIVATIVES
ELECTRICDIPOLEHYPERPOLARIZABILITY
ATOMICAXIALTENSORS
```

If present, these are derivatives with respect to static external fields. If provided back to Gaussian, only the properties in the file are updated in the Gaussian internal data; any other properties already present in the Gaussian internal data are unaltered.

```
SHELLTYPE
NUMBEROFPRIMITIVESPERSHELL
CONTRACTIONCOEFFICIENTS
P(S=P)CONTRACTIONCOEFFICIENTS
COORDINATESOFEACHSHELL
```

These specify the basis set and are in the same format as the same fields in the fchk file. The same field names prefixed with `DENSITY` specify the density fitting set, if any.

```
OVERLAPDERIVATIVES
COREHAMILTONIANDERIVATIVES
F(X)
DENSITYDERIVATIVES
FOCKDERIVATIVES
ALPHAUX
BETAUX
```

These records contain the results of a derivative SCF (CPHF) calculation and are in the notation of [795]: Sx, Hx, F(x), Px, Fx, Ux, and Cx. F(x) and Fx contain all alpha followed by all beta Fock derivatives for open-shell, while the spin-cases of Ux and Cx are in separate records.

```
[Alpha,Beta][SCF,MP2,MP3,MP4,CIRho(1),CI,CC]DENSITY
```

These records hold post-SCF densities, alpha followed by beta for open-shell.

```
REGULAR2EINTEGRALSor
RAFFENETTI2EINTEGRALS
```

Only non-zero integrals are stored with 4 indices *i* ≥*j*, *i* ≥*k*, *k* ≥*l*, *j* ≥*l* if *i* = *k*. *NR* is 1 for regular integrals and 1, 2, or 3 for Raffenetti integral combinations:

*R* 1(*i*, *j*,*k*,*l*) = (*ij*|*kl*)−1/4[(*ik*|*jl*)+(*il*|*jk*)] *R* 2(*i*, *j*,*k*,*l*) = (*ij*|*kl*)+(*il*|*jk*) *R* 3(*i*, *j*,*k*,*l*) = (*ik*|*jl*)−(*il*|*jk*)

The default is *R1* only for closed-shell systems, *R1* and *R2* for UHF. The NoRaff keyword forces regular integrals, and IOp(3/11=*N*) can be used for force a particular set of Raffenetti integrals. If MO 2 electron integrals were requested, then these are stored dense (zeroes included and no integer labels). For restricted calculations there will be one set labelled `AA MO 2E INTEGRALS` with integrals stored over the unique quartets of indices if a fill transformation (*ITran*=5 above) is done. That is, if *NROrb = NBsUse - NFC - NFV* is the number of active orbitals (included in the transformation) then there will *NO4*=(*NOrbTT**(*NOrbTT*+1))/2 integrals, where *NOrbTT*=(*NROrb**(*NROrb*+1))/2, when there was a full transformation. For unrestricted and a full transformation, there will be 3 sets of integrals, AA, BA, and BB. AA and BB are length *NO4* and BA is *NOrbTT* 2, with the beta spin indices running fastest.

For a partial transformation (*ITran*=4) there will be one set of MO integrals for restricted, dimensioned (*NOrbTT,NROrb,NOA*) where *NOA=NAE-NFC* is the number of active occupieds. For restricted there will be AA, AB, BA and BB with dimensions (*NOrbTT,NROrb,NOA*), (*NOrbTT,NROrb,NOB*), (*NOrbTT,NROrb,NOA*), and (*NOrbTT,NROrb,NOB*), respectively.

```
TRANSMOCOEFFICIENTS
```

If MO two-electron integrals are included, this record holds the MO coefficients used in the transformation (i.e., with any frozen core or virtual orbitals omitted), alpha followed by beta spins.

#### E.3.2 Gaussian Scalars

1Virial ratio 2-4Components of applied electric field, if any 52e SCF energy 6SCRF g-factor 7SCRF a0 8Thermal energy 9E(CI/CC/QCI/BD) 10E(CCD+ST4(CCD)/QCISD(T)/BD(T)/CI+Davidson) 11E(VAR1) 12Zero-point energy 13Multi-step (G1, G2, etc.) energy 14Number of imaginary frequencies 15D(PUHF) 16EPUHF 17ECBS2 18ECBSI 19EPMP2-0 20EPMP3-0 21Root-mean-squared force of optimized parameters 22E(CIS-MP2) 23RMS error in density matrix S2 after annihilation of first contaminant 24 25CIS energy 26UMP4D (=UMP4DQ - E4(R+Q)) 27Reference energy for BD 28MP5 29S4SD (computed in ANNIL in L502, used by PSCF spin projection routines) 30Frozen-core part of total energy 31“TAU” from SCFDM 32SCF energy 33UMP2 energy 34UMP3 energy

35UMP4(SDTQ) energy 36CBS OIii 37Total energy with RF from L116 38MP4DQ energy 39MP4SDQ energy 40Used by L116 41Nuclear repulsion energy 42T (length of correction of reference determinant) 43Updated energy for optimizations <S2> of SCF wave function44 <S2> corrected to first order (after DOUBAR)45 <S2> corrected for doubles (not implemented)46 47A0 48Used to accumulate energy during Opt=Simult 49Temperature for thermochemistry 50Pressure for thermochemistry 51Scale factor for frequencies in thermochemistry 52Nuclear repulsion contribution from inactive atom pairs 53Singles contribution to E2 in ROMP2 54E(2) with current orbitals for extrapolation 55Nuclear term in the reaction field energy 56Electronic term in the reaction field energy 57Curvature from projected frequency jobs 58Reaction coordinate for single-points along IRCs 59Flag for status from external programs; see RunExt. 60SCF energy at first iteration 61Job status: -1=in progress; 0=undefined/old chk file; 1=finished successfully; 2=step in multi-step job completed successfully; 3=error termination in Link 9999 62Highest order of nuclear coordinate derivatives available. 63Number of iterations in most recent SCF. 64Nuclear repulsion energy without external field contribution.

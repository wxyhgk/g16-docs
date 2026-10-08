### E.4 FChk File

This file is designed to be machine independent with a structure that makes it easy for post-processors to extract required data and ignore the remainder. The latter fact is important for extensibility as future additions will not interfere with applications designed for previous revisions. Typically a job is run specifying a .chk file, which is the binary file containing results from a calculation which are potentially useful in later calculations or for post-processing, and then after Gaussian has completed, the formchk utility is run to generate the text .fchk file from the binary .chk file. There is also a utility, unfchk, to reverse the process. For backwards compatibility, running formchk without any options produces a subset of the full information. This document describes the results of running formchk -3 *chkfile fchkfile*, which produces a version 3 formatted checkpoint file (the current

and most full-featured version). Here is a description of the data in Fortran formatted form, although there is no particular reason to use Fortran as opposed to other languages to read the data. The first two lines in the file contain strings describing the job:

*Initial 72 characters of the title section.Complete route and title appear later.* *Type, Method, BasisFormat: A10,A30,A30*

*Type* is one of the following keywords:

SPSingle point FOPTFull optimization to a minimum POPTPartial optimization to a minimum FTSFull optimization to a transition state PTSPartial optimization to a transition state FSADDLEFull optimization to a saddle point of order 2 or higher PSADDLEPartial optimization to a saddle point of order 2 or higher FORCEEnergy+gradient calculation FREQVibrational frequency (2nd derivative) calculation SCANPotential surface scan GUESS=ONLYGenerate molecular orbitals only, also used with localized orbital generation LSTLinear synchronous transit STABILITYTest of SCF/KS stability REARCHIVE/MS-Generate archive information from checkpoint file RESTART MIXEDMixed method model chemistry (CBS-x, G1, G2, etc.), with method and basis set implied by model

*Method* is the method of computing the energy (AM1, RHF, CASSCF, MP4, etc.), and *Basis* is the basis set. All other data contained in the file is located in a labeled line/section set up in one of the following forms:

- Scalar values appear on the same line as their data label. This line consists of a string describing the data item, a flag indicating the data type, and finally the value:
- Integer scalars: *Name*,**I**,*IValue*, using format A40,3X,A1,5X,I12.
- Real scalars: *Name*,**R**,*Value*, using format A40,3X,A1,5X,E22.15.
- Character string scalars: *Name*,**C**,*Value*, using format A40,3X,A1,5X,A12.
- Logical scalars: *Name*,**L**,*Value*, using format A40,3X,A1,5X,L1.
- Vector and array data sections begin with a line naming the data and giving the type and number of values, followed by the data on one or more succeeding lines (as needed):
- Integer arrays: *Name*,I,*Num*, using format A40,3X,A1,3X,’N=’,I12. The N= indicates that this is an array, and the string is followed by the number of values. The array elements then follow starting on the next line in format 6I12.
- Real arrays: *Name*,R,*Num*, using format A40,3X,A1,3X,’N=’,I12, where the N= string again in-

dicates an array and is followed by the number of elements. The elements themselves follow on succeeding lines in format 5E16.8. Note that the Real format has been chosen to ensure that at least one space is present between elements, to facilitate reading the data in C.

- Character string arrays (first type): *Name*,C,*Num*, using format A40,3X,A1,3X,’N=’,I12, where the N= string indicates an array and is followed by the number of elements. The elements themselves follow on succeeding lines in format 5A12.
- Character string arrays (second type): *Name*,H,*Num*, using format A40,3X,A1,3X,’N=’,I12, where the N= string indicates an array and is followed by the number of elements. The elements themselves follow on succeeding lines in format 9A8.
- Logical arrays: *Name*,L,*Num*, using format A40,3X,A1,3X,’N=’,I12, where the N= string indicates an array and is followed by the number of elements. The elements themselves follow on succeeding lines in format 72L1. All quantities are in atomic units and in the standard orientation, if that was determined by the Gaussian run. Standard orientation is seldom an interesting visual perspective, but it is the natural orientation for the vector fields. The field names are fairly verbose to make them informative and should not be an impediment as only the interface program needs to use them. An example program, demofc, is distributed with Gaussian and demonstrates how to extract a named field.

Basis Set Data

The basis set information is provided in a reasonably general way which does not assume the specific structure of Gaussian’s Common /B/, which is rather obscure and reflects history more than clarity. The basis set data will include scalars giving the number of shells (*NShell*), largest degree of contraction, highest angular momentum present, and number of primitive shells (*NPrim*). There will then be arrays containing:

- Shell types (*NShell* values): 0=s, 1=p, -1=sp, 2=6d, -2=5d, 3=10f, -3=7f
- Number of primitives per shell (*NShell* values).
- Shell to atom map (*NShell* values): number of the atom on which each shell is located.
- Primitive exponents (*NPrim* values).
- Contraction coefficients (*NPrim* values): contraction coefficients of each normalized primitive shell. Contains the S coefficient for any S=P shells.
- P(S=P) Contraction coefficients (*NPrim* values): contraction coefficients for p portions of S=P shells. Not present if there are no S=P shells. Contains zeros for every primitive which is not part of an S=P shell.
- Coordinates of each shell: (3,*NShell*) array of XYZ coordinates for each shell. Other data, such as basis function indexing arrays, are easily derived from the above. The order of basis functions within shells is the usual Gaussian order:

```
S,X,Y,Z,XX,YY,ZZ,XY,XZ,YZ,XXX,YYY,ZZZ,XYY,XXY,XXZ,XZZ,YZZ,YYZ,XYZ
```

or

```
3ZZ-RR,XZ,YZ,XX-YY,XY,ZZZ-ZRR,XZZ-XRR,YZZ-YRR,XXZ-YYZ,XYZ,XXX-XYY,XXY-YYY
```

Available Items

The following items are among those currently defined:

- Route
- Full Title
- Number of atoms
- Charge
- Multiplicity
- Number of electrons
- Number of alpha electrons
- Number of beta electrons
- Number of basis functions
- Number of contracted shells
- Highest angular momentum
- Largest degree of contraction
- Number of primitive shells
- Virial Ratio
- Atomic numbers
- Nuclear charges
- Current Cartesian coordinates
- Alpha Orbital Energies
- Beta Orbital Energies
- Alpha MO coefficients
- Beta MO coefficients
- Shell types
- Number of primitives per shell
- Shell to atom map
- Primitive exponents
- Contraction coefficients
- P(S=P) Contraction coefficients
- Coordinates of each shell
- Total SCF Density
- Spin SCF Density
- Total MP2 Density
- Spin MP2 Density
- Total CI Density
- Spin CI Density
- Total CC Density
- Spin CC Density
- Cartesian Forces
- Cartesian Force Constants
- Dipole Moment
- Dipole Derivatives
- Polarizability
- Dipole 2nd Derivatives
- Polarizability Derivatives
- HyperPolarizability

#### E.4.1 Formatted Checkpoint File FAQ

**Which energy should be used by default?**

The Total Energy field has the energy at whatever level of theory the user requested. This is so other programs don’t have to figure out where the energy is from the *Method* string. In particular, we can add new methods and you won’t have to change logic to find the energy you’ll normally want.

**Why does the field descriptor include the data type information?**

The purpose of including the data type for each field is to facilitate skipping that field if it’s not of interest, as illustrated in the demo program below.

**How are ECP atomic charges handled?**

The “Nuclear charges” will differ from the atomic numbers if ECPs are in use.

**Which density matrix will be present?**

The total density will always be present; the spin density will be stored only for open-shell systems. By default this will be the SCF density. If a post-SCF density is desired, include the Density keyword in the Gaussian input.

**When will force constants be present?**

The force constants may be present and zero for cases for which only first derivatives were actually computed, or when they were computed at the first point of a geometry optimization but not at later points. They should only be used for vibrational analysis if the job type is Freq.

**Why is there no mapping array between shells and primitives?**

It was pointed out that the mapping from shells to primitives is not made explicit, so that the primitive data is stored separately for every atom, even if some have the same basis set. The information that atoms have the same basis set is discarded early in Gaussian. The basis set is only of interest if the orbitals or density is also used. Since the latter are quadratic in the size of the molecule, the potential savings for large molecules from removing redundant primitives seemed modest.

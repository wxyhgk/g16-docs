### C.1 New Features

#### C.1.1 New Modeling Capabilities

- [**REV B**] Static Raman intensities can be computed for excited states at the CIS and TD levels of theory. TD Freq=Raman computes the polarizability by numerical differentiation with respect to an electric field, so the cost of Freq=Raman for these methods is 7x that of the frequencies without Raman intensities.
- TD-DFT analytic second derivatives for predicting vibrational frequencies/IR and Raman spectra and performing transition state optimizations and IRC calculations for excited states.
- EOMCC analytic gradients for performing geometry optimizations.
- Anharmonic vibrational analysis for VCD and ROA spectra: see Freq=Anharmonic.
- Vibronic spectra and intensities: see Freq=FCHT and related options.
- Resonance Raman spectra: see Freq=ReadFCHT.
- New DFT functionals: M08HX, MN15, MN15L.
- New double-hybrid methods: DSDPBEP86, PBE0DH and PBEQIDH.
- PM7 semi-empirical method.
- Ciofini excited state charge transfer diagnostic: see Pop=DCT.
- The EOMCC solvation interaction models of Caricato: see SCRF=PTED.
- Generalized internal coordinates, a facility which allows arbitrary redundant internal coordinates to be defined and used for optimization constraints and other purposes. See Geom=GIC and GIC Info.

#### C.1.2 Performance Enhancements

- NVIDIA K40, K80 and P100 (Pascal) GPUs are supported under Linux for Hartree-Fock and DFT calculations; P100 support is new with [**REV B**] which also provides performance improvements for all GPU types. See Using GPUs for details on GPU support and usage.

![](../../images/part3/p027_5.jpeg)

- Parallel performance on larger numbers of processors has been improved. See the Parallel Performance tab for information about how to get optimal performance on multiple CPUs and clusters.
- [**REV B**] Dynamic allocation of tasks among Linda workers is now the default, improving parallel efficiency.
- Gaussian 16 uses an optimized memory algorithm to avoid I/O during CCSD iterations.
- There are several enhancements to the GEDIIS optimization algorithm.
- CASSCF improvements for active spaces
- (10,10) increase performance and make active spaces of up to 16 orbitals feasible (depending on the molecular system).
- Significant speedup of the core correlation energies for W1 compound model.
- Gaussian 16 incorporates algorithmic improvements for significant speedup of the diagonal, secondorder self-energy approximation (D2) component of composite electron propagator (CEP) methods as described in [385]. See EPT.

#### C.1.3 Usage Enhancements

- [**REV B**] The ChkChk utility now reports the job status (whether the job completed normally, failed, is in progress, etc.)
- [**REV B**] The optional parameters in the input line for an atom can now specify the radius to use when finite (non-point) nuclei are used. The radius is specified as a floating point value in atomic units using the RadNuclear=*val* item. For example:

```
C(RadNucl=0.001)0.00.03.0
```

- Tools for interfacing Gaussian with other programs, both in compiled languages such as Fortran and C and with interpreted languages such as Python and Perl. Refer to *Interfacing to Gaussian 16* for details. [**REV B**] adds many additional quantities have been added to the matrix element file, including atomic populations, one-electron and property operator matrices and the non-adiabatic coupling vector. The new items are the labeled sections QUADRUPOLE INTEGRALS, OCTOPOLE INTEGRALS, HEX- ADECAPOLE INTEGRALS, [MULLIKEN,ESP,AIM,NPA,MBS] CHARGES, DIP VEL INTEGRALS, R X DEL INTEGRALS, OVERLAP DERIVATIVES, CORE HAMILTONIAN DERIVATIVES, F(X), DENSITY DERIVATIVES, FOCK DERIVATIVES, ALPHA UX, BETA UX, ALPHA MO DERIVA- TIVES, BETA MO DERIVATIVES, [Alpha,Beta] [SCF,MP2,MP3,MP4,CI Rho(1),CI,CC] DENSITY and TRANS MO COEFFICIENTS and the scalars 63-64.
- Parameters specified in Link 0 (%) input lines and/or in a *Default.Route* file can now also be specified via either command-line arguments or environment variables. [**REV B**] introduces command-line options to specify input and/or data using a checkpoint or matrix element file (the equivalent of the %OldChk or %OldMatrix Link 0 commands for input). See the *Equivalencies* tab for details.
- You can now compute the force constants at every nth step of a geometry optimization: see Opt=Recalc.
- [**REV B**] DFTB parameters are now read in Link 301 before the basis set is constructed, so that the presence or absence of d functions for an element can be taken from the parameter file.
- [**REV B**] There are now command-line options to specify input and/or data to/from checkpoint or matrix element files. See the *Equivalencies* tab or the *command line options* page for details.

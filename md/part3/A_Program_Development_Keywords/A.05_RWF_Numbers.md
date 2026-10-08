### A.5 RWF Numbers

The following is a list of read-write files. Those that are permanently on the checkpoint file are marked with the letter **P**, and those that are temporarily on the checkpoint file are marked with the letter **T**. **T** files are saved for use in restarting an optimization or numerical frequency run, but are deleted when the job step completes successfully.

**Type RWFDescription**

**P** 501Gen array.

**P** 502/LABEL/–Title and atomic orbital labels.

503Connectivity information (MxBond,0),NBond(NAtoms),IBond(MxBond,NAtoms),RBond(MxBond, NAtoms), where arrays are rounded to a multiple of IntPWP. 504Dipole derivative matrices (NTT,3,NAt3).

**P** 505Array of copies of /Gen/ from potential surface scan.

**P** 506Saved basis set information before massage, uncontraction, etc.

**P** 507ZMAT/ and /ZSUBST/.

**P** 508/IBF/ Integral Bugger Format.

509Incomplete integral buffer.

**T** 510/FPINFO/ Fletcher-Powell optimization program data.

**P** 511/GRDNT/ energy, First and second derivatives over variables, NVAR.

**P** 512Pseudo-potential information.

**P** 513/DIBF/ integral derivative buffer format.

514Overlap matrix, optionally followed by absolute overlap and absolute overlap over primitives. 515Core-Hamiltonian. There are four matrices here: H(α), the α core Hamiltonian; H(β), the β core Hamiltonian; G’(α), the α G’ contribution to Fock matrix; G’(β), the β G’ contribution to Fock matrix. H(α) and H(β) differ only if Fermi contact integrals have been added. The G’ matrices are for perturbations which are really quadratic in the density (and hence have a factor of 1/2 in their contribution to the energy as compared to the true one-electron terms) but which are computed externally to the SCF.

516Kinetic energy and modifications to the α and β core Hamiltonian. These include ECP terms, Douglas-Kroll-Hess corrections, multipole perturbations and Fermi contact perturbations. The latter are used for calculations in which the nuclear and electronic Coulomb terms are computed together, such as the Harris functional and PBC calculations. For semi-empirical, holds the core Hamiltonian without nuclear attraction terms for use in the initial guess. 517Fermi contact integrals. 518Multipole integrals, in the order X,Y,Z,XX,YY,ZZ,XY,XZ,YZ,XXX,YYY,ZZZ,XYY,XXY,XXZ, XZZ,YZZ,YYZ,XYZ,XXXX,YYYY,ZZZZ, XXXY,XXXZ,YYYX,YYYZ,ZZZX,ZZZY,XXYY, XXZZ,YYZZ,XXYZ,YYXZ,ZZXY.

**T** 519Common /OptEn/–optimization control for link 109.

**T** 520Electronic state: count and packed string (1+9 integers).

**P** 521Electronic state: count and packed string (1+9 integers).

**P** 522Eigenvalues, alpha and if necessary, beta.

523Symmetry assignments.

**P** 524MO coefficients, real alpha.

**P** 525(no longer used)

**P** 526MO coefficients, real beta.

**P** 527(no longer used)

**T** 528SCF density matrix, real alpha.

**T** 529(no longer used)

**T** 530SCF density matrix, real beta.

**T** 531(no longer used)

**T** 532SCF density matrix, real total.

**T** 533(no longer used)

**T** 534SCF density matrix, real spin.

535(no longer used) 536Fock matrix, real alpha. 537Fock matrix, imaginary alpha. 538Fock matrix, real beta. 539Fock matrix, imaginary beta. 540Molecular alpha-beta overlap (U), real. 541Molecular alpha-beta overlap (U), imaginary.

**T** 542Pseudo-potential information.

**T** 543Pseudo-potential information.

**T** 544Pseudo-potential information.

**P** 545/ORB/ – window information.

546Bucket entry points. 547Eigenvalues (double precision with window: always alpha and beta, even in RHF case).

**P** 548MO coefficients (double precision with window, alpha and if necessary beta). Complex if neces-

sary. 549Molecular orbital alpha-beta overlap, double precision with window.

**T** 550Potential surface scan common block.

**T** 551Symmetry operaiton info (permutations, transformation matrices, etc.)

**P** 552Character strings containing the stoichiometric formula and framework group designation.

**T** 553Temporary storage of common/gen/ during FP optimizations.

**T** 554Alternate starting MO coefficients, from L918 to L503, real alpha. Also MO coefficients in S-1/2

basis for L509 and rotation angles from L914 to L508. 555Alternate starting MO coefficients, from L918 to L503, imaginary alpha.

**T** 556Alternate starting MO coefficients, from L918 to L503, real beta. Also MO coefficients in S-1/2

basis for L509 and rotation angles from L914 to L508. 557Alternate starting MO coefficients, from L918 to L503, imaginary beta. 558Saved HF 2nd derivative information for G1, G2, etc. 559Common /MAP/. 560Core-Hamiltonian (a. o. basis) with 2 j – k part of deleted orbitals added in. (i.e. frozen core).

**P** 561External point charges or SCIPCM informations.

**P** 562Symmetry operations and character table in full point group.

**T** 563Integer symmetry assignments (α).

**T** 564Integer symmetry assignments (β).

**T** 565Lists of symmetry equivqlent shells and basis functions.

**T** 566Unused in G16.

**T** 567GVB pair information (currently dimensioned for 100 paired orbitals).

**P** 568Saved hamiltonian information from L504 and L506.

**P** 569Saved read-in window.

**P** 570Saved amplitudes (IAS1,IAS2,IAD1,IAD2,IAD3; only IAS1 and IAD2 for closed-shell).

571Energy weighted density matrix. 572Dipole-velocity integrals <Phi|Del|Phi’>, X, Y, and Z, followed by R × Del integrals (R × X, R

- Y, R
- Z). 573More SCIPCM information.

**T** 574/MSINFO/ Murtaugh-Sargent program data.

**T** 575/OPTGRD/ Gradient optimization program data for L103, L115, and L509.

**T** 576/TESTS/ Control constants in L105.

**T** 577Symmetry adapted basis function data.

**T** 578A logical vector indicating which MO’s are occupied.

**T** 579NEQATM (NATOMS*NOP2) for symmetry.

**T** 580NEQBAS (NBASIS*NOP2+NBas6D*NOp2) for symmetry.

**T** 581NSABF (NBASIS*NOP2) for symmetry. Followed by matching integer character table, always

(8,8).

**T** 582MAPROT (3*NBASIS) for symmetry.

**T** 583MAPPER (NATOMS) for symmetry.

**P** 584FXYZ (3*NATOMS) cartesian forces. During PSCF gradient runs, there will be two arrays here:

first the PSCF gradient, then the HF only component (needed for PSCF with HF 2nd deriv).

**P** 585FFXYZ (NAT3TT) cartesian force constants (lower triangle).

**T** 586Info for L106, L110, and L111.

**T** 587L107 (LST) data.

588Sx over cartesians in the ao basis. 589Hx over cartesians in the ao basis. F(x) over cartesians in the ao basis (all α, followed by all β for UHF) (without CPHF terms).590 591U1(A,I) – MO coefficient derivatives with respect to electric field and nuclear coordinates. 592Electric field and nuclear P1 (AO basis). 593Electric field and nuclear W1 (AO basis). 594Electric field and nuclear S1 (MO basis). 595Magnetic field U1(A,I) – Del(X,Y,Z) then R × (X,Y,Z), 6 α followed by 6 β. 596Full MO Fock derivatives in the MO basis, including CPHF terms.

**P** 597Configuration changes for Guess=Alter.

598User Name. 599Density basis set info: NDBFn, NVar, U0, DenBfn(4,NDBfn), ITypDB(NDBfn), Var(NVar), IJAnDB(NDBfn), IVar(4,NDBfn). 600Saved data for intra-link restart.

**P** 601Saved structures, and possibly forces and force constants along reaction path. All structures, then

all forces, then all force constants. 602Post-SCF two-particle density matrix.

**P** 603Density Matrices at various levels of theory.

**T** common /drt1/ from drt program ··· misc integer ci stuff, followed by variable dimension drt604

arrays.

**P** 605Atomic charges from Mulliken Populations, ESP fits, etc. Bitmap followed by 0 or more NAtoms

arrays. Bits 0/1/2/3/4 Mulliken/ESP-fit/Bader/NPA/APT. 606SCF orbital symmetries in Abelian point group. Alpha and, if necessary, beta, full set followed by windowed set. 607Window’d orbital symmetries like rw 606 (always alpha and beta). 608IBF for sorted integrals (normally on SAO unit). 609Bit map for sorted integrals (normally on SAO unit). 610Sorted AO integrals (normally on SAO unit). 611NTT maps for sorted integrals (normally on SAO unit). 612Some 1E generators for direct CI matrix element generation. 613Some more 1E generators for direct CI matrix element generation. 614Configuration information for CAS-MP2. 615 -Used for CAS-MP2. 616 617Spin-orbit integrals.

**P** 618Nuclear coordinate third derivatives.

**P** 619Electric field derivatives: 1 WP word bit map, dipole, dipole derivative, polarizability, dipole 2nd

derivatives, polarizability derivatives, hyperpolarizability. 620Magnetic field derivatives for GIAOs.

621Susceptiblity and chemical shift tensors. 622Partial overlap derivatives (<Mu|dNu/da>, NBasis*NBasis*NAt3).

**P** 623Born-Oppenheimer wavefunction derivatives (<Phi|d2Phi/dadb> for electronic Phi and a,b nu-

clear, NAt3TT). 624Unused in G16. 625Expansion vectors and AY products from CPHF, in the order Y α, AY α, Y β, AY β. 626MCSCF MO 1PDM (NTT). 627MCSCF MO Lagrangian (NTT). 628MCSCF MO 2PDM (NTT,NTT) or NVTTTT. 629AO 2PDM (shell order).

**T** 630MCSCF information.

631Post-SCF Lagrangian (TA, then TB if UHF). 632O*V*3*NAtoms, followed by O*V*NVar d2E/d(V,O)d(XYZ,Atom).

**P** 633Excited-state CI densities.

**T** 634SCF Restart information (alpha, then possibly beta MOs).

**P** 635CIS and CASSCF CI coefficients and restart information.

636NBO analysis information. 637Natural orbitals generated by link 601. 640MCSCF data or CIS AO Tx’s for 2nd derivatives. 641MCSCF data for 2nd derivatives. 642MCSCF data for 2nd derivatives. 643MCSCF data for 2nd derivatives. 644MCSCF data for 2nd derivatives. 645MCSCF data for 2nd derivatives. 646MCSCF data for 2nd derivatives. 647MCSCF data for 2nd derivatives. 648MCSCF data for 2nd derivatives. 649Eigenvalue derivatives (non-canonical form even if done canonically). 6502PDM derivatives, (LenTQ,NDeriv,ShellQuartet) order. 651Full U’s, canonical or non-canonical as requested. 652Generalized density derivatives for the current method (NTT,NDeriv,IOpCl+1). 653Lagrangian derivatives for the current method (NTT,NDeriv,IOpCl+1). 654Gx(Gamma). 655G(Gamma). 656Non-symmetric S1 and S2 parts of Lagrangian for MP2 or CIS second derivatives. 657t*Ix and t*Ix/D matrices from L811 for L1112. 658L(x) from L1111. 659MO correlated W for correlated frequencies. 6602nd order CPHF results: Pia,xy, Sxy, Fxy (complete) all in MO basis, PSF α then PSF β if UHF. 661Computed electric field from L602. 662Points for electrostatic evaluation.

**T** 663Saved information for L117 and L124.

664Spin projection data.

**P** 665Redundant coordinate information.

666(no longer used) 667CIS AO Fock matrix. 668CIS Gx(T) matrices. 669Saved /ZMat/ and /ZSubst/ during redundant optimzations.

**P** 670New format basis set data (compressed /B/).

**P** 671New optimization (L103/L104) data.

**P** 672Unused in G16.

673Global optimization data. 674ONIOM internal data. 675Saved files for LS during ONIOM. 676Saved files for MS during ONIOM. 677Saved files for LM during ONIOM. 678Saved files for HS during ONIOM. 679Saved files for MM during ONIOM. 680Saved files for LL during ONIOM. 681Saved files for HM during ONIOM. 682Saved files for ML during ONIOM. 683Saved files for HL during ONIOM. 684SABF information for DBFS: equivalent to files 577 and 581 for AOs. 685Cholesky U, or transformation to surviving basis functions. 686Cholesky U-1. 687Molecular mechanics parameters. 688Density in orthogonal basis (α spin) for ADMP or sparse SCF. 691Saved initial files during ONIOM (gridpoint 17, hence 674+17=691). 694Permutation applied to MOs for post-SCF symmetry. 695Magnetic properties. 696Saved magnetic field density derivatives. 698Saved initial structure during geometry optimization, in standard orientation, also used for constraints with the force constants following the structure. 699Density in orthogonal basis (β spin) for ADMP or sparse SCF. 700Saved /Mol/ for ONIOM. 701Saved Trajectory/IRC/Optimization history. 702Fit density for Coulomb. 703Fit density for Coulomb. 704Saved XC contribution to electric field F(xa) for polar derivatives.

**P** 710Basic PCM information.

**P** 711Other PCM data.

**P** 712Non equilibrium data for PCM.

713Saved information for RFO with ONIOM microiterations. 714Saved model system information for ONIOM microiterations. 715Saved rigid fragment information for ONIOM microiterations.

**T** 716Saved copy of basis set data for counterpoise.

**T** 717Saved copy of ECP data for counterpoise.

**T** 718Saved copy of fitting basis for counterpoise.

719Saved DiNa information.

**P** 720Saved DiNa information.

721Frequency-dependent properties. 722Derivatives of frequency-dependent properties. 723Density fitting matrices (metrics). 724Density fitting basis (same format as /B/). 725DBF symmetry information (NEqDBF(NDBF,NOp2),NEqDB6(NDBF6D,NOp2)). 726DBF shell symmetry information (NEqDBS(NDBShl,NOpAll)). 727F(x)(P-Pfit) for density fitting second derivatives. 728PBC cell replication information. 729Alternate new guess during optimizations. 730Counterpoise input specification. 731Counterpoise intermediate data. 732Basis set for finite nuclei. 733PBC Cell scalars and integer cell indices. 734State-specific input parameters for SAC-CI. 735Excitation lables of SAC and SAC-CI. 736Eigenvalues and eigenvectors of SAC and SAC-CI. 737H matrices and their indices of non-zero elements used for SAC/SAC-CI. 738Saved atomic parameters for DFTB/EHTSC. 739Temporary storage for imaginary core Hamiltonian perturbations. 740Orbital information for SAC/SAC-CI gradients and PES by GSUM. 741MOD Orbital information for SAC gradients. 742Saved quadrature grid. 743Alpha Fock matrices in orthonormal basis for ADMP, also alpha HF Fock matrix for non-HF post-SCF. 744Beta Fock matrices in orthonormal basis for ADMP, also beta HF Fock matrix for non-HF post- SCF. 745K-integration mesh information. 746Eigenvalues and orbitals at all k-points. 747Information for external low-level calculations for ONIOM. 748TS vector information for ONIOM TS optimizations. 749Conical intersection information for ONIOM. 750Not used in G16. 751Temporary storage for SO ECP integrals.

752Pseudo-canonical MO Fock matrix for ROMP and ROCC. 753Data for FD polar derivatives. 754Saved PCM charge derivatives. 755PCM inverse matrices. 756Charge information for ONIOM. 757MO:MO embedding charge data for L924. 758Derivatives of embedding charges, when computed explicitly. 759Basis set info for density embedding.

**P** 760Full set of pseudocanonical orbitals for RO.

761Charges from external PCM iterations (both L117 and L124). 762Saved weights for non-symmetric Mulliken analysis. 763File for FC/HT integrals. 764File for FC/HT integrals.

**P** 765Saved normal modes.

766Saved QuadMac vectors (temporary). 767CIS coefficients reordered by symmetry. 768Semi-empirical parameters. 769Saved MOs during numerical differentiation.

**P** 770Saved ground-to-excited state energies and transition moments.

771EOM iteration information. 772Symmetry operations and character table in Abelian point group. 989Multi-step job information (1000 reals and 2000 integers). 990KJob info in some implementations. 991Holds file names, ID’s and save flags. 992Used for link substitution information in some implementations. 993COMMON /INFO/ 994COMMON /PHYCON/ 995COMMON /MUNIT/ 996COMMON /IOP/

**P** 997COMMON /MOL/

**P** 998COMMON /ILSW/

999Overlay data.

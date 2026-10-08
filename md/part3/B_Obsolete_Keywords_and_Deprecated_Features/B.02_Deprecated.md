### B.2 Deprecated

**NoFMM**

This keyword prevents the FMM facility from being used even when it would improve performance. It was required in some circumstances when running in parallel on a cluster or LAN with Linda in Gaussian 03. The associated problems have been fixed, and it is no longer needed.

**CCD+STCCD**

Specifies a coupled cluster calculation using double substitutions and evaluation of the contribution of single and triple excitations through fourth order using the CCD wavefunction. It is superseded by CCSD(T).

**CBS-Q, CBS-Lq**

Request the CBS-Q [180] and CBS-q [178] methods (i.e., Lq for “little q”). These are superceded by CBS-QB3.

**CBS-QB3O**

Uses the original parametrization [110] of CBS-QB3. It is obsolete and is included for backward compatibility only.

**CBS-4O**

Requests the original parametrization [180] of CBS-4. It is obsolete and is included for backward compatibility only.

**Geom=Coord**

Indicates that the geometry specification is in Cartesian coordinates. Cartesian coordinates can be included in molecule specifications without any special options being necessary.

**Geom=OldRedundant**

Use the Gaussian 94 redundant internal coordinate generator.

**Geom=ModLargeRedundant**

Uses the minimal setup for Opt=Big. It may not be used for periodic boundary calculations.

**Int=Raff**

Applies only to SCF=Conventional. Raff requests that the Raffenetti format [787] for the two-electron integrals be used. NoRaff demands that the regular integral format be used. It also suppresses the use of Raffenetti integrals during direct CPHF. This affects conventional SCF and both conventional and direct frequency calculations.

**Int=BWeights**

Use the weighting scheme of Becke for numerical integration.

**ReUse**

Use an existing integral file. Both the integral file and checkpoint file must have been preserved from a previous calculation. Only allowed for single point calculations and Polar=Restart.

**WriteD2E**

Forces the integral derivative file to be written in HF frequency calculations. Useful only in debugging new derivative code.

**LST, LSTCyc**

Requests that an initial guess for a transition structure be generated using Linear Synchronous Transit [788]. The LST procedure locates a maximum along a path connecting two structures and thus provides a guess for the transition structure connecting them. *Note that an LST calculation does not actually locate a proper transition state.* The LST method has been superseded by Opt=QST2.

**Massage**

The Massage keyword requests that the molecule specification and basis set data be modified after it is generated. This keyword is deprecated in favor of ExtraBasis, Charge, Counterpoise and other keywords.

**Opt=EnOnly**

Requests an optimization using a pseudo-Newton-Raphson method with a fixed Hessian and numerical differentiation of energies to produce gradients. This option requires that the Hessian be read in via ReadFC or RCFC. It can be used to locate transition structures and higher saddle points. Requires the molecule be specified as a Z-matrix. The default for energy-only methods is Opt=(EnOnly,EF).

**Opt=FP**

Requests the Fletcher-Powell optimization algorithm [789], which does not require analytic gradients. The maximum number of variables allowed for a Fletcher-Powell optimization is 30.Requires the molecule be specified as a Z-matrix.

**Opt=Grad**

Requests a gradient optimization, using the default method unless another option is specified. This is the default whenever analytic gradients are available and is invalid otherwise.

**Opt=MNDOFC**

Requests that the MNDO (or AM1, if possible) force constants be computed and used to start the (presumably *ab initio*) optimization. We recommend performing a PM6Freq calculation followed by Opt=RCFC instead of this option.

**Opt=MS**

Specifies the Murtaugh-Sargent optimization algorithm [790]. The Murtaugh-Sargent optimization method

is an obsolete alternative, and is retained in Gaussian only for backwards compatibility. The maximum number of variables allowed for a Murtaugh-Sargent optimization is 50. Requires the molecule be specified as a Z-matrix.

**Opt=UnitFC**

Requests that a unit matrix be used instead of the usual valence force field guess for the Hessian.

**Opt=GDIIS**

Specifies the use of the modified GDIIS algorithm [791–793]. The default GEDIIS algorithm is always better.

**Opt=Big**

Requests the optimization to be done using the fast equation solving methods [794] for the coordinate transformations and the Newton-Raphson or RFO step. This method avoids the matrix diagonalizations. Consequently, the eigenvector following methods (Opt=TS) cannot be used in conjunction with it. This option is unreliable and not recommended.

**Output=PolyAtom**

This requests output of an integral file in one variant of the format originated for the PolyAtom integrals program. The format produced by default is that used by the Caltech MQM programs, but the code in Link 9999 is easily modified to produce other variations on the same theme.

**Output=Trans**

Write an MO coefficient file in Caltech (Tran2P5) format. This is only of interest to users of the Caltech programs.

**SCF=Sleazy**

Requested the loose SCF convergence criteria appropriate for single points; equivalent to SCF=(Conver=4,VarInt, NoFinal,Direct). SinglePoint is a synonym for Sleazy. It is never recommended for production quality calculations.

**SCF=VerySleazy**

Reduced cutoffs even further; uses Int=CoarseGrid and single-point integral accuracy during iterations, followed by a single iteration with the usual single point grid (MediumGrid). Not recommended for production quality calculations.

**SCRF=DPCM**

Uses the polarizable dielectric model [685, 686, 688], which corresponds to the Gaussian 98 SCRF=PCM option except for some minor implementation details [700]. This model is no longer recommended for general use. The default SCRF method is IEFPCM.

**SCRF=Numer**

Force numerical SCRF rather than analytic. This keyword is required for multipole orders beyond Dipole. This option implies the use of spherical cavities, which are not recommended. No gradients are available for this option.

**SCRF=Dipole**

The options Dipole, Quadrupole, Octopole, and Hexadecapole specify the order of multipole to use in the SCRF calculation. All but Dipole require that the Numer option be specified as well.

**SCRF=Cards**

Begin the SCRF=Numer calculation with a previously computed reaction field read from the input stream,

immediately after the line specifying the dielectric constant and radius (three free-format reals).

**%SCR**

Used to specify the location of the **.SCR** scratch file.

**Stable=Symm**

Retain symmetry restrictions. NoSymm relaxes symmetry restrictions and is the default.

**Transformation=Old2PDM**

Forces the old-fashioned process of the 2PDM in post-SCF gradients (sorted in L1111 and then processed in L702 and L703). This is slow, but it reduces memory requirements. This option cannot be used for frozen core calculations.

**Transformation=New2PDM**

Causes the 2PDM to be generated, used, and discarded by L1111 in post-SCF gradient calculations.

**Transformation=Conventional**

Requests that the original transformation method based on externally stored integrals be used.

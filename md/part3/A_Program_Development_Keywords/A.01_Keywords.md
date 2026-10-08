### A.1 Keywords

The keywords and options described here are useful for developing new methods and other debugging purposes, but are not recommended for production level calculations.

#### A.1.1 General Job Restart

We discuss here the general use of Restart, designed for debugging. See the Restart section for production use. This keyword restarts a calculation by reusing the read-write file. The form Restart L1 reuses the read-write file but generates a new route. Restarts using the original route can specify the occurrence of a particular link and whether to clean up or retain overlay and link-volatile files using the following syntax:

**#P Restart** [**L** *n*[(*m*)]] [**Clean**|**KeepOverlay**|**KeepAll**]

When all parameters are specified, the job restarts at the *m* th occurrence of Link *n*. Clean requests that all routine and overlay volatile files be removed by Link1, KeepOverlay requests that overlay-volatile files be retained but not link-volatile ones, and KeepAll retains everything. The default is to KeepAll if the read-write file is set up for an intra-link restart and Clean otherwise.

#### A.1.2 IOp Setting Keywords

IOp1=*keyword* This keyword controls various details of the operating system interface. The options are standard, but not all are implemented (or even relevant!) in every version.

FileIODumpDump FileIO tables at the end of each link. FDump is a synonym for this keyword.

![](../../images/part3/p003_1.jpeg)

TimeStampTurn on time stamping. TStamp is a synonym for this keyword. FileIOPrintTurn on additional debug print in FileIO. SynchCurrently a no-op (appears in a few test jobs). NoDFTJTurn off use of the pure Coulomb term for non-hybrid DFT (seldom useful in production jobs). AbelianOnlyForce the use of only abelian symmetry (seldom useful in production jobs). NoPackSortTurn off packing addresses into 32-bits during sorts, even if the address space being sorted is < 231 (seldom useful in production jobs).

IOp2 This option sets the maximum amount of memory which will be dynamically allocated. MDV and Core are synonyms for IOp2. IOp33 This sets the standard debug print option as specified.For example, the following sets IOp(33) to 3 in all invocations of overlay 2, and IOp(33) to 1 in all invocations of overlay 7:

```
IOp33(2=3,7=1)
```

The *Gaussian 16 IOps Reference* also documents all internal options (IOps).

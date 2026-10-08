### E.2 Description

In the past, some people have used functionality from Gaussian by linking the executables for their programs with Gaussian’s libraries, or by having their code called within a Gaussian link. However, this is problematic in many ways. It requires having Gaussian source code, that the user compile their own code with the same compiler and options as Gaussian, and that the user understand the internal data structures and calling conventions within Gaussian. It made the resulting code fragile in that internal changes in future versions of Gaussian, transparent to ordinary users, could break the user’s code. In addition, it created unnecessary complications with respect to code ownership and intellectual property.

#### E.2.1 Goals for a General Interface

Our goals for a general interface are to facilitate all of the above uses in clean and maintainable ways. It should:

- Allow communication between other programs or scripts and standard Gaussian binaries without requiring recompilation, modification of Gaussian, or access to Gaussian source code.
- Be as simple for the user as possible, in particular by providing an interface which does not require knowledge of Gaussian’s internal data structures or algorithms, and requiring as little knowledge of the internal structure of interface files as possible.
- Be self-defining and upward compatible, so that new types of data and new functionality can be added without breaking user code which worked with a previous version of the interface.
- Facilitate the use of Gaussian as either the controlling or the subordinate program.
- Be as non-Gaussian-centric as possible, to allow code that uses the Gaussian interface to also use other quantum chemistry codes which provide the same interface. Previously, we have provided the formatted checkpoint file as an interface mechanism, particularly for postprocessing of results from Gaussian. This file is still supported and available. It is self-defining and extensible.

Being an ordinary text file gives it a relatively simple format to process. However, while this design is suitable for post-processing results from Gaussian, especially for visualization, it is not adequate as a general interface for two reasons. First, the limited precision with which values are stored is not sufficient for intermediate data such as integrals. Second, reading and writing the file is expensive when large amounts of data are involved because of the conversion to and from text form. In addition, since the file was intended for post-processing and for moving data between Gaussian running on different types of hardware, it mirrors many of the internal Gaussian data structures.

#### E.2.2 Structure of the General Interface

There are three basic components of the new interface:

- A binary data file which is self-defining but reasonably compact, and which attempts to store standard data in simple forms rather than using Gaussian’s internal data structures. These forms are supported in either Fortran unformatted form, which is useful for interfacing to programs in Fortran or Python, and as raw binary data, which is suitable for use in C, C++, and Perl programs. Data is organized in the same way in either type of file. Details of the file structure can be found in *Matrix Element File*. The formchk and unfchk utilities can convert between Gaussian checkpoint files and either type of binary interface file.
- Functionality within Gaussian to use such binary data files as input or output for complete Gaussian jobs and as input/output between Gaussian and external programs being run from within Gaussian. A subordinate program is connected to Gaussian via the External interface. Such a program can be used:
- In lieu of a Gaussian SCF link.
- As a post-SCF step using orbitals generated within Gaussian.
- To compute derivatives for use in optimizations and frequency calculations controlled by Gaussian.
- To perform one or more of the sub-calculations within an ONIOM model. Gaussian can also be run as a subordinate program, taking most or all of its input from a data file provided by the controlling program, and producing a new data file containing the results from Gaussian.
- Libraries and scripts which provide easy-to-use interfaces for reading and writing these file. They are open source and hence can be easily incorporated in user programs. The interface will continue to evolve as additional capabilities are required. The quantities which are currently available in the data file include the most common quantities used in SCF and post-SCF calculations, such as the location and identities of atoms, basis set, one and two electron integrals over atomic orbitals, molecular orbital coefficients, and two electron integrals over molecular orbitals.

#### E.2.3 About the Interface Libraries and Scripts

The open source interface libraries and scripts have reached varying degrees of maturity depending on their extent of use so far:

- The Fortran interface routines (in *qcmatrix.F* and *qcmatrixio.F*) provide for convenient reading and writing data from the files with minimal knowledge of their structure. The Fortran interfaces have been tested with the PGI, Gnu and Intel Fortran compilers.
- The Python modules import the Fortran interface via **f2py** but add higher-level functionality, including object interfaces for both the individual items in the file (atomic coordinates, operator matrices, etc. in *QCOpMat.py*) and for the entire file as an object (in *QCMatEl.py*). In addition to reading and writing the file, the file object also provides methods to transparently run Gaussian to generate additional data, so a

Python user can request and consume results from Gaussian without any knowledge of Gaussian’s input or any knowledge of the structure of the interface file on disk. The actual data from the file are stored as **NumPy** arrays and hence are useful directly in **NumPy** and **SciPy** routines. The Python interface uses many features of Python3 and is not supported with Python2.

- The Perl modules (*OpMat.pm* and *MatEl.pm*) provide transparent object interfaces to the data items and entire file in the same style as the Python modules, but do not include all of the higher level functionality.

Details of all the interfaces are in the comments in the source files.

The interface routines assume 4 byte integers in the data file. For the raw form of the file, a fixed integer size must be assumed because there is no reliable way to determine this when the file is read. Since both Perl and Python currently use 32-bit addressing and cannot handle arrays larger than 2 GB, this is not a limitation for these languages. Versions of the Fortran interface routines are built for both 4-byte and 8-byte integers (the latter have 8 appended to their filename).

There is not currently a separate C interface library; depending on the circumstances, C code can either read the raw binary files using the same logic as in the Perl modules, or can call the Fortran interface routines. Since the details of calling Fortran from C or C++ depend on the particular operating system and compilers, we have not attempted to standardize this.

#### E.2.4 Generating Interface Data Files in Gaussian

The binary matrix element file can be produced in three ways:

- Using the formchk utility to convert the binary checkpoint file left after a Gaussian job.
- Using an external script or program is to be run as part of the calculation in Gaussian via the External keyword.
- Using the Output=MatrixElement or Output=RawMatrixElement keywords to cause a file to be generated at the end of the current Gaussian job step.

A formatted checkpoint file can similarly be produced in three ways:

- Using the formchk utility to convert the binary checkpoint file left after a Gaussian job.
- Generating it when an external script or program is to be run as part of the calculation in Gaussian (see External).
- By using the **-fchk** switch on the **g16** command line, which causes a formatted checkpoint file to be written or rewritten at each “interesting” point of a job step: for a new geometry during an optimization, the end of the job step, and the like.

#### E.2.5 Using Data Files as Input to Gaussian

Either the formatted checkpoint file or the binary matrix element file can be used as input to Gaussian by converting it to a binary checkpoint file. This is done using the unfchk utility. You then specify the name of the generated binary checkpoint file with the %Chk or %OldChk Link 0 command to provide the file to the Gaussian job step.

In addition, a matrix element file can be specified as input using the %OldMatrixElement or %OldRawMatrixElement Link 0 commands. These take the data from the matrix element file and move it to the checkpoint file for the current job step, where it can be used to provide the geometry, initial wavefunction, etc.

#### E.2.6 Running Gaussian from within other programs

There are at least two ways this can be accomplished:

- The other program can generate an Gaussian input file. This input filspecifies that Gaussian take input from a data file and/or generate a data file containing its results. The controlling program can then run Gaussian in a subprocess using the UNIX system command, the fork/exec facility, or equivalent functionality.
- The Python interface (*QCMatEl.py*) provides a matrix element class which includes methods which automatically run Gaussian and update a matrix element object with additonal data. This can be used directly by a Python program, or by a program in another language can create a subprocess running a simple Python script which in turn runs Gaussian.

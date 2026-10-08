### 6. Utility Programs

Most utilities are available for both UNIX and Windows versions of Gaussian. However, be sure to consult the release notes accompanying the program for information pertaining to specific operating systems.

The GAUSS_MEMDEF environment variable may be used to increase the memory available to utilities which do not offer such an option themselves. Its value should be set to the desired amount of memory. The default unit is words; the specified value can also be followed by a suffix indicating other units (e.g., GB for gigabytes).

The following lists the available utilities and their functions (*starred* items are included on the Gaussian 16W **Utilities** menu):

- c8616 Converts checkpoint files from previous program versions to Gaussian 16 format.
- chkchk* Displays the route and title sections from a checkpoint file.
- cubegen* Standalone cube generation utility.
- cubman* Manipulates Gaussian-produced cubes of electron density and electrostatic potential (allowing them to be added, subtracted, and so on).
- formchk* Converts a binary checkpoint file into an ASCII form suitable for use with visualization programs and for moving checkpoint files between different types of computer systems.
- freqchk* Prints frequency and thermochemistry data from a checkpoint file. Alternate isotopes, temperature, pressure and scale factor can be specified for the thermochemistry analysis.
- freqmem Determines memory requirements for frequency calculations.

![](../../images/part2/p287_6.jpeg)

- gauopt Performs optimizations of variables other than molecular coordinates.
- ghelp On-line help for Gaussian.
- mm Standalone molecular mechanics program.
- newzmat* Conversion between a variety of molecular geometry specification formats.
- testrt* Route section syntax checker and non-standard route generation.
- unfchk* Convert a formatted checkpoint file back to its binary form (e.g., after moving it from a different type of computer system).

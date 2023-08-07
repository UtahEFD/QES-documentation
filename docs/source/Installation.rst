Installation
============

This section is designed to serve as a step-by-step instruction of how
to build and run QES-Winds. In the first part, packages required to
build the code will be mentioned along with the oldest version of each
package that satisfies the purpose. The next part will be interaction
with the repository on GitHub in which the code is been stored to clone
the code. Also, commands required for cloning the repository and
building the executable of code, will be mentioned. The last part of
this section will cover a brief description of how to change the input
files of the code and run it.

Required Packages
-----------------

The very first package needed to be installed is ”git” package. It
provides the ability to interact with GitHub and use commands to clone
the repository, switch between different branches and etc. This package
does not have any dependencies, so it is always recommended to install
the latest version.

-  The next package inline is ”CMake” and its GUI version ”CCMake”. It
   finds all the packages required, links them together and creates the
   ”makefile” for building the code. CMake should be any version greater
   than 3.10.

-  QES-Winds also needs ”boost” libraries in order to have access to C++
   source libraries. Boost 1.66.0 is sufficient for the purpose of
   QES-Winds.

-  ”Gdal” libraries are necessary to read in Digital Elevation Models
   (DEM) and shapefile (for buildings). Version 2.3.1 of gdal libraries
   will do the job for our applications.

-  The last library that needs to be installed is ”netcdf-c” libraries
   along with netcdf interface with C++, version 4.6 is required. Netcdf
   libraries are essential for reading in WRF output files and writing
   QES-Winds results in netcdf format.

-  Finally, since QES-Winds is written in C++ and CUDA, ”gcc” and ”CUDA”
   compilers needed to be installed. Because there is a compatibility
   issue between versions of CUDA, gcc and Operating System(OS) (for
   more information go to
   https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html),
   version of gcc that is compatible with the version of CUDA and OS is
   required. For CUDA, at least version 8.0 needs to be installed.

Cloning QES-Winds from GitHub
-----------------------------

After making sure all the required packages are installed and ready to
use, a copy of QES-Winds needs to be downloaded on the local computer
(cloning process). To clone the code, go to the directory you want to
have the code downloaded, open a terminal and type ”git clone [address
to the repository]”. To get the address to the repository, go to the
repository GitHub page, UtahEFD/QES-Winds-Public, click on the green
button ”Code” and copy the ”HTTPS” address. It downloads a copy of the
code in the “master” branch of the repository in your local directory.

Building QES
------------

Next steps are:

-  Go to the folder created with name QES-Winds: ”cd QES-Winds-Public”.

-  Create a build directory: ”mkdir build” or ”sudo mkdir build”.

-  Go to folder build: ”cd build”.

-  Type: ”cmake ..”.

There is a chance that cmake fails to find all the packages needed for
running the code (packages installed on unconventional directories). In
this case, you need to do cmake with appropriate flags that point to
those packages.

-  After cmake is done successfully, type: ”build”

-  A successful build will result in creating the executable named
   ”qesWinds”

Linux
~~~~~

On a general Linux system, such as Ubuntu 18.04 or 20.04, the following
packages need to be installed:

-  libgdal-dev

-  libnetcdf-c++4-dev

-  libnetcdf-cxx-legacy-dev

-  libnetcdf-dev

-  netcdf-bin

-  libboost-all-dev

-  cmake

-  cmake-curses-gui

If the system uses ``apt``, the packages can be installed using the
following command:

::

   apt install libgdal-dev libnetcdf-c++4-dev  libnetcdf-cxx-legacy-dev libnetcdf-dev netcdf-bin libboost-all-dev cmake cmake-curses-gui

We separate the build

::

   mkdir build
   cd build
   cmake ..

You can then build the source:

::

   make

macOS
~~~~~

The packages can be installed using Homebrew (https://brew.sh)

::

   brew install cmake boost gdal hdf5 netcdf netcdf-cxx

If openMP multithreading is desired:

::

   brew install libomp

On intel silicon machines:

::

   cmake -DNETCDF_LIBRARIES_CXX=/usr/local/lib/libnetcdf-cxx4.dylib -DENABLE_OPENMP=ON -DCMAKE_PREFIX_PATH=/usr/local/Cellar/libomp/15.0.7/ ..

On apple silicon machines:

::

   cmake -DCMAKE_PREFIX_PATH=/opt/homebrew/Cellar/libomp/15.0.7 -DENABLE_OPENMP=ON -DNETCDF_LIBRARIES_CXX=/opt/homebrew/lib/libnetcdf-cxx4.dylib ..

University of Utah - CHPC
~~~~~~~~~~~~~~~~~~~~~~~~~

*This is the preferred build setup on CHPC*

The code does run on the CHPC cluster. You need to make sure the correct
set of modules are loaded. Currently, we have tested a few
configurations that use

-  GCC 5.4.0 and CUDA 8.0

-  CCC 8.1.0 and CUDA 10.1 (10.2)

-  GCC 8.5.0 and CUDA 11.4

If you build with OptiX support, you will need to use CUDA 10.2 or newer
configuration. Any builds (with or without OptiX) with CUDA 11.4 are
preferred if you don’t know which to use. Older configurations are
provided in ``CHPC/oldBuilds.md``.

After logging into your CHPC account, you will need to load specific
modules. In the following sections, we outline the modules that need to
be loaded along with the various cmake command-line calls that specify
the exact locations of module installs on the CHPC system.

To build with GCC 8.5.0, CUDA 11.4, and OptiX 7.1.0 on CHPC. Please use
the following modules:

::

   module load cuda/11.4
   module load cmake/3.21.4
   module load gcc/8.5.0
   module load boost/1.77.0
   module load intel-oneapi-mpi/2021.4.0
   module load gdal/3.3.3
   module load netcdf-c/4.8.1
   module load netcdf-cxx/4.2

Or use the provided load script, which will always load the latest
tested configuration.

::

   source CHPC/loadmodules_QES.sh

After completing the above module loads, the following modules are
reported from ‘module list‘:

::

   Currently Loaded Modules:
     1) cuda/11.4    (g)   3) gcc/8.5.0      5) intel-oneapi-mpi/2021.4.0   7) netcdf-c/4.8.1
     2) cmake/3.21.4       4) boost/1.77.0   6) gdal/3.3.3                  8) netcdf-cxx/4.2

After the modules are loaded, you can create the Makefiles with cmake.
We keep our builds separate from the source and contain our builds
within their own folders. For example,

::

   mkdir build
   cd build
   cmake -DCUDA_TOOLKIT_DIR=/uufs/chpc.utah.edu/sys/installdir/cuda/11.4.0 -DCUDA_SDK_ROOT_DIR=/uufs/chpc.utah.edu/sys/installdir/cuda/11.4.0 -DOptiX_INSTALL_DIR=/uufs/chpc.utah.edu/sys/installdir/optix/7.1.0 -DCMAKE_C_COMPILER=gcc -DNETCDF_CXX_DIR=/uufs/chpc.utah.edu/sys/installdir/netcdf-cxx/4.3.0-5.4.0g/include ..

Upon completion of the above commands, you can go about editing and
building mostly as normal, and issue the ‘make‘ command in your build
folder to compile the source.

After you’ve created the Makefiles with the cmake commands above, the
code can be compiled on CHPC:

::

   make

Note you *may* need to type make a second time due to a build bug,
especially on the CUDA 8.0 build.

Build Types
-----------

The code support several build types: *Debug*, *Release*,
*RelWithDebInfo*, *MinSizeRel*. You can select the build type

::

   cmake -DCMAKE_BUILD_TYPE=Release ..

*Release* is recommanded for production

cmake options:

-  build code without CUDA support automatically if CUDA is not
   supported by the system

-  build code with openmp support for future multithread
   application,openmp is not automatically enabled. if openmp support is
   enable (``-DENABLE_OPENMP=ON``) the code will run a new red/black
   solver on the CPU. Unfortunately thread safety issues with some plume
   classes did not allow for an easy parallelization of the plume
   advection.

-  default is *RELEASE* with most warning off, ``-O3`` optimization. a
   dev mode was added ``-DENABLE_DEV_MODE=ON`` showing warnings, will
   build the code in DEBUG this option is slow and recommended only for
   active development.

-  ClangTidy option was added

-  use ``-DENABLE_TESTS=ON`` to enable unit, sanity, and regressions
   tests using Catch2 (https://github.com/catchorg/Catch2)

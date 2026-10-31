Installation
============

This page describes how to configure and build QES. The recommended approach
uses vcpkg and CMake presets, which install and configure QES's external
dependencies automatically.

Requirements
------------

QES requires a C++17-compatible compiler. GPU acceleration requires the CUDA
library and an NVIDIA GPU with compute capability 7.0 or newer. QES can also be
built in CPU-only mode.

The following tools must be installed separately:

* CMake 3.24 or newer;
* a C++17-compatible compiler (GCC, Clang, or MSVC);
* Ninja (optional, but recommended for faster builds); and
* Doxygen (optional, to build the API documentation).

QES uses Boost (``program_options`` and ``date_time``), NetCDF C and C++, GDAL,
and nlohmann-json. vcpkg manages these libraries in the recommended setup.

OpenMP is optional. Enable it by passing ``-DENABLE_OPENMP=ON`` during CMake
configuration. On macOS, install its runtime with ``brew install libomp``.

Choose a source branch
----------------------

The public repository's most recent release is on the ``main`` branch. In the
private repository, ``main`` is the most recent stable version and
``workingBranch`` contains active development. For the latest features, switch
to the development branch:

.. code-block:: console

   git checkout workingBranch

Use ``git status`` to confirm the currently checked-out branch.

Recommended build: vcpkg and CMake presets
-------------------------------------------

vcpkg automatically downloads, builds, and configures GDAL, NetCDF, Boost, and
nlohmann-json. This workflow is supported on Windows, macOS, and Linux.

Set up vcpkg
~~~~~~~~~~~~~

Clone vcpkg in a permanent location and bootstrap it:

.. code-block:: console

   git clone https://github.com/microsoft/vcpkg.git
   cd vcpkg

On Windows:

.. code-block:: powershell

   .\bootstrap-vcpkg.bat

On Linux or macOS:

.. code-block:: console

   ./bootstrap-vcpkg.sh

Set the ``VCPKG_ROOT`` environment variable to the vcpkg installation directory.
To persist it on Windows PowerShell, add the following to ``$PROFILE``:

.. code-block:: powershell

   $env:VCPKG_ROOT = "C:\path\to\vcpkg"
   $env:PATH = "$env:VCPKG_ROOT;$env:PATH"

To persist it on Linux or macOS, add the following to ``.bashrc`` or ``.zshrc``:

.. code-block:: console

   export VCPKG_ROOT="/path/to/vcpkg"
   export PATH="$VCPKG_ROOT:$PATH"

Build with a preset
~~~~~~~~~~~~~~~~~~~

From the QES source directory, select a preset for your platform and build it.

**Windows**

Use the x64 Native Tools Command Prompt supplied with Visual Studio 2022:

.. code-block:: console

   cmake --preset=windowsDevNinja
   cmake --build buildWindowsDev

**macOS**

Available presets are:

* ``macOSRelease`` for an optimized production build;
* ``macOSDev`` for a development build; and
* ``macOSDevSanitizer`` for a development build with sanitizers.

For example:

.. code-block:: console

   cmake --preset=macOSDev
   cmake --build buildMacOSDebug

If Homebrew provides OpenMP, pass its installation path during configuration:

.. code-block:: console

   cmake -DOpenMP_ROOT="$(brew --prefix libomp)" --preset=macOSDev

**Linux**

Available presets are:

* ``unixRelease`` for an optimized production build;
* ``unixDev`` for a development build;
* ``unixDevSanitizer`` for a development build with sanitizers; and
* ``unixDevNoCUDA`` for systems without an NVIDIA GPU.

For example:

.. code-block:: console

   cmake --preset=unixDev
   cmake --build buildUnixDebug

Once CMake has configured a build directory, Unix and macOS builds can also be
compiled from that directory with ``make``.

Manual dependency setup
-----------------------

If you prefer to manage dependencies with your system package manager, install
GDAL, the NetCDF C and C++ interfaces, Boost, and CMake yourself.

On Debian or Ubuntu:

.. code-block:: console

   apt install libgdal-dev libnetcdf-c++4-dev libnetcdf-cxx-legacy-dev libnetcdf-dev netcdf-bin libboost-all-dev cmake cmake-curses-gui

On macOS with Homebrew:

.. code-block:: console

   brew install cmake boost netcdf gdal

Then configure and build QES from its source directory:

.. code-block:: console

   mkdir build
   cd build
   cmake ..
   make

Building on the CHPC cluster
----------------------------

The preferred CHPC configuration uses GCC 11.2 and CUDA 11.8. Load the tested
modules:

.. code-block:: console

   module load cuda/11.8
   module load cmake/3.21.4
   module load gcc/11.2.0
   module load boost/1.83.0
   module load gdal/3.8.5
   module load netcdf-c/4.9.2
   module load netcdf-cxx/4.2

Alternatively, use the supplied module script:

.. code-block:: console

   source CHPC/loadmodules_QES.sh

Create a separate build directory, configure it, and compile:

.. code-block:: console

   mkdir build
   cd build
   cmake -DNETCDF_CXX_DIR=/uufs/chpc.utah.edu/sys/installdir/netcdf-cxx/4.3.0-5.4.0g/include ..
   make

NVIDIA OptiX 7.6.0 is supported on CHPC and accelerates mixing-length
calculations. To enable it, add the following option to the CMake command:

.. code-block:: console

   -DOptiX_INSTALL_DIR=/uufs/chpc.utah.edu/sys/installdir/optix/7.6.0

Build types
-----------

Supported CMake build types are ``Debug``, ``Release``, ``RelWithDebInfo``, and
``MinSizeRel``. Use ``Release`` for production, for example:

.. code-block:: console

   cmake -DCMAKE_BUILD_TYPE=Release ..

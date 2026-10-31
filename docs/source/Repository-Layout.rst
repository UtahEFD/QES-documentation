QES source repository layout
============================

This page describes the layout of the main QES source repository. It is
intended for contributors working on the C++ and CUDA code; the documentation
repository has its own, smaller layout described in its root ``README.md``.

Top-level directories and files
-------------------------------

::

   QES/
   ├── CMakeLists.txt          # Top-level build configuration
   ├── CMakePresets.json       # Supported Windows, macOS, and Linux build presets
   ├── vcpkg.json              # External dependency manifest
   ├── cmake/                  # CMake helpers and modules
   ├── src/                    # Shared QES model and utility libraries
   ├── qesWinds/               # QES-Winds executable entry point and CLI options
   ├── qesPlume/               # Stand-alone QES-Plume executable entry point and CLI options
   ├── qes/                    # Coupled Winds/Turb/Plume executable entry point and CLI options
   ├── qesFire/                # Coupled fire executable entry point and CLI options
   ├── data/                   # Input data and example simulation inputs
   ├── testCases/              # Test-case definitions and supporting inputs
   ├── tests/                  # Unit, sanity, and regression tests
   ├── examples/               # Small example programs
   ├── tools/                  # Data-preparation and supporting utilities
   ├── CHPC/                   # CHPC module-loading and cluster build helpers
   ├── paperData/              # Data used for published studies and validation cases
   ├── docs/                   # Source-repository documentation assets
   ├── README.md               # Project overview and build quick start
   └── LICENSE                 # GPL-3.0 license

Core source code
----------------

``src`` contains code shared by one or more executables:

* ``src/winds`` contains QES-Winds models and solvers.
* ``src/plume`` contains QES-Plume models.
* ``src/fire`` contains QES-Fire models.
* ``src/qes`` contains code shared by the coupled drivers.
* ``src/util`` contains common utilities, such as input parsing, output, and
  data handling.

The ``CUDA`` subdirectories within the model and utility directories contain
GPU-specific implementations. Keep CPU and GPU changes together when a feature
is supported by both backends.

Executable front ends
---------------------

The ``qesWinds``, ``qesPlume``, ``qes``, and ``qesFire`` directories each
define a CMake executable target and contain its ``main`` function and
command-line argument handling. Add a command-line option to the argument
handler for the executable that owns the behavior, then update :doc:`Usage`.

Build configuration and dependencies
------------------------------------

Use ``CMakePresets.json`` and ``vcpkg.json`` for supported local builds and
dependency changes. Put reusable CMake logic in ``cmake``. See :doc:`Installation`
for the supported presets, vcpkg setup, and CHPC configuration.

Tests and example data
----------------------

Add automated coverage under ``tests`` and place the associated test input in
``testCases`` or ``data`` as appropriate. Use ``examples`` for small,
stand-alone demonstrations rather than regression coverage. ``paperData`` is
reserved for data associated with published studies and validation cases.

Generated and local files
-------------------------

CMake build directories, such as ``build``, ``buildMacOSDebug``, and
``buildUnixDebug``, are generated locally and must not be committed. Likewise,
do not commit local IDE settings, virtual environments, test caches, or run
output unless a file is intentionally part of a reproducible test case.

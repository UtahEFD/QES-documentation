Running QES
===========

The CMake build creates four user-facing executables. They are placed in
subdirectories of the build directory; for example,
``<build-dir>/qesWinds/qesWinds`` on macOS and Linux. On Windows, use the
corresponding ``.exe`` file. Run an executable with its help option to display
the options available in the version you built.

.. note::

   QES-Turb is not a standalone executable. Enable turbulence calculations
   with the ``-t`` option of ``qesWinds``, ``qes``, or ``qesFire``.

QES-Winds
---------

``qesWinds`` calculates a wind field and can optionally calculate turbulence.
The QES-Winds XML parameter file is required.

.. code-block:: console

   ./qesWinds/qesWinds -q <winds-parameters.xml> [options]

For example, the following runs the GPU dynamic-parallel wind solver, writes
the standard wind and workspace files, and uses ``gaussianHill`` as the output
basename:

.. code-block:: console

   ./qesWinds/qesWinds -q ../data/InputFiles/GaussianHill.xml -s 2 -w -o gaussianHill

Options
~~~~~~~~

* ``-h`` or ``--help``: display help and exit.
* ``-v`` or ``--verbose``: enable verbose output.
* ``-q <path>`` or ``--qesWindsParamFile <path>``: required QES-Winds XML
  parameter file.
* ``-s <1|2|3|4>`` or ``--solvetype <1|2|3|4>``: select the wind solver:

  * ``1``: CPU solver (the default);
  * ``2``: GPU dynamic-parallel solver;
  * ``3``: GPU global-memory solver; and
  * ``4``: GPU shared-memory solver.

  A build without CUDA always uses the CPU solver.
* ``-x`` or ``--windsolveroff``: skip wind solving and wind output.
* ``-t`` or ``--turbcomp``: calculate turbulent fields.
* ``-o <basename>`` or ``--outbasename <basename>``: basename for output
  files. Without it, all file output is disabled.
* ``-w`` or ``--wkout``: additionally write ``<basename>_windsWk.nc``.
* ``-m`` or ``--terrainout``: write the terrain mesh as
  ``<basename>_terrainOut.obj``.
* ``-f`` or ``--firemode``: write wind data back to the WRF input file.

When ``-o`` is supplied, the standard visualization output is
``<basename>_windsOut.nc``. With ``-t``, turbulence output is
``<basename>_turbOut.nc``.

QES-Plume
---------

``qesPlume`` runs QES-Plume in stand-alone mode. It requires a QES-Plume XML
parameter file and supports either a common project basename or individually
named Winds and turbulence input files.

.. code-block:: console

   ./qesPlume/qesPlume -p <plume-parameters.xml> (-f <project-basename> | -w <winds.nc> -t <turbulence.nc> -o <output-basename>) [options]

Using a common project basename, for example ``case``, reads
``case_windsWk.nc`` and ``case_turbOut.nc`` and writes ``case_plumeOut.nc``:

.. code-block:: console

   ./qesPlume/qesPlume -p plume.xml -f case

Options
~~~~~~~~

* ``-h`` or ``--help``: display help and exit.
* ``-v`` or ``--verbose``: enable verbose output.
* ``-g`` or ``--GPU``: enable GPU computation when QES was built with CUDA.
  It is ignored by a CPU-only build.
* ``-p <path>`` or ``--qesPlumeParamFile <path>``: required QES-Plume XML
  parameter file.
* ``-f <basename>`` or ``--projectQESFiles <basename>``: use a shared project
  basename for input and output. This selects ``<basename>_windsWk.nc`` and
  ``<basename>_turbOut.nc`` as input and writes ``<basename>_plumeOut.nc``.
* ``-w <path>`` or ``--inputWINDSFile <path>``: QES-Winds input file. Required
  when ``-f`` is not used.
* ``-t <path>`` or ``--inputTURBFile <path>``: turbulence input file. Required
  when ``-f`` is not used.
* ``-o <basename>`` or ``--outputbasename <basename>``: output basename.
  Required when ``-f`` is not used; QES-Plume writes
  ``<basename>_plumeOut.nc``.
* ``-l`` or ``--particleOutput``: also write debug particle data as
  ``<basename>_particleInfo.nc``.

QES
---

``qes`` is the coupled driver for QES-Winds, optional QES-Turb, and optional
QES-Plume. Supplying a QES-Plume parameter file enables QES-Plume and also
enables the turbulence calculation required by Plume.

.. code-block:: console

   ./qes/qes -q <winds-parameters.xml> [-p <plume-parameters.xml>] [options]

For example, this runs QES-Winds, QES-Turb, and QES-Plume with a common output
basename:

.. code-block:: console

   ./qes/qes -q winds.xml -p plume.xml -s 2 -o case

Options
~~~~~~~~

* ``-h`` or ``--help``: display help and exit.
* ``-v`` or ``--verbose``: enable verbose output.
* ``-q <path>`` or ``--qesWindsParamFile <path>``: required QES-Winds XML
  parameter file.
* ``-p <path>`` or ``--qesPlumeParamFile <path>``: QES-Plume XML parameter
  file. Its presence enables QES-Plume and turbulence computation.
* ``-t`` or ``--turbcomp``: calculate turbulent fields. If Plume is enabled,
  this flag controls whether the turbulence NetCDF file is written; turbulence
  is calculated in either case.
* ``-g <on|off>`` or ``--plumegpu <on|off>``: choose the QES-Plume backend.
  By default Plume follows the Winds/Turb solver backend. ``on`` requires a
  CUDA build and a GPU wind solver.
* ``-s <1|2|3|4>`` or ``--solvetype <1|2|3|4>``: choose the CPU (``1``), GPU
  dynamic-parallel (``2``), GPU global-memory (``3``), or GPU shared-memory
  (``4``) wind solver. CPU-only builds force ``1``.
* ``-x`` or ``--windsolveroff``: skip wind solving and wind output.
* ``-o <basename>`` or ``--outbasename <basename>``: basename for output
  files. Without it, all file output is disabled.
* ``-w`` or ``--wkout``: write ``<basename>_windsWk.nc``.
* ``-m`` or ``--terrainout``: write ``<basename>_terrainOut.obj``.
* ``-l`` or ``--particleOutput``: when Plume is enabled, write
  ``<basename>_particleInfo.nc``.
* ``-z`` or ``--visuout``: accepted for compatibility. Visualization output is
  currently enabled automatically whenever ``-o`` is supplied.

With an output basename, ``qes`` writes ``<basename>_windsOut.nc``. It also
writes ``<basename>_turbOut.nc`` when turbulence output is enabled and
``<basename>_plumeOut.nc`` when Plume is enabled.

QES-Fire
--------

``qesFire`` is the coupled fire driver. It runs the fire model with QES-Winds
and can also use QES-Turb and QES-Plume. Provide the QES-Winds parameter file
and an output basename; provide the QES-Plume parameter file when using Plume.

.. code-block:: console

   ./qesFire/qesFire -q <winds-parameters.xml> -o <output-basename> [options]

Options
~~~~~~~~

* ``-?`` or ``--help``: display help and exit.
* ``-v`` or ``--verbose``: enable verbose output.
* ``-q <path>`` or ``--qesWindsParamFile <path>``: QES-Winds XML parameter
  file.
* ``-p <path>`` or ``--qesPlumeParamFile <path>``: QES-Plume XML parameter
  file; enables QES-Plume and turbulence computation.
* ``-t`` or ``--turbcomp``: calculate turbulent fields.
* ``-s <1|2|3|4>`` or ``--solvetype <1|2|3|4>``: choose the CPU (``1``), GPU
  dynamic-parallel (``2``), GPU global-memory (``3``), or GPU shared-memory
  (``4``) wind solver. CPU-only builds force ``1``.
* ``-x`` or ``--windsolveroff``: skip wind solving and wind output.
* ``-o <basename>`` or ``--outbasename <basename>``: basename for output
  files.
* ``-z`` or ``--visuout``: accepted for compatibility. Visualization output is
  currently enabled automatically whenever ``-o`` is supplied.
* ``-w`` or ``--wkout``: write ``<basename>_windsWk.nc``.
* ``-h`` or ``--terrainout``: write ``<basename>_terrainOut.obj``.
* ``-l`` or ``--doParticleDataOutput``: request debug Lagrangian particle
  output when Plume is enabled. The current argument handling registers this
  option but does not enable particle output.
* ``-b`` or ``--fireout``: write ``<basename>_fireOutput.nc``.
* ``-i`` or ``--fireWindsOff``: disable fire-induced winds.

With an output basename, standard wind visualization output is
``<basename>_windsOut.nc``. QES-Fire also writes the turbulence and Plume
outputs described for ``qes`` when those models are enabled.

Running on CHPC
---------------

Run QES on CHPC through a Slurm job. Place the script in a ``run`` directory
beside the build directory and adapt the account, partition, GPU, and time
settings to your allocation. The module versions should match the build; see
:doc:`Installation` for the current tested CHPC configuration.

.. code-block:: bash

   #!/bin/bash
   #SBATCH --account=efd-np
   #SBATCH --partition=efd-shared-np
   #SBATCH --job-name=qesGaussian
   #SBATCH --nodes=1
   #SBATCH --mem=15G
   #SBATCH --gres=gpu:1
   #SBATCH --time=01:00:00
   #SBATCH --error=init_error.log
   #SBATCH --output=init_out.log

   source ../CHPC/loadmodules_QES.sh
   ../build/qesWinds/qesWinds -q ../data/InputFiles/GaussianHill.xml -s 2 -w -o gaussianHill

Submit the job from the ``run`` directory:

.. code-block:: console

   sbatch rGaussianHill_gpu.slurm

Testing QES
-----------

Use CTest from the configured build directory:

.. code-block:: console

   ctest
   ctest --verbose
   ctest -N
   ctest -R <test-name>

Enable sanity and GPU tests during configuration with:

.. code-block:: console

   cmake -DENABLE_SANITY_TESTS=ON -DENABLE_GPU_TESTS=ON ..

Enable unit tests with:

.. code-block:: console

   cmake -DENABLE_UNITTESTS=ON ..

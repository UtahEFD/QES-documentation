Running QES
===========

The command to run the QES-Winds executable created above is:

::

   ./qesWinds/qesWinds -q [address to XML file] -o [output file] -s [solver type] -z [Visualization output]

At least three elements need to be addressed: input XML file, output
file name and type of solver. The input XML file defines various
variables necessary for running the code. Input files are usually
located in ``QES-Winds/data/InputFiles`` and defined in command line by
``-q``.

::

   [address to XML file] = QES-Winds/data/InputFiles/XMLfilename

User can change the name of output file by ``-o outputname``. QES-Winds
has four solver types: solving on CPU (determined by ``-s 1``), solving
SOR equation on GPU using dynamic parallelism (determined by ``-s 2``),
GPU solver using global memory (determined by ``-s 3``) and GPU solver
using shared memory (determined by ``-s 4``). GPU solvers are much
faster than CPU solver and are highly recommended especially for large
domains.

Turbulence model can be turned on by using ``-t``.

More info about the arguments supported by QES-Winds can be display
using:

::

   ./qesWinds/qesWinds -?

More info about the arguments supported by QES-Plume (stand-alone) can
be display using:

::

   ./qesPlume/qesPlume -?

More info about the arguments supported by QES (QES-Winds – QES-Plume
dynamic coupling) can be display using:

::

   ./qes/qes -?

Running from the Command Line
-----------------------------

QES is run from the terminal using arguments. For exmaple:

::

   ./qesWinds/qesWinds -q ../data/InputFiles/GaussianHill.xml -s 2 -w -o gaussianHill

slurm Template (for CUDA 11.4 build)
------------------------------------

To run QES-Winds, you can take the following slurm template and run on
CHPC. We’d suggest placing it in a ``run`` folder at the same level as
your build folder. Make sure you change the various sbatch parameters as
needed for your access to CHPC.

.. code:: bash

   #!/bin/bash
   #SBATCH --account=efd-np
   #SBATCH --partition=efd-shared-np
   #SBATCH --job-name=qesGaussian
   #SBATCH --nodes=1
   #SBATCH --mem=15G
   #SBATCH --gres=gpu:titanv:1
   #SBATCH --time=01:00:00
   #SBATCH -e init_error.log
   #SBATCH -o init_out.log
   module load gcc/8.5.0
   ulimit -c unlimited -s
   ./qesWinds/qesWinds -q ../data/InputFiles/GaussianHill.xml -s 2 -w -o gaussianHill

Note that if you build with a different GCC (e.g. 5.4.0), you will need
to change the module load to use that version of GCC. Once the slurm
file has been placed in the run folder, you can then send out the job.
For example, assuming you are in the build folder and just built the
code and we saved the slurm template above as a file
``rGaussianHill_gpu.slurm``:

::

   make clean
   make
   cd ../run
   sbatch rGaussianHill_gpu.slurm

This will create the various NetCDF output files in the run folder,
along with any output in the ``init_error.log`` and ``init_out.log``
files.

Testing QES
-----------

We are using ctest to conduct unit tests and sanity check on the code.
Here are a few commands:

::

   ctest           # launch all tests
   ctest --verbose     # launch all tests with verbose (see commant output)
   ctest -N        # get list of tests
   ctest -R $testname  # launch only $testname

Here is a list of tests and testing option. Most test require manuel
inspection of the results. Recursive testing will be implemented in the
future.

QES-Winds Tests
~~~~~~~~~~~~~~~

Test for QES-Winds are designed to check that to code is still running
under a given set of parameters. These tests do not guarentee the
validity of the results. To turn on the basic QES-wind test, use:

::

   cmake -DENABLE_SANITY_TESTS=ON -DENABLE_GPU_TESTS=ON ..

The QES-Winds sanity tests are: - GPU-FlatTerrain: basic empty domain
test - GPU-GaussianHill: basic terrain test - GPU-OklahomaCity: coarse
resolution shapefile reader (without parameterization) -
GPU-MultiSensors: test of multiple sensor and multiple timesteps -
GPU-SaltLakeCity: test of high resolution urban setup with
parameterizations - GPU-RxCADRE: test of high resolution and complex
terrain (DEM)

QES-Turb Tests
~~~~~~~~~~~~~~

There currently is no automated test available for QES-Turb.

QES-Plume Tests
~~~~~~~~~~~~~~~

There currently is no automated test available for QES-Plume. The
following test cases are available - testing well-mixed condition:
``Sinusoidal3D`` ``Channel3D`` ``BaileyLES`` - testing against
analitical soluation: ``UniformFlow_ContRelease``
``PowerLawBLFlow_ContRelease`` - testing against wind-tunnel data:
``EPA_7x11array``

Unit Tests
~~~~~~~~~~

Unit tests can be enable by settong the flag ``ENABLE_UNITTESTS`` to
``ON``.

::

   cmake -DENABLE_UNITTESTS=ON ..

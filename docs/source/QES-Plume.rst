QES-Plume
=========

Introduction
------------

QES-Plume is a Lagrangian stochastic dispersion model for passive tracers.
It advances particles through a steady mean wind field while representing
turbulent velocity fluctuations with the generalized Langevin equations. The
implementation uses a time-implicit integration scheme and a Courant-based
substep to keep particle motion compatible with the QES-Winds grid
:cite:`Margairaz2023`.

QES-Plume normally uses the wind field from QES-Winds and the Reynolds-stress
tensor, stress-tensor divergence, and dissipation rate from QES-Turb. It can
also run stand-alone from previously written QES-Winds workspace and QES-Turb
NetCDF files. Sources emit particles; concentration is calculated by
time-averaging particle mass in user-defined sampling boxes.

Running QES-Plume
-----------------

For a coupled run, provide a QES-Winds XML file, a QES-Plume XML file, and an
output basename to the ``qes`` executable:

.. code:: bash

   ./qes/qes -q winds.xml -p plume.xml -o case

The coupled executable computes the required turbulence fields when a plume
parameter file is supplied. Add ``-t`` when the turbulence output file is also
needed after the run.

For a stand-alone run, use matching QES-Winds workspace and QES-Turb output
files. The ``-f`` form uses one common basename:

.. code:: bash

   ./qesPlume/qesPlume -p plume.xml -f case

This reads ``case_windsWk.nc`` and ``case_turbOut.nc``. Alternatively,
provide the input files and output basename separately:

.. code:: bash

   ./qesPlume/qesPlume -p plume.xml -w winds_workspace.nc \
       -t turbulence.nc -o case

Use ``-l`` to request particle diagnostic output. The XML must include
``particleOutputParameters`` when this option is used.

Parameter files
---------------

The root element is ``QESPlumeParameters``. The required sections are
``plumeParameters``, ``collectionParameters``, and ``boundaryConditions``.
``particleParameters`` defines one or more particle models and their sources.

.. code:: xml

   <QESPlumeParameters>
       <plumeParameters>
           <simDur>600.0</simDur>
           <timeStep>1.0</timeStep>
           <CourantNumber>0.5</CourantNumber>
           <invarianceTol>1e-5</invarianceTol>
           <updateFrequency_particleLoop>10000</updateFrequency_particleLoop>
           <updateFrequency_timeLoop>60</updateFrequency_timeLoop>
           <!-- Optional: triLinear (default), nearestCell,
                or analyticalPowerLaw -->
           <interpolationMethod>triLinear</interpolationMethod>
       </plumeParameters>

       <collectionParameters>
           <timeAvgStart>0.0</timeAvgStart>
           <timeAvgFreq>60.0</timeAvgFreq>
           <boxBoundsX1>0.0</boxBoundsX1>
           <boxBoundsX2>200.0</boxBoundsX2>
           <boxBoundsY1>0.0</boxBoundsY1>
           <boxBoundsY2>200.0</boxBoundsY2>
           <boxBoundsZ1>0.0</boxBoundsZ1>
           <boxBoundsZ2>100.0</boxBoundsZ2>
           <nBoxesX>40</nBoxesX>
           <nBoxesY>40</nBoxesY>
           <nBoxesZ>20</nBoxesZ>
       </collectionParameters>

        <boundaryConditions>
            <!-- Options: exiting, periodic, reflection -->
            <xBCtype>exiting</xBCtype>
            <yBCtype>exiting</yBCtype>
            <zBCtype>exiting</zBCtype>

            <!-- Optional: doNothing (default), setInactive, stairstepReflection,
                meshReflection -->
            <wallReflection>stairstepReflection</wallReflection>
        </boundaryConditions>

       <particleParameters>
           <baseParticle>
               <tag>tracer</tag>
               <source>
                   <!-- Physical properties apply to this source -->
                   <particleDensity>1000.0</particleDensity>
                   <particleDiameter>10.0</particleDiameter>
                   <releaseType_continuous>
                       <particlePerTimestep>100</particlePerTimestep>
                   </releaseType_continuous>
                   <sourceGeometry_Point>
                       <posX>20.0</posX>
                       <posY>50.0</posY>
                       <posZ>10.0</posZ>
                   </sourceGeometry_Point>
               </source>
           </baseParticle>
       </particleParameters>

   </QESPlumeParameters>

Plume parameters (plumeParameters)
-----------------------------------

``simDur`` and ``timeStep`` are the simulation duration and maximum
integration time step in seconds. ``CourantNumber`` must be between zero and
one; QES-Plume uses it to reduce the particle time step near walls.
``invarianceTol`` is the tolerance used when checking that the interpolated
stress tensor is realizable. The two ``updateFrequency`` fields control
progress reporting only.

``interpolationMethod`` is optional. ``triLinear`` is the default and is the
normal choice for QES-Winds and QES-Turb fields. ``nearestCell`` selects the
cell containing the particle, and ``analyticalPowerLaw`` is intended for
analytical boundary-layer test cases.

Concentration collection (collectionParameters)
------------------------------------------------

The collection bounds define the concentration sampling volume in metres.
``nBoxesX``, ``nBoxesY``, and ``nBoxesZ`` subdivide it into sampling boxes.
``timeAvgStart`` sets when time averaging begins and ``timeAvgFreq`` sets the
averaging and concentration-output period, both in seconds. The collection
region should lie within the QES-Winds domain.

Boundary conditions
-------------------

Set ``xBCtype``, ``yBCtype``, and ``zBCtype`` independently to control what
happens when a particle leaves the corresponding domain direction.
``wallReflection`` controls particle interaction with terrain and buildings.
It is optional; omit it to use ``doNothing``. ``meshReflection`` requires a
triangular mesh in the QES-Winds input.

.. code:: xml

   <boundaryConditions>
       <!-- Options: exiting, periodic, reflection -->
       <xBCtype>exiting</xBCtype>
       <yBCtype>exiting</yBCtype>
       <zBCtype>exiting</zBCtype>

       <!-- Optional: doNothing (default), setInactive, stairstepReflection,
            meshReflection -->
       <wallReflection>stairstepReflection</wallReflection>
   </boundaryConditions>


Particle models and sources
---------------------------

Each ``baseParticle`` needs a unique ``tag``. QES-Plume creates one
concentration NetCDF file per tag, named ``<basename>_<tag>_plumeOut.nc``.
One particle model can contain multiple ``source`` elements.

Particle properties and deposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Physical properties are set within each ``source`` so that sources in the
same particle model can use different particles. Specify
``particleDensity`` in kg m\ :sup:`-3` and ``particleDiameter`` in micrometres.
Provide both fields for every source, including passive tracer releases.

Set ``depositionFlag`` in ``baseParticle`` to enable canopy and ground
deposition. With deposition enabled, QES-Plume transfers particle mass to the
deposition field and writes it with the concentration statistics. The optional
``c1`` and ``c2`` parameters control the canopy-deposition efficiency; their
defaults are ``2.049`` and ``1.19``. The optional ``decayConst`` field is
accepted by the XML interface but is not currently applied to particle mass.

.. code:: xml

   <baseParticle>
       <tag>coarse_aerosol</tag>
       <depositionFlag>true</depositionFlag>
       <!-- Optional canopy-deposition constants -->
       <c1>2.049</c1>
       <c2>1.19</c2>
       <!-- Accepted but not currently applied -->
       <!-- <decayConst>0.0</decayConst> -->
       <source>
           <particleDensity>1000.0</particleDensity>
           <particleDiameter>10.0</particleDiameter>
           <!-- Add exactly one release type and one geometry here. -->
       </source>
   </baseParticle>

Each source requires exactly one release type and one geometry. Available
release types are ``releaseType_continuous``, ``releaseType_duration``, and
``releaseType_instantaneous``. Continuous releases require
``particlePerTimestep`` and can optionally specify ``releaseStartTime``.
Duration releases require ``releaseStartTime``, ``particlePerTimestep``, and
either ``releaseEndTime`` or ``releaseDuration``. Instantaneous releases
require ``numPar`` and can optionally specify ``releaseTime``.

Available source geometries are ``sourceGeometry_Point``,
``sourceGeometry_Line``, ``sourceGeometry_Cube``,
``sourceGeometry_SphereShell``, and ``sourceGeometry_FullDomain``. Point
sources use ``posX``, ``posY``, and ``posZ``. Use the corresponding endpoint,
bound, or radius fields for line, cube, and spherical-shell geometries.

Add exactly one release type and one geometry to each ``source`` element.
The following snippets show every available option. Include
``particleDensity`` and ``particleDiameter`` beside the selected snippets.

Release types
~~~~~~~~~~~~~

Continuous release
^^^^^^^^^^^^^^^^^^

.. code:: xml

   <releaseType_continuous>
       <particlePerTimestep>100</particlePerTimestep>
       <!-- Optional: release begins at t = 0 by default -->
       <releaseStartTime>0.0</releaseStartTime>
       <!-- Optional mass specification; choose at most one -->
       <!-- <massPerSec>1.0</massPerSec> -->
       <!-- <massPerTimestep>1.0</massPerTimestep> -->
   </releaseType_continuous>

Duration release
^^^^^^^^^^^^^^^^

.. code:: xml

   <releaseType_duration>
       <releaseStartTime>60.0</releaseStartTime>
       <releaseDuration>120.0</releaseDuration>
       <particlePerTimestep>100</particlePerTimestep>
       <!-- Alternatively use releaseEndTime instead of releaseDuration. -->
       <!-- <releaseEndTime>180.0</releaseEndTime> -->
       <!-- Optional mass specification; choose at most one -->
       <!-- <totalMass>10.0</totalMass> -->
       <!-- <massPerSec>0.08333</massPerSec> -->
   </releaseType_duration>

Instantaneous release
^^^^^^^^^^^^^^^^^^^^^

.. code:: xml

   <releaseType_instantaneous>
       <releaseTime>0.0</releaseTime>
       <numPar>10000</numPar>
       <!-- Optional total mass represented by the release -->
       <!-- <totalMass>10.0</totalMass> -->
   </releaseType_instantaneous>

Source geometries
~~~~~~~~~~~~~~~~~

Point source
^^^^^^^^^^^^

.. code:: xml

   <sourceGeometry_Point>
       <posX>20.0</posX>
       <posY>50.0</posY>
       <posZ>10.0</posZ>
   </sourceGeometry_Point>

Line source
^^^^^^^^^^^

.. code:: xml

   <sourceGeometry_Line>
       <posX_0>20.0</posX_0>
       <posY_0>20.0</posY_0>
       <posZ_0>10.0</posZ_0>
       <posX_1>20.0</posX_1>
       <posY_1>80.0</posY_1>
       <posZ_1>10.0</posZ_1>
   </sourceGeometry_Line>

Cube source
^^^^^^^^^^^

.. code:: xml

   <sourceGeometry_Cube>
       <minX>20.0</minX>
       <minY>40.0</minY>
       <minZ>5.0</minZ>
       <maxX>30.0</maxX>
       <maxY>50.0</maxY>
       <maxZ>15.0</maxZ>
   </sourceGeometry_Cube>

Spherical-shell source
^^^^^^^^^^^^^^^^^^^^^^

.. code:: xml

   <sourceGeometry_SphereShell>
       <posX>25.0</posX>
       <posY>50.0</posY>
       <posZ>10.0</posZ>
       <radius>5.0</radius>
   </sourceGeometry_SphereShell>

Full-domain source
^^^^^^^^^^^^^^^^^^

.. code:: xml

   <sourceGeometry_FullDomain>
   </sourceGeometry_FullDomain>

Output
------


The concentration file contains the time-averaged concentration on the
sampling grid. If particle diagnostics are requested with ``-l``, add the
following optional section to control CSV snapshots of active particles:

.. code:: xml

   <particleOutputParameters>
       <outputStartTime>0.0</outputStartTime>
       <outputFrequency>60.0</outputFrequency>
   </particleOutputParameters>

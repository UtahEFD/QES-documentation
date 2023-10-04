QES-Plume
=========

The model
---------

The XML file
------------

.. code:: xml

   <QESPlumeParameters>
     <plumeParameters>
       <!--....-->
     </plumeParameters>
     <collectionParameters>
       <!--....-->
     </collectionParameters>
     <sourceParameters>
      <!--....-->
     </sourceParameters>
     <boundaryConditions>
       <!--....-->
     </boundaryConditions>
   </QESPlumeParameters>

Simulation Parameters
~~~~~~~~~~~~~~~~~~~~~

The parameters below are the parameters used to run the Plume model.

.. code:: xml

   <simulationParameters>
       <simDur> 1000.0 </simDur>   <!-- Total simulation time -->
       <timeStep> 0.1 </timeStep>  <!-- time step -->
       <CourantNumber> 0.5 </CourantNumber>
       <invarianceTol> 1e-10 </invarianceTol>
       <C_0> 4.0 </C_0>
       <updateFrequency_particleLoop> 10000 </updateFrequency_particleLoop>
       <updateFrequency_timeLoop> 100 </updateFrequency_timeLoop>
   </simulationParameters>

Collection Parameters
~~~~~~~~~~~~~~~~~~~~~

The parameters below are the parameters used to calculate the
concentration of particle (in #particles/m\ :math:`^{3}`). All
parameters are in SI units by default (second and meters). The size of
collection area should be set smaller or equal to the domain.

.. code:: xml

   <collectionParameters>
       <timeAvgStart> 0.0 </timeAvgStart>  <!-- time to start calc of concentration -->
       <timeAvgFreq> 60.0 </timeAvgFreq>   <!-- averaging period -->
       <boxBoundsX1> 0.0 </boxBoundsX1>    <!-- beginning of collection area -->
       <boxBoundsX2> 200.0 </boxBoundsX2>  <!-- end of collection area -->
       <boxBoundsY1> 0.0 </boxBoundsY1>
       <boxBoundsY2> 200.0 </boxBoundsY2>
       <boxBoundsZ1> 0.0 </boxBoundsZ1>
       <boxBoundsZ2> 200.0 </boxBoundsZ2>
       <nBoxesX> 200 </nBoxesX>            <!-- resolution of concentration -->
       <nBoxesY> 200 </nBoxesY>
       <nBoxesZ> 200 </nBoxesZ>
   </collectionParameters>

Source Parameters
~~~~~~~~~~~~~~~~~

.. code:: xml

   <sourceParameters>
     <source>
       <sourceStrength> 10 </sourceStrength>
       <!-- HERE COME THE GEOMETRY -->
       <!-- HERE COME THE RELEASE TYPE -->
       <!-- HERE COME THE PARTICLE TYPE -->
     </sources>
   </sourceParameters>

Source Geometry
^^^^^^^^^^^^^^^

.. code:: xml

   <sourceGeometry_Point>
       <posX> 40.0 </posX>
       <posY> 80.0 </posY>
       <posZ> 30.0 </posZ>
   </sourceGeometry_Point>

.. code:: xml

   <sourceGeometry_Line>
       <posX_0> 25.0 </posX_0>
       <posY_0> 175.0 </posY_0>
       <posZ_0> 40.0 </posZ_0>
       <posX_1> 50.0 </posX_1>
       <posY_1> 25.0 </posY_1>
       <posZ_1> 40.0 </posZ_1>
   </sourceGeometry_Line>

.. code:: xml

   <sourceGeometry_Cube>
       <minX> 75.0 </minX>
       <minY> 25.0 </minY>
       <minZ> 70.0 </minZ>
       <maxX> 80.0 </maxX>
       <maxY> 35.0 </maxY>
       <maxZ> 80.0 </maxZ>
   </sourceGeometry_Cube>

.. code:: xml

   <sourceGeometry_SphereShell>
       <posX> 40.0 </posX>
       <posY> 80.0 </posY>
       <posZ> 30.0 </posZ>
       <radius> 30.0 </radius>
   </sourceGeometry_SphereShell>

.. code:: xml

   <sourceGeometry_FullDomain>
   </sourceGeometry_FullDomain>

Release types
^^^^^^^^^^^^^

.. code:: xml

   <releaseType_continuous>
     <parPerTimestep>10</parPerTimestep>
   </releaseType_continuous>

.. code:: xml

   <releaseType_duration>
     <releaseEndTime>0</releaseEndTime>
     <releaseEndTime>5</releaseEndTime>
     <parPerTimestep>10</parPerTimestep>
   </releaseType_duration>

.. code:: xml

   <releaseType_instantaneous>
     <numPar>100000</numPar>
   </releaseType_instantaneous>

Particle types
^^^^^^^^^^^^^^

.. code:: xml

   <particleTracer>
   </particleTracer>

.. code:: xml

   <particleSmall>
     <particleDensity> 2.0 </particleDensity>
     <particleDiameter> 5 </particleDiameter>
     <depositionFlag>false</depositionFlag>
     <decayConst> 0.0 </decayConst>
   </particleSmall>

Boundary Conditions
~~~~~~~~~~~~~~~~~~~

.. code:: xml

   <boundaryConditions>
     <xBCtype>exiting</xBCtype>
     <yBCtype>exiting</yBCtype>
     <zBCtype>exiting</zBCtype>
     <wallReflection>stairstepReflection</wallReflection>
   </boundaryConditions>

Here are the option of the boundary conditions types:

-  ``exiting`` particle exit the domain

-  ``periodic`` particle reenter the domain at the other side

-  ``reflection`` particle is reflected from the domain boundary (works
   only of domain ends)

Here are the option of the wall reflections methods

-  ``doNothing`` nothing happen when particle enter wall

-  ``setInactive`` (default) particle is set to inactive when entering a
   wall

-  ``stairstepReflection`` particle use full stair step reflection when
   entering a wall

Full XML Example
~~~~~~~~~~~~~~~~

.. code:: xml

   <QESPlumeParameters>
     <plumeParameters>
       <simDur> 1000.0 </simDur>
       <timeStep> 0.1 </timeStep>
       <CourantNumber> 1 </CourantNumber>
       <invarianceTol> 1e-10 </invarianceTol>
       <C_0> 1.0 </C_0>
       <updateFrequency_particleLoop> 10000 </updateFrequency_particleLoop>
       <updateFrequency_timeLoop> 100 </updateFrequency_timeLoop>
     </plumeParameters>
     <collectionParameters>
       <timeAvgStart> 0.0 </timeAvgStart>
       <timeAvgFreq> 60.0 </timeAvgFreq>
       <boxBoundsX1> 0.0 </boxBoundsX1>
       <boxBoundsX2> 200.0 </boxBoundsX2>
       <boxBoundsY1> 0.0 </boxBoundsY1>
       <boxBoundsY2> 200.0 </boxBoundsY2>
       <boxBoundsZ1> 0.0 </boxBoundsZ1>
       <boxBoundsZ2> 200.0 </boxBoundsZ2>
       <nBoxesX> 200 </nBoxesX>
       <nBoxesY> 200 </nBoxesY>
       <nBoxesZ> 200 </nBoxesZ>
     </collectionParameters>
     <sourceParameters>
       <source>
         <releaseType_continuous>
           <parPerTimestep> 100 </parPerTimestep>
         </releaseType_continuous>
         <sourceGeometry_Point>
           <posX> 15 </posX>
           <posY> 30 </posY>
           <posZ> 1.5 </posZ>
         </sourceGeometry_Point>
       </source>
     </sourceParameters>
     <boundaryConditions>
       <xBCtype>exiting</xBCtype>
       <yBCtype>exiting</yBCtype>
       <zBCtype>exiting</zBCtype>
       <wallReflection>stairstepReflection</wallReflection>
     </boundaryConditions>
   </QESPlumeParameters>

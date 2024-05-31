QES-Turb
========

The model
---------

Coming soon ...

The XML file
------------

Note that the turbulence parameters goes in the QES-Winds parameters
file (see below)

.. code:: xml

   <QESWindsParameters>
       ...
       <turbParams>
           <method>3</method>      <!-- Mixing length method (0-height, 1-serial, 2-raytracing, 3-OptiX, 4-file) -->
           <samples>2000</samples> <!-- Samples per air cell for ray-traced mixing length calculations -->
           <nonLocalMixing>true/false<nonLocalMixing>
           <terrainWallFlag>2<terrainWallFlag>
           <buildingWallFlag>2<buildingWallFlag>
           <turbUpperBound>10<turbUpperBound>
           <backgroundMixing>0.3<backgroundMixing>
           <sigmaConst>2.5 2.0 1.3<sigmaConst>
       </turbParams>                           
       ...
   </QESWindsParameters>

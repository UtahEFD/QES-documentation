QES-Turb
========

Introduction
------------

QES-Turb computes turbulence fields from the wind field produced by
QES-Winds. It is enabled as part of a QES-Winds or coupled QES run; it is
not a separate executable. The model derives velocity gradients and a local
mixing length, then produces Reynolds-stress components, turbulent kinetic
energy, and a dissipation-rate field :cite:`Margairaz2023`. These fields can be used by QES-Plume.

Run QES-Winds with the ``-t`` option to enable the turbulence computation.
The QES-Winds XML file must then include a ``turbParams`` section. When an
output basename is supplied with ``-o``, QES-Turb writes
``<basename>_turbOut.nc``.

The turbulence model
--------------------

QES-Turb uses the QES-Winds domain, terrain, buildings, and wind field. A
local mixing length is defined for fluid cells, and wall treatments are
applied at terrain and building surfaces. The local mixing length determines
the length scale used to calculate the turbulence quantities.

Local mixing length
~~~~~~~~~~~~~~~~~~~

The ``method`` parameter selects the local mixing-length treatment:

* ``0`` uses height above terrain. This is the default local method.
* ``1`` computes a serial, geometry-aware mixing length.
* ``3`` uses OptiX ray tracing when QES was built with OptiX support. Without
  OptiX support, QES automatically falls back to method ``1``.
* ``4`` reads a mixing-length field from a NetCDF file.

Method ``2`` is reserved and is not currently available. Methods ``1`` and
``3`` can save a calculated mixing-length field for later reuse. Method ``4``
requires the corresponding NetCDF file.

Parameter files
---------------

The turbulence parameters are part of the QES-Winds parameter file, under
``QESWindsParameters``. ``method`` is required; the remaining parameters are
optional and use the defaults noted below.

.. code:: xml

   <QESWindsParameters>
       <!-- QES-Winds parameters ... -->
       <turbParams>
           <!-- Local mixing-length method: 0-height, 1-serial,
                3-OptiX, 4-NetCDF file -->
           <method>1</method>

           <!-- Optional wall-gradient treatments: 1-log law, 2-finite
                difference (default) -->
           <terrainWallFlag>2</terrainWallFlag>
           <buildingWallFlag>2</buildingWallFlag>

           <!-- Optional turbulence controls -->
           <nonLocalMixing>false</nonLocalMixing>
           <turbUpperBound>20.0</turbUpperBound>
           <backgroundMixing>0.0</backgroundMixing>
           <sigmaConst>2.5 2.0 1.3</sigmaConst>

           <!-- Required for method 4; also used to save the calculated
                mixing length when save is true -->
           <!-- <LMfile>mixing_length.nc</LMfile> -->
           <!-- <varname>mixlength</varname> -->
           <!-- <save>true</save> -->
           <!-- <samples>2000</samples> -->
       </turbParams>
   </QESWindsParameters>

Turbulence parameters (turbParams)
-----------------------------------

``nonLocalMixing`` enables non-local building mixing; it defaults to
``false``. ``terrainWallFlag`` and ``buildingWallFlag`` select the wall
treatment independently. A value of ``1`` uses a logarithmic wall law and a
value of ``2`` uses finite differences; both default to ``2``.

``turbUpperBound`` limits the turbulence fields and defaults to ``20.0``.
``backgroundMixing`` adds a uniform background velocity scale and defaults to
``0.0``. ``sigmaConst`` accepts three values for the velocity-fluctuation
constants. If it is omitted, QES uses its internal defaults.

For method ``4``, set ``LMfile`` to the NetCDF file and use ``varname`` to
select the mixing-length variable (``mixlength`` by default). For an OptiX
run, ``samples`` sets the number of samples per air cell; its default is
``2000``.

Output
------

The turbulence output NetCDF file is written when QES-Turb is enabled and an
output basename is supplied. It contains the local mixing length, velocity
gradient tensor, Reynolds-stress tensor, turbulent kinetic energy,
dissipation rate, and stress-tensor divergence on the cell-centred turbulence
grid.

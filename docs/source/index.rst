Welcome to QES's documentation!
===================================

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg?style=svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.7098279.svg?style=svg
   :target: https://doi.org/10.5281/zenodo.7098279


Behnam Bozorgmehr |orcid_bb|, Jeremy A Gibbs |orcid_jg|, Fabien Margairaz |orcid_fm|, Lucas Ulmer |orcid_lu|,
Eric R Pardyjak |orcid_ep|, Rob Stoll |orcid_rs|, Pete Willemsen

.. |orcid_bb| image:: https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png
    :target: https://orcid.org/0000-0003-1633-8383

.. |orcid_fm| image:: https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png
    :target: https://orcid.org/0000-0003-0208-3455

.. |orcid_rs| image:: https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png
    :target: https://orcid.org/0000-0002-4777-6944

.. |orcid_ep| image:: https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png
    :target: https://orcid.org/0000-0002-0180-0857

.. |orcid_jg| image:: https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png
    :target: https://orcid.org/0000-0001-9340-2663

.. |orcid_lu| image:: https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png
    :target: https://orcid.org/0000-0002-8887-5738



The Quick Environmental Simulation (**QES**) code is a low-computational-cost
framework designed to compute high-resolution wind and concentration fields in
complex atmospheric-boundary-layer environments.

The modules are the following:

* **QES-Winds** is the new wind model computing divergence-free steady-state 3D wind field in complex domain.

* **QES-TURB** is a stand-alone turbulence model that computes turbulence fields from the calculated wind field in QES-Winds.

* **QES-Plume** is a stand-alone Lagrangian dispersion model with the ability to calculate spatially and temporally varying scalar concentrations.

* **QES-Fire** is a fire-spread model.

* **QES-Transport** is a transport model (to be implemented)

.. warning::
   **QES requires a NVIDIA GPU with Compute Capability of 7.0 (or higher)**.


.. note::
   * the latest version of the document corresponds to the private version of QES.
   * if using the public version of QES, please select the corresponding release version in the bottom left corner (ex. v2.1.0).


.. toctree::
   :maxdepth: 2
   :caption: User Guide

   GettingStarted
   Installation
   Usage

.. toctree::
   :maxdepth: 2
   :caption: Technical Guide

   QES-Winds
   QES-Turb
   QES-Plume

.. toctree::
   :maxdepth: 2
   :caption: References

   References

Publications
------------

-  QES-Winds: Dynamic Parallelism Solver
  Bozorgmehr, B., Willemsen, P., Gibbs, J.A., Stoll, R., Kim, J.-J.,
  Pardyjak, E.R., 2021. Utilizing dynamic parallelism in CUDA to
  accelerate a 3D red-black successive over relaxation wind-field
  solver. Environ Modell Softw 137, 104958.
  https://doi.org/10.1016/j.envsoft.2021.104958

-  QES-Winds: Isolated Tree Model
  Margairaz, F., Eshagh, H., Hayati, A.N., Pardyjak, E.R., Stoll, R.,
  2022. Development and evaluation of an isolated-tree flow model for
  neutral-stability conditions. Urban Clim 42, 101083.
  https://doi.org/10.1016/j.uclim.2022.101083

-  QES-Winds: Raw-Oriented Canopy Model
  Ulmer, L., Margairaz, F., Bailey, B.N., Mahaffee, W.F., Pardyjak,
  E.R., Stoll, R., 2022. A fast-response, wind angle-sensitive model
  for predicting mean winds in row-organized canopies. Agric. For.
  Meteorol. 329, 109273.
  https://doi.org/10.1016/j.agrformet.2022.109273

-  QES-Plume: Lagrangian Dispersion Model
  Margairaz, F., Singh, B., Gibbs, J.A., Atwood, L., Pardyjak, E.R.,
  Stoll, R., 2023. QES-Plume v1.0: a Lagrangian dispersion model.
  Geosci Model Dev 16:5729–5754.
  https://doi.org/10.5194/gmd-16-5729-2023

-  QES-Fire: wildfire model
  Moody, M.J., Gibbs, J.A., Krueger, S., Mallia, D., Pardyjak, E.R.,
  Kochanski, A.K., Bailey, B.N., Stoll, R., 2022. QES-Fire: a
  dynamically coupled fast-response wildfire model. Int J Wildland Fire
  31, 306–325. https://doi.org/10.1071/wf21057

-  QES: Turbulence and Passive scalar transport in Raw-Oriented Canopy
  Ulmer L., Margairaz F., Mahaffee W.F., Stoll R., 2024. A
  fast-response model of turbulence and passive scalar transport in
  row-organized canopies. Agric For Meteorol 349:109919.
  https://doi.org/10.1016/j.agrformet.2024.109919


Acknowledgements
----------------

This work was partly supported by grants from:

* The National Institute of Environment Research (NIER), funded by the Ministry of Environment (MOE) of the Republic of Korea (NIER-SP2019-312). In addition, we would like to acknowledge Dr. Jae-Jin Kim from Department of Environmental Atmospheric Sciences, Pukyong National University, Republic of Korea, as the main Principal Investigator (PI) on the grant from the National Institute of Environment Research (NIER).

* The United States Department of Agriculture National Institute for Food and Agriculture Specialty Crop Research Initiative Award No. 2018-03375.

* The United States Department of Agriculture Agricultural Research Service through Research Support Agreement 58-2072-0-036.

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
   :caption: Getting Started

   Introduction
   Installation
   Usage

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   QES-Winds
   QES-Turb
   QES-Plume
   QES-Fire

.. toctree::
   :maxdepth: 2
   :caption: References

   References

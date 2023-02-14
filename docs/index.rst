.. PyPatchwork documentation master file, created by
   sphinx-quickstart on Mon Feb 13 09:12:24 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyPatchwork
===========

PyPatchwork is a Python library to access the `Patchwork`_ REST API.

.. _Patchwork: http://jk.ozlabs.org/projects/patchwork

Installation
------------

This package can be installed from `Python Package Index <https://pypi.org>`_ (PyPi):

.. code-block:: shell

   $ pip install PyPatchwork

Usage
-----

.. code-block:: python3

   from patchwork import Patchwork

   # Create Patchwork object
   pw = Patchwork('https://patchwork.kernel.org')

   # Create Patchwork object with access token
   pw = Patchwork('https://patchwork.kernel.org', 'access_token')

Examples
--------

.. code-block:: python3

   from patchwork import Patchwork

   pw = Patchwork('https://patchwork.kernel.org')

   # Get projects
   project = pw.get_project(395)

   # Get Series
   series = pw.get_series(565705)

.. toctree::
   :maxdepth: 1
   :caption: API Reference

   classes

.. toctree::
   :maxdepth: 1
   :caption: TODO

   TODO
.. dwc_tools documentation master file

Welcome to dwc_tools's documentation!
======================================

``dwc_tools`` is a Python package providing helpers for working with Darwin Core (DwC) taxonomic occurrence data.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   api
   examples

Installation
============

.. include:: installation.rst

Quick Start
===========

Here's a quick example of using dwc_tools:

.. code-block:: python

   from dwc_tools import validate_dwc_record, format_scientific_name

   # Validate a Darwin Core record
   record = {"scientificName": "Homo sapiens"}
   is_valid = validate_dwc_record(record)
   print(f"Record is valid: {is_valid}")

   # Format a scientific name
   name = format_scientific_name("Homo", "sapiens", "Linnaeus, 1758")
   print(name)  # Output: Homo sapiens Linnaeus, 1758

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

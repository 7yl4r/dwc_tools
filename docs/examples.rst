Examples
========

Validating Darwin Core Records
-------------------------------

The most common use case is validating Darwin Core records:

.. code-block:: python

   from dwc_tools import validate_dwc_record

   # Valid record with required fields
   record1 = {"scientificName": "Quercus alba"}
   print(validate_dwc_record(record1))  # True

   # Invalid record missing required fields
   record2 = {"genus": "Quercus"}
   print(validate_dwc_record(record2))  # False

   # Valid record with additional fields
   record3 = {
       "scientificName": "Quercus alba",
       "genus": "Quercus",
       "specificEpithet": "alba",
       "kingdom": "Plantae"
   }
   print(validate_dwc_record(record3))  # True

Formatting Scientific Names
----------------------------

Format scientific names according to Darwin Core standards:

.. code-block:: python

   from dwc_tools import format_scientific_name

   # Basic usage
   name1 = format_scientific_name("Homo", "sapiens")
   print(name1)  # "Homo sapiens"

   # With authority
   name2 = format_scientific_name("Homo", "sapiens", "Linnaeus, 1758")
   print(name2)  # "Homo sapiens Linnaeus, 1758"

   # Another example
   name3 = format_scientific_name("Canis", "lupus", "Linnaeus, 1758")
   print(name3)  # "Canis lupus Linnaeus, 1758"

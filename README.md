# dwc_tools

[![Tests](https://github.com/7yl4r/dwc_tools/actions/workflows/tests.yml/badge.svg)](https://github.com/7yl4r/dwc_tools/actions/workflows/tests.yml)
[![Documentation](https://github.com/7yl4r/dwc_tools/actions/workflows/docs.yml/badge.svg)](https://github.com/7yl4r/dwc_tools/actions/workflows/docs.yml)
[![PyPI](https://img.shields.io/pypi/v/dwc-tools.svg)](https://pypi.org/project/dwc-tools/)
[![Python Version](https://img.shields.io/pypi/pyversions/dwc-tools.svg)](https://pypi.org/project/dwc-tools/)

Python helpers for working with Darwin Core (DwC) taxonomic occurrence data.

## Installation

```bash
pip install dwc-tools
```

## Quick Start

```python
from dwc_tools import validate_dwc_record, format_scientific_name

# Validate a Darwin Core record
record = {"scientificName": "Homo sapiens"}
is_valid = validate_dwc_record(record)

# Format a scientific name
name = format_scientific_name("Homo", "sapiens", "Linnaeus, 1758")
print(name)  # Output: Homo sapiens Linnaeus, 1758
```

## Development

### Setup

```bash
git clone https://github.com/7yl4r/dwc_tools.git
cd dwc_tools
pip install -e ".[dev,docs]"
```

### Running Tests

```bash
pytest
```

### Building Documentation

```bash
cd docs
sphinx-build -b html . _build/html
```

## Features

- Validate Darwin Core records
- Format scientific names according to standards
- Extensible for additional DwC operations

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

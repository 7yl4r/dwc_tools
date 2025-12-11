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
# TODO
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

- Download Darwin Core records from multiple sources (OBIS, GBIF)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

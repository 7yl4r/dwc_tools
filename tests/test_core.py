"""Tests for core functionality."""

import pytest
from dwc_tools.core import validate_dwc_record, format_scientific_name


class TestValidateDwcRecord:
    """Tests for validate_dwc_record function."""
    
    def test_valid_record(self):
        """Test with a valid record."""
        record = {"scientificName": "Homo sapiens"}
        assert validate_dwc_record(record) is True
    
    def test_invalid_record_empty(self):
        """Test with an empty record."""
        record = {}
        assert validate_dwc_record(record) is False
    
    def test_invalid_record_missing_required(self):
        """Test with a record missing required fields."""
        record = {"genus": "Homo"}
        assert validate_dwc_record(record) is False
    
    def test_valid_record_extra_fields(self):
        """Test with a valid record that has extra fields."""
        record = {
            "scientificName": "Homo sapiens",
            "genus": "Homo",
            "specificEpithet": "sapiens"
        }
        assert validate_dwc_record(record) is True


class TestFormatScientificName:
    """Tests for format_scientific_name function."""
    
    def test_format_without_authority(self):
        """Test formatting without authority."""
        result = format_scientific_name("Homo", "sapiens")
        assert result == "Homo sapiens"
    
    def test_format_with_authority(self):
        """Test formatting with authority."""
        result = format_scientific_name("Homo", "sapiens", "Linnaeus, 1758")
        assert result == "Homo sapiens Linnaeus, 1758"
    
    def test_format_different_species(self):
        """Test with different species."""
        result = format_scientific_name("Quercus", "alba")
        assert result == "Quercus alba"
    
    def test_format_with_empty_authority(self):
        """Test with empty authority string."""
        result = format_scientific_name("Pinus", "strobus", "")
        assert result == "Pinus strobus"

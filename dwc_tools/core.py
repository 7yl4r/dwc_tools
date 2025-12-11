"""
Core functionality for working with Darwin Core data.
"""


def validate_dwc_record(record: dict) -> bool:
    """
    Validate a Darwin Core record has required fields.
    
    Args:
        record: Dictionary containing Darwin Core fields
        
    Returns:
        True if record is valid, False otherwise
        
    Examples:
        >>> validate_dwc_record({"scientificName": "Homo sapiens"})
        True
        >>> validate_dwc_record({})
        False
    """
    required_fields = ["scientificName"]
    return all(field in record for field in required_fields)


def format_scientific_name(genus: str, species: str, authority: str = "") -> str:
    """
    Format a scientific name according to Darwin Core standards.
    
    Args:
        genus: The genus name
        species: The specific epithet
        authority: Optional authority citation
        
    Returns:
        Formatted scientific name string
        
    Examples:
        >>> format_scientific_name("Homo", "sapiens", "Linnaeus, 1758")
        'Homo sapiens Linnaeus, 1758'
        >>> format_scientific_name("Quercus", "alba")
        'Quercus alba'
    """
    name = f"{genus} {species}"
    if authority:
        name = f"{name} {authority}"
    return name

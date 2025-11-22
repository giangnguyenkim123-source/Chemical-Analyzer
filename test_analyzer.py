"""
Test suite for Chemical Formula Analyzer
Run this file to test the functionality with various chemical formulas
"""

from chemical_analyzer import (
    parse_chemical_formula,
    calculate_molecular_weight,
    calculate_element_percentages,
    calculate_unsaturation_degree
)

def run_tests():
    """
    Run comprehensive tests on various chemical formulas
    """
    test_cases = [
        "H2O",           # Water
        "C6H12O6",       # Glucose
        "CH3COOH",       # Acetic acid
        "C2H5OH",        # Ethanol
        "Fe2(SO4)3",     # Iron(III) sulfate
        "NaCl",          # Sodium chloride
        "H2SO4",         # Sulfuric acid
        "C60",           # Fullerene
        "Al2(SO4)3",     # Aluminum sulfate
        "C6H5OH",        # Phenol
    ]
    
    print("=== TESTING CHEMICAL ANALYZER ===")
    for formula in test_cases:
        print(f"\n--- Testing: {formula} ---")
        try:
            # Parse formula into element counts
            elements_count = parse_chemical_formula(formula)
            print(f"Elements: {elements_count}")
            
            # Calculate molecular weight
            molecular_weight = calculate_molecular_weight(elements_count)
            print(f"Molecular Weight: {molecular_weight:.3f} g/mol")
            
            # Calculate mass percentages
            percentages = calculate_element_percentages(elements_count, molecular_weight)
            print(f"Percentages: {percentages}")
            
            # Calculate degree of unsaturation
            unsaturation = calculate_unsaturation_degree(elements_count)
            print(f"Unsaturation Degree: {unsaturation}")
            
        except Exception as e:
            print(f"ERROR with {formula}: {e}")

if __name__ == "__main__":
    run_tests()

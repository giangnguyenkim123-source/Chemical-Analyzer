"""
Basic Usage Example for Chemical Analyzer
Demonstrates fundamental functionality of the chemical formula parser
"""

# Import the main functions from the chemical analyzer module
from chemical_analyzer import (
    parse_chemical_formula,
    calculate_molecular_weight,
    calculate_element_percentages,
    calculate_unsaturation_degree
)

def main():
    """
    Main function demonstrating basic usage of chemical analyzer
    """
    print("=== CHEMICAL ANALYZER - BASIC USAGE ===\n")
    
    # Example 1: Simple formula analysis
    formula = "C6H12O6"  # Glucose formula
    print(f"Analyzing: {formula}")
    
    # Step 1: Parse formula into element counts
    elements = parse_chemical_formula(formula)
    # Step 2: Calculate molecular weight
    mass = calculate_molecular_weight(elements)
    # Step 3: Calculate mass percentages
    percentages = calculate_element_percentages(elements, mass)
    # Step 4: Calculate unsaturation degree (for organic compounds)
    unsat = calculate_unsaturation_degree(elements)
    
    print(f"Elemental Composition: {elements}")
    print(f"Molecular Weight: {mass:.3f} g/mol")
    print(f"Mass Percentages: {percentages}")
    print(f"Degree of Unsaturation: {unsat}")
    
    print("\n" + "="*50)
    
    # Example 2: Analyze multiple compounds in a loop
    compounds = ["H2O", "CH3COOH", "C2H5OH", "NaCl"]
    
    print("\nBatch Analysis of Common Compounds:")
    for compound in compounds:
        elements = parse_chemical_formula(compound)
        mass = calculate_molecular_weight(elements)
        print(f"\n{compound}:")
        print(f"  → Composition: {elements}")
        print(f"  → Molecular Weight: {mass:.2f} g/mol")

# Standard Python idiom to run main function when script is executed directly
if __name__ == "__main__":
    main()

"""
Batch Processing Example
Demonstrates analyzing multiple chemical formulas efficiently
"""

# Import required functions from the main module
from chemical_analyzer import (
    parse_chemical_formula,
    calculate_molecular_weight,
    calculate_element_percentages
)

def analyze_multiple_formulas(formula_list):
    """
    Analyze a list of chemical formulas and return comprehensive results
    
    Args:
        formula_list (list): List of chemical formula strings
    
    Returns:
        list: List of dictionaries containing analysis results
    """
    results = []
    
    for formula in formula_list:
        try:
            # Parse the chemical formula into element counts
            elements = parse_chemical_formula(formula)
            # Calculate molecular weight
            mass = calculate_molecular_weight(elements)
            # Calculate mass percentages for each element
            percentages = calculate_element_percentages(elements, mass)
            
            # Store results in a structured format
            results.append({
                'formula': formula,
                'elements': elements,
                'molecular_weight': mass,
                'percentages': percentages
            })
        except Exception as e:
            # Handle any errors during analysis
            results.append({
                'formula': formula,
                'error': str(e)
            })
    
    return results

def main():
    """
    Main function demonstrating batch processing capabilities
    """
    # List of common chemical compounds for analysis
    compounds = [
        "H2O",      # Water
        "CO2",      # Carbon dioxide
        "CH4",      # Methane
        "C6H12O6",  # Glucose
        "NaCl",     # Sodium chloride
        "H2SO4",    # Sulfuric acid
        "NH3",      # Ammonia
        "C2H5OH",   # Ethanol
        "Fe2O3",    # Iron oxide
        "Al2(SO4)3" # Aluminum sulfate
    ]
    
    print("=== BATCH CHEMICAL ANALYSIS ===\n")
    print(f"Analyzing {len(compounds)} chemical compounds...\n")
    
    # Perform batch analysis
    results = analyze_multiple_formulas(compounds)
    
    # Display results in a formatted table
    print("RESULTS:")
    print("-" * 60)
    for result in results:
        if 'error' in result:
            # Display error message for failed analyses
            print(f"❌ {result['formula']}: ERROR - {result['error']}")
        else:
            # Display successful analysis results
            print(f"✅ {result['formula']:10} | "
                  f"MW: {result['molecular_weight']:7.2f} g/mol | "
                  f"Elements: {result['elements']}")

if __name__ == "__main__":
    main()

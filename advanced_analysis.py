"""
Advanced Analysis Example
Demonstrates comprehensive chemical analysis with compound classification
"""

# Import all analysis functions
from chemical_analyzer import (
    parse_chemical_formula,
    calculate_molecular_weight,
    calculate_element_percentages,
    calculate_unsaturation_degree
)

def comprehensive_analysis(formula):
    """
    Perform comprehensive analysis of a chemical compound
    
    Args:
        formula (str): Chemical formula string
    
    Returns:
        dict: Comprehensive analysis results
    """
    # Basic chemical analysis
    elements = parse_chemical_formula(formula)
    mass = calculate_molecular_weight(elements)
    percentages = calculate_element_percentages(elements, mass)
    unsat = calculate_unsaturation_degree(elements)
    
    # Additional statistics
    total_atoms = sum(elements.values())
    different_elements = len(elements)
    
    # Compound classification
    compound_type = classify_compound(elements)
    
    # Structure comprehensive results
    return {
        'formula': formula,
        'elements': elements,
        'molecular_weight': mass,
        'mass_percentages': percentages,
        'unsaturation_degree': unsat,
        'total_atoms': total_atoms,
        'different_elements': different_elements,
        'compound_type': compound_type
    }

def classify_compound(elements):
    """
    Classify compound as organic, inorganic, or organometallic
    
    Args:
        elements (dict): Element counts dictionary
    
    Returns:
        str: Compound classification
    """
    has_carbon = 'C' in elements
    has_hydrogen = 'H' in elements
    has_metal = any(element in ['Na', 'K', 'Ca', 'Mg', 'Fe', 'Cu', 'Zn', 'Ag', 'Au'] 
                   for element in elements.keys())
    
    if has_carbon:
        if has_metal:
            return "Organometallic Compound"
        elif has_hydrogen:
            return "Organic Compound"
        else:
            return "Inorganic Carbon Compound"
    else:
        return "Inorganic Compound"

def print_analysis_report(analysis):
    """
    Print formatted analysis report
    
    Args:
        analysis (dict): Comprehensive analysis results
    """
    print(f"🔬 COMPREHENSIVE ANALYSIS: {analysis['formula']}")
    print(f"📊 Compound Type: {analysis['compound_type']}")
    print(f"🧪 Elemental Composition: {analysis['elements']}")
    print(f"⚖️  Molecular Weight: {analysis['molecular_weight']:.3f} g/mol")
    print(f"📈 Total Atoms: {analysis['total_atoms']}")
    print(f"🎯 Unique Elements: {analysis['different_elements']}")
    
    # Display unsaturation degree for organic compounds
    if analysis['unsaturation_degree'] != 'not an organic compound':
        print(f"🔬 Degree of Unsaturation: {analysis['unsaturation_degree']}")
    
    # Display mass percentages
    print(f"📋 Mass Percentages: {analysis['mass_percentages']}")
    print("-" * 50)

def main():
    """
    Main function demonstrating advanced analysis capabilities
    """
    print("=== ADVANCED CHEMICAL ANALYSIS ===\n")
    
    # Test compounds representing different compound classes
    test_compounds = [
        "C6H12O6",    # Glucose (organic)
        "H2SO4",      # Sulfuric acid (inorganic)  
        "NaCl",       # Sodium chloride (inorganic)
        "CH3COOH",    # Acetic acid (organic)
        "CO2",        # Carbon dioxide (inorganic carbon)
        "Fe(CO)5",    # Iron pentacarbonyl (organometallic)
    ]
    
    print("Performing comprehensive analysis of test compounds...\n")
    
    for compound in test_compounds:
        try:
            # Perform comprehensive analysis
            analysis = comprehensive_analysis(compound)
            # Display formatted report
            print_analysis_report(analysis)
            
        except Exception as e:
            print(f"❌ Error analyzing {compound}: {e}")
            print("-" * 50)

if __name__ == "__main__":
    main()

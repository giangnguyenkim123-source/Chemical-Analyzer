"""
Custom Elements Example
Demonstrates how to add custom elements and isotopes to the atomic mass database
"""

# Import required modules and functions
from chemical_analyzer import (
    parse_chemical_formula, 
    calculate_molecular_weight,
    ATOMIC_MASS  # Reference to the atomic mass dictionary
)

def add_custom_elements():
    """
    Add custom elements and isotopes to the atomic mass database
    
    Returns:
        dict: Updated atomic mass dictionary
    """
    # Define custom elements and isotopes with their atomic masses
    custom_elements = {
        'D': 2.014,        # Deuterium (Hydrogen-2)
        'T': 3.016,        # Tritium (Hydrogen-3)
        'U235': 235.0439,  # Uranium-235 isotope
        'U238': 238.0508,  # Uranium-238 isotope
        'Ac': 227.0,       # Actinium (updated value)
        'Pu': 244.0,       # Plutonium
    }
    
    # Update the global atomic mass dictionary with custom elements
    ATOMIC_MASS.update(custom_elements)
    print("✅ Custom elements added to database!")
    
    return ATOMIC_MASS

def main():
    """
    Main function demonstrating custom element functionality
    """
    print("=== CUSTOM ELEMENTS AND ISOTOPES EXAMPLE ===\n")
    
    # Add custom elements to the database
    updated_masses = add_custom_elements()
    
    # Test formulas containing custom elements and isotopes
    test_formulas = [
        "D2O",           # Heavy water (Deuterium oxide)
        "C2D4",          # Deuterated ethylene
        "U235O2",        # Uranium-235 dioxide
        "PuO2",          # Plutonium dioxide
    ]
    
    print("\nTesting custom element analysis:")
    print("-" * 40)
    
    for formula in test_formulas:
        try:
            # Parse formula and calculate properties
            elements = parse_chemical_formula(formula)
            mass = calculate_molecular_weight(elements)
            
            print(f"\n🔬 Formula: {formula}")
            print(f"   Elemental Composition: {elements}")
            print(f"   Molecular Weight: {mass:.3f} g/mol")
            
            # Display custom elements used in this formula
            custom_in_formula = [elem for elem in elements.keys() 
                               if elem in ['D', 'T', 'U235', 'U238', 'Pu']]
            if custom_in_formula:
                print(f"   Custom Elements: {custom_in_formula}")
            
        except Exception as e:
            print(f"❌ Error analyzing {formula}: {e}")

if __name__ == "__main__":
    main()

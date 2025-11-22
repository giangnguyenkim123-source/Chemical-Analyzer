# Compound Analysis Tool
# A comprehensive chemical formula parser and molecular property calculator

# Atomic mass database (values in g/mol)
ATOMIC_MASS = {
    'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81,
    'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
    'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.085, 'P': 30.974,
    'S': 32.06, 'Cl': 35.45, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
    'Sc': 44.956, 'Ti': 47.867, 'V': 50.942, 'Cr': 51.996, 'Mn': 54.938,
    'Fe': 55.845, 'Co': 58.933, 'Ni': 58.693, 'Cu': 63.546, 'Zn': 65.38,
    'Ga': 69.723, 'Ge': 72.630, 'As': 74.922, 'Se': 78.971, 'Br': 79.904,
    'Kr': 83.798, 'Rb': 85.468, 'Sr': 87.62, 'Y': 88.906, 'Zr': 91.224,
    'Nb': 92.906, 'Mo': 95.95, 'Tc': 98.0, 'Ru': 101.07, 'Rh': 102.91,
    'Pd': 106.42, 'Ag': 107.87, 'Cd': 112.41, 'In': 114.82, 'Sn': 118.71,
    'Sb': 121.76, 'Te': 127.60, 'I': 126.90, 'Xe': 131.29, 'Cs': 132.91,
    'Ba': 137.33, 'La': 138.91, 'Ce': 140.12, 'Pr': 140.91, 'Nd': 144.24,
    'Pm': 145.0, 'Sm': 150.36, 'Eu': 151.96, 'Gd': 157.25, 'Tb': 158.93,
    'Dy': 162.50, 'Ho': 164.93, 'Er': 167.26, 'Tm': 168.93, 'Yb': 173.05,
    'Lu': 174.97, 'Hf': 178.49, 'Ta': 180.95, 'W': 183.84, 'Re': 186.21,
    'Os': 190.23, 'Ir': 192.22, 'Pt': 195.08, 'Au': 196.97, 'Hg': 200.59,
    'Tl': 204.38, 'Pb': 207.2, 'Bi': 208.98, 'Po': 209.0, 'At': 210.0,
    'Rn': 222.0, 'Fr': 223.0, 'Ra': 226.0, 'Ac': 227.0, 'Th': 232.04,
    'Pa': 231.04, 'U': 238.03, 'Np': 237.0, 'Pu': 244.0, 'Am': 243.0,
    'Cm': 247.0, 'Bk': 247.0, 'Cf': 251.0, 'Es': 252.0, 'Fm': 257.0,
    'Md': 258.0, 'No': 259.0, 'Lr': 266.0, 'Rf': 267.0, 'Db': 268.0,
    'Sg': 269.0, 'Bh': 270.0, 'Hs': 277.0, 'Mt': 278.0, 'Ds': 281.0,
    'Rg': 282.0, 'Cn': 285.0, 'Nh': 286.0, 'Fl': 289.0, 'Mc': 289.0,
    'Lv': 293.0, 'Ts': 294.0, 'Og': 294.0
}

def parse_chemical_formula(formula):
    """
    Parse a chemical formula into elemental composition dictionary
    Supports nested parentheses and complex formulas
    
    Args:
        formula (str): Chemical formula string (e.g., "C6H12O6", "Fe2(SO4)3")
    
    Returns:
        dict: Dictionary with elements as keys and counts as values
    """
    # Stack to handle nested parentheses
    stack = []
    # Dictionary to store element counts
    elements_count = {}
    # Temporary variables for current element and count
    element = ''
    count = ''
    
    def multiply_counts(elements_count, multiplier):
        """
        Multiply all element counts by a multiplier
        
        Args:
            elements_count (dict): Element counts dictionary
            multiplier (int): Multiplier value
        
        Returns:
            dict: New dictionary with multiplied counts
        """
        return {element: multiplier * count for element, count in elements_count.items()}
    
    def merge_counts(count1, count2):
        """
        Merge two element count dictionaries
        
        Args:
            count1 (dict): First element counts dictionary
            count2 (dict): Second element counts dictionary
        
        Returns:
            dict: Merged dictionary with summed counts
        """
        result = count1.copy()
        for element, count in count2.items():
            result[element] = result.get(element, 0) + count
        return result
    
    # Main parsing loop - iterate through each character in formula
    i = 0
    while i < len(formula):
        char = formula[i]
        
        # Handle uppercase letters (start of new element)
        if char.isupper():
            # Process previous element if exists
            if element:
                current_count = int(count) if count else 1
                elements_count[element] = elements_count.get(element, 0) + current_count
                element = char
                count = ''
            else:
                element = char
            i += 1
        
        # Handle lowercase letters (continuation of element name)
        elif char.islower():
            element += char
            i += 1
            
        # Handle digits (element count)
        elif char.isdigit():
            count += char
            i += 1
            
        # Handle opening brackets/parentheses
        elif char in '([':
            # Process current element before starting group
            if element:
                current_count = int(count) if count else 1
                elements_count[element] = elements_count.get(element, 0) + current_count
                count = ''
                element = ''
            # Push current state to stack and reset for nested group
            stack.append(elements_count)
            elements_count = {}
            i += 1

        # Handle closing brackets/parentheses
        elif char in '])':
            # Process current element before ending group
            if element:
                current_count = int(count) if count else 1
                elements_count[element] = elements_count.get(element, 0) + current_count
                count = ''
                element = ''
                
            i += 1
            # Parse multiplier after closing bracket
            multiplier_str = ''
            while i < len(formula) and formula[i].isdigit():
                multiplier_str += formula[i]
                i += 1
            multiplier = int(multiplier_str) if multiplier_str else 1
            
            # Multiply counts in current group and merge with previous state
            current_counts = multiply_counts(elements_count, multiplier)
            previous_counts = stack.pop()
            elements_count = merge_counts(previous_counts, current_counts)
            
    # Process any remaining element after loop completion
    if element:
        current_count = int(count) if count else 1
        elements_count[element] = elements_count.get(element, 0) + current_count
    
    return elements_count

def calculate_molecular_weight(elements_count):
    """
    Calculate molecular weight from element counts
    
    Args:
        elements_count (dict): Dictionary of element counts
    
    Returns:
        float: Molecular weight in g/mol
    """
    molecular_weight = 0.0
    for element, count in elements_count.items():
        # Add atomic mass multiplied by count for each element
        molecular_weight += ATOMIC_MASS.get(element, 0) * count
    return molecular_weight

def calculate_element_percentages(elements_count, molecular_weight):
    """
    Calculate mass percentage composition of each element
    
    Args:
        elements_count (dict): Dictionary of element counts
        molecular_weight (float): Total molecular weight
    
    Returns:
        dict: Dictionary with elements as keys and percentage strings as values
    """
    elements_composition = {}
    for element, count in elements_count.items():
        # Calculate percentage: (element mass / total mass) * 100
        percentage = (ATOMIC_MASS.get(element, 0) * count * 100) / molecular_weight
        elements_composition[element] = f'{percentage:.2f}%'
    
    return elements_composition

def calculate_unsaturation_degree(elements_count):
    """
    Calculate degree of unsaturation for organic compounds
    Formula: DU = (2C + 2 + N - H - X)/2
    Where X = F, Cl, Br, I
    
    Args:
        elements_count (dict): Dictionary of element counts
    
    Returns:
        int or str: Degree of unsaturation or message for inorganic compounds
    """
    if 'C' in elements_count:
        # Get counts of relevant elements
        carbon = elements_count.get('C', 0)
        hydrogen = elements_count.get('H', 0)
        nitrogen = elements_count.get('N', 0)
        halogens = (elements_count.get('F', 0) + elements_count.get('Cl', 0) + 
                   elements_count.get('Br', 0) + elements_count.get('I', 0))
        
        # Apply degree of unsaturation formula
        unsaturation_degree = (carbon * 2 + 2 + nitrogen - hydrogen - halogens) // 2
        return unsaturation_degree
    else:
        return 'not an organic compound'

# Main execution flow
def main():
    """Main function to run the chemical analyzer"""
    # Get chemical formula from user input
    molecule_formula = input('What is the molecule formula? ')
    
    # Step 1: Parse chemical formula into element counts
    elements_count = parse_chemical_formula(molecule_formula)
    print('Element Counts:', elements_count)

    # Step 2: Calculate molecular weight
    molecular_weight_value = calculate_molecular_weight(elements_count)
    print(f'Molecular Weight: {molecular_weight_value:.3f} g/mol')

    # Step 3: Calculate element mass percentages
    element_percentages = calculate_element_percentages(elements_count, molecular_weight_value)
    print('Element Percentages:', element_percentages)
    
    # Step 4: Calculate degree of unsaturation (for organic compounds)
    unsaturation_degree = calculate_unsaturation_degree(elements_count)
    print('Degree of Unsaturation:', unsaturation_degree)

if __name__ == "__main__":
    main()

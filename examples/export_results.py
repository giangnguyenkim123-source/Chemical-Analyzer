"""
Export Results Example
Demonstrates how to export chemical analysis results to JSON and CSV files
"""

# Import required libraries for data export
import json
import csv
from datetime import datetime

# Import chemical analysis functions
from chemical_analyzer import (
    parse_chemical_formula,
    calculate_molecular_weight,
    calculate_element_percentages
)

def analyze_and_export(formulas, output_format='json'):
    """
    Analyze chemical formulas and export results to specified format
    
    Args:
        formulas (list): List of chemical formula strings
        output_format (str): Export format - 'json' or 'csv'
    
    Returns:
        list: Analysis results
    """
    results = []
    
    print(f"Analyzing {len(formulas)} formulas...")
    
    for formula in formulas:
        # Perform chemical analysis
        elements = parse_chemical_formula(formula)
        mass = calculate_molecular_weight(elements)
        percentages = calculate_element_percentages(elements, mass)
        
        # Structure results for export
        results.append({
            'formula': formula,
            'composition': elements,
            'molecular_weight': round(mass, 3),
            'mass_percentages': percentages,
            'analysis_date': datetime.now().isoformat()
        })
    
    # Export to JSON format
    if output_format == 'json':
        filename = 'chemical_analysis.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"✅ Results exported to {filename}")
    
    # Export to CSV format
    elif output_format == 'csv':
        filename = 'chemical_analysis.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Write header row
            writer.writerow(['Formula', 'Molecular Weight (g/mol)', 
                           'Composition', 'Mass Percentages', 'Analysis Date'])
            
            # Write data rows
            for result in results:
                writer.writerow([
                    result['formula'],
                    result['molecular_weight'],
                    str(result['composition']),
                    str(result['mass_percentages']),
                    result['analysis_date']
                ])
        print(f"✅ Results exported to {filename}")
    
    return results

def main():
    """
    Main function demonstrating data export capabilities
    """
    print("=== EXPORT CHEMICAL ANALYSIS RESULTS ===\n")
    
    # List of compounds to analyze and export
    compounds = [
        "H2O",        # Water
        "CO2",        # Carbon dioxide
        "C6H12O6",    # Glucose
        "NaCl",       # Sodium chloride
        "CH3COOH"     # Acetic acid
    ]
    
    print(f"Processing {len(compounds)} compounds for export...\n")
    
    # Export to JSON format
    print("1. Exporting to JSON format:")
    json_results = analyze_and_export(compounds, 'json')
    
    # Export to CSV format  
    print("\n2. Exporting to CSV format:")
    csv_results = analyze_and_export(compounds, 'csv')
    
    # Display summary of results
    print(f"\n📊 ANALYSIS SUMMARY:")
    print(f"   Total compounds processed: {len(compounds)}")
    print(f"   Export files created: chemical_analysis.json, chemical_analysis.csv")
    
    # Preview first result
    if json_results:
        first_result = json_results[0]
        print(f"\n📋 Sample Result for {first_result['formula']}:")
        print(f"   Molecular Weight: {first_result['molecular_weight']} g/mol")
        print(f"   Composition: {first_result['composition']}")
        print(f"   Mass Percentages: {first_result['mass_percentages']}")

if __name__ == "__main__":
    main()

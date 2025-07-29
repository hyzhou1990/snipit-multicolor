#!/usr/bin/env python3
"""
snipit-mc Python API Examples

This script demonstrates various ways to use the snipit-mc Python API
for generating SNP visualizations programmatically.
"""

from snipit import (
    snipit_plot, 
    SnipitConfig, 
    quick_plot, 
    publication_plot, 
    protein_plot,
    get_color_palettes,
    validate_alignment
)
from pathlib import Path


def example_1_basic_usage():
    """Example 1: Basic plot generation"""
    print("=== Example 1: Basic Usage ===")
    
    # Simple plot with Nature palette
    alignment_file = "test.fasta"  # Replace with your file
    
    result = snipit_plot(alignment_file, colour_palette="nature")
    
    if result['success']:
        print(f"✓ Generated plot: {result['output_files']}")
    else:
        print(f"✗ Failed: {result['message']}")
    
    print()


def example_2_configuration():
    """Example 2: Using configuration objects"""
    print("=== Example 2: Configuration Objects ===")
    
    # Create detailed configuration
    config = SnipitConfig(
        colour_palette="vangogh",
        width=12,
        height=8,
        format="pdf",
        sort_by_mutation_number=True,
        solid_background=True,
        output_file="vangogh_analysis"
    )
    
    alignment_file = "test.fasta"  # Replace with your file
    result = snipit_plot(alignment_file, config=config)
    
    if result['success']:
        print(f"✓ Generated configured plot: {result['output_files']}")
        print(f"  Used palette: {result['config'].colour_palette}")
        print(f"  Format: {result['config'].format}")
    else:
        print(f"✗ Failed: {result['message']}")
    
    print()


def example_3_convenience_functions():
    """Example 3: Using convenience functions"""
    print("=== Example 3: Convenience Functions ===")
    
    alignment_file = "test.fasta"  # Replace with your file
    
    # Quick plot
    result1 = quick_plot(alignment_file, palette="monet", width=10)
    print(f"Quick plot: {'✓' if result1['success'] else '✗'}")
    
    # Publication plot
    result2 = publication_plot(alignment_file, palette="nature", width=12)
    print(f"Publication plot: {'✓' if result2['success'] else '✗'}")
    
    # Protein plot (for amino acid sequences)
    protein_file = "protein.fasta"  # Replace with your protein file
    if Path(protein_file).exists():
        result3 = protein_plot(protein_file, palette="nature_aa")
        print(f"Protein plot: {'✓' if result3['success'] else '✗'}")
    else:
        print("Protein plot: Skipped (no protein file)")
    
    print()


def example_4_validation():
    """Example 4: File validation"""
    print("=== Example 4: File Validation ===")
    
    alignment_file = "test.fasta"  # Replace with your file
    
    # Validate alignment file
    validation = validate_alignment(alignment_file)
    
    if validation['valid']:
        print(f"✓ Valid alignment:")
        print(f"  Sequences: {validation['num_sequences']}")
        print(f"  Length: {validation['alignment_length']}")
        print(f"  IDs: {validation['sequence_ids'][:3]}...")  # Show first 3
    else:
        print(f"✗ Invalid alignment:")
        for issue in validation['issues']:
            print(f"  - {issue}")
    
    print()


def example_5_color_palettes():
    """Example 5: Exploring color palettes"""
    print("=== Example 5: Color Palettes ===")
    
    palettes = get_color_palettes()
    
    print("Available artistic palettes:")
    artistic_palettes = [
        'nature', 'morandi', 'vangogh', 'monet', 'matisse'
    ]
    
    for palette in artistic_palettes:
        if palette in palettes:
            info = palettes[palette]
            print(f"  {palette:10} - {info['description']}")
    
    print(f"\nTotal palettes available: {len(palettes)}")
    print()


def example_6_batch_processing():
    """Example 6: Batch processing multiple files"""
    print("=== Example 6: Batch Processing ===")
    
    # Simulate multiple alignment files
    alignment_files = ["test.fasta"]  # Add more files as needed
    palettes = ["nature", "morandi", "vangogh"]
    
    results = {}
    
    for alignment_file in alignment_files:
        if not Path(alignment_file).exists():
            print(f"Skipping {alignment_file} (not found)")
            continue
            
        file_results = {}
        
        for palette in palettes:
            config = SnipitConfig(
                colour_palette=palette,
                output_file=f"{Path(alignment_file).stem}_{palette}",
                format="png",
                width=10
            )
            
            result = snipit_plot(alignment_file, config=config)
            file_results[palette] = result['success']
            
        results[alignment_file] = file_results
        print(f"Processed {alignment_file}: {sum(file_results.values())}/{len(palettes)} successful")
    
    print()


def example_7_genbank_annotations():
    """Example 7: GenBank gene annotations"""
    print("=== Example 7: GenBank Annotations ===")
    
    alignment_file = "covid_sequences.fasta"  # Replace with your file
    genbank_file = "NC_045512.gb"  # Replace with your GenBank file
    
    if Path(alignment_file).exists() and Path(genbank_file).exists():
        config = SnipitConfig(
            colour_palette="nature",
            genbank=genbank_file,
            width=15,
            height=10,
            sort_by_mutation_number=True,
            output_file="covid_with_genes"
        )
        
        result = snipit_plot(alignment_file, config=config)
        
        if result['success']:
            print(f"✓ Generated plot with gene annotations: {result['output_files']}")
        else:
            print(f"✗ Failed: {result['message']}")
    else:
        print("Skipped (missing alignment or GenBank file)")
        print("  - Download SARS-CoV-2 GenBank file from NCBI")
        print("  - Prepare COVID-19 sequence alignment")
    
    print()


def example_8_error_handling():
    """Example 8: Comprehensive error handling"""
    print("=== Example 8: Error Handling ===")
    
    # Try with non-existent file
    try:
        result = snipit_plot("nonexistent.fasta", colour_palette="nature")
        print(f"Result: {result['success']}")
        if not result['success']:
            print(f"Error handled gracefully: {result['message']}")
    except FileNotFoundError:
        print("✓ FileNotFoundError caught and handled")
    
    # Try with invalid parameter
    try:
        result = snipit_plot("test.fasta", invalid_parameter="value")
        print("This shouldn't print")
    except ValueError as e:
        print(f"✓ ValueError caught: {e}")
    
    print()


def main():
    """Run all examples"""
    print("snipit-mc Python API Examples")
    print("=" * 40)
    print()
    
    # List available examples
    examples = [
        ("Basic Usage", example_1_basic_usage),
        ("Configuration Objects", example_2_configuration),
        ("Convenience Functions", example_3_convenience_functions),
        ("File Validation", example_4_validation),
        ("Color Palettes", example_5_color_palettes),
        ("Batch Processing", example_6_batch_processing),
        ("GenBank Annotations", example_7_genbank_annotations),
        ("Error Handling", example_8_error_handling),
    ]
    
    print("Available examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")
    print()
    
    # Run examples that don't require specific files
    safe_examples = [4, 5, 8]  # Validation, Palettes, Error Handling
    
    print("Running examples that don't require specific files:")
    for i in safe_examples:
        examples[i-1][1]()
    
    print("To run other examples, ensure you have the required alignment files.")
    print("See the API documentation for more details.")


if __name__ == "__main__":
    main()
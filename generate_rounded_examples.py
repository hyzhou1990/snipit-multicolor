#!/usr/bin/env python3
"""
Generate updated example images showing the new rounded rectangle design
"""

import os
import sys
from pathlib import Path

# Add current directory to path to import snipit
sys.path.insert(0, str(Path(__file__).parent))

from snipit import snipit_plot, SnipitConfig


def generate_examples():
    """Generate example plots with rounded rectangles"""
    
    # Create output directory for new examples
    output_dir = Path("docs/examples_rounded")
    output_dir.mkdir(exist_ok=True)
    
    # Test data files
    test_fasta = "docs/test.fasta"
    aa_fasta = "docs/aa_alignment.fasta"
    genbank_file = "docs/NC_045512.gb"
    
    print("Generating new rounded rectangle examples...")
    
    # Example 1: Nature palette with nucleotides
    print("1. Generating Nature palette example...")
    config1 = SnipitConfig(
        colour_palette="nature",
        width=12,
        height=6,
        format="png",
        output_file="nature_rounded",
        solid_background=True
    )
    
    try:
        result1 = snipit_plot(test_fasta, config=config1)
        if result1['success']:
            print(f"   ✓ Generated: {result1['output_files']}")
        else:
            print(f"   ✗ Failed: {result1['message']}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Example 2: Morandi palette 
    print("2. Generating Morandi palette example...")
    config2 = SnipitConfig(
        colour_palette="morandi",
        width=12,
        height=6,
        format="png",
        output_file="morandi_rounded",
        solid_background=True
    )
    
    try:
        result2 = snipit_plot(test_fasta, config=config2)
        if result2['success']:
            print(f"   ✓ Generated: {result2['output_files']}")
        else:
            print(f"   ✗ Failed: {result2['message']}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Example 3: Van Gogh palette
    print("3. Generating Van Gogh palette example...")
    config3 = SnipitConfig(
        colour_palette="vangogh",
        width=12,
        height=6,
        format="png",
        output_file="vangogh_rounded",
        solid_background=True
    )
    
    try:
        result3 = snipit_plot(test_fasta, config=config3)
        if result3['success']:
            print(f"   ✓ Generated: {result3['output_files']}")
        else:
            print(f"   ✗ Failed: {result3['message']}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Example 4: Monet palette
    print("4. Generating Monet palette example...")
    config4 = SnipitConfig(
        colour_palette="monet",
        width=12,
        height=6,
        format="png",
        output_file="monet_rounded",
        solid_background=True
    )
    
    try:
        result4 = snipit_plot(test_fasta, config=config4)
        if result4['success']:
            print(f"   ✓ Generated: {result4['output_files']}")
        else:
            print(f"   ✗ Failed: {result4['message']}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Example 5: Amino acid with nature_aa palette
    print("5. Generating amino acid example...")
    config5 = SnipitConfig(
        sequence_type="aa",
        colour_palette="nature_aa",
        width=12,
        height=6,
        format="png",
        output_file="nature_aa_rounded",
        solid_background=True
    )
    
    try:
        result5 = snipit_plot(aa_fasta, config=config5)
        if result5['success']:
            print(f"   ✓ Generated: {result5['output_files']}")
        else:
            print(f"   ✗ Failed: {result5['message']}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # Example 6: GenBank annotation with SARS-CoV-2 (if files exist)
    if Path(genbank_file).exists():
        print("6. Generating GenBank annotation example...")
        config6 = SnipitConfig(
            colour_palette="nature",
            genbank=genbank_file,
            width=15,
            height=8,
            format="png",
            output_file="sars_cov2_nature_rounded",
            solid_background=True,
            sort_by_mutation_number=True
        )
        
        try:
            result6 = snipit_plot(test_fasta, config=config6)
            if result6['success']:
                print(f"   ✓ Generated: {result6['output_files']}")
            else:
                print(f"   ✗ Failed: {result6['message']}")
        except Exception as e:
            print(f"   ✗ Error: {e}")
    
    # Example 7: Comparison plot with multiple palettes
    print("7. Generating palette comparison...")
    palettes = ["nature", "morandi", "vangogh", "monet"]
    
    for i, palette in enumerate(palettes, 1):
        config = SnipitConfig(
            colour_palette=palette,
            width=10,
            height=4,
            format="png",
            output_file=f"comparison_{palette}_rounded",
            solid_background=True
        )
        
        try:
            result = snipit_plot(test_fasta, config=config)
            if result['success']:
                print(f"   ✓ Generated comparison {i}/4: {palette}")
            else:
                print(f"   ✗ Failed comparison {i}/4: {palette}")
        except Exception as e:
            print(f"   ✗ Error comparison {i}/4: {e}")
    
    print("\nExample generation complete!")
    print(f"Check the current directory for generated PNG files.")


if __name__ == "__main__":
    generate_examples()
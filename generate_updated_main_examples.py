#!/usr/bin/env python3
"""
Generate updated main example images with rounded rectangles
"""

import subprocess
import os
from pathlib import Path

def generate_main_examples():
    """Generate the main example images used in documentation"""
    
    # Ensure output directory exists
    os.makedirs("docs/examples", exist_ok=True)
    
    # Generate main SARS-CoV-2 example with nature palette (this updates the main genome_graph.png)
    cmd1 = [
        "python", "-m", "snipit.snipit",
        "--input", "data/sars_cov2_demo.fasta",
        "--output", "docs/genome_graph.png",
        "--palette", "nature",
        "--format", "png",
        "--width", "16",
        "--height", "6"
    ]
    
    print("Generating main genome graph...")
    result = subprocess.run(cmd1, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    print("✓ Generated docs/genome_graph.png")
    
    # Generate amino acid example with rounded rectangles
    cmd2 = [
        "python", "-m", "snipit.snipit", 
        "--input", "data/aa_alignment.fasta",
        "--output", "docs/examples/nature_aa_example.png",
        "--palette", "nature",
        "--format", "png",
        "--width", "14",
        "--height", "4"
    ]
    
    print("Generating amino acid example...")
    result = subprocess.run(cmd2, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    print("✓ Generated docs/examples/nature_aa_example.png")
    
    # Generate SARS-CoV-2 nature example with gene annotations
    cmd3 = [
        "python", "-m", "snipit.snipit",
        "--input", "data/sars_cov2_demo.fasta", 
        "--output", "docs/examples/sars_cov2_nature.png",
        "--palette", "nature",
        "--genbank", "data/reference.gb",
        "--format", "png",
        "--width", "16",
        "--height", "6"
    ]
    
    print("Generating SARS-CoV-2 nature example...")
    result = subprocess.run(cmd3, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    print("✓ Generated docs/examples/sars_cov2_nature.png")
    
    return True

if __name__ == "__main__":
    success = generate_main_examples()
    if success:
        print("\n✅ All main example images updated with rounded rectangles!")
    else:
        print("\n❌ Some images failed to generate")
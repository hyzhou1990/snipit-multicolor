#!/usr/bin/env python3
"""
Generate amino acid example with rounded rectangles
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'snipit'))

from snipit.scripts import snp_functions as sfunks

def generate_aa_example():
    """Generate amino acid example using direct function calls"""
    
    # Check if AA alignment file exists
    if not os.path.exists("docs/aa_alignment.fasta"):
        print("❌ docs/aa_alignment.fasta not found")
        return False
        
    os.makedirs("docs/examples", exist_ok=True)
    
    # Set up parameters for AA example
    alignment_file = "docs/aa_alignment.fasta"
    ref_input = None
    sequence_type = "aa"
    cds_mode = False
    
    try:
        # Load and process alignment
        num_seqs, ref_input, record_ids, length = sfunks.qc_alignment(
            alignment_file, ref_input, cds_mode, sequence_type, os.getcwd()
        )
        
        # Create label map (using sequence names)  
        label_map = sfunks.label_map(record_ids, None, "name,label", os.getcwd())
        
        # Get reference and alignment
        reference, alignment = sfunks.get_ref_and_alignment(
            alignment_file, ref_input, label_map
        )
        
        # Find SNPs for amino acids
        snp_dict, record_snps, num_snps = sfunks.find_snps(
            reference, alignment, False, sequence_type, "snps"
        )
        
        # Find ambiguities
        record_ambs = sfunks.find_ambiguities(alignment, snp_dict, sequence_type)
        
        # Get nature_aa palette colors
        colours = sfunks.get_colours("nature_aa")
        
        # Generate AA example
        output_file = "docs/examples/nature_aa_example.png"
        sfunks.make_graph(
            num_seqs, num_snps, record_ambs, record_snps, output_file,
            label_map, colours, length, 14, 4, "scale", False, False,
            "snps", False, None, None, False, True, False, None,
            False, None, None, "nature_aa", sequence_type
        )
        print(f"✓ Generated {output_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating AA example: {e}")
        return False

if __name__ == "__main__":
    success = generate_aa_example()
    if success:
        print("\n✅ Amino acid example updated with rounded rectangles!")
    else:
        print("\n❌ Failed to generate AA example")
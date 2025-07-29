#!/usr/bin/env python3
"""
Update example images directly by importing the snipit functions
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'snipit'))

from snipit.scripts import snp_functions as sfunks
from Bio import SeqIO

def generate_updated_examples():
    """Generate updated examples using direct function calls"""
    
    # Check if data files exist
    if not os.path.exists("docs/test.fasta"):
        print("❌ docs/test.fasta not found")
        return False
        
    os.makedirs("docs/examples", exist_ok=True)
    
    # Set up parameters for main genome graph
    alignment_file = "docs/test.fasta"
    ref_input = None
    sequence_type = "nt"
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
        
        # Find SNPs
        snp_dict, record_snps, num_snps = sfunks.find_snps(
            reference, alignment, False, sequence_type, "snps"
        )
        
        # Find ambiguities
        record_ambs = sfunks.find_ambiguities(alignment, snp_dict, sequence_type)
        
        # Get nature palette colors
        colours = sfunks.get_colours("nature")
        
        # Generate main genome graph
        output_file = "docs/genome_graph.png"
        sfunks.make_graph(
            num_seqs, num_snps, record_ambs, record_snps, output_file,
            label_map, colours, length, 16, 6, "scale", False, False,
            "snps", False, None, None, False, True, False, None,
            False, None, None, "nature", sequence_type
        )
        print(f"✓ Generated {output_file}")
        
        # Generate GenBank annotated version if genbank file exists
        if os.path.exists("docs/test_reference.gb"):
            gene_features = sfunks.parse_genbank("docs/test_reference.gb", os.getcwd(), sequence_type)
            output_file = "docs/examples/sars_cov2_nature.png"
            sfunks.make_graph(
                num_seqs, num_snps, record_ambs, record_snps, output_file,
                label_map, colours, length, 16, 6, "scale", False, False,
                "snps", False, None, None, False, True, False, None,
                False, None, gene_features, "nature", sequence_type
            )
            print(f"✓ Generated {output_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating examples: {e}")
        return False

if __name__ == "__main__":
    success = generate_updated_examples()
    if success:
        print("\n✅ Main example images updated with rounded rectangles!")
    else:
        print("\n❌ Failed to generate some images")
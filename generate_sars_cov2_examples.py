#!/usr/bin/env python3
"""
Generate SARS-CoV-2 examples with Morandi and Monet palettes
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'snipit'))

from snipit.scripts import snp_functions as sfunks

def generate_sars_cov2_examples():
    """Generate SARS-CoV-2 examples with GenBank annotations"""
    
    if not os.path.exists("docs/test.fasta"):
        print("❌ docs/test.fasta not found")
        return False
        
    if not os.path.exists("docs/test_reference.gb"):
        print("❌ docs/test_reference.gb not found")
        return False
        
    os.makedirs("docs/examples", exist_ok=True)
    
    alignment_file = "docs/test.fasta"
    ref_input = None
    sequence_type = "nt"
    cds_mode = False
    
    try:
        # Load and process alignment
        num_seqs, ref_input, record_ids, length = sfunks.qc_alignment(
            alignment_file, ref_input, cds_mode, sequence_type, os.getcwd()
        )
        
        label_map = sfunks.label_map(record_ids, None, "name,label", os.getcwd())
        reference, alignment = sfunks.get_ref_and_alignment(alignment_file, ref_input, label_map)
        snp_dict, record_snps, num_snps = sfunks.find_snps(reference, alignment, False, sequence_type, "snps")
        record_ambs = sfunks.find_ambiguities(alignment, snp_dict, sequence_type)
        
        # Parse GenBank file
        gene_features = sfunks.parse_genbank("docs/test_reference.gb", os.getcwd(), sequence_type)
        
        # Generate SARS-CoV-2 Morandi example
        colours = sfunks.get_colours("morandi")
        output_file = "docs/examples/sars_cov2_morandi.png"
        sfunks.make_graph(
            num_seqs, num_snps, record_ambs, record_snps, output_file,
            label_map, colours, length, 16, 6, "scale", False, False,
            "snps", False, None, None, False, True, False, None,
            False, None, gene_features, "morandi", sequence_type
        )
        print(f"✓ Generated {output_file}")
        
        # Generate SARS-CoV-2 Monet example
        colours = sfunks.get_colours("monet")
        output_file = "docs/examples/sars_cov2_monet.png"
        sfunks.make_graph(
            num_seqs, num_snps, record_ambs, record_snps, output_file,
            label_map, colours, length, 16, 6, "scale", False, False,
            "snps", False, None, None, False, True, False, None,
            False, None, gene_features, "monet", sequence_type
        )
        print(f"✓ Generated {output_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = generate_sars_cov2_examples()
    if success:
        print("\n✅ SARS-CoV-2 Morandi and Monet examples updated!")
    else:
        print("\n❌ Failed to generate examples")
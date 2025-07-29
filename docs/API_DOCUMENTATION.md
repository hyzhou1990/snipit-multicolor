# snipit-mc Python API Documentation

snipit-mc provides both command-line and Python API interfaces for generating beautiful SNP visualizations. This documentation covers the Python API, which allows you to integrate snipit-mc functionality directly into your Python scripts and workflows.

## Installation

```bash
pip install snipit-mc
```

## Quick Start

### Basic Usage

```python
from snipit import snipit_plot

# Generate a basic SNP plot
result = snipit_plot("alignment.fasta", colour_palette="nature")
print(f"Generated: {result['output_files']}")
```

### Using Configuration Objects

```python
from snipit import snipit_plot, SnipitConfig

# Create a configuration
config = SnipitConfig(
    colour_palette="vangogh",
    width=12,
    height=8,
    format="pdf",
    genbank="reference.gb"
)

# Generate plot with configuration
result = snipit_plot("alignment.fasta", config=config)
```

## API Reference

### Core Functions

#### `snipit_plot(alignment_file, config=None, **kwargs)`

Main function for generating SNP visualization plots.

**Parameters:**
- `alignment_file` (str or Path): Path to input alignment FASTA file
- `config` (SnipitConfig, optional): Configuration object with plot parameters
- `**kwargs`: Additional parameters that override config settings

**Returns:**
- `dict`: Dictionary containing:
  - `success` (bool): Whether the plot generation succeeded
  - `output_files` (list): List of generated output files
  - `config` (SnipitConfig): Final configuration used
  - `message` (str): Success or error message

**Example:**
```python
# Basic usage
result = snipit_plot("alignment.fasta", colour_palette="nature")

# Advanced usage
result = snipit_plot(
    "alignment.fasta",
    colour_palette="monet",
    width=15,
    height=10,
    format="svg",
    genbank="reference.gb",
    sort_by_mutation_number=True
)
```

#### `SnipitConfig`

Configuration class for snipit plotting parameters.

**Key Attributes:**

**Input Options:**
- `sequence_type` (str): 'nt' or 'aa'. Default: 'nt'
- `reference` (str): Reference sequence ID
- `labels` (str): Path to CSV file with sequence labels
- `genbank` (str): Path to GenBank file for gene annotations

**Output Options:**
- `output_file` (str): Output file name stem. Default: 'snp_plot'
- `format` (str): Output format ('png', 'pdf', 'svg', 'jpg', 'tiff'). Default: 'png'
- `write_snps` (bool): Write SNPs to CSV file. Default: False

**Figure Options:**
- `colour_palette` (str): Color palette name. Default: 'classic'
- `width` (float): Figure width
- `height` (float): Figure height
- `solid_background` (bool): Use solid background. Default: False
- `sort_by_mutation_number` (bool): Sort by SNP count. Default: False

**Example:**
```python
config = SnipitConfig(
    sequence_type="aa",
    colour_palette="nature_aa",
    width=12,
    height=8,
    format="pdf",
    solid_background=True,
    sort_by_mutation_number=True
)
```

### Convenience Functions

#### `quick_plot(alignment_file, palette="nature", **kwargs)`

Generate a quick plot with minimal configuration.

```python
from snipit import quick_plot

result = quick_plot("alignment.fasta", palette="vangogh", width=10)
```

#### `publication_plot(alignment_file, palette="nature", width=12, format="pdf", **kwargs)`

Generate a publication-ready plot with optimal settings.

```python
from snipit import publication_plot

result = publication_plot(
    "alignment.fasta",
    palette="nature",
    genbank="reference.gb"
)
```

#### `protein_plot(alignment_file, palette="nature_aa", **kwargs)`

Generate a plot optimized for protein sequences.

```python
from snipit import protein_plot

result = protein_plot("protein_alignment.fasta", palette="monet_aa")
```

#### `genbank_plot(alignment_file, genbank_file, palette="nature", **kwargs)`

Generate a plot with GenBank gene annotations.

```python
from snipit import genbank_plot

result = genbank_plot(
    "covid_sequences.fasta",
    "NC_045512.gb",
    palette="nature",
    width=14
)
```

### Utility Functions

#### `get_color_palettes()`

Get information about available color palettes.

```python
from snipit import get_color_palettes

palettes = get_color_palettes()
for name, info in palettes.items():
    print(f"{name}: {info['description']}")
```

#### `validate_alignment(alignment_file)`

Validate an alignment file for snipit compatibility.

```python
from snipit import validate_alignment

result = validate_alignment("alignment.fasta")
if result['valid']:
    print(f"Valid alignment with {result['num_sequences']} sequences")
else:
    print(f"Issues found: {result['issues']}")
```

## Color Palettes

### Artistic Palettes

snipit-mc includes several artistic color palettes inspired by famous painters:

#### Nature Style
- **Palette names:** `nature`, `nature_extended`, `nature_aa`
- **Description:** High-saturation colors suitable for Nature publications
- **Best for:** Scientific publications, clear data presentation

#### Morandi Style  
- **Palette names:** `morandi`, `morandi_extended`, `morandi_aa`
- **Description:** Muted, grey-toned colors inspired by Giorgio Morandi
- **Best for:** Sophisticated, artistic presentations

#### Van Gogh Style
- **Palette names:** `vangogh`, `vangogh_extended`, `vangogh_aa`  
- **Description:** Vibrant, expressive colors inspired by Vincent van Gogh
- **Best for:** Eye-catching, vibrant presentations

#### Monet Style
- **Palette names:** `monet`, `monet_extended`, `monet_aa`
- **Description:** Soft impressionist pastels inspired by Claude Monet
- **Best for:** Soft, elegant presentations

#### Matisse Style
- **Palette names:** `matisse`, `matisse_extended`, `matisse_aa`
- **Description:** Bold, pure colors inspired by Henri Matisse
- **Best for:** Bold, modern presentations

### Classic Palettes

- `classic`: Traditional SNP visualization colors
- `primary`: Primary colors  
- `purine-pyrimidine`: Color by base type
- `greyscale`: Monochrome visualization
- `wes`: Wes Anderson inspired
- `verity`: Pink/purple theme
- `ugene`: UGENE software colors (amino acids)

## Examples

### Example 1: Basic Nucleotide Analysis

```python
from snipit import snipit_plot, SnipitConfig

# Configure for nucleotide analysis
config = SnipitConfig(
    colour_palette="nature",
    width=12,
    height=8,
    format="png",
    sort_by_mutation_number=True
)

# Generate plot
result = snipit_plot("nucleotide_alignment.fasta", config=config)

if result['success']:
    print(f"Plot saved to: {result['output_files'][0]}")
else:
    print(f"Error: {result['message']}")
```

### Example 2: Protein Sequence Analysis

```python
from snipit import protein_plot

# Generate protein plot with Monet palette
result = protein_plot(
    "protein_alignment.fasta",
    palette="monet_aa",
    width=14,
    height=6,
    format="pdf"
)
```

### Example 3: SARS-CoV-2 Analysis with Gene Annotations

```python
from snipit import genbank_plot

# Download SARS-CoV-2 GenBank file first
# curl -o NC_045512.gb "https://www.ncbi.nlm.nih.gov/sviewer/..."

result = genbank_plot(
    "covid_sequences.fasta",
    "NC_045512.gb",
    palette="nature",
    width=15,
    height=10,
    sort_by_mutation_number=True,
    format="pdf"
)
```

### Example 4: Batch Processing

```python
from snipit import snipit_plot, SnipitConfig
from pathlib import Path

# Define color palettes to try
palettes = ["nature", "morandi", "vangogh", "monet"]

# Process multiple alignments
alignment_files = Path("data").glob("*.fasta")

for alignment_file in alignment_files:
    for palette in palettes:
        config = SnipitConfig(
            colour_palette=palette,
            output_file=f"{alignment_file.stem}_{palette}",
            format="png",
            width=12
        )
        
        result = snipit_plot(alignment_file, config=config)
        print(f"Generated {palette} plot for {alignment_file.name}")
```

### Example 5: Custom Analysis Pipeline

```python
from snipit import validate_alignment, snipit_plot, get_color_palettes

def analyze_alignment(alignment_file, output_dir="results"):
    """Complete analysis pipeline with validation and multiple outputs."""
    
    # Step 1: Validate alignment
    validation = validate_alignment(alignment_file)
    if not validation['valid']:
        print(f"Validation failed: {validation['issues']}")
        return
    
    print(f"Valid alignment: {validation['num_sequences']} sequences, "
          f"length {validation['alignment_length']}")
    
    # Step 2: Generate plots with different palettes
    palettes = ["nature", "morandi", "vangogh"]
    results = {}
    
    for palette in palettes:
        result = snipit_plot(
            alignment_file,
            colour_palette=palette,
            output_dir=output_dir,
            output_file=f"analysis_{palette}",
            format="png",
            width=12,
            write_snps=True,
            sort_by_mutation_number=True
        )
        results[palette] = result
    
    # Step 3: Generate publication-ready PDF
    pub_result = snipit_plot(
        alignment_file,
        colour_palette="nature",
        output_dir=output_dir,
        output_file="publication_figure",
        format="pdf",
        width=12,
        height=8,
        solid_background=True
    )
    results['publication'] = pub_result
    
    return results

# Run analysis
results = analyze_alignment("my_alignment.fasta")
```

## Error Handling

The API includes comprehensive error handling:

```python
from snipit import snipit_plot, validate_alignment

# Validate file first
validation = validate_alignment("alignment.fasta")
if not validation['valid']:
    print(f"File issues: {validation['issues']}")
    exit(1)

# Generate plot with error handling
try:
    result = snipit_plot("alignment.fasta", colour_palette="nature")
    
    if result['success']:
        print(f"Success: {result['message']}")
        print(f"Files: {result['output_files']}")
    else:
        print(f"Failed: {result['message']}")
        if 'error' in result:
            print(f"Error details: {result['error']}")
            
except FileNotFoundError as e:
    print(f"File not found: {e}")
except ValueError as e:
    print(f"Invalid parameter: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Integration with Jupyter Notebooks

snipit-mc works seamlessly in Jupyter notebooks:

```python
# In a Jupyter notebook cell
from snipit import quick_plot, get_color_palettes
from IPython.display import Image, display
import matplotlib.pyplot as plt

# Generate plot
result = quick_plot("alignment.fasta", palette="nature", format="png")

if result['success']:
    # Display the generated image
    display(Image(result['output_files'][0]))
    
    # Show available palettes
    palettes = get_color_palettes()
    print("Available palettes:")
    for name, info in palettes.items():
        if info['type'] == 'nucleotide':
            print(f"  {name}: {info['description']}")
```

## Advanced Configuration

### Working with Large Datasets

```python
from snipit import snipit_plot, SnipitConfig

# Configuration for large alignments
config = SnipitConfig(
    colour_palette="nature",
    include_positions="1-1000",  # Focus on specific region
    exclude_positions="500-600", # Exclude problematic region
    height=20,  # Tall figure for many sequences
    width=15,
    format="pdf"
)

result = snipit_plot("large_alignment.fasta", config=config)
```

### Recombination Analysis

```python
from snipit import snipit_plot, SnipitConfig

config = SnipitConfig(
    reference="REF_SEQUENCE",
    recombi_mode=True,
    recombi_references="PARENT1,PARENT2",
    colour_palette="nature",
    width=15
)

result = snipit_plot("recombinant_sequences.fasta", config=config)
```

## Performance Tips

1. **Use appropriate figure sizes**: Large figures take more memory and time
2. **Choose suitable formats**: PNG for web, PDF for publications, SVG for editing
3. **Filter positions**: Use `include_positions` and `exclude_positions` for large alignments
4. **Batch processing**: Process multiple files in loops for efficiency

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure snipit-mc is installed: `pip install snipit-mc`
2. **File Not Found**: Check file paths are correct and files exist
3. **Memory Issues**: For large alignments, try reducing figure size or filtering positions
4. **Format Issues**: Ensure alignment files are valid FASTA format

### Getting Help

- Check alignment validity: `validate_alignment("file.fasta")`
- View available palettes: `get_color_palettes()`
- Use error messages in the returned result dictionary
- Report issues at: https://github.com/hyzhou1990/snipit-multicolor/issues

## Changelog

### Version 0.0.4
- Added comprehensive Python API
- Added configuration classes
- Added utility and convenience functions
- Added validation functions
- Enhanced error handling

### Version 0.0.3
- Fixed image display on PyPI
- Updated documentation

### Version 0.0.2
- Enhanced PyPI metadata
- Improved package description

### Version 0.0.1
- Initial release with multicolor palettes
- GenBank annotation support
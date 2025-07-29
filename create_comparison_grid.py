#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import numpy as np

# Create figure with subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.patch.set_facecolor('white')

# Load and display images
images = [
    ('Classic', 'docs/examples/classic_example.png'),
    ('Nature', 'docs/examples/nature_example.png'),
    ('Morandi', 'docs/examples/morandi_example.png'),
    ('Van Gogh', 'docs/examples/vangogh_example.png'),
    ('Monet', 'docs/examples/monet_example.png'),
    ('Matisse', 'docs/examples/matisse_example.png')
]

for idx, (title, path) in enumerate(images):
    row = idx // 3
    col = idx % 3
    
    try:
        img = mpimg.imread(path)
        axes[row, col].imshow(img)
        axes[row, col].axis('off')
        axes[row, col].set_title(title, fontsize=16, fontweight='bold', pad=10)
    except:
        axes[row, col].text(0.5, 0.5, f'{title}\n(Image not found)', 
                            ha='center', va='center', fontsize=14)
        axes[row, col].axis('off')

plt.suptitle('snipit-multicolor: Artistic Color Palettes', fontsize=20, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig('docs/examples/palette_comparison.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()

# Create a showcase image with the best example
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('white')

try:
    img = mpimg.imread('docs/examples/nature_example.png')
    ax.imshow(img)
    ax.axis('off')
except:
    ax.text(0.5, 0.5, 'Nature Example\n(Image not found)', 
            ha='center', va='center', fontsize=14)
    ax.axis('off')

plt.title('snipit-multicolor: Publication-Ready SNP Visualization', 
          fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('docs/genome_graph.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()

print("Comparison grid created successfully!")
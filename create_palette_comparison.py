#!/usr/bin/env python3
"""
Create a palette comparison image showing the rounded rectangle design
"""

from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

def create_palette_comparison():
    """Create a comparison image showing multiple palettes with rounded rectangles"""
    
    # Image files for different palettes
    palette_images = [
        ("comparison_nature_rounded.png", "Nature Style"),
        ("comparison_morandi_rounded.png", "Morandi Style"), 
        ("comparison_vangogh_rounded.png", "Van Gogh Style"),
        ("comparison_monet_rounded.png", "Monet Style")
    ]
    
    # Check if all images exist
    missing_images = []
    for img_file, _ in palette_images:
        if not Path(img_file).exists():
            missing_images.append(img_file)
    
    if missing_images:
        print(f"Missing images: {missing_images}")
        print("Please run generate_rounded_examples.py first")
        return
    
    # Load images
    images = []
    labels = []
    
    for img_file, label in palette_images:
        try:
            img = Image.open(img_file)
            images.append(img)
            labels.append(label)
            print(f"Loaded: {img_file} ({img.size})")
        except Exception as e:
            print(f"Error loading {img_file}: {e}")
            return
    
    if not images:
        print("No images loaded")
        return
    
    # Calculate dimensions
    img_width = images[0].width
    img_height = images[0].height
    
    # Create comparison layout (2x2 grid)
    margin = 20
    label_height = 40
    grid_width = 2
    grid_height = 2
    
    total_width = grid_width * img_width + (grid_width + 1) * margin
    total_height = grid_height * (img_height + label_height) + (grid_height + 1) * margin
    
    # Create new image
    comparison = Image.new('RGB', (total_width, total_height), 'white')
    draw = ImageDraw.Draw(comparison)
    
    # Try to use a nice font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            font = ImageFont.load_default()
    
    # Place images in grid
    for i, (img, label) in enumerate(zip(images, labels)):
        row = i // grid_width
        col = i % grid_width
        
        # Calculate position
        x = margin + col * (img_width + margin)
        y = margin + row * (img_height + label_height + margin)
        
        # Paste image
        comparison.paste(img, (x, y))
        
        # Add label
        label_y = y + img_height + 5
        
        # Get text dimensions for centering
        bbox = draw.textbbox((0, 0), label, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = x + (img_width - text_width) // 2
        
        draw.text((text_x, label_y), label, fill='black', font=font)
    
    # Save comparison image
    output_file = "docs/examples/palette_comparison.png"
    comparison.save(output_file)
    print(f"Saved palette comparison to: {output_file}")
    
    return output_file

if __name__ == "__main__":
    create_palette_comparison()
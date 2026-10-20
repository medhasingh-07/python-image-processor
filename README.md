# Pure Python Image Processor

A command-line image processing tool built entirely in core Python (without NumPy, OpenCV, or Pillow) as part of a computer vision and vehicle perception foundation assignment.

## Features & Functions

1. **Pixel-Wise Operations:**
   - **Inversion (`invert`):** Reverses pixel brightness values by subtracting each from 255 (`255 - v`).
   - **Brightness Adjustment (`brightness`):** Adds a fixed value to every pixel and clamps the result between 0 and 255 to prevent overflow.
   - **Thresholding (`threshold`):** Converts the grayscale image into a binary black-and-white grid based on a specified cutoff value.

2. **Geometric Operations:**
   - **Horizontal Flip (`flip`):** Reverses the order of pixels in each row to create a mirror effect.
   - **90-Degree Clockwise Rotation (`rotate`):** Re-maps row and column indices to rotate the 2D grid clockwise.

3. **Neighborhood Operations:**
   - **3x3 Box Blur (`blur`):** Applies a spatial kernel filter by averaging surrounding neighbor pixels. Includes explicit boundary checking to handle edge pixels safely without out-of-bounds errors.

## What the Terminal Output Shows
The program prints structured 5x5 numerical grids (ranging from 0 to 255) in the terminal before and after each operation, allowing a reader to manually verify pixel-level transformations without needing a graphical display.

## How to Run
```bash
python3 image_processor.py

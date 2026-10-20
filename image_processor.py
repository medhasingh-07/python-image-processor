def show(img, name):
    print(f"\n--- {name} ---")
    for r in img:
        print(" ".join(f"{v:3d}" for v in r))
# 1. Original 5X5 Image
img = [
    [10, 20, 30, 20, 10],
    [20, 200, 220, 200, 20],
    [30, 220, 255, 220, 30],
    [20, 200, 220, 200, 20],
    [10, 20, 30, 20, 10],
]
show(img, "Original")

# 2. Pixel-wise: Invert
inv = [[255 - v for v in row] for row in img]
show(inv, "Inverted")

# 3. Pixel-wise: Brightness(+50)
bright = [[max(0, min(255, v+50))for v in row]for row in img]
show(bright, "Brightness +50")

# 4. Pixel-wise Threshold(>100)
thresh = [[255 if v>100 else 0 for v in row] for row in img]
show(thresh, "Threshold (>100)")

# 5. Geometric: Horizontal Flip
flip = [row[::-1] for row in img]
show(flip, "Flipped Horizontal")

# 6. Geometric: Rotate 90 Clockwise
rot = [[img[r][c] for r in range(4, -1, -1)] for c in range(5)]
show(rot, "Rotated 90 Clockwise")

# 7. Neighbourhood: 3X3 Box Blur
blur = [row[:] for row in img]
for r in range(5):
    for c in range(5):
        total, count = 0,0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if 0 <= i<5 and 0<= j<5:
                    total += img[i][j]
                    count += 1
        blur[r][c] = total // count
show(blur, "3X3 Box Blur")

# ==========================================
# BONUS: LOAD A PPM IMAGE BY HAND
# ==========================================

def load_ppm_manual(filename):
    """Parses a simple plain-text PPM (P3) image file line by line in pure Python."""
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Filter out comment lines starting with '#' and strip whitespace
    tokens = []
    for line in lines:
        line = line.split('#')[0].strip() # Remove comments
        if line:
            tokens.extend(line.split())
            
    # Read PPM header metadata
    magic_number = tokens[0]
    if magic_number != 'P3':
        raise ValueError("Not a valid P3 PPM file format!")
        
    width = int(tokens[1])
    height = int(tokens[2])
    max_val = int(tokens[3])
    
    # Extract pixel color triplets (R, G, B)
    pixel_data = [int(x) for x in tokens[4:]]
    
    # Reorganize into a 2D grid of RGB pixels
    image_grid = []
    idx = 0
    for r in range(height):
        row = []
        for c in range(width):
            r_val = pixel_data[idx]
            g_val = pixel_data[idx+1]
            b_val = pixel_data[idx+2]
            row.append((r_val, g_val, b_val))
            idx += 3
        image_grid.append(row)
        
    print(f"\n--- Loaded PPM Image ({width}x{height}) Successfully! ---")
    return image_grid
# Test the bonus function
# (It will look for a file named sample.ppm, or you can just print that the function is ready)
print("\n--- Bonus PPM Loader Ready ---")

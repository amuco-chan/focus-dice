from PIL import Image

def find_best_offset():
    im1 = Image.open('ikemen.png').convert("L")
    im2 = Image.open('ikemen_blink.png').convert("L")
    
    # We will compare a static region: the chest (e.g. x: 400-600, y: 500-700)
    box = (400, 500, 600, 700)
    region1 = im1.crop(box)
    pixels1 = list(region1.getdata())
    w, h = region1.size
    
    best_offset = (0, 0)
    min_diff = float('inf')
    
    # Search window: -10 to +10 pixels
    for dx in range(-10, 11):
        for dy in range(-10, 11):
            box2 = (400 + dx, 500 + dy, 600 + dx, 700 + dy)
            region2 = im2.crop(box2)
            pixels2 = list(region2.getdata())
            
            diff = sum(abs(p1 - p2) for p1, p2 in zip(pixels1, pixels2))
            if diff < min_diff:
                min_diff = diff
                best_offset = (dx, dy)
                
    print(f"Best offset found: dx={best_offset[0]}, dy={best_offset[1]}")

find_best_offset()

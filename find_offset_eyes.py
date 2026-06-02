from PIL import Image

def find_best_offset():
    im1 = Image.open('ikemen.png').convert("L")
    im2 = Image.open('ikemen_blink.png').convert("L")
    
    # We will compare the eye region but slightly expanded
    box = (380, 180, 640, 220)
    region1 = im1.crop(box)
    pixels1 = list(region1.getdata())
    w, h = region1.size
    
    best_offset = (0, 0)
    min_diff = float('inf')
    
    # Search window: -5 to +5 pixels
    for dx in range(-5, 6):
        for dy in range(-5, 6):
            box2 = (380 + dx, 180 + dy, 640 + dx, 220 + dy)
            region2 = im2.crop(box2)
            pixels2 = list(region2.getdata())
            
            diff = sum(abs(p1 - p2) for p1, p2 in zip(pixels1, pixels2))
            if diff < min_diff:
                min_diff = diff
                best_offset = (dx, dy)
                
    print(f"Best offset found for eyes: dx={best_offset[0]}, dy={best_offset[1]}")

find_best_offset()

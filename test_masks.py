from PIL import Image, ImageDraw, ImageFilter, ImageChops

def create_masked_layer(base_img, polygons, blur_radius, out_name):
    w, h = base_img.size
    mask = Image.new('L', (w, h), 0)
    draw = ImageDraw.Draw(mask)
    for poly in polygons:
        draw.polygon(poly, fill=255)
    
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Extract alpha from base_img and multiply by mask
    r, g, b, a = base_img.split()
    new_alpha = ImageChops.multiply(a, mask)
    
    layer = Image.merge("RGBA", (r, g, b, new_alpha))
    layer.save(out_name)
    print(f"Saved {out_name}")

img = Image.open('ikemen.png').convert("RGBA")

# Head (including some hair)
head_poly = [(300,50), (700,50), (700,450), (300,450)]
create_masked_layer(img, [head_poly], 40, 'layer_head.png')

# Front Hair
hair_poly = [(350,50), (674,50), (674,250), (350,250)]
create_masked_layer(img, [hair_poly], 20, 'layer_hair.png')

# Left Arm (viewer left)
l_arm_poly = [(0,400), (450,400), (450,1024), (0,1024)]
create_masked_layer(img, [l_arm_poly], 40, 'layer_arm_l.png')

# Right Arm (viewer right)
r_arm_poly = [(600,400), (1024,400), (1024,1024), (600,1024)]
create_masked_layer(img, [r_arm_poly], 40, 'layer_arm_r.png')

# Dice Area
dice_poly = [(400,600), (600,600), (650,900), (350,900)]
create_masked_layer(img, [dice_poly], 30, 'layer_dice.png')


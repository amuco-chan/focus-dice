from PIL import Image, ImageDraw, ImageFilter, ImageChops

def create_inverted_mask(w, h, polygons, blur_radius):
    mask = Image.new('L', (w, h), 255) # Start fully opaque
    draw = ImageDraw.Draw(mask)
    for poly in polygons:
        draw.polygon(poly, fill=0) # Erase these regions
    
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
    return mask

img = Image.open('ikemen.png').convert("RGBA")
w, h = img.size

# The polygons used for the arms earlier:
l_arm_poly = [(0,400), (450,400), (450,1024), (0,1024)]
r_arm_poly = [(600,400), (1024,400), (1024,1024), (600,1024)]

# Create a mask that erases the arms
# Wait, if we use a large blur, the arms will be semi-transparent near the edge, 
# which might still show a ghost. 
# We should use a slightly smaller polygon to erase the core of the arm, 
# or just a smaller blur so the arm is fully gone.
# Actually, the best way to prevent double vision is to completely erase the arm, 
# even eroding a bit into the body, because the overlapping arm layer will cover it anyway!

mask = create_inverted_mask(w, h, [l_arm_poly, r_arm_poly], 20)

r, g, b, a = img.split()
new_alpha = ImageChops.multiply(a, mask)

body_no_arms = Image.merge("RGBA", (r, g, b, new_alpha))
body_no_arms.save('layer_body_no_arms.png')
print("Saved layer_body_no_arms.png")

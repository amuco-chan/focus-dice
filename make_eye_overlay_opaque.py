from PIL import Image, ImageDraw, ImageFilter, ImageChops

img_blink = Image.open('ikemen_blink.png').convert("RGBA")
w, h = img_blink.size

mask = Image.new('L', (w, h), 0)
draw = ImageDraw.Draw(mask)

# Increase height slightly so the core remains 100% opaque after blur.
# Height: 40px (180 to 220).
bbox = [370, 180, 654, 220] 
# Use a rectangle with rounded corners or just a thicker ellipse
draw.ellipse(bbox, fill=255)

# Use a smaller blur radius (3px) so it only softens the very edge.
# This guarantees the center (the closed eyes) will remain at 255 (fully opaque),
# completely hiding the open eyes underneath.
mask = mask.filter(ImageFilter.GaussianBlur(3))

r, g, b, a = img_blink.split()
new_alpha = ImageChops.multiply(a, mask)

img_eyes = Image.merge("RGBA", (r, g, b, new_alpha))
img_eyes.save('ikemen_blink_eyes.png')
print("Saved fully opaque ikemen_blink_eyes.png!")

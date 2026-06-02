from PIL import Image, ImageDraw, ImageFilter, ImageChops

img_blink = Image.open('ikemen_blink.png').convert("RGBA")
w, h = img_blink.size

mask = Image.new('L', (w, h), 0)
draw = ImageDraw.Draw(mask)

# Make the mask extremely tight vertically to ONLY catch the eyelids.
# Avoid eyebrows (which are higher) and cheeks (which are lower).
bbox = [380, 185, 644, 215] 
draw.ellipse(bbox, fill=255)

# Smaller blur to prevent the mask from bleeding into eyebrows
mask = mask.filter(ImageFilter.GaussianBlur(8))

r, g, b, a = img_blink.split()
new_alpha = ImageChops.multiply(a, mask)

img_eyes = Image.merge("RGBA", (r, g, b, new_alpha))
img_eyes.save('ikemen_blink_eyes.png')
print("Saved perfectly tight ikemen_blink_eyes.png!")

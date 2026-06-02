from PIL import Image, ImageDraw, ImageFilter, ImageChops

img_blink = Image.open('ikemen_blink.png').convert("RGBA")
w, h = img_blink.size

mask = Image.new('L', (w, h), 0)
draw = ImageDraw.Draw(mask)

# If Y=250-330 was the mouth, the eyes must be higher up, around Y=150-230.
bbox = [360, 150, 664, 230] 
draw.ellipse(bbox, fill=255)

# Tight blur
mask = mask.filter(ImageFilter.GaussianBlur(15))

r, g, b, a = img_blink.split()
new_alpha = ImageChops.multiply(a, mask)

img_eyes = Image.merge("RGBA", (r, g, b, new_alpha))
img_eyes.save('ikemen_blink_eyes.png')
print("Saved fixed ikemen_blink_eyes.png!")

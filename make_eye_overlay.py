from PIL import Image, ImageDraw, ImageFilter
import os

img_blink = Image.open('ikemen_blink.png').convert("RGBA")
w, h = img_blink.size

# Create an empty mask
mask = Image.new('L', (w, h), 0)
draw = ImageDraw.Draw(mask)

# Define an ellipse around the eyes.
# Assuming standard anime portrait: 
# Center X ~ 512. Center Y ~ 300.
# Width ~ 400. Height ~ 200.
bbox = [350, 200, 674, 400]
draw.ellipse(bbox, fill=255)

# Apply Gaussian Blur for soft feathering
mask = mask.filter(ImageFilter.GaussianBlur(30))

# Apply the mask to the alpha channel of img_blink
r, g, b, a = img_blink.split()

# The new alpha is the minimum of original alpha and our mask
# Wait, let's just multiply them
def multiply_channels(c1, c2):
    return c1.point(lambda p: p) # need pixel access or ImageChops

from PIL import ImageChops
new_alpha = ImageChops.multiply(a, mask)

img_eyes = Image.merge("RGBA", (r, g, b, new_alpha))
img_eyes.save('ikemen_blink_eyes.png')
print("Saved ikemen_blink_eyes.png!")

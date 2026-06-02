from PIL import Image

# Open the images
img_main = Image.open('ikemen.png').convert("RGBA")
img_blink = Image.open('ikemen_blink.png').convert("RGBA")

# Make sure they are the same size
if img_main.size != img_blink.size:
    img_blink = img_blink.resize(img_main.size)

# Extract alpha channel from main image
r, g, b, alpha = img_main.split()

# Apply the alpha channel to the blink image
r_b, g_b, b_b, a_b = img_blink.split()
img_blink_transparent = Image.merge("RGBA", (r_b, g_b, b_b, alpha))

# Save the new blink image
img_blink_transparent.save('ikemen_blink.png')
print("Successfully applied alpha channel!")

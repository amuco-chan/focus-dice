from PIL import Image
import sys

img1 = Image.open('ikemen.png').convert("RGBA")
img2 = Image.open('ikemen_blink.png').convert("RGBA")

w, h = img1.size
best_dx = 0
best_dy = 0
min_diff = float('inf')

# We only care about the center region (where the face/body is)
cx1, cx2 = int(w*0.3), int(w*0.7)
cy1, cy2 = int(h*0.2), int(h*0.8)

# Convert to grayscale for diff
g1 = img1.convert("L").load()
g2 = img2.convert("L").load()

# Search window
search_range = 20

for dy in range(-search_range, search_range + 1):
    for dx in range(-search_range, search_range + 1):
        diff = 0
        for y in range(cy1, cy2, 5): # skip pixels to speed up
            for x in range(cx1, cx2, 5):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    v1 = g1[x, y]
                    v2 = g2[nx, ny]
                    diff += abs(v1 - v2)
                else:
                    diff += 255 # penalty
        
        if diff < min_diff:
            min_diff = diff
            best_dx = dx
            best_dy = dy

print(f"Best offset: dx={best_dx}, dy={best_dy}")

# Shift img2 by best_dx, best_dy
shifted = Image.new("RGBA", (w, h), (0, 0, 0, 0))
shifted.paste(img2, (-best_dx, -best_dy))
shifted.save('ikemen_blink.png')
print("Saved aligned image!")

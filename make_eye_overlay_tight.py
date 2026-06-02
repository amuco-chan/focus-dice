from PIL import Image, ImageDraw, ImageFilter, ImageChops

img_blink = Image.open('ikemen_blink.png').convert("RGBA")
w, h = img_blink.size

mask = Image.new('L', (w, h), 0)
draw = ImageDraw.Draw(mask)

# 以前のbbox = [350, 200, 674, 400] は縦に広すぎたため、口元まで入っていた可能性大。
# 目元だけに絞るため、縦幅を極端に狭くする。
# 目はおおよそ上から1/4〜1/3付近にあると想定。
bbox = [380, 250, 644, 330] 
draw.ellipse(bbox, fill=255)

# ぼかしも弱めにして、鼻や口元に影響が出ないようにする
mask = mask.filter(ImageFilter.GaussianBlur(15))

r, g, b, a = img_blink.split()
new_alpha = ImageChops.multiply(a, mask)

img_eyes = Image.merge("RGBA", (r, g, b, new_alpha))
img_eyes.save('ikemen_blink_eyes.png')
print("Saved ikemen_blink_eyes.png with tight mask!")

from PIL import Image, ImageDraw, ImageFilter, ImageChops

img_blink = Image.open('ikemen_blink.png').convert("RGBA")
w, h = img_blink.size

mask = Image.new('L', (w, h), 0)
draw = ImageDraw.Draw(mask)

# 以前の幅は横に広すぎたため（X: 370〜654）、耳の横のAI生成のゴミ（白いピクセル等）を拾っていた。
# 目の周辺だけに限定するため、横幅を左右50pxずつ削る。
# bbox = [420, 180, 604, 220]
bbox = [410, 180, 614, 220] 
draw.ellipse(bbox, fill=255)

# 中心を不透明に保ちつつ境界だけなじませる
mask = mask.filter(ImageFilter.GaussianBlur(4))

r, g, b, a = img_blink.split()
new_alpha = ImageChops.multiply(a, mask)

img_eyes = Image.merge("RGBA", (r, g, b, new_alpha))
img_eyes.save('ikemen_blink_eyes.png')
print("Saved narrow ikemen_blink_eyes.png!")

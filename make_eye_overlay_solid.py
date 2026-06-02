from PIL import Image, ImageDraw, ImageFilter, ImageChops

img_blink = Image.open('ikemen_blink.png').convert("RGBA")
w, h = img_blink.size

mask = Image.new('L', (w, h), 0)
draw = ImageDraw.Draw(mask)

# 楕円（ellipse）だと端のほうが細くなってしまい、元の開いている目が見えて（透けて）しまっていた可能性大。
# 四角形（rectangle）にして、元の目を100%確実に覆い隠すようにする。
# さらに縦幅も少しだけ広げて、目が確実に見えなくなるようにする。
bbox = [400, 170, 620, 230] 
draw.rectangle(bbox, fill=255)

# 境界のぼかしも最小限（3px）にとどめる
mask = mask.filter(ImageFilter.GaussianBlur(3))

r, g, b, a = img_blink.split()
new_alpha = ImageChops.multiply(a, mask)

img_eyes = Image.merge("RGBA", (r, g, b, new_alpha))
img_eyes.save('ikemen_blink_eyes.png')
print("Saved solid rectangle ikemen_blink_eyes.png!")

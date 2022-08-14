from PIL import Image, ImageDraw
im = Image.new("RGB", (256,256))
draw = ImageDraw.Draw(im)
draw.ellipse((64,64,192,192),fill=(255,0,0))

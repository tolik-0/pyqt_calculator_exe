from pathlib import Path
from PIL import Image, ImageDraw

size = 128
img = Image.new('RGBA', (size, size), (240, 244, 250, 0))
draw = ImageDraw.Draw(img)

body_color = (44, 62, 80, 255)
border_color = (236, 240, 241, 255)
draw.rounded_rectangle((12, 12, 116, 116), radius=12, fill=body_color, outline=border_color, width=3)

# Screen
draw.rounded_rectangle((24, 20, 104, 44), radius=6, fill=(93, 173, 226, 255), outline=border_color, width=2)
draw.rectangle((26, 22, 102, 42), fill=(191, 235, 255, 255))

# Buttons
btn_fill = (236, 240, 241, 255)
btn_outline = (52, 73, 94, 255)
btn_special = (241, 196, 15, 255)
start_x, start_y = 28, 52
btn_size = 18
pad = 10
labels = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
]
for r, row in enumerate(labels):
    for c, label in enumerate(row):
        x0 = start_x + c * (btn_size + pad)
        y0 = start_y + r * (btn_size + pad)
        x1 = x0 + btn_size
        y1 = y0 + btn_size
        fill = btn_special if label in {'C', '+'} else btn_fill
        draw.rounded_rectangle((x0, y0, x1, y1), radius=4, fill=fill, outline=btn_outline, width=2)
        draw.text((x0 + 5, y0 + 2), label, fill=btn_outline)

# Equals key
draw.rounded_rectangle((28, 104, 100, 118), radius=6, fill=(39, 174, 96, 255), outline=btn_outline, width=2)
draw.text((58, 106), '=', fill=(255, 255, 255, 255))

sizes = [128, 64, 48, 32, 24, 16]
img.save('calculator.ico', format='ICO', sizes=[(s, s) for s in sizes])
print('Icon created at calculator.ico')

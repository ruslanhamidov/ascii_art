from PIL import Image
from colorama import Fore
from cam import capture_photo
import sys

ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

if sys.argv[1] == 'capture':
    capture_photo()
    path = 'capture.jpg'
else:
    path = sys.argv[1]
color = getattr(Fore, sys.argv[2].upper())
formula = sys.argv[3]

im = Image.open(f"images/{path}")

new_width = im.width // 7
new_height = im.height // 7

shrunk_img = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
shrunk_img.save("images/shrunk_scaled.jpg")

pixels = shrunk_img.load()
print(f"""Successfully constructed pixel matrix!
Pixel matrix size: {new_width}x{new_height}
Iterating through pixel contents:
""")

for row in range(new_height):
    res = 0
    for col in range(new_width):
        rgb = pixels[col, row]
        match formula:
            case 'a':
                res = sum(rgb) / 3
            case 'mm':
                minimum = min(rgb)
                maximum = max(rgb)

                res = int((minimum + maximum) / 2)
            case 'l':
                res = int(0.21 * rgb[0] + 0.72 * rgb[1] + 0.07 * rgb[2])
            case 'i':
                res = (255 - sum(rgb)) / 3
        for _ in range(3):
            if res == 0:
                print(color + ascii[0], end='')
            else:
                print(color + ascii[int(100 / (255 / res) * 0.2)], end='')
    print()

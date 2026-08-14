from PIL import Image
import sys
from colorama import Fore

path = sys.argv[1]
color = getattr(Fore, sys.argv[2].upper())
im = Image.open(f"images/{path}")

ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

new_width = im.width // 7
new_height = im.height // 7

# Resize using the high-quality Resampling.LANCZOS filter
shrunk_img = im.resize((new_width, new_height), Image.Resampling.LANCZOS)
shrunk_img.save("shrunk_scaled.jpg")

pixels = shrunk_img.load()
print(f"""Successfully constructed pixel matrix!
Pixel matrix size: {new_width}x{new_height}
Iterating through pixel contents:
""")

# formula = int(100 / (255 / n) * 0.2)
for row in range(new_height):
    sum_of_rgb = 0
    for col in range(new_width):
        sum_of_rgb = sum(pixels[col, row])
        brightness = sum_of_rgb / 3
        for _ in range(3):
            if brightness == 0:
                print(color + ascii[0], end='')
            else:
                print(color + ascii[int(100 / (255 / brightness) * 0.2)], end='')
    print()

'''Pillow: redimensionando imagens com Python'''
from PIL import Image
from pathlib import Path

ROOT = Path(__file__).parent
ORIG = ROOT / 'original.jpg'
NEW = ROOT / 'new.jpg'


pil_image = Image.open(ORIG)
width, height = pil_image.size
exif = pil_image.info['exif']

new_width = 640
new_height = round(height * new_width / width) # type: ignore

new_img = pil_image.resize((new_width, new_height))
new_img.save(
    NEW,
    optimize=True,
    quality=70,
    exif=exif,
)
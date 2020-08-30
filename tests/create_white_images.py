from PIL import Image, ImageDraw

img = Image.new('RGB', (690,245), color='white')
img.save('white_wide.jpg')


img = Image.new('RGB', (340,500), color='white')
img.save('white_tall.jpg')

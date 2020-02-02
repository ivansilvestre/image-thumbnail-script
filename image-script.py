from PIL import Image, ImageFilter

img = Image.open("path")
img.thumbnail((100, 100))
img.save("thumbnail.jpg")


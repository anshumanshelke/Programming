from PIL import Image

img = Image.open("color.png")

print(img.size)

img = img.convert("L")          # L = grey scale 
img = img.resize((2048,2048))

img.save("color_XX.png")
print(img.size)
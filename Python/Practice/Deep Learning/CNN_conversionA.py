from PIL import Image

img = Image.open("color.png")

print(img.size)

img = img.convert("L")          # L = grey scale 
img = img.resize((2048,2048))

#here change in parameters are not only for experimental purposes- 
#But also signify that there are limits- and pixels can be concised 
#But not Increased- to increase the quality of the image

img.save("color_XX.png")
print(img.size)

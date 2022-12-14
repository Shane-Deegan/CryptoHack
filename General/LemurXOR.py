from PIL import Image, ImageChops

image1 = Image.open('firstImage.png')
image2 = Image.open('SecondImage.png')

#use import to XOR bits by subtracting the image bits from each other and compaing the images
image3 = ImageChops.add(ImageChops.subtract(image2, image1), ImageChops.subtract(image1, image2))

#show image to extract key
image3.show()

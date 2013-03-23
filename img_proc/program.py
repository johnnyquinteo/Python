import Image

img = Image.open('img/DSC04977.JPG')
breathe = Image.open('breathe.png')
virgen = Image.open('virgen.png')
camara = Image.open('camara.png')

# print img.format, breathe.format, virgen.format, camara.format

# print breathe.size, breathe.format
# img_crop = breathe.crop((0,0,20,20))
# print img_crop.size, img_crop.format
# breathe.paste(img_crop)

breathe.format = 'JPEG'
img.paste(breathe,(0,0),breathe)
img.save('img1.jpg')

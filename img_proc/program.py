import Image
import ImageEnhance
import os

# VARIABLES DE CONFIGURACION
result_path = 'Imagenes'
base_name = 'Imagen'
start_num = 1
center = 'front_images/breathe.png'
corner = 'front_images/virgen.png'

# DICCIONARIOS
pos_script = {
	'top-left':'(0,0)',
	'top-center':'(0,(img_back.size[1]/2) - (img_front.size[1]/2))',
	'top-right':'(0,img_back.size[1]-img_front.size[1])',
	'center-left':'((img_back.size[0]/2) - (img_front.size[0]/2),0)',
	'center':'((img_back.size[0]/2) - (img_front.size[0]/2), (img_back.size[1]/2) - (img_front.size[1]/2))',
	'center-right':'((img_back.size[0]/2) - (img_front.size[0]/2),img_back.size[1]-img_front.size[1])',
	'bottom-left':'(img_back.size[0]-img_front.size[0],0)',
	'botom-center':'(img_back.size[0]-img_front.size[0],(img_back.size[1]/2) - (img_front.size[1]/2))',
	'bottom-right':'(img_back.size[0]-img_front.size[0],img_back.size[1]-img_front.size[1])'
}

def change_opacity(img,opacity):
	"""Cambia la opacidad de una imagen"""
	if img.mode != 'RGBA':
		img = img.convert('RGBA')
	else:
		img = img.copy()
	alpha = img.split()[3]
	alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
	img.putalpha(alpha)
	return img

def pos_scale(img_back,img_front,position,scale=1):
	"""Posiciona la imagen y la escala
	Se puede mejorar: posiciones verticales en un diccionario y horizontales en otro ademas de eso peromitir posiciones dadas por valores numericos"""
	layer = Image.new('RGBA',img_back.size,(0,0,0,0))
	img_front = img_front.resize((int(img_front.size[0]*scale),int(img_front.size[1]*scale)))
	x,y = eval(pos_script[position])
	layer.paste(img_front,(x,y))
	return Image.composite(layer,img_back,layer)

def watermaker(img):
	img = img.convert('RGBA')
	corner_img = Image.open(corner)
	center_img = Image.open(center)
	corner_img = change_opacity(corner_img, 0.5)
	center_img = change_opacity(center_img, 0.3)
	return pos_scale(pos_scale(img,corner_img,'bottom-right'),center_img,'center',8.5)

def test():
	if not os.path.isdir(result_path):
		os.mkdir(result_path)
	for root,dirs,files in os.walk('img'):
		i = start_num
		files = files[2:]
		count = len(files)
		for file_name in files:
			img = Image.open(os.path.join(root, file_name))
			img = watermaker(img)
			img.save(result_path+'/'+base_name+str(i)+'.jpg')
			print str(int((float(i)/count)*100))+'% - '+file_name+'\n'
			i += 1



if __name__ == '__main__':
    test()


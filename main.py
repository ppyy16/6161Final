
#CS6161 Algo Final 
import sys
from seam_carving import SeamCarving
from PIL import Image



def mainer(image):
	pic = Image.open(image)
	pixels = pic.load()
	w, h = pic.size
	image_info = [[[0 for k in range(3)] for j in range(h)] for i in range(w)]
	for i in range(w):
	    for j in range(h):
	        image_info[i][j][0] = pixels[i, j][0]
	        image_info[i][j][1] = pixels[i, j][1]
	        image_info[i][j][2] = pixels[i, j][2]


	

	SeamCarver = SeamCarving()
	weight = SeamCarver.run(image_data)
	print("weight: " + str(weight))
	print("seam: " + str(SeamCarver.getSeam()))


	seam = SeamCarver.getSeam() 
	y = 0
	for x in seam:
	    pic.putpixel((x,y), 0x000000ff)
	    y = y+1
	pic.show()



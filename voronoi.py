from PIL import Image
import random
import math




def nrandompixels(image, points, numcells):
	width, height = image.size
	
	#new image canvas
	newimage = Image.new("RGB", (width, height))


	nx = []
	ny = []


	imgx, imgy = image.size
	# image = image.convert('RGB')

	image.show()
	loaded = image.load()



	for i in range(int(points)):
		nx.append(random.randrange(imgx))
		ny.append(random.randrange(imgy))
		# print(nx[count], ny[count])

	voronoi(nx, ny, points, newimage, loaded, image, int(numcells))

	#find the pixel color at given point
	# img[x,y] = value


def voronoi(nx,ny, points, canvas, loaded, image, num_cells):
	iterator = 0
	xlen = len(nx)
	ylen = len(ny)


	# def hypot(X,Y):
 #    	return (X-x)**2 + (Y-y)**2


	putpixel = canvas.putpixel

	imgx, imgy = image.size

	
	colors = []

	nr = []
	ng = []
	nb = []

	for i in range(xlen):
		x = nx[i]
		y = ny[i]
		#rgba


		color = loaded[x,y]

		nr.append(color[0])
		ng.append(color[1])
		nb.append(color[2])

		colors.append(color)
		# print x, y, color


		putpixel((x,y), color)


	# print(num_cells)

	for y in range(imgy):
			for x in range(imgx):
				dmin = math.hypot(imgx-1, imgy-1)
				j = -1
				for i in range(num_cells):
					d = math.hypot(nx[i]-x, ny[i]-y)
					if d < dmin:
						dmin = d
						j = i
				# print(x,y)
				putpixel((x, y), (nr[j], ng[j], nb[j]))






	canvas.save("rollerballedited.png", "PNG")
	canvas.show()




 


# img = Image.open('test1.jpeg')  
# # d = grey_scale(img)

# nrandompixels(img, 10,10)


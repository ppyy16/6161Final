from seam_carving import SeamCarving

from voronoi import nrandompixels

import imghdr

import sys

from pprint import pprint

import inquirer

from main import mainer

from PIL import Image


     


image = raw_input("What image would you like to manipulate? \n")


isimage = imghdr.what(image)




if isimage == None:
	pprint("File is not an image, try again")
	sys.exit()




questions = [
    inquirer.List('program',
                  message="Which function would you like to use?",
                  choices=['Voronoi', 'Seam Carving'],
              ),
]

answer = inquirer.prompt(questions)

value = answer["program"]

if value == "Seam Carving":
	pprint("Loading...")
	mainer(image)
	sys.exit()


elif value == 'Voronoi':
	openedimage = Image.open(image)
	points = raw_input("Number of random points? ")
	cells = raw_input("Number of cells? ")

	pprint("Loading...")
	nrandompixels(openedimage, points, cells)
	sys.exit()

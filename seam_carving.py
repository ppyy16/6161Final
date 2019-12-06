
#ALGO GROUP 
#SEAM CARVING

import math
import numpy
class SeamCarving:
    def __init__(self):
        self.energyList = []
        return

  
    # @return the seam's weight
    def run(self, image):

        rows = len(image[0])-1
        cols = len(image)-1


        cost = numpy.zeros((rows+1,cols+1)).astype(float)

        
        for i in range(0,rows+1):
            for j in range(0,cols+1):
                if i == 0:
                    cost[i][j] = self.energy(image,j,i)
                else:
                    if j == (cols):
                        cost[i][j] = min(cost[i - 1][j - 1], cost[i - 1][j]) + self.energy(image,j,i)
                    elif j == 0:
                        cost[i][j] = min(cost[i - 1][j], cost[i - 1][j + 1]) + self.energy(image,j,i)
                    else:
                        #cost[i][j] = cost[i - 1][j] + self.energy(image,j,i)
                        cost[i][j] = min(cost[i-1][j-1],cost[i-1][j],cost[i-1][j+1]) + self.energy(image,j,i)
        self.energyList = cost
        
        return min(cost[rows][:])
        



    


    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        
        rows = len(self.energyList)-1
        
        result = []
        size = None
        
        for row in range(rows,-1,-1):
            if row == rows:
                location = numpy.argmin(self.energyList[row][:])
                
                result.append(location)
                size = 0
               
            else:
                searchLocation = result[size]
                searchrange = self.energyList[row][searchLocation-1:searchLocation+2]
                
                location = numpy.argmin(searchrange)
                
            
                result.append(location+(searchLocation-1))

                
                size += 1
                

        result.reverse()
        return result
         


    def energy(self,image,col,row):
        rowBound  = len(image[0])-1
        colBound = len(image)-1
        pixel = (col,row)
        
        if pixel == (0,0): #Top Left 
            p_right = self.euclidian3D(image,col,row,col+1,row)
            p_down = self.euclidian3D(image,col,row,col,row+1)
            calc = (p_right + p_down)/2

            return calc

        elif pixel == (colBound,0): #Top Right 
            p_down = self.euclidian3D(image,col,row,col,row+1)
            p_left = self.euclidian3D(image,col,row,col-1,row)
            calc = (p_down + p_left)/2
            return calc
        elif pixel == (0,rowBound): #Bottom Left
            p_right = self.euclidian3D(image,col,row,col+1,row)
            p_up = self.euclidian3D(image,col,row,col,row-1)
            calc = (p_up + p_right)/2

            return calc
        elif pixel == (colBound,rowBound): #Bottom Right 
            p_left = self.euclidian3D(image,col,row,col-1,row)
            p_up = self.euclidian3D(image,col,row,col,row-1)
            calc = (p_left + p_up)/2
            return calc
      
        elif (col in range(1,colBound) and row == 0): #TopBoundry
            p_left = self.euclidian3D(image,col,row,col-1,row)
            p_right = self.euclidian3D(image,col,row,col+1,row)
            p_down = self.euclidian3D(image,col,row,col,row+1)
            calc = (p_left + p_right + p_down)/3

            return calc
        elif (col in range(1,colBound) and row == rowBound): #Bottom Boundry
            p_left = self.euclidian3D(image,col,row,col-1,row)
            p_right = self.euclidian3D(image,col,row,col+1,row)
            p_up = self.euclidian3D(image,col,row,col,row-1)
            calc = (p_left + p_right + p_up)/3

            return calc


        elif col == 0 and (row in range(1,rowBound)): #Left Boundry
            p_right = self.euclidian3D(image,col,row,col+1,row)
            p_up = self.euclidian3D(image,col,row,col,row-1)
            p_down = self.euclidian3D(image,col,row,col,row+1)
            calc =  (p_right + p_up + p_down)/3

            return calc
        elif col == colBound and (row in range(1,rowBound)): #Right Boundry
            p_left = self.euclidian3D(image,col,row,col-1,row)
            p_up = self.euclidian3D(image,col,row,col,row-1)
            p_down = self.euclidian3D(image,col,row,col,row+1)
            calc = (p_left + p_up + p_down)/3
            return calc
        else:
            p_left = self.euclidian3D(image,col,row,col-1,row)
            p_right = self.euclidian3D(image,col,row,col+1,row)
            p_up = self.euclidian3D(image,col,row,col,row-1)
            p_down = self.euclidian3D(image,col,row,col,row+1)
            calc = (p_left + p_right + p_up + p_down)/4
            return calc




    
    

    def euclidian3D(self,image,col1,row1,col2,row2):
            redCalc = (image[col1][row1][0] - image[col2][row2][0]) ** 2
            greenCalc = (image[col1][row1][1] - image[col2][row2][1]) ** 2
            blueCalc = (image[col1][row1][2] -  image[col2][row2][2]) ** 2
            calc = math.sqrt(redCalc + blueCalc + greenCalc)
            return calc 











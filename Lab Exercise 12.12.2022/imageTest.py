##Lab Exercise 12/12/2022
##Author: 

from images import Image

def main(filename = "smokey.gif"):
    image = Image(filename)
    image.draw()
    blackAndWhite(image)
    image.draw()
    grayScale(image)
    image.draw()
    image = detectEdges(image,40)
    image.draw()

def blackAndWhite(image):
    #Add code here
    

def grayScale(image):
    #Add code here
    

def detectEdges(image, amount):
    

main()

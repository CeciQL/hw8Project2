#Exercise: Homework 8 Project 2
#File Name: hw8Project2.py
#Programmer: Cecilia Dougherty
#Date:       05/2022
#
#Overall Plan:def grayscale; get file; use image file to get dynamic of window; get center point of photo; get current Pixel for loop

from graphics import*

print("This program grayscales images\n")

def grayscale(): \
  
    infile = input('In what file is the image?: ')
    outfile = input('What file do you want it saved?: ')

    file = Image(Point(0,0), infile)
    width = file.getWidth()
    height = file.getHeight()

    cWidth = width / 2
    cHeight = height / 2
    cen = Point(cWidth, cHeight)

    image = Image(cen,infile)
    win = GraphWin("Grayscale Image", width, height)
    image.draw(win)

    p = win.getMouse()
    x = p.getX()
    y = p.getY()

    for x in range(height):
        for y in range(width):
            r, g, b = image.getPixel(x, y)
            gray = int(round(.299*r + .587*g + .114*b))
            image.setPixel(x,y, color_rgb(gray, gray, gray))
 
            win.update()
         
    image.save(outfile)
    win.getMouse()
    win.close()

grayscale()
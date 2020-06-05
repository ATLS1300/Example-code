#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use
colormode(255)

#Create a panel to draw on. 
panel = Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#=======Add your code here======

shaper = Turtle()

# Let's pick up the pen and move it toward the middle of our screen
# and draw some shapes
shaper.up()
shaper.goto(200,200)
shaper.down()

# Now let's create some variables to draw our shape
size = 100 # change this value to change size of square
numSides = 4 # determines the number of sides in your shape
angle = 360/numSides # determines inside angle of shape

# This for loop will draw a square
for i in range(numSides):
    shaper.forward(size)
    shaper.right(angle)
    

# Using this formula, we can change one value and draw different shapes!
    
# First let's move the turtle again.
shaper.up()
shaper.forward(200)
shaper.down()

# Now let's change numSides to 5, and redefine our angle
numSides = 5
angle = 360/numSides

# And now we can use that SAME EXACT LOOP but make a different shape!

# This for loop will draw a pentagon
for i in range(numSides):
    shaper.forward(size)
    shaper.right(angle)
    
shaper.up()
shaper.left(90)
shaper.forward(200)
shaper.down()
    
# Your turn! Try drawing a hexagon with a side size of 50...


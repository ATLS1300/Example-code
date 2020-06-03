#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

#Create a panel to draw on. 
panel = Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, -h, 0)

#### LIST OF COLORS ####
'''yellow, gold, orange, red, maroon, violet, magenta, purple, navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white.

'''
#=======Add your code here======

panel = Screen()
panel.clear()
panel.bgcolor("orange")

# Create a turtle
Harry = Turtle()

# Change its shape to a circle
Harry.shape("circle")

# Move it around and rotate.
Harry.forward(150)
Harry.right(90) #degrees
Harry.forward(100)

# Send it to a specific location
Harry.goto(0,0)

# Go to a specific location without drawing
Harry.up() 
Harry.goto(200,300)
Harry.down()

# Change color!
Harry.color("chocolate")

# Draw shapes!
Harry.circle(50) # pass in radius
Harry.dot(50) # pass in diameter

Harry.up() #pick up the pen
Harry.forward(100)
Harry.down() # put down the pen to draw

# Change color!
Harry.color("white","turquoise")

# Filled shapes
# To fill in the shape, call begin_fill() BEFORE drawing the shape
Harry.begin_fill() # Don't put anything in the parentheses
Harry.circle(50)
Harry.end_fill() # End fill gets called AFTER you draw the shape.

# Change color with RGB values

#########################################
colormode(255) # Required function!!   ##
#########################################

myRGB = (80, 129, 152) #make a color, always put color values in parentheses!
Harry.color(myRGB) # put your color variable in the color function

Harry.pensize(10) # change pen thickness
Harry.forward(100)

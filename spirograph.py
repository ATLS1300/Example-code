#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
ATLS 1300
Author: Dr. Z
Spirograph example
'''

import math
from turtle import * #import the library of commands that you'd like to use
colormode(255)

#Create a panel to draw on. 
panel = Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#=======Add your code here======
spiro = Turtle()
colormode(255)

panel.bgcolor('black')
spiro.color((80,80,200))
spiro.speed(10) #fastest speed
spiro.up()

#===============================
#Polygon spirograph

#set the size, number of sides, and internal angle of your shape that will make your spirograph
size = 50
sides = 5
angle = 360/sides

inc = 10 # angle increment between shapes in pattern
numIt = int(360/inc) # the number of iterations to make a complete circle. 
innerCirc = 20 # radius of inner circle

spiro.goto(400,500)
for k in range(numIt):
    spiro.down()
    for i in range(sides):
        spiro.forward(size)
        spiro.right(angle)
    spiro.up()
    spiro.forward(innerCirc)
    spiro.right(inc)

#===============================
#Circle spirograph
    
inc = 10 # angle increment between shapes in pattern
numIt = int(360/inc) # the number of iterations to make a complete circle. 
innerCirc = 2 # radius of inner circle
rad = 50 #radius of circles drawn in pattern

spiro.goto(200,200)
for k in range(numIt):
    spiro.down()
    spiro.circle(rad)
    spiro.forward(innerCirc)
    spiro.right(inc)    
    

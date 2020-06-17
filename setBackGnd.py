#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:55:03 2020

@author: Dr Z
Uses a turtle to drop a photo as the background. For upper left origin ONLY!
"""
import random
from turtle import * #import the library of commands that you'd like to use
colormode(255)
delay(3000)

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

backGnd = Turtle()
colormode(255) # 0-255 RGB
spider.up()
spider.speed(10)

bkgnd = input('Enter the name of your background image, with extension. (.gif only) ')

panel.addshape(bkgnd)

# NOTE: using panel.bgpic() will place the picture at the original (0,0) and
# there's no easy way to fix it. Instead, we'll change the Turtle into a
# background, and stamp it in the middle of our screen, then change it to the 
# spider shape

# Make background
backGnd.shape(bkgnd)
backGnd.goto(w/2,h/2)  #spider.home()
backGnd.stamp()
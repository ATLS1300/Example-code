#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 00:06:47 2020

@author: Dr. Z
Creates a turtle that moves to the location of a mouse click
"""
#Modified from https://keepthinkup.wordpress.com/programming/python/python-turtle-handling-with-mouse-click/

import turtle

turtle.setup(400,500) # sets up screen size and turns on listener ***REQUIRED***
window = turtle.Screen() # create our Screen variable
window.clear()
window.title("How to handle mouse clicks on the window!")
window.bgcolor("lightgreen")

# Create our turle variable
draw = turtle.Turtle() 
draw.color("darkblue")
draw.pensize(3)
draw.shape("circle")
 
# define callback function. This one makes the turtle go to the click location
def h1(x, y): # for click callbacks, x and y should be set up as parameters
  draw.goto(x, y) # when called with click, x and y names get click coordinate values (pixels)
 
window.onclick(h1) # now set up mouseclick, pass the NAME of the function in as an argument

window.mainloop() # call mainloop to keep the click listener running.

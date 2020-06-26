#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:28:53 2020

@author: Dr. Z
Click counter - this code demonstrates how we can build a counter that determines clicks
"""

from turtle import *

colormode(255)

#Create a panel to draw on. 
setup()
panel = Screen()
panel.clear()
w = 200 # width of panel
h = 200 # height of panel
panel.setup(width=w, height=h)
panel.setworldcoordinates(0, w, h, 0)

square = Turtle(shape='square')
fillcolor = 'yellow'
square.color('black',fillcolor)
square.up()
square.goto(100,100)

clicked = False # boolean to determine click count (for two options)

def changeColor(x,y):
    global clicked # callbacks are funny, so we have to make out variables global
    clicked = not clicked
    if clicked:
        square.color('black','red')
        print('first click')
        print('clicked is ' + str(clicked))
    else:
        square.color('black','pink')
        print('second click')
        print('clicked is ' + str(clicked))

# Becuase clicked is a global, it updates and can be used elsewhere in your script.
# You can use clicked as a conditional statement for different tasks!
       
panel.onclick(changeColor)
listen()


done()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:01:00 2020

@author: Dr. Z
Keypress refresh for GENERATIVE ART GALLERIES
When creating your art, this will allow a keystroke to be added in that will clear your screen.
In the code following, you can generate the next piece.

I recommend organizing your code so that each drawing is contained in a function
Then, after every keypress, you call a specific function.

=============== TO TEST THIS CODE ===================
Select the window and hit the 'n' key to change the background color from the original
light blue to white.
"""

import random
from turtle import * #import the library of commands that you'd like to use
#import winsound
from pydub.playback import _play_with_simpleaudio as Play
from pydub import AudioSegment

#Create a panel to draw on. 
setup()
panel = Screen()
panel.clear() # "refreshes" the panel

w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
panel.setworldcoordinates(0, w, h, 0)

panel.bgcolor('light blue')

def close():
    bye()

def drawImg():
    global panel
    panel.clear()
    panel.bgcolor('gray')
    circle = Turtle(shape='circle')
    colormode(255)
    red = [255,0,0]
    circle.color('black',tuple(red))
    circle.up()
    circle.goto(100,100)
    for i in range(50):
        circle.stamp()
        circle.right(30)
        circle.fd(8)
        red[0] -= 5
        if red[0]<0:
            red[0]=0
        circle.color('black',tuple(red))
    panel.delay(3000)
    panel.clear()
    #panel.onkey(panel.clear,'n')
    panel.onkey(close,'Escape')

def clear():
    panel.clear()
    panel.onkey(drawImg,'1')
    panel.onkey(close,'Escape')
        
# Set a background color

run = True
    
# =============== Call your first drawing function here or draw your first artpiece here ===============

#panel.onkey(panel.clear,'n')  # the screen will clear when the assigned letter is pressed(here I put n)
panel.onkey(drawImg,'1') # will animate

# =============== Call your next function here or draw your next piece here =================

listen() # turn on listeners

done() # this should be the last line of code! You can stop your code running by clicking the red x in the window.
    


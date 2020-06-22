#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:37:35 2020

@author: Dr. Z
Select a turtle - this code allows users to click and drag on a turtle
"""


import random
from turtle import * #import the library of commands that you'd like to use
colormode(255)

#Create a panel to draw on. 
setup()
panel = Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#========================MAKE VARIABLES=======================
panel.bgcolor('blue')

#Create a bunch of 5 randomly moving items (bubbles), using turtles
numBubbles = 2
turtList = [] # create an empty list
        
def moveBubbles(tList, stride=2):
    '''Animates bubble movement when called inside the game loop.
    tList - the list of turtles to move
    stride - the number of pixels to take per frame. higher numbers are faster'''
    for i in range(len(tList)):
        t = turtList[i] # pull out the turtle...
        t.forward(stride)

def isCollision(turt,target,buffer=30):
    '''Detects collision with an object or list of objects.
    turt is the main object 
    target is the collision target (can be turtle or list of turtles)
    buffer is area surrounding turt center that counts as a collision. Default value is 30 pixels.
    Returns true or false statement if the two items have collided'''
    target = target[:]
    x = turt.xcor()
    y = turt.ycor()
    if type(target)==list:
        # If it's a list, step through each value and check
        if turt in target: #is the turtle we're colliding in the list?
            idx = target.index(turt) # find out where it is
            target.pop(idx) # remove it (just for the function)
        for i in range(len(target)):
            targX = target[i].xcor()
            targY = target[i].ycor()
            if round(targX)-buffer<=round(x)<=round(targX)+buffer and round(targY)-buffer<=round(y)<=round(targY)+buffer:
                return True
            else:
                return False
    elif type(target)== Turtle:
        # If it's a turtle, get its position and checks for collision
        targX = target[i].xcor()
        targY = target[i].ycor()
        if round(targX)-buffer<=round(x)<=round(targX)+buffer and round(targY)-buffer<=round(y)<=round(targY)+buffer:
            return True
        else:
            return False

# Create list of turtles to act as bubble items

tracer(0) #turn off animation

for i in range(numBubbles):
    turt = Turtle(shape='circle') #set our bubble shape
    turt.color('black','cyan') #set the color
    turt.up() #pick up the pen
    turt.shapesize(5) # make it a random size
    turtList.append(turt) # add it to a list. 

# set two turtles to face toward each other.

turtList[0].goto(100,300)
turtList[0].seth(0)
turtList[1].goto(400,300)
turtList[1].seth(180)
#=====================INITIAL CONDITIONS=======================
    
stride = 3 # speed bubbles move in
fps = 30 # frames per second
selected = 0    
T = 0
run = True

#=====================GAME LOOP=======================

while run:
    
    # step through all the bubbles and move them a bit
    moveBubbles(turtList)
    
    for k in range(len(turtList)):
        if isCollision(turtList[k],turtList):
            print('bonk!')
            turtList[k].seth(turtList[k].heading()+180) # one bubble goes in the opposite direction if it bounces with others
        
    # stop if the first bubble goes off screen
    if turtList[0].xcor()<0 or turtList[0].xcor()>w:
        run = False
        
    delay(fps) #set frame rate
    update() # update the image with each "frame"

panel.mainloop()
        
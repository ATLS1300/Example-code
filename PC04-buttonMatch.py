#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:14:23 2020

@author: Dr. Z

simpleaudio play sound example
"""
import simpleaudio as sa
import random
from turtle import *

# Global variables 

filename = 'tech.wav' # CHANGE THIS TO YOUR FILE NAME. 
# Make sure your sound file is in the same folder as your script (.py file)


class Button: # create a class for my button
    def __init__(self, size,x,y,lineColor='black',fillColor='magenta',filename=None): # I don't know my parameters yet, so I'll leave this empty for now
        # define attributes, these will be the variables from my button script
        if filename: # only load the sound if filename has a value
            self.sound = sa.WaveObject.from_wave_file(filename) #this will change based on your sound component
        self.size = size
        self.x = x
        self.y = y
        self.lineColor = lineColor
        self.fillColor = fillColor
        self.startColor = fillColor

        # Now let's make the turtle object
        self.imgBtn = Turtle(shape='square') 
        
        self.makeBtnImg() # you can call a method inside the init funciton, and 
        # it will automatically run that method when you instantiate your object
        self.imgBtn.onclick(self.changeColor)  # starts onclick detection when object is made.

        
# When I made my button, I set up all the features. This should make a nice method.
    def makeBtnImg(self): # again, I don't know what my parameters will be...
        self.imgBtn.shapesize(self.size)
        self.imgBtn.pensize(10)
        self.imgBtn.color(self.lineColor,self.fillColor) # values in the class
        self.imgBtn.up()
        self.imgBtn.goto(self.x,self.y) #values in the class
        self.imgBtn.down()
        self.imgBtn.stamp() # make the box    

    def checkMatch(self,selected,colors):
        if selected in colors:
            idx = colors.index(selected) # give the index where the selected button is in the list
            self.imgBtn.clear() #erase the stamped box
            self.imgBtn.ht() # if using turtles instead of stamps, use ht()

    def changeColor(self, x, y):
        selected = self.fillColor # get color (or image!) before doing anything
        if self.fillColor == self.startColor:
            self.fillColor = 'yellow'
        elif self.fillColor=='yellow':
            self.fillColor = self.startColor
        self.imgBtn.color('white',self.fillColor)
        self.checkMatch(selected,colors)



# Treat this area like the rest of your script...

# Create a panel to draw on.     
panel = Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
panel.setworldcoordinates(0, w, h, 0)    

run = True
selected = None # None acts as a placeholder for a value. we'll put the color here and check to see if it's in our colors list.

# create the button object...
colors = ['red','yellow','orange']
random.shuffle(colors) # randomize the order of colors

# Make a 3x1 grid of buttons
playerList = []
for i in range(3):
    playerList.append(Button(3, (i*75)+50,200, lineColor='black',fillColor=colors[i]))
    # make list of buttons spaced every 75 pixels and with randomized fill colors.

colors[0]='blue'

# add your while loop here
panel.mainloop()

# this shoudl happen outside your while loop
done()











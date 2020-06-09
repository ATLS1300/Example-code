#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Turtle starter code
ATLS 1300
Author: Dr. Z
May 29, 2020
'''
import random
import math
from turtle import * #import the library of commands that you'd like to use
colormode(255)

#Create a panel to draw on. 
panel = Screen()
panel.clear()
w = 720 # width of panel
h = 720 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

greens = [(70,78,71),(86,130,89),(150,230,179),(204,252,203),(241,255,250)]
#dark to light

panel.bgcolor('black')

squiggle=Turtle()
colormode(255)
squiggle.color(random.choice(greens))
squiggle.shape('circle') #'triangle, classic

squiggle.ht()
squiggle.pensize(3)

startx = random.randint(300,400)
starty = random.randint(300,400)
head = random.randint(0,230)

tracer(0,0)

#circPtsx = math.sin(list(range(0,360)))
#circPtsy = math.cos(list(range(0,360)))

for k in range(300):
    squiggle.up()
    squiggle.goto(startx-math.sin(head),starty-math.cos(head))
    
    head = random.randint(0,230)
    squiggle.setheading(head)
    
    step = 0
    color = 0
    
    squiggle.color(random.choice(greens))

    for i in range(100):
    #while 0<squiggle.position()[0]<w and 0<squiggle.position()[1]<h:
        squiggle.down()
        step +=1
        squiggle.forward(15)
        squiggle.stamp()
        head += random.randint(-15,15)
        squiggle.setheading(head)
#        if step % 2:
#            color +=1
#            if color >= len(greens):
#                color = 0
        
update()  

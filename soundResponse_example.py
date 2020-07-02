#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:18:09 2020

@author: master
"""

import soundResponse as SR
import turtle

panel = turtle.Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
panel.setworldcoordinates(0, w, h, 0)    
turtle.tracer(0)


circ = turtle.Turtle(shape='circle')
circ.up()
circ.goto(300,300)

music = SR.Ctrlr('tech.wav') # create object
run = True

def stop():
    '''callback function that stops animation while it's running'''
    global run
    run = False

def go():
    '''Callback function that plays sound and does entire animation'''
    global run
    music.start() # start song
    
    while run:
        amp = music.getCurrAmp()[0]/1000 #work only with the first value returned, the amplitude
        circ.shapesize(amp) 
    #    print(amp)
    
        if amp > 3:
            circ.color('lightblue','lightblue') #turn light color if really loud.
        else:
            circ.color('black','black')
    
        turtle.update()
        
        # quit the while loop when the song ends
        if amp ==-1:
            run = False
        panel.onkey(stop,'s')

panel.onkey(go,'s')
turtle.listen()
        
turtle.done()

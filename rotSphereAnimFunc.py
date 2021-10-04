#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 07:40:49 2021

@author: sazamore
"""
import turtle, math, time

turtle.colormode(255)
turtle.tracer(0) # turn off animation

'''
Parametric equations for a sphere
Formulas from https://www2.math.uconn.edu/~stein/math210/Slides/math210-09notes.pdf

x= ρsin φcos θ
y= ρsin φsin θ
z= ρcos φ

We'll rotate the sphere about y using a rotation matrix:
    R_y(theta) = [[cosθ  0  sinθ],
                  [0     1   0 ],
                  [-sinθ 0  cosθ]]
'''

rho = 250 # radius
density = 20 # number of points per dimension
# panel = turtle.Screen()

sphereDot = turtle.Turtle(visible=False)
sphereDot.up()
sphereDot.color("magenta")

panel = turtle.getscreen()
panel.bgcolor((61, 64, 91))

def rotateY(rot,x,y,z):
    '''rotates about y. 
    rot = rotation angle (radians)'''

    X = math.cos(rot)*x + 0*y + math.sin(rot)*z
    # y = 0*x + 1*y + 0*z
    Z = math.sin(rot)*x + 0*y + math.cos(rot)*z
    return X,y,Z

def getXY(theta):
    '''calculates flat plane positiona'''
    theta = math.radians(theta)
    x = rho * math.sin(psi) * math.cos(theta)
    y = rho * math.sin(psi) * math.sin(theta)
    return x,y

def checkTheta(theta):
    '''Determines color and size to generateperspective 
    drawing. Call before converting angles to radians'''
    global color, size
    if (0<=theta<80) or (-80<theta<0):
        size = int(psi*2)
        color = "darkmagenta"
    elif 80<=theta<150 or -80<=theta<-150:
        size = int(psi)
        color = "magenta"#2"
    else:
        size = int(psi/3)
        color = "magenta"

def draw(theta,rot,color):
    '''draws sphere based on rotation angle (rot) and drawing angle (theta)
    both radians'''
    x,y = getXY(theta)
    x,y,Z = rotateY(rot,x,y,z)
    
    sphereDot.goto(Z,y)
    # sphereDot.color(color)
    sphereDot.dot(size)

for turt in panel.turtles():
    turt.ht()

for rot in range(10,180):
    rot = math.radians(rot)
    sphereDot.clear()


    for psi in range(0,360,density):
        # vertical for loop
        
        #uncomment to slice
        # sphereDot.clear()
        psi = math.radians(psi) # convert to radians
        z = rho * math.cos(psi)

        
        for theta in range(-90,90, int(density/2)):
            # horizontal plane for loop
            
            checkTheta(theta)
            draw(theta,rot,color)
            checkTheta(-theta)
            draw(-theta,rot,color)
            # turtle.update()
    # time.sleep(.1)
    turtle.delay(1000)
    turtle.update()


turtle.update()
        
        
turtle.bye()

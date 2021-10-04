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

sphereDot = turtle.Turtle(shape="circle", visible=False)
sphereDot.up()
sphereDot.color("magenta")

panel = turtle.getscreen()
panel.bgcolor((61, 64, 91))

for turt in panel.turtles():
    if id(turt) != id(sphereDot):
        turt.ht()

# for rot in range(0,180,10):
for rot in range(0,180,20):
    rot = math.radians(rot)
    sphereDot.clear()


    for psi in range(0,360,density):
        # vertical for loop
        psi = math.radians(psi) # convert to radians
        z = rho * math.cos(psi)
        # if z < 0:
        #     z *= -1
        
        for theta in range(0,360, int(density/2)):
    
        # horizontal plane for loop
            
            # perspective drawing before converting to radians
            if (theta<=60) or (theta>300):
                size = 3
                color = "darkmagenta"
            elif 60<theta<=120 or 210<theta<=300:
                size = 7
                color = "magenta2"
            else:
                size = 10
                color = "magenta"
            
            # calculate flat plane position
            theta = math.radians(theta)
            x = rho * math.sin(psi) * math.cos(theta)
            y = rho * math.sin(psi) * math.sin(theta)
            
            # rotate about y
            X = math.cos(rot)*x + 0*y + math.sin(rot)*z
            # y = 0*x + 1*y + 0*z
            Z = math.sin(rot)*x + 0*y + math.cos(rot)*z
            
            sphereDot.goto(Z,y)
            # sphereDot.color(color)
            sphereDot.dot(size)
            # if (theta<=60) or (theta>300):
            #     sphereDot.dot(1)
            # elif 60<theta<=120 or 210<theta<=300:
            #     sphereDot.dot(3)
            # else:
            #     sphereDot.dot(5)

    time.sleep(.3)
    turtle.update()


turtle.update()
        
        
turtle.bye()

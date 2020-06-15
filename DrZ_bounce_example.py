'''
Bounce Example
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
June 11, 2020

Animated spider bounces around the screen, leaving a spiderweb in its wake. The short lengths
of the web are a different color than the long.
'''
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

spider = Turtle()
colormode(255) # 0-255 RGB
spider.up()
spider.speed(10)

# VariableS!
blues = [(76,175,206),(180,227,231),(219,249,244)]
thickLine = False # determines if a thick line is drawn or not
run = True
count = 0 #initializing counter at 0
travel = 0 # initializing counter travel
step = 10 # size of movement increment per "frame"
thresh = 400 # distance threshold for "long" vs "short"


bkgnd = 'grass_bkgnd.gif'
spidey = 'spidey.gif'

panel.addshape(bkgnd)
panel.addshape(spidey)

# NOTE: using panel.bgpic() will place the picture at the original (0,0) and
# there's no easy way to fix it. Instead, we'll change the Turtle into a
# background, and stamp it in the middle of our screen, then change it to the 
# spider shape

# Make background
spider.shape(bkgnd)
spider.goto(w/2,h/2)  #spider.home()
spider.stamp()

# Change spider avatar to spidey!
spider.shape('classic') #neet to change to classic first!
spider.shape(spidey)

#Initializations!
spider.goto(random.randint(100,500),random.randint(100,500))
spider.seth(random.randint(0,360))

while run:
    spider.forward(step)
    x = spider.xcor() # spider.position()
    y = spider.ycor() 
    heading = spider.heading()
    travel += step
    
    if x < 0: # left side boundary
        spider.down()
        AOI = 0 - 2*heading
        spider.seth(AOI)
        spider.goto(0,y)
        count +=1
        if travel >= thresh:
            thickLine = False
        else:
            thickLine = True
        travel = 0

    elif x > w: # right side boundary
        spider.down()
        AOI = 180 - 2*heading
        spider.seth(AOI)
        spider.goto(w,y)
        count +=1
        if travel >= thresh:
            thickLine = False
        else:
            thickLine = True
        travel = 0

    elif y < 0: # top side boundary
        spider.down()
        AOI = 270 - 2*heading
        spider.goto(x,0)
        spider.seth(AOI)
        count +=1
        if travel >= thresh:
            thickLine = False
        else:
            thickLine = True
        travel = 0

    elif y > h: # bottom side boundary
        spider.down()
        AOI = 90 - 2*heading
        spider.goto(x,h)
        spider.seth(AOI)
        count +=1
        if travel >= thresh:
            thickLine = False
        else:
            thickLine = True
        travel = 0

    else:
        continue #ignore this condition
        
    # Determine stroke features
    if thickLine:
        spider.color(random.choice(blues))
        spider.pensize(3)
    else:
        spider.color('white')
        spider.pensize(1)
    
    # Terminating condition
    if count >= 25:
        run = False
        
# when finished, draw 3 concentric circles
spider.up()
spider.goto(w/2,h/2) # spider.home()

# draw concentric circles
# modified from https://stackoverflow.com/questions/24636271/python-turtle-draw-concentric-circles-using-circle-method
for rad in range(10,300,100):
    spider.color('white')
    spider.right(90)
    spider.forward(rad)
    spider.right(270)
    spider.down()
    spider.circle(rad)
    spider.up()
    spider.goto(w/2,h/2)
        
        
    
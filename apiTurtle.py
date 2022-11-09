import turtle, requests
turtle.tracer(0)
turtle.colormode(255)

#set up our screen (global variables)
turtle.setup()
w = 400
h = 400
panel = turtle.Screen()
panel.bgcolor('black')

#import data GLOBAL variable with website!!
URL = 'https://api.weather.gov/gridpoints/BOU/53,74/forecast'

#create classes
#use API data (temperature) to control sizes of different circles
class tempCirc:
  def __init__(self,panel,temp=3,location=[-200,-250],color=(255,0,0)): #special method that runs when we instantiate our object
    self.data=[] #our data will automatically get stored here when we run self.updatData in the next line
    self.numCirc=6 #number of circles to draw
    self.radius,self.forecast= self.updateData() #store the temp data to self.radius
    self.location= location
    self.color= color
    
    #create objects/inital conditions/local variables

  def updateData(self, URL=URL):
    '''Pulls data from URL (API only) and parses it into a data dictionary.
    You should update this function to parse your own code!'''
    #Pull data from the URL
    self.data = requests.get(URL).json() #pull data from your URL
    
    #create data variable with values you want to work with. You may want to make more than one.. 
    #Here we'll just use temp
    temp=[]
    for i in range(self.numCirc):
      temp.append(self.data['properties']['periods'][i]['temperature']) #list of temp
    
    #example second data (not used)
    forecast=[]
    for i in range(self.numCirc):
      forecast.append(self.data['properties']['periods'][i]['shortForecast']) #list of short forecast descriptions
    return temp, forecast

  def labelData(self,idx,loc,xoffset=0, yoffset=0, fontsize = 40,fontcolor=(255,255,255),background=(0,0,0)):
      '''Adds text to describe data. Gets called when circles are drawn, but can be called whenever! Add the label variable as a parameter to be able to use whatever text you want, not just data-related text.'''

      font = ('arial', fontsize) 
      
      label=self.data['properties']['periods'][idx]['name'] #CHANGE THIS to your datase label, if any
      
      #Add text from: https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
      # text = font.render(label, True, fontcolor) 
      text = turtle.Turtle(visible=False)
      text.up()
      text.color('white')
      
      # set the center of the shape. 
      text.goto(loc[0]+xoffset // 2, loc[1]+yoffset // 2) 
    
      # copying the text surface object 
      # to the display surface object  
      # at the center coordinate. 
      text.write(str(label),align = 'left',font=font)
      panel.update()

  def drawCirc(self,label=True):
    '''Draws circles with radii based on the NWS temperature data. This method should be changed to whatever illustration you want.'''
    t = turtle.Turtle(shape='circle')
    t.up()
    
    for i in range(self.numCirc):
        loc = (self.location[0], int(self.location[1] + i*100)) #space circles by 10
        t.color(self.color)
        t.goto(loc)
        t.shapesize(self.radius[i]/10)
        
        red = self.radius[i]*2
        
        if red >255:
            red==255

        t.stamp()
        #add labels
        if label:
          self.labelData(i,loc,xoffset=400,yoffset=0) #offsets control locations...
        screen.update()
        

#create object
bubble = tempCirc(screen) #our object only has one required 

bubble.drawCirc()
    


"""
Created on Fri Apr 24 11:41:45 2020

@author: Dr. Z
Modified from:
    
    measuring elapsed time: https://stackoverflow.com/questions/45520104/counting-time-in-pygame
    frequency calc: https://stackoverflow.com/questions/2648151/python-frequency-detection
    
This uses pydub to get sample data from your track, but uses pygame to PLAY your track.
You will need both to have the timeing calculated.
Timing pulls from samples based off of when the sound plays.
To work with multiple sounds, you'll have to create multiple soundCtrlr objects
You can have one soundCtrlr object manipulate multiple animations this way.

The sound file associated with this script (tech.wav) has a commons license.

***Using this class will NOT COUNT toward your final number of classes when scoring your final code.

"""
import pygame
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import pdb
pygame.init()
pygame.mixer.init()

fps = 60 #graphics rate
color = pygame.Color('forestgreen')

CW = list(np.linspace(0,6*np.pi, 500)) # angles to calculate CW rotation
CCW = list(np.linspace(6*np.pi,0, 500)) # angles to calculate CCW rotation

# From Dr. Z's soundSync script
class soundCtrlr:
    def __init__(self,filename='tech.wav',fps=60, channel=0):
        self.sound = AudioSegment.from_file(filename) #replace string with YOUR filename with extension (works with wav and mp3)
        self.pySound = pygame.mixer.Sound(filename) #for playing sounds
        self.fps = fps # needed for frequency calculation. update if using a different animation speed (like 30 fps)
        self.samples = self.sound.get_array_of_samples() #puts the sound file into a numpy array, for manipulation
        self.bitrate = 1/(self.sound.duration_seconds/len(self.samples)) # samplerate (bitrate) of pydub sound, in Hz
        self.channel=channel
        self.start()
        
    def start(self):
        '''Plays corresponding sound. To play multiple sounds from multiple objects,
        change the channel index. The default number of pygame sound channels is 16.
        You can continually play 16 sounds at once.'''
        
        pygame.mixer.Channel(self.channel).play(self.pySound)
        self.start_time = pygame.time.get_ticks() # gets the time when the sound starts playing.
   
    def getCurrAmp(self):
        '''Gets the amount of time that has passed since the song started playing
        amount of time that has lapsed from start of play, in s. Then calculates 
        the sample index from which to grab data. Returns the amplitude of the sound
        at the current time, and the index of the samples list'''
        
        self.timenow = (pygame.time.get_ticks() - self.start_time)/1000 # time elapsed sing song started, in s
        idx = int(self.timenow * self.bitrate) 
        if idx>len(self.samples):
            idx = -1
        amp = int(np.abs(self.samples[idx])) # get data from sample at the given time (idx), returns amplitude (which is all the sound data is)
        return amp, idx
    
    def getCurrFreq(self,idx=None):
        '''Calculates the dominant frequency at a given time point. This is an approximation,
        as frequency will always require more than one samples for the calculation. 
        The math here is pretty complicated, but you just need to know that it will output 
        the two most prominent ("loudest") frequencies over a frame of animation (single iteration of while loop).'''
        self.timenow = (pygame.time.get_ticks() - self.start_time) /1000 # time elapsed sing song started, in s
        if not idx:
            idx = int(self.timenow * self.bitrate)
        self.winSize = int(30./self.fps*1000) # how many samples we'll use to calculate the frequency, based on ratio of bitrate to fps
        #idx must be multiple of two
        if not idx//2: # if two doesn't divide evenly into a number, add 1 to it.
            idx += 1
        
        if self.winSize < idx < len(self.samples)-self.winSize:
            # uses a blackman window to get chunk of time, we'll use a bit before the current time, and a bit after
            indata = self.samples[idx-self.winSize:idx+self.winSize] * np.blackman(2*self.winSize) # creates a tapered window to calculate frequency, size of self.winSize
        elif idx >= self.winSize:
            indata = self.samples[0:idx+(2*self.winSize)-1] * np.blackman(2*self.winSize)
        else:
            idx = -1 # when the song ends, continue to calculate the final frequency
            indata = self.samples[-self.winSize-1:idx] * np.blackman(self.winSize)
            
        fftData = abs(np.fft.rfft(indata))**2 # take the Fourier transform of the data (real numbers only) and square it
        maxFreq = fftData[1:].argmax() # the index where the largest value is found. This is a proxy for frequency
        # use quadratic interpolation around the max (smooth the values)
        if 0 < maxFreq != len(fftData)-1:
            y0,y1,y2 = np.log(fftData[maxFreq-1:maxFreq+2:]) # get log power values around the max frequency location
            x1 = np.abs((y2 - y0) * .5 / (2 * y1 - y2 - y0))
            # find the frequency and output it
            return (maxFreq+x1)*self.bitrate/self.winSize, idx # convert to frequency based on song bitrate
#        elif maxFreq == 0:
#            y0,y1,y2 = np.log(fftData[maxFreq:maxFreq+3:])
#            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
#            if x1<0:
#                pdb.set_trace()
#            # find the frequency and output it
#            return (maxFreq+x1)*self.bitrate/self.winSize, idx
        else:
            return maxFreq*self.bitrate/self.winSize, idx

def circPath(x0,y0,r,theta):    
    '''Create the circular path for my shape, and call the shape drawing function.
    You can use this same function for multiple animations!'''  
    x = r * np.cos(theta) + x0  
    y = r * np.sin(theta) + y0  
    return int(x),int(y)

# Set the width and height of the screen [width, height]
size = (600, 600)
screen = pygame.display.set_mode(size)
fillColor = pygame.Color('darkslateblue')

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
done = True
i = 0 # index counter for CW and CCW 

freqRect=pygame.Rect(50,300,500,200) # Rect for arc (frequency animation)


# make the object (plays sound when intantiated)
techno = soundCtrlr()
# -------- Main Program Loop -----------
while done:
    
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            pygame.mixer.pause() # stop song play

    # Fill in the background
    screen.fill(fillColor)
    
    # Get amplitude data from soundCtrlr object
    amp,idx = techno.getCurrAmp() 
    freq,idx = techno.getCurrFreq()
    # When the sound has finished playing, these functions will return idx = -1 and a fixed amp value

    if idx == -1:
        #when the song stops playing, idx = -1
        amp=5000
    
    # Stop animations with song length (DURATION EXAMPLE)
    if idx<0:
#        amp = int(np.abs(techno.samples[idx]))
        fillColor = pygame.Color('grey24')
        
    # --- Replace with your drawing code 
    
    # Draw a rectangle with a height varies with the frequency
    freqRect.h = int(freq/2)
    freqRect.centery = 300
    if freq<200:
        # bass tones make the width wider
        pygame.draw.rect(screen, pygame.Color('hotpink3'), freqRect,6)

    else:
        # everything else is represented with circles
        pygame.draw.circle(screen, pygame.Color('thistle4'), freqRect.center,int(freq/2),2)
#        pygame.draw.circle(screen, pygame.Color('darkorchid'), freqRect.center,int(freq/2.9),1)
    
    # Outer circles go clockwise in a small circle
    # AMPLITUDE (loudness) used to adjust radii of circles
    x,y=circPath(100,300,15,CW[i])
    pygame.draw.circle(screen,color,(x,y),int(amp/300)) # tiny
    
    #inner circles go ccw in a medium circle    
    x,y=circPath(200,300,25,CCW[i])
    pygame.draw.circle(screen,color,(x,y),int(amp/500)) # medium
    
    pygame.draw.circle(screen,color,(300,300),int(amp/1000)) # small/still
    
    x,y=circPath(400,300,25,CCW[i]) # circle is basically at 400,400
    pygame.draw.circle(screen,color,(x,y),int(amp/500)) # medium
    
    x,y=circPath(500,300,15,CW[i])    
    pygame.draw.circle(screen,color,(x,y),int(amp/300)) # tiny

    i+=1
    #reset i for continuous movement
    if i >= len(CW):
        i = 0

    #change color of the circle with AMPLITUDE (loudness)
    if amp < 7000:
        color  = pygame.Color('turquoise4')
    else:
        color = pygame.Color('lightsteelblue1')
        
    # --- End drawing code


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip() #similar to pygame.display.update()
 
    # --- Limit animation to 60 frames per second
    clock.tick(fps)

# Close the window and quit.
pygame.mixer.pause() # stop song play
pygame.quit()

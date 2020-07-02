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
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as Play
import time, os
import numpy as np

fps = 60 #graphics rate

class Ctrlr:
    def __init__(self,filename='tech.wav',fps=60,startOnInst=False):
        self.sound = AudioSegment.from_file(filename) #replace string with YOUR filename with extension (works with wav and mp3)
        self.fps = fps # needed for frequency calculation. update if using a different animation speed (like 30 fps)
        self.samples = self.sound.get_array_of_samples() #puts the sound file into a numpy array, for manipulation
        self.bitrate = 1/(self.sound.duration_seconds/len(self.samples)) # samplerate (bitrate) of pydub sound, in Hz
        if startOnInst:
            self.start()
        
    def start(self):
        '''Plays corresponding sound. To play multiple sounds from multiple objects,
        change the channel index. The default number of pygame sound channels is 16.
        You can continually play 16 sounds at once.'''
        
        Play(self.sound)
        self.start_time = time.time() # gets the time when the sound starts playing.
   
    def getCurrAmp(self):
        '''Gets the amount of time that has passed since the song started playing
        amount of time that has lapsed from start of play, in s. Then calculates 
        the sample index from which to grab data. Returns the amplitude of the sound
        at the current time, and the index of the samples list'''
        
        self.timenow = time.time() - self.start_time # time elapsed sing song started, in s
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
#        self.timenow = (pygame.time.get_ticks() - self.start_time) /1000 # time elapsed sing song started, in s
        self.timenow = time.time() - self.start_time # time elapsed sing song started, in s

        if not idx:
            idx = int(self.timenow * self.bitrate)
        self.winSize = int(30./self.fps*1000) # how many samples we'll use to calculate the frequency, based on ratio of bitrate to fps
        #idx must be multiple of two
        if not idx//2: # if two doesn't divide evenly into a number, add 1 to it.
            idx += 1
        
        if self.winSize < idx < len(self.samples)-self.winSize:
            # uses a blackman window to get chunk of time, we'll use a bit before the current time, and a bit after
            indata = self.samples[idx-self.winSize:idx+self.winSize] * np.blackman(2*self.winSize) # creates a tapered window to calculate frequency, size of self.winSize
        elif idx >= len(self.samples)-2*self.winSize:
            indata = self.samples[-(2*self.winSize):] * np.blackman(2*self.winSize)
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

        else:
            return maxFreq*self.bitrate/self.winSize, idx
        
        def cleanUp(self):
            pass
        def pause(self):
            pass



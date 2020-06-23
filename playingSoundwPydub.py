#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:26:36 2020

@author: Dr. Z
Demonstrates how to import, manipulate and play sounds using pydub and simple audio

#####INSTALLS#####
First, in your command line, type:
    pip install pydub
Then type:
    pip install simpleaudio
"""

from pydub.playback import _play_with_simpleaudio as Play
from pydub import AudioSegment


filename = 'tech.wav'
techSong = AudioSegment.from_wav(filename) #make sure command matches file type

#Play(techSong)

# no stop/pause option


# You can break up the song and play it by section
# pydub does things in milliseconds
ten_seconds = 10 * 1000

first_10_seconds = techSong[:ten_seconds]

last_5_seconds = techSong[-5000:]

#Play(last_5_seconds)


# You can change the amplitude (volume) of it, too

# Make the beginning louder and the end quieter

# boost volume by 6dB
beginning = first_10_seconds + 6

# reduce volume by 3dB
end = last_5_seconds - 3

Play(first_10_seconds)
#Play(beginning)


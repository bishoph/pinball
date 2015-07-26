#!/usr/bin/python
# (c) 2015 Martin Kauss, yo@bishoph.org

# This code is for my custom pinball machine/flipper.
# You find more information about the project/hardware
# at http://bishoph.org

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# HINT: If using HDMI for sound but with a non different HDMI
# resolution then just configure 
# hdmi_drive=2 
# in the file 
# /boot/config.txt 
# and reboot to make the sound work

import pygame
import effects

class control:

    counter=0

    def __init__(self, init_sounds):
     pygame.init()
     pygame.mixer.init()
     self.counter=0
     self.playsound(init_sounds)

    def playsound(self, files):
     if (len(files) >= 0):
      pygame.mixer.music.load(files[0])
      for a in range (1, len(files)):
       pygame.mixer.music.queue(files[a])
     pygame.mixer.music.play()

    def checksilence(self):
     if (pygame.mixer.music.get_busy() == False):
      if (self.counter >= 2000):
       self.playsound(effects.getrandomsoundeffect())
       self.counter=0
      else:
       self.counter=self.counter+1

    # this is to play sound effects on top of the background music
    def playeffect(self, effect):
     print (effect[0])
     e = pygame.mixer.Sound(effect[0])
     pygame.mixer.Sound.play(e)

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
import time

class control:

    def __init__(self, init_sounds):
     pygame.init()
     pygame.mixer.init()
     self.playsound(init_sounds)

    def playsound(self, files):
     if (len(files) >= 0):
      pygame.mixer.music.load(files[0])
      for a in range (1, len(files)):
       pygame.mixer.music.queue(files[a])
     pygame.mixer.music.play()


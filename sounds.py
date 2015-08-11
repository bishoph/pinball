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

import multiprocessing
import pygame
import effects

class control(multiprocessing.Process):

    RUNNING=True
    counter=0

    def __init__(self, queue, init_sounds):
     multiprocessing.Process.__init__(self, name="sound control")
     self.queue = queue
     self.counter = 0
     self.init_sounds = init_sounds

    def run(self):
     pygame.init()
     pygame.mixer.init()
     self.playsound(self.init_sounds)
     while self.RUNNING:
      master_process_input = self.queue.get()
      if (master_process_input == 'quit' or master_process_input == 'exit' or master_process_input == 'stop'):
       self.stop()
       break
      elif (master_process_input == 'checksilence'):
       self.checksilence()
      else:
       self.playeffect(master_process_input)

    def stop(self):
     self.RUNNING=False
     self.queue.close()

    # this is to background music
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
     print ('>>> '+effect[0])
     e = pygame.mixer.Sound(effect[0])
     print (str(e))
     pygame.mixer.Sound.play(e)

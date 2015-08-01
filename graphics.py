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

import os
import pygame

class control():

    def __init__(self):
     os.putenv('SDL_VIDEODRIVER', 'fbcon')
     pygame.display.init()
     size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
     print "Framebuffer size: %d x %d" % (size[0], size[1])
     self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
     pygame.font.init()

     self.screen.fill((64, 64, 64))
     self.myfont = pygame.font.SysFont("monospace", 24)
     label = self.myfont.render('000000000', 1, (255,255,255))
     self.screen.blit(label, (200,200))
     pygame.display.update()

    def showscore(self, score):
      cur_score = '{0:09d}'.format(score)
      try:
       self.screen.fill((64, 64, 64))
       label = self.myfont.render(cur_score, 1, (255,255,255))
       self.screen.blit(label, (200,200))
       pygame.display.update()
      except Exception, err:
       print ('error : '+str(err))


    

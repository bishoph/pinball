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
import random

class control():

    color_fx = [ (255,100,100), (255,0,0), (255,255,0) ]
    last_fx = ''
    fx_counter = 0

    def __init__(self):
     os.putenv('SDL_VIDEODRIVER', 'fbcon')
     pygame.display.init()
     size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
     print "Framebuffer size: %d x %d" % (size[0], size[1])
     self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
     self.counter=0
     self.score_current_ball_display='{0:09d}'.format(0)
     self.score_display='{0:09d}'.format(0)
     self.high_score_display='{0:09d}'.format(0)
     self.fx_display=''
     self.ball=0
     pygame.font.init()

     self.screen.fill((64, 64, 64))
     print (pygame.font.get_fonts())
     self.scorefont = pygame.font.Font("/usr/local/share/fonts/pinball.ttf", 72)
     self.fxfont = pygame.font.Font("/usr/local/share/fonts/comicfx.ttf", 144)
     self.change_display()
     pygame.display.update()

    def setstate(self, score_current_ball, score, high_score, fx, ball):
      self.counter = self.counter + 1
      if (self.counter > 100):
       self.counter = 0
       self.score_current_ball_display = '{0:09d}'.format(score_current_ball)
       self.score_display = '{0:09d}'.format(score)
       self.high_score_display = '{0:09d}'.format(high_score)
       if (fx != self.last_fx):
        self.fx_display=fx
        self.last_fx=fx
        self. fx_counter = 0
       else:
        self.fx_counter = self.fx_counter + 1
        if (self.fx_counter < 5):
         self.fx_counter = self.fx_counter + 1
        else:
         self.fx_display=''
       self.ball_display='{0:09d}'.format(ball)
       self.change_display()

    def change_display(self):
      try:
       c = random.randint(200, 255)
       self.screen.fill((64, 64, 64))
       score_current_ball_label = self.scorefont.render(self.score_current_ball_display, 1, (c,c,c))
       self.screen.blit(score_current_ball_label, (60,60))

       score_label = self.scorefont.render(self.score_display, 1, (c,c,c))
       self.screen.blit(score_label, (60,160))

       ball_label = self.scorefont.render(self.ball_display, 1, (c,c,c))
       self.screen.blit(ball_label, (60,260))

       high_score_label = self.scorefont.render(self.high_score_display, 1, (255,255,255))
       self.screen.blit(high_score_label, (60,420))

       fxlabel = self.fxfont.render(self.fx_display, 1, random.sample(self.color_fx,1)[0])
       x = random.randint(0, 100)
       y = random.randint(0, 100)
       self.screen.blit(fxlabel, (500+x,100+y))

       pygame.display.update()
      except Exception, err:
       print ('error : '+str(err))


    

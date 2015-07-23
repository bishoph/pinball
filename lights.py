#!/usr/bin/python
# (c) 2015 Martin Kauss, yo@bishoph.org

# This code is for my custom pinball machine/flipper.
# You find more information about the project/hardware
# at http://bishoph.org

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

import time
import effects

class control:

    INTERVAL=0.1
    counter=0
    timer=0
    last=0
    id=0
    state=False
    idle_counter=0
    effect=[]

    def __init__(self, id, default_state, idle_counter):
     self.id = id
     self.default_state = default_state
     self.idle_counter = idle_counter
     self.timer = time.time()
     self.last = 0
     self.counter = 0
     self.state=False
     self.effect=[]

    def getstate(self):
     if (self.last + self.INTERVAL <= self.timer):
      self.last=self.timer
      #print("light "+str(self.id) + " / "+str(self.effect) + " // "+str(self.counter))
      if (self.counter < len(self.effect)):
       self.state=bool(self.effect[self.counter])
      else:
       self.state=self.default_state
       self.effect=[]
      self.counter=self.counter+1
      if (self.counter > self.idle_counter):
       self.last=0
       self.seteffect(effects.getrandomeffect())
      
     self.timer=time.time()
     return self.state

    def seteffect(self, effect):
     self.effect=effect
     self.counter=0

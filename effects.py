#!/usr/bin/python
# (c) 2015 Martin Kauss, yo@bishoph.org

# This code is for my custom pinball machine/flipper.
# You find more information about the project/hardware
# at http://bishoph.org

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

import random

e={
   'shooter_alley_1': [ 0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0 ],
   'shooter_alley_2': [ 1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1 ],
   'slingshot_1': [ 1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1 ],
   'slingshot_2': [ 1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1 ],
  }

e2={
   'blink_1': [ 1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0 ],
   'blink_2': [ 1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0 ]
  }

s={
   'startup': [ 'sounds/alarm_long.mp3', 'sounds/thunder.mp3' ],
   'shooter_alley': [ 'sounds/laser_beam.mp3' ],
   'outlane': [ 'sounds/shutdown.mp3' ]
  }


def geteffect(id):
 if (id in e):
  print('effect : '+id)
  return e[id]
 else:
  return []

def getrandomeffect():
 id=random.sample(e2,1)[0]
 print('effect : '+id)
 return e2[id]

def getsoundeffect(id):
 if (id in s):
  print('sound effect : '+id)
  return s[id]
 else:
  return []

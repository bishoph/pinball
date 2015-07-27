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
   'shooter_1': [ 0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0 ],
   'shooter_2': [ 1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1 ],
   'out_1': [ 0,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0 ],
   'spinner': [ 1,0 ]
  }

e2={
   'blink_1': [ 1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0 ],
   'blink_2': [ 1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0 ],
   'blink_3': [ 1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0 ],
   'blink_4': [ 1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0 ]
  }

s={
   'startup': [ 'sounds/alarm_long.mp3' ],
   'shooter_alley': [ 'sounds/laser_beam.ogg' ],
   'outlane': [ 'sounds/shutdown.ogg' ],
   'spinner' : ['sounds/deskbell.ogg' ]
  }

s2={
   'spooky': [ 'sounds/spooky.mp3' ],
   'choir': [ 'sounds/choir.mp3' ],
   'sorry': [ 'sounds/oh_sorry.mp3' ],
   'try': [ 'sounds/one_must_try.mp3' ],
   'giggle': [ 'sounds/giggle.mp3' ],
   'meh': [ 'sounds/meh.mp3' ],
   'uuuuhhhh': [ 'sounds/uuuuhhhh.mp3' ],
   'piano': [ 'sounds/piano.mp3' ],
   'explosion': [ 'sounds/explosion.mp3' ],
   'witch': [ 'sounds/witch.mp3' ],
   'wee_wee': [ 'sounds/wee_wee.mp3' ],
   'sacrifice': [ 'sounds/sacrifice.mp3' ]
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

def getrandomsoundeffect():
 id=random.sample(s2,1)[0]
 print('sound effect : '+id)
 return s2[id]


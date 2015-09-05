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
   'bumper': [ 1,1,1,1,1,1,1,1,1,0,0,0,0,0 ],
   'spinner': [ 1,0 ],
   'slingshot': [ 1,1,0,0,1,1,0,0,1,1,0,0,1,1 ]
  }

e2={
   'blink_1': [ 1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0 ],
   'blink_2': [ 1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0 ],
   'blink_3': [ 1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0 ],
   'blink_4': [ 1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0 ]
  }

s={
   'startup': [ '/home/pi/pinball/sounds/alarm_long.mp3' ],
   'shooter_alley': [ '/home/pi/pinball/sounds/laser_beam.ogg' ],
   'outlane': [ '/home/pi/pinball/sounds/shutdown.ogg' ],
   'spinner' : [ '/home/pi/pinball/sounds/deskbell.ogg' ], 
   'bumper_1': [ '/home/pi/pinball/sounds/laser_beam2.ogg' ],
   'slingshot': [ '/home/pi/pinball/sounds/spring.ogg' ],
  }

s2={
   'spooky': [ '/home/pi/pinball/sounds/spooky.mp3' ],
   'choir': [ '/home/pi/pinball/sounds/choir.mp3' ],
   'sorry': [ '/home/pi/pinball/sounds/oh_sorry.mp3' ],
   'try': [ '/home/pi/pinball/sounds/one_must_try.mp3' ],
   'giggle': [ '/home/pi/pinball/sounds/giggle.mp3' ],
   'meh': [ '/home/pi/pinball/sounds/meh.mp3' ],
   'uuuuhhhh': [ '/home/pi/pinball/sounds/uuuuhhhh.mp3' ],
   'piano': [ '/home/pi/pinball/sounds/piano.mp3' ],
   'explosion': [ '/home/pi/pinball/sounds/explosion.mp3' ],
   'witch': [ '/home/pi/pinball/sounds/witch.mp3' ],
   'wee_wee': [ '/home/pi/pinball/sounds/wee_wee.mp3' ],
   'sacrifice': [ '/home/pi/pinball/sounds/sacrifice.mp3' ]
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


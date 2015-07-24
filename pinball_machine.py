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
import RPi.GPIO as GPIO
import lights
import effects

# SLEEP/WAIT TIME FOR LOOP
SLEEP=0.005

# flipper high max. timeout
# Value defines the max. time high current flows 
# depending on resistors/diodes and coils you may
# need higher values but beware to not burn the coil
# or other components like Solid State Relays (SSR).
# For my environment with a FL-11630 0.04 seconds
# works pretty well.
FLIPPER_HIGH_MAX=0.04

# INPUT (GPIO Pin)
FLIPPER_FINGER_BUTTON_RIGHT=3
FLIPPER_FINGER_BUTTON_LEFT=5
FLIPPER_FINGER_EOS_RIGHT=8
FLIPPER_FINGER_EOS_LEFT=10

SHOOTER_ALLEY=16
OUTHOLE=37

# OUTPUT (GPIO Pin)
FLIPPER_FINGER_HIGH_RIGHT=11
FLIPPER_FINGER_HOLD_RIGHT=12
FLIPPER_FINGER_HIGH_LEFT=13
FLIPPER_FINGER_HOLD_LEFT=15

LIGHT_1=32
LIGHT_2=33

# MODE (GPIO Pin)
GPIO.setmode(GPIO.BOARD)

# SETTINGS IN
GPIO.setup(FLIPPER_FINGER_BUTTON_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(FLIPPER_FINGER_EOS_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(FLIPPER_FINGER_BUTTON_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(FLIPPER_FINGER_EOS_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(SHOOTER_ALLEY, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(OUTHOLE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# SETTINGS OUT
GPIO.setup(FLIPPER_FINGER_HIGH_RIGHT, GPIO.OUT)
GPIO.setup(FLIPPER_FINGER_HOLD_RIGHT, GPIO.OUT)
GPIO.setup(FLIPPER_FINGER_HIGH_LEFT, GPIO.OUT)
GPIO.setup(FLIPPER_FINGER_HOLD_LEFT, GPIO.OUT)

GPIO.setup(LIGHT_1, GPIO.OUT)
GPIO.setup(LIGHT_2, GPIO.OUT)

# DEFAUTs
GPIO.output(FLIPPER_FINGER_HIGH_RIGHT, False)
GPIO.output(FLIPPER_FINGER_HOLD_RIGHT, False)
GPIO.output(FLIPPER_FINGER_HIGH_LEFT, False)
GPIO.output(FLIPPER_FINGER_HOLD_LEFT, False)

GPIO.output(LIGHT_1, False)
GPIO.output(LIGHT_2, False)

# VARIABLES
FLIPPER_FINGER_HIGH_ACTIVE_RIGHT=False
FLIPPER_FINGER_HOLD_ACTIVE_RIGHT=False
FLIPPER_FINGER_HIGH_COOLDOWN_RIGHT=0

FLIPPER_FINGER_HIGH_ACTIVE_LEFT=False
FLIPPER_FINGER_HOLD_ACTIVE_LEFT=False
FLIPPER_FINGER_HIGH_COOLDOWN_LEFT=0

LIGHT_1_STATUS=False
LIGHT_2_STATUS=False


light_control_1=lights.control(1, False, 90)
light_control_2=lights.control(2, False, 70)

# this is our main loop and loops forever
while True:

 # right flipper finger input (button + eos)
 input_state_3 = GPIO.input(FLIPPER_FINGER_BUTTON_RIGHT)
 input_state_8 = GPIO.input(FLIPPER_FINGER_EOS_RIGHT)
 # left flipper finger input (button + eos)
 input_state_5 = GPIO.input(FLIPPER_FINGER_BUTTON_LEFT)
 input_state_10 = GPIO.input(FLIPPER_FINGER_EOS_LEFT)
 # shooter alley
 input_state_16 = GPIO.input(SHOOTER_ALLEY)
 input_state_37 = GPIO.input(OUTHOLE)

 # LOGIC SECTION
 if (input_state_3 == False and FLIPPER_FINGER_HIGH_ACTIVE_RIGHT == False and FLIPPER_FINGER_HOLD_ACTIVE_RIGHT == False):
  # KICK the right flipper finger hard
  print('Flipper Finger Button right pressed')
  FLIPPER_FINGER_HIGH_ACTIVE_RIGHT=True
  FLIPPER_FINGER_HIGH_COOLDOWN_RIGHT=time.time()+FLIPPER_HIGH_MAX
 if (input_state_3 == True and (FLIPPER_FINGER_HIGH_ACTIVE_RIGHT == True or FLIPPER_FINGER_HOLD_ACTIVE_RIGHT == True)):
  # Release right flipper finger completely
  print('Flipper Finger Button right released')
  FLIPPER_FINGER_HIGH_ACTIVE_RIGHT=False
  FLIPPER_FINGER_HOLD_ACTIVE_RIGHT=False
  FLIPPER_FINGER_HIGH_COOLDOWN_RIGHT=0

 if ((input_state_8 == False and FLIPPER_FINGER_HIGH_COOLDOWN_RIGHT > 0) or (FLIPPER_FINGER_HIGH_ACTIVE_RIGHT == True and FLIPPER_FINGER_HIGH_COOLDOWN_RIGHT <= time.time())):
  # Relase HIGH and change to HOLD / right flipper finger
  print('Flipper Finger right HIGH=0 HOLD=1 (pressed + cooldown)')
  FLIPPER_FINGER_HIGH_ACTIVE_RIGHT=False
  FLIPPER_FINGER_HOLD_ACTIVE_RIGHT=True

 if (input_state_5 == False and FLIPPER_FINGER_HIGH_ACTIVE_LEFT == False and FLIPPER_FINGER_HOLD_ACTIVE_LEFT == False):
  # KICK the left flipper finger hard
  print('Flipper Finger Button left pressed')
  FLIPPER_FINGER_HIGH_ACTIVE_LEFT=True
  FLIPPER_FINGER_HIGH_COOLDOWN_LEFT=time.time()+FLIPPER_HIGH_MAX
 if (input_state_5 == True and (FLIPPER_FINGER_HIGH_ACTIVE_LEFT == True or FLIPPER_FINGER_HOLD_ACTIVE_LEFT == True)):
  # Release left flipper finger completely
  print('Flipper Finger Button left released')
  FLIPPER_FINGER_HIGH_ACTIVE_LEFT=False
  FLIPPER_FINGER_HOLD_ACTIVE_LEFT=False
  FLIPPER_FINGER_HIGH_COOLDOWN_LEFT=0
 if ((input_state_10 == False and FLIPPER_FINGER_HIGH_COOLDOWN_LEFT > 0) or (FLIPPER_FINGER_HIGH_ACTIVE_LEFT == True and FLIPPER_FINGER_HIGH_COOLDOWN_LEFT <= time.time())):
  # Relase HIGH and change to HOLD / left flipper finger
  print('Flipper Finger left HIGH=0 HOLD=1 (pressed + cooldown)')
  FLIPPER_FINGER_HIGH_ACTIVE_LEFT=False
  FLIPPER_FINGER_HOLD_ACTIVE_LEFT=True

 # switches and effects
 if (input_state_16 == False):
  print('shooter alley')
  light_control_1.seteffect(effects.geteffect('shooter_alley_1'))
  light_control_2.seteffect(effects.geteffect('slingshot_1'))
 if (input_state_37 == False):
  print('ball out')
  light_control_1.seteffect(effects.geteffect('shooter_alley_2'))
  light_control_2.seteffect(effects.geteffect('slingshot_2'))

 # lights and magic
 LIGHT_1_STATUS=light_control_1.getstate()
 LIGHT_2_STATUS=light_control_2.getstate()

 # ##################################
 # stuff gets real below this comment
 # ################################## 

 # right flipper finger
 if (FLIPPER_FINGER_HIGH_ACTIVE_RIGHT == True):
  GPIO.output(FLIPPER_FINGER_HIGH_RIGHT, True)
 else:
  GPIO.output(FLIPPER_FINGER_HIGH_RIGHT, False)
  
 if (FLIPPER_FINGER_HOLD_ACTIVE_RIGHT == True):
  GPIO.output(FLIPPER_FINGER_HOLD_RIGHT, True)
 else:
  GPIO.output(FLIPPER_FINGER_HOLD_RIGHT, False)

 # left flipper finger
 if (FLIPPER_FINGER_HIGH_ACTIVE_LEFT == True):
  GPIO.output(FLIPPER_FINGER_HIGH_LEFT, True)
 else:
  GPIO.output(FLIPPER_FINGER_HIGH_LEFT, False)

 if (FLIPPER_FINGER_HOLD_ACTIVE_LEFT == True):
  GPIO.output(FLIPPER_FINGER_HOLD_LEFT, True)
 else:
  GPIO.output(FLIPPER_FINGER_HOLD_LEFT, False)

 # light 1
 if (LIGHT_1_STATUS == True):
  GPIO.output(LIGHT_1, True)
 else:
  GPIO.output(LIGHT_1, False)

 # light 2
 if (LIGHT_2_STATUS == True):
  GPIO.output(LIGHT_2, True)
 else:
  GPIO.output(LIGHT_2, False)

 time.sleep(SLEEP)

GPIO.cleanup()
 


#!/usr/bin/env python
#this code is for using piezo sensor with python and intel edison 
#ardiono breakout board

import mraa
import time

# attaching piezo positive end to pin 10

sd=10
pz=mraa.Gpio(sd)
pz.dir(mraa.DIR_OUT)

pz.write(0)

while True:
    pz.write(1)
    time.sleep(1e-15)
    pz.write(0)
    time.sleep(1e-15)

#!/usr/bin/env python
import mraa
import time



outpin_left=mraa.Gpio(3)
inpin_left=mraa.Gpio(2)
outpin_right=mraa.Gpio(5)
inpin_right=mraa.Gpio(4)


outpin_right.dir(mraa.DIR_OUT)
inpin_right.dir(mraa.DIR_IN)
outpin_left.dir(mraa.DIR_OUT)
inpin_left.dir(mraa.DIR_IN)


def delayMicroseconds(delay=0):
    microsecond=delay/1e6
    time.sleep(microsecond)

def pulseIn(GPIOpin):

    while not GPIOpin.read():
        continue
    start=time.time()

    while GPIOpin.read():
        continue
    end=time.time()

    return (end-start)*1e6

def read_val(pin1, pin2):
    pin1.write(0)
    delayMicroseconds(2)
    pin1.write(1)
    delayMicroseconds(10)
    pin1.write(0)

    duration=pulseIn(pin2)
    distance=duration/58.2
    return distance


while True:
   distance_right=read_val(outpin_right,inpin_right)
   distance_left=read_val(outpin_left,inpin_left)
#  dist_l=pulseIn(inpin_left)
#  distance_left=dist_l/58.2
   print distance_right
   print distance_left
   print "----------"
   time.sleep(0.2)




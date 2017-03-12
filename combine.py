#!/usr/bin/env python
import mraa
import time
import sys

#lets define the pins of the servo motor
motor_right=mraa.Pwm(9)
motor_left=mraa.Pwm(6)
motor_right.enable(True)
motor_left.enable(True)
motor_right.period_us(5000)
motor_left.period_us(5000)

#difine sound pin
pz=mraa.Gpio(10)
pz.dir(mraa.DIR_OUT)
pz.write(0)



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

def read_val(pin1,pin2):
    pin1.write(0)
    delayMicroseconds(2)
    pin1.write(1)
    delayMicroseconds(10)
    pin1.write(0)
    duration=pulseIn(pin2)
    distance=duration/58.2
    return distance

def sound():
    pz.write(1)
    time.sleep(1e-15)
    pz.write(0)
    time.sleep(1e-15)


while True:
    distance_left=read_val(outpin_left,inpin_left)
    distance_right=read_val(outpin_right,inpin_right)



    if distance_left >20 and distance_right>10:
        motor_left.write(0.5)
        motor_right.write(0.1)
        print 'straight'
    elif distance_left<20 and distance_left>=6 and distance_right>10:
        motor_left.write(0.5)
        motor_right.write(0)
        print 'right'
        sound()
    elif distance_left>20 and distance_right<10:
        motor_left.write(0)
        motor_right.write(0.1)
        print 'left'
        sound()
    elif distance_left<15 and distance_right<10:
        motor_left.write(100)
        motor_right.write(100)
        print 'stop'
    else:
        motor_left.write(100)
        motor_right.write(100)
        print 'stop only'
    #print distance_right
    #print distance_left
    #print '----------'
    time.sleep(0.2)


#!/usr/bin/env/ python

import mraa
import time
import sys

pot=mraa.Aio(0)

while 1:
    potval=float(pot.read())
    
    voltage=float(potval/1024)*5

    temprature=float(voltage-0.5)*100
    time.sleep(0.5)
    print temprature
    

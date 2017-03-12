import mraa
import time
import sys

l=False
pin1= 6
pin2= 9

motor1=mraa.Pwm(pin1)
motor2=mraa.Pwm(pin2)
motor1.enable(True)
motor2.enable(True)
motor1.period_us(5000)
motor2.period_us(5000)
val=['f','r','lt','rt','done']

while True:
     
 motor1.write(100)
 motor2.write(200)
 a=raw_input('what motion do you want?  ')
 if a in val:
  if a=="f":
     motor1.write(0.5)   
     motor2.write(0.1)
     time.sleep(0.3)
    
  elif a=='r':
       motor1.write(0.1)
       motor2.write(0.5)
       time.sleep(0.3)
     
  elif a=='rt':
       motor1.write(0.5)
       motor2.write(100)
       time.sleep(0.3)

  elif a=='lt':
       motor1.write(100)
       motor2.write(0.1)
       time.sleep(0.3)
  elif a=='done':
       l=True
       break
   
  else:
      motor1.write(100)
      motor2.write(100)
      time.sleep(0.5)
 else:
     print'provide valid input forward(f), reverse(r) left(lt) right(rt) or "done" for exit'
    

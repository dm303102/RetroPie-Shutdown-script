
#!/bin/python  
# Simple script for shutting down the raspberry Pi at the press of a button.  
# by Inderpreet Singh  
  
import RPi.GPIO as GPIO  
import os  
#import webiopi
import time  
import subprocess
import datetime
from datetime import datetime

# Setup the Pin with Internal pullups enabled and PIN in reading mode.  
BUTTON=5
LED=13
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
GPIO.setup(LED, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
t1 = 999999999999999999999

def Blink(numTimes,speed):
	for i in range(0,numTimes):## Run loop numTimes
		##print "Iteration " + str(i+1)## Print current loop
		GPIO.output(LED,True)## Switch on pin 7
		time.sleep(speed)## Wait
		GPIO.output(LED,False)## Switch off pin 7
		time.sleep(speed)## Wait

def Light(speed):
        my_pwm=GPIO.PWM(LED,100)
        my_pwm.start(1)
        for i in range(2, 100):## Run loop numTimes
                my_pwm.ChangeDutyCycle(i)
                if i<30:
                   time.sleep(speed)## Wait

def exitEmulator(BUTTON):
    #Blink(2,.5)
    if GPIO.input(BUTTON) == False:
        global t1
        t1 = datetime.now()
        print "Button pressed"
    elif GPIO.input(BUTTON) == True:
        print "Button released"
        t2 = datetime.now()
        delta = t2-t1
        deltaseconds = delta.total_seconds()
        if (deltaseconds > 4) : # pressed for > 5 seconds
            Blink(4,.5)
            print "Shutting down"
            subprocess.call(['sudo reboot "System halted by GPIO action" &'], shell=True)
        elif (deltaseconds > .4) : # press for > .4 < 4 seconds
            Blink(30,.1)
            print "Restarting System"
            subprocess.call(['sudo shutdown -r now "System halted by GPIO action" &'], shell=True)
            #os.system("sudo shutdown -h now")

Light(.3)
Blink(2,.5)
GPIO.output(LED,True)
GPIO.add_event_detect(BUTTON, GPIO.BOTH, callback=exitEmulator, bouncetime=200)
subprocess.call(['sudo echo "performance" |sudo tee /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor &'], shell=True)

# Now wait!  
try:
   while 1:  
       if GPIO.input(BUTTON) == False:
          #Blink(30,.05)
          GPIO.output(LED,True)
       time.sleep(1)
except KeyboardInterrupt:
   GPIO.cleanup()

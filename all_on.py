#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import random
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## use board pin numbering

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, True)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, True)
time.sleep(45)
nums=[11, 7,15]
lightshow = True
t = 0


while lightshow:
    for i in nums:
        random_lights = random.choice(nums)
        t = t+1
        # print "Testing %s" % i
        GPIO.setup(random_lights, GPIO.OUT)
        GPIO.output(random_lights, True)
        # raw_input("Next")

        time.sleep(.1)
        GPIO.output(random_lights, False)
        if t >= 140:
            lightshow = False
GPIO.cleanup()
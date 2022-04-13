#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)

print("LED on")

GPIO.output(14,GPIO.HIGH)
time.sleep(5)

print("LED off")

GPIO.output(14,GPIO.LOW)
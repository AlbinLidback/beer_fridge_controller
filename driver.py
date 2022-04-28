#!/usr/bin/env python3
import RPi.GPIO as GPIO

class driver:
    pins = {"fridge": 0}

    def __init__():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(fridge, GPIO.OUT)
        
    def toggle(name : str):
        pin = pins[name]
        if GPIO.input(pin):
            GPIO.output(pin, GPIO.LOW)
        else:
            GPIO.output(pin, GPIO.HIGH)
    
        #print("{} set to {}".format(name, GPIO.input(pin)))
        return GPIO.input(pin)


    
    def on(name : str):
        pin = pins[name]
        GPIO.output(pin, GPIO.HIGH)

        #print("{} set to {}".format(name, GPIO.input(pin)))
        #return GPIO.input(pin)
            
    def off(name : str):
        pin = pins[name]
        GPIO.output(pin, GPIO.LOW)
        
        #print("{} set to {}".format(name, GPIO.input(pin)))
        #return GPIO.input(pin)

    def get_names():
        return list(pins)
        
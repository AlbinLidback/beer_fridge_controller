#!/usr/bin/env python3

import RPi.GPIO as GPIO

class driver:
    pins = {"barskap_pin": 0, "slinga_pin": 1}

    def __init__():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(barskap_pin, GPIO.OUT)
        GPIO.setup(slinga_pin, GPIO.OUT)
        
    def toggle(name : str):
        pin = pins[name]
        if GPIO.input(pin):
            GPIO.output(pin, False)
        else:
            GPIO.output(pin, True)
        return GPIO.input(pin)
    
    def on(name : str):
        pin = pins[name]
        GPIO.output(pin, True)
        return GPIO.input(pin)
            
    def off(name : str):
        pin = pins[name]
        GPIO.output(pin, False)
        return GPIO.input(pin)

    def get_names():
        return list(pins)
        
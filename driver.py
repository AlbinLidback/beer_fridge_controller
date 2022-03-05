#!/usr/bin/env python3

import RPi.GPIO as GPIO

class driver:
    pins = {"barskap_pin": 0, "slinga_pin": 1}

    def init():
        try:
            GPIO.setmode(GPIO.BOARD)

            GPIO.setup(barskap_pin, GPIO.OUT)
            GPIO.setup(slinga_pin, GPIO.OUT)
        except:
            return "error"

    def toggle(name : str):
        try:
            pin = pins[name]
            if GPIO.input(pin):
                GPIO.output(pin, False)
            else:
                GPIO.output(pin, True)
            return GPIO.input(pin)
        except:
            return "error"

    def on(name : str):
        try:
            pin = pins[name]
            GPIO.output(pin, True)
            return GPIO.input(pin)
        except:
            return "error"
            
    def off(name : str):
        try:
            pin = pins[name]
            GPIO.output(pin, False)
            return GPIO.input(pin)
        except:
            return "error"
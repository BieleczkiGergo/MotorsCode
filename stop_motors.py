#! /bin/python

import RPi.GPIO as GPIO

pins = (11, 13, 15, 8)

GPIO.setmode( GPIO.BOARD )

for pin in pins:
	GPIO.setup( pin, GPIO.OUT )
	GPIO.output( pin, GPIO.LOW )


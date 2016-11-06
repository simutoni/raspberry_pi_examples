import RPi.GPIO as GPIO
import random
from time import sleep

red_pin = 27 # because I set bellow GPIO to BCM mode, else would be 13
green_pin = 4
blue_pin = 17
colision_sensor = 18 

GPIO.setmode(GPIO.BCM)

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(colision_sensor, GPIO.IN)

def set_color(r, g, b):
	GPIO.output(red_pin, r)
	GPIO.output(green_pin, g)
	GPIO.output(blue_pin, b)

# on the rgb sensor that I use 1 means False and 0 means True.
# so maybe in your case you need to inverse them.
def set_red():
	set_color(0, 1, 1)

def set_white():
	set_color(0, 0, 0)

def set_yellow():
	set_color(0, 0, 1)

def set_purple():
	set_color(0, 1, 0)

def set_green():
	set_color(1, 0, 1)

def set_light_blue():
	set_color(1, 0, 0)

def set_blue():
	set_color(1, 1, 0)

colors_list = [set_red, set_blue, set_green, set_white, set_yellow, set_purple, set_light_blue]

try:  
	while True:
		# you can use a button here if you want, then you dont need the not condition.
		# the colision sensor that I use sends data all the time and when is triggered
		# it will stop sending data.
		if not GPIO.input(colision_sensor):
			print ("button pressed")
			random.sample(colors_list,  1)[0]() # call the method to turn on the led.
		sleep(0.1)
finally:  
	print("Cleaning up.")
	GPIO.cleanup()


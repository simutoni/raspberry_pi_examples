import os
import pygame, sys
import pygame.camera
import RPi.GPIO as GPIO
import random
from time import sleep
from pygame.locals import *

# because I set bellow GPIO to BCM mode, else would be 12
vibration_sensor = 18

# set image weight
width = 640
height = 480

#initialise pygame   
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(width,height))
cam.start()

GPIO.setmode(GPIO.BCM)
GPIO.setup(vibration_sensor, GPIO.IN)

image_index = 0
try:  
	while True:
		if GPIO.input(vibration_sensor):
			image_index += 1
			print("vibration detected")

			#take a picture
			image = cam.get_image()

			#save picture
			pygame.image.save(image, 'picture{}.jpg'.format(image_index))
finally:  
	print("Cleaning up.")
	GPIO.cleanup()
	cam.stop()


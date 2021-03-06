from time import sleep
import RPi.GPIO as GPIO

# because I set bellow GPIO to BCM mode, else would be 12
motion_sensor = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_sensor, GPIO.IN)

try:
    while True:
        if GPIO.input(motion_sensor):
            print("motion detected")
        sleep(1)
finally:
    print("Cleaning up.")
    GPIO.cleanup()

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

step_pins = [4, 17, 27, 22]
# if you want to make the rotation the other way around you need to revert the list of gpios.
#step_pins.reverse()

print("Setup pins")
for pin in step_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)


seq = [[1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1],
       [1, 0, 0, 1]
       ]

for i in range(512):
    for half_step in range(8):
        for pin in range(4):
            GPIO.output(step_pins[pin], seq[half_step][pin])
        # this sleep controls the speed of the motor
        time.sleep(0.001)

GPIO.cleanup()

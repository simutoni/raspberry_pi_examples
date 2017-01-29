import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 17
GPIO_ECHO = 20
speedSound = 34300  # Speed of sound in cm/s
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO, GPIO.IN)  # Echo


def get_distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # start time
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    # time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    # Calculate the time in which the wave travels from sensor to the object.
    # taking into account just half the time as the total time is from sensor to the object and back.
    wave_time = (stop_time - start_time)
    return wave_time * speedSound / 2

print("Distance: {0:5.1f} cm".format(get_distance()))

GPIO.cleanup()

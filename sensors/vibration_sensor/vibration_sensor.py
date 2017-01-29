import RPi.GPIO as GPIO

# because I set bellow GPIO to BCM mode, else would be 12
vibration_sensor = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(vibration_sensor, GPIO.IN)

try:
    while True:
        if GPIO.input(vibration_sensor):
            print("vibration detected")
finally:
    print("Cleaning up.")
    GPIO.cleanup()

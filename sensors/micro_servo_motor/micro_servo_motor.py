import RPi.GPIO as GPIO
import time


# make sure that you have rights to access the gpio
# sudo chown your_user.gpio /dev/gpiomem
# sudo chmod g+rw /dev/gpiomem

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 50)

p.start(7.5)

p.ChangeDutyCycle(2.5)  # turn towards 0 degree
time.sleep(1)  # sleep 1 second
p.ChangeDutyCycle(3.5)  # turn towards 0 degree
time.sleep(1)  # sleep 1 second
p.ChangeDutyCycle(5.0)  # turn towards 45 degree
time.sleep(1)  # sleep 1 second
p.ChangeDutyCycle(7.5)  # turn towards 90 degree
time.sleep(1)  # sleep 1 second
p.ChangeDutyCycle(10.0)  # turn towards 135 degree
time.sleep(1)  # sleep 1 second
p.ChangeDutyCycle(12.5)  # turn towards 180 degree
time.sleep(1)  # sleep 1 second

p.stop()
GPIO.cleanup()

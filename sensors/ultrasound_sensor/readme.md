# Ultrasound sensor module HC-SR04
## How to wire it:
- Echo - Connect it to any gpio pin (in our case is gpio17 in BCM mode)
- Trig - Here you need an 1kOhm resistance because the sensor sends through trigger 5v and the raspberry pi supports on GPIO pins only 3v.
So connect the resistance to the trig pin and only after that connect it to any gpio pin on raspberry (in our case gpio16 BCM mode)
- vcc (power 5v) - 5v pins for example pin 2 or 4 with board mode
- gnd you - can connect it to ground pins ex. pin 6, 9, 14, 20 (board mode)

## How it works
Fist, when you trigger the sensor it sends an ultrasonic wave that is going tu bunp into the object and came back to the sensor.
In this way we know how much time the wave made from the sensor to the object and back.
Next we need to multiply the time with the speed of sound which is 34300 m/s and after this we need to divede it by 2
because we need only the distance from the sensor to the object excluding the way back of the wave.
# Vibration sensor
## You have three pins that you need to connect to raspberry:
- Gnd(-) - groud (you can connect it to ground pins ex. pin 6, 9, 14, 20...)
- vcc (power 5v) - 5v pins for example pin 2 or 4 (Board mode)
- DO - you can connect it on any gpio pin but in this example we are using gpio18 (BCM mode)

## How it works:
The sensor sends 1 or 0 through it's output pin.
- 1 means that it detected a vibration.
- 0 means that it didn't detect anything.

This sensor has a hardware potentiometer where you can set the sensibility.
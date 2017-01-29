# LCD module i2c

## 1. Connecting the lcd to raspberry through the i2c interface.
- we assuming that we take the board numbering not BCM one
- GND - connects to ground for example (pin 6 )
- VCC - to pin 2 or 4 that are 5v power pins
- SDA - connects to pin 3
- scl - connects to pin 5

## 2. Install the smbus library : sudo apt-get install python3-smbus

## 3. If it still doesn't work you sould do next thigs:
- sudo apt-get update
- sudo apt-get upgrade
- sudo reboot


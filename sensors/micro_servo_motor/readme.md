# Micro servo motor 9g

## You have three wires that are coming from the servo motor:
- Orange: signal pin (you can connect it to any gpio pin but take that into consideration in the code)
- Red: vcc (power 5v) + (you can connect it to 5v pins for example pin 2 or 4  board mode)
- Brown: groud (you can connect it to ground pins ex. pin 6, 9, 14, 20...)

## How it works
The servo motor has an input pin where you can send the DutyCycle that you want to chage for example (turn it to 30 degrees).
You can do this with this method ChangeDutyCycle.
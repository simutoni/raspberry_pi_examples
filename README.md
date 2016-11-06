# raspberry_pi_examples
I created this repository to share with you some examples of using some sensors with raspberry pi.

I attached an image with the pins description os raspberry pi 3.
Take into account that the pin number can be used in python only if you use GPIO.setmode(GPIO.BOARD) else if you use GPIO.setmode(GPIO.BCM) you will work with the number from the pin name.
![alt tag](https://github.com/simutoni/images_for_git_projects/blob/master/pi_pins.png)

## Vibration sensor example
In this example I am using a usb camera and a vibration sensor. When the vibration sensor is triggered the camera is going to take and save an image.

On vibration sensor you have 3 pins:
vcc means the power pin, the second one in the middle is ground pin and DO is the output pin.
![alt tag](https://github.com/simutoni/images_for_git_projects/blob/master/vibration_sensor1.jpg)
![alt tag](https://github.com/simutoni/images_for_git_projects/blob/master/vibration_sensor2.jpg)

## RGB led example
In this example I am using a RGB led and a colision sensor(because I don't have a button now).
Take into account the for the RGB led that I am using for input values True means False and False means True so they are opposite.
And also the collision sensor sends data all the time and the only case when is not sends data is when is triggered.

On RGB led you have 4 pins: 3 of them are for RGB and one of them is for power(vcc)
![alt tag](https://github.com/simutoni/images_for_git_projects/blob/master/rgb_led.jpg)

On colision sensor you have 3 pins: vcc means the power pin, the GND is ground pin and OUT is the output pin.
![alt tag](https://github.com/simutoni/images_for_git_projects/blob/master/colision_sensor.jpg)

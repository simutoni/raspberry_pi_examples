# raspberry_pi_examples
I created this repository to share with you some examples of using some sensors with raspberry pi.

I attached an image with the pins description os raspberry pi 3.
Take into account that the pin number can be used in python only if you use GPIO.setmode(GPIO.BOARD) else if you use GPIO.setmode(GPIO.BCM) you will work with the number from the pin name.
![alt tag](https://github.com/simutoni/images_for_git_projects/blob/master/pi_pins.png)


## Things you need yo configure before starting

1) Make sure that your i2c and camera are enabled on the raspberry pi.
Type "sudo raspi-config" and search for i2c and camera there.

2) Make sure that you have the permissions to use the camera the i2c interface and the gpio pins.
sudo adduser your_username adm
sudo adduser your_username i2c
sudo adduser your_username gpio
sudo adduser your_username video
sudo adduser your_usernae spi

3) You need to install some libraries:
sudo apt-get update
sudo apt-get upgrade
sudo apt-get -y install python3-rpi.gpio
sudo apt-get install python3-smbus

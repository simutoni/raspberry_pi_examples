from time import sleep
import picamera

camera = picamera.PiCamera()

# here are some settings that you may want to work with:
# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
# camera.video_stabilization = False
# camera.exposure_compensation = 0
# camera.exposure_mode = 'auto'
# camera.meter_mode = 'average'
# camera.awb_mode = 'auto'
# camera.image_effect = 'none'
# camera.color_effects = None
# camera.rotation = 0
# camera.hflip = False
# camera.vflip = False
# camera.crop = (0.0, 0.0, 1.0, 1.0)


# if you camera is upside down or in other position you can flip the image like this:
# camera.hflip = True # horizontal flip
# camera.vflip = True # vertical flip

# for photo
camera.capture('image1.jpg')

# for video
# camera.start_recording('video.h264')
# sleep(5)
# camera.stop_recording()

# Camera module v2

This module is pretty easy to use.
You have some values that you can play with in order to get the best image.
- camera.sharpness = 0
- camera.contrast = 0
- camera.brightness = 50
- camera.saturation = 0
- camera.ISO = 0
- camera.video_stabilization = False
- camera.exposure_compensation = 0
- camera.exposure_mode = 'auto'
- camera.meter_mode = 'average'
- camera.awb_mode = 'auto'
- camera.image_effect = 'none'
- camera.color_effects = None
- camera.rotation = 0
- camera.hflip = False
- camera.vflip = False
- camera.crop = (0.0, 0.0, 1.0, 1.0)

You need only to say camera.capture('image_name') after you instantiate the camera obj and is going to work.
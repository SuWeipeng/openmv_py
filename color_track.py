import sensor
import image

red_threshold = (0, 80, 43, 75, 35, 55)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10)
sensor.set_auto_whitebal(False)

while(True):
  img = sensor.snapshot()
  blobs = img.find_blobs([red_threshold])
  if blobs:
    print(blobs)
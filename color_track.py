import sensor
import image
import time

red_threshold = (0, 80, 43, 75, 35, 55)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10)
sensor.set_auto_whitebal(False)

clock = time.clock()

while(True):
  clock.tick()
  img = sensor.snapshot()
  blobs = img.find_blobs([red_threshold], area_threshold=110)
  if blobs:
    print(blobs)
    for b in blobs:
      img.draw_rectangle(b[0:4])
  print(clock.fps())
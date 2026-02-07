import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 0)
light_time = 0.2
try:
    while True:
        for led in leds:
            GPIO.output(led, 1)
            time.sleep(light_time)
            GPIO.output(led, 0)
        for led in reversed(leds):
            GPIO.output(led, 1)
            time.sleep(light_time)
            GPIO.output(led, 0)
except KeyboardInterrupt:
    GPIO.cleanup()
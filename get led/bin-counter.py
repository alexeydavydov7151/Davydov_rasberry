import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
up_button = 26
down_button = 19
for pin in leds:
    GPIO.setup(pin, GPIO.OUT)
for pin in leds:
    GPIO.output(pin, GPIO.LOW)
GPIO.setup(up_button, GPIO.IN)
GPIO.setup(down_button, GPIO.IN)
num = 0
def dec2bin(value):
    binary_string = bin(value)[2:]
    binary_string = binary_string.zfill(8)
    result = []
    for bit in binary_string:
        result.append(int(bit))
    return result
sleep_time = 0.2
try:
    while True:
        if GPIO.input(up_button):
            if num < 255:
                num = num + 1
                print(num, dec2bin(num))
                GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
        if GPIO.input(down_button):
            if num > 0:
                num = num - 1
                print(num, dec2bin(num))
                GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
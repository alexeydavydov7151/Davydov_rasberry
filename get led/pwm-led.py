import time
import RPi.GPIO as GPIO
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
pwm = GPIO.PWM(LED_PIN, 200)
brightness = 0
pwm.start(brightness)
while True:
    pwm.ChangeDutyCycle(brightness)
    time.sleep(0.05)
    brightness += 1
    if brightness > 100:
        brightness = 0
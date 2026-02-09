import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led_pin = 26
sensor_pin = 6
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(sensor_pin, GPIO.IN)
while True:
    # Читаем состояние фототранзистора
    sensor_state = GPIO.input(sensor_pin)
    if sensor_state == 1:
        GPIO.output(led_pin, 0) 
    else:
        GPIO.output(led_pin, 1) 
    
    time.sleep(0.1)
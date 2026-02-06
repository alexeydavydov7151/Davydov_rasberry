import RPi.GPIO as GPIO
import time

# Настройка пинов
GPIO.setmode(GPIO.BCM)
led_pin = 5
sensor_pin = 6

# Настройка входа/выхода
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(sensor_pin, GPIO.IN)

# Бесконечный цикл
while True:
    # Читаем состояние фототранзистора
    sensor_state = GPIO.input(sensor_pin)
    
    # Включаем светодиод наоборот
    if sensor_state == 1:
        GPIO.output(led_pin, 0)  # выключить
    else:
        GPIO.output(led_pin, 1)  # включить
    
    time.sleep(0.1)
import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def set_number(self, number):
        bin_value = bin(number)[2:].zfill(len(self.gpio_bits))
        for i in range (len(self.gpio_bits)):
            GPIO.output(self.gpio_bits[i],int(bin_value[i]))
        if self.verbose:
            print(f"Установлено число: {number}")
    def set_voltage(self, voltage):
        max_number = 2**len(self.gpio_bits) - 1
        number = int(voltage * max_number / self.dynamic_range)
        number = max(0, min(number, max_number))
        self.set_number(number)
        if self.verbose:
            print(f"Установлено напряжение: {voltage} В")

if __name__ == "__main__":
    dac = None
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.149, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        if dac:
            dac.deinit()
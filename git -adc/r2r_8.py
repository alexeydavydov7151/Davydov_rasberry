import RPi.GPIO as GPIO
import time 

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def clean(self):
        self.number_to_dac(0)
        GPIO.cleanup()

    def number_to_dac(self,number):
        out =  [int(i) for i in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, out)
        
    def sequential_counting_adc(self):
        for code in range (256):
            self.number_to_dac(code)
            time.sleep(self.compare_time)
            comp_value = GPIO.input(self.comp_gpio)
            if comp_value == 1:
                return code
                
        return 255

    def code_to_voltage(self, code):
        return (code / 255) * self.dynamic_range
        
    def get_sc_voltage(self):
        code = self.sequential_counting_adc()
        voltage = self.code_to_voltage(code)
        return voltage
        
if __name__ == "__main__":
    DYNAMIC_RANGE_V = 3.21

    adc = None

    try:
        adc = R2R_ADC(dynamic_range = DYNAMIC_RANGE_V, compare_time=0.01, verbose=True)
        
        while True:
            voltage = adc.get_sc_voltage()
            print(voltage)

    finally:
        if adc:
            adc.number_to_dac(0)
            GPIO.cleanup()
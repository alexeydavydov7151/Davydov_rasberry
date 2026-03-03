import time
from adc_plot import plot_voltage_vs_time
from r2r_adc import R2R_ADC 

DYNAMIC_RANGE = 3.21
COMPARE_TIME = 0.001 
DURATION = 3.0  

def main():
    adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE, 
                  compare_time=COMPARE_TIME, 
                  verbose=False)
    
    voltage_values = []
    time_values = []
    
    try:
        start_time = time.time()
        while time.time() - start_time < DURATION:
            voltage = adc.get_sc_voltage()
            current_time = time.time() - start_time
            
            voltage_values.append(voltage)
            time_values.append(current_time)

        plot_voltage_vs_time(time_values, voltage_values, DYNAMIC_RANGE)
        
    finally:
        del adc

if __name__ == "__main__":
    main()
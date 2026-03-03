import adc_plot as plot
import r2r_8 as adc
import time

adc_object = adc.R2R_ADC(dynamic_range=3.3)

voltages = []
times = []
duration = 5.0

try:
    start = time.time()
    while (time.time() - start) < duration:
        voltage = adc_object.get_sar_voltage()
        voltages.append(voltage)
        times.append(time.time() - start)
    
    plot.plot_voltage_vs_time(times, voltages, 3.3)
    plot.plot_sampling_period_hist(time)
finally:
    adc_object.clean()
import adc_plot as plot
import r2r_adc as adc
import time

r2r = adc.R2R_ADC(3.183,0.001,True)
voltages = list()
times = list()
duration = 5
try:
    start = time.time()
    while (time.time()-start) < duration:
        voltage =r2r.sequential_counting_adc()
        voltages.append(voltage)
        times.append(time.time()-start)
finally:
    r2r.deinit()
plot.plot_voltage_vs_time(times,voltages,3.18)
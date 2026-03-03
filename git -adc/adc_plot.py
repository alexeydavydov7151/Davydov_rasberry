from matplotlib import pyplot as plt
def plot_voltage_vs_time(time , voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.xlim(0,10)
    plt.ylim(max_voltage)
    plt.grid(True)
    plt.show()
time=list()
voltage = list()

plot_voltage_vs_time(time, voltage, 3.18)
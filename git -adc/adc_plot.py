import matplotlib.pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("зависимость напряжения от времени", fontsize=14)
    plt.xlabel("Время, с", fontsize=12)
    plt.ylabel("Напряжение, в", fontsize=12)
    plt.legend()
    plt.show()
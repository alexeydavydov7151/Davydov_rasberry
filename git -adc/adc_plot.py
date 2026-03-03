import matplotlib.pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("зависимость напряжения от времени", fontsize=14)
    plt.xlabel("Время, с", fontsize=12)
    plt.ylabel("Напряжение, в", fontsize=12)
    plt.legend()
    plt.show()
def plot_sampling_period_hist(time):
    # 2. Создаем список для хранения промежутков времени
    sampling_periods = []
    
    # 3. Заполняем список разницами между соседними моментами времени
    for i in range(1, len(time)):
        period = time[i] - time[i-1]
        sampling_periods.append(period)
    
    # Проверка на наличие данных
    if not sampling_periods:
        print("Нет данных для построения гистограммы!")
        return
    
    # 4. Создаем окно для отображения графика
    plt.figure(figsize=(10,6))
    
    # 5. Размещаем гистограмму
    plt.hist(sampling_periods, bins=30, edgecolor='black', alpha=0.7, color='skyblue')
    
    # 6. Задаем название графика и осей
    plt.title("Распределение периодов измерений", fontsize=14)
    plt.xlabel("Период измерения, с", fontsize=12)
    plt.ylabel("Количество измерений", fontsize=12)
    
    # 7. Задаем границы по оси X
    plt.xlim(0, 0.06)
    
    # 8. Включаем отображение сетки
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # 9. Отображаем гистограмму
    plt.tight_layout()
    plt.show()
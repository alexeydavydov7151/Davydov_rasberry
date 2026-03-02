import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        """
        Конструктор класса.
        dynamic_range: максимальное входное напряжение АЦП (динамический диапазон)
        compare_time: время ожидания после установки кода на ЦАП для компаратора (по умолчанию 0.01 с)
        verbose: флаг для вывода отладочной информации
        """
        self.dynamic_range = dynamic_range
        self.compare_time = compare_time
        self.verbose = verbose

        # Пины ЦАП (8 бит)
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        # Пин компаратора
        self.comp_gpio = 21

        # Инициализация GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.comp_gpio, GPIO.IN)

        if self.verbose:
            print("R2R_ADC инициализирован: dynamic_range={} В, compare_time={} с".format(
                dynamic_range, compare_time))

    def __del__(self):
        """Деструктор: сбрасывает ЦАП и очищает настройки GPIO."""
        self.number_to_dac(0)  # Устанавливаем все пины в 0
        GPIO.cleanup()
        if self.verbose:
            print("GPIO очищены, ЦАП сброшен в 0.")

    def number_to_dac(self, number):
        """
        Подаёт целое число (0–255) на параллельный вход ЦАП.
        Устанавливает соответствующие биты на выходах GPIO.
        """
        if number < 0 or number > 255:
            raise ValueError("Число должно быть в диапазоне 0–255")
        
        # Проходим по всем битам (от младшего к старшему)
        for i, gpio in enumerate(self.bits_gpio):
            # Проверяем i-й бит числа (0 — младший)
            bit = (number >> i) & 1
            GPIO.output(gpio, bit)
        
        if self.verbose:
            print("Установлен код ЦАП: {} ({:08b})".format(number, number))

    def sequential_counting_adc(self):
        """
        Последовательный АЦП (счёт):
        - Подаёт коды от 0 до 255
        - После каждого кода ждёт compare_time
        - Читает компаратор
        - Если компаратор показал превышение (1), возвращает последний поданный код
        - Если дошли до 255 и превышения не было, возвращает 255
        """
        for code in range(256):
            self.number_to_dac(code)
            time.sleep(self.compare_time)
            
            # Чтение компаратора (1 = Vdac > Vin)
            comp_value = GPIO.input(self.comp_gpio)
            
            if self.verbose:
                print("Код={}, компаратор={}".format(code, comp_value))
            
            if comp_value == 1:
                if self.verbose:
                    print("Превышение при коде", code)
                return code
        
        # Если ни разу не превысило, возвращаем максимальный код
        if self.verbose:
            print("Превышение не достигнуто, возвращаем 255")
        return 255

    def get_sc_voltage(self):
        """
        Выполняет измерение методом последовательного счёта
        и возвращает напряжение в вольтах.
        """
        code = self.sequential_counting_adc()
        # Преобразование кода в напряжение
        voltage = (code / 255.0) * self.dynamic_range
        return voltage


if __name__ == "__main__":
    # Вставьте сюда измеренное мультиметром значение dynamic_range (в вольтах)
    DYNAMIC_RANGE = 3.3  # Пример: измените на реальное значение
    
    adc = None
    try:
        # Создаём объект АЦП с динамическим диапазоном и включенным verbose для отладки
        adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE, compare_time=0.01, verbose=True)
        
        while True:
            voltage = adc.get_sc_voltage()
            print("Измеренное напряжение: {:.3f} В".format(voltage))
            # Небольшая пауза между измерениями
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nИзмерение прервано пользователем")
    finally:
        if adc:
            # Явно вызываем деструктор (хотя он вызовется и при сборке мусора,
            # но для гарантии чистоты GPIO делаем это здесь)
            adc.__del__()
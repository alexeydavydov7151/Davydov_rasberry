import smbus
class MCP4725:
    def __init__(self,dynamic_range,address = 0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        self.adress = address
        self.wm = 0x00
        self.pds = 0x00
        self.verbose = verbose
        self.dynamic_range = dynamic_range
        self.max_number=4095
    def deinit(self):
        self.bus.close()
    def set_number(self,number):
        if not isinstance (number,int):
            print(" На вход ЦАП можно подавать только целые числа")
        if not (0 <= number<= 4095):
            print("Число выходит за разрядность драйвера 12 бит")
        first_byte =self.wm | self.pds | number >>8 
        second_byte= number & 0xFF
        self.bus.write_byte_data(0x61,first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number},отправленные по I2c данные [0x{(self.adress<<1):02X},0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    def set_voltage(self, voltage):
        number = int(voltage * self.max_number / self.dynamic_range)
        number = max(0, min(number, self.max_number))
        self.set_number(number)
if __name__=="__main__":
    dac=MCP4725(dynamic_range = 5,address=0x61,verbose=True)
    try:
        voltage =float (input("Введите число:"))
        dac.set_voltage(voltage)
    finally:
        dac.deinit()




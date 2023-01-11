# 4 Инкапсуляция. Определить класс Car, который будет содержать конструктор,
# в котором будет инициализироваться private переменная maxprice,
# а также методы изменения и вывода максимальной стоимости машины.
class Car():

    def __init__(self, maxprice):
        self.__maxprice = maxprice

    def upgrade(self, maxprice):
        self.__maxprice = float(input(maxprice))
        return self.__maxprice

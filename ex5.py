# 5 Создать класс Animal и определить в нем метод make_a_sound(). Метод должен вывоводить строку "Издает звук"
# Cоздать классы Cat и Dog с методами scratch() и dig() соответственно.
# Метод scratch должен выводить строку "Царапать мебель".
# Метод dig должен выводить строку "Рыть землю".
# в классах Cat и Dog переопределите метод make_a_sound() базового класса Animal.

class Animal():

    def make_a_sound(self):
        print("Издает звук")

class Cat(Animal):

    def scratch(sel):
        print("Царапать мебель")

    def make_a_sound(self):
        print("Издает звук мяу")

class Dog(Animal):

    def dig(self):
        print("Рыть землю")

    def make_a_sound(self):
        print("Издает звук гав")

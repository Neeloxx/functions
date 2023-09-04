import datetime


# Создайте класс MathUtils, который будет содержать статический метод multiply,
# принимающий два числа и возвращающий их произведение.
# Используйте этот метод для умножения двух чисел и выведите результат.

class MathUtils:
    @staticmethod
    def multiply(a, b):
        return a * b


res = MathUtils.multiply(2, 3)
print(res)


# Создайте класс Person, у которого будет статический метод is_adult,
# принимающий возраст человека. Метод должен вернуть True, если возраст больше или равен 18,
# и False в противном случае. Создайте несколько объектов класса Person
# с разными возрастами и проверьте их на совершеннолетие.

class Person:
    @staticmethod
    def is_adult(age):
        return True if age >= 18 else False


a = Person
print(a.is_adult(17))
b = Person
print(b.is_adult(20))


# Создайте класс DateUtils, который будет содержать статический метод is_weekend,
# принимающий дату в виде строки в формате 'гггг-мм-дд'.
# Метод должен вернуть True, если дата выпадает на выходной день (суббота или воскресенье),
# и False в противном случае. Используйте метод для проверки нескольких дат.

class DateUtils:
    @staticmethod
    def is_weekend(date):
        date = date.split('-')
        year, month, day = int(date[0]), int(date[1]), int(date[2])
        date = datetime.date(year, month, day)
        return date.weekday() >= 5


a = DateUtils
print(a.is_weekend('2022-01-01'))
b = DateUtils
print(a.is_weekend('2022-01-25'))


# Создайте класс Rectangle, у которого будут атрибуты width (ширина) и height (высота).
# Создайте метод класса create_square, который будет принимать только одно значение (сторону квадрата) и
# создавать объект Rectangle со сторонами, равными этому значению.
# Используйте метод класса для создания объекта Rectangle в форме квадрата.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def create_square(cls, side):
        return cls(side, side)


a = Rectangle.create_square(10)
print(a.width)
print(a.height)


# Создайте класс Square, у которого будет атрибут side (сторона квадрата).
# Создайте метод класса create_from_perimeter, который будет
# принимать значение периметра и создавать объект Square с равными сторонами,
# чтобы получился квадрат с заданным периметром. Используйте метод класса для создания
# квадрата на основе периметра.

class Square:
    def __init__(self, side):
        self.side = side

    @classmethod
    def create_from_perimetr(cls, perimetr):
        side = perimetr / 4
        return cls(side)


c = Square.create_from_perimetr(20)
print(c.side)


# Создайте класс Circle, у которого будет атрибут radius.
# Определите свойство diameter, которое будет возвращать диаметр
# окружности (удвоенное значение радиуса). Также определите сеттер diameter,
# который будет устанавливать новое значение радиуса на основе переданного диаметра.
# Проверьте работу свойства и сеттера.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diametr(self):
        return self.radius * 2

    @diametr.setter
    def diametr(self, new_diametr):
        self.radius = new_diametr / 2


v = Circle(2)
print(v.diametr)
v.diametr = 10
print(v.radius)


# Создайте класс Temperature, у которого будет атрибут celsius.
# Определите свойства fahrenheit и kelvin, которые будут возвращать соответствующие
# значения температуры в других шкалах
# (по формулам: fahrenheit = celsius * 9/5 + 32, kelvin = celsius + 273.15).
# Также определите сеттеры fahrenheit и kelvin, которые будут устанавливать новые значения
# температуры на основе переданных значений в других шкалах. Проверьте работу свойств и сеттеров.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def farenheit(self):
        return self.celsius * 9 / 5 + 32

    @property
    def kelvin(self):
        return self.celsius + 273

    @farenheit.setter
    def farenheit(self, value):
        self.celsius = value * 9 / 5 + 32

    @kelvin.setter
    def kelvin(self, value):
        self.celsius = value - 273


print('--------')
t = Temperature(20)
print(t.farenheit)
t.farenheit = 30
print(t.farenheit)
print(t.kelvin)
t.kelvin = 30
print(t.kelvin)


# Создайте класс Product, у которого будет атрибут price.
# Определите свойство discounted_price, которое будет возвращать цену с учетом скидки (например, 10% скидка).
# Также определите сеттер discounted_price, который будет устанавливать новую цену
# с учетом скидки на основе переданного значения. Проверьте работу свойства и сеттера.

class Product:
    def __init__(self, price, per=0.1):
        self.price = price
        self.per = per

    @property
    def discounted_price(self):
        value = self.price * (1 - self.per)
        return value

    @discounted_price.setter
    def discounted_price(self, value):
        self.price = value / (1 - self.per)


print('------------')
d = Product(100)
print(d.discounted_price)
d.discounted_price = 200
print(d.discounted_price)
print(d.price)
print('------------')


# Создайте класс Password, у которого будет атрибут password.
# Определите свойство hashed_password, которое будет возвращать хешированное
# значение пароля (например, с использованием функции hashlib.sha256).
# Также определите сеттер hashed_password, который будет устанавливать новое
# хешированное значение пароля на основе переданного значения. Проверьте работу свойства и сеттера.
import hashlib
class Passwoed:
    def __init__(self, password):
        self.__password = password

    @property
    def hashed_password(self):
        return hashlib.sha256(self.__password)

    @hashed_password.setter
    def hashed_password(self, new_password):
        self.__password = new_password


# Создайте класс Multiplier, который будет представлять умножитель.
# У класса Multiplier должен быть атрибут factor, инициализированный значением 1.
# Определите метод __call__, который будет принимать число в качестве аргумента
# и возвращать результат умножения этого числа на factor. Также добавьте метод set_factor,
# который будет изменять значение атрибута factor.

class Multiplaier:
    factor = 1

    def __call__(self, num):
        return self.factor * num

    def set_factor(self, new_factor):
        self.factor = new_factor


m = Multiplaier()
print(m(3))
m.set_factor(2)
print(m(3))


# Создайте класс AverageCalculator, который будет представлять калькулятор среднего значения.
# У класса AverageCalculator должен быть атрибут numbers, инициализированный пустым списком.
# Определите метод __call__, который будет принимать число в качестве аргумента и добавлять его в список numbers.
# Также добавьте метод calculate_average, который будет возвращать среднее значение всех чисел в списке numbers.

class AverageCalculator:
    number = []

    def __call__(self, num):
        self.number.append(num)

    def calculate_average(self):
        return sum(self.number) / len(self.number)


k = AverageCalculator()
k(1)
k(2)
k(3)
print(k.calculate_average())


# Создайте класс Logger, который будет представлять логгер.
# У класса Logger должен быть атрибут log, инициализированный пустой строкой.
# Определите метод __call__, который будет принимать строку в качестве аргумента и добавлять
# ее в атрибут log с новой строки. Также добавьте метод clear_log, который будет очищать атрибут log.

class Logger:
    log = ''

    def __call__(self, s):
        if self.log == '':
            self.log += f'{s}'
        else:
            self.log += f'\n{s}'

    def clear_log(self):
        self.log = ''


l = Logger()
l('abc')
l('cdz')
print(l.log)
l.clear_log()
print(l.log)
l('cdz')
l('cdz')
print(l.log)

# Создайте класс FunctionRunner, который будет представлять исполнителя функций.
# У класса FunctionRunner должен быть атрибут function, инициализированный значением None.
# Определите метод __call__, который будет принимать произвольное количество аргументов и
# передавать их в вызываемую функцию, заданную атрибутом function. Также добавьте метод set_function,
# который будет устанавливать новую вызываемую функцию.

# class FunctionRunner:
#     function = None
#
#     def __call__(self, *args, **kwargs):
#         self.function = args
#
#     def set_function(self):
#         pass

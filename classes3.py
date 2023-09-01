from dataclasses import dataclass
# Создайте класс Person, у которого есть атрибуты name и age.
# Реализуйте магический метод getattr, который будет возвращать сообщение "Атрибут не существует",
# если запрашиваемого атрибута нет.
# Проверьте, что при обращении к несуществующему атрибуту выводится соответствующее сообщение.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        return 'атрибут не существует'


p = Person('Alex', 25)
print(p.name)
print(p.age)
print(p.work)


# Реализуйте класс Temperature, который представляет температуру в градусах Цельсия.
# Добавьте магический метод __getattribute__, который будет конвертировать температуру
# в градусах Фаренгейта при обращении к атрибуту fahrenheit.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __getattr__(self, item):
        if item == 'fahrenheit':
            return self.celsius * 9 / 5 + 32
        else:
            return 'Mistake'


t = Temperature(10)
print(t.celsius)
print(t.fahrenheit)
print(t.kelvin)


# Создайте класс Logger, у которого есть атрибут log.
# Реализуйте магический метод setattr, который будет записывать все значения атрибутов в атрибут log.
# Проверьте, что при изменении значений атрибутов, изменения записываются в атрибут log.

class Logger:
    def __init__(self):
        self.log = []

    def __setattr__(self, key, value):
        if key != 'log':
            self.log.append(f'{key}:{value}')
        super().__setattr__(key, value)


l = Logger()
l.name = 'Alex'
l.age = 25
print(l.log)


# Реализуйте класс ProtectedAttributes, который запрещает доступ к определенным атрибутам.
# Класс должен иметь список "защищенных" атрибутов,
# и при попытке получения или установки значения для этих атрибутов должно возникать исключение.

class ProtectedAttributes:
    def __init__(self, **kwargs):
        super().__setattr__('_protected', kwargs)

    def __getattribute__(self, item):
        protected = super().__getattribute__('_protected')
        if item in protected:
            raise AttributeError(f"Доступ к {item} запрещен")
        else:
            return super().__getattribute__(item)

    def __setattr__(self, key, value):
        protected = super().__getattribute__('_protected')
        if key in protected:
            raise AttributeError(f"Изменение {key} запрещена")
        else:
            super().__setattr__(key, value)


# Создайте класс CurrencyConverter, который представляет собой конвертер валюты.
# Реализуйте магический метод __setattr__, чтобы при установке значения атрибуту rate
# выполнялась проверка на положительность значения.

# class CurrencyConverter:
#     def __init__(self):
#         self.rate = None
#
#     def __setattr__(self, name, value):
#         if name == 'rate' and value is not None and value <= 0:
#             return 'rate <= 0'
#         super().__setattr__(name, value)
#
#     @property
#     def rate(self):
#         return self.rate
#
#     @rate.setter
#     def rate(self, value):
#         self.rate = value
#
#
# c = CurrencyConverter()
# c.rate = 1.5
# print(c.rate)


# Реализуйте класс Rectangle, который представляет собой прямоугольник.
# Добавьте магический метод __eq__, чтобы два прямоугольника считались равными, если их ширина и высота совпадают.

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b
        return False


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(15, 20)
print(r1 == r2)
print(r1 == r3)


# Создайте класс Vector, представляющий собой вектор в трехмерном пространстве.
# Реализуйте магический метод __lt__, чтобы один вектор считался меньше другого, если его длина меньше.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1 / 2)

    def __lt__(self, other):
        if isinstance(other, Vector):
            return self.length() < other.length()
        return False


v1 = Vector(1, 2, 3)
v2 = Vector(2, 3, 4)
v3 = Vector(3, 4, 5)
print(v1 < v2)
print(v1 < v3)
print(v2 < v1)


# Реализуйте класс Book, который представляет собой книгу.
# Добавьте магический метод __le__, чтобы одна книга считалась меньше или равной другой,
# если ее год выпуска меньше или равен.

class Book:
    def __init__(self, year):
        self.year = year

    def __le__(self, other):
        if isinstance(other, Book):
            return self.year <= other.year
        return False


b1 = Book(1999)
b2 = Book(2000)
b3 = Book(2001)
print(b1 <= b2)
print(b2 <= b3)
print(b3 <= b1)


# Создайте класс Fraction, который представляет собой дробь.
# Реализуйте магический метод __ne__, чтобы две дроби считались неравными, если их числитель или знаменатель отличаются.

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __ne__(self, other):
        return self.a != other.a and self.b != other.b


f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
f3 = Fraction(2, 1)
print(f1 != f2)
print(f1 != f3)


# Вам необходимо создать класс Student с использованием декоратора dataclass и следующими полями:
# name (строка) - имя студента.
# age (целое число) - возраст студента.
# major (строка) - специальность студента.
# gpa (вещественное число) - средний балл студента.
# Также вам нужно реализовать метод calculate_grade, который будет принимать средний балл студента и возвращать его оценку:
# Если средний балл больше или равен 4.0, оценка будет "Отлично".
# Если средний балл больше или равен 3.0, оценка будет "Хорошо".
# Если средний балл больше или равен 2.0, оценка будет "Удовлетворительно".
# В остальных случаях оценка будет "Неудовлетворительно".

@dataclass
class Student:
    name: str
    age: int
    major: str
    gpa: float

    def calculate_grade(self):
        if self.gpa >= 4.0:
            return 'Отлично'
        if self.gpa >= 3.0:
            return 'Хорошо'
        if self.gpa >= 2.0:
            return 'Удовлетворительно'
        else:
            return 'Неудовлетворительно'


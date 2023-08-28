# Создайте класс "Сотрудник" (Employee) с атрибутами "имя" (name), "возраст" (age) и "зарплата" (salary).
# Добавьте метод "получить_информацию" (get_info), который будет выводить
# информацию о сотруднике (имя, возраст и зарплата).
import math


class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def get_info(self):
        print(f'{self.name} {self.age} : {self.salary}')


q = Employee('Alex', 20, 20000.15)
q.get_info()


# Создайте класс "Прямоугольник" (Rectangle) с атрибутами "длина" (length) и "ширина" (width).
# Добавьте метод "площадь" (area), который будет возвращать площадь прямоугольника,
# и метод "периметр" (perimeter),
# который будет возвращать периметр прямоугольника.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


a = Rectangle(2, 3)
print(a.area())
print(a.perimeter())


# Создайте класс "Круг" (Circle) с атрибутом "радиус" (radius). Добавьте метод "площадь" (area),
# который будет возвращать площадь круга, и метод "длина_окружности" (circumference),
# который будет возвращать длину окружности.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return math.pi * self.radius * 2


c = Circle(3)
print(c.area())
print(c.circumference())


# Создайте класс "Автомобиль" (Car) с атрибутами "марка" (brand), "модель" (model) и "год_выпуска" (year).
# Добавьте метод "описание" (description), который будет выводить
# полное описание автомобиля (марка, модель и год выпуска).

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        print(f'Марка:{self.brand}\nМодель:{self.model}\nГод выпуска: {self.year}')


car = Car('audi', 'a3', 2020)
car.description()


# Создайте класс "Банковский счет" (BankAccount) с атрибутами "владелец" (owner) и "баланс" (balance).
# Добавьте методы "пополнить" (deposit), который будет увеличивать баланс на определенную сумму,
# и "снять" (withdraw), который будет уменьшать баланс на определенную сумму.
# Также добавьте метод "получить_баланс" (get_balance), который будет возвращать текущий баланс.


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        self.balance += num

    def withdraw(self, num):
        self.balance -= num

    def get_balance(self):
        print(self.balance)


b = BankAccount('alex', 128)
b.get_balance()
b.deposit(100)
b.get_balance()
b.withdraw(200)
b.get_balance()

# Задача 1 Напишите функцию, которая принимает на вход список чисел
# и функцию для преобразования каждого числа в этом списке.
# Функция должна вернуть список,
# в котором каждое число преобразовано с использованием переданной функции.
def func1(a, operation):
    res = operation(a)
    return res


def multiply(a):
    return [i ** 2 for i in a]


# Задача 2 Напишите лямбда-функцию, которая принимает на вход число и возвращает его квадрат.
sq = lambda x: x ** 2


# Задача 3 Напишите функцию, которая принимает произвольное количество аргументов и возвращает их сумму.
# Функция должна уметь работать с разными типами аргументов (числа, строки, списки).
def func3(*args):
    # res_int = 0
    # res_str = ''
    # res_lst = []
    # if isinstance(args[0], int):
    #     for i in args:
    #         res_int += i
    #     return res_int
    # elif isinstance(args[0], str):
    #     for i in args:
    #         res_str += i
    #     return res_str
    #
    # elif isinstance(args[0], list):
    #     for i in args:
    #         res_lst += i
    #     return res_lst
    return sum(args)


# Задача 4 Напишите функцию, которая принимает на вход неопределенное количество именованных
# аргументов и возвращает словарь, содержащий только аргументы с четными значениями.
def func4(**kwargs):
    # res = {}
    # for key, value in kwargs.items():
    #     if value % 2 == 0:
    #         res[key] = value
    return {key: value for key, value in kwargs.items() if value % 2 == 0}


# Задача 5 Напишите функцию, которая сортирует словарь по длине его значений
def func5(d):
    return dict(sorted(d.items(), key=lambda x: len(x[1])))
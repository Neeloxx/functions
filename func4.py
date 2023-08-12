import datetime
import time
from functools import wraps


# Задача 1
# Создать декоратор, который вычисляет и выводит (через print) время работы декорируемой функции
# При каждом вызове декорируемой функции печатать имя функции и сколько она выполнялась.

def date_function(num):
    def wrapper1(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            time.sleep(num)
            res = func(*args, **kwargs)
            end_time = datetime.datetime.now()
            time_func = end_time - start_time
            print(time_func)
            print(func.__name__)
            return res

        return wrapper

    return wrapper1


@date_function(2)
def summa(a, b):
    return a + b


# print(summa.__name__)


print(summa(1, 2))


# Задача 2
# Изучить функцию wraps (from functools import wraps) и применить её к декоратору из прошлой задачи
def date_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        res = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        time_func = end_time - start_time
        print(time_func)
        print(func.__name__)
        return res

    return wrapper


@date_function
def summa(a, b):
    return a + b


print(summa.__name__)

# Задача 3
# Создать декоратор, оптимизирующий работу декорируемой функции (без аргументов).
# Декоратор должен сохранять результат работы функции на ближайшие 5 запусков и вместо выполнения функции возвращать сохранённый результат.
# После 5 запусков функция должна вызываться вновь, а результат работы функции — вновь кешироваться.
def cache_result(func):
    cache = func()
    counter = 0

    @wraps(func)
    def wrapper():
        nonlocal cache, counter
        if counter < 5:
            counter += 1
            return cache
        else:
            counter = 1
            cache = func()
            return cache

    return wrapper


@cache_result
def func_test():
    print("test")
    return 22


print(func_test())
print(func_test())
print(func_test())
print(func_test())
print(func_test())
print(func_test())
print(func_test())



# ---------------------------
#Задача 4
# Улучшить декоратор из предыдущей задачи (кеширование результата).
# Добавить возможность передавать кол-во запусков, которые будут закэшированы, как аргумент декоратора

def cache_result(size):
    def decorator(func):
        cache = func()
        counter = 0

        @wraps(func)
        def wrapper():
            nonlocal cache, counter
            if counter < size:
                counter += 1
                return cache
            else:
                counter = 1
                cache = func()
                return cache

        return wrapper

    return decorator


@cache_result(3)
def func_test():
    print('test')
    return 11


print(func_test())
print(func_test())
print(func_test())
print(func_test())
print(func_test())
print(func_test())
print(func_test())


# -----------------------
#Задача 5
# Улучшить декоратор из Задачи 4
# Добавить возможность кэшировать результат функции с аргументами.
def cache_result(size):
    def decorator(func):
        cache = None
        counter = 0

        @wraps(func)
        def wrapper(*args):
            nonlocal cache, counter
            if counter < size:
                counter += 1
                return cache
            else:
                counter = 1
                cache = {args: func(*args)}
                return cache

        return wrapper

    return decorator


@cache_result(3)
def func_test(a, b):
    print(f'Count... {a} + {b}')
    return a + b


print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
print(func_test(1, 2))
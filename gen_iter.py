# Напишите генератор, который будет возвращать все четные числа в заданном диапазоне.

def func1(l):
    for num in l:
        if num % 2 == 0:
            yield num


f = func1([1, 2, 3, 4, 5])
print(next(f))
print(next(f))


# Создайте итератор, который будет возвращать элементы
# последовательности Фибоначчи до определенного значения. Итератор должен останавливаться,
# когда очередное число превышает заданное значение.

class Fibiter:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


f = Fibiter(10000000)
print(iter(f))
print(next(f))
print(next(f))


# Напишите генератор, который будет возвращать все простые числа в заданном диапазоне.

def generator(n):
    for num in range(n + 1):
        if num > 1:
            for i in range(2, int(num / 2) + 1):
                if num % i == 0:
                    break
            else:
                yield num


g = generator(10)
for i in g:
    print(i)


# Создайте итератор, который будет возвращать элементы из двумерного списка построчно.
# Например, для списка [[1, 2], [3, 4], [5, 6]] итератор должен возвращать последовательность [1, 2, 3, 4, 5, 6].

class LineIter:
    def __init__(self, double_list):
        self.double_list = double_list
        self.current_row = 0
        self.current_col = 0
        self.result = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_row >= len(self.double_list):
            raise StopIteration

        current_element = self.double_list[self.current_row][self.current_col]
        self.result.append(current_element)
        self.current_col += 1

        if self.current_col >= len(self.double_list[self.current_row]):
            self.current_row += 1
            self.current_col = 0

        return self.result


dlist = [[1, 2], [3, 4], [5, 6]]
li = LineIter(dlist)
for e in li:
    print(e)


# Напишите генератор, который будет возвращать все подстроки заданной строки.
# Например, для строки "hello", генератор должен возвращать
# последовательность "h", "he", "hel", "hell", "hello", "e", "el", "ell", "ello", "l", "ll", "llo", "l", "lo", "o".

def sub_gen(s):
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            yield s[start:end]


string = "hello"
for substring in sub_gen(string):
    print(substring)


# Задача на итераторы:
# Создайте итератор, который будет возвращать элементы списка в обратном порядке.

class Backiter:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            element = self.lst[self.index]
            self.index -= 1
            return element
        else:
            raise StopIteration


lst = [1, 2, 3, 4]
bi = Backiter(lst)
for i in bi:
    print(i)

# Напишите генератор, который будет возвращать все перестановки заданного списка элементов.
# можно использовать функцию itertools.permutations


import itertools


def change_gen(lst_lst):
    for i in itertools.permutations(lst_lst):
        yield i


l = [1, 2, 3]
c = change_gen(l)
for i in c:
    print(i)

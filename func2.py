# 1. Поиск среднего значения элементов в массиве.
def func1(a):
    return sum(a) / len(a)


# 2. Проверка, является ли число простым.
def func2(a):
    d = 2
    while a % d != 0:
        d += 1
    return d == a


# 3. Нахождение самого длинного палиндрома в строке
def func3(s):
    res = ''

    def get_pal(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(len(s)):
        op1, op2 = get_pal(s, i, i), get_pal(s, i, i + 1)
        if len(op1) > len(res):
            res = op1
        if len(op2) > len(res):
            res = op2
    return res


# 4. Проверка, все ли элементы в массиве уникальны (не используя set)
def func4(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                return False
    return True


# 5. Поиск наибольшего общего делителя (НОД) двух чисел.
def func5(n1, n2):
    if n1 > n2:
        temp = n1
    else:
        temp = n2
    for i in range(1, temp + 1):
        if n1 % i == 0 and n2 % i == 0:
            nod = i
    return nod


# 6. Поиск наименьшего общего кратного (НОК) двух чисел.
def func6(n1, n2):
    if n1 > n2:
        temp = n1
    else:
        temp = n2

    while True:
        if temp % n1 == 0 and temp % n2 == 0:
            nok = temp
            break
        temp += 1
    return nok


# 7. Вычисление факториала числа.
def func7(n):
    if n == 1:
        return 1
    return func7(n - 1) * n


# 8. Поиск суммы цифр числа.
def func8(n):
    x = 0
    while n > 0:
        x += n % 10
        n //= 10
    return x

# 9. Вычисление первых N чисел Фибоначчи
def func9(n):
    arr = [0] * n
    arr[1] = 1
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr
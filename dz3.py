"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.

"""

n = input('Введите число: ')

n1 = n + n
n2 = n + n + n

print(int(n) + int(n1) + int(n2))

"""
Реализовать функцию ​ my_func()​ , которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    number = [a, b, c]
    number.remove(min(number))
    return sum(number)


print(my_func(30, 40, 10))

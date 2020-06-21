"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль
"""


def div(a, b):
    try:
        return round((a / b), 2)
    except ZeroDivisionError:
        return 'Правило математики - "На 0 делить нельзя"'


arg1 = int(input('Введите делимое: '))
arg2 = int(input('Введите делитель: '))

print(f'Результат деления:  {div(arg1, arg2)}')


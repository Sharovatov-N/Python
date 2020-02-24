"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать
явно, в программе.
"""
a = [1, 'my', False, (1, 5), {1, 6, 8}, {True: (1, 8), 7: 8}, [1, 6, 9], 5.8]

for n, i in enumerate(a, 1):
    print(n, f"{i} - {type(i)}")

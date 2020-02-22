"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
namber = int(input('Введите целое положительное число: '))

max_digit = namber % 10
namber = namber // 10

while namber > 0:
    if namber % 10 > max_digit:
        max_digit = namber % 10
    namber = namber // 10

print('Самая большая цифра в числе:', max_digit)

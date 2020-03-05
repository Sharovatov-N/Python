"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""

with open('file_1.txt', 'w') as my_f:
    while True:
        line = input('Введите текст \n')
        if line == '':
            break
        my_f.write(line + '\n')


with open('file_1.txt') as my_f:
    content = my_f.read()
    print(content)

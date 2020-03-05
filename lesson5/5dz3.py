"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""
with open('file_3.txt') as my_f:
    wages = []
    staff = []
    my_list = my_f.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            staff.append(i[0])
            wages.append(i[1])
print(f'Оклад меньше 20000\n{staff}\nСредний оклад - {round((sum(map(float, wages)) / len(wages)), 2)}')
"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""
el_count = int(input('Введите количество элементов списка: '))

users_list = []

for i in range(el_count):
    user_el = input(f'Введите элемент списка {i}: ')
    users_list.append(user_el)

print(f'Исходный список: {users_list}')

j = 0
for i in range((len(users_list) // 2)):
    users_list[j], users_list[j + 1] = users_list[j + 1], users_list[j]
    j += 2

print(f'Список после трансформации: {users_list}')

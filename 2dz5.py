"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с
тем же значением должен разместиться после них.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {my_list}')
rating = float(input('Введите Ваш рейтинг: '))
while True:
    for el in range(len(my_list)):
        if my_list[el] > rating > my_list[el + 1]:
            my_list.insert(el + 1, rating)
            break
        elif my_list[el] == rating:
            my_list.insert(el + 1, rating)
            break
        elif my_list[0] < rating:
            my_list.insert(0, rating)
        elif my_list[-1] > rating:
            my_list.append(rating)

    print(f'текущий список рейтинга - {my_list}')
    rating = float(input('Введите Ваш рейтинг: '))

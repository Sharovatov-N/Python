"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Реализовать вывод данных о
пользователе одной строкой.
"""


def personal_data(name, surname, year_of_birth, city_of_residence, email, phone):
    print(name, surname, year_of_birth, city_of_residence, email, phone)


personal_data(surname='Васечкин', name='Петя', year_of_birth='2019', email='123@mail.ru', phone=1234567890,
              city_of_residence='Москва')

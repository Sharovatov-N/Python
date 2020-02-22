"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в
формате чч:мм:сс. Используйте форматирование строк.
"""
number_seconds = int(input('Введите количество секунд: '))

seconds = number_seconds % 60
minutes = number_seconds // 60 % 60
hours = number_seconds // 3600
print("%02d"":""%02d"":""%02d" % (hours, minutes, seconds))
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
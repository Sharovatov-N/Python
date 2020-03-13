'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Textil(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def get_square(self):
        pass

class Coat(Textil):
    def __init__(self, quantity, size):
        self.quantity = quantity
        self.size = size

    @property
    def get_square_c(self):
        sum_c = round(self.quantity * (self.size / 6.5 + 0.5), 2)
        return f'Пальто:\nКоличество в заказе - {self.quantity}\nОбщий расход ткани - {sum_c}'

class Jacket(Textil):
    def __init__(self, quantity, height):
        self.quantity = quantity
        self.height = height

    @property
    def get_square_j(self):
        sum_j = round(self.quantity * (self.height * 2 + 0.3), 2)
        return f'Костюм:\nКоличество в заказе - {self.quantity}\nОбщий расход ткани - {sum_j}'


coat = Coat(2, 4)
jacket = Jacket(5, 2)
print(coat.get_square_c)
print(jacket.get_square_j)


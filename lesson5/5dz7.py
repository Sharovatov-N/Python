"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
profit = {}
ar = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as my_f:
    for line in my_f:
        name, firm, earning, damage = line.split()
        profit[name] = float(earning) - float(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    ar = {'average_profit': round(prof_aver)}
    print(f'Прибыль каждой компании - {profit}')
    final_list = [profit, ar]
    print(f'Итоговый список:\n{final_list}')

with open('file_7.json', 'w') as write_js:
    json.dump(final_list, write_js)

    js_str = json.dumps(final_list)
    print(f'Создан файл с расширением json со следующим содержимым:\n'
          f'{js_str}')

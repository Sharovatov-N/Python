"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
subj = {}
with open('file_6.txt') as my_f:
    for line in my_f:
        subject, lecture, practice, lab = line.split()
        lecture = 0 if lecture == '-' else lecture[:-4]
        practice = 0 if practice == '-' else practice[:-6]
        lab = 0 if lab == '-' else lab[:-8]
        subj[subject] = int(lecture) + int(practice) + int(lab)

print(f'Общее количество часов по предмету - \n {subj}')

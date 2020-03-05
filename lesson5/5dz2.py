"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
with open('file_2.txt') as my_f:
    line = 0
    number_words = 0
    for i in my_f:
        line += 1
        marker = 0
        word = 0
        for j in i:
            if j != ' ' and marker == 0:
                word += 1
                marker = 1
            elif j == ' ':
                marker = 0
        number_words = number_words + word
        print(f'{i} Кол-во слов в строке: {word} (Символов - {len(i)})')
print(f'Кол-во строк в файле - {line}\nКол-во слов в файле - {number_words}')

#Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать количество полученных элементов

import re
file = open('experience.txt')
values = file.read().split("\n")
data = []
for key in values:
    value = re.findall(r"[-+]?\.\d+|\d+", key) # получаем все возможные цифры с текствого файла
    if value != []:
        data.append(value)
def changing(matrix):   #изменяем матрицу в массив, чтобы получить точное кол-во всех элементов
    arr = [elem for el in matrix for elem in el]
    print(len(arr))

print(data)
changing(f'Всего элементов: {data}')




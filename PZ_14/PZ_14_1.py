#Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать количество полученных элементов

import re

with open('experience.txt', encoding='utf-8') as file:
    data = file.readlines()
datal = []

for key in data:
    value = re.findall(r"[-+]?\.\d+|\d+", key) # получаем все возможные цифры с текствого файла
    if value != []:
        datal.append(value)
def changing(matrix):   #изменяем матрицу в массив, чтобы получить точное кол-во всех элементов
    arr = [elem for el in matrix for elem in el]
    print('Общее кол-во элементов',len(arr))


changing(datal)




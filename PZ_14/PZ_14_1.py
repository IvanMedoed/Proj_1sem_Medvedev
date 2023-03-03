#Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать количество полученных элементов

import re

file = open('experience.txt')
values = file.read().split("\n")
data = []
for key in values:
    value = re.findall(r"[-+]?\.\d+|\d+", key) # получаем все возможные цифры с текствого файла
    if value != []:
        data.append(value)

data_new = [list(map(int, x)) for x in data] #переводим матрицу в тип инт
data_new[8].append(0)
print(data_new) #матрица исходных данных стажа работы

month = 0
year = 0
for i in data_new:
    month += i[1]
    year += i[0]

print(f'Стаж работы: {year} лет, {month} месяцев')




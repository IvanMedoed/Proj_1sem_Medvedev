#Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать количество полученных элементов

import re
import numpy as np
file = open('experience.txt')
values = file.read().split("\n")
data = []
for key in values:
    value = re.findall(r"[-+]?\.\d+|\d+", key)
    if value != []:
        data.append(value)

print(data)
data_new = [list(map(int, x)) for x in data]
data_new[8].append(0)
print(data_new)

def sumColumn(m):
    years = []
    for column in range(len(m[0])):
        t = 0
        for row in m:
            t += row[column]
        years.append(t)
        return years

print(sumColumn(data_new))

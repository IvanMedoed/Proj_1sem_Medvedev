# Дан словарь на 6 персон, найти и вывести их средний возраст(Пример {"Андрей": 32, "Виктор": 29, "Максим":18, ... }, среднее 26,33)
import math
ages = {"Андрей": 32, "Виктор": 29, "Максим":18, "Егор": 23, "Василий":33, "Антон": 23}
c = 0
sum = 0
for key in ages:
  c += 1
  sum += ages[key]
sred = sum/c
print('Средний возраст ', round(sred,2))

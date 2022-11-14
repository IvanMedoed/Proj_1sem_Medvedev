# Дан список размера N. Найти номера двух ближайших элементов из этого списка( то есть элементов с наименьшем модулем
# разности) и вывести эти номера в порядке возрастания
import random

N = int(input('Введите размер списка  =>'))
a = [random.randrange(1,100) for i in range(N)]

print('Spisok', a)
o_min = abs(a[0] - a[1])
i_min = 0
j_min = 1
for i in range(0, N-1):
  for j in range(i+1, N):
    b_tmp = abs(a[i] - a[j])
    if o_min > b_tmp:
      o_min = b_tmp
      i_min = i
      j_min = j
print(o_min)
print(i_min, ',', j_min)




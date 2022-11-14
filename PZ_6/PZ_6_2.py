# Дан список размера N. Найти номера двух ближайших элементов из этого списка( то есть элементов с наименьшем модулем
# разности) и вывести эти номера в порядке возрастания
import random
N = []
c=0
b = int(input('Введите размер списка  =>'))
while c < b:
  N.append(random.randint(0,b))
  c +=1

o_min = abs(N[0] - N[1])
i_min = 0
j_min = 1
for i in range(0, N-1):
  for j in range(i+1, N):
    b_tmp = abs(N[i] - N[j])
    if o_min > b_tmp:
      o_min = b_tmp
      i_min = i
      j_min = j
print(o_min)
print(N[i_min], '', N[j_min])




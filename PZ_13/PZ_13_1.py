#Сгенерировать матрицу на произвольное количество элементов, в которой задается преобразование от предыдущего элемента
# к следующему на произвольное значение
from functools import reduce
import random
mat = [[], []]
c = 0
for i in range(0, random.randint(3, 35)):
    mat[0].append(random.randint(0, 39))
    y = random.randint(0,39)
    print(y)
    b = reduce(lambda x,y: x + y, mat[0])
    mat[1].append(b)

print(mat)
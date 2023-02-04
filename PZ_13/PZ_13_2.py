#В матрице найти сумму элементов первых строк
import random
from functools import reduce


mat = [[], []]

for i in range(0, random.randint(3, 35)):
    mat[0].append(random.randint(0, 39))
    mat[1].append(random.randint(0, 40))

print(mat)
pin = reduce(lambda x, y: x + y, mat[0])
print(pin)
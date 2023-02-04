#Сгенерировать матрицу на произвольное количество элементов, в которой задается преобразование от предыдущего элемента
# к следующему на произвольное значение
import random
mat = [[], []]

for i in range(0, random.randint(3, 35)):
    mat[0].append(random.randint(0, 39))
    mat[1].append(random.randint(0, 40))
#Сгенерировать матрицу на произвольное количество элементов, в которой задается преобразование от предыдущего элемента
# к следующему на произвольное значение
import random
mat = [[], []]
y = []
for i in range(0, random.randint(3, 35)):
    mat[0].append(random.randint(0, 35))
    y.append(random.randint(0, 35))
    c = map(sum, zip(mat[0], y))
mat[1].append(list(c))
print(y)
print(mat[0])
print(mat)



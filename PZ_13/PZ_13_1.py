#Сгенерировать матрицу на произвольное количество элементов, в которой задается преобразование от предыдущего элемента
# к следующему на произвольное значение
import random
mat = [[], []]
y = []
for i in range(0, random.randint(0, 35)):
    mat[0].append(random.randint(0, 35))
    y.append(random.randint(0, 35))
    c = map(sum, zip(mat[0], y)) # первая строка матрицы суммируется с рандомными элементами
mat[1].append(list(c)) # Эти значения добавляет во вторую строку матрицу
print(mat[0]) #первая строка матрицы
print(y)
print(mat) # вся матрица



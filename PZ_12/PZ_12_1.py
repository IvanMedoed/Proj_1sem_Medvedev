#В последовательности на  n целых чисел умножить
a = list(map(int, input().split()))
min=a[0]
i_min=0
for i in range (len(a)):
    if a[i]<min:
        i_min=i
print([x * a[i_min] for x in a])
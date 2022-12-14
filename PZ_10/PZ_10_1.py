#Даны имена девочек. Определить, какие из этих имен встречаются в группах
# на всех вторых курсах,  какие есть только в некоторых группах и где не встречаются
# ни в одной из групп.
girllist = { 'Алина', 'Надежда', 'Анна', 'Елена', 'Ника', 'Нина',
             'София', 'Диана', 'Вера', 'Галя', 'Людмила', 'Дарья'}

x = {'Надежда', 'Анна', 'Елена', 'Ника'}
y = {'Анна', 'Людмила', 'Елена', 'София'}
z = {'Елена', 'Нина', 'Надежда', 'Диана' }
d = {'Диана', 'Елена', 'Людмила', 'Дарья'}

print("Во всем втором курсе встречаются имена: ", x & y & z & d)

print("В первой группе и третьей есть:", (x & z) - (y | d) )

print("В первой группе и второй есть:", (x & y) - (z | d) )

print("Во второй и четвертой группе есть:", (y & d) - (x | z) )

print("В третьей и четвертой есть:", (z & d) - (x | y) )

print("Ни в одной группе нет:", girllist - (x | y | z | d) )
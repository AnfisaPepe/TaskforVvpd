import random


c = 0
lst = []
m = int(input('Кол-во строк: '))
n = int(input("Кол-во столбцов: "))
for i in range(m):
    lst.append([])
    for j in range(n):
        lst[i].append(random.randint(-1000,1000))


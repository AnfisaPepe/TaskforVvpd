import random


c = 0
lst = []
m = int(input('Кол-во строк: '))
n = int(input("Кол-во столбцов: "))
for i in range(m):
    lst.append([])
    for j in range(n):
        lst[i].append(random.randint(-1000,1000))
for i in range(len(lst)):
    for j in range(1, len(lst[i])):
        if j < i and lst[i][j] < 0:
            c += 1
for i in range(len(lst)):
    print(lst[i])
print(c)

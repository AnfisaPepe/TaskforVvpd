import random


def change(lst):
    for g in range(len(lst)):
        if len(lst) == len(lst[g]):
            for i in range(len(lst)):
                for j in range(len(lst[i])):
                    if i != j:
                        lst[i][j] == lst[j][i]
            return lst
        else:
            print("Матрица должна быть квадратной")
            return lst


def createauto(m,n):
    lst = []
    for i in range(m):
        lst.append([])
        for j in range(n):
            lst[i].append(random.randint(-1000,1000))
    return lst


def massiv(lst):
    lstmx = []
    for i in range(len(lst)):
        mx = max([max(x) for x in lst[i]])
    for j in range(len(lst)):
        lstmx.append([])
        for g in range(len(lst[j])):
            lstmx[j].append(lst[j][g]/mx)
    return lstmx


def num_massiv(lst):
    lst_num = []
    for i in range(len(lst)):
        for j in lst[i]:
            if j == 10:
                lst_num.append(i)
    return lst_num


def createhands(m,n):
    lst = []
    for i in range(m):
        a = [int(a) for a in input().split()]
        if len(a) == n:
            lst.append(a)
        else:
            print("Введены некорректные данные")
            return []
    return lst


def menu1():
    lst1 = [1,2,3,4]
    lst2 = ['Создать массив',"Посмотреть имеющийся массив","Посмотреть функционал","Выход"]
    for i in range(len(lst1)):
        print(lst1[i],' - ',lst2[i])


def menu2():
    lst1 = [1, 2, 3]
    lst2 = ['Автоматически', "Вручную", "Назад"]
    for i in range(len(lst1)):
        print(lst1[i], ' - ', lst2[i])


def menu3():
    lst1 = [1, 2, 3, 4, 5, 6]
    lst2 = ['Получить новый массив путем деления всех элементов данного массива на ее больший по модулю элемент',
            "Вывести номера тех строк массива, в которых есть хотя бы один элемент, равный 10.",
            "Сделать функцию, меняющую местами элементы матрицы симметрично побочной диагонали",
            "Вычисление суммы тех положительных элементов двумерного массива А, которые стоят в строках, не содержащих нулевых элементов.",
            "Удалить из массива строку и столбец, на пересечении которых расположен минимальный элемент",
            "Назад"]
    for i in range(len(lst1)):
        print(lst1[i], ' - ', lst2[i])


def main():
    while True:
        try:
            menu1()
            answer = int(input('Введите номер: '))
            match answer:
                case 1:
                    m = int(input('Кол-во строк: '))
                    n = int(input("Кол-во столбцов: "))
                    menu2()
                    ans = int(input('Как вы хотите создать массив: '))
                    match ans:
                        case 1:
                            lst = createauto(m,n)
                        case 2:
                            lst = createhands(m,n)
                case 2:
                    for i in range(len(lst)):
                        print(lst[i])
                case 3:
                    print('Доступные функции')
                    menu3()
                    main3(lst)
                case 4:
                    break
        except ValueError:
            print('Некорректные данные')
            continue


def main3(lst):
    while True:
        ans = int(input())
        match ans:
            case 1:
                lstmx =massiv(lst)
                print(lstmx)
            case 2:
                lst_num=num_massiv(lst)
                print(lst_num)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                 break
if __name__ == '__main__':
    main()
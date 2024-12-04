import random


def createauto(m,n):
    lst = []
    for i in range(m):
        lst.append([])
        for j in range(n):
            lst[i].append(random.randint(-1000,1000))
    return lst


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
    lst1 = [1, 2, 3, 4,5]
    lst2 = ['Получить новый массив путем деления всех элементов данного массива на ее больший по модулю элемент',
            "Вывести номера тех строк массива, в которых есть хотя бы один элемент, равный 10.",
            "Сделать функцию, меняющую местами элементы матрицы симметрично побочной диагонали",
            "Составить программу вычисления суммы тех положительных элементов двумерного массива А, которые стоят в строках, не содержащих нулевых элементов.",
            "Удалить из массива строку и столбец, на пересечении которых расположен минимальный элемент."]
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
                    main3()
                case 4:
                    break
        except ValueError:
            print('Некорректные данные')
            continue


def main3():
    while True:
        ans = int(input())
        match ans:
            case 1:
                pass

if __name__ == '__main__':
    main()
from cosx import *


def main():
    while True:
        try:
            x = float(input('Введите желаемый x(n = 100): '))
            print(f'1 - Вывести cos({x})')
            print(f'2 - Вывести ch({x})')
            print(f'3 - Вывести (1-{x})^m')
            ans = int(input('Какую операцию вы хотите воспроизвести: '))
            match ans:
                case 1:
                    cosx = cos(x)
                    print(cosx)
                case 2:
                    chx = ch(x)
                    print(chx)
                case 3:
                    if -1 < x < 1:
                        m = int(input("Введите параметр m: "))
                        c = pow((1-x),m)
                        print(c)
                    else:
                        print('x должен входить в диапозон (-1,1)')
                        continue
        except ValueError:
            print('Некорректные данные')
            continue

if __name__ == '__main__':
    main()
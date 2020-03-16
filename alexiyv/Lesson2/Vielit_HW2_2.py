# coding: utf-8
from random import randint

more = 'y'
while more.lower()[0] == 'y' or more.lower()[0] == 'o':
    print(f'Загадано число в диапазоне от 1 до 100\nВам нужно его угадать!')
    x = randint(1, 100)
    #print(x)
    bingo = 0
    count = 0
    while bingo != 1:
        y = int(input('Введите ваше число: '))
        if y > x:
            print('Введенное число больше искомого')
            count += 1
        elif y < x:
            print('Введенное число меньше искомого')
            count += 1
        else:
            bingo = 1
            count += 1
    print(f'Вы угадали число за {count} попыток')
    more = input('Хотите сыграть еще? (y/n): ')
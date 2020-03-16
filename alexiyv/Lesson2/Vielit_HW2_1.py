# coding: utf-8
import math

#----------------Start first---------------------------
x = abs(int(input('Введите число: ')))
if not (x%2): print('Вы ввели четное число')
else: print('Вы ввели нечетное число')

#----------------Stdrt second---------------------------
x = abs(int(input('Введите число: ')))
if (x%2) and not (x%3) and not (x%5) and (x%9): print('Вы ввели нечетное число, которое одновременно делится на 3 и 5 без остатка, но не делится на 9')
elif not (x%2): print('Вы ввели четное число')
elif not (x%3) and not (x%5): print('Вы ввели нечетное число, которое одновременно делится на 3 и 5 без остатка, но так же делится и на 9')

#----------------Stdrt third---------------------------
x = abs(int(input('Введите число: ')))
res = str()
for i in range(1, math.ceil(math.sqrt(x))+3):
    if not (x%i): res += str(i)+ " "
print ('Делители введенного числа: ', res)

#----------------Stdrt fourth---------------------------
x = abs(int(input('Введите число: ')))
count = 0
while x:
    count+=1
    y=x%10
    x=int((x-y)/10)
    print (f'Число {count}-го разряда: ', y)
    res = str()
    for i in range(1, 10):
        if not (y%i): res += str(i)+ " "
    print ('Делители данного числа: ', res)    
print (f'Всего число имеет {count} разряд(а/ов)')
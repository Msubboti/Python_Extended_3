# coding: utf-8
from random import randint
from math import sqrt
import itertools

# ------------------------- 1 ---------------------------
'''
s = "Canada, Belgium, Afghanistan, Algeria, Antigua and Barbuda, Burundi, Cook Islands, Egypt, Germany, Japan, Ukrain"
s1 = 'Welcome to California!'
l_c = s.split(', ')
for cont in l_c:
    print(s1[:s1.find("C")]+cont)
'''
# ------------------------- 2 ---------------------------
'''
n = ["Mary", "Max", "Lera", "Alex", "Anton"]
sn = ["Gray", "Black", "Green", "McFly", "Stone"]
l1 = [n[randint(0,4)]+ ' ' + sn[randint(0,4)] for i in range(50)]
#while i<=50:
    #l1.append(n[randint(0,4)]+ ' ' + sn[randint(0,4)])
    #i +=1    
print(l1)
l2 = l1.copy()
count_test = 0 # ---- test for right result 
for name in l1:
    count = 0
    i = 0
    x = len(l2)
    while i<x:
        if name == l2[i]:
            count += 1
            l2.pop(i)
            i -= 1 # ---- for not skipped l2 items after pop element
            x -= 1 
        i +=1
        #
    if count !=0:
        print (name + f' Встречается {count} раз')
        count_test += count
print(count_test)
'''
# ------------------------- 2 I think this is Python-style :)---------------------------
'''
n = ["Mary", "Max", "Lera", "Alex", "Anton"]
sn = ["Gray", "Black", "Green", "McFly", "Stone"]
l1 = [n[randint(0,4)]+ ' ' + sn[randint(0,4)] for i in range(50)]
print(l1)
l2 = [[name, l1.count(name)] for name in list(set(l1))]
#test_count = 0
for i in range(len(l2)):
    print (l2[i][0] + f' Встречается {l2[i][1]} раз')
    test_count += l2[i][1]
#print(test_count)
'''
# ------------------------- 3 ---------------------------
'''
kub = [x**3 for x in range(20) if x%2]
print(kub)
'''
# ------------------------- 4 ---------------------------
'''
len_list = 10
distance = [randint(100,1000) for x in range(len_list)]
time = [randint(10,100) for x in range(len_list)]
speed = [round(distance[x]/time[x],2) for x in range(len_list)]
#---- part for debug ----
#s_dist = sum(distance)
#s_time = sum(time)
#s_speed = sum(speed)
#print (str(s_dist)+ ' ' +str(s_time)+ ' ' +str(s_speed))
#middle_speed = round(sum(distance)/sum(time),2) #---- I know this isn`t right

middle_speed = round(sum(speed)/len_list,2)
above_middle_speed = [ams for ams in speed if ams > middle_speed]
for i in range(len_list):
    print(f'Расстояние: {distance[i]}m, затраченное время: {time[i]}s, скорость {speed[i]}m/s')
print(f'Средняя скорость: {middle_speed}m/s')
print(f'Скорости, превысившие среднюю скорость: {above_middle_speed}')
'''
# ------------------------- Simple 1 ---------------------------
'''
x = input('Введите первое число: ')
y = input('Введите второе число: ')
if x>y: print('Первое число больше второго')
elif x<y: print('Второе число больше первого')
else: print('Числа равны')
'''
# ------------------------- Simple 2 ---------------------------
'''
x = input('Введите массив чисел через пробел: ')
l = x.split(' ')
print(l)
l1 = sorted(l)
print(l1)
'''
# ------------------------- Simple 3 ---------------------------
'''
z = 0
x = int(input('Введите числo: '))
for y in range(2,int(sqrt(x))+3):
    if not(x%y):
        z = 1
        break
if not z:print('Число простое')
else:print('Попробуйте какое-нибудь другое число')
'''
# ------------------------- Simple 4 ---------------------------
'''
l = [randint(1,100) for i in range(25)]
print(l)
for x in l:
    if x%2 and not x%3:print(x)
'''
# ------------------------- Simple 5 ---------------------------
'''
l = int(input('Введите число: '))
#l = [randint(1,100) for i in range(25)] #---not nesessery to input number each time
#print(l)
x = l
#for x in l:
if 10<x<=90 and x%2 and x%7:print(x)
'''
# ------------------------- Lists 6 ---------------------------
'''
l = [randint(1,100) for i in range(25)]
print(l)
x = int(input('Введите числo: '))
res = [i for i in l if i==x]
if res:
    print(res)
else:
    print('Нет такого числа')
'''
# ------------------------- Lists 7 ---------------------------
'''
x = 0
l = []
while x <= 1000:
    x = int(input('Введите числo: '))
    if x<=1000:l.append(x)
print(sum(l))
'''
# ------------------------- Lists 7-1 ---------------------------
'''
x = (int(input('Введите числo: ')) for i in itertools.count())
y = next(x)
l = []
while y<=1000:
    l.append(y)
    y = next(x)
print(sum(l))
'''
# ------------------------- Lists 8 ---------------------------
'''
#l = [randint(1,100) for i in range(25)]
#print(l)
l1 = [l*2 for l in [randint(1,100) for i in range(25)]]
print(l1)
'''
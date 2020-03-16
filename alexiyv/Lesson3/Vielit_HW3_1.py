# coding: utf-8

#---------------Start first---------------
#'''
from random import randint
#-----Cycle "FOR"---------
l = [randint(1,9) for i in range(randint(10,30))]
s = 0
for i in range(len(l)):
    s += l[i]
print(str(l) + '\n' + str(s))
#-----Cycle "WHILE"---------
l = []
for i in range(randint(10,30)):
    l.append(randint(1,9))
s = 0
i = 0
while i < len(l):
    s += l[i]
    i += 1
print(str(l) + '\n' + str(s))
#'''
#---------------Start second--------------
#'''
import sys
filename = sys.argv[0]
f = open(filename, 'r')
l = []
for line in f:
    l.append(line)
x = len(l)
for i in range(x):
    print(l[i], end="")
#'''
#---------------Start third---------------   
#'''
import sys
filename = sys.argv[0]
f = open(filename, 'r')
l = [line for line in f]
#l.reverse() - reverse all list in memory is use more system resorses, I think... If list is realy BIG
x = len(l)
for i in reversed(range(x)):
    print(l[i], end="")
#'''
#---------------Start fourth---------------
#'''
x = int(input('Введите сумму, которую желаете получить: '))
nominal = [1000,500,200,100,50,20,10,5,2,1]
i = 0
while x>0:
    n=x//nominal[i]
    print(f'Номиналом {nominal[i]} Вы получите {n} купюр')
    x -= n*nominal[i]
    i +=1
#'''

#---------------Start fifth---------------   
#'''
x = int(input('Введите сумму, которую желаете получить: '))
nominal = [1000,500,200,100,50,20,10,5,2,1] # for clarity and better understanding
nominal.reverse()
i = 0
z = 10 #max quantity of banknots
l_n = len(nominal)
my_output = []
while x>0:
    while i<=l_n:
        while z>=1:
            n = x-z*nominal[i]
            if i==l_n-1 or n<=0:
                my_output.append('Номиналом ' +str(nominal[i])+' Вы получите ' +str(x//nominal[i])+ ' купюр\n')
                x = 0
                i = l_n+1
                z = 0
            elif not(n%nominal[i+1]):
                my_output.append('Номиналом ' +str(nominal[i])+' Вы получите ' +str(z)+ ' купюр')
                x -= z*nominal[i]
                z = 0
                i += 1
            z-=1
        z=10
if x!=0: print('Мы не можем выдать требуемую сумму')
else: 
    for out in my_output: print(out)
#--------------Test for right work of my programm-----------
res = 0
for line in my_output:
    temp = line.split()
    nom = int(temp[1])
    q_ty = int(temp[4])
    res += nom*q_ty
print(f'Запрошенная Вами сумма: {res}')

#'''   
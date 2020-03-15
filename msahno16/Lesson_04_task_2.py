import sys
import random
from random import randrange
N=open('nums1.txt', 'w')
N.close 
n_1=[i for i in range (1, 40) if i <11 and not i%2==0]
n_2=[i for i in range (1, 40) if i %2==0]
n_3=[i for i in range (1, 40) if i >11]
for j in range(21):
    x=randrange(len(n_1))
    y=randrange(len(n_2))
    z= randrange(len(n_3))
    res='%s %s %s' %(n_1[x], n_2[y], n_3[z])
    #print(res)
    N=open('nums1.txt', 'a')
    N.write(res + '\n')      
N.close

s=1
F=open('fizz_buzz.txt', 'w')
F.close 
while s:
    F_B=str()
    file = open('nums1.txt', mode='r', encoding='utf-8-sig')
    print('Введите номер строки')
    q=int(input())
    if q<=20:
        q-=1
        f=file.readlines()[q]
        p=f.split(' ')
        fizz=int(p[0])
        buzz=int(p[1])
        n=int(p[2])
        F_B+=('Числа в строке № %s : %s, %s, %s\n--Результат:'%(q+1, fizz, buzz, n))
        for i in range(1, n):
            if not i%fizz and not i%buzz:
                F_B+='FB '
            elif not i%fizz:
                F_B+='F '
            elif not i%buzz:
                F_B+='B '
            else:
                F_B+=str(i)+' '
        print(F_B)
        F=open('fizz_buzz.txt', 'a')
        F.write(F_B + '\n')
    else:
        F.write('На этом всё!\nДо скорых встреч!')
        print('На этом всё!\nДо скорых встреч!')
        break

    
        

    
F.close()   






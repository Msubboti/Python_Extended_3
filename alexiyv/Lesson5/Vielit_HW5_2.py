# coding: utf-8
from random import randint

def fbn(f_b_n): #---return string with FizzBuzz
    result = str()
    for i in range(1, int(f_b_n[2])+1):
        if not (i%int(f_b_n[0])) and not (i%int(f_b_n[1])): result += 'FB '
        elif not (i%int(f_b_n[0])): result += 'F '
        elif not (i%int(f_b_n[1])): result += 'B '
        else: result += str(i)+' '
    return result

def gen_fbn():
    fizz = randint(2, 9)
    buzz = randint(2, 9)    
    while (fizz == buzz):
        fizz = randint(2, 9)
        buzz = randint(2, 9)
    max_number = randint(10, 50)
    fbn = str(fizz)+' '+str(buzz)+' '+str(max_number)+'\n'
    return fbn

# ------------------------- Working with file and functions ---------------------------
'''
with open("f1.txt", 'w') as file_first:
    for i in range(20):
        file_first.write(gen_fbn())

with open("f1.txt", 'r') as file_first:
    with open("f2.txt", 'w') as file_sec:
        for line in file_first:
            res = fbn(line.split())
            print(line, end='')
            print(res, end='\n\n')
            file_sec.write(line + res + '\n\n')
'''
# ------------------------- Working with lists and map ---------------------------
#'''
n = int(input('Сколько наборов чисел, для которых нужно посчитать FizzBuzz, Вы хотите получить: '))
l1 = [gen_fbn().split() for i in range(n)]
#print(l1)
l2 = list(map(fbn, l1))
#print(l2)
for i in range(n):
    print(str(l1[i])+'\n'+ l2[i]+'\n')
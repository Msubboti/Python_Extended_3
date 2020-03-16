# coding: utf-8
from math import sqrt
from random import randint
#------------------------- 1 -------------------------------
'''
def up_s(s):
    return s.upper()

def down_s(s):
    return s.lower()

str1 = ['askjdhhkjasd', 'jksfhjkhfdugu', 'ASFFjjhjhGHY', 'AsDfGhJkL']
str1_up = list(map(up_s, str1))
str1_dn = list(map(down_s, str1))
print(str1)
print(str1_up)
print(str1_dn)
'''
#------------------------- 2 -------------------------------
'''
def square(n):
    z = False
    for y in range(2,int(sqrt(n))+1):
        if not(n%y):
            z = True
            break            
    if not z:return n**2
    else:return n    

num_l = [randint(1,100) for i in range(25)]
num_l1 = list(map(square, num_l))
print(num_l)
print(num_l1)
'''
#------------------------- 3 -------------------------------
'''
def rep(xxx):
    res = xxx.replace(',', '')
    res = res.replace('.', '')
    res = res.replace(' ', '')
    res = res.replace('-', '')
    res = res.replace('!', '')
    res = res.replace(':', '')
    return res
    
my_file = open("A_Fishy_Story-Clare_West.txt", 'r')
l1 = [list(map(rep,line.split(sep=None))) for line in my_file ]
my_file.close()
l2 = [item for line in l1 for item in line]
#print(l1)
#print(l2)
l3 = [[name, l2.count(name)] for name in sorted(list(set(l2)))]
for i in range(len(l3)):
    print (f'Слово {l3[i][0]} встречается {l3[i][1]} раз')
'''
#------------------------- 3-1 -------------------------------
#------- The different method of work with *.txt file --------
#------- Makeing list of words from file in one step ---------
def rep(xxx):
    res = xxx.replace(',', '')
    res = res.rstrip('.') #--- In some cases this .rstrip that should del '.' on end of word isn`t work
    res = res.rstrip("'")
    res = res.lstrip("'")
    res = res.rstrip('-')
    res = res.lstrip('-')
    res = res.rstrip('!')
    res = res.rstrip('?')
    res = res.rstrip(':')
    res = res.rstrip(';')
    return res
    
my_file = open("A_Fishy_Story-Clare_West.txt", 'r')
l1 = list(map(rep, my_file.read().split()))
my_file.close()
#print(l1)
l2 = [[name, l1.count(name)] for name in sorted(list(set(l1)))]
for i in range(len(l2)):
    print (f'Слово {l2[i][0]} встречается {l2[i][1]} раз')
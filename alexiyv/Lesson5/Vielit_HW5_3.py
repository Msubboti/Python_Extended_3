# coding: utf-8
import random, string

def my_zip(list1, list2, act):
    res = act(list1, list2)
    return res

def min_len_list(*args):
    return len(sorted(args, key=len)[0])

def make_dict(a,b): 
    res = dict([a[i],b[i]] for i in range(min_len_list(a,b)))
    return res
    
def make_list(a,b):
    res = [[a[i],b[i]] for i in range(min_len_list(a,b))]
    return res    
    
def make_tuple(a,b):
    res = [(a[i],b[i]) for i in range(min_len_list(a,b))]
    return res    
    
n1 = int(input('Kакой длины генерировать первый список: '))
n2 = int(input('Kакой длины генерировать второй список: '))
my_act = int(input('В каком виде хотите получить результат работы моей ZIP-функции:\n'
                   '1-словарь\n'
                   '2-список\n'
                   '3-кортеж\n'
                   '--------> '))
act_dic = {
          1: make_dict,
          2: make_list,
          3: make_tuple
          }

l1 = [random.randint(1, 100) for i in range(n1)]
l2 = list()
while len(l2) < n2:
    l2.append(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
print(l1)
print(l2)
print(my_zip(l1,l2,act_dic[my_act]))
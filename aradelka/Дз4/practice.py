import random
import math

###### 1


countries = 'Oz,Narnia,Middle Earth,Westeros'
greetings = 'Welcome to California!'

countries_l = countries.split(',')
print(countries_l)

g = greetings[:-11]

for i in countries_l:
    print(g +str(i)+'!')
print()

####### 3


l = list(range(1, 11))

print(l)

c = [a**3 for a in l if a%2 != 0]
print(c)
print()
######### 2

n = ['Mary', 'Max', 'Lera', 'Alex', 'Anton']
s = ['Grey', 'Black', "Green", 'McFly', 'Stone']

ns = []
i = 0

while i < 26:
    r_num1 = random.randint(0, 4)
    r_num2 = random.randint(0, 4)
    a = n[r_num1]
    b = s[r_num2]
    ns.append(a + ' ' + b)
    i += 1
print(ns)

ns1 = list(set(ns))

for i in ns1:
    k = 0
    for j in ns:
        #while j >= i:
            #if ns[i] == ns1[j]:
        if i == j:
            k += 1
            #ns1.remove(j)
    print(f'{i}: {k}')

print()
########## 4
#Даны два списка по 10 элементов: расстояния и затраченное время.
# При помощи list comprehensions вывести скорости, превысившие среднюю.

S = [1, 2, 32, 43, 44, 60, 75, 95, 97, 99]
t = [8, 20, 28, 32, 38, 64, 71, 87, 90, 98]
V = []

for i in range(0, 9):
    v = S[i]/t[i]
    V.append(v)
print(V)

AV = [v for v in V if v > (sum(V)/10)]
print(AV)
print()

########### 5
#Ввести два целых числа, вывести большее из них.

a = int(input('a = '))
b = int(input('b = '))

c = a/b

if c > 1:
    print('a')
elif c < 1:
    print('b')
else:
    print('a = b')

print(max(a, b))
print()

############## 6 Ввести три целых числа, вывести их по возрастанию.

numbers = input()
numbers = numbers.split()

n_l = [int(n) for n in numbers]
n_l = sorted(n_l)
n_l1 = [str(n) for n in n_l]
print(' '.join(n_l1))

print()


####################
# Ввести целое число, вывести, являестя ли это число простым
p = int(input('p = '))

if p == 1:
    print(str(p)+' is not a prime number.')
if p == 2:
    print(str(p) + ' is a prime number.')
else:
    for i in range(2, math.ceil(math.sqrt(p)) + 1):
        if p % i != 0:
            print(str(p)+' is a prime number.')
            break
        else:
            print(str(p) + ' is not a prime number.')
            break
# else:
#     m = 2
#     while m < math.ceil(math.sqrt(p)) + 1 and p % m != 0:
#         m += 1
#     print(str(p) + ' is a prime number.')

print()

####### Вводить целые числа. Выводить только те, которые являются нечетными и кратными трем.

nums = input('Enter five numbers: ')
nums = nums.split()

N = [int(n) for n in nums]
NN = [str(n) for n in N if n % 2 != 0 and n % 3 == 0]

print(' '.join(NN))
print()

########Ввести целое число от 1 до 100 включая,
# вывести это число, только при условии,
# что оно больше 10 и меньше или равно 90 !!!одним!!! условием (10 < x <= 90), нечетное и не кратно семи.

x = int(input('Enter the number: '))

if x % 2 !=0 and 10 < x <= 90 and x % 7 !=0:
    print(x)
else:
    print('Bad number')
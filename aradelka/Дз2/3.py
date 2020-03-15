import math

num = int(input("Enter a number: "))
l = list()

for i in range(1, math.ceil((math.sqrt(num)))+1):
    if num % i == 0:
        l.append(i)
        l.append(int(num/i))

l = list(set(l))
l.sort()
print('All dividers:'+str(l))

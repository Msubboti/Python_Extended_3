import random

###1

def up(s):
    return str(s).upper()

s = input()
print(up(s))

def low(s):
    return s.lower()

print(low(s))

s1 = ['qw', 'er', 'dF', 'gF']
s2 = ['FG', 'YT', 'Hf']

l = list(map(up, s1))
print(l)
print(list(map(low, s2)))

####2

x = random.randint(2, 100)

print(x)

def prime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return 0
            #break
        i += 1
    else:
        return x*x
    
print(prime(x))


lst = [random.randint(0, 20) for i in range(20)]
print(lst)

lst2 = list(map(prime, lst))
lst3 = [l for l in lst2 if l != 0 and l != 1]

print(lst3)
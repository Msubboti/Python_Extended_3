import math

b = 1
def square(num):
    return num**2
def ud(num):
    return (num%num + num%b)
a = [1, 2, 3, 4, 5, 12, 15, 30]
sqr = list(map(square, a))
c = list(map(ud, a))

 
         


for element in a:
    i = range(1, 100)
    g = element % i
    if g < 2 and g == 0:
       sqr = list(map(square, a))
    print(sqr)



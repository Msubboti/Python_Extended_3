#Зная значение n! (n! = 1 * 2 * ... * (n - 1) * n), определите значение n.

def fact(m):
    n = 1
    i = 1
    while m > 1 and n != m:
        n *= i
        i += 1
    if m <= 1:
        return 1
    else:
        return i-1


f = int(input('enter Fizz:' ' '))
b = int(input('enter Buzz:' ' '))
n = int(input('enter Number:' ' '))
FB = list(map(lambda x: 'Fizz'*(x % f == 0) + 'Buzz'*(x % b == 0) or x, range(1, n)))
print(FB)




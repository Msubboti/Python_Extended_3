numbers = input()
numbers = numbers.split()

fizz = int(numbers[0])
buzz = int(numbers[1])
third = int(numbers[2])

l = []

for i in range(1, third+1):
    if i % fizz == 0 and i % buzz == 0:
        l.append('FB')

    elif i % fizz == 0:
        l.append('F')

    elif i % buzz == 0:
        l.append('B')

    else:
        l.append(i)

for i in l:
    print(i, end=' ')

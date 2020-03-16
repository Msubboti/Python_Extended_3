# coding: utf-8
from random import randint

file_first = open("f1.txt", 'w')
fizz = int()
buzz = int()
for i in range(20):
    fizz = randint(1, 9)
    buzz = randint(1, 9)    
    while (fizz == buzz):
        fizz = randint(1, 9)
        buzz = randint(1, 9)
    max_nember = randint(10, 50)
    file_first.write(str(fizz) + ' ' + str(buzz) + ' ' + str(max_nember) + '\n')
file_first.close()

file_first = open("f1.txt", 'r')
file_second = open("f2.txt", 'w')
for line in file_first:
    fbn = line.split()
    fizz = int(fbn[0])
    buzz = int(fbn[1])
    max_number = int(fbn[2])
    result = str()
    for i in range(1, max_number+1):
        if not (i%fizz) and not (i%buzz): result += 'FB '
        elif not (i%fizz): result += 'F '
        elif not (i%buzz): result += 'B '
        else: result += str(i)+' '
    print (line, end='')
    print (result)
    file_second.write(line + result + '\n\n')

file_first.close()
file_second.close()
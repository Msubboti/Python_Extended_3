# coding: utf-8
from random import randint

file_first = open("f1.txt", 'w')
fbn = [[randint(1, 9),randint(1, 9),randint(10, 50)] for i in range(10)]
print(fbn)
for x in range(10):
    l1 = [
          'FB' if not i%fbn[x][0] and not i%fbn[x][1] else 'F' if not (i%fbn[x][0]) else 'B' if not (i%fbn[x][1]) else i
          for i in range(1, fbn[x][2]+1)
         ]
    print(l1)
    file_first.write(str(fbn[x]) + '\n' + str(l1) + '\n')

import sys
filename = sys.argv[0]
f = open(filename, 'r')
for line in f:
    print(line)
f.close()

import sys
filename = sys.argv[0]
f = open(filename, 'r')
sum=''
for line in f:
    sum+=line  
f.close()
print(sum[::-1])
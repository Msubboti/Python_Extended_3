num = input()
#
a = int(num)
k = 0

while a != 0:
    print('{} * 10^{}'.format(a % 10, k))
    k += 1
    a = int(a / 10)
print()
#
k = 0
for i in num[::-1]:
    print('{} * 10^{}'.format(i, k))
    k += 1

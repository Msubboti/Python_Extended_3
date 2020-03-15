from random import randint as ran
# bubble sorting
l = []
for x in range(10):
    l.append(ran(1, 70))
print(l)

for i in range(10 - 1):
    for j in range(10 - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print(l)
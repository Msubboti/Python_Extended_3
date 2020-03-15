# 6. Подготовить в программе список целых чисел.
# Ввести число, вывести в консоль ответ,
# встречается такое число в списке или нет.
# Использовать встроенную функцию.


from random import randint
lst = [randint(0, 20) for i in range(20)]

#print(lst)

x = int(input('Enter the number: '))

if x in lst:
    print('Yes')
else:
    print('No')
print()

# 7. Вводить целые числа, добавлять их в список.
# Как только будет введено число больше 1000, перестать вводить число и
# вывести сумму всех введенных чисел, среднее число, максимальное и минимальное.
# Использовать встроенные функции, сумму руками не писать.

numbers = []

n = int(input('Enter the number: '))

while n < 1000+1:
    numbers.append(n)
    n = int(input('Enter the number: '))

print(numbers)

s = sum(numbers)
an = s / len(numbers)
m = min(numbers)
M = max(numbers)

#print(s, an, m, M)

print(f'''Sum of numbers: {s},
Avarage number: {an},
minimal: {m},
maximal: {M}
''')

# 8. Ввести список чисел, вывести список удовенных чисел,
# созданый при помощи List Comprehensions.

l = input('Enter the numbers: ')
l = l.split()
print(l)

l1 = [2*int(ll) for ll in l]
print(l1)
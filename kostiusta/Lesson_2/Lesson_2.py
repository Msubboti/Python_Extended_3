# Задание 1
    
    # Проверить, является ли введеное число четным
print('Enter your number please:')
a=int(input())
if not(a%2):
    print(a,'even number')

    # Проверить, является ли число нечетным, делится ли на три и на пять одновременно, но так, чтобы не делиться на 10
print('Enter your number please:')
a=int(input())
if a%2 and not(a%3) and not(a%5) and a%10:
    print(a,'correct number')

    # Ввести число, вывести все его делители
print('Enter your number please:')
a=int(input())
print('The factors of',a,'are:')
for i in range(1,a+1):
    if not(a%i):
        print(i)

    # Ввести число, вывести его разряды и их множители
print('Enter your number please:')
a=int(input())
dozen = a//10
unit=a%10
if dozen>0:
    print('Your number contains',dozen,'dozen and',unit,'units')
else: 
    print('Your number contains 0 dozen and',a,'units')

# Задание 2
   
    #Придумать свои собственные примеры на альтернативные варианты if и активное использование булевой алгебры.
    # 1. Вывести большее число
a=int(input())
b=int(input())
if a==b:
    print('Числа равные')
elif a>b:
    print(a, 'большее число')
else:
    print(b, 'большее число')

    # 2. Определить високосный год или нет
year=int(input())
if not(year%4):
    print('Год высокосный')
elif year%100:
    if year%400:
        print('Год не высокосный')
    else:
        print('Год высокосный')
else:
    print('Год не высокосный')
        

    # Задание 3
        #У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz. 
        #До третьего необходимо досчитать от единицы. Считая, надо выводить число. 
        #Если число кратно fizz - надо выводить F вместо числа. Если число кратно buzz - надо выводить B вместо числа. 
        #Если число кратно и fizz и buzz, надо выводить FB. И так - пока не будет достигнуто третье введенное число.
print('Enter Fizz number please:')
f=int(input())  # Fizz number
print('Enter Buzz number please:')
b=int(input())  # Buzz number
print('Enter Third number please:')
t=int(input())  # Third number
for i in range(1,t+1):
    if not (i%f) and not (i%b):
        i='FB'
    elif not (i%b):
        i='B'
    elif not (i%f):
        i='F'
    print(i)
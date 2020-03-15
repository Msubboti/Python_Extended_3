#Проверить, является ли число нечетным, делится ли на три и на пять одновременно, но так, чтобы не делилось на 9.


num = int(input("Enter a number: "))

if num % 2 != 0 \
    and num % 3 == 0 \
    and num % 5 == 0 \
    and num % 9 != 0:
    print(str(num) + ' is right number!')
else:
    print(str(num) + ' is not right number :(')



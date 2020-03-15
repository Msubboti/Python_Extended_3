import random

number = random.randint(0, 100)
print(number)

div = int(input('Guess the divider: '))

while number < div:
    print('The guess is too big.')
    div = int(input('Guess the divider: '))
else:
    while number % div != 0:
         print('No, it`s not. Try again!')
         div = int(input('Guess the divider: '))
    else:
        print('You`ve guessed the divider!')


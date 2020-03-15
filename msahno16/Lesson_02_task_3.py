print('Enter the first number')
fizz=int(input())
print('Enter the second number')
buzz=int(input())
print('Enter the third number')
n=int(input())
for i in range(1, n):
    if not i%fizz and not i%buzz:
        print('FB', end = ' ')
    elif not i%fizz:
        print('F', end = ' ')
    elif not i%buzz:
        print('B', end = ' ')
    else:
        print(i, end = ' ')



        

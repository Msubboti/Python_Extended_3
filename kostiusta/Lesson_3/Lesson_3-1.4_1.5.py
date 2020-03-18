nominals=[50,100,200,500,1000]
print('Enter the sum:')
sum=int(input())
while sum:
    for i in nominals:
        if sum/i>=1:
            print(i, '-', sum//i)
            sum=sum%i

nominals=[1000,500,200,100,50]
print('Enter the sum:')
sum=int(input())
while sum:
    for i in nominals:
        if sum/i>=1:
            print(i, '-', sum//i)
            sum=sum%i

nominals=[50,100,200,500,1000]
print('Enter the sum:')
sum=int(input())
while sum:
    for i in nominals:
        if sum/i>=1:
            if sum//i<=10:
                print(i, '-', sum//i)
                sum=sum%i
            else:
                print(i, '- 10')
                sum-=10*i
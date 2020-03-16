#Первый уровень
 
#1.

a = 5
if a % 2 == 0:
    print('even number')
else:
    print('odd number')

#2.

a = 105
if (a % 2 != 0) and (a % 3 == 0) and (a % 5 == 0) and (a % 10 != 0):
    print('число является нечетным, делится на три и на пять одновременно, но не делится на 10')
else:
    print('неподходящее число')

#3.

number=7
for i in range(1, number+1):
    if(number%i==0):
        print(i)

#Второй уровень

#1.
miles = int(input('Enter the distance in miles:' ' '))
print (miles* 1609, 'kilometers')

#3.
f = float(input('Enter degrees fahrenheit °F:' ' '))
print ('Celsius:', round((f - 32) * (5/9)) , '°C')

#2.
age = int(input('Enter your age:' ' '))
if (age < 6):
    print ("Toto, I’ve got a feeling we’re not in Kansas anymore")
elif ((age > 6) and (age <= 18)):
    print ("You can’t handle the truth!")
elif ((age > 18) and (age <= 28)):
    print ("May the Force be with you!")
elif ((age > 28) and (age <= 38)):
    print ("After all, tomorrow is another day!")
elif ((age > 38) and (age <= 45)):
    print ("Great men are not born great, they grow great.")
elif ((age > 45) and (age <= 55)):
    print ("I'm too old for this sh*t")
elif ((age > 55) and (age <= 65)):
    print ("All we have to decide is what to do with the time that is given to us.")
else:
    print ("Get busy livin’, or get busy dyin’.")

#Третий уровень

fizz = int(input('enter fizz' ' '))
buzz = int(input('enter buzz' ' '))
number = int(input('enter number' ' '))
string = ''
for i in range(1, number+1):
  if i%fizz==0 and i%buzz==0:
    i = 'FB'
    i = str(i)
    string += i + ' '
  elif (i%fizz==0):
    i = 'F'
    i = str(i)
    string += i + ' '
  elif (i%buzz==0):
    i = 'B'
    i = str(i)
    string += i + ' '
  elif i%fizz==0 and i%buzz==0:
    i = 'FB'
    i = str(i)
    string += i + ' '
  else:
    i = str(i)
    string += i + ' '
print (string)


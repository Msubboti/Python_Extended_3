# coding: utf-8
#--------------------------- 1 ---------------------------
'''
def porch_and_floor_found(a,b,c):
    tmp = a//(b*c)
    porch = (a-1)//(b*c)+1
    floor = ((a-1)-(porch-1)*(b*c))//b+1
    result = [porch,floor]
    return result

flat_n = int(input('Введите номер квартиры: '))
flats_on_floor = int(input('Введите колличество квартир на этаже: '))
floors_in_building = int(input('Введите колличество этажей в доме: '))

res = porch_and_floor_found(flat_n, flats_on_floor, floors_in_building)
print(f'Квартира находится в {res[0]} подъезде на {res[1]} этаже.')
'''
#--------------------------- 2 ---------------------------
#'''
x = 0
while not x%2:
    x = int(input('Введите целое нечетное число: '))
    if not x%2:print('Вы очень невнимательны! Попробуйте еще раз :)))')
l = []
n = 1
z = False
for i in range(x):
    m = int((x-n)/2)
    l.append(m*' '+ n*'x'+m*' ')
    if n<x and not z:n+=2
    elif n==x:
        z=True
        n-=2
    else:n-=2
for line in l:
    print(line)
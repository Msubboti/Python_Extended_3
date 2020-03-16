# coding: utf-8
#--------------------------- 1 ---------------------------
'''
stud = {'Иванов':[], 'Петров':[], 'Сидоров':[]}

for i in stud:
    stud.update({i:list(map(int,input(f'Введите через пробел оценки для {i}: ').split()))})

stud_mid = {}

for key,val in stud.items():
    mid = round(sum(val)/len(val),2)
    stud_mid.update({key:mid})

for key,val in stud_mid.items():
    if val == max(stud_mid.values()):print(f'Лучший студент {key} со средней оценкой {val}')
    elif val == min(stud_mid.values()):print(f'Худший студент {key} со средней оценкой {val}')
'''
#--------------------------- 2 ---------------------------
'''
stud = {'Иванов':[], 'Петров':[], 'Сидоров':[]}
courses = ('Python', 'FrontEnd', 'FullStack', 'Java')
i = []
for student in stud.keys():
    print(f'В каких группах учится {student} \n(Python - 1, FrontEnd - 2, FullStack - 3, Java - 4)')
    i = list(map(int,input(f'Введите группу(ы) для {student} через пробел: ').split()))
    stud.update({student:i})
print(stud)

z = False
print('Учатся в двух и более группах:')
for student, group in stud.items():
    if len(group)>=2:
        print(student)
        z = True
if not z:print('таких нет.')

def my_chek(a):
    for n_g in a:
        if n_g == 2:
            return False
    return True

print('Cтуденты, которые не учатся на фронтенде:')
#tmp = [student for student, group in stud.items() if my_chek(group)] #---different variant for finding students
#print(tmp)
z = 0
for student, group in stud.items():
    for n_g in group:
        if n_g == 2:
            z = 1
            break
    if not(z):
        print(student)
    z = 0

print('Cтуденты, которые изучают Python или Java:')
z = False
for student, group in stud.items():
    for n_g in group:
        if n_g == 1 or n_g == 4:
            z = True
            break
    if z:
        print(student)
    z = False
'''
#--------------------------- 3 ---------------------------
def my_found(req):
    my_dict = {'XXS':[42, 36, 8, 38, 24], 'XS':(2), 'S':(4), 'M':(6), 'L':(8), 'XL':(10), 'XXL':(12), 'XXXL':(14)}
    if req[0] != 'XXS': answ = my_dict['XXS'][req[1]-1]+my_dict[req[0]]
    else: answ = my_dict['XXS'][req[1]-1]
    return answ

#my_dict = {'XXS':[42, 36, 8, 38, 24], 'XS':[2], 'S':[4], 'M':[6], 'L':[8], 'XL':[10], 'XXL':[12], 'XXXL':[14]}
#for key,val in my_dict.items():
    #if key == 'XS': my_dict.update({key:[val+2 for val in my_dict['XXS']]})
    #elif key == 'S': my_dict.update({key:[val+4 for val in my_dict['XXS']]})
    #elif key == 'M': my_dict.update({key:[val+6 for val in my_dict['XXS']]})
    #elif key == 'L': my_dict.update({key:[val+8 for val in my_dict['XXS']]})
    #elif key == 'XL': my_dict.update({key:[val+10 for val in my_dict['XXS']]})
    #elif key == 'XXL': my_dict.update({key:[val+12 for val in my_dict['XXS']]})
    #elif key == 'XXXL': my_dict.update({key:[val+14 for val in my_dict['XXS']]})

country = {1:'Россия', 2:'Германия', 3:'США', 4:'Франция', 5:'Великобритания'}

print('Программа перевода размеров женского белья из\n'
      'международной системы в системы следующих стран:\n'
      '1 - Россия, 2 - Германия, 3 - США, 4 - Франция, 5 - Великобритания.\n'
      'Справка (международная система): XXS, XS, S, M, L, XL, XXL, XXXL')

req = []
while len(req)<=1:   
    req = list(input('>>> Введите через пробел международный размер и страну,\n'
                'в систему которой перевести данный размер: ').split())
    req[0] = req[0].upper()
    if len(req)<=1: print('Вы таки что-то сделали не так... \nНужно повторить попытку!')
    else:req[1] = int(req[1])

print(f'Выбранный Вами размер "{req[0]}" в системе размеров "{country[req[1]]}" будет: {my_found(req)}')

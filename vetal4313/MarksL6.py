def keyFunc(item):
    return item[1]


students = dict( Roguly = [], Morozova = [], Djafarov = [])
students['Mahmad'] = []
values1 = (9, 10, 6, 10)
values2 = ( 12, 8, 6, 9)
values3 = (6, 10, 8, 12)

marks = tuple(zip(values1, values2,values3))
Students0 = dict(zip(students.keys(), marks))
average = dict()

for student in Students0:
    average[student] = sum(Students0[student]) / len(Students0[student])
    list_d = list(average.items())
    list_d.sort(key=lambda i: i[1], reverse = True)
    for i in list_d:
      
        print(list_d)
    

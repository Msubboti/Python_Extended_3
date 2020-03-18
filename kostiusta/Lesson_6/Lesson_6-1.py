students=dict(Sidorov=[], Petrov=[], Ivanov=[])
students['Sosnov']=[]
marks_1=(8,5,6,7)
marks_2=(10,8,6,7)
marks_3=(8,9,7,9)
all_marks=list(zip(marks_1,marks_2,marks_3))
students_study=dict(zip(students,all_marks))
print(students_study)
average_mark=dict()
for student in students_study:
    average_mark[student]=sum(students_study[student])/len(students_study[student])
final_result=list(average_mark.items())
final_result.sort(key=lambda i: i[1])
mn=final_result[:1]
mx=final_result[-1:]
print ('Отстающий студент -', mn)
print ('Успешный студент -', mx)
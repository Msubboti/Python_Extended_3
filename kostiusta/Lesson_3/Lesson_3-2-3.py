with open(r'F:\Python\Lesson 3\2-3\data_file.txt','r') as f:
    final_res=[]
    for line in f:
        res=(line.split())
        f=int(res[0])  # Fizz number
        b=int(res[1])  # Buzz number
        t=int(res[2])  # Third number
        for i in range(1,t+1):
            if not (i%f) and not (i%b):
                i='FB'
            elif not (i%b):
                i='B'
            elif not (i%f):
                i='F'
            final_res.append(i)
        final_res.append('/n')
file_result_name=str(input('Enter mame for result file:')) #вводим имя для будущего файла с результатом
file_result=open(file_result_name + '.txt', 'w') #создаем файл в который запишем результат
for i in final_res:
    file_result.write(str(i)+' ')
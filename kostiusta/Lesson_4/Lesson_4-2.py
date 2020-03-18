with open(r'F:\Python\Lesson 3\2-3\data_file.txt','r') as f:
    final_res=[]
    r=[]
    for line in f:
        
        res=(line.split())
        f=int(res[0])  # Fizz number
        b=int(res[1])  # Buzz number
        t=int(res[2])  # Third number1
        
        r=['FB' if not (i%f) and not (i%b) else 'B' if not (i%b) else 'F' if not (i%f) else i for i in range(1,t+1)]
        final_res.append(r)
        
file_result_name=str(input('Enter mame for result file:'))
file_result=open(file_result_name + '.txt', 'w')
for i in final_res:
    file_result.write(str(i))
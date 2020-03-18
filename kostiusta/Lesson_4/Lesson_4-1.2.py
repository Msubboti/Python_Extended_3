n=['Коля','Вася','Петя','Иван','Дмитрий']
s=['Иванов','Сидоров','Петров','Карасев','Окунь']
res=[]
import random   
for i in range(0,25):
    ns=random.choice(n) + ' ' + random.choice(s)
    res.append(ns)
print(res)
for i in res:
    print (i+' - '+str(res.count(i)))
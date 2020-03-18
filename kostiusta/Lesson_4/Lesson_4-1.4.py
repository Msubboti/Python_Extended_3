import random
d=[random.randint(1, 1000) for i in range(10)]
t=[random.randint(1, 20) for i in range(10)]
s=[i//x for i,x in zip(d,t)] #List comprehensions
av=sum(s)/len(s)
res=[]
for i in s:
    if i>av:
        res.append(i)
print(d)
print(t)
print(s)    
print(av)
print(res)
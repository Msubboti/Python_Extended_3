#1 задание
a='Ukraine,Russia,England'
b='Welcome to California!'
r=a.split(',')
for i in r:
    f=b[0:11] + i + b[-1:]
    print(f)



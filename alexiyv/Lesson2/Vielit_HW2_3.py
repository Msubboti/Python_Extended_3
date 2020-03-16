
fizz = int(input('Insert first number "fizz": '))
buzz = int(input('Insert second number "buzz": '))
max_nember = int(input('Insert third number: '))
result = str()
for i in range(1, max_nember+1):
    if not (i%fizz) and not (i%buzz): result += 'FB '
    elif not (i%fizz): result += 'F '
    elif not (i%buzz): result += 'B '
    else: result += str(i)+' '
print (result)

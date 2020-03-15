
def dubl2(line, d):
    line1 = line.strip().split()
    for word in line1:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1


d = {}

with open("just_text.txt", 'r', encoding='utf-8') as file:
    line = file.readline()
    if line:
        dubl2(line.strip(), d)
    while line:
        line = file.readline()
        dubl2(line.strip(), d)


for key in d.keys():
    print(f'{key} : {d[key]}')



def dubl2(line, d):
    line1 = line.strip().split()
    for word in line1:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1


# d = {}
#
# with open("just_text.txt", 'r', encoding='utf-8') as file:
#     line = file.readline()
#     if line:
#         dubl2(line.strip(), d)
#     while line:
#         line = file.readline()
#         dubl2(line.strip(), d)
#
#
# for key in d.keys():
#     print(f'{key} : {d[key]}')
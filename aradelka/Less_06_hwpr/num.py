with open('numbers.txt', 'r') as file:
    for line in file:
        line1 = line.split(';')
        # print(line[0], '+', line[1])
        a = line1[0].split()
        b = line1[1].strip().split()
        k = 0
        for i in a:
            k = k + int(i)

        n = k // len(a)
        m = k % len(a)
        #print(n, '+', m)
        if n == int(b[0]) and m == int(b[1]):
            print(line+' True')
        else:
            print(line+' False')

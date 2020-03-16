with open('numbers.txt', 'r') as file:
    for line in file:
        line1 = line.split(';')
        a = line1[0].split()
        b = line1[1].split()
        k = 0
        for i in a:
            k = k + int(i)

        n = k // len(a)
        m = k % len(a)
        if n == int(b[0]) and m == int(b[1]):
            print(f"{' '.join(map(str, a))};{' '.join(map(str, b))} True")
        else:
            print(f"{' '.join(map(str, a))};{' '.join(map(str, b))} False")

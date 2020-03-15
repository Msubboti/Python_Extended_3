with open("triplets.txt", 'r') as file:
    with open("triplets_fb_results.txt", 'w') as f:
        for line in file:
            #print(line, end='')
            line = line.split()

            fizz = int(line[0])
            buzz = int(line[1])
            third = int(line[2])

            l = []

            for i in range(1, third + 1):
                if i % fizz == 0 and i % buzz == 0:
                    l.append('FB')

                elif i % fizz == 0:
                    l.append('F')

                elif i % buzz == 0:
                    l.append('B')

                else:
                    l.append(str(i))
            print(' '.join(l))

            l.append('\n')

            f.write(' '.join(l))


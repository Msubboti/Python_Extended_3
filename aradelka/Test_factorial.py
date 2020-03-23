from factorial import fact

def test(recieved, expected):
    if fact(recieved) == expected:
        return True
    else:
        return False

def sequence():
    print('\tSequense test')
    results = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}

    i = 0
    for j in results.keys():
        if test(results[j], j):
            print('Test', i, 'passed!')
        else:
            print('Test', i, 'failed!')
        i += 1

def boundary():
    print('\tBoundary test')
    results = {1: 1, 7: 5040}

    i = 0
    for j in results.keys():
        if test(results[j], j):
            print('Test', i, 'passed!')
        else:
            print('Test', i, 'failed!')
        i += 1

def mix():
    print('\tMix test')
    results = {5: 120, 10: 3628800, 2: 2, 6: 720}

    i = 0
    for j in results.keys():
        if test(results[j], j):
            print('Test', i+1, 'passed!')
        else:
            print('Test', i, 'failed!')
        i += 1

sequence()
boundary()
mix()
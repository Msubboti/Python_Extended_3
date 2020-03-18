s=input('Enter your text:')

def low (s):
    return s.lower()
print(low(s))

def upp (s):
    return s.upper()
print(upp(s))

m=input('Enter your text:')
x=list(map(low,(m)))
print(x)

n=input('Enter your text:')
x=list(map(upp,(n)))
print(x)
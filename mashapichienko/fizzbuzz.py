def message(str):
    print("Please, input ", str)
def vvod():
    s = int(input())
    return s
def check(a,b):
   if a%b==0:
       return True
   else: return False
def fizzbuzz(fizz,buzz,n):
    l = []
    for i in range(1, n + 1):
        if check(i, fizz) and check(i, buzz):
            l.append("FB")
        elif check(i, fizz):
            l.append("F")
        elif check(i, buzz):
            l.append("B")
        else:
            l.append(i)
    return l
message("'fizz'")
fizz = vvod()
message("'buzz'")
buzz = vvod()
message("third number")
n = vvod()
l=fizzbuzz(fizz,buzz,n)
print(l)
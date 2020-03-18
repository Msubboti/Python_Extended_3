n=int(input('n='))

k=1

while k<=n:
    print(' '*int((n-k)/2)+'*'*k+' '*int((n-k)/2))
    k+=2

j=1

while(n-2*j)>=1:
    print(' '*j+'*'*(n-2*j)+' '*(j))
    j+=1
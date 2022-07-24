def prime(i):
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return 0
    return 1
n=int(input())
a=[]
for i in range(2,n+1):
    if(i==2):
        a.append(i)
    else:
        if(prime(i)):
            a.append(i)
c=0
b=[]
for i in a:
    if(n%i==0):
        c+=1
        b.append(i)
if(c==2):
    print(*b)
else:
    print('-1')

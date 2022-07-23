def fact(s):
    c=1
    for i in range(2,s//2+1):
        if(s%i==0):
            c+=i
    return c
m=int(input())
n=int(input())
r1=fact(m)
r2=fact(n)
if(r1==n and r2==m):
    print('Amicable')
else:
    print('Not Amicable')
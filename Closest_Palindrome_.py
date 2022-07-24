def rev(s):
    d=s
    k=0
    while(s>0):
        r=s%10
        k=r+k*10
        s=s//10
    if(k==d):
        return 1
    else:
        return 0
n=int(input())
d=n
i=n
while(1):
    i=i-1
    if(rev(i)):
        m1=i
        break
i=d
while(1):
    i=i+1
    if(rev(i)):
        m2=i
        break
r1=d-m1
r2=m2-d
if(r1<r2):
    print(m1)
elif(r2<r1):
    print(m2)
else:
    print(m1,m2)
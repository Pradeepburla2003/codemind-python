n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if(i%2==1):
        b.append(i)
    else:
        c.append(i)
d=max(len(b),len(c))
for i in range(d):
    if(i<len(b)):
        print(b[i],end=" ")
    if(i<len(c)):
        print(c[i],end=" ")
if(n%2==1):
    print('0')
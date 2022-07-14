n=int(input())
a=list(map(int,input().split()))
d=[]
c=[]
for i in range(n):
    if(i%2==0):
        c.append(a[i])
    else:
        d.append(a[i])
e=[]
for i in range(len(c)):
    for j in range(c[i]):
        e.append(d[i])
print(*e)
x=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
c=[]
d=0
for i in a:
    if(i>=m and i<=n):
        c.append(i)
        d=1
if(d==0):
    print('-1')
else:
    print(min(c))
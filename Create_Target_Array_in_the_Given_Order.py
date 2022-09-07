a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
f=[]
for i in range(a):
    t=d[i]
    f.insert(t,b[i])
print(*f)
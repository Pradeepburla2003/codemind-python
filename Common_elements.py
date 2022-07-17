a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
f=[]
for i in c:
    if i in d and i not in f:
        f.append(i)
print(*f)
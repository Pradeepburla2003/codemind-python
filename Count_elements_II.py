a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
f=[]
for i in c:
    if i not in d and i not in f:
        f.append(i)
for i in d:
    if i not in c and i not in f:
        f.append(i)
print(len(f))
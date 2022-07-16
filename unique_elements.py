n=int(input())
a=list(map(int,input().split()))
b=[]
c=list(set(a))
for i in a:
    if i in c and i not in b:
        b.append(i)
print(*b)
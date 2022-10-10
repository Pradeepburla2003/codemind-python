n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if(a.count(i)==1):
        b.append(i)
k=sorted(b)
print(*k)
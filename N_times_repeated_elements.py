n=int(input())
a=list(map(int,input().split()))
c=int(input())
b=[]
d=0
for i in a:
    if(a.count(i)==c and i not in b):
        b.append(i)
        d=1
if(d==0):
    print('-1')
else:
    print(*b)
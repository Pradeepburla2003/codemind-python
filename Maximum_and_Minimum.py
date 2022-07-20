n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if(a.count(i)==i):
        c=1
        b.append(i)
if(c==1):
    print(min(b),max(b))
else:
    print('-1')